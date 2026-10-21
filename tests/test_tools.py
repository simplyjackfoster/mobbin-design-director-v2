import base64
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'skills/mobbin-design-director/scripts'


def module(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / (name + '.py'))
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


sheet, validator, sync = module('sheet'), module('validate'), module('sync_local')


def fixture(root):
    (root / 'agents').mkdir(parents=True)
    (root / 'references/sources').mkdir(parents=True)
    (root / 'scripts').mkdir()
    (root / 'SKILL.md').write_text('---\nname: mobbin-design-director\ndescription: Test fixture\n---\n')
    (root / 'agents/openai.yaml').write_text('default_prompt: "$mobbin-design-director"\n')
    for source, count in validator.EXPECTED.items():
        data = dict(source_id=source, title='Fixture', authors=['Test'], edition='1',
                    year=2026, pdf_pages=count, sha256='0' * 64, extraction_notes=[],
                    figure_checks=[], chapters=[])
        for n in range(1, count + 1):
            data['chapters'].append(dict(number=n, title='Fixture', pdf_start=n,
                pdf_end=n, printed_start=n, printed_end=n, disposition='full-study',
                read_pdf_ranges=[[n, n]], excluded_pdf_ranges=[], notes='Fixture'))
        (root / 'references/sources' / (source + '-coverage.json')).write_text(json.dumps(data))
        (root / 'references/sources' / (source + '.md')).write_text('Fixture\n')
    heading = 'AF-01 — Define the task outcome'
    (root / 'references/sources/about-face.md').write_text('### ' + heading + '\n')
    (root / 'references/goals.md').write_text('# Goals\n')
    record = dict(id='AF-01', title='Define the task outcome',
                  source=dict(path='references/sources/about-face.md', heading=heading),
                  kind='heuristic', domains=['goals'], tags=['core'], platforms=['ios','web'],
                  stages=['frame'], triggers=['Starting a task'], exceptions='Adapt to the task.',
                  verification=dict(methods=['inspection'], question='Is the outcome clear?'),
                  related=[], routes=['references/goals.md'])
    (root / 'references/principles.json').write_text(json.dumps(dict(schema_version=1, principles=[record])))
    for name in ('validate.py', 'coverage.py'):
        shutil.copy2(SCRIPTS / name, root / 'scripts' / name)


class ToolTests(unittest.TestCase):
    def test_sheet_is_portable_and_escapes_text(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            png = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Y9ZlZAAAAAASUVORK5CYII=')
            (root / 'image.png').write_bytes(png)
            result = sheet.build({'title': '<title>', 'rows': [{'items': [{'img': 'image.png', 'name': '<img>', 'url': 'https://example.test/?a=1&b=2'}]}]}, root)
            self.assertIn('data:image/png;base64,', result)
            self.assertNotIn('file://', result)
            self.assertIn('&lt;title&gt;', result)
            self.assertIn('a=1&amp;b=2', result)
            with self.assertRaises(ValueError):
                sheet.build({'width': 0}, root)
            with self.assertRaises(FileNotFoundError):
                sheet.build({'rows': [{'items': [{'img': 'missing.png'}]}]}, root)
            with self.assertRaises(ValueError):
                sheet.build({'rows': [{'items': [{'img': 'image.png', 'url': 'javascript:alert(1)'}]}]}, root)

    def test_validation_catches_false_complete_and_bad_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); fixture(root)
            self.assertEqual(validator.validate(root)[0], [])
            p = root / 'references/sources/about-face-coverage.json'
            data = json.loads(p.read_text()); data['chapters'][0]['read_pdf_ranges'] = []
            p.write_text(json.dumps(data))
            self.assertTrue(any('unaccounted' in e for e in validator.validate(root)[0]))
            data['chapters'][0]['disposition'] = 'partial-study'; p.write_text(json.dumps(data))
            self.assertTrue(any('Incomplete' in e for e in validator.validate(root)[0]))
            self.assertEqual(validator.validate(root, allow_partial=True)[0], [])
            (root / 'bad.md').write_text('[missing](missing.md)')
            self.assertTrue(any('broken link' in e for e in validator.validate(root, True)[0]))

    def test_package_validation_rejects_registry_omission(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); fixture(root)
            dossier = root / 'references/sources/about-face.md'
            dossier.write_text(dossier.read_text() + '\n### AF-02 — Missing from registry\n')
            self.assertTrue(any('AF-02: missing registry entry' in e for e in validator.validate(root)[0]))

    def test_sync_dry_run_backup_and_content_hash(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); src = root / 'source'; fixture(src)
            dst = root / 'installed'; dst.mkdir(); (dst / 'local-note').write_text('preserve me')
            backup = root / 'backups'
            command = [sys.executable, str(SCRIPTS / 'sync_local.py'), str(dst), '--source', str(src)]
            p = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertTrue((dst / 'local-note').exists())
            p = subprocess.run(command + ['--apply', '--backup-dir', str(backup)], capture_output=True, text=True)
            self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
            self.assertEqual(next(backup.glob('*/local-note')).read_text(), 'preserve me')
            self.assertEqual(sync.digest_tree(src), sync.digest_tree(dst))
            self.assertIn(sync.digest_tree(src), (dst / 'SOURCE').read_text())
            # Failed validation must leave the installed version intact.
            before = sync.digest_tree(dst)
            (src / 'bad.md').write_text('[missing](missing.md)')
            p = subprocess.run(command + ['--apply', '--backup-dir', str(backup)], capture_output=True, text=True)
            self.assertNotEqual(p.returncode, 0)
            self.assertEqual(sync.digest_tree(dst), before)

    def test_sync_refuses_symlink_destination(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); src = root / 'source'; fixture(src)
            target = root / 'target'; target.mkdir()
            link = root / 'link'; link.symlink_to(target)
            p = subprocess.run([sys.executable, str(SCRIPTS / 'sync_local.py'), str(link), '--source', str(src)], capture_output=True, text=True)
            self.assertNotEqual(p.returncode, 0)
            self.assertTrue(link.is_symlink())


if __name__ == '__main__':
    unittest.main()
