# iOS craft: what the best apps do

Read this when you design or review a native iPhone screen and want checkable behaviors, each with a shipped example where one exists. [ios](ios.md) holds the verification loop and [ios-components](ios-components.md) picks the element. This file says what the top apps do with it.

Each bullet here is one line plus a source. For the full rule sets behind them read [WWDC digests](wwdc-digests.md) for the Apple sessions and [craft digests](craft-digests.md) for the designer essays. Read the digest before you apply a rule in a way the one-liner does not cover.

Baseline: iOS 26 shipped Liquid Glass (September 2025). iOS 27 shipped September 2026. Apple's doc says the `UIDesignRequiresCompatibility` opt-out is ignored when you build for iOS 27. An app that still shows the iOS 18 chrome is an app built with an old SDK. Source: https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility

## 1. What the Apple Design Awards rewarded, 2024 to 2026

- Interaction means fewer steps and focus off the screen. Example: Crouton (2024 winner) shows only the current cooking step. Davies: "I spent a lot of time figuring out what to leave out." Source: https://www.apple.com/newsroom/2024/06/apple-announces-winners-of-the-2024-apple-design-awards/ , https://developer.apple.com/news/?id=9x75y43e
- Interaction in 2023 meant system surfaces, not app screens. Example: Flighty won for Live Activities and Dynamic Island modeled on airport boards ("one line per flight"). Source: https://www.apple.com/newsroom/2023/06/apple-announces-winners-of-the-2023-apple-design-awards/ , https://developer.apple.com/news/?id=970ncww4
- Interaction in 2026 meant Liquid Glass done well. Example: Moonlitt won for "easy onboarding and best-in-class Liquid Glass integration". Tide Guide was a finalist. Source: https://www.apple.com/newsroom/2026/06/apple-reveals-winners-of-the-2026-apple-design-awards/
- Visuals in 2026 meant custom animation plus the system material. Example: Tide Guide won for "full-screen charts filled with custom animations, Liquid Glass integration ... sky-matching palette". (Not Boring) Camera was a finalist. Source: https://www.apple.com/newsroom/2026/06/apple-reveals-winners-of-the-2026-apple-design-awards/
- Visuals in 2025 meant touch and Pencil interaction as the visual. Example: Feather: Draw in 3D. Source: https://www.apple.com/newsroom/2025/06/apple-unveils-winners-and-finalists-of-the-2025-apple-design-awards/
- Delight and Fun means one small idea, delivered with care. Example: Bears Gratitude (2024), CapWords (2025), grug (2026). Source: https://www.apple.com/newsroom/2024/06/apple-announces-winners-of-the-2024-apple-design-awards/ , https://www.apple.com/newsroom/2025/06/apple-unveils-winners-and-finalists-of-the-2025-apple-design-awards/ , https://www.apple.com/newsroom/2026/06/apple-reveals-winners-of-the-2026-apple-design-awards/
- Indie apps reach the finalist lists. Example: Arc Search (2024 Interaction finalist), Copilot Money (2024 Innovation finalist), iA Writer and Mela (2025 Interaction finalists), Structured (2026 Inclusivity finalist). Source: https://www.apple.com/newsroom/2024/06/apple-announces-winners-of-the-2024-apple-design-awards/ , https://www.apple.com/newsroom/2025/06/apple-unveils-winners-and-finalists-of-the-2025-apple-design-awards/ , https://www.apple.com/newsroom/2026/06/apple-reveals-winners-of-the-2026-apple-design-awards/

## 2. Indie craft decisions

