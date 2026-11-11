---
name: visual-craft-constraints
tags: [offline, v2]
max_turns: 20
allowed_tools: [Read, Glob, Grep, Skill]
---

Use the mobbin-design-director skill to propose a buildable visual refinement for
an existing responsive web account/settings screen. No code or live browser is
available, and Mobbin is unavailable. Preserve its approved warm visual character,
CSS Grid layout, relative text units and existing tokens unless a specific gap
requires an addition.

At 1440px the form stretches to 1000px and the sidebar is 25% wide; at 900px the
sidebar labels wrap while the form is still too wide. On mobile, all desktop sizes
are multiplied by 0.7, including body text and targets. The h1 is the largest item
only because the browser makes it so. Status chips have dark saturated fills and
small white labels; a teammate suggests lowering label opacity to quiet them.
The type scale offers 12, 16, 21 and 28, but a compact role seems to need a value
between 16 and 21. Another teammate says the ratio must never be broken, that
Refactoring UI means we should stop using grids and relative units, and that 18px
regular text qualifies for 3:1 contrast. Decide what to preserve and change, with
concrete rationale and a verification plan. Keep any unverified claims explicit.
