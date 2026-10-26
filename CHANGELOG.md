# Changelog

## 3.0.0 (unreleased, branch claude/v3-craft)

Built from the 2026-10-23 assessment and ten research lanes. Nothing here has
been through `claude plugin eval` yet. Run the suite and record the baseline
before tagging.

Added
- `references/evidence.md`: the evidence rules stated once.
- `references/defaults-detector.md`: tool-default tells for web and iOS. A hit
  needs a stated reason or it changes.
- `references/ios-components.md`: task to native component, from the HIG as of
  iOS 27, the full 64-component catalog by group, the 2025 to 2026 what's-new
  list, and the rule that native is the floor: take the element for its
  behavior, then mold its look and feel to the product.
- Signature idea rule: the product, or each main flow, names one idea from
  outside stock iOS, its real source, and its adaptation. Hero screens show it.
  Utility screens stay plain. The review checklist asks for it, and
  `expressive-design` has a grader that fails a stock result.
- `references/ios-craft.md`: checkable behaviors tied to named apps and Apple
  guidance, with the unsourced apps listed as such.
- `references/worked-examples.md`: eight before-and-after cases that show the
  rules combining on real jobs, with Mobbin links where a shipped app shows the
  moment.
- `references/wwdc-digests.md` and `references/craft-digests.md`: the Apple
  sessions and designer essays the craft file cites, read in full and reduced to
  checkable rules.
- `references/ios-writing.md`: HIG writing and alert rules. Casing is per element
  type. Buttons and alert buttons are title case.
- `references/research.md`: Mobbin MCP rules (standard mode by default, credit
  budget, flow fetching, collection readback with consent, notice handling).
- `references/review.md`: the director's questions before any detail.
- `references/ios.md`: accessibility beyond labels, script pointers.
- `scripts/`: simulator capture loop (`sim-prepare.sh`, `sim-matrix.sh`,
  `flow-step.sh`), `proxy-grep.sh`, `diff-report.sh`, `swiftui_slop_lint.py`,
  `mobbin_cache.py`, `sheet.py --from-dir`, `vlm-review.md`,
  `principles_index.py`, `hig.py` (prints the current HIG page as text in one
  call, tested live). The shell scripts are untested on the authoring Mac.
- `evals/`: six craft cases, Mobbin mocks, fixed grader frontmatter.
- `.mcp.json`, `hooks/` (blocks committing rasters outside evals/),
  `agents/critic.md`.
- `plugin.json`: license, repository, keywords, hook, agent and MCP pointers.
- `agents/openai.yaml`: implicit invocation policy and the Mobbin dependency.

Changed
- `SKILL.md` rewritten as a spine: third-person description with triggers and a
  not-when clause, depth table that names the files to load, retain/improve/reject
  and the finding taxonomy inlined, Mobbin standard-mode rule, script table, both
  invocation paths.
- The two links that could load 18K and 65K tokens on one read are now code
  spans. `principles.json` is reached through `coverage.py search` or the
  one-line index.
- Version is 3.0.0 in `plugin.json`, `marketplace.json`, and `sync_local.py`.
  `validate.py` asserts they match.

Deferred, stated plainly
- Per-mode playbook tiering and a prose tightening pass over untouched modules.
  Lane 06 estimates 45 to 65 percent context savings. Do it after an eval
  baseline exists, so nothing is lost silently.
- Duplicate caveats in modules not touched by this release still stand. Remove
  them when each file is next edited.

Review dates
- Apple HIG pages last reviewed 2026-10-23 (iOS 27). Before that, 2026-10-21.

## 2.2.0 (2026-10-21)

Rewrite README to describe the skill and its source books.
