import importlib.util
import io
from contextlib import redirect_stderr, redirect_stdout
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'skills/mobbin-design-director/scripts'


def module(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / (name + '.py'))
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


cache = module('mobbin_cache')

RESULTS = {
    'query': 'onboarding paywall',
    'screens': [
        {'id': 'scr-1', 'image_url': 'https://cdn.example.test/scr-1.webp?token=abc',
         'mobbin_url': 'https://mobbin.com/screens/scr-1', 'app_name': 'Apple Store',
         'platform': 'ios'},
    ],
    'flows': [
        {'app_name': 'Calm', 'platform': 'ios', 'mobbin_url': 'https://mobbin.com/flows/flow-9',
         'screens': [
             {'screen_id': 'scr-2', 'image_url': 'https://cdn.example.test/scr-2.png', 'position': 1},
         ]},
    ],
}


def fake_urlopen(request, timeout=None):
    return io.BytesIO(b'image-bytes:' + request.full_url.encode())


def run(argv):
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        code = cache.main(argv)
    return code, out.getvalue(), err.getvalue()


class MobbinCacheTests(unittest.TestCase):
    def test_downloads_both_shapes_and_writes_sidecars(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            results = root / 'results.json'
            results.write_text(json.dumps(RESULTS))
            out_dir = root / 'cache'
            with mock.patch.object(cache.urllib.request, 'urlopen', side_effect=fake_urlopen) as opened:
                code, text, _ = run([str(results), str(out_dir)])
                self.assertEqual(code, 0, text)
                self.assertEqual(opened.call_count, 2)
            self.assertTrue((out_dir / 'scr-1.webp').read_bytes().startswith(b'image-bytes:'))
            self.assertTrue((out_dir / 'scr-2.png').exists())
            sidecar = json.loads((out_dir / 'scr-1.json').read_text())
            self.assertEqual(sidecar['mobbin_url'], 'https://mobbin.com/screens/scr-1')
            self.assertEqual(sidecar['app_name'], 'Apple Store')
            self.assertEqual(sidecar['platform'], 'ios')
            self.assertEqual(sidecar['source_query'], 'onboarding paywall')
            self.assertIn('+00:00', sidecar['fetched_at'])
            inherited = json.loads((out_dir / 'scr-2.json').read_text())
            self.assertEqual(inherited['app_name'], 'Calm')
            self.assertEqual(inherited['mobbin_url'], 'https://mobbin.com/flows/flow-9')
            self.assertIn('fetched 2, skipped 0', text)
            # A second run skips every existing image and touches the network for none.
            with mock.patch.object(cache.urllib.request, 'urlopen', side_effect=fake_urlopen) as opened:
                code, text, _ = run([str(results), str(out_dir), '--query', 'other'])
                self.assertEqual(code, 0)
                self.assertEqual(opened.call_count, 0)
            self.assertIn('fetched 0, skipped 2', text)
            self.assertEqual(json.loads((out_dir / 'scr-1.json').read_text())['source_query'],
                             'onboarding paywall')

    def test_dry_run_prints_the_plan_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            results = root / 'results.json'
            results.write_text(json.dumps(RESULTS))
            out_dir = root / 'cache'
            with mock.patch.object(cache.urllib.request, 'urlopen', side_effect=fake_urlopen) as opened:
                code, text, _ = run([str(results), str(out_dir), '--dry-run'])
                self.assertEqual(code, 0)
                self.assertEqual(opened.call_count, 0)
            self.assertIn('DRY RUN: 2 screens', text)
            self.assertIn('would fetch https://cdn.example.test/scr-2.png', text)
            self.assertFalse(out_dir.exists())

    def test_refuses_an_output_dir_inside_a_git_repo(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            results = root / 'results.json'
            results.write_text(json.dumps(RESULTS))
            repo = root / 'repo'
            (repo / 'nested').mkdir(parents=True)
            (repo / '.git').write_text('gitdir: elsewhere\n')  # a worktree keeps .git as a file
            with mock.patch.object(cache.urllib.request, 'urlopen', side_effect=fake_urlopen) as opened:
                code, _, err = run([str(results), str(repo / 'nested/cache'), '--dry-run'])
                self.assertEqual(opened.call_count, 0)
            self.assertEqual(code, 2)
            self.assertIn('inside a git repository', err)
            self.assertFalse((repo / 'nested/cache').exists())
            self.assertTrue(cache.inside_git_repo(repo / 'nested'))
            self.assertFalse(cache.inside_git_repo(root / 'elsewhere'))


if __name__ == '__main__':
    unittest.main()
