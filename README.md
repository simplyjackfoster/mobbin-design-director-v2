# Mobbin Design Director

An agent skill that works like a design director for **native iPhone and web**
products. It runs in Claude Code and Codex. Give it a screen, a flow or an
existing design, and it takes the work from user goals to a built, reviewed
result:

**goals → journeys → relevant patterns → visual direction → build → evaluation**

It researches real apps on [Mobbin](https://mobbin.com) when that connector is
available, grounds its choices in eight interaction-design books, recommends a
direction instead of listing options, and checks the running result rather than
trusting a static mockup. Mobbin is useful but not required.

## What it does

- **Frames the outcome first.** It works out who the person is, what they are
  trying to do and what success looks like before laying anything out. Unknowns
  are labelled as hypotheses. It never invents interviews, personas or analytics.
- **Designs the journey, not just the screen.** Multi-step work gets entry points,
  actions, responses, carried-forward information, completion and recovery paths
  before any polish.
- **Researches with intent.** Mobbin searches answer specific open decisions. What
  it sees there counts as evidence that a convention exists, not proof that it is
  usable. It records links and the limits of what it observed, then says what to
  keep, improve or reject.
- **Recommends, with tradeoffs.** It combines user evidence, book principles,
  platform guidance and observed patterns into one recommendation. Only
  consequential taste calls go to the owner, as a short visual checkpoint.
- **Treats visual craft as real work.** Hierarchy, type, color, grouping, imagery
  and motion are designed on purpose. Expressive design is encouraged when it
  serves the task.
- **Builds natively.** Separate implementation paths for iPhone (HIG, system chrome,
  touch ergonomics) and web (responsive layout, routing, keyboard and browser
  behavior). It reuses the project's own design system.
- **Evaluates honestly.** It walks the real scenarios in a simulator or browser. On
  substantial work an independent critic reviews the result. Verified defects,
  predicted usability risks and aesthetic preferences are reported separately, and
  it says what was not checked.
- **Scales its effort.** A copy fix or an approved tweak stays quick. A new journey
  or a major redesign gets the full loop and a compact evidence packet.

## The books behind it

The method draws on eight books. Each has a dossier in
[`references/sources/`](skills/mobbin-design-director/references/sources/README.md):
an original, decision-oriented summary of lessons with principle IDs, plus a
coverage file recording chapter-by-chapter reading, exclusions and figure checks.

| Book | Authors | Edition | Best for |
|---|---|---|---|
| [The UX Book](skills/mobbin-design-director/references/sources/ux-book.md) | Rex Hartson, Pardha Pyla | 2nd, 2019 | Process, discovery, modeling, emotional experience, prototyping, evaluation |
| [About Face](skills/mobbin-design-director/references/sources/about-face.md) | Alan Cooper, Robert Reimann, David Cronin, Christopher Noessel | 4th, 2014 | Goals, personas and scenarios, conceptual models, flow, excise |
| [Designing Interfaces](skills/mobbin-design-director/references/sources/designing-interfaces.md) | Jenifer Tidwell, Charles Brewer, Aynne Valencia | 3rd, 2020 | Patterns in context, information architecture, navigation, input |
| [Designing with the Mind in Mind](skills/mobbin-design-director/references/sources/mind-in-mind.md) | Jeff Johnson | 2nd, 2014 | Attention, perception, memory, learning, decisions, responsiveness |
| [User Interface Inspection Methods](skills/mobbin-design-director/references/sources/inspection-methods.md) | Chauncey Wilson | 1st, 2014 | Walkthroughs, independent inspection, evidence and its limits |
| [Touch Design for Mobile Interfaces](skills/mobbin-design-director/references/sources/touch-design.md) | Steven Hoober | 2021 | Grip, real hit regions, occlusion, neighboring actions, mobile disclosure |
| [Interaction Design: Beyond Human–Computer Interaction](skills/mobbin-design-director/references/sources/interaction-design.md) | Yvonne Rogers, Helen Sharp, Jennifer Preece | 6th, 2023 | Conceptual models, emotional and contextual interaction, prototype fidelity |
| [Practical UI](skills/mobbin-design-director/references/sources/practical-ui.md) | Adham Dannaway | 2nd, 2024 | Hierarchy, color, typography, grouping, controls and forms |

The lessons are collected in a registry of 184 principles
([`principles.json`](skills/mobbin-design-director/references/principles.json)),
each with its triggers, exceptions and review questions. A
[coverage workflow](skills/mobbin-design-director/references/coverage.md) uses it to
pick the lessons that apply to a task and track the evidence for each.

Where the books disagree (expert speed vs novice learnability, consistency vs a
useful exception, expression vs attention), the skill keeps the disagreement and
explains the tradeoff for the audience at hand. Dated platform, security and
numeric advice from the books is checked against current guidance before it is
applied.

The dossiers are paraphrases and applications in this repo's own words. No PDF,
extracted book text or book image is included. See
[attribution](skills/mobbin-design-director/references/ATTRIBUTION.md).

## Repository layout

```
skills/mobbin-design-director/
  SKILL.md            compact entrypoint: the working loop and modes
  references/         topic modules (goals, flows, cognition, research, synthesis,
                      visual, taste, input, touch, ios, web, quality, review,
                      critic prompt, agents), loaded only as needed via index.md
  references/sources/ book dossiers and coverage manifests
  templates/          design-context, design-decisions, design-taste, design-packet
  scripts/            coverage.py, validate.py, sheet.py (contact sheets),
                      token-audit.js (web style audit), sync_local.py
  agents/openai.yaml  Codex UI metadata
evals/                behavioral eval cases with graders
tests/                unit tests for the scripts
.claude-plugin/       Claude Code plugin and marketplace metadata
```

## Use

Codex: `$mobbin-design-director [mode] [ios|web] <task>`

Claude Code: `/mobbin-design-director [mode] [ios|web] <task>`

Plain-language requests work too.

| Mode | Result |
|---|---|
| default | Adapts depth to the request; designs through implementation when asked |
| deep | Full journey, design and review loop, with a compact evidence packet |
| quick | Focused component or approved-design work |
| research | Findings, alternatives, a recommendation and limitations; no product code |
| taste | Focused visual calibration with comparable alternatives |
| critique | Findings and verification limits; no implementation unless asked |

### Project context

Product-specific context stays in the project, not in this skill. The skill reads
`docs/design-context.md`, `docs/design-decisions.md` and `docs/design-taste.md`
when they exist. Approved decisions are respected, and agent defaults are kept
distinct from owner approvals. Missing files don't block work. Starter versions
are in [`templates/`](skills/mobbin-design-director/templates/).

## Install

Keep this repository as the source of truth and copy the skill into a directory
your agent discovers. A shared `~/.agents/skills/mobbin-design-director` can be
linked from `~/.codex/skills/` and `~/.claude/skills/`.

The sync helper (standard library only) validates the source, backs up the
destination, copies the skill and writes a `SOURCE` file with the base commit and
a content hash:

```sh
# dry run
python3 skills/mobbin-design-director/scripts/sync_local.py /path/to/skill-copy
# apply
python3 skills/mobbin-design-director/scripts/sync_local.py /path/to/skill-copy --apply --backup-dir /path/outside/repos/backups
```

It does not follow symlinked destinations and performs no network or Git writes.
Inspect an existing installation for local changes before overwriting it.

## Validation

```sh
python3 skills/mobbin-design-director/scripts/validate.py
python3 -m unittest discover -s tests -v
```

These are structural checks. They can't prove reading depth or design quality.
Behavioral cases live in [`evals/`](evals/README.md), which covers matched runs,
evidence and runtime limits.

## License

MIT for the original code and skill text. Third-party notices are preserved in
[attribution](skills/mobbin-design-director/references/ATTRIBUTION.md). The source
books keep their own copyrights. They are cited as intellectual sources and are not
redistributed or relicensed, and citing them doesn't imply endorsement by their
authors or publishers.
