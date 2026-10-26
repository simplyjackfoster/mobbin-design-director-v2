#!/usr/bin/env bash
# PreToolUse hook. Refuses a git add or git commit that would stage raster
# images outside evals/. Mobbin images and simulator captures stay out of Git.
# Exit 2 blocks the tool call and shows the message to the agent.
set -u
input="$(cat)"
cmd="$(printf '%s' "$input" | sed -n 's/.*"command"[[:space:]]*:[[:space:]]*"\(.*\)".*/\1/p' | head -1)"
case "$cmd" in
  *"git add"*|*"git commit"*) ;;
  *) exit 0 ;;
esac
root="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0
staged="$(git -C "$root" diff --cached --name-only 2>/dev/null; printf '%s' "$cmd" | grep -oE '[^ "]+\.(png|jpe?g|webp|gif|mp4)' || true)"
bad="$(printf '%s\n' "$staged" | grep -iE '\.(png|jpe?g|webp|gif|mp4)$' | grep -vE '^evals/|/evals/|\.claude-plugin/icon\.png$' || true)"
if [ -n "$bad" ]; then
  printf 'Blocked: raster files outside evals/ must not be committed:\n%s\n' "$bad" >&2
  exit 2
fi
exit 0
