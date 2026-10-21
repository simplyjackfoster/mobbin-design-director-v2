---
name: mobbin-design-director
description: Design, redesign, implement, or critique iPhone and web screens and complete user flows. Connect user goals, interaction design, Mobbin research, visual direction, and runtime review. Use for meaningful UI work, design options, UX inspections, and research-only requests; keep approved tweaks lightweight. Mobbin access is useful but not required.
---

# Mobbin Design Director

Design an experience people can understand, enjoy, and complete. Work from
**goals → journeys → relevant patterns → visual direction → build → evaluation**.
Native iPhone is the primary specialization; web gets its own interaction rules.

## Orient and choose depth

Read project instructions and the existing design context, decisions, and taste
files (defaults: `docs/design-context.md`, `docs/design-decisions.md`, and
`docs/design-taste.md`). Inspect the implementation before relying on an old doc.
Preserve approved decisions and working behavior; distinguish approvals from
agent defaults. If files are absent, infer what you can and use the optional
[templates](templates/design-context.md) when durable context would help.

Explicit task/platform instructions win, then current project evidence. Infer
iOS from native app targets and web from the actual frontend; a product can have
both. Ask only if the target genuinely remains ambiguous. iPhone-first does not
mean forcing iOS behavior onto web or assuming every iOS project is SwiftUI.

| Request | Work to do |
|---|---|
| Copy, bug fix, approved component adjustment | Apply the established design; check the affected behavior. No research packet, taste gate, or subagent by default. |
| New component or substantial screen | Focused framing, relevant research, composition, applicable states, runtime check. |
| New journey, navigation, major redesign, consequential uncertainty | Scenarios and wireflow, targeted references, visual direction, independent inspection, compact evidence packet. |

Scale effort by uncertainty and consequence, not screenshot counts. State the
chosen depth briefly. Read only the relevant modules from the
[topic index](references/index.md); do not load the entire source library.

## The working loop

1. **Frame the outcome.** Establish the person's goal, context, relevant prior
   knowledge, constraints, desired feeling, and success criteria. Use
   [goals and evidence](references/goals.md). Label unknowns as hypotheses; never
   manufacture interviews, personas, analytics, or participant findings. For substantial
   work, use [coverage](references/coverage.md) to select relevant lessons, scan all
   design areas, and separate requirements, contextual heuristics, and taste.
2. **Structure the experience.** For multi-step work, use
   [flows and IA](references/flows.md) before polishing screens. Map entry,
   actions, responses, information carried forward, completion, and relevant
   escape/recovery paths. Separate functional requirements from layout ideas.
3. **Research the open decisions.** Use [research](references/research.md) before
   Mobbin calls. Ask what references can actually answer; inspect relevant flow
   moments, record links and observation limits, and critique what to retain,
   improve, or reject. Familiarity and prevalence are evidence of a
   convention, not proof of usability. Stop when searches stop changing the
   decision. If access or evidence is missing, continue with named limits.
4. **Synthesize and recommend.** Use [synthesis](references/synthesis.md) to
   combine user evidence, book principles, platform guidance, observed patterns,
   and constraints. Explain the useful mechanism, fit, and tradeoffs, then carry
   it into build criteria. Improve on references where justified; guidelines
   inform judgment rather than set a ceiling. Check novel solutions against
   their assumptions and intended effects.
5. **Establish visual direction.** Use [visual direction](references/visual.md)
   and [taste](references/taste.md). Rank real decision content, compose a coherent
   direction, and give expression a useful role. Recommend it; bring the owner only consequential
   choices not already settled. Show alternatives on the same task/content,
   with one focused visual question. A checkpoint is not a universal approval
   requirement; respect existing authorization and requests for autonomy.
6. **Build the interaction and its expression.** Reuse the project system and
   deliberately extend it where needed. Apply [input and feedback](references/input.md)
   and the [iOS](references/ios.md) or [web](references/web.md) path. Resolve
   state/data ownership and transitions before dividing implementation work.
   Preserve meaningful personality; consistency alone does not make a design good.
7. **Evaluate the actual result.** Follow [review](references/review.md). Exercise
   scenarios, inspect rendered output, and verify relevant platform/accessibility
   behavior. Substantial work gets an independent
   [critic](references/critic-prompt.md) when delegation is available. Fix
   evidenced defects, test the changed path, and expose remaining uncertainties.
   Link applicable criteria to evidence; have the critic check for omitted criteria
   after independently inspecting the task. A completed checklist is not proof of UX.
8. **Record outcomes.** Save approved decisions, contextual taste evidence, and
   important unresolved risks. Significant work uses the
   [packet template](templates/design-packet.md); routine changes do not need it.
   Owner choices, agent defaults, and hypotheses remain distinguishable.

## Useful constraints

- Research explains choices; it does not authorize unrelated product changes.
- A screenshot cannot establish latency, state persistence, accessibility, or
  unseen branches. Mark these unknown until exercised or otherwise verified.
- Do not copy a reference's screen or average references into a collage. Transfer
  the useful principle into the project's content, behavior, and visual language.
- A rule violation, a predicted usability risk, and an aesthetic preference are
  different findings. Confidence and impact are separate dimensions.
- Native chrome and native behavior must be evaluated natively. A web prototype
  can explore content but cannot validate native materials, gestures, or semantics.
- An AI walkthrough is expert inspection, never a participant study. Report what
  was checked, how, and what was not. Missing tools reduce the verification claim.
- Keep product-specific taste out of this reusable skill. Keep copyrighted source
  PDFs, raw book text, and temporary reference images out of Git.

## Invocation and delegation

Codex: `$mobbin-design-director [mode] [ios|web] <task>`.
Claude Code: `/mobbin-design-director [mode] [ios|web] <task>`.
Natural-language requests work too; explicit user scope controls all modes.

| Mode | Meaning |
|---|---|
| default | Adapt depth to the request; design through implementation when requested. |
| `deep` | Full relevant journey/design/review loop and evidence packet. |
| `quick` | Focused component or established-design pass; avoid unnecessary ceremony. |
| `research` | Evidence, options, recommendation, and validation gaps; no product code. |
| `taste` | Focused visual calibration using comparable alternatives. |
| `critique` | Inspect existing work; report findings without implementing unless asked. |

For complex work, use [agents and environments](references/agents.md): one lead,
bounded researchers/implementers, and independent review. Do not spawn a team for
routine work or assume a tool or model exists. Discover the session's capabilities.

The [source index](references/sources/README.md) links original distilled lessons
and honest chapter coverage. Book examples inform reasoning; current platform
documentation and the project's deployment target govern implementation details.
