# Craft digests

Read this when you design or review an iPhone screen or a product UI and want the checkable rules behind the craft sources. [ios-craft](ios-craft.md) holds one line per source. This file holds the rest of each source as rules and does not restate those lines. [defaults-detector](defaults-detector.md) holds the palette and motion tells, so this file skips them too.

Each rule is one sentence you can check on a screen or in code. A quote marks wording that matters. "Applies to iOS as" says how a web rule transfers. "Does not say" stops over reading.

## 1. Invisible Details of Interaction Design

Rauno Freiberg. July 2023. https://rauno.me/craft/interaction-design

1. Build the whole interface on two gestures, tap and swipe, and teach any third gesture through one of them.
2. Let a dismissed element carry the angle and speed of the throw into its settle, so no two dismissals look identical.
3. Apply the gesture delta on the first frame of a pinch or drag, then animate past the threshold, never jump from 0 to 1 at the threshold.
4. Launch a detail from its source element when more than one source could own it, and from a fixed spot when the source is unique (Spotify from the icon, Clock from the Island).
5. Keep app icon art inside the safe zone, because the morph to icon stretches the bottom edge.
6. Animate out, not in, on a menu used thousands of times a day, and blink the chosen item once so the user knows it took.
7. Skip the switcher UI when the key chord is fast enough to show intent (Command Tab).
8. Show what the finger hides: a loupe over the caret, an enlarged key, a mirrored thumb for a small scrubber.
9. Keep a slider drag alive when the finger leaves the track while still pressed.
10. Blur app content in the app switcher when the screen holds sensitive data.
11. Put the most used targets in corners and at edges, where the target size is infinite.
12. Let a short swipe peek at the next screen and commit only when the gesture ends past the threshold.
13. Make a surface fidgetable (something to twist or flick) only when it costs nothing in function.
14. Use context as input where it is unambiguous: brightness up for a scannable pass, the route visible on a glance.

Applies to iOS as: this is written about iOS and SwiftUI, so apply as is. Use `DragGesture` velocity and `.interactiveSpring` for rules 2 and 3, and `matchedGeometryEffect` or the zoom transition for rule 4.
Does not say: never animate. He animates where novelty is high and removes motion where frequency is high.

## 2. interfaces (README checklist)

Rauno Freiberg. https://github.com/raunofreiberg/interfaces

1. Let a toggle take effect at once, with no confirm step.
2. Disable a submit control after the first tap so one action sends one request.
3. Leave no dead gap between rows in a list, grow the row padding instead.
4. Keep font weight constant on hover and on select so nothing shifts.
5. Use tabular figures wherever numbers change in place (timers, tables).
6. Pause a looping animation when it leaves the screen.
7. Never flash a hover state on a touch press.
8. Never autofocus a field on a touch device, the keyboard will cover the screen.
9. Never put a tooltip on a disabled control, nobody can reach it.
10. Let a decorative glow or gradient pass touches through, it must never swallow a tap.
11. Show feedback at the trigger: an inline check on copy, a highlighted field on error, not a banner.
12. Make an empty state prompt the first create, with optional templates.
13. Update locally first and roll back with feedback if the server fails.
14. Switch themes with no transition on any element.

Applies to iOS as: rule 5 is `.monospacedDigit()`. Rules 7 and 9 concern the iPad pointer and macOS, not iPhone. Rule 11 means in place state, not a toast, which the HIG feedback page also says. Rule 14 maps to `.animation(nil)` on a color scheme change.
Does not say: the list is web only and calls itself not exhaustive. It does not rank the items.

## 3. Great Animations, and 7 Practical Animation Tips

Emil Kowalski. https://emilkowal.ski/ui/great-animations , https://emilkowal.ski/ui/7-practical-animation-tips

1. Answer every action at once: a loading state on submit, a success state on copy, "as if it's listening to the user".
2. Spin a spinner faster, the load feels faster at the same duration.
3. Use a custom curve, the built in easings "are usually not strong enough".
4. Let the user reverse an animation mid flight with no jump (open an item, press Escape at once).
5. Drive an animation off the main thread when that thread is busy, a frame drop on page load is the symptom.
6. Pace animations through a flow so each one enriches the content, or the user is overwhelmed and none land.
7. Open peer tooltips instantly once one is open, no delay and no animation.
8. Add 2 px of blur to a crossfade that still feels wrong after easing and duration changes.
9. Keep easing and duration cohesive with the component, the page, and the name (Sonner is slower and uses plain `ease` because that fits).
10. Tune an opacity plus height change by trial, there is no formula.
11. Review the animation the next day with fresh eyes.

