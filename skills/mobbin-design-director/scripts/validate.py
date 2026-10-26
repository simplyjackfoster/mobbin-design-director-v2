#!/usr/bin/env python3
"""Validate package links, provenance/coverage structure, and metadata (stdlib).

This checks recorded evidence, not whether a human/agent truly read a page.
Use --allow-partial while building; release validation rejects incomplete study.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import re
import sys

EXPECTED = {'ux-book': 33, 'about-face': 21, 'designing-interfaces': 12,
            'mind-in-mind': 14, 'inspection-methods': 6, 'touch-design': 13,
            'interaction-design': 16, 'practical-ui': 8}


def validate(root, allow_partial=False):
    errors, partial = [], []
    entry = (root / 'SKILL.md').read_text()
    if not entry.startswith('---\n'):
        errors.append('SKILL.md has no YAML frontmatter')
    front = entry.split('---', 2)[1]
    for field in ('name', 'description'):
        if not re.search(r'^' + field + r':\s*\S', front, re.M):
            errors.append('Missing frontmatter ' + field)
    for doc in root.rglob('*.md'):
        # Inline links only; placeholders, URLs, and heading fragments are not files.
        for target in re.findall(r'\]\(([^)]+)\)', doc.read_text()):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            target = target.split('#', 1)[0].strip('<>')
            if '<' in target or not target:
                continue
            if not (doc.parent / target).exists():
                errors.append(f'{doc.relative_to(root)}: broken link {target}')
    for source, count in EXPECTED.items():
        path = root / 'references/sources' / (source + '-coverage.json')
        if not path.exists():
            errors.append('Missing ' + path.name)
            continue
        try:
            data = json.loads(path.read_text())
            required = ('source_id', 'title', 'authors', 'edition', 'year', 'pdf_pages',
                        'sha256', 'extraction_notes', 'chapters', 'figure_checks')
            if any(k not in data for k in required):
                raise ValueError('missing source metadata')
            if data['source_id'] != source or not re.fullmatch('[a-f0-9]{64}', data['sha256']):
                raise ValueError('invalid identity/hash')
            if len(data['chapters']) != count:
                raise ValueError(f'expected {count} chapters')
            previous_end = 0
            for expected_number, ch in enumerate(data['chapters'], 1):
                lo, hi = ch['pdf_start'], ch['pdf_end']
                if ch['number'] != expected_number or not (previous_end < lo <= hi <= data['pdf_pages']):
                    raise ValueError('invalid chapter order or range')
                previous_end = hi
                accounted = set()
                for start, end in ch['read_pdf_ranges']:
                    if not lo <= start <= end <= hi:
                        raise ValueError(f'chapter {expected_number}: read range out of bounds')
                    accounted.update(range(start, end + 1))
                for excluded in ch['excluded_pdf_ranges']:
                    start, end = excluded['start'], excluded['end']
                    if not excluded.get('reason') or not lo <= start <= end <= hi:
                        raise ValueError(f'chapter {expected_number}: invalid exclusion')
                    accounted.update(range(start, end + 1))
                disposition = ch['disposition']
                if disposition not in ('full-study', 'assessed-excluded', 'partial-study'):
                    raise ValueError('unknown disposition ' + disposition)
                missing = set(range(lo, hi + 1)) - accounted
                if disposition == 'partial-study':
                    partial.append(f'{source} chapter {expected_number}')
                elif missing:
                    raise ValueError(f'chapter {expected_number}: {len(missing)} unaccounted pages')
                if disposition == 'assessed-excluded' and not ch.get('notes'):
                    raise ValueError('exclusion needs chapter rationale')
            for figure in data['figure_checks']:
                if not 1 <= figure['pdf_page'] <= data['pdf_pages'] or not figure['inspection']:
                    raise ValueError('invalid figure inspection')
            dossier = path.with_name(source + '.md').read_text()
            for figure in data['figure_checks']:
                for principle in figure['principle_ids']:
                    if principle not in dossier:
                        raise ValueError('figure references absent principle ' + principle)
        except (ValueError, KeyError, TypeError, OSError) as exc:
            errors.append(f'{path.name}: {exc}')
    if partial and not allow_partial:
        errors.append('Incomplete study: ' + ', '.join(partial))
    ui = (root / 'agents/openai.yaml').read_text()
    if '$mobbin-design-director' not in ui:
        errors.append('Codex prompt does not name the skill')
    spec = importlib.util.spec_from_file_location('design_coverage', Path(__file__).with_name('coverage.py'))
    coverage = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(coverage)
    registry_errors, _ = coverage.validate_registry(root)
    errors.extend(registry_errors)
    # One version everywhere. plugin.json is the source; marketplace.json must
    # match. sync_local.py reads plugin.json at run time, so it needs no check.
    repo = root.parent.parent
    plugin = repo / '.claude-plugin/plugin.json'
    market = repo / '.claude-plugin/marketplace.json'
    if plugin.exists() and market.exists():
        pv = json.loads(plugin.read_text()).get('version')
        mv = [p.get('version') for p in json.loads(market.read_text()).get('plugins', [])]
        if any(v != pv for v in mv):
            errors.append(f'version drift: plugin.json {pv} vs marketplace.json {mv}')
    # The one-line index must ship with the full registry. Test fixtures carry
    # a small registry and no index, so the check applies to the real tree only.
    registry = root / 'references/principles.json'
    index = root / 'references/principles-index.md'
    if registry.exists() and not index.exists():
        count = len(json.loads(registry.read_text()).get('principles', []))
        if count >= 100:
            errors.append('references/principles-index.md missing; run scripts/principles_index.py')
    return errors, partial


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--allow-partial', action='store_true')
    args = parser.parse_args()
    errors, partial = validate(args.root.resolve(), args.allow_partial)
    for error in errors:
        print('ERROR:', error)
    print(f'{len(errors)} errors; {len(partial)} partial chapters; recorded coverage only, not behavioral proof')
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
