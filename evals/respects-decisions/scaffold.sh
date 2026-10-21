#!/usr/bin/env bash
# Seeds a project with locked design decisions for the eval.
set -euo pipefail
mkdir -p docs
cat > docs/design-decisions.md <<'MD'
# Design decisions
## Decided
- 2026-09-01 Light only. No dark mode, including dark "moments".
- 2026-09-01 No coloured boxes behind answers; answers sit unboxed on the page.
## Rejected
- 2026-09-01 Gradient hero headers
MD
