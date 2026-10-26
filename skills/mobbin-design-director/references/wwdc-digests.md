# WWDC digests: checkable rules from the sessions this skill cites

Read this when a review or a design needs the exact rule an Apple session states and the place in the session that states it. [ios-craft](ios-craft.md) holds one headline per session. This file holds the layer below it. Each rule is one sentence a reviewer can check on a screen or in code. Quotes are at most twelve words. Times are approximate and come from the transcript. Chapter names are Apple's. Every session below had a transcript on its Apple page on 25 October 2026.

## 1. Meet Liquid Glass

WWDC25, session 219. https://developer.apple.com/videos/play/wwdc2025/219/

1. Give glass elements rounded floating forms that nest in the device corners. "rounded, floating forms that nest neatly" (Dynamics, 1:30)
2. Fade glass in and out by modulating the lensing, never by a plain opacity fade. "Instead of fading, Liquid Glass objects materialize" (Dynamics, 2:30)
3. Keep a control quiet at rest and let it lift into glass only on touch. "lift up into Liquid Glass temporarily" (Dynamics, 4:00)
4. Morph the controls between app states instead of swapping them, so one floating plane persists. (Dynamics, 4:30)
5. Open a menu from its button in place. "keeps everything right where you just tapped" (Dynamics, 5:00)
6. Let small bars, nav and tab, flip between light and dark with the content behind them. (Adaptivity, 6:30)
7. Do not let a menu or a sidebar flip light to dark. "transitions like these would be distracting" (Principles, 15:30)
8. Treat the sidebar and the tab bar as one navigation element that scales with the canvas. (Adaptivity, 8:30)
9. Use the hard scroll edge style only when a pinned accessory, such as column headers, sits under the toolbar. (Adaptivity, 9:30)
10. Keep glass off a table view or any other content layer element. "muddy the hierarchy" (Principles, 13:00)
11. Build anything that sits on glass from fills, transparency, and vibrancy, not a second glass. (Principles, 13:30)
12. Never mix the Regular and Clear variants. "They should never be mixed" (Principles, 13:30)
13. Use Clear only when all three hold: the element is over media rich content, a dimming layer does not hurt that content, and the content above the glass is bold and bright. (Principles, 14:30)
14. Put a dimming layer under Clear, localized when the footprint is small. (Principles, 14:30)
15. Tint with the material's own tint, never a solid fill, and only on the primary action. "Avoid tinting all your elements." (Principles, 17:00)
16. Put brand color in the content layer, not on the controls. (Principles, 17:30)
17. At launch and in steady states, move or scale content so it does not sit under glass. (Principles, 18:00)
18. Check Reduce Transparency, Increase Contrast, and Reduce Motion each change the material. (Principles, 18:30)

What this session does not say: it gives no dim percentage for Clear, no radius values, and no API names.

## 2. Get to know the new design system

WWDC25, session 356. https://developer.apple.com/videos/play/wwdc2025/356/

