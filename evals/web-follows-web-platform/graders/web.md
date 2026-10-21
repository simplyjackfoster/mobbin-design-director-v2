---
type: llm
weight: 1
---
All must hold:
1. It names Mobbin `platform` `web`, not `ios`.
2. Navigation follows web rules: routes or URLs for each section, the browser back button, and a focus-trapping dialog or a new route instead of an iOS sheet or back chevron.
3. The review plan checks several widths (a phone width and a desktop width), keyboard focus and 200% zoom, using a browser devtools MCP rather than an iOS simulator.
4. It writes no UI code.
