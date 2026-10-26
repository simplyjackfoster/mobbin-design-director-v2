#!/usr/bin/env bash
# sim-prepare.sh: put one iOS simulator into a known capture state, then relaunch the app.
#
# UNTESTED on this author's Mac (no Xcode.app). Verify on a Mac with Xcode before relying on it.
# Commands come from research/04 steps 2 and 3 ("nothing was run; all from docs").
# Lines marked "not from research" carry an argument the research did not state.
set -euo pipefail

usage() {
  cat <<'EOF'
usage: sim-prepare.sh <udid> <app-path> <bundle-id> [options]

Boots the simulator, installs the app, sets the capture environment, then
terminates and relaunches the app so the accessibility defaults take effect.

options:
  --appearance light|dark          default: light
  --content-size <name>            default: large
                                   (large, extra-extra-extra-large,
                                    accessibility-medium,
                                    accessibility-extra-extra-extra-large, ...)
  --increase-contrast on|off       default: off
  --reduce-motion on|off           default: off
  --reduce-transparency on|off     default: off
  --locale <id>                    e.g. de_DE; passed as -AppleLocale and -AppleLanguages
  --no-launch                      set state and install, do not launch
  -h, --help                       show this text
EOF
}

if [ "$#" -lt 3 ]; then
  usage >&2
  exit 2
fi

udid="$1"; app_path="$2"; bundle_id="$3"
shift 3

appearance="light"
content_size="large"
increase_contrast="off"
reduce_motion="off"
reduce_transparency="off"
locale=""
launch="yes"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --appearance) appearance="$2"; shift 2 ;;
    --content-size) content_size="$2"; shift 2 ;;
    --increase-contrast) increase_contrast="$2"; shift 2 ;;
    --reduce-motion) reduce_motion="$2"; shift 2 ;;
    --reduce-transparency) reduce_transparency="$2"; shift 2 ;;
    --locale) locale="$2"; shift 2 ;;
    --no-launch) launch="no"; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "sim-prepare.sh: unknown option $1" >&2; usage >&2; exit 2 ;;
  esac
done

for value in "$increase_contrast" "$reduce_motion" "$reduce_transparency"; do
  case "$value" in
    on|off) ;;
    *) echo "sim-prepare.sh: expected on or off, got $value" >&2; exit 2 ;;
  esac
done

bool() {
  # map on|off to the -bool value defaults(1) expects; the loop above validated the input
  if [ "$1" = "on" ]; then echo true; else echo false; fi
}

command -v xcrun >/dev/null || { echo "sim-prepare.sh: xcrun not found; install Xcode" >&2; exit 127; }

# Step 2: boot, install. "boot" fails when the device is already booted, so tolerate that.
xcrun simctl boot "$udid" 2>/dev/null || true
xcrun simctl bootstatus "$udid" -b
xcrun simctl install "$udid" "$app_path"

# Step 3: environment via simctl ui and the status bar override.
xcrun simctl ui "$udid" appearance "$appearance"
xcrun simctl ui "$udid" content_size "$content_size"
# not from research: the research names the increase_contrast verb, not its argument form.
if [ "$increase_contrast" = "on" ]; then
  xcrun simctl ui "$udid" increase_contrast enabled
else
  xcrun simctl ui "$udid" increase_contrast disabled
fi
xcrun simctl status_bar "$udid" override --time 9:41

# Step 3: no simctl verb for Reduce Motion / Reduce Transparency, so write the
# accessibility defaults and relaunch (research/04).
xcrun simctl spawn "$udid" defaults write com.apple.Accessibility ReduceMotionEnabled -bool "$(bool "$reduce_motion")"
# not from research: the Reduce Transparency key name. The research states only that
# the same defaults-write route is the way to set it. Confirm the key on a real Mac.
xcrun simctl spawn "$udid" defaults write com.apple.Accessibility EnhancedBackgroundContrastEnabled -bool "$(bool "$reduce_transparency")"

if [ "$launch" = "no" ]; then
  echo "prepared $udid: $appearance $content_size contrast=$increase_contrast motion=$reduce_motion transparency=$reduce_transparency (not launched)"
  exit 0
fi

# Relaunch so the defaults apply. terminate fails when the app is not running.
xcrun simctl terminate "$udid" "$bundle_id" 2>/dev/null || true
if [ -n "$locale" ]; then
  # Step 2: locale via launch arguments. -AppleLanguages takes a plist array literal.
  language="${locale%%_*}"
  xcrun simctl launch "$udid" "$bundle_id" -AppleLanguages "($language)" -AppleLocale "$locale"
else
  xcrun simctl launch "$udid" "$bundle_id"
fi
echo "prepared $udid: $appearance $content_size contrast=$increase_contrast motion=$reduce_motion transparency=$reduce_transparency locale=${locale:-default}"
