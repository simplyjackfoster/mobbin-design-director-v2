# Goals into flows and information architecture

Use before screen composition when multiple screens, states, or destinations are
involved. Keep an existing successful path unless the task calls for changing it.

## Model the task, then the interface

1. Write a context scenario without control names: trigger, situation, desired
   outcome, needed information, constraints. Include prior knowledge and likely
   interruptions as hypotheses when unobserved.
2. Identify the domain objects and relationships users need to understand. Use
   their vocabulary consistently across destinations, labels, errors, and help.
3. Separate destinations people revisit from actions they finish and contextual
   detail. Frequency, importance, and discoverability guide placement; do not force
   every product into the same tabs or put all account tasks behind an avatar.
4. Draw the key path as a wireflow, then the alternate paths relevant to the task.
   Arrows represent actions and responses, not just screen order.

For an unfamiliar product, make the conceptual model concrete before choosing
screen containers: what objects exist, what states they can occupy, which actions
change them, and how people can recognize those changes. A helpful metaphor can
aid initial understanding but should not imply operations or capabilities the
product lacks. Include meaningful handoffs and work outside the app; a screen's
success message is not necessarily completion of the person's goal. These are
operational applications of [Interaction Design](sources/interaction-design.md),
ID-02, ID-03 and ID-16 (ch. 3 and 12).

Use a Mermaid flow or this compact table:

| State / entry | What the person needs to know | Action → response / next state | Carried state | Escape / recovery |
|---|---|---|---|---|
| Name a concrete state | Visible information, question, consequence | Include pending and completion where consequential | Selection, input, position, context | Back, cancel, edit, retry, resume as applicable |

Do not expand every theoretical state. Mark genuinely irrelevant conditions briefly.

## Decisions to settle before implementation

- Where does the journey really start, including deep links or returning visits?
- What defines success, how is it recognizable, and where does the person land?
- What data is draft, saved, submitted, or irreversible? Who owns it?
- What do Back, interactive dismissal, Cancel, retry, and re-entry do to that data?
- What happens if input/network/permission is missing, results are partial, or the
  app is interrupted? Can the user correct a previous choice without restarting?
- Are explanatory context and earlier selections available when a later decision
  needs them? Is any cleanup incorrectly left until after apparent completion?

Distinguish reversible exploration from commitment. Avoid inventing backend
capabilities such as offline success, undo, or persistence that the project lacks.
When a needed behavior requires backend work, identify that dependency explicitly.

Describe prototype fidelity by dimension when it affects a conclusion: visual
detail, interaction behavior, real versus fixture data, persistence, external
services, and platform execution. A polished native prototype can still simulate
an entire service. Decide which dimension needs realism for the current question;
do not infer production readiness from visual finish or require a full backend to
evaluate a local layout. Rationale: [ID-17](sources/interaction-design.md),
pp. 451–455; these dimension labels are our implementation convention.

For a buildable behavior specification, answer those questions with a concrete
contract, not just a checklist. Name the edited value, last committed value, and
currently active effect when they differ; state which action changes each. For
example, a stored reminder-time draft is not proof that an existing reminder was
replaced. Define what remains active during editing and what acknowledgment makes
the new setting effective. Mark an unresolved dependency explicitly.

## Reduce imposed effort

Review repeated entry, forced decisions without enough information, navigation
detours, arbitrary modes, hidden arithmetic, unnecessary confirmations, and memory
demands. A familiar, slightly longer path may be easier than a compressed puzzle.
Wizards suit genuinely ordered or unfamiliar tasks; they can burden frequent
expert work. Let task dependencies decide, not the popularity of stepped screens.

## Early walkthrough

Before expensive polish, walk the scenario through the wireflow. At consequential
steps ask: will the intended user know what to do, notice the available action,
associate it with their goal, and understand the response? Record predicted
problems as usability risks, not observed participant failures.

Then add visual and behavioral acceptance criteria. Example:
“Changing banks preserves selected cards; cancel discards only this unsaved edit;
catalog failure exposes retry without removing the existing wallet.” Confirm the
product actually wants those semantics rather than adopting this example blindly.

Sources: [About Face](sources/about-face.md), [The UX Book](sources/ux-book.md),
[Designing Interfaces](sources/designing-interfaces.md),
[Inspection Methods](sources/inspection-methods.md).
