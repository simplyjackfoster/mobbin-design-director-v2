# Make the relevant guidance hard to miss

Use this alongside the design packet for substantial screens and journeys. An
approved routine edit needs the affected behavior checked, not a generated ledger.
The [registry](principles.json) indexes every retained source lesson; it is a
retrieval aid, not a command to apply every principle or a claim of complete UX
knowledge. Read relevant source cards for rationale, context, and exceptions.

## Select, then challenge the selection

1. Frame the requested deliverable and current project decisions. Separate binding
   **requirements** (explicit user/project constraints or adopted standards), contextual **heuristics**,
   and **preferences**. A book or platform recommendation does not become a binding rule merely by
   being published; identify the actual requirement and its scope.
2. Choose depth and task tags, then retrieve candidate lessons. The eight core
   candidates address goals, context, flow, effort, accessibility, and evaluation;
   they still require contextual judgment. A tag match is not applicability.
3. Scan all ten areas once: goals, flows, cognition, content, visual, accessibility,
   recovery, platform, research, evaluation. Consider information missing from the
   brief, including touch/reach, localization, interrupted work, and cross-device
   continuity where relevant. Explicitly exclude irrelevant areas with a reason.
4. For each candidate, apply it, justify a departure, explain non-applicability,
   or keep it unresolved/deferred. Add relevant lessons missed by the tags. Record
   conflicts and tradeoffs; do not resolve them by counting agreeing books/apps.
5. Turn applicable guidance into observable criteria for this task. One scenario
   or visual inspection may cover several lessons: reuse its criterion/evidence,
   rather than running a separate test per principle. Keep the human packet short.

For example, a card-selection journey may require “after interruption, selected
cards remain selected and the return destination is clear.” Test the transition
and restored state. A still image can support hierarchy judgment but cannot
establish that persistence. A touch-target measurement also cannot establish that
an action is comfortable in every grip or discoverable to a first-time user.

## Optional machine-readable companion

For substantial work that benefits from repeatable omission checks, keep a small
`brief.json` and `coverage.json` beside the human design packet. Do not put private
product evidence into the reusable skill repository. Commands run from the skill
folder; Python 3.9+ and the standard library are sufficient.

```sh
python3 scripts/coverage.py search interruption recovery
python3 scripts/coverage.py show UX-11 DI-03
python3 scripts/coverage.py init --brief brief.json --out coverage.json
python3 scripts/coverage.py check coverage.json
python3 scripts/coverage.py hash evidence/run.md
python3 scripts/coverage.py check coverage.json --require-verified
```

`search` returns at most eight ranked pointers; `show` retrieves up to eight exact
source cards with their original rationale, exceptions, and locators. Use this
instead of loading every dossier. Search is lexical, so try synonyms and check the
area scan for relevant lessons it may miss.

Minimal brief (use actual task context and tags):

```json
{"summary":"Design an interrupted first-use setup flow", "platform":"ios", "depth":"journey", "mode":"design", "tags":["onboarding","interruption","input"]}
```

`platform`: ios / web / mixed / unspecified. `depth`: routine / screen / journey.
`mode` describes the requested deliverable: build / design / research / critique.
The skill's `taste` invocation maps to design; `quick` and `deep` control depth,
not whether implementation was requested. Research and design do not require a
runtime pass for an implementation that was never in scope.

Tags: core, onboarding, navigation, selection, comparison, input, persistence,
interruption, permissions, errors, latency, content, visual, motion, accessibility,
localization, data, expert, discovery, evaluation, implementation, touch. Choose actual
uncertainties, not every tag. `init` refuses overwrite and creates unresolved
candidates, never pre-approved passes.

The generated file contains:

- `domains`: each area's applicability, reason, and applicable principle/requirement
  IDs. Use `applicable`, `not_applicable`, or `unresolved`.
- `guidance`: ID, disposition, reason, criterion, verification. Dispositions are
  `applied`, `departed`, `not_applicable`, `deferred`, `unresolved`.
- `requirements`: task-specific rows with an `id` starting `REQ-`, `kind` (requirement / heuristic /
  preference), `origin`, criterion, disposition, reason, and verification. Capture
  actual user/project/platform constraints here; never silently waive one.
- `artifacts`: evaluated source/spec files, each `{ "path": "relative/path", "sha256": "…" }`.
- `review`: status `not_requested`, `pending`, or `completed`, plus evidence.
- `registry_sha256`: exact registry used; a changed registry requires re-assessment.

A verification object has `status` (not_verified / pass / fail), `method` (source /
 runtime / visual / participant / inspection), `evidence`, and `limit`. Each evidence
item has a relative file `path`, an exact `sha256`, and a specific `observation`.
Paths resolve from the coverage file; `../` is allowed for neighboring project
artifacts. URLs, directories, absolute paths, and the coverage file itself are not
file evidence. Record external source links and their observed content in a local
research note; do not mislabel that note as runtime evidence.

A pass needs an actual criterion and evidence. A hash binds a file's bytes; it does
not establish that its content is truthful, relevant, or sufficient. The lead and
reviewer must check **method fit**: runtime evidence for transitions, native checks
for native behavior, inspected renders for visual judgment, and real participants
for participant claims. If the capability is missing, record the exact gap and
keep implementation verification partial. Do not relabel an unperformed runtime
check as a successful inspection to satisfy the validator.

`check` accepts a structurally honest partial packet while listing its blockers.
`--require-verified` additionally rejects unresolved/deferred work, failed or
unperformed applicable checks, pending review, and departed binding requirements.
Nonroutine claims require at least one applicable passing criterion, with active
criteria linked to an applicable design area; marking
everything irrelevant cannot establish verification. Nonroutine build/design/critique
claims also bind evaluated artifact hashes. This
checks the record, **not the quality of the experience**. A checked research report
is verified only as a research deliverable; it does not validate a product.

When artifacts or evidence change, re-run affected checks, inspect the new output,
and only then update hashes. Never simply restamp a stale packet. If the registry
changes, compare candidate selection and source changes; preserve prior decisions
and re-assess affected rows rather than discarding unresolved work.

## Independent omission review and learning

For substantial work, follow the two-stage [critic prompt](critic-prompt.md).
First review task/artifacts without the implementer's checklist or persuasive
rationale. Then compare the checklist to that independent assessment: what should
have been tested but was absent, wrongly excluded, or weakly evidenced? Add missing
criteria and re-run affected checks. Broad tag unions can retrieve many candidates;
use the concise human packet when a machine ledger adds more work than value.
Keep the area scan, shared criteria, and explicit consequential departures either way. Review agreement is still expert inspection.

When a miss recurs, keep a small failure record: trigger, observed consequence,
source/criterion, and reproduction. Classify the cause as a source gap, retrieval
routing gap, application error, or verification gap. Fix the narrow lesson/tag/
workflow and add a realistic regression case; re-run affected cases and the routine
edit case. Do not turn one product preference into a universal prohibition. New
book lessons need provenance and contextual review before joining the registry.
