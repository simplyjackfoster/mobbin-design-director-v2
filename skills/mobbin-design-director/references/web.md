# Web design and verification

Follow the project's actual framework, component library, design system, supported
browsers, and responsive requirements. Shared product goals do not require copying
iPhone navigation or chrome.

- Model meaningful destinations and shareable state in URLs as appropriate. Test
  direct entry, reload, browser Back/Forward, and filter/detail restoration.
  Verify focus after the route has actually rendered, with a meaningful fallback
  when no originating control exists. Skip links must reach the current content
  without accidentally changing the routed view.
- Use semantic links for navigation and buttons for actions. Prefer native form
  elements and well-tested accessible components over rebuilding controls.
- Keyboard users can reach and operate actions with a visible focus indicator.
  Dialogs manage focus, offer an appropriate escape, and return focus meaningfully.
  Pointer/hover must not be the only way to reveal essential content or controls.
- Check touch and pointer use, readable line lengths, long content, responsive
  grouping, and reflow. Start with project breakpoints and inspect narrow phone,
  intermediate/tablet, and wide desktop configurations relevant to the audience.
- Test zoom, increased text size, contrast, semantic structure, accessible names,
  error associations, and state announcements. Do not infer accessibility from a
  screenshot or an automated checker alone.
- Reserve appropriate space for asynchronous content. Preserve form input and
  context across recoverable failures. Honor motion/appearance preferences within
  the product's supported configurations.

Consult current [WCAG](https://www.w3.org/TR/WCAG22/) and
[WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/) for the actual
criteria and interaction pattern under review, including exceptions. Avoid
claiming conformance from a few spot checks or transplanting an iOS point size
into CSS as a universal standard.

For mobile web, use [touch](touch.md) and check browser chrome, keyboard, and
fixed controls together. A screenshot cannot prove the actual hit areas or that
scrolling and gesture handling coexist correctly.

Run the product using its commands. Use the connected browser tools available in
this environment, inspect the rendered result and accessibility information, and
exercise navigation, input, errors, and recovery. Existing automated checks are
useful for regressions; keep visual and task inspection separate.

`scripts/token-audit.js` can reveal unexpected computed-style diversity when the
browser tool permits evaluation. Treat counts as a diagnostic, not a grade. Use
`scripts/sheet.py` for a comparison artifact with sources and realistic content.
