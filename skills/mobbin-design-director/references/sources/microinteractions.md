# Microinteractions — source dossier

Dan Saffer, *Microinteractions: Designing with Details* (O'Reilly, 1st ed., 2013;
foreword by Don Norman). The supplied copy is a 277-page ebook conversion with
no printed page numbers. Its copyright and revision pages give 2013 and a first
release of 2013-04-25. All page references below are one-based **PDF pages of
the supplied file**; another copy of the book paginates differently. See the
[coverage manifest](microinteractions-coverage.json) for the file hash, read
ranges and actual visual checks.

This is original synthesis, not extracted text or a reproduction of figures.
Three bounded readers studied all substantive text and inspected the rendered
figures that bear on a lesson. The book is a craft text: its evidence is mostly
2011–2013 product screenshots, designer anecdotes and three hypothetical worked
examples. It contributes a precise vocabulary for small, contained moments
(trigger, rules, feedback, loops and modes) and specification checks the other
books state only in general. It is not stronger evidence than this skill's
existing sources for user needs, accessibility or measured performance. The
[microinteraction workflow](../microinteractions.md) operationalizes the
incremental lessons without requiring the PDF during use.

## What is retained without a duplicate principle

| Source pages | Existing home / distinction |
|---|---|
| 6–9: foreword (error message with no remedy; a car that restores each driver's settings) | PU-16, AF-24 and DI-23 already require a concrete recovery route; AF-09 owns considerate assistance. |
| 22–30: sign-up, password and translation examples; polish and cross-device consistency | DI-22, PU-24, UX-08. Illustrations without a new mechanism; market-failure claims are opinion. |
| 31–37: history (modeless cut and paste, scrolling, buttons, remotes, sensors) | LU-01/LU-02 own learned expectations; modelessness is carried by MI-15. |
| 47–50: three ways to work; Signature Moments | DI-01 and RU-01 own scope; MI-18 keeps only the "usually no signature moment" default. |
| 53–56: vending-machine idle screen (whole screen accepts the touch; one question per screen) | TD-16 and LU-03 own effective hit regions; DI-08 owns stepped guidance. The speed claim is a designer anecdote. |
| 61–64, 131–136: prefilled fields, minimal choice, simple icons | DI-21, DI-22, PU-03, LU-07, DI-14. MI-09 keeps only the labelled-default and meaningful-option checks. |
| 79–85, 142–145: labels and microcopy | PU-15, PU-22, IA-09/10, JJ-14. "Label only when needed" never removes an accessible name from an icon-only control. |
| 120–122, 137–142: constraints, forgiving input, error prevention | AF-14, AF-17, LU-09, DI-23. Silently replacing offensive input changes intent and conflicts with AF-14. |
| 128–131: Tesler's law; computers absorb calculation and memory | LU-17, JJ-13. |
| 151–155: slot machines and intermittent reward | LU-23. Saffer's own conclusion is predictable, consistent feedback for ordinary moments. |
| 175–181: animation purpose, direction and duration | UX-10, AF-13, DI-13, AF-22. Keep the distinction that an element leaves along the path it entered and matches its gesture; honour Reduce Motion. Duration-halving is a craft heuristic. |
| 181–182: accurate messages; no bare "error" | PU-16, AF-24, LU-12. |
| 185–186: recorded speech versus synthesis | Voice UI is outside current scope; only the "action last" prompt order is kept in MI-12. |
| 214–218: tailored task form, defaults with Change links, price distribution beside the input | DI-21, PU-03, DD-04. |
| 224–225, 228–229, 235: match candidates, tab-title badge, look-alike objects, welcome-back summary | JJ-12, IA-17, JJ-05, AF-21, PU-05, IA-04. Red/green-only states fail without a second cue. |
| 231–234, 240–241: prototype on the platform; storyboards and keyframes | UX-18 and ID-17 own fidelity by question; MI-19 keeps the coupled-behavior argument. |
| 238–239: closing essay | ID-06, UX-16. Motivational, no new rule. |
| 245–246: statistical versus practical significance | UX-21, ID-27, DD-05. |

## Contextual source cards

### MI-01 — Specify a small moment from its end-state goal as written rules

- **Trigger:** A contained feature (mute, follow, save, add to cart, snooze, sync) exists only as a mockup, or a learned behavior is about to change.
- **Author's account:** Saffer treats each single-purpose moment as its own design object with four parts: what starts it, the rules it runs, the feedback that makes those rules perceivable, and the meta-rules for repetition, duration and modes. He frames the goal as the end state (being woken, being signed in) rather than a step, lists the rules in order, then adds the nuance branches. A flowchart of the rules exposes logic errors; if the team cannot write or diagram the rules simply, people cannot form the model either. His worked examples run the same pass: goal, rules, trigger, what is already known, controls, feedback, loops and modes, then a revised rule list.
- **Rationale / application:** Before visual work, write one line of goal and a short rule table: trigger, preconditions, branches (already added, offline, signed out), what the person can cancel or undo, and the end state. Annotate each rule with its feedback and any loop. Run the platform-constraint check early (background limits, notification permissions, Live Activities, tab visibility). When replacing a learned rule, confirm the new value is apparent at once or keep the old path.
- **Exception / conflict:** The four parts are a design lens, not an empirical taxonomy, and the cautionary macOS Save As story is a 2011–2012 case. A rule table does not replace journey, object or information-architecture modeling.
- **Review:** Can the team state the goal in one line and show every rule and branch, including the end state and what can be cancelled?
- **Source / dating:** Ch. 1 pp. 19–25, 37–47; Ch. 3 pp. 99–112; worked examples pp. 219–231. Figure p. 111 is a plain flowchart of label rules, not a notation requirement. iOS 6 platform limits in the examples are dated.

### MI-02 — Show what a mode or setting does not cover after its confirmation fades

- **Trigger:** A silence, pause, focus, privacy or "do not disturb" control has carve-outs, or its only evidence is a brief overlay.
- **Author's account:** The book opens with a concert stopped by an alarm on a phone whose owner had flipped the mute switch: the device's rule let sounds the owner had scheduled still play. The rule was hidden and the lasting state indicator was minimal. Saffer argues that a different rule would require different feedback; both are deliberate choices, not defaults.
- **Rationale / application:** Where a person sets the mode, state its exceptions (alarms, allowed people, security email, mentions). Keep a persistent state indicator after the transient confirmation ends, and make it reachable by assistive technology. Examples: Focus and Silent mode exceptions on iOS; "mute thread" or "pause notifications" on web stating what still arrives.
- **Exception / conflict:** One news anecdote, and the author takes a side on which rule is right. Hardware details are dated (later iPhones replace the switch with a configurable button); verify current platform indicators instead of citing the book's description.
- **Review:** At the moment of setting and afterward, can the person see what this mode does not silence, pause or hide?
- **Source / dating:** Ch. 1 pp. 19–21, 37–47, 51.

### MI-03 — Set each trigger's visibility by breadth, frequency and consequence

- **Trigger:** Deciding whether an action is a persistent control, a contextual control, a menu item or a gesture; or a frequent action is buried.
- **Author's account:** Saffer adapts a three-tier rule: actions most people use often should be highly discoverable, actions some people use sometimes easily discoverable, and rare actions for few people may take some searching. He ranks trigger forms from most to least discoverable (moving element, affordance with label, label with icon, icon alone, menu item, nothing) and calls a drop-down menu item close to invisible. Motion and sound capture attention involuntarily, so they suit high-priority triggers, with repeated motion reserved for errors and alerts. Some triggers must be global; others belong only in context, such as a formatting bar that appears with a selection.
- **Rationale / application:** Estimate share of users, frequency and consequence, then pick a tier: toolbar or primary button; contextual control tied to a selection or state; overflow menu; shortcut that duplicates a visible route. Check that no frequent action lives only in an overflow menu or gesture and that rare, consequential settings remain findable in a stable location.
- **Exception / conflict:** The tiers and the ladder are rules of thumb, not measured thresholds. A rare but urgent action (stop sharing, cancel a payment) may need high visibility. Motion as a discoverability cue must respect Reduce Motion and WCAG 2.2.2.
- **Review:** Is each action's visibility justified by breadth, frequency and consequence, with no frequent action reachable only through a menu or gesture?
- **Source / dating:** Ch. 2 pp. 38–39, 54–58, 62–64, 97. Perception timings on p. 63 rest on old indirect studies and are not timing rules.

### MI-04 — Put the most-sought current state on the trigger itself

- **Trigger:** A control launches something with live state (messages, a download, a timer, sync, a value) and people open it just to check.
- **Author's account:** Under the principle of bringing the data forward, the trigger shows what is inside before or while it runs: market direction on a stocks icon, progress on a download icon, time remaining on an appliance button, the next track on hover. The designer must know the single most valuable item. The trigger then becomes ambient information that may prompt use or make it unnecessary.
- **Rationale / application:** Identify the one fact people most often open the feature to learn and render it on the entry point: a badge, a progress ring on the button that started the task, the current value on a settings row, Live Activities or a widget for an ongoing task, a tab-title count on web. Expose the same value and changes to assistive technology.
- **Exception / conflict:** Hover previews do not exist on touch and cannot be the only route (WCAG 1.4.13 governs hover content on web). Ambient counts can drive compulsive checking, so badge only what a person would act on (LU-23). Stale data misleads; show freshness or hide the value when unknown.
- **Review:** Does the entry point show the one current fact people most often open it to learn, with that fact also available without hover and to assistive technology?
- **Source / dating:** Ch. 2 pp. 59–60, 75–78, 97. Example products are discontinued.

### MI-05 — Treat invisible triggers as shortcuts with a visible route and an off switch

- **Trigger:** A design adds a gesture, shake, long press, voice command, keyboard shortcut or sensor trigger with no on-screen cue.
- **Author's account:** Saffer accepts hidden triggers to avoid clutter but says invisibility should follow from context or technology, never be a goal. A hidden trigger must be learnable (available everywhere or under clear conditions), guessable, or met during a related action, as when pulling a list past its top reveals refresh. A high-priority action should not have only an invisible trigger. He distinguishes operational simplicity (one control per command) from perceived simplicity (one control doing several things) and treats redundant shortcuts as accelerators for frequent users. A rendered example (p. 69) explains a shake gesture the first time it fires and states how to turn it off.
- **Rationale / application:** List the visible equivalent of every hidden trigger (button, menu item, context-menu entry, VoiceOver custom action). Keep availability consistent or tied to an obvious condition. On first firing, especially an accidental one, say what happened and how to disable it. This aligns with WCAG 2.5.1 (single-pointer alternative), 2.5.4 (motion actuation alternative and disable) and 2.1.4 (character shortcuts).
- **Exception / conflict:** What is guessable shifts with convention; pull-to-refresh was novel in 2013. Always-listening voice raises consent and privacy issues the book does not address. Many example products are discontinued.
- **Review:** Does every hidden trigger have a visible, single-pointer equivalent, and does a motion or shortcut trigger explain itself when it first fires and offer a way to turn it off?
- **Source / dating:** Ch. 2 pp. 64–75; Ch. 3 pp. 127–128, 136–139. Figures pp. 66 and 69 inspected.

### MI-06 — Give each system-initiated trigger rules, indicators, an in-place off switch and a manual twin

- **Trigger:** Something starts without a direct action: an arrival, a location or time condition, background sync, a sensor or clipboard detection, another person's action, or one step completing and starting the next.
- **Author's account:** Saffer lists system-trigger sources and says each automatic trigger needs a way to adjust or disable it, ideally where it fires and at least in settings, plus a manual equivalent (sync now) for reassurance and for when automation fails. Its rules must answer how often it fires, what known context tunes it (fewer at night), what shows that it is about to happen, is happening and has happened, and what it does on failure. One rendered example offers a rotation-lock control right after a quick accidental rotation; another proposes the drive home and proceeds after a visible countdown.
- **Rationale / application:** For each automatic behavior specify the firing condition and frequency cap, suppressing context, before/during/after indicators, failure and retry policy, an in-place control ("Stop suggesting this", "Turn off for this thread"), a settings home, and the manual trigger. When behavior signals a likely mistake, offer the relevant setting inline.
- **Exception / conflict:** An auto-proceeding countdown needs a visible timer and an equally easy cancel, must give enough time (WCAG 2.2.1), and never applies to consequential or irreversible actions. Reading the clipboard is now a permission and privacy decision. Some notices (security, legally required) cannot be disabled; say so.
- **Review:** For each automatic behavior, are its frequency, indicator states, failure policy, in-place off control and manual equivalent all specified?
- **Source / dating:** Ch. 2 pp. 42, 85–97. Figures pp. 93 and 96 inspected; the countdown on p. 96 appears only in the figure, not the text. The claim that most triggers will soon be system-initiated is a 2013 speculation.

### MI-07 — Match the control to state count and risk, and define every state on it

- **Trigger:** Choosing a control, a control behaves differently by context, or its states are drawn in one static frame.
- **Author's account:** Saffer maps control type to state structure: a button for a one-shot action, a switch for two states (a plain button that silently changes state is worst), a set of buttons or a dial for a few discrete states, a slider for a continuum, paired steppers for an unbounded value. A trigger should do the same thing every time, and a control must work the way it looks. Every interactive object needs at least an inviting default, an active state during interaction and an updated state afterward; drag and drop also needs a dragging state and a screen state that shows valid drop areas. Indicators and expansions stay on the trigger. Frequent continuous adjustment can share one control, but a fast, error-intolerant action such as a call's mute should never be folded into a volume control.
- **Rationale / application:** Start from the platform component: `Toggle`/`UISwitch` or `role="switch"` for binary; segmented control, menu or radio group for few options; `Slider`/range input for ranged; `Stepper` for increments. Define default, focus, pressed, working, disabled with reason, error, current value and empty states on the control itself, including container states during drag. Keep a working indicator on the submit button and anchor any expansion to it. Keep safety- and privacy-critical toggles as dedicated, labelled controls. If an action changes with context, its label or icon must change too.
- **Exception / conflict:** The book's state diagram (p. 61) shows only pointer states; keyboard focus, touch press and disabled-with-reason are required now (WCAG 2.4.7). Accepted platform conventions outrank the invariance rule (tapping the active tab scrolls to top or pops to root). Hardware dials are illustrations to translate, not copy.
- **Review:** Does the control fit the action's state count and risk, do the same thing on every activation unless its label changes, and have every state defined on the control itself?
- **Source / dating:** Ch. 2 pp. 57–64, 75–79; Ch. 3 pp. 115–120, 136–139. Figures pp. 61, 82, 114 and 117 inspected; p. 114 hides an option until use, which conflicts with LU-18, and p. 117 includes a dimming-only state cue.

### MI-08 — Start from known context, then apply a harm test

- **Trigger:** A moment opens with blank fields, generic defaults or identical behavior for every person and situation.
- **Author's account:** After the trigger, Saffer asks what is already known: platform, time, location, battery, calendar, time since last use and past behavior. Examples raise brightness to display a ticket code and tailor download steps to the browser. He sets a limit: data that could embarrass, shame or endanger people should not be collected. Later he advises transparency about collection but not announcing each collection as in-the-moment feedback.
- **Rationale / application:** Prefill from legitimate context (AutoFill and content types, `autocomplete`, locale formats, last-used option). Change device state only for the screen's purpose and restore it on exit. Run the harm test for health, location, finance and household data, and keep every inferred value visible and editable.
- **Exception / conflict:** Not announcing collection is acceptable only when disclosure and consent happen elsewhere (permission prompts, privacy labels, settings); it is never licence for unannounced collection (AF-09, ID-07). The claim that tracking costs nothing ignores battery, data cost and privacy law. The book's blocking alert for the brightness change is one the author himself calls probably unnecessary.
- **Review:** Does the first state use context the product legitimately holds, and would any inferred value embarrass or endanger the person if shown or wrong?
- **Source / dating:** Ch. 3 pp. 121–128; Ch. 4 pp. 169–170. Figure p. 124 inspected.

### MI-09 — State the value each default applies, and keep only options that change outcomes

- **Trigger:** A moment applies a hidden default (snooze length, sharing scope) or offers options of uncertain value.
- **Author's account:** Every option adds at least one rule, and fewer rules make a clearer moment. Saffer favours smart defaults and emphasising the likely next action, and prefers a snooze label that names its duration to a bare verb. A choice is meaningful only if it changes an outcome the person can later use; a highlight colour that cannot be searched or exported fails. A choice that rewrites how the whole moment behaves is really a mode.
- **Rationale / application:** Put the default's value in the label or result ("Remind me in 1 hour", "Share with 3 people"). Offer alternates through a menu beside the primary action, and on web make the default the form's submit target. Show derived values instead of asking people to compute them. Remove options that change nothing.
- **Exception / conflict:** His one-major-option limit is opinion. Making the likely action dominant conflicts with PU-17 and JJ-16 when choices are equally valid or the "likely" choice serves the business; never make a destructive default dominant (PU-20). Auto-performing the next step must stay reversible (AF-17). Usage and cost figures on p. 134 are second-hand press reports.
- **Review:** Does each default state the value it applies, and does each remaining option change an outcome the person cares about?
- **Source / dating:** Ch. 3 pp. 128–136, 139.

### MI-10 — Specify algorithm inputs and tunable variables as design decisions

- **Trigger:** A moment depends on ranking, suggestion, scoring, autofill or a computed metric.
- **Author's account:** Saffer asks designers to help define such algorithms in four parts: sequence, decisions, repetition and variables. Named variables let the team tune without rewriting, and telling people which variables drive a result lets them adjust their behavior; an unexplained activity score is his counter-example. The algorithm should encode the person's intent and values, not efficiency alone.
- **Rationale / application:** In the specification, list the inputs, exclusions, ordering, refresh cadence (per keystroke, debounced) and the tunable values. Where people can act on it, offer a short "why this" or score breakdown and a way to correct an input.
- **Exception / conflict:** Written before learned ranking; explanations of learned models must be honest and must not imply control that does not exist (ID-14). The book gives no evidence that disclosure improves outcomes.
- **Review:** Are the algorithm's inputs, exclusions and tunable values written down, and can a person see and correct the inputs that matter to them?
- **Source / dating:** Ch. 3 pp. 146–148.

### MI-11 — Decide which rule events must, could and should not produce feedback

- **Trigger:** Specifying feedback, especially for background or system-initiated work.
- **Author's account:** Feedback exists to reveal the rules, and Saffer asks for the least feedback that keeps the model working. It must follow every manual trigger or adjustment, system changes that matter (new mail, not every check), reaching the edge of a rule (end of a list, wrong password), a command that cannot run, and long critical work. It could mark the start or end of a process or mode. Sometimes it should say what did not happen, such as confirming that sharing did not subscribe the person to a mailing list.
- **Rationale / application:** Derive a feedback table from the MI-01 rules: event → message type → channel → location. Suppress no-change polls; announce meaningful arrivals with a badge or a polite live region. Retry transient network failures quietly, then show an inline, actionable error. State non-effects where people fear side effects.
- **Exception / conflict:** Delaying an error until retries fail must never hide a lasting failure or lose input (AF-24, DD-27). Minimal feedback still needs programmatic announcements for state changes.
- **Review:** Does every user-initiated action get acknowledgement, and do only the background events that change what the person can do produce feedback?
- **Source / dating:** Ch. 4 pp. 155–161.

### MI-12 — Scale feedback channels and intensity to consequence and frequency

- **Trigger:** Choosing animation, sound, haptics, blinking or repetition for a feedback event.
- **Author's account:** Each added channel increases intrusion. Saffer makes more important feedback more prominent and multichannel, and frequent feedback less intrusive; blink only when attention is required. Feedback should map to its action rather than be arbitrary. It has its own rules: context (quieter at night), duration and dismissal, intensity and escalation, and repetition. Sound suits screenless devices, background events and moments when looking is unsafe; his foghorn test asks whether people would want to know about the event when they cannot see the device, and even then offers a way to turn it off. Earcons should be brief, distinct per event and never looped; haptics carry little information and work best enhancing a physical action or replacing unwanted sound.
- **Rationale / application:** Define a small feedback scale in the system: inline visual → visual + haptic → visual + sound + haptic → interruptive alert, and map events by consequence and frequency. Specify duration, dismissal, escalation and repeat limits. On iOS use the semantic feedback generators or `.sensoryFeedback` for selection, success, warning and error rather than ad-hoc patterns, and let system sounds follow Silent mode and Focus. On web avoid autoplaying sound. Keep every meaning carried by sound or haptics visible as well, and honour Reduce Motion.
- **Exception / conflict:** Some people keep sound and haptics off, so no meaning may depend on them (JJ-04, TD-21). The multimodal advantage rests on one 1989 study, and the haptic-level and earcon figures come from 1969–2004 sources; current haptic engines are finer, though the low-bandwidth point stands.
- **Review:** For each event, are channel count and intensity justified by consequence and frequency, with duration, dismissal and repetition specified and a visual equivalent present?
- **Source / dating:** Ch. 4 pp. 163–164, 174, 183–191. Figure p. 190 inspected.

### MI-13 — Carry feedback in UI that already exists before adding new elements

- **Trigger:** A state needs to be shown and the instinct is to add a banner, badge, label or dialog.
- **Author's account:** Saffer uses overlooked parts of the interface as carriers: cursors, scrollbars, progress bars, tooltips and the control itself. His examples include a cursor that shows italics while typing in italics, a cart count inside the cart button, a resize cursor that shows a blocked direction and a scroll edge that deforms at the end of a list. Visual feedback belongs near the point of input; an error at the top of a long form is missed when the button is at the bottom.
- **Rationale / application:** Show state on the control (a button that shows its own progress, a filled symbol variant for on, a badge on the tab item, overscroll bounce). On web, change the button's own label and state, use `aria-busy`, and place errors beside fields with `aria-describedby`. Change the icon and the accessible name together.
- **Exception / conflict:** Cursors do not exist on touch and are invisible to screen readers, tooltips are hover-only, and a finger can occlude feedback on the control (TD-13); none can be the only signal.
- **Review:** Before adding a new element, was the existing control, scroll edge or progress area considered as the carrier, with an equivalent accessible announcement?
- **Source / dating:** Ch. 3 pp. 106–107; Ch. 4 pp. 156–159, 164–165, 175. Figure p. 179 inspected. Cursor and overscroll examples are 2011–2012 platform versions.

### MI-14 — Keep personality to rare, low-stakes moments

- **Trigger:** Writing playful copy, mascots, faces or jokes into feedback, errors or waits.
- **Author's account:** Feedback can carry character, and brief moments work best in tense spots such as long waits or dead ends. Overdone personality turns creepy or tiresome and raises expectations of intelligence, so Saffer aims for a veneer. He rejects attitude on frequent paths such as sign-in and mockery of a forgotten password, and notes a smiling face on an empty inbox misfires when the message may not be happy.
- **Rationale / application:** Limit humor to infrequent, low-stakes moments (empty states, long uploads, over-pull) and keep the functional status plain beside it. Never joke where money, data or safety is at stake. Check tone across localization, and do not let an AI feature's first-person voice overclaim ability.
- **Exception / conflict:** His preference to avoid "you" in errors is a style choice; follow the project's and platform's writing guidance. Humor ages and translates poorly, and a joke never replaces a useful next action.
- **Review:** Is any personality limited to rare, low-stakes moments, with the plain status and recovery clear on its own?
- **Source / dating:** Ch. 4 pp. 161–169, 182, 187–191. Figures pp. 162 and 190 inspected; on p. 190 the joke is decoration while the real status is the spinner and its label.

### MI-15 — Admit at most one mode, and prefer transient modes with a non-hold path

- **Trigger:** A design adds an edit, select, settings or alternate-command state that changes what the same controls do.
- **Author's account:** A mode forks the rules and invites errors, so Saffer allows a microinteraction one mode at most, preferably none, and only for an infrequent subtask that would otherwise clutter the main purpose. A necessary mode gets its own screen and a transition in and out, and on return the main view is unchanged apart from the edits. Two lighter forms cannot trap people: a spring-loaded mode lasts only while a physical action continues, and a one-off mode ends after one command. Modes entered by a wake word or gesture need a timeout. In one worked example a long press on an existing button replaces a look-alike extra button, with a printed hint.
- **Rationale / application:** Put configuration in a sheet or pushed view with explicit Done or Cancel rather than an in-place toggle that repurposes taps. When a list edit mode changes what a row tap does, show a persistent mode bar with count and exit. On exit, keep scroll position, selection and filters and show the changed item. Hold-to-act needs a visible hint, visible duration while held, and an equivalent menu item or accessibility action.
- **Exception / conflict:** Strongly signalled in-place edit modes are current platform convention (table edit, multi-select) and acceptable. The one-mode cap is an uncited heuristic. Press-and-hold and held-key modes are hard with motor impairments, switch control and screen readers. A separate screen can lose context on large web layouts, where an inline panel may serve better.
- **Review:** Mid-task, can people tell which mode they are in and how to leave it, does leaving restore their view plus their changes, and does every held mode have a non-hold path?
- **Source / dating:** Ch. 5 pp. 196–202, 213; applied pp. 222, 229–231. Figure p. 199 inspected (iOS 6-era edit screen with explicit exit).

### MI-16 — Write each loop's kind, end condition and visible time window

- **Trigger:** A rule says every, until, after N or for each: retries, polling, timeouts, auto sign-out, rate limits or idle prompts.
- **Author's account:** Saffer uses loop for any repeating cycle that sets a moment's pace and lifespan: count-controlled, condition-controlled, collection-controlled and infinite, either fixed or adjusting to feedback. Too few cycles feels rushed, too many sluggish. Uses include a visible countdown for editing an order before it prints, security timeouts, rate warnings and offering help when a wait stalls. His worked examples cap every unbounded loop: an alarm that stops on its own, a playlist with a song limit, an appliance that resets after being left open.
- **Rationale / application:** For each loop write the kind, interval, maximum count or end condition, what people see each cycle and what happens at the end. Examples: retry with backoff then a clear error and Retry; polling that pauses when the tab is hidden; an undo-send or order-edit window shown as remaining time; session expiry with warning and extend; a "still working" message after a threshold.
- **Exception / conflict:** Time limits must meet WCAG 2.2.1 (warn, extend or justify). The rate-limit example (p. 205) is accusatory and adds a CAPTCHA; it illustrates a loop rule, not good copy or accessible design. All specific durations and counts are illustrative.
- **Review:** For every repeating or timed rule, is the end condition written down, and is any time-bound window visible with a way to act or extend before it closes?
- **Source / dating:** Ch. 5 pp. 202–206, 213; applied pp. 222–223, 226, 229–231. Figures pp. 204–205 inspected.

### MI-17 — Design the repeat visit: remember visibly, stop when declined, reduce reversibly

- **Trigger:** A recurring interaction starts from zero every time, a "remember" control does not remember, or a design plans to hide guidance as people gain experience.
- **Author's account:** Because moments can hold memory, Saffer designs long loops that improve over repeated use: fading recent additions, marking recent searches, temporary unsubscribe. He calls the unreliable remember-me checkbox a broken loop. In a worked example the app offers a repeated alarm on launch, keeps offering while accepted and stops when declined. He prefers a consistent default rule over an intermittent clever one. Progressive reduction removes labels and emphasis as skill grows (one rendered button loses its label, then its prominence), and the interface may need to become explicit again after a period of disuse.
- **Rationale / application:** Prefill last-used values visibly and editably. Offer an inferred repeat as a dismissible suggestion, not an automatic action. Treat persistence controls (keep me signed in, don't show again) as testable promises. Reduce hints only after successful use, keep an icon-only state's accessible name and target size, and restore guidance after long absence or a redesign; removing a control by non-use needs a restore path.
- **Exception / conflict:** Memory raises privacy and shared-device concerns; offer a way to clear it. The long-term-value framing leans on loyalty, and scarcity emails (p. 210) or nag loops can become manipulative; agency outranks engagement (LU-23). Per-user layout changes hurt support, documentation and muscle memory. Evidence is anecdotal; the reduction example is one company with no data. Overlaps LU-18 on disclosure; MI-17 adds the reduction and reversion checks.
- **Review:** On the third visit, what does this moment already know, is that knowledge visible and editable, does a declined suggestion stop recurring, and how does reduced guidance come back?
- **Source / dating:** Ch. 5 pp. 206–212, 213; applied pp. 220–223, 226, 230, 238; test prompt p. 246. Figures pp. 210 and 212 inspected.

### MI-18 — Map neighboring moments and their handoffs before polishing one

- **Trigger:** A feature contains several small moments, or one is being refined in isolation.
- **Author's account:** For larger features Saffer lists the microinteractions, draws a map of which ones touch or trigger which, and checks the handoffs between them. He then decides which, if any, earns a signature moment; usually none should, especially gateways such as sign-in. A closing checklist for dull moments asks about known context, data brought forward, error prevention, hidden expert shortcuts, human copy, motion, extra feedback channels and long loops.
- **Rationale / application:** Draw a small neighbor map (list ↔ scroll ↔ search ↔ item actions) and note conflicts, shared gestures and state handoffs before detailed design. Default to no signature moment; give expression to one only when it serves identity without slowing frequent work. Use the checklist as a review pass, not a mandate to add every item.
- **Exception / conflict:** The map (p. 236) is an informal adjacency sketch, not a flow model; [flows](../flows.md) still owns journeys. The checklist invites ornament if applied indiscriminately (ID-06, DI-13).
- **Review:** Can you name every neighboring moment this one hands off to or conflicts with, and justify any signature treatment?
- **Source / dating:** Ch. 1 pp. 47–50; Ch. 6 pp. 234–238. Figure p. 236 inspected.

### MI-19 — Test the coupled behavior at high fidelity and trace symptoms to causes

- **Trigger:** Planning a usability test, A/B test or analytics for a control or short flow.
- **Author's account:** Saffer assumes the concept is needed and tests flow and structure, which needs the highest-fidelity prototype available because trigger, rules, feedback and loops are tightly coupled. He validates the true goal, which data matters, whether copy is needed and clear, and timing including loop length; long loops need longitudinal study. He maps remarks to likely causes: no sense that anything happened points to missing or subtle feedback, not knowing where one is points to transitions or modes, and not knowing an action existed points to a hidden trigger. Measures include completion, overall and per-step time (geometric mean for skewed times), steps, errors split into slips and mistakes. Small differences need large samples, so analytics events complement sessions; data informs but does not decide. His protocol asks for expectations before exposure, unaided use, think-aloud, what the moment should remember tomorrow, and the one thing to fix, over at least two rounds.
- **Rationale / application:** Test the real component in code or a high-fidelity prototype, not static frames. Instrument start, each step, errors and completion. Report task time with a geometric mean, classify slips versus mistakes, and log symptom → cause → fix. Add the expectation and "remember tomorrow" questions to session guides.
- **Exception / conflict:** Sample-size figures are rough rules, not calculations, and the claim that only quantitative work can catch nuance overstates; sessions still find causes. Asking people to explain the rules can teach them the answer (UX-23). A/B tests on consent or pricing raise ethical concerns. Metrics never override agency.
- **Review:** Does the plan say which of goal, data, copy and timing it validates, at what fidelity, and how each observed symptom will be traced to a cause?
- **Source / dating:** Ch. 6 pp. 231–234; Appendix A pp. 240–247. Figure p. 233 inspected (state storyboard). The analytics tool named is dated.