1. Align alert and onboarding type to the left and use a bolder weight. (Design Language, 2:30)
2. Build nested shapes from three types only: fixed radius, capsule, and concentric. (Design Language, 3:30)
3. Make a capsule radius half the container height. (Design Language, 3:30)
4. Compute a concentric radius as the parent radius minus the padding. (Design Language, 3:30)
5. On macOS keep Mini, Small, and Medium controls as rounded rectangles and give Large and X Large controls capsules. (Design Language, 4:00)
6. Fix a corner that looks pinched or flared by making the shape concentric. (Design Language, 5:00)
7. Near a phone screen edge use a capsule with extra margin. On iPad and Mac use a concentric shape aligned to the window edge. (Design Language, 5:30)
8. Give a component that works both nested and alone a concentric shape with a fallback radius. (Design Language, 6:00)
9. Spring an action sheet from the control that opened it, not from the screen bottom. (Structure, 7:00)
10. Apply glass to the custom control itself, not to its inner views. (Structure, 7:00)
11. Pair a sheet that interrupts the flow with a dimming layer. Leave a parallel task sheet undimmed. (Structure, 7:30)
12. Remove custom backgrounds and borders from bar buttons. "now's the time to clean them up" (Structure, 8:30)
13. Move secondary bar actions into a More menu when the bar is crowded. (Structure, 9:00)
14. Group bar items by function and frequency. Never group a symbol with a text button. "could be perceived as a single button" (Structure, 9:30)
15. Keep a primary action such as Done separate and tinted. (Structure, 10:00)
16. Put only persistent features in a tab bar accessory view, never a screen specific action such as checkout. (Structure, 10:30)
17. Use a scroll edge effect only where floating UI meets content, one per view, and never stack soft on hard. "scroll edge effects are not decorative" (Structure, 11:30)
18. Keep the edge effects of split view panes the same height. (Structure, 12:30)
19. Use the background extension effect for hero images and tinted surfaces, and layer text and controls above it. (Structure, 12:30)
20. Reuse the same symbols across devices, and use a text label when no clear shorthand exists, as with Select or Edit. (Continuity, 15:00)
21. In a menu, use one symbol to introduce a group of related actions and let text do the rest. (Continuity, 15:30)

What this session does not say: it gives no radius, margin, or spacing numbers, and no rule for custom tab bars.

## 3. Design foundations from idea to interface

WWDC25, session 359. https://developer.apple.com/videos/play/wwdc2025/359/

1. Check that the first screen answers where am I, what can I do, and where can I go. (Structure, 2:00)
2. Do not open on a menu or a brand title. "feels more like branding" (Structure, 2:30)
3. List every feature, imagine the user's routine, then cut, rename, and group before you draw. (Structure, 4:00)
4. Give a tab only to a top level section. Merge a tab that is just a grouping screen. (Navigation, 5:30)
5. Keep actions out of the tab bar. "tabs are for navigation, not for taking action" (Navigation, 6:00)
6. Label each tab with a direct noun and an SF Symbol. (Navigation, 6:30)
7. Put the screen name in the toolbar title with the few essential actions beside it. (Navigation, 7:30)
8. Show a few items first and reveal the rest behind a disclosure control. (Content, 9:00)
9. Keep the same arrangement on the expanded screen so it reads as the previous one grown. (Content, 9:00)
10. Use a list for structured text and a collection for many images, with even spacing and little text. (Content, 10:30 and 12:30)
11. Group large content by time, progress, or pattern before you lay it out. (Content, 11:30)
12. Squint at the screen. The eye must land on the most important element first. (Visual Design, 14:00)
13. Use system text styles, then test long text, other languages, and large Dynamic Type. (Visual Design, 14:30)
14. Put a gradient or blur behind text that sits on an image. (Visual Design, 15:30)
15. Use semantic colors for backgrounds, labels, and icons. Use the accent color sparingly. (Visual Design, 17:00)

What this session does not say: it gives no numbers, and it names no components beyond tab bar, toolbar, disclosure control, list, collection, and SF Symbols.

## 4. Design intuitive search experiences

WWDC26, session 292. https://developer.apple.com/videos/play/wwdc2026/292/