Applies to iOS as: springs are the SwiftUI default (Motion section of [ios-craft](ios-craft.md)). Rule 3 is `.timingCurve(_:_:_:_:)`. Rule 4 is met by implicit animation, which retargets, unless you chain `withAnimation` calls. Rule 5 is Core Animation on the render server, so do not drive motion from a timer. Rule 8 is `.blur(radius: 2)` during the swap.
Does not say: always use springs, or that every animation must be under 300 ms (the explanatory v0 animation is longer on purpose).

## 4. emil design eng skill

Emil Kowalski. https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md

1. Decide by frequency first: 100 or more times a day gets "No animation. Ever.", tens a day gets reduced motion, occasional gets standard, rare gets delight.
2. Name the purpose before you animate: spatial consistency, state change, explanation, feedback, or preventing a jarring change.
3. Size the duration to the element: press 100 to 160 ms, tooltip 125 to 200, dropdown 150 to 250, modal or drawer 200 to 500.
4. Keep a modal centered, the origin rule is for popovers that have a trigger.
5. Dismiss on velocity as well as distance, a quick flick dismisses from anywhere.
6. Damp a drag past its boundary so it slows instead of stopping.
7. Ignore a second finger once a drag starts.
8. Make the press slow where the user decides (hold to delete, 2 s linear) and the release fast (200 ms ease out).
9. Make exit faster than enter.
10. Stagger grouped entries by 30 to 80 ms and never block input while a stagger plays.
11. Under reduced motion keep opacity and color and remove movement, "fewer and gentler animations, not zero".
12. Match motion to the mood: "A professional dashboard should be crisp and fast".
13. Test at slow speed, frame by frame, and on a real device.
14. Review UI code as a Before, After, Why table, one row per issue.

Applies to iOS as: rule 3 maps to `.easeOut(duration:)` or `.spring(duration:)`. Rules 5 and 6 come from `DragGesture` predicted end translation and a rubber band on overshoot. Rule 11 reads `accessibilityReduceMotion`. Rule 4 is a `.sheet` versus a `.popover` anchored to its source.
Does not say: it does not give a spring value for iOS, its "Apple's approach" example is a Motion config.

## 5. Family Values

Benji, benji.org, with the Family wallet team. July 2024. https://benji.org/family-values

1. Use a tray for a transient action and a full screen for something that stays, so a confirm or warning appears in place.
2. Overlay a tray on the current screen, never replace it, so the user keeps context.
3. Give every tray a title and one icon that dismisses the first tray or goes back through a stack.
4. Let the tray theme follow the flow (a dark flow gets a dark tray).
5. Keep a component that persists into the next step on screen, never let it duplicate itself during the transition.
6. Keep the unchanged words of a sentence fixed when one part updates (empty states, counts on a button).
7. Keep commas shifting in place as a number is typed.
8. Polish every screen to the same level or the weak one drags the rest down, "a fancy restaurant ... a dirty bathroom".
9. Spend delight in inverse proportion to frequency, the rarer the feature the bigger the moment (the Delight Impact Curve).
10. Hide a surprise on a screen used often enough to find it and rarely enough not to annoy (the QR ripple).
11. Mark a rare, important moment (new wallet, backup done) with a reward such as confetti.
12. Return a spinner to where the pending item now lives (speed up moves the spinner back to the original tray).
13. Remove an animation only after a side by side shows nothing is lost, "digital whiplash" is the failure to watch for.

Applies to iOS as: this is an iOS app. Trays are `.sheet` with `presentationDetents` and a distinct height per step. Rule 5 is `matchedGeometryEffect`. Rules 6 and 7 use `contentTransition(.numericText())`.
Does not say: delight everywhere. Frequent features get small touches and the curve says more would annoy.

## 6. How we redesigned the Linear UI (part II), and Why is quality so rare?

Karri Saarinen with Yann-Edern Gillet, Andreas Eldh, Romain Cascino. March 2024 and May 2025. https://linear.app/now/how-we-redesigned-the-linear-ui , https://linear.app/now/why-is-quality-so-rare

