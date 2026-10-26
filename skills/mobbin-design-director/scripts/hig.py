#!/usr/bin/env python3
"""Print a Human Interface Guidelines page as plain text (stdlib, network).

Apple serves each HIG page as JSON. This renders the headings, paragraphs and
list items so an agent can read the current rule in one call instead of trusting
a stale summary or a bare link. Nothing is cached in the repo.

Usage:
  python3 scripts/hig.py sheets
  python3 scripts/hig.py tab-bars --max-chars 6000
  python3 scripts/hig.py --list            # slugs of every component page
"""
import argparse
import json
import sys
import urllib.request

BASE = 'https://developer.apple.com/tutorials/data/design/human-interface-guidelines/'
GROUPS = ['components', 'content', 'layout-and-organization', 'menus-and-actions',
          'navigation-and-search', 'presentation', 'selection-and-input', 'status',
          'system-experiences', 'patterns', 'foundations']


def fetch(slug):
    req = urllib.request.Request(BASE + slug + '.json', headers={'User-Agent': 'mobbin-design-director/3.0'})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode('utf-8'))


REFS = {}


def inline(parts):
    out = []
    for p in parts or []:
        t = p.get('type')
        if t in ('text', 'codeVoice'):
            out.append(p.get('text') or p.get('code', ''))
        elif t == 'reference':
            ref = REFS.get(p.get('identifier', ''), {})
            out.append(inline(p.get('inlineContent')) or ref.get('title') or p.get('title', ''))
        elif t in ('emphasis', 'strong', 'link'):
            out.append(inline(p.get('inlineContent')) or p.get('title', ''))
        elif t == 'inlineHead':
            out.append(inline(p.get('inlineContent')))
    return ''.join(out)


def render(content, depth=0):
    lines = []
    for block in content or []:
        t = block.get('type')
        if t == 'heading':
            lines.append('\n' + '#' * max(2, block.get('level', 2)) + ' ' + block.get('text', ''))
        elif t == 'paragraph':
            lines.append(inline(block.get('inlineContent')))
        elif t in ('unorderedList', 'orderedList'):
            for item in block.get('items', []):
                body = render(item.get('content'), depth + 1).strip()
                lines.append('  ' * depth + '- ' + body)
        elif t == 'aside':
            lines.append('Note: ' + render(block.get('content'), depth).strip())
        elif t == 'termList':
            for item in block.get('items', []):
                lines.append('- ' + inline(item.get('term', {}).get('inlineContent')) + ': '
                             + render(item.get('definition', {}).get('content'), depth).strip())
    return '\n'.join(l for l in lines if l is not None)


def page_text(data):
    REFS.update(data.get('references', {}))
    title = data.get('metadata', {}).get('title', '')
    abstract = inline(data.get('abstract'))
    body = []
    for sec in data.get('primaryContentSections', []):
        body.append(render(sec.get('content')))
    return f'# {title}\n{abstract}\n' + '\n'.join(body)


def list_slugs():
    seen = []
    for g in GROUPS:
        try:
            data = fetch(g)
        except Exception as exc:  # network or 404; keep going
            print(f'{g}: {exc}', file=sys.stderr)
            continue
        for ref in data.get('references', {}).values():
            url = ref.get('url', '')
            if url.startswith('/design/human-interface-guidelines/') and url.count('/') == 3:
                slug = url.rsplit('/', 1)[1]
                if slug not in seen:
                    seen.append(slug)
    return seen


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('slug', nargs='?')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--max-chars', type=int, default=12000)
    args = ap.parse_args()
    if args.list:
        print('\n'.join(list_slugs()))
        return 0
    if not args.slug:
        ap.error('give a slug such as sheets, or --list')
    text = page_text(fetch(args.slug))
    if len(text) > args.max_chars:
        text = text[:args.max_chars].rstrip() + f'\n[truncated at {args.max_chars} chars; raise --max-chars]'
    print(text)
    print(f'\nSource: https://developer.apple.com/design/human-interface-guidelines/{args.slug}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