1. Keep the search icon, placeholder, clear button, and on iOS the Cancel button, even with custom iconography. (Search field, 2:00)
2. Make any custom search icon resemble the magnifying glass. (Search field, 2:30)
3. Prefer search in the bottom toolbar on iOS, where the field rises over the keyboard. (Patterns and placement, 3:00)
4. Decide placement by two questions: how people navigate, and what the scope is. (3:30)
5. Start search as a button when the toolbar holds more than two other items. (4:30)
6. Use the top toolbar only when a sheet occupies the bottom, as in Stocks. (5:00)
7. In a tabbed app give search one primary entry point, a Search tab. (5:30)
8. Make the Search tab prominent when people know what they want and the keyboard should appear on tap. Use a standard tab when they browse. (6:00)
9. Place an inline field under the title to scope search to one section, and state the scope in the placeholder. (7:00)
10. Keep iPad and Mac search aligned. Use the trailing toolbar position in split view apps and when results land in the detail view. (8:00)
11. Put search in the sidebar when it filters the sidebar list. (9:00)
12. Show recent searches inline on focus on iOS, and in a menu from a toolbar or sidebar field on iPad and Mac. (10:30)
13. Let people remove one recent search by swipe and clear all from the section header. (11:30)
14. Distinguish the typed part from the predicted part of a suggestion, and limit the count. (12:00)
15. Start the primary search broad and let people narrow. Use a scope bar for light filtering. (12:30)
16. Show only filters relevant to the current query. (13:30)
17. Pair tokens with a scope bar or visible filters. "tokens can also be less discoverable" (14:30)
18. Show a no results view with symbol, title, subtitle, and the typed text. (15:00)

What this session does not say: it gives no result counts, debounce timings, or ranking rules.

## 5. Principles of great design

WWDC26, session 250. https://developer.apple.com/videos/play/wwdc2026/250/

1. Cut any feature that cannot justify the time, attention, and trust it asks for. (Purpose, 0:30)
2. Let people start without a forced path. (Agency, 2:00)
3. Offer undo for send, change, and delete. (Agency, 2:30)
4. Interrupt only before a destructive action. "only when someone is about to make a big mistake" (Agency, 3:00)
5. Ask for a permission at the moment the feature needs it, never at launch. (Responsibility, 4:00)
6. Ask only for the data you need and say what it is for. (Responsibility, 4:30)
7. For an AI feature, write down how it could be misused, then add a preview, confirmation, or disclaimer, or remove it. (Responsibility, 5:30)
8. Use a metaphor people can predict, neither too literal nor too abstract. (Familiarity, 7:00)
9. Never reuse a known icon such as the trash can for another meaning. (Familiarity, 7:30)
10. Make controls that look the same behave the same. (Familiarity, 8:00)
11. Keep the same action in the same place across screens and devices. (Familiarity, 8:30)
12. Let people rearrange or hide controls when one layout cannot fit everyone. (Flexibility, 10:30)
13. Write in plain language and cut steps. "we don't mean minimal" (Simplicity, 11:30)
14. Make the most important item the most obvious through order, spacing, and contrast. (Simplicity, 12:00)
15. Add context where a decision needs it, as a play control shows time left. (Simplicity, 13:00)
16. Treat a wait after tap, jittery scroll, misaligned icons, or a broken rotation as craft failures. (Craft, 14:00)
17. Name the emotion you want and reinforce it. Do not add confetti. (Delight, 16:00)

What this session does not say: it gives no measurements and no component rules.

## 6. Animate with springs

WWDC23, session 10158. https://developer.apple.com/videos/play/wwdc2023/10158/

1. Keep position and velocity continuous at every animation start and end. (Why springs, 2:00)
2. Use linear only for a repeating indicator, never for movement. (Why springs, 4:00)
3. Do not use an ease curve after a gesture. It cannot take the gesture's velocity. (Why springs, 5:00)
4. Let properties in one animation settle at different times. "these times usually don't line up perfectly" (Why springs, 7:30)
5. Configure a spring with duration and bounce, not mass, stiffness, and damping. (How springs work, 9:30)
6. Read bounce as a percent. Above 0 overshoots, 0 is smooth, below 0 is flattened. (How springs work, 10:30)
7. Use a negative bounce for decaying motion such as a scroll. (How springs work, 16:00)
8. Never wait for the settling duration. Use the completion handler, which fires at the perceptual duration. (How springs work, 17:00)
9. Start from a preset and change its duration or add relative bounce. (How to use springs, 18:00)
10. Choose duration first for pacing, then bounce for character. (How to use springs, 20:30)
11. Read 15 percent as brisk, 30 percent as noticeably bouncy, and above 40 as exaggerated. (How to use springs, 21:00)
12. Add bounce only for playfulness or at the end of a gesture, and keep it consistent across the app. (How to use springs, 21:30)