- Adopt the system material, then re-tune your own shapes. Example: Things 3.22 added "a touch of glass in the sidebar", "increased curvature of to-dos, dialogs, and controls", "wider spacing", and "glassy buttons that respond to touch with a subtle glow and scale". Things 3.21.6 "Improved haptic feedback when dragging a to-do." Source: http://culturedcode.com/things/support/articles/2409121/
- Put haptics on physical actions. Use white space and bold type. Example: a Things 3 review notes a Taptic "kickback" on certain actions, "bold fonts ... thoughtful splashes of color", and tasks that "pop out into a card". Source: https://www.macstories.net/reviews/things-3-beauty-and-delight-in-a-task-manager/
- Model a gesture on a physical control, and always give it a tap equivalent. Example: Halide swipes "like dials on a camera" and "one tap toggles manual". It ships a custom UI typeface, Halide Router, and a haptic on the level guide (1.1). Source: https://www.lux.camera/introducing-halide/ , https://www.lux.camera/halide-1-1-better-faster-stronger/
- Big feedback needs an intentional input. Example: the (Not Boring) Habits checkbox requires a long press with hold feedback, then a 3D animation, a custom sound, and custom haptics. "most games probably have two or three times" the feedback layers. Source: https://developer.apple.com/news/?id=9ab1g4r3
- "Fly instead of teleport." Example: Family trays have distinct heights per step, button labels morph (Continue to Confirm), a spinner moves into the tab bar to show where the pending item lives, and tab switches move in the tapped direction. Each tray carries "a singular piece of information or action per tray". Source: https://benji.org/family-values
- Use native controls, molded. Example: Copilot says "It's all native" and "we just tweak it a lot". Data is kept local "so the app is really responsive". Swift Charts draws the interactive charts. Source: https://developer.apple.com/articles/copilot-money
- Put glass only where a finger covers it. Example: Tide Guide put glass buttons on small day of week controls with haptics, replaced a card scale animation with interactive glass, and swapped a nested context menu for a glass popover. Their rule: "adopt and then redesign." Source: https://developer.apple.com/videos/play/meet-with-apple/257/
- Move controls to the bottom bar under Liquid Glass. Example: Apple's gallery text says Fantastical moved calendar and search controls into a Liquid Glass bottom toolbar. Unverified, seen in a search snippet only. MacRumors confirms Fantastical and Carrot Weather are in the gallery. Source: https://developer.apple.com/design/new-design-gallery-2026 (snippet only), https://macrumors.com/2026/04/06/apple-liquid-glass-design-gallery-update/
- Soften, do not re-skin. Example: Bear "softened the sidebar" and refreshed the toolbar and icons. Earlier the team said Liquid Glass "doesn't seem to be very compatible with our theming system." Source: https://community.bear.app/t/bear-update-os26-ready/18219 , https://community.bear.app/t/plans-for-ios-26-ipados-26-macos-tahoe/17302
- Rebuild for reach. Example: the Overcast 2024 rewrite was "optimized for easily-reached controls on today's phone sizes." Source: https://marco.org/2024/07/
- Use system behaviors wholesale. Example: Apollo shipped with 3D Touch, customizable gestures, Safari View Controller, "Using Apple's iOS design guidelines." Source: https://9to5mac.com/2017/10/23/apollo-beautiful-ios-reddit-client/
- Add one new gesture, built on a known one. Example: Arc Search pinch to summarize folds the page. "Once you try it, the behavior feels obvious." Source: https://spyglass.org/pinch-to-summarize/
- Use custom type only with a reason. Example: iA Writer Duospace widens only m, M, w, and W to keep the monospace rhythm. Source: https://ia.net/topics/in-search-of-the-perfect-writing-font

## 3. Liquid Glass (iOS 26 and iOS 27)

- Remove custom backgrounds from nav bars, tab bars, toolbars, and split views. Use the system components. Source: https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass
- Check the API list: `glassEffect(_:in:)`, `GlassEffectContainer`, `.buttonStyle(.glass)` and `.glassProminent`, `scrollEdgeEffectStyle(_:for:)`, `safeAreaBar`, `backgroundExtensionEffect()`, `ConcentricRectangle`, `tabBarMinimizeBehavior(.onScrollDown)`, `Tab(role: .search)`, `ToolbarSpacer`. UIKit: `UIGlassEffect`, `UICornerConfiguration`, `UIScrollEdgeElementContainerInteraction`. Source: https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass
- Keep glass in the navigation layer, never the content layer. "always avoid glass on glass". Tint only primary actions. Source for glass on glass: https://developer.apple.com/videos/play/wwdc2025/219/ . Use `.clear` only over media, with a 35 percent dim if the media is bright. Source for the number: https://developer.apple.com/design/human-interface-guidelines/materials (session 219 says a dim is needed but gives no percentage).
- Prefer the automatic scroll edge effect. Use it only under floating controls, one per view. Source: https://developer.apple.com/design/human-interface-guidelines/scroll-views
- Title case section headers. Grouped forms. Action sheets anchored to their source. Half sheets inset. Source: https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass
- Badly adopted glass looks like text over images, crowded tabs, controls that move or appear, motion with no purpose, and a search pill that fragments the tab bar. Source: https://www.nngroup.com/articles/liquid-glass/
- iOS 27 (secondary source, unverified against a WWDC26 session): a hard scroll edge by default with `.soft` restoring iOS 26, a user transparency slider, a `prominent` tab role on any tab, swipe actions outside lists. Source: https://designfornative.com/what-designers-need-to-know-about-ios-27/

