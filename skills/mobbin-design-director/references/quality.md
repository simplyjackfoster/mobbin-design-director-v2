# Build completeness

Use the relevant parts, not a universal checklist for every change.

- **Goal and content:** the implementation supports the brief's outcome; real
  content, labels, units, and unavailable data are represented honestly.
- **Flow:** actions, destinations, Back/Cancel, completion, draft/saved state,
  interruption, and recovery agree with the [flow contract](flows.md).
- **States:** relevant initial, pending, populated, empty, failed, retry, partial,
  offline, disabled, selected, long-content, keyboard, and text-scale conditions
  have defined behavior. Do not build impossible offline success or unused states.
- **Visual craft:** hierarchy, grouping, reading/action sequence, rhythm, imagery,
  and motion realize the [direction](visual.md) across neighboring screens.
- **System:** reuse components and tokens. Explain intentional additions and fix
  accidental drift. No fake data, broken assets, or misleading interactive cues.
- **Platform:** use the [iOS](ios.md) or [web](web.md) checks appropriate to the
  actual deployment target and supported configurations.
- **Verification:** check the running result using [review](review.md), with
  evidence for critical behaviors and explicit limits on what was not tested.

`scripts/token-audit.js` is a web diagnostic that counts computed styles. It does
not understand semantic tokens, inheritance, theme variants, or artistic intent;
compare its output with the design system before interpreting a value as drift.
Native style review uses source tokens plus rendered output, not a pretend DOM audit.
