#!/usr/bin/env python3
"""Count the iOS "AI-felt UI" tells in SwiftUI sources (stdlib only).

Each tell is one small text check. The checks are approximations, so a count
is a pointer for a human read, never a verdict. The tells come from the iOS
section of the slop taxonomy (wholiver, vermont42, Hudson). Exit status is
always 0; the output is the report.

Usage: python3 swiftui_slop_lint.py PATH [--limit N]
PATH is a directory (scanned for *.swift) or one .swift file.
"""
import argparse
from pathlib import Path
import re
import sys

# (key, description, how the check approximates the tell)
TELLS = [
    ('gradient_purple_blue', 'LinearGradient with purple or blue',
     'LinearGradient on a line, .purple or .blue on that line or the next 3'),
    ('fixed_font_size', 'Fixed .font(.system(size:)) instead of Dynamic Type',
     'literal match'),
    ('font_weight', 'fontWeight() density',
     'every fontWeight( call; compare against screen count'),
    ('tap_gesture_not_button', 'onTapGesture instead of Button',
     'onTapGesture with no Button on that line or the 3 above'),
    ('color_purple', 'Color.purple',
     'literal match'),
    ('emoji_in_text', 'Emoji inside Text("...")',
     'a character in the emoji ranges inside a Text string literal'),
    ('symbol_without_label', 'Image(systemName:) in a file with no accessibilityLabel',
     'per occurrence, when the whole file has no accessibilityLabel'),
    ('corner_radius_with_shadow', '.cornerRadius( next to .shadow(',
     'both on one line, or on adjacent lines'),
    ('lorem', 'Lorem placeholder copy',
     'literal match, case sensitive'),
    ('padding_off_grid', 'padding with a literal that is not a multiple of 4',
     '.padding(N) or .padding(edges, N); N is a number literal'),
    ('hamburger_symbol', 'Hamburger menu symbol (line.3.horizontal)',
     'literal match'),
]

GRADIENT = re.compile(r'LinearGradient')
PURPLE_BLUE = re.compile(r'\.(purple|blue)\b')
FIXED_FONT = re.compile(r'\.font\(\.system\(size:')
FONT_WEIGHT = re.compile(r'fontWeight\(')
TAP = re.compile(r'onTapGesture')
BUTTON = re.compile(r'\bButton\b')
COLOR_PURPLE = re.compile(r'Color\.purple')
TEXT_LITERAL = re.compile(r'Text\(\s*"((?:[^"\\]|\\.)*)"')
SYMBOL = re.compile(r'Image\(systemName:')
A11Y_LABEL = re.compile(r'accessibilityLabel')
CORNER = re.compile(r'\.cornerRadius\(')
SHADOW = re.compile(r'\.shadow\(')
LOREM = re.compile(r'Lorem')
PADDING = re.compile(r'\.padding\((?:[^()]*?,\s*)?(\d+(?:\.\d+)?)\s*\)')
HAMBURGER = re.compile(r'line\.3\.horizontal')


def is_emoji(char):
    code = ord(char)
    return code >= 0x1F000 or 0x2600 <= code <= 0x27BF


def scan_lines(lines):
    """Return {tell_key: [line_number, ...]} for one file's lines."""
    hits = {key: [] for key, _, _ in TELLS}
    has_label = any(A11Y_LABEL.search(line) for line in lines)
    for index, line in enumerate(lines):
        number = index + 1
        if GRADIENT.search(line):
            window = ''.join(lines[index:index + 4])
            if PURPLE_BLUE.search(window):
                hits['gradient_purple_blue'].append(number)
        if FIXED_FONT.search(line):
            hits['fixed_font_size'].append(number)
        hits['font_weight'].extend([number] * len(FONT_WEIGHT.findall(line)))
        if TAP.search(line):
            context = ''.join(lines[max(0, index - 3):index + 1])
            if not BUTTON.search(context):
                hits['tap_gesture_not_button'].append(number)
        if COLOR_PURPLE.search(line):
            hits['color_purple'].append(number)
        for literal in TEXT_LITERAL.findall(line):
            if any(is_emoji(char) for char in literal):
                hits['emoji_in_text'].append(number)
                break
        if not has_label and SYMBOL.search(line):
            hits['symbol_without_label'].append(number)
        if CORNER.search(line):
            window = ''.join(lines[max(0, index - 1):index + 2])
            if SHADOW.search(window):
                hits['corner_radius_with_shadow'].append(number)
        if LOREM.search(line):
            hits['lorem'].append(number)
        for value in PADDING.findall(line):
            if float(value) % 4 != 0:
                hits['padding_off_grid'].append(number)
        if HAMBURGER.search(line):
            hits['hamburger_symbol'].append(number)
    return hits


def swift_files(path):
    if path.is_file():
        return [path]
    return sorted(p for p in path.rglob('*.swift') if p.is_file())


def scan(path):
    """Return {tell_key: [(file, line_number), ...]} for every .swift under path."""
    findings = {key: [] for key, _, _ in TELLS}
    for file in swift_files(path):
        lines = file.read_text(encoding='utf-8', errors='replace').splitlines(keepends=True)
        for key, numbers in scan_lines(lines).items():
            findings[key].extend((file, number) for number in numbers)
    return findings


def render(findings, root, limit):
    width = max(len(key) for key, _, _ in TELLS)
    out = [f'{"tell".ljust(width)}  count  description']
    for key, description, _ in TELLS:
        out.append(f'{key.ljust(width)}  {len(findings[key]):5d}  {description}')
    out.append('')
    for key, _, approximation in TELLS:
        pointers = findings[key]
        if not pointers:
            continue
        out.append(f'{key} ({approximation}):')
        for file, number in pointers[:limit]:
            try:
                shown = file.relative_to(root)
            except ValueError:
                shown = file
            out.append(f'  {shown}:{number}')
        if len(pointers) > limit:
            out.append(f'  ... {len(pointers) - limit} more')
    out.append('')
    out.append('Counts are diagnostics, not verdicts.')
    return '\n'.join(out)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('path', type=Path)
    parser.add_argument('--limit', type=int, default=10,
                        help='file:line pointers to print per tell (default 10)')
    args = parser.parse_args(argv)
    path = args.path
    root = path if path.is_dir() else path.parent
    if not path.exists():
        print(f'nothing scanned: {path} does not exist')
    findings = scan(path) if path.exists() else {key: [] for key, _, _ in TELLS}
    print(render(findings, root, max(args.limit, 0)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