## 4. Tells that an app feels like a web app

- Hidden hamburger navigation. Tasks run 15 percent slower on mobile and discoverability nearly halves. The HIG says a tab bar is for navigation and never hides it. Source: https://www.nngroup.com/articles/hamburger-menus/ , https://developer.apple.com/design/human-interface-guidelines/tab-bars
- A custom back button, or no edge swipe. HIG: "Use the standard Back and Close buttons". Shortcut gestures supplement, never replace. Source: https://developer.apple.com/design/human-interface-guidelines/toolbars , https://developer.apple.com/design/human-interface-guidelines/gestures , https://developer.apple.com/documentation/uikit/uinavigationcontroller/interactivepopgesturerecognizer
- No rubber band, or wrong scroll physics. HIG: custom scrolling must keep "the elastic behavior that people expect." Flutter's copy of the UIScrollView bounce is "close but not identical". Source: https://developer.apple.com/design/human-interface-guidelines/scroll-views , https://github.com/edde746/plezy/issues/2662
- A spinner where content could show. HIG Loading: "Show something as soon as possible". The wrapper tell is "a loading spinner where a native equivalent would already be rendering." Source: https://developer.apple.com/design/human-interface-guidelines/loading , https://www.techwelike.com/2026/09/real-app-vs-web-wrapper/
- A bottom sheet with no grabber or detents, or no swipe to dismiss. Source: https://developer.apple.com/design/human-interface-guidelines/sheets
- A switch outside a list row, or recolored without need. Source: https://developer.apple.com/design/human-interface-guidelines/toggles
- A toast instead of in place status. HIG: integrate status feedback into the interface. Confirm only significant actions. Source: https://developer.apple.com/design/human-interface-guidelines/feedback
- Context menus missing or inconsistent. Top menu actions must match swipe actions. Source: https://developer.apple.com/design/human-interface-guidelines/context-menus , https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass
- The keyboard covers the field. Use the keyboard layout guide. Source: https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards
- Safe area and Dynamic Type violations. Rows must grow and stacks must reflow. The check procedure is in [ios](ios.md). Source: https://developer.apple.com/design/human-interface-guidelines/layout
- Corners that are not continuous. Use `CALayerCornerCurve.continuous` (iOS 13 and later). Source: https://developer.apple.com/documentation/quartzcore/calayercornercurve/continuous

## 5. Typography and spacing

- Use the text styles. At Large: Large Title 34, Title 1 28, Title 2 22, Title 3 20, Headline 17 semibold, Body 17, Callout 16, Subhead 15, Footnote 13, Caption 1 12, Caption 2 11. Minimum 11 pt. Avoid Ultralight, Thin, and Light. Source: https://developer.apple.com/design/human-interface-guidelines/typography
- Let optical size happen. SF Pro transitions from Text to Display "between 17 and 28 points". The tracking tables are in Apple Design Resources. Source: https://developer.apple.com/videos/play/wwdc2020/10175/
- Use SF Rounded for "soft or rounded UI elements, or ... an alternative typographic voice": `Font.system(.body, design: .rounded)`. Use `.serif` for New York and `.monospaced` for SF Mono. Source: https://developer.apple.com/design/human-interface-guidelines/typography , https://developer.apple.com/videos/play/wwdc2020/10175/
- Match SF Symbols weights to the text. Fill variant in tab bars and swipe actions, outline in toolbars. Source: https://developer.apple.com/design/human-interface-guidelines/sf-symbols

## 6. Motion