What this session does not say: it names no preset values and no duration numbers.

## 7. Designing Fluid Interfaces

WWDC18, session 803. https://developer.apple.com/videos/play/wwdc2018/803/ No chapters. Times approximate.

1. Hunt for delays on every tap and press, not only on swipes. (6:00)
2. Let a gesture be redirected mid flight, so thought and gesture run in parallel. (7:00 to 8:30)
3. Let the user interact with an app while it is still launching. (10:00)
4. Detect a pause from the finger's acceleration spike, not from a timer. (11:00)
5. Make a thing leave the way it entered. A pushed screen returns to the right. (12:30)
6. Grow an element toward its final state as the finger presses, as Control Center modules do. (14:00)
7. Amplify a light input into a large result using position, velocity, and force. (15:00)
8. Rubber band at every edge, and hand off between tracked elements on smooth curves. (17:00 to 18:00)
9. Slow fast movement or add stretch when adjacent frames differ too much. "it's not just about framerate" (19:00)
10. Give conceptually heavier content more mass. Apps are heavier than photos. (21:30)
11. Describe a spring by damping and response, never by duration. (34:30)
12. Use bounce as a hint. The Flashlight button bounces to teach a firmer press. (38:00)
13. Keep one family of behaviors, so scroll and scroll to top feel the same. (40:00)
14. Project the thrown endpoint for scale and rotation too, not only position. (47:00)
15. Highlight a button on touch down and confirm on touch up. (50:00)
16. Add margin around the tap area. Cancel when the finger drags out and highlight again when it returns. (50:30)
17. Begin a swipe after about 10 points of hysteresis and decide its axis then. (51:30)
18. Keep the grab point under the finger. Never recenter the dragged element. (52:00)
19. End a drag with the velocity from the touch history, not the last position. (52:30)
20. Read velocity, pressure, and size from the touches. Avoid recognizers that fire only at the end. (54:30)
21. Detect every candidate gesture from the first touch and cancel the losers once intent is clear. (55:30)
22. Avoid double tap where a single tap matters. It delays the tap by about half a second. (56:30)
23. Clip the last row, show a page indicator, or add a grabber to teach scroll, pages, and panes. (58:00)
24. Lift a draggable element to its own plane, like the switch knob. (59:00)
25. Animate the button action the same way the gesture moves, so one teaches the other. (59:30)
26. Explain a gesture in words once, and only when it recurs. (60:00)
27. Build an interactive prototype. "worth a million static designs" (62:00)

What this session does not say: it gives no spring numbers beyond the Music 100 and 80 percent damping, and no code beyond the projection function.

## 8. Enhance your UI animations and transitions

WWDC24, session 10145. https://developer.apple.com/videos/play/wwdc2024/10145/

1. Use the zoom transition where the tapped cell is large. (New transitions, 1:30)
2. Match the identifier and namespace on the source and the presented view. (Zoom transitions in SwiftUI, 2:30)
3. In UIKit capture a stable model identifier in the source closure, never the cell. (Zoom transitions in UIKit, 3:30)
4. Use the closure context to zoom back to the current item after a swipe. (Zoom transitions in UIKit, 3:30)
5. Expect a push to turn into a pop at any time, and never branch on being in a transition. (Life cycle, 6:30 and Tips, 7:00)
6. Keep transition state minimal and reset it in viewDidAppear or viewDidDisappear. (Tips, 7:30)
7. Bridge an animated binding through the context animate call in updateUIView. (Animating representables, 10:30)
8. Animate UIKit views with SwiftUI animation types to keep velocity across a gesture. (Gesture driven animations, 12:30)

What this session does not say: it gives no durations. Every demo runs at half speed, so do not read timing from the video.

## 9. Practice audio haptic design

