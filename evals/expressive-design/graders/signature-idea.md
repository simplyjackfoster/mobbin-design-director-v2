---
type: llm
weight: 2
---
Judge whether the direction has a signature idea from outside stock iOS. PASS if all hold:
(a) The reply names at least one specific idea that changes the look or feel beyond system defaults, such as a type treatment, a color system, a transition, a gesture, haptics, or a layout move.
(b) The reply names where the idea came from: a shipped app, a craft example from the skill's references, or a Mobbin reference. Mobbin is unavailable in this case, so a Mobbin screen cited as seen is a FAIL.
(c) The reply says how the idea is adapted to the field-guide app and why it serves the task.
(d) The idea keeps native behavior: back swipe, scroll physics, Dynamic Type, and VoiceOver.
Do not penalize plain utility parts, such as a save confirmation or a settings row, when the hero screen carries the idea.
FAIL if the direction is a system list or a Settings-like layout with only a color change, if no source is named, if the source is invented, or if the idea replaces native navigation or scrolling.
