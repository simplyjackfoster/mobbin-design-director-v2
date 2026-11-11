# Apply psychology to an observed design problem

Use when a named UX law, a change in learned behavior, choice/attention burden,
perceived responsiveness, or persuasive interaction is material to the task.
For an approved small edit, use the affected existing module and keep it small.
[The Laws of UX dossier](sources/laws-of-ux.md) supplies rationale and boundaries;
its 2024 second edition presents guidelines, not a replacement for user research.

## Make a mechanism testable

Start with the person's task and the observed difficulty or explicitly labeled
hypothesis. Explain what the proposed change makes easier to find, interpret,
reach, remember, decide, or recover from. Name the law only if it helps explain
that mechanism. Keep the strongest plausible alternative and what evidence would
change the recommendation. A citation or familiar product example is not proof.

| Trigger | Apply | Boundary / check |
|---|---|---|
| Familiar behavior changes (Jakob; LU-01–02) | Preserve useful mental models, explain new behavior at the point of use, and plan continuity during migration | Identify the actual audience's prior experience. Familiarity can preserve harmful conventions; test first use and returning use separately. |
| A control is difficult to acquire (Fitts; LU-03–04) | Inspect target size, distance, spacing, surrounding actions, and reachable placement | Visible size is not the hit region. Use [touch](touch.md) and current platform requirements; desktop edge benefits do not automatically transfer to fingers or spatial input. |
| People must recall or parse too much (Miller; LU-05–06) | Externalize needed context and form meaningful groups with recognizable labels | Seven plus/minus two is not a menu quota. Visible alternatives are not all held in memory; avoid arbitrary chunks that destroy useful relationships. |
| Choosing is difficult (Hick; LU-07–08) | Clarify distinctions, sequence dependent decisions, provide relevant search/filtering or an explainable recommendation | Fewer controls can mean more inference, navigation, or hidden costs. Compare total task effort, including experts and correction paths. |
| Entry varies in harmless ways (Postel; LU-09–10) | Accept equivalent formats and adapt to supported contexts while keeping output predictable | Define safe normalization versus semantic ambiguity. Do not guess a consequential date, amount, identity, or intent; show interpretation and allow correction. |
| A journey has painful peaks or an unclear ending (peak–end; LU-11–12) | Repair consequential moments and make completion, remaining work, and recovery clear | Remembered satisfaction differs from successful completion. Delight cannot compensate for loss, obstruction, or concealed failure. |
| Polish earns unusually positive reactions (aesthetic–usability; LU-13–14) | Preserve coherent expression and separately observe comprehension, errors, recovery, and task completion | A liking score does not establish usability; attractive presentation can mask reported difficulty. Do not remove approved personality without a task reason. |
| Important information competes for attention (Von Restorff; LU-15–16) | Reserve contrast for meaningful differences; use stable semantics and another channel beyond color | Everything cannot be exceptional. Inspect routine and exceptional states, reduced motion, and assistive access; a conspicuous destructive control may increase activation risk. |
| A simple-looking UI moves work elsewhere (Tesler; LU-17–18) | Track who interprets, enters, verifies, and recovers; absorb reliable mechanical work | Complexity conservation is a design lens, not a measurable invariant. Automation still needs uncertainty, control, correction, and a reachable manual path where required. |
| Waiting interrupts work (Doherty; LU-19–20) | Distinguish prompt acknowledgment from actual completion; use honest ongoing state and preserve work | 400 ms is not a universal release threshold. Measure real conditions; no fake progress, invented success, or deliberate delay to simulate effort. |

Read [cognition](cognition.md), [input](input.md), [flows](flows.md) or
[visual direction](visual.md) for the corresponding implementation work; this
module connects the explanation to the task rather than adding a separate process.

## Apply principles without turning them into quotas

For consequential decisions, capture one compact chain:
**observed fact / hypothesis → mechanism → change → exception → check**.
Use LU-21–22 when translating a general principle into a team convention: name the
scope, example and counterexample, and reassess after contradictory evidence.
The book's example three-choice and eighty-character team rules are not universal
limits. Do not assign all ten laws to every screen or require a workshop for a fix.

## Check whose outcome is being improved

For defaults, recommendations, prompts, retention loops and consequential choices,
ask whether the person can understand the consequence, decline, correct, stop,
and leave without misleading emphasis or disproportionate friction. Distinguish
useful reassurance from concealing uncertainty, and chosen engagement from time
captured by interruption or compulsion. Pair business measures with the user's
intended outcome, avoid collecting extra behavioral data merely to justify a
choice, and inspect effects on people outside the assumed ideal audience.
These are task-specific design questions, not a mandatory compliance ceremony
(LU-23–24).

Do not use a good final moment to excuse a harmful journey, a recommendation to
hide legitimate alternatives, or simplified input to conceal consequential
assumptions. If a meaningful commitment needs deliberation, use an explicit review
step that exposes the consequence; don't simulate computation to manufacture trust.

## Match verification to the claim

Source checks can establish parsing and state rules; runtime checks can exercise
acknowledgment, pending, success, failure, repeated input, cancellation and recovery.
Rendered inspection can reveal grouping, emphasis and hit-region layout. Claims
about learning, remembered experience, confidence, attention or user benefit need
appropriate participant evidence; an agent walkthrough only predicts risks.
Compare behavioral observations separately from preference and explain untested
conditions. Use [review](review.md), with current platform checks where applicable.