WWDC21, session 10278. https://developer.apple.com/videos/play/wwdc2021/10278/ No chapters.

1. Make the cause of each haptic obvious. A texture plays only while its visual shows. (3:30)
2. Match size across senses. "A small ball should feel small and sound small." (4:00)
3. Reserve haptics and sound for significant moments. (4:30)
4. Test on a physical iPhone 8 or later with the silent switch off. (6:30)
5. Match a continuous visual change to a continuous haptic, not three transients. (9:00)
6. Loop a texture with the advanced player instead of a short pattern that stops. (13:00)
7. Match haptic density to visual density. A dense pattern wants a fine texture. (14:00)

What this session does not say: no intensity, sharpness, or timing values, and nothing on the system feedback generators.

## 10. Get started with Dynamic Type

WWDC24, session 10074. https://developer.apple.com/videos/play/wwdc2024/10074/

1. Test at all 12 sizes, 7 default and 5 accessibility. (Introduction, 1:30)
2. Use a text style, never a fixed font. (Scaled text, 3:00)
3. In UIKit set adjustsFontForContentSizeCategory and a line count of zero. (Scaled text, 4:00)
4. Check for truncation and clipping with the Xcode Dynamic Type variants and the accessibility audit. (Scaled text, 5:00)
5. Switch a horizontal stack to vertical at accessibility sizes. (Dynamic layouts, 7:00)
6. Keep decorative images unscaled and wrap text beneath them. (Images and symbols, 9:30)
7. Drop a purely decorative view at the largest size only if nothing essential goes with it. (Images and symbols, 9:30)
8. Scale an essential image with ScaledMetric or a symbol configuration. (Images and symbols, 11:00)
9. Do not let a bar grow with large text. Add the large content viewer to any custom bar instead. (Large content viewer, 12:30)
10. Let the large content viewer gesture win over the control's own recognizer. (Large content viewer, 14:00)

What this session does not say: no point sizes, and nothing about Dynamic Type on macOS.

## 11. The details of UI typography

WWDC20, session 10175. https://developer.apple.com/videos/play/wwdc2020/10175/ No chapters.

1. Prefer the predefined instances of a variable font over its sliders. (8:00)
2. Leave kerning alone. (10:30)
3. Apply the tracking table for each point size in SF comps, with new values from 17 to 28 points. (11:00)
4. Use the tracking API, not kerning, to tighten a string. (12:00)
5. Prefer automatic tight tracking and let the string truncate past that range. (12:30)
6. Use the emphasized variant for a heavier weight, not a hand picked weight. (17:30)
7. Use tight or loose leading, which moves line height by 2 points. (19:00)
8. Pass the rounded or serif design when you construct a SwiftUI font. (21:00)
9. Use `system-ui`, `ui-rounded`, `ui-serif`, or `ui-monospace` in CSS for web views. (21:30)
10. Scale a custom font with UIFontMetrics or relativeTo, and scale spacing with ScaledMetric. (25:30 and 28:00)
11. Make custom tracking size specific. (30:00)

What this session does not say: no SF size table, and no line height table beyond the 2 point shift.

## 12. Liquid Glass showcase: Tide Guide

Meet with Apple, session 257, published 18 December 2025. https://developer.apple.com/videos/play/meet-with-apple/257/ No chapters.

1. Give every button a touch down state and a loading animation. (3:00)
2. Use the identity glass variant on a surface that should look plain until touched. (4:30)
3. Replace a scale on press with the interactive glass effect so cards match the platform. (5:00)
4. Use glass as a highlight on a scrubbed value and on an empty state animation. (5:30)
5. Replace a nested context menu that dismisses on each choice with a glass popover. (6:30)
6. Collapse the popover back into its ellipsis button. (7:30)
7. Align the leading edge of every row so color and icon read the action. (8:30)
8. Ship padding and hierarchy changes to older OS versions too. (9:30)

What this session does not say: no API names, and no numbers.
