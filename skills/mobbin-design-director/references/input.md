# Input, decisions, feedback, and recovery

Use for forms, selection, editing, permissions, transactions, or delayed work.
Sources: [Designing Interfaces](sources/designing-interfaces.md),
[Mind in Mind](sources/mind-in-mind.md), [About Face](sources/about-face.md).

## Ask for necessary work at an understandable moment

Explain unusual or sensitive requests in context. Use known information and
appropriate defaults when reliable and permitted; let people inspect and correct
them. Defer nonessential decisions. Do not assume all typing is bad: free text
can be the appropriate way to express something that choices cannot capture.

Choose input controls around data shape, task frequency, familiarity, and platform.
Use meaningful labels, units, examples where useful, and sensible keyboards/autofill.
Avoid forcing users to translate domain concepts into storage formats. Preserve
valid input when a field or request fails.

Keep field meaning available during entry; a disappearing placeholder is usually
insufficient as the sole label. Put essential constraints where people can find
them before an avoidable error, then check the focused state with the keyboard,
autofill and larger text. A familiar search field can be compact while retaining
an accessible name. Native layout can differ from a web example if the purpose
and help remain clear ([PU-21–23](sources/practical-ui.md)).

Choose validation timing for the constraint: do not flag unfinished typing as an
error prematurely. After an error, help people locate, correct and confirm its
resolution. Keep asynchronous replies from overwriting newer input. A syntax
check is not verified eligibility, a saved account or a completed transaction
([PU-24](sources/practical-ui.md)); the async state contract is our adaptation.

## Specify action → acknowledgment → outcome

For consequential actions distinguish:
- input accepted from work completed;
- draft from saved or submitted state;
- waiting from failure;
- partial success from complete success;
- cancellation requested from cancellation confirmed.

Provide honest progress and useful feedback near the affected object. Avoid
precise progress percentages without supporting data. Prevent duplicate submissions
where relevant, but do not freeze unrelated interaction merely because work is pending.

## Help people recover

Put errors where the person can connect them to the action, explain what happened
in useful language, and offer a feasible next step. Re-entry should not require
redoing unaffected work. Use prevention, preview, undo, confirmation, or explicit
commitment according to the consequence and actual system capabilities.

A confirmation is not a substitute for reversible design; undo is not a promise
unless the backend can honor it. Test retry/cancel against real request behavior
where implemented. Use deterministic failure fixtures when live failure is unsafe
or unreliable, and label the fixture-based evidence.

For touch interaction, use the [touch inspection](touch.md): distinguish visible
affordance from actual hit region, check nearby conflicting actions and obscured
feedback, and exercise repeat activation and correction.

## Decision support

Expose comparable attributes, totals, qualifications, and uncertainty at the
moment they matter. Do not hide important costs or constraints behind a visually
strong recommendation. Check labels, ordering, and defaults for accidental or
coercive choices. Completion should make the outcome and next destination clear.

Review with realistic long content, empty results, keyboard visible, validation,
slow response, failed response, repeated actions, and interruption where relevant.

An unavailable action needs a discoverable reason and a viable next step where
one exists. Do not enable an unsafe operation merely to avoid disabled styling.
Give equally legitimate choices comparable discoverability; a single-primary-action
heuristic must not conceal cancellation or manufacture the preferred answer
([PU-17–18](sources/practical-ui.md)).