1. Aim a refresh at three things: less visual noise, kept alignment, and denser navigation with clearer hierarchy.
2. Cut a problem from scope when it stops being a design problem (they dropped navigation).
3. Redesign the chrome (the inverted L), not the product down to its atoms.
4. Align every label, icon, and button on both axes in the sidebar and tabs, "something that you'll feel after a few minutes".
5. Explore in black and white opacities first to settle elevation and hierarchy before color.
6. Generate a theme from three variables (base, accent, contrast) in LCH, not 98 hand set values, so the contrast variable yields the high contrast theme.
7. Make text and neutral icons darker in light mode and lighter in dark mode, and limit how much accent hue leaks into neutrals.
8. Stress test the direction on every view type (list, board, split, timeline) before engineering starts.
9. Ship behind a flag, dogfood with every team, and put a toggle in the dev toolbar to compare old and new.
10. Do a redesign fast or it blocks every other project and creates design debt.
11. Ask "does this improve quality?" before "will this ship faster?".
12. Keep MVPs internal, fix every bug within 7 days, and keep 3 to 5 people with taste on a decision.

Applies to iOS as: rule 6 maps to asset catalog color sets with Any, Dark, and High Contrast variants derived from one base, read through `colorSchemeContrast` (`.increased`) or `UIAccessibility.isDarkerSystemColorsEnabled`. Rule 9 is a TestFlight build with a debug toggle.
Does not say: part II does not say how to redesign navigation, that was cut on purpose. The quality post states a business case, not a visual rule.

## 7. Web Interface Guidelines

Vercel Labs. https://github.com/vercel-labs/web-interface-guidelines

Only the rules that transfer to native or any product UI.

1. Make every hit target at least 44 pt on mobile even when the glyph is smaller.
2. Keep the button label visible during loading and add a spinner beside it.
3. Delay a spinner or skeleton 150 to 300 ms and keep it at least 300 to 500 ms once shown, to stop flicker.
4. End a label with an ellipsis when it opens a further step ("Rename…") or is in progress ("Saving…"), and use the single character.
5. Confirm a destructive action or offer Undo with a safe window.
6. Restore scroll position on back.
7. Give every drag, swipe, or pinch a tap and keyboard equivalent unless the gesture is essential.
8. Nudge alignment by 1 pt where perception beats geometry.
9. Balance an icon and text that sit together, a thin icon next to medium text needs a heavier stroke.
10. Design empty, sparse, dense, and error states and give every screen a next step.
11. Never use color alone for status.
12. Test every layout with short, average, and very long content.
13. Format dates, numbers, and currency for the locale.
14. Keep submit enabled until the request starts, allow any keystroke and validate after, and focus the first error on submit.
15. Warn before navigation when data would be lost.
16. Raise contrast on press and focus, and tint borders and shadows toward the background hue.
17. Make an error say how to leave it: "Your API key is incorrect or expired" plus the fix (from the brand section, kept because it holds anywhere).
18. Name the outcome on a button: "Save API Key", not "Continue" (from the brand section, same reason).

Skipped as web only: hydration, URL state, SVG transforms, preconnect, font subsetting, workers, scrollbars.

Applies to iOS as: rule 3 wraps a `ProgressView` in a delayed show. Rule 7 is the HIG gestures page. Rule 10 uses `ContentUnavailableView`. Rule 11 is `accessibilityDifferentiateWithoutColor`. Rule 13 is `FormatStyle`. Vercel's Title Case for buttons matches HIG control capitalization, and sentence case stays for body copy.
Does not say: the rest of the Copywriting section is marked as Vercel brand choice, not a guideline.

## 8. frontend design skill

Anthropic. https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md

1. Name the subject, the audience, and the primary job before you choose a color or a face.
2. "Spend your boldness in one place" and keep everything around it quiet.
3. Remove one accessory before you ship (the Chanel mirror check).
4. Use one or two faces, and if two make them clearly distinct.
5. Never accent one word of a headline in italic, bold, or color.
6. Never set labels in all caps and never add a label above content that does not need one.
7. Number items only when the content is a sequence.
8. Treat each border, divider, eyebrow, or label as information, and cut it if it only decorates.
9. Keep one orchestrated reveal per page at most, and let every other motion answer a user action.
10. Flag template chrome: eyebrow caps, middle dot meta strings, spaced dash labels, tinted near black, mono data labels, arrows on links, one radius and one grey shadow on every card.
11. Keep the same verb through a flow: "Publish" produces "Published".
12. Make the CTA say what happens: "Save changes," not "Submit."
13. Write errors that never apologize and are never vague about what happened.
14. Plan in two passes: a token plan, then a review against the brief that revises anything you would have produced for any similar page.
15. Follow the brief exactly when it names a look, even a cliché one.

Applies to iOS as: rule 10 reads as `.textCase(.uppercase)` eyebrows, chevrons on every row, and one `cornerRadius` on every card. Rules 5 and 6 hold for navigation titles too. HIG capitalization wins for controls and titles, sentence case for body copy.
Does not say: it does not ban cream or terracotta when the brief asks for them. The brief's own words always win.

