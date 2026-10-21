# Mobbin Design Director v2.2

A reusable design skill for **native iPhone and web**, shared by Codex and Claude
Code. It connects user goals, complete journeys, context-sensitive patterns,
Mobbin references, visual direction, implementation, and runtime evaluation.

It recommends a direction, calibrates consequential choices with the owner, and
handles routine details autonomously. Small approved edits stay fast. Major flows
use explicit state/transition design and independent review when available.

## What changed

- Retained lessons indexed by task triggers, exceptions, routes, and review questions.
- Proportional coverage and evidence checks, with independent review for omitted criteria.
- Hash-bound evaluation records and explicit partial verification; no checklist quality score.

- Eight source-backed book dossiers, chapter coverage ledgers, and a topic index.
- Interaction Design deepens conceptual models, emotional context, prototype fidelity and evaluation limits.
- Practical UI sharpens hierarchy, typography, grouping, color and input craft, with dated or context-specific prescriptions qualified.
- Touch ergonomics, real hit regions, occluded feedback, and mobile disclosure, with dated prescriptions qualified.
- Goals and scenarios before composition; state continuity and recovery before polish.
- Mobbin observations distinguished from user evidence and usability proof.
- Dedicated visual craft guidance, with coherent expressive design encouraged.
- Native iPhone and web implementation/review paths with current-platform checks.
- Verified defects, predicted usability risks, and aesthetic preferences reported separately.
- Useful evidence-limited work when Mobbin or a native runtime is unavailable.

The active entrypoint stays compact. Source PDFs and extracted text are not part
of the package. See [the source index](skills/mobbin-design-director/references/sources/README.md)
for editions, provenance, study coverage, and limitations.

## Repository

Maintained by `simplyjackfoster` as a standalone skill repository.

## Use

Codex: `$mobbin-design-director [mode] [ios|web] <task>`

Claude Code: `/mobbin-design-director [mode] [ios|web] <task>`

| Mode | Result |
|---|---|
| default | Adaptive design/build/review within the request |
| deep | Substantial journey/design loop and compact evidence packet |
| quick | Focused component or approved-design work |
| research | Findings, alternatives, recommendation, limitations; no product code |
| taste | Focused visual calibration |
| critique | Findings and verification limits; no implementation unless asked |

Product context, approved decisions, and taste remain in the project. Existing
`docs/design-context.md`, `docs/design-decisions.md`, and `docs/design-taste.md`
continue to work. New audience/evidence and success sections are optional. Missing
files do not block work; templates are in the skill's `templates/` directory.

## Local installation and synchronization

Keep this repository as the source of truth. Copy the skill into a host-discovered
skill directory; a shared `~/.agents/skills/mobbin-design-director` can be linked
from `~/.codex/skills/` and `~/.claude/skills/` where those environments use them.
Do not overwrite an existing installation without inspecting local changes.
The repository retains Claude plugin metadata and Codex UI metadata.

The stdlib sync helper validates the source, creates a backup, copies the skill,
and writes `SOURCE` with base commit and a content hash covering local changes:

```sh
python3 skills/mobbin-design-director/scripts/sync_local.py /path/to/skill-copy
python3 skills/mobbin-design-director/scripts/sync_local.py /path/to/skill-copy --apply --backup-dir /path/outside/repos/backups
```

The first command is a dry run. Symlink destinations are deliberately not followed;
inspect and synchronize their canonical target. No network or Git write is performed.
Keep product-specific rules outside the vendored skill. Align project instructions
with v2's recommendation style without changing approved product decisions.

## Validation

```sh
python3 skills/mobbin-design-director/scripts/validate.py
python3 -m unittest discover -s tests -v
```

Use the [coverage workflow](skills/mobbin-design-director/references/coverage.md)
to retrieve lessons and track task-specific checks. Routine approved edits stay light.

Structural checks cannot prove reading or design quality. Behavioral cases live in
`evals/`; see [the evaluation protocol](evals/README.md) for matched runs, evidence,
and runtime limitations. Run native/browser checks on actual artifacts. A generated
plan or static screenshot does not demonstrate a complete working journey.

## License

MIT for the original code and skill text; existing notices are preserved in
[attribution](skills/mobbin-design-director/references/ATTRIBUTION.md). Source books
are referenced intellectual sources and are not redistributed or relicensed.
