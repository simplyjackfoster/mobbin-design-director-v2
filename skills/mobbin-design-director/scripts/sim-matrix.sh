#!/usr/bin/env bash
# sim-matrix.sh: run one flow script across appearance x content size and collect captures.
#
# UNTESTED on this author's Mac (no Xcode.app). Verify on a Mac with Xcode before relying on it.
# The matrix follows research/04 step 6 (content size x style). Simulator state is set by
# sim-prepare.sh (steps 2 and 3). Each capture is named step-NN_<cfg>.png, where
# cfg = <appearance>-<content-size>; sheet.py --from-dir reads that name.
set -euo pipefail

usage() {
  cat <<'EOF'
usage: sim-matrix.sh <udid> <app-path> <bundle-id> <out-dir> <flow-script> [options]

For every appearance x content size, prepare the simulator, then run
<flow-script> with these variables exported:
  MDD_UDID       simulator udid
  MDD_BUNDLE_ID  app bundle id
  MDD_OUT_DIR    directory for this run's captures
  MDD_CFG        <appearance>-<content-size>, used in capture names
The flow script calls flow-step.sh once per step. Captures land in
<out-dir>/step-NN_<cfg>.png with the AXe tree beside each as .json.

options:
  --appearances "light dark"      space separated; default: light dark
  --sizes "<name> ..."            space separated; default:
                                  large extra-extra-extra-large
                                  accessibility-medium
                                  accessibility-extra-extra-extra-large
  --prepare-args "<args>"         extra sim-prepare.sh options, e.g.
                                  "--reduce-motion on --reduce-transparency on"
  -h, --help                      show this text
EOF
}

if [ "$#" -lt 5 ]; then
  usage >&2
  exit 2
fi

udid="$1"; app_path="$2"; bundle_id="$3"; out_dir="$4"; flow_script="$5"
shift 5

appearances="light dark"
sizes="large extra-extra-extra-large accessibility-medium accessibility-extra-extra-extra-large"
prepare_args=""

while [ "$#" -gt 0 ]; do
  case "$1" in
    --appearances) appearances="$2"; shift 2 ;;
    --sizes) sizes="$2"; shift 2 ;;
    --prepare-args) prepare_args="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "sim-matrix.sh: unknown option $1" >&2; usage >&2; exit 2 ;;
  esac
done

here="$(cd "$(dirname "$0")" && pwd)"
prepare="$here/sim-prepare.sh"
[ -x "$prepare" ] || { echo "sim-matrix.sh: $prepare is missing or not executable" >&2; exit 2; }
[ -x "$flow_script" ] || { echo "sim-matrix.sh: flow script $flow_script is missing or not executable" >&2; exit 2; }

mkdir -p "$out_dir"
runs=0
# shellcheck disable=SC2086  # the two lists are split on purpose
for appearance in $appearances; do
  for size in $sizes; do
    cfg="${appearance}-${size}"
    echo "== $cfg"
    # shellcheck disable=SC2086
    "$prepare" "$udid" "$app_path" "$bundle_id" --appearance "$appearance" --content-size "$size" $prepare_args
    MDD_UDID="$udid" MDD_BUNDLE_ID="$bundle_id" MDD_OUT_DIR="$out_dir" MDD_CFG="$cfg" "$flow_script"
    runs=$((runs + 1))
  done
done

count="$(find "$out_dir" -name 'step-*_*.png' | wc -l | tr -d ' ')"
echo "matrix done: $runs configurations, $count captures in $out_dir"
echo "next: python3 sheet.py --from-dir $out_dir sheet.html"
