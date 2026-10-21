#!/usr/bin/env python3
"""Route contextual design principles and check recorded task evidence (stdlib).

A successful check establishes record completeness, never usability or beauty.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

DOMAINS = set('goals flows cognition content visual accessibility recovery platform research evaluation'.split())
TAGS = set('core onboarding navigation selection comparison input persistence interruption permissions errors latency content visual motion accessibility localization data expert discovery evaluation implementation touch'.split())
PLATFORMS = {'ios', 'web'}
STAGES = {'frame', 'research', 'design', 'build', 'verify'}
METHODS = {'source', 'runtime', 'visual', 'participant', 'inspection'}
HEADING = re.compile(r'^#{2,3} (([A-Z]+-\d{2}) [—–-] (.+?))\s*$', re.M)


def meaningful(value):
    """Reject empty and conventional placeholder values, without judging prose."""
    return (isinstance(value, str) and bool(value.strip()) and
            value.strip().lower() not in {'todo', 'tbd', 'n/a', 'na', 'none', 'pending', 'unknown', '-', '...'} and
            not re.match(r'^(?:todo|tbd|fixme)(?:$|[\s:])', value.strip(), re.I) and
            not re.fullmatch(r'<[^>]*>', value.strip()))


def strings(value, allowed=None, nonempty=True):
    return (isinstance(value, list) and (bool(value) or not nonempty) and
            all(meaningful(v) for v in value) and len(value) == len(set(value)) and
            (allowed is None or set(value) <= allowed))


def local_file(root, name):
    if not isinstance(name, str) or not name or Path(name).is_absolute():
        return False
    try:
        path = (root / name).resolve()
        return path.is_relative_to(root.resolve()) and path.is_file()
    except (OSError, RuntimeError, ValueError):
        return False


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def registry_digest(root):
    return hashlib.sha256((Path(root) / 'references/principles.json').read_bytes()).hexdigest()


def validate_registry(root):
    """Return (errors, records); malformed input produces diagnostics, not a traceback."""
    root = Path(root)
    errors, inventory = [], {}
    for path in sorted((root / 'references/sources').glob('*.md')):
        try:
            headings = HEADING.findall(path.read_text(encoding='utf-8'))
        except (OSError, UnicodeError) as exc:
            errors.append(f'{path.name}: {exc}')
            continue
        for heading, ident, title in headings:
            if ident in inventory:
                errors.append(f'duplicate dossier heading {ident}')
            inventory[ident] = (path.relative_to(root).as_posix(), heading, title)
    if not inventory:
        errors.append('no dossier principle headings found')
    try:
        data = read_json(root / 'references/principles.json')
    except (OSError, UnicodeError, ValueError) as exc:
        return errors + [f'principles.json: {exc}'], []
    if not isinstance(data, dict) or type(data.get('schema_version')) is not int or data['schema_version'] != 1:
        return errors + ['registry schema_version must be 1'], []
    records = data.get('principles')
    if not isinstance(records, list) or not records:
        return errors + ['registry principles must be a nonempty list'], []
    found = set()
    for i, record in enumerate(records):
        label = f'principles[{i}]'
        if not isinstance(record, dict):
            errors.append(f'{label}: must be an object')
            continue
        ident = record.get('id')
        if not isinstance(ident, str) or not re.fullmatch(r'[A-Z]+-\d{2}', ident):
            errors.append(f'{label}: invalid id')
            continue
        label = ident
        if ident in found:
            errors.append(f'{label}: duplicate registry id')
        found.add(ident)
        expected = inventory.get(ident)
        source = record.get('source')
        if expected is None:
            errors.append(f'{label}: absent from dossier headings')
        elif not isinstance(source, dict) or (source.get('path'), source.get('heading'), record.get('title')) != expected:
            errors.append(f'{label}: source path, heading, or title differs from dossier')
        if record.get('kind') != 'heuristic':
            errors.append(f'{label}: book principles must have kind heuristic')
        for field, allowed in [('domains', DOMAINS), ('tags', TAGS), ('platforms', PLATFORMS), ('stages', STAGES), ('triggers', None)]:
            if not strings(record.get(field), allowed):
                errors.append(f'{label}: invalid {field}')
        if not meaningful(record.get('exceptions')):
            errors.append(f'{label}: exceptions must describe contextual limits')
        verification = record.get('verification')
        if not isinstance(verification, dict) or not strings(verification.get('methods'), METHODS) or not meaningful(verification.get('question')):
            errors.append(f'{label}: invalid verification methods/question')
        related = record.get('related')
        if not strings(related, nonempty=False) or (isinstance(related, list) and any(not isinstance(v, str) or v == ident or v not in inventory for v in related)):
            errors.append(f'{label}: invalid related IDs (unknown, self, or duplicate)')
        routes = record.get('routes')
        if not strings(routes):
            errors.append(f'{label}: routes must be a nonempty list')
        else:
            for route in routes:
                if not route.startswith('references/') or route.startswith('references/sources/') or not route.endswith('.md') or not local_file(root, route):
                    errors.append(f'{label}: route is not an existing operational module: {route}')
    for ident in sorted(set(inventory) - found):
        errors.append(f'{ident}: missing registry entry')
    return errors, records


DISPOSITIONS = {'unresolved', 'applied', 'departed', 'not_applicable', 'deferred'}


def validate_brief(brief):
    if not isinstance(brief, dict):
        return ['brief must be an object']
    errors = []
    if not meaningful(brief.get('summary')):
        errors.append('brief.summary must be explicit')
    for field, allowed in [('platform', PLATFORMS | {'mixed', 'unspecified'}),
                           ('depth', {'routine', 'screen', 'journey'}),
                           ('mode', {'build', 'design', 'research', 'critique'})]:
        if not isinstance(brief.get(field), str) or brief[field] not in allowed:
            errors.append(f'brief.{field} invalid')
    if not strings(brief.get('tags'), TAGS, nonempty=False):
        errors.append('brief.tags must be an explicit list of known tags')
    return errors


def candidates(brief, principles):
    if brief['depth'] == 'routine':
        return []
    tags = set(brief['tags']) | {'core'}
    return [p for p in principles if
            (brief['platform'] in {'mixed', 'unspecified'} or brief['platform'] in p['platforms']) and
            tags.intersection(p['tags'])]


def new_verification():
    return {'status': 'not_verified', 'method': 'inspection', 'evidence': [], 'limit': ''}


def init_packet(brief, root, principles):
    errors = validate_brief(brief)
    if errors:
        raise ValueError('; '.join(errors))
    return {'schema_version': 1, 'registry_sha256': registry_digest(root), 'brief': brief,
            'claimed_status': 'partial',
            'domains': [] if brief['depth'] == 'routine' else [
                {'domain': domain, 'status': 'unresolved', 'reason': '', 'principle_ids': [], 'requirement_ids': []}
                for domain in sorted(DOMAINS)],
            'guidance': [{'id': p['id'], 'disposition': 'unresolved', 'reason': '', 'criterion': '',
                          'verification': new_verification()} for p in candidates(brief, principles)],
            'requirements': [], 'artifacts': [], 'review': {'status': 'not_requested', 'evidence': []}}


def check_evidence(evidence, base, label, required=False, require_hash=False, packet_path=None, artifacts=False):
    errors = []
    if not isinstance(evidence, list) or (required and not evidence):
        return [f'{label}: evidence must be a {"nonempty " if required else ""}list']
    for i, item in enumerate(evidence):
        loc = f'{label}.evidence[{i}]'
        if not isinstance(item, dict):
            errors.append(f'{loc}: must be an object')
            continue
        path = item.get('path')
        if (not meaningful(path) or Path(path).is_absolute() or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', path)):
            errors.append(f'{loc}: path must be a relative local artifact file')
        else:
            try:
                exists = (base / path).is_file()
            except (OSError, ValueError):
                exists = False
            if not exists:
                errors.append(f'{loc}: evidence file does not exist or is not a regular file: {path}')
        if meaningful(path) and not Path(path).is_absolute() and not re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', path):
            try:
                resolved = (base / path).resolve()
            except (OSError, RuntimeError, ValueError):
                errors.append(f'{loc}: evidence path cannot be resolved')
                continue
            if packet_path is not None and resolved == Path(packet_path).resolve():
                errors.append(f'{loc}: packet cannot serve as its own evidence or artifact')
            digest = item.get('sha256')
            if require_hash or digest is not None:
                if not isinstance(digest, str) or not re.fullmatch(r'[a-f0-9]{64}', digest):
                    errors.append(f'{loc}: sha256 must record the inspected file hash')
                elif resolved.is_file():
                    try:
                        current_digest = hashlib.sha256(resolved.read_bytes()).hexdigest()
                    except OSError as exc:
                        errors.append(f'{loc}: cannot read evidence: {exc}')
                    else:
                        if current_digest != digest:
                            errors.append(f'{loc}: stale sha256; file changed since observation')
        if not artifacts and not meaningful(item.get('observation')):
            errors.append(f'{loc}: observation must record a specific result')
    return errors


def check_record(record, base, label, requirement=False, packet_path=None):
    errors, blockers = [], []
    disposition = record.get('disposition')
    if not isinstance(disposition, str) or disposition not in DISPOSITIONS:
        return [f'{label}: invalid disposition'], []
    if disposition in {'departed', 'deferred', 'not_applicable'} and not meaningful(record.get('reason')):
        errors.append(f'{label}: {disposition} needs a reason')
    if disposition in {'applied', 'departed'} and not meaningful(record.get('criterion')):
        errors.append(f'{label}: {disposition} needs an observable criterion')
    if disposition in {'unresolved', 'deferred'}:
        blockers.append(f'{label}: {disposition}')
    if requirement:
        if not isinstance(record.get('kind'), str) or record['kind'] not in {'requirement', 'heuristic', 'preference'}:
            errors.append(f'{label}: invalid requirement kind')
        if not meaningful(record.get('origin')):
            errors.append(f'{label}: origin required')
        if record.get('kind') == 'requirement' and disposition == 'departed':
            blockers.append(f'{label}: binding requirement departed; revise its origin/criterion explicitly before claiming verified')
    verification = record.get('verification')
    if not isinstance(verification, dict):
        return errors + [f'{label}: verification must be an object'], blockers
    status = verification.get('status')
    if not isinstance(status, str) or status not in {'not_verified', 'pass', 'fail'}:
        return errors + [f'{label}: invalid verification status'], blockers
    if not isinstance(verification.get('method'), str) or verification['method'] not in METHODS:
        errors.append(f'{label}: invalid verification method')
    if not isinstance(verification.get('limit'), str):
        errors.append(f'{label}: verification.limit must be a string')
    if status == 'pass' and not meaningful(record.get('criterion')):
        errors.append(f'{label}: passing verification needs an observable criterion')
    errors.extend(check_evidence(verification.get('evidence'), base, label, required=status in {'pass', 'fail'}, require_hash=status == 'pass', packet_path=packet_path))
    if status == 'fail':
        blockers.append(f'{label}: verification failed')
    elif disposition in {'applied', 'departed'} and status != 'pass':
        blockers.append(f'{label}: {disposition} is not verified')
    return errors, blockers


def check_packet(packet, packet_path, root, principles, require_verified=False):
    """Return structural/claim errors and unresolved scope limitations separately."""
    errors, blockers = [], []
    if not isinstance(packet, dict):
        return ['packet must be an object'], []
    if type(packet.get('schema_version')) is not int or packet['schema_version'] != 1:
        errors.append('packet schema_version must be 1')
    if packet.get('registry_sha256') != registry_digest(root):
        errors.append('stale or missing registry_sha256; reconcile against the current registry')
    brief_errors = validate_brief(packet.get('brief'))
    errors.extend(brief_errors)
    if packet.get('claimed_status') not in ('partial', 'verified_for_scope'):
        errors.append('claimed_status must be partial or verified_for_scope')
    known = {p['id']: p for p in principles}
    rows = {}
    requirements = {}
    base = Path(packet_path).resolve().parent
    for field, destination in [('guidance', rows), ('requirements', requirements)]:
        records = packet.get(field)
        if not isinstance(records, list):
            errors.append(f'{field} must be a list')
            continue
        for i, record in enumerate(records):
            label = f'{field}[{i}]'
            if not isinstance(record, dict):
                errors.append(f'{label}: must be an object')
                continue
            ident = record.get('id')
            if not isinstance(ident, str):
                errors.append(f'{label}: id must be a string')
                continue
            label = ident
            if ident in destination:
                errors.append(f'{label}: duplicate {field} id')
            destination[ident] = record
            if field == 'guidance' and ident not in known:
                errors.append(f'{label}: unknown principle')
            if field == 'requirements' and not re.fullmatch(r'REQ-[A-Za-z0-9][A-Za-z0-9_-]*', ident):
                errors.append(f'{label}: requirement id must start REQ-')
            row_errors, row_blockers = check_record(record, base, label, field == 'requirements', packet_path)
            errors.extend(row_errors)
            blockers.extend(row_blockers)
    if not brief_errors:
        expected = {p['id'] for p in candidates(packet['brief'], principles)}
        for ident in sorted(expected - set(rows)):
            errors.append(f'{ident}: missing routed candidate; record its disposition instead of deleting it')
    domains = packet.get('domains')
    seen = set()
    if not isinstance(domains, list):
        errors.append('domains must be a list')
        domains = []
    for i, domain in enumerate(domains):
        label = f'domains[{i}]'
        if not isinstance(domain, dict):
            errors.append(f'{label}: must be an object')
            continue
        name = domain.get('domain')
        if not isinstance(name, str) or name not in DOMAINS:
            errors.append(f'{label}: invalid domain')
            continue
        label = f'domain {name}'
        if name in seen:
            errors.append(f'{label}: duplicate domain')
        seen.add(name)
        status = domain.get('status')
        if status not in ('unresolved', 'applicable', 'not_applicable'):
            errors.append(f'{label}: invalid status')
        if status == 'unresolved':
            blockers.append(f'{label}: unresolved')
        if status == 'not_applicable' and not meaningful(domain.get('reason')):
            errors.append(f'{label}: not_applicable needs a reason')
        active = False
        for field, records in [('principle_ids', rows), ('requirement_ids', requirements)]:
            ids = domain.get(field)
            if not strings(ids, nonempty=False):
                errors.append(f'{label}: invalid {field}')
                continue
            for ident in ids:
                if ident not in records:
                    errors.append(f'{label}: missing {field} record {ident}')
                    continue
                if field == 'principle_ids' and (ident not in known or name not in known[ident]['domains']):
                    errors.append(f'{label}: principle {ident} does not cover this domain')
                if records[ident].get('disposition') != 'not_applicable':
                    active = True
        if status == 'applicable' and not active:
            errors.append(f'{label}: applicable domain needs an active guidance or requirement reference')
        if status == 'not_applicable' and active:
            errors.append(f'{label}: not_applicable contradicts an active guidance or requirement reference')
    if not brief_errors and packet['brief']['depth'] != 'routine':
        for name in sorted(DOMAINS - seen):
            errors.append(f'missing domain {name}')
    review = packet.get('review')
    if not isinstance(review, dict):
        errors.append('review must be an object')
    else:
        if review.get('status') not in ('not_requested', 'pending', 'completed'):
            errors.append('review: invalid status')
        if review.get('status') == 'pending':
            blockers.append('independent review pending')
        errors.extend(check_evidence(review.get('evidence'), base, 'review', required=review.get('status') == 'completed', require_hash=review.get('status') == 'completed', packet_path=packet_path))
    needs_artifact = (not brief_errors and packet['brief']['depth'] != 'routine' and
                      packet['brief']['mode'] in {'build', 'design', 'critique'} and
                      packet.get('claimed_status') == 'verified_for_scope')
    errors.extend(check_evidence(packet.get('artifacts', []), base, 'artifacts', required=needs_artifact,
                                 require_hash=True, packet_path=packet_path, artifacts=True))
    if (not brief_errors and packet['brief']['depth'] != 'routine' and
            packet.get('claimed_status') == 'verified_for_scope'):
        passed_criteria = [row for row in list(rows.values()) + list(requirements.values())
                           if row.get('disposition') in ('applied', 'departed') and
                           meaningful(row.get('criterion')) and isinstance(row.get('verification'), dict) and
                           row['verification'].get('status') == 'pass']
        if not passed_criteria:
            errors.append('verified_for_scope requires at least one applied/departed passing criterion for nonroutine scope')
        linked = set()
        for domain in domains:
            if isinstance(domain, dict) and domain.get('status') == 'applicable':
                for field in ('principle_ids', 'requirement_ids'):
                    if strings(domain.get(field), nonempty=False):
                        linked.update(domain[field])
        for ident, row in list(rows.items()) + list(requirements.items()):
            if row.get('disposition') in ('applied', 'departed') and ident not in linked:
                errors.append(f'{ident}: active criterion needs an applicable domain reference for verified scope')
    if packet.get('claimed_status') == 'verified_for_scope' and blockers:
        errors.append('verified_for_scope claim contradicted by: ' + '; '.join(blockers))
    if require_verified and packet.get('claimed_status') != 'verified_for_scope':
        errors.append('verified_for_scope required; packet honestly claims partial')
    return errors, blockers


def search(principles, terms, limit=8):
    tokens = set(re.findall(r'[a-z0-9]+', ' '.join(terms).lower()))
    hits = []
    for principle in principles:
        title_words = set(re.findall(r'[a-z0-9]+', (principle['id'] + ' ' + principle['title']).lower()))
        route_words = set(re.findall(r'[a-z0-9]+', ' '.join(principle['tags'] + principle['domains']).lower()))
        trigger_words = set(re.findall(r'[a-z0-9]+', ' '.join(principle['triggers']).lower()))
        relevance = 4 * len(tokens & title_words) + 2 * len(tokens & route_words) + len(tokens & trigger_words)
        if relevance:
            hits.append((relevance, principle))
    hits.sort(key=lambda hit: (-hit[0], hit[1]['id']))
    return [p for _, p in hits[:limit]]



def show_cards(root, principles, ids):
    """Read exact cited cards, without loading unrelated chapters into the output."""
    known = {p['id']: p for p in principles}
    requested = list(dict.fromkeys(ids))
    if not requested or len(requested) > 8 or any(ident not in known for ident in requested):
        raise ValueError('show requires 1–8 known principle IDs')
    cards = []
    for ident in requested:
        source = known[ident]['source']
        text = (Path(root) / source['path']).read_text(encoding='utf-8')
        pattern = r'^#{2,3} ' + re.escape(source['heading']) + r'\s*$'
        start = re.search(pattern, text, re.M)
        if start is None:
            raise ValueError(f'{ident}: source heading missing')
        remaining = text[start.end():]
        end = re.search(r'^#{1,3} ', remaining, re.M)
        body = remaining[:end.start()] if end else remaining
        cards.append(source['path'] + '\n' + start.group().strip() + '\n' + body.strip())
    return '\n\n'.join(cards)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('registry', 'init', 'check', 'search', 'show', 'hash'):
        command = commands.add_parser(name)
        command.add_argument('--root', type=Path, default=argparse.SUPPRESS)
        if name == 'init':
            command.add_argument('--brief', type=Path, required=True)
            command.add_argument('--out', type=Path, required=True)
        elif name == 'check':
            command.add_argument('packet', type=Path)
            command.add_argument('--require-verified', action='store_true')
        elif name == 'hash':
            command.add_argument('file', type=Path)
        elif name == 'show':
            command.add_argument('ids', nargs='+')
        elif name == 'search':
            command.add_argument('terms', nargs='+')
    args = parser.parse_args(argv)
    try:
        if args.command == 'hash':
            print(hashlib.sha256(args.file.read_bytes()).hexdigest())
            return 0
        errors, principles = validate_registry(args.root.resolve())
        if errors:
            for error in errors:
                print('ERROR:', error)
            return 1
        if args.command == 'registry':
            print(f'{len(principles)} contextual principles; registry matches dossier inventory and operational routes')
        elif args.command == 'show':
            print(show_cards(args.root, principles, args.ids))
        elif args.command == 'init':
            packet = init_packet(read_json(args.brief), args.root, principles)
            with args.out.open('x', encoding='utf-8') as output:
                json.dump(packet, output, indent=2, ensure_ascii=False)
                output.write('\n')
            print(f'Created {args.out}: {len(packet["guidance"])} candidates; partial; applicability requires judgment')
        elif args.command == 'check':
            packet = read_json(args.packet)
            errors, blockers = check_packet(packet, args.packet, args.root, principles, args.require_verified)
            for error in errors:
                print('ERROR:', error)
            if errors:
                print('Record inconsistent; no claim of quality/usability verified')
                return 1
            print(f'record consistent; {packet["claimed_status"]}; no claim of quality/usability verified')
            for blocker in blockers:
                print('OPEN:', blocker)
        else:
            hits = search(principles, args.terms)
            for p in hits:
                print(f'{p["id"]} — {p["title"]}\n  {p["source"]["path"]} :: {p["source"]["heading"]}\n  Routes: {", ".join(p["routes"])}')
            if not hits:
                print('No matching principles; try a task, domain, or interaction tag.')
        return 0
    except (OSError, UnicodeError, ValueError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
