# Design context

Project settings for the `mobbin-design-director` skill. Keep this short.
Everything product-specific lives here and in `design-decisions.md` and
`design-taste.md`, never in the skill.

## Owner
**Design owner:** <name or role>. They make the taste calls.

## Product lens
<2–4 sentences: what the product helps people do, how it should feel, and
what it must not look like.>
Favour references that excel at: <e.g. explainability, dense but readable data>.
Strong sources outside the category: <e.g. fitness scores, travel pricing>.
Default checkpoint question: "Which feels most like <product>?"

## Surfaces
| Surface | Mobbin `platform` | Design system (source of truth) | Run and review |
|---|---|---|---|
| <e.g. iOS app> | `ios` | <token file / doc> | <e.g. simulator commands> |
| <e.g. web app> | `web` | <token file / UI guide> | <e.g. `pnpm dev`, widths 360/390/1280> |

Delete the rows you don't have. A product with one platform has one row.

Appearances supported: <light / dark / both>

## Files
- Decisions: `docs/design-decisions.md`
- Taste: `docs/design-taste.md`
- Research packets: `docs/research/<YYYY-MM-DD>-design-<topic>/README.md`

## Copy voice
<3–5 rules, e.g. "short plain words; no jargon; one job per line">

## Audience and evidence (optional)
Relevant behaviors, prior knowledge, frequency, context, and access needs:
Known user/product evidence and where it came from:
Working hypotheses and the questions they leave open:

## Success and collaboration (optional)
Task outcomes and meaningful validation criteria:
Runtime configurations and accessibility checks relevant to this product:
Default: adaptive depth; recommend a direction and use selective visual checkpoints.
Any explicit project-specific exception:
