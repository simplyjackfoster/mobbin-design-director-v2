#!/usr/bin/env bash
# proxy-grep.sh: count the source proxies for haptics, sound and Liquid Glass in a Swift tree.
#
# UNTESTED on this author's Mac (no Xcode.app). Verify on a Mac with Xcode before relying on it.
# Haptics and sound have no simulator capture, so the source grep is the proxy (research/04
# step 8). Liquid Glass has no Apple audit; the research (step 9) says to grep the glass APIs
# and check that Info.plist does not set UIDesignRequiresCompatibility.
set -euo pipefail

usage() {
  cat <<'EOF'
usage: proxy-grep.sh <source-root>

Prints one table row per pattern with its match count across *.swift files,
then the UIDesignRequiresCompatibility check across *.plist and *.pbxproj.
A count is a pointer to read the call sites, not a pass or fail. Exit 0.
EOF
}

case "${1:-}" in
  "") usage >&2; exit 2 ;;
  -h|--help) usage; exit 0 ;;
esac
root="$1"
[ -d "$root" ] || { echo "proxy-grep.sh: $root is not a directory" >&2; exit 2; }

count() {
  # -F: the patterns hold dots and parentheses, so match them as fixed strings.
  grep -rF --include='*.swift' -c -- "$1" "$root" 2>/dev/null | awk -F: '{ n += $NF } END { print n + 0 }'
}

printf '%-32s %6s  %s\n' "pattern" "count" "proxy for"
printf '%-32s %6s  %s\n' "sensoryFeedback" "$(count 'sensoryFeedback')" "haptics (SwiftUI)"
printf '%-32s %6s  %s\n' "UIFeedbackGenerator" "$(count 'UIFeedbackGenerator')" "haptics (UIKit base class)"
# App code names the subclasses (UIImpactFeedbackGenerator, UINotificationFeedbackGenerator,
# UISelectionFeedbackGenerator), and the base class name is not a substring of those.
printf '%-32s %6s  %s\n' "FeedbackGenerator (any)" "$(count 'FeedbackGenerator')" "haptics (UIKit subclasses)"
printf '%-32s %6s  %s\n' "CHHapticEngine" "$(count 'CHHapticEngine')" "haptics (Core Haptics)"
printf '%-32s %6s  %s\n' "AudioServicesPlaySystemSound" "$(count 'AudioServicesPlaySystemSound')" "sound"
printf '%-32s %6s  %s\n' "glassEffect" "$(count 'glassEffect')" "Liquid Glass"
printf '%-32s %6s  %s\n' "GlassEffectContainer" "$(count 'GlassEffectContainer')" "Liquid Glass"
printf '%-32s %6s  %s\n' "buttonStyle(.glass" "$(count 'buttonStyle(.glass')" "Liquid Glass"
echo

# Modern projects generate Info.plist from build settings, so check the pbxproj too.
hits="$(grep -rlF --include='*.plist' --include='*.pbxproj' -- 'UIDesignRequiresCompatibility' "$root" 2>/dev/null || true)"
if [ -z "$hits" ]; then
  echo "UIDesignRequiresCompatibility: absent (the app opts in to the Liquid Glass design)"
else
  echo "UIDesignRequiresCompatibility: PRESENT. The app may be opted out of the Liquid Glass design. Found in:"
  echo "$hits" | sed 's/^/  /'
fi
echo
echo "Counts are proxies. Read each call site; a count says nothing about timing or intensity."
echo "Capture glass screens with Reduce Transparency, Increase Contrast and Reduce Motion on (research/04 step 9)."
