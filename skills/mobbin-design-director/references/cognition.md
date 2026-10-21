# Cognition and clarity

Use these as context-dependent questions, not numerical laws. Source rationale:
[Designing with the Mind in Mind](sources/mind-in-mind.md),
[Designing Interfaces](sources/designing-interfaces.md), and
[About Face](sources/about-face.md).

| Trigger | Design response | Review question / boundary |
|---|---|---|
| The intended action is missed | Align language, location, and emphasis with the current goal | Would someone pursuing this task notice it? High contrast alone does not ensure attention. |
| Content feels dense or disconnected | Use proximity, alignment, similarity, headings, and whitespace to express actual relationships | Does visual grouping match meaning? More cards or more whitespace is not automatically clearer. |
| Later decisions depend on earlier information | Externalize selections, context, units, constraints, and consequences | What must the person remember or mentally calculate? Avoid repeating everything indiscriminately. |
| Frequent actions are hard to discover | Make the path recognizable; provide shortcuts as additional paths | Can a newcomer complete the task without knowing a hidden gesture? Expert tools may intentionally optimize learned use. |
| A flow is short but confusing | Reduce interpretation and context switching before reducing taps | Does each action have an understandable effect? One giant form can be harder than a few meaningful stages. |
| Labels expose system internals | Use a stable domain vocabulary and conceptual model | Does the same object/action keep the same name across UI, feedback, and help? |
| Comparisons require hidden arithmetic | Align meaningful dimensions, totals, units, and qualifications | Can the decision be made from what's visible? Do not fabricate unavailable data. |
| Color carries meaning | Add text, shape, position, or another suitable channel | Is the meaning retained without hue and under supported contrast conditions? |
| Small or crowded controls cause mistakes | Match visible and actual hit regions; separate competing actions | Check on touch hardware/simulator; desktop edge-target arguments do not transfer mechanically. |
| Waiting feels broken | Acknowledge input, show honest ongoing status, preserve context | Can users tell accepted input from completed work? Avoid fake precision in progress. |
| Learned behavior is disrupted | Preserve predictable placement, terminology, and action effects | Is the benefit of change worth relearning? Consistency must not preserve a harmful design forever. |
| User finishes the apparent goal before essential cleanup | Integrate required work before completion or handle it automatically | Is anything vital left to remember after the task seems done? |

Use these to explain a concrete observed fact or a clearly identified hypothesis.
Do not diagnose users from screenshots, invoke “cognitive load” without specifying
the actual burden, or turn historic timing/memory examples into current thresholds.

Do not turn short-term-memory experiments into a maximum number of visible menu
items. Visible, meaningful alternatives can be inspected without remembering
every item. Recognition is also not universally better than entry: a person who
knows an exact name may benefit more from search than from a long picker. Choose
from vocabulary, familiarity, data size and correction needs. [Interaction Design
ID-05 and ID-08](sources/interaction-design.md), pp. 115–116 and 207–208, makes
these boundaries explicit.
