# Evaluate the experience and the implementation

Match review depth to changed behavior and uncertainty. Significant work needs
both interaction evidence and visual inspection. Routine changes need the relevant
checks, not a full study. Method rationale: [Inspection Methods](sources/inspection-methods.md)
and [The UX Book](sources/ux-book.md).

## 0. Ask the director's questions first

Answer these before any detail. They come from how Figma, Airbnb, and Apple
leads run critique (Dill, Zhuo, Baxley).

- Who arrived here, from where, with what on their mind?
- What must they feel and achieve on this screen?
- How high are the stakes? Higher stakes mean every detail is inspected.
- Does the whole flow cohere before any one screen is judged?
- Which tenet decides this call? A tenet decides a case. "Simple" does not.
- What shipped example proves the alternative? Show it, do not describe it.
- What is the product's signature idea, and where did it come from? A product
  with none reads as stock. Hero screens show it. Utility screens stay plain
  and carry it only through shared type, color, and spacing. An idea that
  breaks native behavior is a defect.
- Ask, do not direct. A question that exposes the problem beats an instruction.

## 1. Choose what the review can establish

Name the consequential claim before choosing a method. Specify the observation
that would support it, the conditions the method can reproduce, and what would
remain unknown. Repeatable scripted success, an owner's preference, participant
comprehension and continued use are different outcomes. Combining complementary
methods can answer more of the question; repeating the same inspection cannot.
Use early findings to change the design while changes remain cheap, and rerun the
affected scenario. This applies [ID-23 and ID-24](sources/interaction-design.md), ch. 14,
pp. 520–532 and 543–546; it does not require a formal study for routine work.

Choose the next check for the unresolved claim, not to maximize realism in every
dimension. Credible fixtures can support a comprehension or composition study;
live-service integration is needed when service behavior is the question. Do not
make a complete backend a prerequisite for evaluating a design prototype
([ID-17](sources/interaction-design.md)).

| Method | Use when | Evidence limit |
|---|---|---|
| Source/automated checks | Logic, regressions, structure, measurable rules | Passing code does not establish visual quality or real usability. |
| Runtime scenario check | Verify actions, states, recovery, and navigation | Proves exercised conditions, not every user/context. |
| Cognitive walkthrough | First-use or unfamiliar tasks | Predicts discoverability/learning risks from explicit user assumptions. |
| Visual inspection | Composition, type, coherence, polish | Expert judgment; a “five-second scan” by an agent is not a user test. |
| Independent perspective review | Consequential uncertainty or complex work | Reduces shared blind spots; agent agreement is not participant evidence. |
| Participant study | User explicitly requests/authorizes research | Reports observed tasks, participants, and limitations, not universal conclusions. |

## 2. Exercise the task

Use the surface's [iOS](ios.md) or [web](web.md) runtime path. Start from the real
entry context. Walk the primary scenario, then relevant correction, Back/Cancel,
interruption/resume, errors/retry, empty/partial states, and completion. Inspect
what is carried forward and whether the outcome is clear. Include a neighboring
screen or transition when a local change can affect it.

Record action, expected response, actual response, and evidence for important
checks. Distinguish fixture launches from actual transition tests. Do not infer
state persistence or responsiveness from static captures. If the toolchain is
missing, do useful source/spec inspection and state the exact runtime gap.

## 3. Inspect visual and accessible behavior

Open screenshots at useful device scale. Check hierarchy, grouping, rhythm, real
content, supported text sizes/appearances, and cross-screen character against the
brief. Examine relevant assistive interaction, focus, hit regions, keyboard, and
motion settings; record checks not exercised. Token audit is only a consistency
diagnostic, never a visual-quality score.

For a visual comparison use the same content, viewport, state, and scale. References
remain attributed. A combined image can help, but do not shrink away the detail
needed to judge. Preserve positive findings so later fixes do not erase strengths.

Record changed variables. A redesign that changes the offer, wording, information
or starting state cannot attribute its apparent improvement solely to typography
or layout. Owner calibration between two screens is not a randomized A/B study.
If real participant comparisons are authorized, account for order, learning,
prompts and sample limitations before interpreting performance differences.

## 4. Inspect independently when justified

Use [critic-prompt.md](critic-prompt.md) with a fresh reviewer and minimum relevant
artifacts. First give the task, audience assumptions, approved requirements,
flow/recording or runnable surface, screenshots, and known verification limits.
Withhold the implementer-generated checklist until the reviewer records an initial
assessment. Then provide the applicability ledger and acceptance criteria: ask what
was omitted, wrongly excluded, or weakly verified. Check criterion-to-method fit
and add missing scenarios before the final verdict.
Do not give the implementer's persuasive reasoning or desired verdict.

Relevant lenses include first-use discovery, returning-user efficiency,
accessibility, recovery, and visual craft. Combine lenses when the task is small.
Merge duplicates, resolve disagreements through evidence, and keep systemic causes
separate from repeated instances. Reviewers need not invent a minimum issue count.

## 5. Classify, fix, and report

Every consequential finding contains observed fact, affected task/state, evidence
or principle, kind, confidence, impact, and a feasible fix direction.

- **Verified defect:** reproduced behavior failure or observable violation of an
  applicable requirement/approved criterion. Cite the actual evidence.
- **Usability risk:** reasoned prediction tied to a user/task assumption and a
  principle. State the hypothesis and how to test it.
- **Aesthetic preference:** visual judgment or taste tradeoff; do not disguise it
  as a scientific requirement.

Severity reflects consequence: **critical** blocks a core task or creates serious
loss; **major** materially obstructs understanding/completion; **minor** is localized
friction or polish. Confidence is independently high, medium, or low with a reason.
A low-confidence risk can have high potential impact and need investigation.

Fix verified defects within scope, investigate major risks, and make routine
quality improvements autonomously. Bring consequential unresolved taste/product
choices to the owner. Re-run affected scenarios and look at the changed render;
repeat broader testing only when the change creates new uncertainty.

Report **verified for stated scenarios**, **partial verification**, or **blocked
on a named required capability/decision**. No unresolved critical defect may be
reported as a pass; major findings must be fixed or explicitly dispositioned.
Report accepted tradeoffs and untested conditions. Use [coverage](coverage.md) to
keep applicable checks traceable; its structural pass cannot establish evidence
quality, visual quality, or user success. Never say “users validated it”
or “fully accessible” based only on expert/automated checks.

## Participant testing, when requested

Define the question, relevant audience, realistic neutral task, initial state,
observations, and decision the results will inform. Avoid wording that teaches
the intended action. Observe behavior separately from interpretation and proposed
fixes. Compare success, misunderstanding, errors, recovery, and useful qualitative
responses; do not invent a sample or measured improvement. Recruitment and external
messages require the user's authorization.

Let the question and method determine the sample and measures; neither five
participants nor repeated agent runs is a universal sufficiency threshold. Record
denominators and consequential anomalies. Investigate outliers rather than removing
them by habit. Short sessions cannot establish long-term adoption or comfort.
These adaptations use [ID-12 and ID-25](sources/interaction-design.md), ch. 9 and 15–16; its illustrative
statistical explanations are not an analysis recipe.

When existing analytics informs a design, define the event, population, filter,
time window and denominator before comparing values. Short sessions can reflect
efficient completion or abandonment; logs alone do not establish motives. Link
metrics to the person's goal and investigate plausible rival explanations
([ID-27](sources/interaction-design.md)). This is an optional evidence path, not
authorization to install tracking or collect additional personal data.
