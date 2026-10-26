#!/usr/bin/env python3
"""Cache Mobbin screen images locally with a provenance sidecar (stdlib only).

Input is a JSON file in the shape the Mobbin MCP returns:
  {"screens": [{"id", "image_url", "mobbin_url", "app_name", "platform"}, ...]}
or
  {"flows": [{"app_name", "platform", "mobbin_url",
              "screens": [{"screen_id", "image_url", "position"}, ...]}, ...]}
A flow screen inherits app_name, platform and mobbin_url from its flow when it
has none of its own.

Each image lands at OUT_DIR/<id>.<ext> with OUT_DIR/<id>.json beside it holding
mobbin_url, app_name, platform, fetched_at and source_query. An image that is
already present is skipped. The output dir must not be inside a git repository:
cached screens are session material, never repo content.

Usage: python3 mobbin_cache.py results.json OUT_DIR [--dry-run] [--query TEXT]
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import urllib.request
from urllib.parse import urlparse

USER_AGENT = 'mobbin-design-director cache (stdlib urllib)'
DEFAULT_TIMEOUT = 30


def inside_git_repo(path):
    """True when path or any parent holds a .git entry (a dir, or a worktree file)."""
    resolved = path.expanduser().resolve()
    return any((p / '.git').exists() for p in [resolved, *resolved.parents])


def screens_from(data):
    """Flatten the two result shapes into one list of screen dicts."""
    screens = []
    for screen in data.get('screens', []):
        screens.append(dict(id=screen['id'], image_url=screen['image_url'],
                            mobbin_url=screen.get('mobbin_url'), app_name=screen.get('app_name'),
                            platform=screen.get('platform')))
    for flow in data.get('flows', []):
        for screen in flow.get('screens', []):
            screens.append(dict(id=screen.get('screen_id') or screen['id'],
                                image_url=screen['image_url'],
                                mobbin_url=screen.get('mobbin_url') or flow.get('mobbin_url'),
                                app_name=screen.get('app_name') or flow.get('app_name'),
                                platform=screen.get('platform') or flow.get('platform')))
    return screens


def image_path(out_dir, screen):
    suffix = Path(urlparse(screen['image_url']).path).suffix.lower() or '.bin'
    return out_dir / (str(screen['id']) + suffix)


def fetch(url, timeout):
    request = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def cache(screens, out_dir, source_query, dry_run=False, timeout=DEFAULT_TIMEOUT):
    """Return (fetched, skipped) counts. Writes nothing on a dry run."""
    fetched, skipped = 0, 0
    for screen in screens:
        target = image_path(out_dir, screen)
        if target.exists():
            print(f'skip    {target.name} (exists)')
            skipped += 1
            continue
        if dry_run:
            print(f'would fetch {screen["image_url"]} -> {target}')
            fetched += 1
            continue
        out_dir.mkdir(parents=True, exist_ok=True)
        target.write_bytes(fetch(screen['image_url'], timeout))
        sidecar = dict(id=screen['id'], image_url=screen['image_url'],
                       mobbin_url=screen['mobbin_url'], app_name=screen['app_name'],
                       platform=screen['platform'],
                       fetched_at=datetime.now(timezone.utc).isoformat(),
                       source_query=source_query)
        target.with_suffix('.json').write_text(json.dumps(sidecar, indent=2) + '\n')
        print(f'fetched {target.name}')
        fetched += 1
    return fetched, skipped


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('results', type=Path, help='JSON file of Mobbin results')
    parser.add_argument('out_dir', type=Path, help='cache directory, outside any git repo')
    parser.add_argument('--dry-run', action='store_true', help='print the plan, write nothing')
    parser.add_argument('--query', help='search text to record as source_query; '
                                       'falls back to a top-level "query" key in the JSON')
    parser.add_argument('--timeout', type=float, default=DEFAULT_TIMEOUT)
    args = parser.parse_args(argv)
    if inside_git_repo(args.out_dir):
        print(f'refused: {args.out_dir} is inside a git repository. '
              'Cache Mobbin images in the session scratchpad, not in a repo.', file=sys.stderr)
        return 2
    data = json.loads(args.results.read_text())
    screens = screens_from(data)
    source_query = args.query if args.query is not None else data.get('query')
    if args.dry_run:
        print(f'DRY RUN: {len(screens)} screens -> {args.out_dir}')
    fetched, skipped = cache(screens, args.out_dir, source_query, args.dry_run, args.timeout)
    verb = 'would fetch' if args.dry_run else 'fetched'
    print(f'{verb} {fetched}, skipped {skipped}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
