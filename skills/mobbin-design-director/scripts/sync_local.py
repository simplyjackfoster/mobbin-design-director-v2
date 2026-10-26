#!/usr/bin/env python3
"""Copy a validated skill locally, preserving a backup and content provenance.

Default is a dry run. Use --apply --backup-dir OUTSIDE_REPOS after validation.
Does not fetch, push, install a CLI, edit project instructions, or change symlinks.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys


def digest_tree(root):
    digest = hashlib.sha256()
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.name != 'SOURCE' and '__pycache__' not in p.parts:
            digest.update(p.relative_to(root).as_posix().encode() + b'\0')
            digest.update(p.read_bytes())
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path)
    parser.add_argument('--source', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--backup-dir', type=Path)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    src, dst = args.source.resolve(), args.destination.expanduser().absolute()
    if dst.is_symlink():
        sys.exit('Destination is a symlink; inspect its owner and sync the canonical copy instead.')
    if src == dst.resolve() or src in dst.resolve().parents or dst.resolve() in src.parents:
        sys.exit('Source and destination must be separate trees.')
    if not (src / 'SKILL.md').is_file():
        sys.exit('Source is not a skill.')
    if not args.apply:
        print(f'DRY RUN: copy {src} to {dst}; content sha256 {digest_tree(src)}')
        return
    if not args.backup_dir:
        sys.exit('--backup-dir is required for apply.')
    result = subprocess.run([sys.executable, str(src / 'scripts/validate.py'), '--root', str(src)])
    if result.returncode:
        sys.exit('Validation failed; no destination changes made.')
    backup_dir = args.backup_dir.expanduser().resolve()
    if backup_dir in (src, dst.resolve()) or src in backup_dir.parents or dst.resolve() in backup_dir.parents:
        sys.exit('Backup directory must be outside source and destination.')
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup = backup_dir / (dst.name + '-' + stamp)
    dst.parent.mkdir(parents=True, exist_ok=True)
    staging = dst.with_name(dst.name + '.staging-' + stamp)
    shutil.copytree(src, staging, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    source_hash = digest_tree(src)
    try:
        base = subprocess.check_output(['git', '-C', str(src), 'rev-parse', 'HEAD'], text=True).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        base = 'not available'
    manifest = json.loads((src.parent.parent / '.claude-plugin/plugin.json').read_text())
    (staging / 'SOURCE').write_text(
        f"Locally synchronized {manifest['name']} v{manifest['version']}.\n"
        f"Canonical repository: {manifest.get('repository', 'not recorded')}.\n"
        f'Base commit: {base}\n'
        f'Content SHA-256 (excluding SOURCE): {source_hash}\n'
        'The content hash identifies the local tree, including uncommitted changes.\n'
        'Change the source repository and re-sync; preserve project-specific context separately.\n')
    if digest_tree(staging) != source_hash:
        shutil.rmtree(staging)
        sys.exit('Staging verification failed; destination unchanged.')
    if dst.exists():
        shutil.copytree(dst, backup)
        shutil.rmtree(dst)
    try:
        staging.rename(dst)
    except OSError:
        if backup.exists() and not dst.exists():
            shutil.copytree(backup, dst)
        raise
    print(f'Synced {dst}; sha256 {source_hash}; backup {backup if backup.exists() else "not needed (new install)"}')


if __name__ == '__main__':
    main()
