---
name: microinteraction-spec
tags: [offline, v2]
max_turns: 20
allowed_tools: [Read, Glob, Grep, Skill]
---

Use the mobbin-design-director skill to specify an iPhone "quiet hours" control
for a team messaging app. Only this description is available; Mobbin and runtime
are not. The proposal: a two-finger swipe down anywhere on the inbox turns quiet
hours on, with a brief toast as the only confirmation. Quiet hours still lets
direct mentions from managers through, but the toast does not say so. The app
also turns quiet hours on automatically when the calendar shows a meeting, with
no indicator. While on, tapping a conversation row selects it for bulk archive
instead of opening it. Quiet hours ends "after a while".

Produce a buildable specification for this microinteraction. Distinguish
requirements, predicted risks and taste. Do not implement or imply that the
described interface has been inspected live.