- Use the platform spring. Springs are the SwiftUI default and `Animation.default` has been a spring since iOS 17. Write `.spring(duration:bounce:)`. Bounce is 0 by default. Use caution above 0.4. Gestures hand velocity to the spring automatically. Source: https://developer.apple.com/videos/play/wwdc2023/10158/ , https://developer.apple.com/documentation/swiftui/animation/default , https://nilcoalescing.com/blog/AnimationTimingInSwiftUI
- Respond instantly. Give continuous feedback. Stay interruptible and redirectable. Start at 100 percent damping and add overshoot only when the gesture has momentum. Example: Music uses 100 percent on tap and 80 percent on swipe. Project the fling endpoint with `UIScrollView.DecelerationRate`. Source: https://developer.apple.com/videos/play/wwdc2018/803/
- Use zoom transitions: `navigationTransition(.zoom(sourceID:in:))` plus `matchedTransitionSource`. UIKit: `preferredTransition = .zoom`. Source: https://developer.apple.com/videos/play/wwdc2024/10145/ , https://developer.apple.com/documentation/swiftui/view/matchedgeometryeffect(id:in:properties:anchor:issource:)
- Retarget in flight and keep velocity. Example: the Wave library. Source: https://github.com/jtrivedi/Wave
- Let destructive actions wait for the gesture to end. Lightweight ones commit mid swipe. Reduce animation on high frequency actions. A mistap must be interruptible. No motion on keyboard or mouse commands. Source: https://rauno.me/craft/interaction-design
- Ease out for enter and exit, never ease in. Under 300 ms. Transform and opacity only. Never animate a keyboard initiated action. Example: Family is cited as snappy. Source: https://emilkowal.ski/ui/great-animations , https://emilkowal.ski/ui/7-practical-animation-tips
- Bounce 0.1 to 0.3 or none. Popovers scale from the trigger, never from scale(0). Source: https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md
- Keep interactions at 200 ms or less. Press scale about 0.96, never 0.8. No weight below 400. Source: https://github.com/raunofreiberg/interfaces
- "Make motion optional". Keep feedback "brief and precise". Source: https://developer.apple.com/design/human-interface-guidelines/motion
- Nest corners concentrically. The inner radius equals the outer radius minus the border and padding, clamped at zero. Apple says controls nest "maintaining concentricity throughout the UI" (Apple quote, no URL in the research file). Source: https://dev.to/sgbp/the-concentric-border-radius-rule-why-nested-rounded-corners-look-slightly-wrong-3hog

## 7. Haptics and sound

- Use the system patterns by their documented meaning (success, warning, error. light, medium, heavy, rigid, soft. selection). Standard controls already play them. Match haptic sharpness to the animation. Short haptics for discrete events. Make them optional. Source: https://developer.apple.com/design/human-interface-guidelines/playing-haptics
- Causality, harmony, utility. "Don't add feedback just because you can." Source: https://developer.apple.com/videos/play/wwdc2021/10278/
- Let sound respect the silent switch through the audio category. Play the standard key click in custom input views. Source: https://developer.apple.com/design/human-interface-guidelines/playing-audio , https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards
- Apps that do it: Not Boring Habits (checkbox), Things (drag), Halide (level guide), Tide Guide (glass buttons). Source: https://developer.apple.com/news/?id=9ab1g4r3 , http://culturedcode.com/things/support/articles/2409121/ , https://www.lux.camera/halide-1-1-better-faster-stronger/ , https://developer.apple.com/videos/play/meet-with-apple/257/

## Unsourced

Treat any rule about these as belief, not evidence.

- No first person craft posts were found for Fantastical typography, Carrot Weather, Ivory, Amie, Retro, Darkroom (ADA 2020 winner only), Structured, Timery, Drafts, Pixelmator, or Craft (App Store Mac App of the Year 2021, not an ADA).
- Apple's new design gallery captions could not be fetched directly. Only one snippet (Fantastical) was seen.
- The iOS 27 design changes rest on one secondary blog plus the compatibility key doc. No WWDC26 session was read.
- Section 7 has no sourced example of an app that deliberately omits haptics.
- Things and Fantastical type settings (sizes, weights) are unsourced.
