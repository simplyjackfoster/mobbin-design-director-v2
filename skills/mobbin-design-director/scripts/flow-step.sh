#!/usr/bin/env bash
# flow-step.sh: one step of a simulator flow: optional tap, then the AXe tree and a screenshot.
#
# UNTESTED on this author's Mac (no Xcode.app). Verify on a Mac with Xcode before relying on it.
# AXe verbs (describe-ui, tap --label, screenshot) come from research/04 step 4
# ("nothing was run; all from docs"). Lines marked "not from research" carry a flag the
# research did not state.
set -euo pipefail

usage() {
  cat <<'EOF'
usage: flow-step.sh <NN> [--tap <label>] [--settle <seconds>] [--udid <udid>]
                    [--out-dir <dir>] [--cfg <name>]

Writes <out-dir>/step-NN_<cfg>.png and <out-dir>/step-NN_<cfg>.json (the AXe
describe-ui tree). NN is two digits, e.g. 03. --tap taps the element whose
accessibility label matches, then waits --settle seconds (default 1) before the
capture. --udid, --out-dir and --cfg default to MDD_UDID, MDD_OUT_DIR and
MDD_CFG, which sim-matrix.sh exports.

Install AXe: brew install cameroncooke/axe/axe
EOF
}

if [ "$#" -lt 1 ]; then
  usage >&2
  exit 2
fi

step="$1"; shift
case "$step" in
  -h|--help) usage; exit 0 ;;
esac

tap_label=""
settle="1"
udid="${MDD_UDID:-}"
out_dir="${MDD_OUT_DIR:-}"
cfg="${MDD_CFG:-}"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --tap) tap_label="$2"; shift 2 ;;
    --settle) settle="$2"; shift 2 ;;
    --udid) udid="$2"; shift 2 ;;
    --out-dir) out_dir="$2"; shift 2 ;;
    --cfg) cfg="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "flow-step.sh: unknown option $1" >&2; usage >&2; exit 2 ;;
  esac
done

command -v axe >/dev/null || {
  echo "flow-step.sh: axe not found. Install it with: brew install cameroncooke/axe/axe" >&2
  exit 127
}

case "$step" in
  [0-9][0-9]) ;;
  *) echo "flow-step.sh: step must be two digits, got $step" >&2; exit 2 ;;
esac
[ -n "$udid" ] || { echo "flow-step.sh: no udid; pass --udid or export MDD_UDID" >&2; exit 2; }
[ -n "$out_dir" ] || { echo "flow-step.sh: no out dir; pass --out-dir or export MDD_OUT_DIR" >&2; exit 2; }
[ -n "$cfg" ] || { echo "flow-step.sh: no cfg; pass --cfg or export MDD_CFG" >&2; exit 2; }

mkdir -p "$out_dir"
png="$out_dir/step-${step}_${cfg}.png"
tree="$out_dir/step-${step}_${cfg}.json"

if [ -n "$tap_label" ]; then
  # not from research: --udid as the device selector flag.
  axe tap --label "$tap_label" --udid "$udid"
  sleep "$settle"
fi

# not from research: --udid, and describe-ui writing JSON to stdout.
axe describe-ui --udid "$udid" > "$tree"
# not from research: --output as the screenshot path flag.
axe screenshot --udid "$udid" --output "$png"

[ -s "$png" ] || { echo "flow-step.sh: screenshot missing or empty: $png" >&2; exit 1; }
echo "step $step ($cfg): $png"
