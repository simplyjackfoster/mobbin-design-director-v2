# Visual direction and emotional character

A useful interface can also feel distinctive and pleasurable. Define a governing
idea that serves the task and experience goal, then develop a coherent visual
language across the journey. These are design judgments, not universal scientific
rules. Rationale: [Designing Interfaces](sources/designing-interfaces.md),
[About Face](sources/about-face.md), [The UX Book](sources/ux-book.md).

## Compose with real content

Use realistic text, numbers, image proportions, and long/short content early.
Specify what the eye should encounter first, what follows, and which action or
information should remain available. A single dominant element can be useful;
comparison and expert work may require a balanced field instead.

| Lever | Decide deliberately | Check in the result |
|---|---|---|
| Typography | Role, scale, weight, rhythm, brand character | Hierarchy survives real content and text scaling; custom type remains legible. |
| Space and density | Related groups, section rhythm, reading/action sequence | Space expresses relationships; compactness and calm are both legitimate. |
| Color and contrast | Semantic meaning, identity, emphasis, supported appearances | Meaning survives without hue; color does not compete with the task. |
| Geometry and surfaces | Alignment, shape language, grouping, layering | Containers explain relationships rather than decorate every item. |
| Imagery and illustration | Information, recognition, emotion, storytelling | Assets earn attention; repeated generic embellishment does not crowd the task. |
| Motion and haptics | Feedback, continuity, pacing, character | Interaction stays responsive; reduced-motion alternatives retain meaning. |
| Content and voice | Terminology, tone, reassurance, consequence | Copy helps act or understand; personality fits the moment. |

Do not impose universal bans on cards, gradients, shadows, display typography,
illustration, or celebration. A purposeful treatment can be right. Diagnose a
specific failure: competing hierarchy, illegible text, misleading affordance,
inconsistent grouping, needless delay, or conflict with the product's direction.

## Develop comparable alternatives

When a consequential direction is open, explore a small number of meaningfully
different compositions. Hold content and task fixed. Use owner references and
research to identify qualities, not to assemble a header/list/chart collage.
Describe the relationship being explored: contrast between text roles, rhythm
within/between groups, content-to-image balance, or changing emphasis at an
important moment. Separate observed composition from inferred fonts, tokens,
hit areas, and motion. A screenshot is not an implementation specification.
Abstract studies can explore character; bring viable directions onto representative
content before judging fit. Improve weak reference execution while preserving
useful character, and inspect a neighboring or contrasting state when relevant.
Recommend one and show the visual tradeoff using [taste](taste.md).

Review the family of screens together: shared composition, navigation, type,
feedback, and content vocabulary should support orientation. Allow deliberate
variation for different screen roles and moments of emphasis.

## From direction to craft

When asked for a buildable spec without an existing system, resolve the material
choices into a small usable set of type, spacing, color, and component values.
Describe the intended appearance of real content and action states. A mood name
or palette adjectives alone leave too much to a later implementer; avoid inventing
a large token library when a few deliberate choices suffice.

At actual device size, refine alignment, line wrapping, optical balance, asset
quality, hierarchy, empty/populated states, pressed/selected states, and transitions.
Look at a real render after each meaningful correction. Counts of rendered styles
can reveal drift; they cannot measure beauty or authorize removal of character.

### Build hierarchy from the decision

Before picking sizes or containers, rank the real content by the person's current
decision: essential object/action, evidence or qualification needed to use it,
then supporting context. Translate that order through a deliberate combination
of position, scale, weight, contrast and spacing. A count or headline should not
dominate merely because it is easy to make large. Comparison tasks may need equal
emphasis across relevant alternatives rather than a single hero.

Keep an object's label, value, unit, period and status visually associated. Use
tighter internal spacing than the gap to an unrelated group; a consistent spacing
scale alone does not establish the relationship. Use containers where they clarify
ownership or interaction, and simpler alignment/spacing where that already works.
Distinguish static status and illustration from controls: a noninteractive icon or
badge that resembles an adjacent button sends a conflicting signal.

Inspect the result at device size and in a reduced-detail view to judge prominence,
then return to readable detail to check meaning, labels and accessibility. A squint
test diagnoses visual competition; it cannot establish comprehension or contrast
compliance. When learning from a before/after example, identify which variables
changed, what content is held equal and what the example does not test. Do not
copy its numerical grid, typography or button placement as a platform requirement.

These adaptations draw on [Practical UI PU-02 and PU-08–10](sources/practical-ui.md),
pp. 63–64, 164–186 and 194–200. Its examples explain mechanisms; their checkmarks are not user-study
results for the current product.

### Preserve meaning through visual refinement

Keep price, unit and period together, using a shared baseline where it helps
reading. With long labels, preserve the portion that distinguishes the objects;
identical truncated prefixes can defeat an otherwise clean list. Test these with
real strings and supported text sizes, not just a short ideal specimen
([PU-10 and PU-11](sources/practical-ui.md), pp. 207–209 and 216).

Test text and controls against their actual composited backgrounds, including
transparency and overlapping surfaces. Isolated palette swatches do not establish
rendered contrast. A consistent action color can clarify interaction while other
brand colors remain available for illustration and identity. Do not turn this into
a one-color limit or a universal ban on pure black ([PU-04–06](sources/practical-ui.md),
pp. 79–106 and 127–138).

Use the project's applicable contrast requirements. Do not replace an adopted
standard with an experimental metric because an older book prefers it. As checked
2026-10-21, [WCAG 3](https://www.w3.org/TR/wcag3/) is a Working Draft with the
contrast algorithm undetermined; [WCAG 2.2](https://www.w3.org/TR/WCAG22/) remains
a W3C Recommendation. APCA can inform additional investigation, not waive the
project's requirement. Native details also follow [the iOS path](ios.md).

### Give expression a role across the journey

Specify what character should contribute at a particular moment: orientation,
explanation, identity, reassurance or recognition of a real outcome. Consider
immediate appearance, the experience while acting, and the impression after
repeated use separately. A cheerful first visit does not prove a repeated prompt
will stay welcome. Match tone to the actual state, especially uncertainty or loss.

Separate a passive resident character, a user-invoked guide and unsolicited
assistance. They have different attention costs; criticism of an interrupting
assistant does not justify banning all resident mascots. Keep help dismissible or
correctable when its assumptions can be wrong. Ensure appearance and language do
not imply knowledge, agency or emotional understanding the product lacks.

Preserve useful personality while keeping the task legible. During a failure,
truthful status and a clear recovery action remain prominent; an expressive image
must not substitute for either. Evaluate attractiveness, perceived trust and actual
task success separately. These are our operational applications of [ID-03 and
ID-06](sources/interaction-design.md), ch. 6 (pp. 172–195) and ch. 12 (pp. 461–462), not prescribed
mascot placements or evidence that a particular audience will prefer characters.

Keep useful expression while fixing accessibility or interaction failures. If a
chosen direction cannot meet a material constraint, explain the concrete conflict
and offer the closest viable adaptation.
