"""Mutation tests: completeness and evidence consistency, never quality scoring."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/mobbin-design-director/scripts/coverage.py'
spec = importlib.util.spec_from_file_location('task_coverage', SCRIPT)
coverage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(coverage)


def fixture(root):
    (root / 'references/sources').mkdir(parents=True)
    (root / 'references/goals.md').write_text('# Operational module\n')
    records = []
    headings = []
    for ident, title, tags, domains, platforms in [
        ('AF-01', 'Define the outcome', ['core'], ['goals'], ['ios', 'web']),
        ('AF-02', 'Assist meaningful input', ['input'], ['content'], ['web']),
    ]:
        heading = f'{ident} — {title}'
        headings.append('### ' + heading)
        records.append(dict(id=ident, title=title, source=dict(path='references/sources/book.md', heading=heading),
                            kind='heuristic', domains=domains, tags=tags, platforms=platforms,
                            stages=['design', 'verify'], triggers=['Starting a task'], exceptions='Context matters.',
                            verification=dict(methods=['inspection', 'runtime'], question='Does the outcome remain clear?'),
                            related=[], routes=['references/goals.md']))
    (root / 'references/sources/book.md').write_text('\n\n'.join(headings))
    (root / 'references/principles.json').write_text(json.dumps(dict(schema_version=1, principles=records)))
    return records


class CoverageTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.principles = fixture(self.root)
        self.path = self.root / 'packet.json'
        self.brief = dict(summary='Make account setup understandable', platform='web', depth='screen', mode='build', tags=[])
        self.packet = coverage.init_packet(self.brief, self.root, self.principles)

    def errors(self, packet=None, require_verified=False):
        return coverage.check_packet(packet or self.packet, self.path, self.root, self.principles, require_verified)[0]

    def evidence(self, name='observed.md'):
        path = self.root / name
        path.write_text('Observed the entire setup flow and recorded results.\n')
        return dict(path=name, observation='The confirmation names the saved account and offers a return action.',
                    sha256=hashlib.sha256(path.read_bytes()).hexdigest())

    def verified(self):
        packet = copy.deepcopy(self.packet)
        row = packet['guidance'][0]
        row.update(disposition='applied', criterion='Completion identifies the account that was saved.')
        row['verification'].update(status='pass', method='runtime', evidence=[self.evidence()])
        for domain in packet['domains']:
            domain.update(status='not_applicable', reason='Outside the scoped account confirmation change.')
            if domain['domain'] == 'goals':
                domain.update(status='applicable', principle_ids=['AF-01'])
        artifact = self.evidence('implementation.txt')
        packet['artifacts'] = [{key: artifact[key] for key in ('path', 'sha256')}]
        packet['claimed_status'] = 'verified_for_scope'
        return packet

    def test_registry_inventory_heading_routes_and_context(self):
        self.assertEqual(coverage.validate_registry(self.root)[0], [])
        mutations = [
            lambda d: d['principles'].pop(),
            lambda d: d['principles'].append(copy.deepcopy(d['principles'][0])),
            lambda d: d['principles'][0]['source'].update(heading='AF-01 — Wrong title'),
            lambda d: d['principles'][0].update(routes=['references/missing.md']),
            lambda d: d['principles'][0].update(routes=['references/sources/book.md']),
            lambda d: d['principles'][0].update(kind='requirement'),
            lambda d: d['principles'][0].update(related=['AF-01']),
            lambda d: d['principles'][0].update(domains=['unsupported']),
        ]
        registry = self.root / 'references/principles.json'
        original = registry.read_text()
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                data = json.loads(original); mutation(data); registry.write_text(json.dumps(data))
                self.assertTrue(coverage.validate_registry(self.root)[0])
        registry.write_text(original)
        with (self.root / 'references/sources/book.md').open('a') as output:
            output.write('\n## ZZ-01 — Orphan heading\n')
        self.assertTrue(any('ZZ-01' in e for e in coverage.validate_registry(self.root)[0]))

    def test_candidates_routing_and_no_silent_deletion(self):
        self.assertEqual([r['id'] for r in self.packet['guidance']], ['AF-01'])
        self.assertEqual(self.errors(), [])
        self.packet['guidance'] = []
        self.assertTrue(any('missing routed candidate' in e for e in self.errors()))
        web = coverage.init_packet(dict(self.brief, tags=['input']), self.root, self.principles)
        ios = coverage.init_packet(dict(self.brief, tags=['input'], platform='ios'), self.root, self.principles)
        self.assertEqual(len(web['guidance']), 2)
        self.assertEqual(len(ios['guidance']), 1)

    def test_honest_research_partial_and_routine(self):
        self.packet['brief']['mode'] = 'research'
        self.assertEqual(self.errors(), [])
        self.assertTrue(self.errors(require_verified=True))
        routine = coverage.init_packet(dict(self.brief, depth='routine', tags=['input']), self.root, self.principles)
        self.assertEqual(routine['guidance'], [])
        self.assertEqual(routine['domains'], [])
        self.assertEqual(self.errors(routine), [])

    def test_invalid_brief_and_stale_registry(self):
        for field, value in [('platform', 'android'), ('mode', 'publish'), ('tags', ['bogus']), ('tags', None), ('summary', 'TODO')]:
            with self.subTest(field=field, value=value):
                with self.assertRaises(ValueError):
                    coverage.init_packet(dict(self.brief, **{field: value}), self.root, self.principles)
        registry = self.root / 'references/principles.json'
        registry.write_text(registry.read_text() + '\n')
        self.assertTrue(any('stale' in e for e in self.errors()))

    def test_fake_pass_and_missing_evidence(self):
        row = self.packet['guidance'][0]
        row['disposition'] = 'applied'
        row['verification']['status'] = 'pass'
        self.assertTrue(any('criterion' in e for e in self.errors()))
        self.assertTrue(any('evidence' in e for e in self.errors()))
        row['criterion'] = 'The saved account is identified on completion.'
        row['verification']['evidence'] = [self.evidence()]
        self.assertEqual(self.errors(), [])
        for mutation in [lambda e: e.update(path='absent.txt'), lambda e: e.update(path='references'),
                         lambda e: e.update(path='https://example.org'), lambda e: e.update(observation='TBD'), lambda e: e.update(observation='TODO: inspect this'),
                         lambda e: e.pop('sha256')]:
            packet = copy.deepcopy(self.packet)
            mutation(packet['guidance'][0]['verification']['evidence'][0])
            self.assertTrue(self.errors(packet))

    def test_verified_departure_failure_and_binding_requirement(self):
        packet = self.verified()
        self.assertEqual(self.errors(packet, True), [])
        row = packet['guidance'][0]
        row.update(disposition='departed', reason='The limited confirmation task needs only the saved account identity.')
        self.assertEqual(self.errors(packet, True), [])
        packet['requirements'] = [dict(copy.deepcopy(row), id='REQ-1', kind='requirement', origin='User brief')]
        self.assertTrue(any('binding requirement departed' in e for e in self.errors(packet)))
        packet['requirements'][0]['kind'] = 'preference'
        next(d for d in packet['domains'] if d['domain'] == 'goals')['requirement_ids'] = ['REQ-1']
        self.assertEqual(self.errors(packet), [])
        row['verification']['status'] = 'fail'
        self.assertTrue(any('verification failed' in e for e in self.errors(packet)))
        packet['claimed_status'] = 'partial'
        self.assertEqual(self.errors(packet), [])

    def test_nonroutine_verification_cannot_be_vacuous(self):
        packet = self.verified()
        for row in packet['guidance']:
            row.update(disposition='not_applicable', reason='Outside the narrowly defined scope.')
            row['verification'] = coverage.new_verification()
        for domain in packet['domains']:
            domain.update(status='not_applicable', reason='Outside the narrowly defined scope.', principle_ids=[])
        self.assertTrue(any('passing criterion' in e for e in self.errors(packet)))
        packet['claimed_status'] = 'partial'
        self.assertEqual(self.errors(packet), [])
        routine = coverage.init_packet(dict(self.brief, depth='routine'), self.root, self.principles)
        routine['claimed_status'] = 'verified_for_scope'
        self.assertEqual(self.errors(routine), [])

    def test_verified_active_criteria_need_area_links(self):
        packet = self.verified()
        for domain in packet['domains']:
            domain.update(status='not_applicable', reason='Claimed outside the task.', principle_ids=[], requirement_ids=[])
        self.assertTrue(any('active criterion needs an applicable domain' in e for e in self.errors(packet, True)))
        packet['claimed_status'] = 'partial'
        self.assertEqual(self.errors(packet), [])

    def test_hashes_detect_changed_evidence_and_implementation(self):
        packet = self.verified()
        (self.root / 'observed.md').write_text('Changed observation.')
        self.assertTrue(any('stale sha256' in e for e in self.errors(packet)))
        packet = self.verified()
        (self.root / 'implementation.txt').write_text('Changed implementation.')
        self.assertTrue(any('stale sha256' in e for e in self.errors(packet)))
        packet['claimed_status'] = 'partial'
        self.assertTrue(any('stale sha256' in e for e in self.errors(packet)))

    def test_artifacts_self_reference_and_independent_review(self):
        packet = self.verified()
        packet['artifacts'] = []
        self.assertTrue(any('artifacts' in e for e in self.errors(packet)))
        packet['brief']['mode'] = 'design'
        self.assertTrue(any('artifacts' in e for e in self.errors(packet)))
        packet['brief']['mode'] = 'research'
        self.assertEqual(self.errors(packet), [])
        packet['review']['status'] = 'pending'
        self.assertTrue(any('review pending' in e for e in self.errors(packet)))
        packet['review'].update(status='completed', evidence=[])
        self.assertTrue(any('review' in e for e in self.errors(packet)))
        packet['review']['evidence'] = [self.evidence('review.md')]
        self.assertEqual(self.errors(packet), [])
        self.path.write_text('{}')
        packet['review']['evidence'] = [dict(path='packet.json', observation='Self assertion.', sha256=hashlib.sha256(b'{}').hexdigest())]
        self.assertTrue(any('own evidence' in e for e in self.errors(packet)))

    def test_domains_and_placeholder_reasons(self):
        packet = self.verified()
        packet['domains'].pop()
        self.assertTrue(any('missing domain' in e for e in self.errors(packet)))
        packet = self.verified()
        packet['domains'][0].update(status='not_applicable', reason='   ')
        self.assertTrue(any('needs a reason' in e for e in self.errors(packet)))
        packet['domains'][0].update(status='applicable', principle_ids=['AF-01'])
        self.assertTrue(any('does not cover' in e for e in self.errors(packet)))

    def test_not_applicable_domain_cannot_reference_active_records(self):
        for disposition in ('applied', 'departed', 'deferred', 'unresolved'):
            with self.subTest(disposition=disposition):
                packet = self.verified()
                packet['guidance'][0].update(disposition=disposition, reason='A scoped contextual decision.')
                domain = next(d for d in packet['domains'] if d['domain'] == 'goals')
                domain.update(status='not_applicable', reason='Outside this task.')
                self.assertTrue(any('not_applicable contradicts' in e for e in self.errors(packet, True)))
        packet = self.verified()
        packet['claimed_status'] = 'partial'
        packet['guidance'][0].update(disposition='not_applicable', reason='Outside this task.')
        domain = next(d for d in packet['domains'] if d['domain'] == 'goals')
        domain.update(status='not_applicable', reason='Outside this task.')
        self.assertEqual(self.errors(packet), [])
        packet['requirements'] = [dict(copy.deepcopy(packet['guidance'][0]), id='REQ-1',
                                       kind='requirement', origin='User brief', disposition='applied')]
        domain['requirement_ids'] = ['REQ-1']
        self.assertTrue(any('not_applicable contradicts' in e for e in self.errors(packet)))

    def test_malformed_nested_values_report_diagnostics(self):
        for change in [lambda p: p['guidance'][0].update(disposition=[]),
                       lambda p: p['guidance'][0]['verification'].update(status={}),
                       lambda p: p['domains'][0].update(principle_ids=[{}]),
                       lambda p: p.update(requirements=[None]), lambda p: p.update(review=[])]:
            packet = copy.deepcopy(self.packet); change(packet)
            self.assertTrue(self.errors(packet))

    def test_cli_refuses_overwrite_and_reports_partial(self):
        brief = self.root / 'brief.json'; brief.write_text(json.dumps(self.brief))
        command = [sys.executable, str(SCRIPT), '--root', str(self.root)]
        result = subprocess.run(command + ['init', '--brief', str(brief), '--out', str(self.path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        original = self.path.read_bytes()
        result = subprocess.run(command + ['init', '--brief', str(brief), '--out', str(self.path)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.path.read_bytes(), original)
        result = subprocess.run(command + ['check', str(self.path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('record consistent; partial; no claim of quality/usability verified', result.stdout)
        result = subprocess.run(command + ['hash', str(brief)], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), hashlib.sha256(brief.read_bytes()).hexdigest())
        result = subprocess.run(command + ['check', str(self.path), '--require-verified'], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)

    def test_search_is_bounded_and_relevant(self):
        self.assertEqual([p['id'] for p in coverage.search(self.principles, ['input'])], ['AF-02'])
        self.assertEqual(coverage.search(self.principles, ['xyzzy']), [])

    def test_show_reads_only_requested_cards_and_rejects_unknown(self):
        doc = self.root / 'references/sources/book.md'
        doc.write_text('### AF-01 — Define the outcome\nSpecific rationale and source.\n\n### AF-02 — Assist meaningful input\nUnrelated second card.\n')
        result = coverage.show_cards(self.root, self.principles, ['AF-01'])
        self.assertIn('Specific rationale and source.', result)
        self.assertNotIn('Unrelated second card.', result)
        self.assertNotIn('AF-02', result)
        with self.assertRaises(ValueError):
            coverage.show_cards(self.root, self.principles, ['ZZ-01'])

    def test_real_flow_and_touch_routing_regressions(self):
        root = SCRIPT.parents[1]
        errors, records = coverage.validate_registry(root)
        self.assertEqual(errors, [])
        for tags in [['onboarding', 'permissions', 'interruption', 'input'], ['comparison', 'selection', 'input']]:
            brief = dict(self.brief, platform='ios', depth='journey', tags=tags)
            self.assertIn('UX-10', {r['id'] for r in coverage.candidates(brief, records)})
            self.assertEqual(coverage.candidates(dict(brief, depth='routine'), records), [])
        touch = dict(self.brief, platform='ios', depth='screen', tags=['touch'])
        ids = {r['id'] for r in coverage.candidates(touch, records)}
        self.assertTrue({'TD-03','TD-05','TD-11','TD-16','TD-19','TD-20'} <= ids)
        card = coverage.show_cards(root, records, ['TD-16'])
        self.assertIn('PDF 180–190', card)
        self.assertIn('Exceptions', card)
        self.assertNotIn('TD-17 —', card)

    def test_shipped_registry(self):
        root = SCRIPT.parents[1]
        if not (root / 'references/principles.json').exists():
            self.skipTest('Registry authoring in progress')
        errors, records = coverage.validate_registry(root)
        self.assertEqual(errors, [])
        self.assertEqual(len(records), 184)

    def test_new_sources_selective_retrieval_and_routine_boundary(self):
        root = SCRIPT.parents[1]
        errors, records = coverage.validate_registry(root)
        self.assertEqual(errors, [])
        selected = coverage.show_cards(root, records, ['ID-06', 'PU-09'])
        self.assertIn('ID-06 —', selected)
        self.assertIn('PU-09 —', selected)
        self.assertNotIn('ID-07 —', selected)
        self.assertNotIn('PU-10 —', selected)
        # Adding two books must not turn a routine approved edit into a full ledger.
        brief = dict(self.brief, platform='ios', depth='routine', tags=['visual', 'evaluation'])
        self.assertEqual(coverage.candidates(brief, records), [])
        new = [r for r in records if r['id'].startswith(('ID-', 'PU-'))]
        self.assertTrue(new)
        self.assertFalse(any('core' in r['tags'] for r in new))
        for query, expected in [('hierarchy', 'PU-09'), ('APCA', 'PU-04'),
                                ('placeholder', 'PU-22'), ('Dynamic Type', 'PU-11')]:
            self.assertIn(expected, {r['id'] for r in coverage.search(records, [query])})


if __name__ == '__main__':
    unittest.main()
