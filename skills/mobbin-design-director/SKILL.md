---
name: mobbin-design-director
description: Designs, redesigns, implements, or critiques native iPhone and web screens and complete user flows the way a design director would, from user goals through Mobbin research, visual direction, build, and runtime review. Use when the user asks for a new screen or flow, a redesign, design options, a UX or visual critique, "this feels generic or AI-made", "make it feel native", pattern research on Mobbin, or a taste call between directions. Also use for small approved UI tweaks, where it stays lightweight. Not for backend work, copy-only edits with no layout change, or marketing pages with no product UI. Mobbin access helps but is not required.
argument-hint: "[deep|quick|research|taste|critique] [ios|web] <task>"
allowed-tools: Read Grep Glob Bash WebFetch mcp__mobbin__* mcp__plugin_mobbin-design-director_mobbin__*
---

# Mobbin Design Director

Design an experience people can understand, enjoy, and complete. Work from
goals, to journeys, to relevant patterns, to visual direction, to build, to
evaluation. Native iPhone is the primary specialization. Web has its own rules.

Read [evidence rules](references/evidence.md) once per task. They govern every
claim this skill makes.

## Orient and choose depth

1. Read project instructions, then `docs/design-context.md`,
   `docs/design-decisions.md` and `docs/design-taste.md` if present.
2. Check the implementation. It beats a stale doc.
3. Keep approved decisions and working behavior. Mark agent defaults as defaults.
4. Platform: the task instruction wins, then project evidence. Native target
   means iOS. A frontend means web. Both can apply. Ask only if still ambiguous.
   Do not force iOS behavior on web. Do not assume SwiftUI.

| Request | Depth | Read |
|---|---|---|
| Copy, bug fix, approved component tweak | Apply the established design. Check the affected behavior. No packet, no taste gate, no subagent. | the platform file only |
| New component or substantial screen | Frame, research the open decisions, compose, cover the states, check at runtime. | goals, research, synthesis, visual, defaults detector, platform files, review, and the matching [worked example](references/worked-examples.md) if one fits |
| New journey, navigation, major redesign | Scenarios and wireflow, targeted references, visual direction, independent critic, compact packet. | the row above plus flows, playbooks, coverage, critic prompt, packet template |

Scale effort by uncertainty and consequence. State the chosen depth in one line.
Load only the files the row names. The [topic index](references/index.md) routes
the rest.

## The working loop

1. **Frame.** Goal, context, prior knowledge, constraints, desired feeling,
   success criteria. [Goals](references/goals.md). Label unknowns as hypotheses.
2. **Structure.** For multi-step work, [flows](references/flows.md) before screens:
   entry, actions, responses, carried state, completion, recovery.
3. **Research the open decisions.** [Research](references/research.md). Default
   to Mobbin `mode: "standard"`. Deep mode costs credits. Record links and limits.
4. **Synthesize and recommend.** [Synthesis](references/synthesis.md). For each
   reference, write retain / improve / reject in a few lines:
   - Retain: the mechanism or visual relationship that serves the task, and why.
   - Improve: an observed weakness, with the adaptation.
   - Reject: a mismatched prerequisite, a needless step, or a treatment that
     conflicts with this product's direction.
5. **Set visual direction.** [Visual](references/visual.md), then run the
   [defaults detector](references/defaults-detector.md). Every choice that matches
   a known tool default needs a one-line reason in the packet, or it changes.
   Bring the owner only consequential open taste calls, one decision at a time,
   same content, with a recommendation. [Taste](references/taste.md).
6. **Build.** Reuse the project system. [Input](references/input.md), then the
   platform path: [iOS](references/ios.md) with
   [components](references/ios-components.md), [craft](references/ios-craft.md)
   and [writing](references/ios-writing.md), or [web](references/web.md).
   On iOS, native is the floor, not the goal. Take the native element for its
   behavior: back swipe, scroll physics, Dynamic Type, VoiceOver, keyboard
   avoidance. Then mold its look and feel until it belongs to this product:
   type scale, color, spacing, haptics, transitions, the one gesture that fits.
   A stock List that reads as the Settings app is a detector hit. The apps the
   craft file cites are all native and none of them look stock. The product,
   or each main flow, names one signature idea from outside stock iOS: its
   source (a Mobbin reference or a craft example, never an invented one), what
   it adapts, and why it serves this product. Hero screens show it. Utility
   screens (settings, forms, alerts, permissions) carry it only through the
   shared type, color, and spacing, and add no idea of their own. Restraint on
   any screen is valid when you state why. The idea changes the look and feel,
   never the native behavior above. Before a
   number, a placement, or a convention decides a choice, read the page:
   `scripts/hig.py <slug>`. A link in a reference file is a pointer, not the rule.
7. **Evaluate the real result.** [Review](references/review.md). Exercise the
   scenarios. Open the captures. Substantial work gets an independent
   [critic](references/critic-prompt.md). Classify every finding:
   - Verified defect: reproduced failure or an observable violation. Cite evidence.
   - Usability risk: a reasoned prediction tied to a user assumption and a
     principle. State how to test it.
   - Aesthetic preference: a taste tradeoff. Never dress it as a requirement.
   Severity (critical / major / minor) and confidence (high / medium / low) are
   separate. Verdict is one of: verified for stated scenarios / partial / blocked
   on a named capability.
8. **Record.** Approved decisions, taste evidence, open risks. Significant work
   uses the [packet](templates/design-packet.md). Routine work does not.

## Modes

Bare skill: `/mobbin-design-director [mode] [ios|web] <task>`. As a plugin:
`/mobbin-design-director:mobbin-design-director ...`. Codex:
`$mobbin-design-director ...`. Plain language works too.

| Mode | Meaning |
|---|---|
| default | Adapt depth to the request. Build when asked. |
| `deep` | Full journey, design and review loop with a packet. |
| `quick` | Focused component or established-design pass. |
| `research` | Evidence, options, recommendation, gaps. No product code. |
| `taste` | Focused visual calibration with comparable alternatives. |
| `critique` | Findings and verification limits. No implementation unless asked. |

## Tools in this skill

Scripts live under `${CLAUDE_PLUGIN_ROOT}/scripts/` (or this folder's `scripts/`
when installed bare). The simulator scripts are untested on the authoring Mac.
Verify them once on a Mac with Xcode.

| Need | Script |
|---|---|
| Boot a simulator with 9:41, appearance, text size, contrast, motion set | `sim-prepare.sh` |
| Capture a flow across appearance x text sizes x locales | `sim-matrix.sh` with `flow-step.sh` |
| Tap through a flow by accessibility label and save tree plus PNG | `flow-step.sh` |
| Find haptics, sound and glass adoption in source | `proxy-grep.sh` |
| Count generic iOS tells in Swift source (diagnostic only) | `swiftui_slop_lint.py` |
| Diff captures against baselines and build a contact sheet | `diff-report.sh`, `sheet.py --from-dir` |
| Keep Mobbin images past their 30-day URL expiry, outside Git | `mobbin_cache.py` |
| Ask a vision model to name tells in a pair of captures | `vlm-review.md` |
| Read the current HIG page for a component or pattern in one call | `hig.py <slug>` (`--list` for slugs) |
| Rank principles for a brief without loading the registry | `coverage.py search`, `principles-index.md` |

For complex work use [agents](references/agents.md): one lead, bounded
researchers and implementers, an independent critic. Do not spawn a team for
routine work. Discover the session's tools before using them.