## 9. Introducing Halide, and Halide 1.1

Lux Team, Ben Sandofsky. May and August 2017. https://www.lux.camera/introducing-halide/ , https://www.lux.camera/halide-1-1-better-faster-stronger/

1. Default to automatic and keep manual one tap away.
2. Let the user arrange the button layout.
3. Make review a swipe pair, right to keep and left to delete, and let it open and close mid session without breaking flow.
4. Honor the hardware convention first (the volume shutter was "the number one request").
5. Fire the action on touch down, not on lift, when the physical tool does (65 ms of felt latency removed).
6. Warm up the expensive path at launch so the first use is as fast as the second (1 s to 150 ms).
7. Relabel a control when the device lacks the feature (RAW becomes MAX) instead of showing a dead one.
8. Pick the overlay color that stands out in real scenes (green peaking).
9. Do not prompt for ratings in app.

Applies to iOS as: written for iOS. Rule 5 is a `DragGesture(minimumDistance: 0)` onChanged, not a `Button` action. Rule 4 is the camera volume button API.
Does not say: it does not describe the Halide Router typeface or the gesture set beyond the dial metaphor.

## 10. Copilot Money, and (Not Boring) Habits

Apple Developer. Andrés Ugarte, Bastian Suarez, Sergio Campamá. Andy Allen, Mark Dawson. https://developer.apple.com/articles/copilot-money , https://developer.apple.com/news/?id=9ab1g4r3

1. Mold core UIKit components rather than replace them, so the Mac app is the iOS app plus a few components.
2. Reach for the system framework before a custom build ("Why should we build something from scratch").
3. Count fewer components as fewer bugs.
4. Keep the founders coding to stay close to the craft.
5. Keep standard controls stock and spend the budget on one ritual action.
6. Prototype until the feedback tells the user to keep holding.
7. Compete on design when you cannot compete on features, "design is difficult to copy".
8. Frame the product as a journey with levels when the goal is a 66 day habit.

Applies to iOS as: both are iOS. Rule 1 is `UIAppearance` and subclassing, not a reimplementation. Rules 5 and 6 are SceneKit plus `CHHapticEngine` on a long press.
Does not say: Habits does not say every control is loud, and Copilot does not say never customize.

## 11. Taste for Makers

Paul Graham. February 2002. https://paulgraham.com/taste.html

Use the fourteen as review questions.

1. Simple: does the beauty rest on a few structural elements, or is ornament "camouflage on insipid form"?
2. Timeless: would this look right in 1500 and 2500, or does it lean on a fashion?
3. Right problem: does the control layout mirror what it controls (stove dials in a square like the burners)?
4. Suggestive: does it give a few elements the user can combine, or a program they must follow?
5. Slightly funny: does it take itself too seriously ("may not always be true")?
6. Hard: did a hard constraint force the elegance, or was there effort to spare for flourishes?
7. Looks easy: is every line in exactly the right place, like a Leonardo head?
8. Symmetry: does repetition or recursion carry the structure, and is it thought or a substitute for it?
9. Resembles nature: does the answer look like nature's answer to the same problem?
10. Redesign: did we throw early work away, and is the medium easy to change?
11. Can copy: do we know where the idea came from, or are we "imitating an imitator"?
12. Strange: did strangeness appear on its own, and did we leave it alone?
13. Chunks: are we close to people working on related problems?
14. Daring: did we look where "conventional wisdom and truth don't quite meet"?

Closing vocabulary: "What a hack! There must be a better way" and "very exacting taste, plus the ability to gratify it".

Applies to iOS as: a review vocabulary, not a screen rule. Question 3 is the one direct check, a control's layout mirrors the thing it controls.
Does not say: it does not rank the fourteen, and it says the funny one may not hold.

## 12. Ten principles for good design

Dieter Rams, via Vitsœ. https://vitsoe.com/gb/about/good-design

1. Innovative: innovate with the technology, never as an end in itself.
2. Makes a product useful: cut anything that detracts from use.
3. Aesthetic: only a well executed object can be beautiful.
4. Makes a product understandable: the structure explains itself.
5. Unobtrusive: neutral and restrained, room for the user.
6. Honest: no promise the product cannot keep.
7. Long lasting: avoid fashion so it never looks antiquated.
8. Thorough down to the last detail: nothing arbitrary.
9. Environmentally friendly: conserve resources, cut visual pollution.
10. As little design as possible: "Less, but better".

Applies to iOS as: principles 4 and 5 are the HIG's clarity and deference. Principle 8 is the whole of this file.
Does not say: it is not a scorecard and it gives no screen level rules.
