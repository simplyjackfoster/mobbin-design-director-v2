# Design for touch in real contexts

Use for native iPhone, touch web, dense selectable content, gestures, and consequential
nearby actions. This module operationalizes [Hoober's touch research and proposals](sources/touch-design.md)
with the other sources and current platform guidance. It is our synthesis, not a
claim that one book or one grip model supplies universal layout rules.

## Start with the task and physical context

Identify supported devices and actual use conditions: handheld or mounted,
portrait/landscape, one or two available hands, interruptions, lighting, keyboard,
and assistive input where relevant. People can change grip within a task. Do not
assign every person a permanent right-thumb zone, or treat a simulator pointer as
a finger. A phone on a stand may call for different checks from a carried phone.

Prioritize the content people must read and manipulate. Hoober's reported center
preference is a reason to examine content placement and interaction accuracy; it
is not a rule to move every primary action to the middle, discard native tabs, or
ignore someone who cannot comfortably reach a control. Preserve task, platform,
and accessibility evidence when it conflicts with a simplified zone diagram.

## Inspect three different things

- **Visible affordance:** what looks actionable, what is labeled, and what appears
  selected or disabled. An invisible hit-area extension cannot repair an ambiguous
  icon or an action that nobody notices.
- **Actual hit area:** the complete region that activates the intended action,
  including padding, clipping, overlays, and neighboring controls. Test boundaries
  and blank space within apparent buttons/rows. Check nested row/detail actions.
- **Obscured feedback:** what the hand, keyboard, or system chrome hides during the
  action. Keep the resulting state understandable after release; an animation under
  a finger cannot be the only indication that something changed.

Check near misses by consequence, not spacing alone. A harmless nonresponse differs
from deleting an item or submitting an irreversible choice. Separate conflicting
neighbors, support appropriate correction, and guard repeated activation while
acknowledgment or work is pending. Do not promise undo or cancellation the system
cannot perform. Preserve normal scrolling and system gestures when adding custom
interaction. Avoid blanket touch-coordinate offsets and unnecessary custom gestures;
justified specialized gestures need discoverable alternatives and must preserve
expected standard/system behavior.

## Keep units and standards explicit

Current guidance checked 2026-10-21:

- Apple's [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)
  recommends a general minimum hit region of 44 × 44 points and adequate surrounding
  space. Use current component and deployment-target guidance; inspect actual hit
  regions rather than assuming the icon's visual frame proves them. Apple's current
  Accessibility table separately lists 44-point default and 28-point minimum iOS
  control sizes; do not flatten these contexts into a universal size law or silently
  shrink primary hit regions. Reconcile the component and interaction being built.
- Apple's [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures)
  and [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
  support familiar gestures, responsive feedback, and alternative ways to perform
  actions. Essential functionality must not depend on a hidden precision gesture.
- Web checks use the actual adopted WCAG version/level. [WCAG 2.2 SC 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
  defines the 24 × 24 CSS-pixel minimum with explicit spacing and other exceptions.
  That is a conformance criterion, not a universal comfort target or a conversion
  from Apple's points. Larger targets can still be appropriate.

Physical millimeters in the book, platform points, CSS pixels, rendered screenshot
pixels, and device density are different quantities. Do not convert them with a
single universal multiplier or copy the book's historical conversion table. Record
measured geometry and units. A book's accuracy percentage does not certify this
product's error rate, and a compliant target does not establish comfortable use.

## Information and disclosure still matter

Make likely actions recognizable with content, labels, grouping, and clear states.
Retain expressive visual character while checking readability under the supported
text sizes, appearances, and relevant environmental conditions. Avoid universal
bans on color, dark mode, minimal controls, or animation based on one example.

Use disclosure when it preserves a comprehensible task and enough context to
choose well. Compare inline expansion, a detail destination, a native sheet, or a
persistent action area against the actual information and return contract. Fixed
controls can help orientation and also cover content or shrink the usable viewport.
Check the keyboard, large text, safe areas, and mobile browser chrome separately.
Do not adopt fixed tab counts, navigation depths, or a universal one-open-accordion
rule without a task reason.

## Make Mobbin answer the touch question

Search a specific decision: selecting rows while retaining detail access; correcting
a mistaken choice; revealing a secondary action; saving with the keyboard visible;
or reviewing a long selection before commitment. Use comparable native or mobile-web
flows and inspect equivalent states, including selected/expanded/keyboard states
when available. Compare which content and actions remain visible and recognizable.

Record what to retain, improve, or reject. A popular app's crowded controls are a
candidate weakness, not a pattern to copy. Screenshots can show visual separation
and wording; they cannot reveal exact hit rectangles, gesture arbitration, finger
occlusion during a real action, or accidental-activation rates. Carry those unknowns
into implementation checks. Do not infer screen size in millimeters from a capture.
If the evidence is incomplete, design from the task and platform guidance and test
the uncertain behavior instead of collecting more unrelated attractive screens.

## Verify the promise at the right level

Source inspection can establish configured hit regions and state contracts.
Automated runtime checks can exercise target boundaries, repeated actions, row/detail
separation, scrolling, correction, and continuity. For ordinary buttons or rows,
start a touch on the control, drag into a scroll or cancellation, and release
outside: verify that an aborted activation does not commit. Specialized drag
interactions need their own explicit completion/cancellation contract. Inspect the rendered result with
real labels and large text. On available real hardware, check relevant hand use,
occlusion, and environmental constraints; describe this as expert inspection unless
actual participant research was performed. A simulator cannot validate grip comfort.

For a consequential selector, a shared criterion might be: tapping the row's apparent
selection region changes only that row; opening detail preserves the selection;
rapid repeat activation cannot submit twice; returning from interruption preserves
the promised state. Record actual observations and failed/untested conditions.
Use the [coverage workflow](coverage.md) to connect these checks to source lessons
without creating a separate test for each overlapping principle.
