#!/usr/bin/env bash
# diff-report.sh: compare two capture directories pixel by pixel and build a contact sheet.
#
# UNTESTED on this author's Mac (no Xcode.app). Verify on a Mac with Xcode before relying on it.
# Tools come from research/04 step 6: odiff or magick compare for the diff, magick montage for
# the contact sheet ("nothing was run; all from docs"). Lines marked "not from research" carry
# a flag or an exit code the research did not state.
set -euo pipefail

usage() {
  cat <<'EOF'
usage: diff-report.sh <before-dir> <after-dir> <out-dir> [--threshold <0..1>]

Pairs every *.png in <before-dir> with the file of the same name in
<after-dir>, writes <out-dir>/diff-<name>.png for each pair, then builds
<out-dir>/contact-sheet.png with before, after and diff side by side.
Uses odiff when it is on PATH, else magick compare. --threshold is the
odiff per-pixel colour tolerance (default 0.1); magick ignores it.

exit 0  no pair differs
exit 1  at least one pair differs, or a file is missing on one side
exit 2  usage error, or neither odiff nor magick is installed
EOF
}

if [ "$#" -lt 3 ]; then
  usage >&2
  exit 2
fi
case "$1" in -h|--help) usage; exit 0 ;; esac

before="$1"; after="$2"; out="$3"
shift 3
threshold="0.1"
while [ "$#" -gt 0 ]; do
  case "$1" in
    --threshold) threshold="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "diff-report.sh: unknown option $1" >&2; usage >&2; exit 2 ;;
  esac
done
[ -d "$before" ] || { echo "diff-report.sh: $before is not a directory" >&2; exit 2; }
[ -d "$after" ] || { echo "diff-report.sh: $after is not a directory" >&2; exit 2; }

if command -v odiff >/dev/null; then
  tool="odiff"
elif command -v magick >/dev/null; then
  tool="magick"
else
  echo "diff-report.sh: neither odiff nor magick is installed. brew install odiff, or brew install imagemagick" >&2
  exit 2
fi

mkdir -p "$out"
differing=0
same=0
missing=0
tiles=()

for a in "$before"/*.png; do
  [ -e "$a" ] || { echo "diff-report.sh: no *.png in $before" >&2; exit 1; }
  name="$(basename "$a")"
  b="$after/$name"
  diff="$out/diff-$name"
  if [ ! -f "$b" ]; then
    echo "MISSING  $name (not in $after)"
    missing=$((missing + 1))
    continue
  fi
  status=0
  if [ "$tool" = "odiff" ]; then
    # not from research: --threshold, and odiff's nonzero exit on a difference.
    odiff --threshold "$threshold" "$a" "$b" "$diff" >/dev/null 2>&1 || status=$?
  else
    # not from research: -metric AE, and compare's exit 1 (differs) / 2 (error).
    magick compare -metric AE "$a" "$b" "$diff" >/dev/null 2>&1 || status=$?
    if [ "$status" -eq 2 ]; then
      echo "diff-report.sh: magick compare failed on $name" >&2
      exit 2
    fi
  fi
  if [ "$status" -eq 0 ]; then
    echo "SAME     $name"
    same=$((same + 1))
  else
    echo "DIFFERS  $name -> $diff"
    differing=$((differing + 1))
  fi
  tiles+=("$a" "$b" "$diff")
done

# bash 3.2 rejects "${tiles[@]}" on an empty array under set -u, so test the count first.
if [ "${#tiles[@]}" -gt 0 ]; then
  if command -v magick >/dev/null; then
    # not from research: the montage flags. Three tiles per row: before, after, diff.
    magick montage "${tiles[@]}" -tile 3x -geometry +4+4 -label '%f' "$out/contact-sheet.png"
    echo "contact sheet: $out/contact-sheet.png"
  else
    echo "no magick on PATH, so no contact sheet (brew install imagemagick)"
  fi
fi

echo "same $same, differing $differing, missing $missing"
if [ "$differing" -gt 0 ] || [ "$missing" -gt 0 ]; then
  exit 1
fi
