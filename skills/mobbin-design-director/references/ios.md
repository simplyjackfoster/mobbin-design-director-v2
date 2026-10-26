# Native iPhone design and verification

Start with the project's supported OS versions, framework, device families,
appearances, localization, design system, and current build/run commands. iPhone
is the default specialization; add iPad adaptation when the product supports it.
Do not silently migrate UIKit or React Native to SwiftUI.

## Current guidance, durable reasoning

Books explain goals, perception, and interaction tradeoffs. Current Apple guidance
and framework behavior supply present-day native conventions. The HIG is on
iOS 27. Pick the native element with [components](ios-components.md), the
behavior with [craft](ios-craft.md), and the words with [writing](ios-writing.md).
Official references (see the CHANGELOG for the last review date):

- [Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios)
- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- [Typography](https://developer.apple.com/design/human-interface-guidelines/typography)
- [VoiceOver](https://developer.apple.com/design/human-interface-guidelines/voiceover)
- [Motion](https://developer.apple.com/design/human-interface-guidelines/motion)
- [Navigation and search](https://developer.apple.com/design/human-interface-guidelines/navigation-and-search)

Recheck relevant pages when a convention, measurement, new OS feature, or API
availability determines the decision. `scripts/hig.py <slug>` prints the current
page as text in one call, so there is no reason to trust a stale summary. Do not turn book-era drawers, motion
thresholds, or keyboard examples into modern rules. Native system components
adapt over OS versions; do not recreate a screenshot of an obsolete bar.

## Native structure

Use standard navigation, tabs, sheets, menus, alerts, pickers, and controls where
they fit. In SwiftUI inspect appropriate `NavigationStack`, `TabView`, sheet and
presentation APIs against the deployment target. Preserve expected back gestures
and distinguish dismissing a task from navigating within it. Sheet complexity,
stack behavior, and tab re-selection depend on the task; avoid arbitrary universal
rules such as “a second step cannot be a sheet.”

Define draft/committed state, cancellation, deep-link entry, and return context.
Use system input and permitted device capabilities to reduce unnecessary work.
Permission denial and returning from Settings need meaningful continuation when
relevant. Do not request sensitive permission just to make the prototype convenient.

Use [touch](touch.md) for grip variability, actual hit areas, obscured feedback,
nearby-action risk, and the limits of simulator-based ergonomics checks.

## Visual and interaction checks

- Content and actions remain reachable around safe areas, system bars, and keyboard.
- Inspect a representative phone and a small supported configuration. Choose actual
  available devices and sizes; do not freeze one pixel dimension as “current iOS.”
- Dynamic Type reflows rather than merely shrinking or clipping. Custom fonts and
  metrics scale relative to suitable text styles. Check accessibility text sizes.
  When adjacent labels squeeze meaningful names into fragments, stack the content.
  Fixed bottom controls must leave a usable scrolling region; move optional detail
  into reachable scrolling content when the large-text layout needs it.
- Use comfortably sized, separated hit areas. A 44pt square is a useful recommended
  default, not a substitute for checking Apple's current component-specific guidance.
- VoiceOver gets meaningful labels, values, traits, grouping, focus order, and state
  feedback. Decorative images should not interrupt the spoken task. Inspect semantics
  and exercise the task with assistive technology when available.
- Confirm focus and primary actions remain usable with the keyboard. Support relevant
  autofill and field semantics; do not implement a custom input puzzle unnecessarily.
- Verify supported appearances and contrast conditions. An approved light-only product
  stays light-only; record its limitation rather than silently adding dark mode.
  Inspect readable action labels in enabled, disabled, selected, and saved states;
  a control being present in the accessibility tree does not prove visible contrast.
- Motion explains response, continuity, or character without delaying frequent work.
  Respect Reduce Motion, retaining equivalent information. Avoid arbitrary timing laws.
- Verify long/localized text, selected states, slow/error responses, and interruption
  or relaunch where the flow promises persistence.

## Accessibility beyond labels

- Switch Control: explicit element order, `accessibilityNavigationStyle = .combined`
  for grouped rows, no timeouts, confirm destructive actions.
- Dynamic Type: text styles and `@ScaledMetric`; swap HStack for VStack when
  `dynamicTypeSize.isAccessibilitySize`; Large Content Viewer for custom bars.
- Honor `accessibilityReduceMotion`, `accessibilityDifferentiateWithoutColor`,
  `accessibilityShowButtonShapes`, `legibilityWeight`.
- Voice Control needs spoken names that match visible labels.
- Assistive Access: one interaction per screen, confirm destructive actions twice.
- Audit in UI tests with `performAccessibilityAudit(for: .all)`. Export the
  attachments. The audit does not replace a VoiceOver walk.

## Runtime loop

Discover available simulators with `xcrun simctl list devices available`.
Use `scripts/sim-prepare.sh`, `sim-matrix.sh`, and `flow-step.sh` for the
capture loop, `proxy-grep.sh` for haptics, sound, and glass adoption, and
`swiftui_slop_lint.py` as a diagnostic. They are untested on the authoring Mac. Use the
project's build commands and an explicitly identified simulator; never reset a
shared simulator or interrupt another agent's app. Serialize heavy builds when
project instructions require it. Use a disposable harness for isolated experiments.

Build, install, launch, exercise relevant transitions, capture screenshots or a
recording, and **open the captures**. Use available UI automation/XCTest/Maestro or
manual interaction for behavior; launching directly into several fixtures does
not prove the transitions between them. Restore any accessibility settings changed
for testing and clean up only task-owned resources.

A native prototype can be small, but its standard chrome should be real. If native
execution is unavailable, continue flow/spec/source work and label runtime,
gesture, accessibility, and material verification as unperformed. HTML proves only
the content/composition behavior actually exercised in the browser.
