# Touch Design for Mobile Interfaces — contextual source lessons

Steven Hoober. Smashing Media AG, 2021. ISBN 978-3-945749-97-5.
The supplied title/copyright pages identify the 2021 publication; no numbered
edition is stated. PDF creation metadata says 2024 and is not an edition date.
One-based PDF page = printed Arabic page + 1 for the chapter body. Some divider
and blank leaves have no visible printed numeral. [Coverage manifest](touch-design-coverage.json).

All 13 chapters and the master checklist were studied in bounded full-text batches.
Thirty-five consequential figure/table pages and one additional prose page were
rendered and inspected. This does not claim every image was inspected, the underlying
research was independently audited, or the author's findings were replicated.
Original PDF, extraction cache, and rendered book pages remain outside Git.

The cards distinguish the author's claims from our operational adaptations. They
extend the earlier books with physical context, actual hit regions, occlusion,
nearby-action consequences, and touch-sensitive disclosure. They do not override
user goals, approved product decisions, accessibility needs, or current platform
behavior. Use [touch](../touch.md) for the operational workflow and official links.

## Reconcile, do not universalize

Treat center-out behavior as a contextual research finding and design hypothesis,
not a reason to relocate every action or reject native bottom navigation. The
book's grip percentages, probability contours, physical measurements, fixed counts,
and historical OS examples are not universal thresholds. Distinguish visible
control size, actual hit region, physical units, logical points, and CSS pixels.
Source advice on fixed controls has costs and internal qualifications; inspect the
actual keyboard/chrome/content interaction. Prefer meaningful comparison and user
orientation over categorical bans on tables, cards, horizontal scrolling, or sheets.

These principles overlap intentionally with AF/DI/JJ/UX/WI: reuse their scenarios
and evidence rather than multiplying mandatory tests. Detailed provenance remains
here so normal skill use can retrieve an individual card without reopening the PDF.

### TD-01 — Define the supported device context from the audience

- **Trigger:** Choosing target platforms, breakpoints, a test device set, or a mobile research brief.
- **Author’s account:** The book challenges designers’ preferred-device assumptions, recommends an audience-specific device collection, and describes portable, fixed, and mixed-input uses across nominal device classes.
- **Rationale / application:** Our recommendation is to record who needs access, devices and browsers actually encountered, connection conditions, available inputs, and unsupported cases. Choose representative hardware from that evidence; include a mobile-network check when the task depends on one. Keep observed audience facts separate from market assumptions.
- **Exception / conflict:** A bounded native feature need not support every device ever sold. Explain its scope and provide an appropriate alternative where access matters; do not turn a book’s inclusion aspiration into an unbounded implementation demand.
- **Review:** Can each meaningful compatibility decision be traced to the task and audience, and has the essential route run on the selected device set?
- **Source / dating:** Ch. 1, printed pp. 21–34 (PDF 22–35), especially device-lab discussion pp. 24–27 (PDF 25–28); ch. 5, pp. 85–88 (PDF 86–89). Market shares, feature-phone prevalence, and predictions describe the author’s 2020/2021 context; they are not current planning inputs. The ChromeOS categorization argument is not needed to support this lesson.

### TD-02 — Check touch behavior on the actual hardware and in its environment

- **Trigger:** Field work, gloves, moisture, vibration, protective cases, styluses, or specialized touch hardware.
- **Author’s account:** Different sensing technologies and physical assemblies have different constraints; the book describes resistive panels requiring appreciable pressure and capacitive interactions affected by contact, gloves, and moisture.
- **Rationale / application:** Our recommendation is to identify the intended input hardware and test the real task with relevant accessories and operating conditions. Record missed or accidental activation, feedback, recovery, and available alternate input. A successful desktop simulation does not establish field performance.
- **Exception / conflict:** Do not assume every modern device shares the book’s stated sensor behavior, or ask users to compensate by pressing harder. Environmental checks should reflect credible use, avoid damage, and include the needs of affected users.
- **Review:** Can the person complete and recover from the task under the scoped conditions, with the equipment actually available?
- **Source / dating:** Ch. 2, printed pp. 51–55 (PDF 52–56); ch. 3, pp. 61–70 (PDF 62–71), especially pp. 63–65 (PDF 64–66). Technical descriptions and product examples are the author’s 2021 synthesis, not a current device specification or a validated medical explanation.

### TD-03 — Separate contact sensing, visible controls, and hand occlusion

- **Trigger:** Deciding target geometry, interpreting inaccurate taps, or placing feedback near a touched control.
- **Author’s account:** The illustrated contact patch, its center, and the area visually covered by a thumb are different. The author disputes using finger breadth as a direct proxy for required target size.
- **Rationale / application:** Our recommendation is to inspect the visible control, its actual hit region, neighboring targets, touch feedback, and obscured content separately. Test selection and correction in plausible grips; evaluate the required target dimensions and spacing under current applicable guidance. Do not derive a universal size from the pictured thumb or the sensor’s theoretical precision.
- **Exception / conflict:** The book’s categorical finger-size and touch-centroid claims exceed what these chapters establish. Firmware interpretation, accessibility needs, task consequences, and hardware vary. This lesson does not authorize smaller targets or removal of platform safeguards.
- **Review:** Are intended selection and recovery reliable, and can users perceive the result despite their hands covering part of the screen?
- **Source / dating:** Ch. 3, printed pp. 65–69 (PDF 66–70); ch. 4, pp. 78–80 (PDF 79–81). Contact/occlusion illustration PDF 67 and finger/contact illustration PDF 80 visually inspected. They are conceptual diagrams, not dimensional specifications or proof of zero correlation.

### TD-04 — Trace a design rule to its scope before translating it

- **Trigger:** Conflicting target-size advice, a borrowed checklist, or a claim that a familiar numeric rule settles a design choice.
- **Author’s account:** The book argues that standards can preserve assumptions about older sensors, workstations, and populations after their original context changes.
- **Rationale / application:** Our recommendation is to record the rule’s source, date/version, units, intended device and population, and whether it is binding or advisory. Distinguish a compliance constraint from an ergonomic hypothesis. When two rules appear to conflict, inspect what each measures and test the uncertain task behavior rather than voting among sources.
- **Exception / conflict:** Historical criticism is not permission to disregard current accessibility or platform requirements. The author’s old standards quotations and use of “44 px” must not be adopted as current normative guidance or silently converted into logical units.
- **Review:** Does the implementation satisfy the actual current requirement, and is any advisory departure explicit, justified, and checked?
- **Source / dating:** Ch. 4, printed pp. 73–82 (PDF 74–83). The 9.5 mm and 22–23 mm examples are quoted through a 2012 discussion of older standards; none is a recommended universal target here. Claims about standards’ unchanged status are dated author assertions, not independently re-audited facts.

### TD-05 — Preserve usability while grip, hand, and posture change

- **Trigger:** Primary-action placement, forms, long scrolling, reach assumptions, or a proposed universal thumb zone.
- **Author’s account:** Observations and examples show one-hand use, cradling, held-and-tapped use, two-hand use, surface support, and changes within a task. A single-thumb interaction is not synonymous with holding a phone in one hand.
- **Rationale / application:** Our recommendation is to walk the complete task through relevant grip and posture transitions, including reaching, typing, returning, and correction. Observe which actions require a grip change and whether that introduces difficulty, lost context, or accidental activation. Include both hands where relevant rather than treating preferred handedness as a fixed interaction mode.
- **Exception / conflict:** People’s ability to change grip does not prove that every user can safely do so. Preserve a required one-hand route when the task or access need demands it; do not require users to adopt the designer’s posture. Historical percentages are not universal layout weights.
- **Review:** Can the intended users complete the essential sequence in their actual constrained postures, including switching and returning?
- **Source / dating:** Ch. 5, printed pp. 92–106 (PDF 93–107), especially pp. 93–95, 99–104 (PDF 94–96, 100–105). Figures PDF 94, 96, 100, and 102 inspected. The older “over five inches” category is not a present-day device breakpoint; the four-frame example illustrates one participant, not population frequency.

### TD-06 — Keep observational findings attached to their sample and uncertainty

- **Trigger:** Turning a grip study, informal observation, or null demographic result into a product requirement.
- **Author’s account:** The first reported study used 1,333 valid public observations, of which 780 involved touching; a later study reported 651 observations across 22 countries. Pilot observations were excluded. The author reports no significant differences across several demographic categories in the later data.
- **Rationale / application:** Our recommendation is to record sampling context, dates, observation unit, denominator, categories, exclusions, and what was not measured. Use these observations to challenge a universal assumption and generate representative test scenarios. Treat task success, accuracy, access, and preference as separate questions requiring relevant evidence.
- **Exception / conflict:** Public observation is not random sampling and does not establish causality. Avoiding participant awareness does not remove all bias. Missing significance does not prove equivalence; these chapters do not supply subgroup power or disability coverage sufficient for the author’s broader all-people conclusion. Country count alone does not establish representativeness.
- **Review:** Would the recommendation still be defensible without transferring the reported percentage or asserting that an unrepresented group behaves identically?
- **Source / dating:** Ch. 5, printed pp. 88–94, 102–104 (PDF 89–95, 103–105). Studies dated 2013 and 2014; figure PDF 93 inspected. Its pie includes listening/talking, so its denominator must not be confused with the touching subset. Raw data and cited primary reports were not independently examined.

### TD-07 — Keep essential actions available across input and orientation changes

- **Trigger:** Responsive interfaces, convertible hardware, attached keyboards, touchless gestures, or orientation changes during a task.
- **Author’s account:** The book describes people mixing touch, keyboard, pointer, and other methods; it warns against hidden hover dependence and content obscured by an onscreen keyboard.
- **Rationale / application:** Our recommendation is to provide discoverable essential actions, meaningful keyboard focus, semantic controls, and a usable route with the onscreen keyboard visible. Check supported orientation and input changes during an unfinished task, including whether focus, values, feedback, and return paths survive. Use actual capabilities and user needs rather than viewport width as a proxy for input method.
- **Exception / conflict:** The book’s “support all” language needs task-specific scope. Some orientation limits are justified; record the reason and access implications. Device detection cannot reveal moment-to-moment grip, and a modern capability signal does not make exclusive-input assumptions safe.
- **Review:** Can the scoped task continue when input or orientation changes, and are essential controls usable without hover or an undisclosed gesture?
- **Source / dating:** Ch. 2, printed pp. 55–58 (PDF 56–59); ch. 5, pp. 105–108 and 111–112 (PDF 106–109, 112–113). Gesture and hardware examples are dated; current native and web behaviors require current implementation checks.

### TD-08 — Evaluate readability at the expected viewing distance

- **Trigger:** Scaling layouts from phones to tablets, surface-mounted use, larger displays, or dense mobile typography.
- **Author’s account:** Larger devices were more often supported on surfaces or stands in the described observations; the book connects greater viewing distance with reduced apparent size.
- **Rationale / application:** Our recommendation is to test the critical text, icons, controls, and status information at plausible distances and support positions. Include user text scaling and realistic content. A layout that merely fills a larger viewport may leave information too small to read comfortably; adjust hierarchy and size based on the task, not device diagonal alone.
- **Exception / conflict:** Device size is an imperfect clue, not a sensor for the user’s eyes or vision. Do not force a class-wide scale or reduce phone text merely because phones can be held closer. Accessibility needs and user settings remain independent constraints.
- **Review:** Can users read and distinguish the information needed for the task without unwanted zooming, leaning, truncation, or loss of function at increased text size?
- **Source / dating:** Ch. 5, printed pp. 96–98 and 108–110 (PDF 97–99, 109–111). Figures PDF 97, 99, and 110 inspected. The charts communicate historical trends; their schematic device classes and distance endpoints are not universal sizing constants or a calibrated responsive formula.

### TD-11 — Evaluate touch accuracy in its actual position and context

- **Trigger:** Small controls, densely packed navigation, frequent misses, or reusing one target geometry everywhere.
- **Rationale/source basis:** Hoober reports variation in tap accuracy and speed by screen position after reanalyzing a 2014 mixed moderated/unmoderated study with 31 participants, earlier observations, and cited external studies. His center/edge target proposals are a synthesis, not a universal experimental guarantee. Chapter 8 explains that his selected 95% probability contour is a practicality tradeoff that leaves errors outside it.
- **Application:** Start with current applicable target and accessibility guidance, then inspect actual rendered/hit-tested geometry, position, neighboring actions, hand availability, and target consequence. Test relevant device classes and usage contexts rather than treating a schematic thumb sweep or one designer's grip as the whole audience. Physical scale can reveal differences that a screenshot at arbitrary zoom conceals.
- **Exceptions:** Do not replace current minimums with the book's smaller central targets or promote its 7–12 mm proposals and 95% contour into acceptance thresholds. A population aggregate does not establish every individual's precision, comfort, access needs, or grip. The author's kiosk caveat and later encumbrance findings limit transfer even when the hardware is an iPad. An inability or unwillingness to shift grip remains a valid requirement for a particular audience.
- **Review:** Exercise the affected targets at actual size with representative neighboring actions and input conditions; record misses, unintended adjacent activation, and recovery. A target-size inspection establishes geometry, not population-level error rates or comfort.
- **Source:** Ch. 6, PDF 119–129 / printed 118–128; PDF 133–136 / printed 132–135. Ch. 8, PDF 180–182 / printed 179–181. Ch. 9, PDF 205–207 / printed 204–206. Figures PDF 123 and 126 visually inspected.
- **Dating:** The book's claims about then-current Apple/Google units and target guidance are historical and require current verification. Printed figure labels mix mm and “pt”; do not transplant those numerical labels into iOS points or CSS pixels.

### TD-12 — Let people bring important content into a usable viewing position

- **Trigger:** Long forms, the last list row or paragraph, a keyboard-covered action, or an interface that stops scrolling exactly at the viewport boundary.
- **Rationale/source basis:** The author reports participants moving list choices toward the screen's center before selecting, and subsequent observations of missed final fields or actions. He proposes center-out composition and additional trailing scroll space. This is a contextual design proposal from observed behavior; it does not prove that every task or audience should put its primary action at the center.
- **Application:** Test whether final content and actions can be brought into a comfortable, unobscured area with real system chrome, text size, keyboard, and orientation. Add useful trailing space or adapt scrolling when evidence shows clipping, occlusion, or difficult reading. Keep content order and action meaning coherent as the visible region changes.
- **Exceptions:** Do not center every control, force all secondary controls to edges, impose a four-tab limit, or discard platform navigation conventions. A fixed control may be appropriate. Excessive padding and surprising automatic scrolling can themselves cost effort or disorient. The source critiques the F-pattern as a universal composition recipe; replacing it with another universal location rule would repeat that mistake.
- **Review:** Reach the final field/item with large and ordinary text, open the relevant keyboard/picker, and finish the task. Check user-initiated scroll, focus movement, and return position. An expert inspection can identify clipping but cannot establish users' attention distribution.
- **Source:** Ch. 6, PDF 117–118 / printed 116–117; PDF 135–141 / printed 134–140. Ch. 9, PDF 208–209 / printed 207–208.
- **Dating:** Historical OS overscroll and browser-toolbar examples motivate checks; verify present target behavior rather than copying their screenshots or fixed layout advice.

### TD-13 — Make action feedback visible despite finger occlusion

- **Trigger:** A small icon changes state under the finger, selection feels unresponsive, or input acknowledgement is hard to notice.
- **Rationale/source basis:** Chapter 7 distinguishes a detected contact centroid from the larger contact patch and still larger obscured screen region. A control can be touchable yet hide its own feedback. The author's enlarged pressed-state Twitter example is a proposed redesign, not evidence that Twitter implemented it or that users validated it.
- **Application:** Use perceptible pressed, selected, pending, and completed states appropriate to the action. Let feedback extend across a coherent control or row when that makes it visible around the finger without implying a larger action scope. Preserve a perceivable result after release where the state matters. Combine channels as appropriate to the task and current accessibility behavior.
- **Exceptions:** A bigger invisible hit region alone does not solve obscured feedback. A pressed appearance acknowledges input, not successful remote completion. Do not mandate flashing, haptics, sound, text labels on every familiar icon, or a large colored box around every action. Haptics can supplement but cannot replace accessible feedback, and current system/user preferences govern their use.
- **Review:** Observe the control while touching it, then after release and during delayed/failing work. Verify that the actual activated object and resulting state remain recognizable. Inspect relevant assistive announcements separately; an occlusion sketch is not an accessibility test.
- **Source:** Ch. 7, PDF 144–146 / printed 143–145; PDF 156–166 / printed 155–165. Figures PDF 159 and 163 visually inspected.
- **Dating:** Twitter/UI examples are historical. The book's description of web `:active` does not make transient styling proof that an action completed; verify actual native/browser events and state semantics.

### TD-14 — Support correction in precision touch tasks

- **Trigger:** Drawing, text placement, handles, fine sliders, cropping, dragging, or accidental drag activation during a tap.
- **Rationale/source basis:** The source discusses display/sensor parallax, motion during liftoff, and research in which magnification enabled much finer placement. The small precision values belong to particular feedback-assisted experiments; they do not describe ordinary unaided touchscreen performance.
- **Application:** Prefer tested platform interaction behavior where it fits. For genuinely precise work, consider magnification, fine adjustment, meaningful snapping, an inspectable selection preview, and easy correction. Determine when a tap becomes a drag and how users cancel or recover. Use a distinct manipulation mode only when its benefit outweighs the added mode burden.
- **Exceptions:** Do not hard-code optical offsets, activate consequential actions on touch-down, or replace native gesture thresholds from the book's simplified mouse/touch event explanation. Display hardware, APIs, input device, and accessibility settings vary. Snapping must not silently overrule intended placement; precision aids need understandable exits.
- **Review:** Try near-boundary taps, small motion before release, interrupted drags, correction, and cancellation on the intended runtime. Verify exact final selection and feedback rather than inferring it from finger or cursor position.
- **Source:** Ch. 7, PDF 147–156 / printed 146–155. Figures PDF 150 and 154 visually inspected.
- **Dating:** Historical calibration, stylus, and click-processing descriptions explain possible failure mechanisms; current platform event semantics govern implementation.

### TD-15 — Keep scrolling compatible with reading and selection

- **Trigger:** Dense lists/tables, a feed full of interactive rows, scrolling that accidentally activates content, or support for different writing directions.
- **Rationale/source basis:** In the author's observed tasks, people often selected near meaningful label content but placed scrolling gestures in relatively empty regions. He describes mirrored avoidance for right-to-left text. This is content-relative behavior, not a fixed universal right-side scroll lane.
- **Application:** Preserve usable reading structure and reasonable space for gestures; test scrolling through selectable content without unintended activation. Let native scrolling tolerate ordinary nonstraight movement. In genuinely two-dimensional surfaces, provide orientation and a recoverable route to a useful view. Evaluate writing direction and real content lengths rather than blindly copying left alignment.
- **Exceptions:** Do not reserve a permanent empty column, force left alignment for every locale, or ban horizontal and two-axis interaction where the task requires them. The chapter's final “always left-aligned” checklist must be read with its explicit RTL discussion. Cards, charts, maps, and visual canvases need task-specific behavior rather than universal text-list treatment.
- **Review:** Scroll and select with long/short content, both relevant writing directions, and the actual input methods. Check that diagonal motion during ordinary scrolling does not unexpectedly switch views or activate destructive behavior. Measure user effects with representative users when claiming reduced effort.
- **Source:** Ch. 7, PDF 166–175 / printed 165–174. Figure PDF 168 visually inspected.
- **Dating:** The book's broad negative claims about horizontal scrolling are not a current platform prohibition. Preserve useful native gestures and establish fit in the product's context.

### TD-16 — Inspect the actual hit regions and their neighboring consequences

- **Trigger:** Icons that appear well separated, custom button markup, compact rows, nested actions, or a mismatch between a visible container and its tappable area.
- **Rationale/source basis:** Chapter 8 treats touch as a distribution rather than a perfectly aimed point. Its overlay method asks which neighboring regions an inaccurate tap would hit. Historical examples distinguish icon appearance from the larger implemented action area.
- **Application:** Inspect hit-test geometry at actual scale as well as visible boundaries. Make a coherent button or row respond across its intended surface where appropriate, and keep competing targets unambiguous. Review the result of a near miss: no response, adjacent action, navigation, or external commitment. Use native/semantic controls when they supply the needed behavior.
- **Exceptions:** A hand overlay or probability circle is an inspection aid, not measured task performance. Do not expand regions until they overlap, make every containing card a button, or consume scroll space with an unintended action. Separate actions inside a row require deliberate semantics. The book's specific probability radius/diameter language should not become an implementation formula.
- **Review:** Probe the visually implied control surface, its boundary, and neighboring targets in runtime; verify exactly which action occurs. Include nested controls and enlarged text/layout variants. Record actual geometry and observed activation rather than claiming a global touch-success percentage.
- **Source:** Ch. 8, PDF 180–190 / printed 179–189. Figures PDF 181 and 185 visually inspected.
- **Dating:** Historical charged-button and Twitter behavior illustrates an approach; it is not a guarantee about current system hit testing or permission to rely on undocumented expansion.

### TD-17 — Design recovery around the consequence of a mistaken tap

- **Trigger:** Submit versus Cancel, Delete near frequent actions, accidental navigation, or a touch mistake that could lose work or commit an external action.
- **Rationale/source basis:** The source recommends larger effective targets, consequence-sensitive separation, and recovery instead of assuming all taps are intentional. It illustrates reversible navigation and delayed/undoable sending, but does not establish that every action can be undone.
- **Application:** Remove truly unnecessary destructive choices, distinguish action scope, separate dangerous actions where useful, and retain work across recoverable misnavigation. Define the real commit boundary and choose prevention, preview, confirmation, cancellation, or reversal to match system capability and consequence. Recovery should remain available at a useful moment.
- **Exceptions:** Do not remove Cancel, Clear, reset, or confirmation solely because the author disfavors them; these may express a real user intent or required protection. Do not hide every consequential command in a low-use menu or promise undo when an external effect cannot be reversed. Preserve necessary consent and distinguish a compensating action from true rollback.
- **Review:** Intentionally activate the relevant neighboring control in a safe fixture. Check data retention, true external state, recovery, and the original path after returning. Verify any undo window and late failure rather than relying on an attractive undo label.
- **Source:** Ch. 8, PDF 190–195 / printed 189–194; ch. 9, PDF 202–206 / printed 201–205.
- **Dating:** Gmail and Twitter examples describe historical interfaces. Exact current product behavior and available backend guarantees require separate verification.

### TD-18 — Treat environment and access conditions as part of the task

- **Trigger:** A mobile task may occur with occupied hands, glare, noise, motion, divided attention, or different sensory/motor capabilities.
- **Rationale/source basis:** Chapter 9 combines situational constraints with accessibility-oriented design. It also cites an encumbrance study in which carrying a bag and walking changed touch accuracy substantially. This qualifies the earlier broad center/edge model; the source itself acknowledges little evidence on when oversized controls stop looking interactive.
- **Application:** Identify plausible environments and access requirements from product evidence. Preserve essential information across interruption, provide appropriate alternatives to audio-only or color-only meaning, and design safe correction when movement causes input error. Test text, contrast, input, and assistive behavior in the configurations that matter.
- **Exceptions:** Temporary constraints are useful design prompts, not a replacement for disabled people's actual requirements or dedicated accessibility checks. Do not claim that designing for noise or glare makes an interface work for every user. Security/expiry may require timeouts; give understandable notice, preservation, extension, or recovery where appropriate. Do not turn every notice into a permanent obstruction.
- **Review:** Exercise a representative interrupted/encumbered scenario safely, plus relevant assistive interactions. Record remaining contexts and unverified assumptions. Do not infer safety while driving or performing hazardous activity from ordinary mobile checks.
- **Source:** Ch. 9, PDF 198–207 / printed 197–206; PDF 218–219 / printed 217–218. Figure PDF 205 visually inspected.
- **Dating:** Disability population figures and quoted performance differences are historical, study-specific claims; neither becomes a present-day prevalence estimate or universal target-sizing multiplier.

### TD-19 — Make rapid repeated and unintended input safe across state changes

- **Trigger:** A button can submit twice, toggle twice, open a confirmation under the same touch location, or start dragging when a tap was intended.
- **Rationale/source basis:** The author describes accidental multiple taps, drops, and drags caused by movement or tremor. His confirmation example moves the final destructive choice away from the initiating control so an unintended repeat does not immediately confirm it.
- **Application:** Define behavior for fast repeated activation, delayed acknowledgement, and state changes under the pointer/finger. Prevent duplicate consequential operations using the appropriate UI and system mechanisms. Ensure that a protection step requires intentional action instead of consuming an already queued repeat. Use platform-appropriate alternatives when precise drag control is not required.
- **Exceptions:** Do not disable all repeated input, suppress intended double-tap gestures, or introduce arbitrary delays into every control. Moving controls can disorient users or harm access; inspect the full interaction and native conventions. UI debouncing alone may not prevent duplicate server effects, while a confirmation alone may not prevent an accident.
- **Review:** Send repeated taps before, during, and after acknowledgement; observe both visible state and actual committed operations. Test cancellation, queued input, and false drag initiation with safe fixtures. Check that the prevention mechanism does not block intentional repeated work or assistive activation.
- **Source:** Ch. 9, PDF 202–204 / printed 201–203; ch. 7, PDF 154–156 / printed 153–155. Figure PDF 203 visually inspected.
- **Dating:** ClickFix/macOS examples and historical inline-guard layouts illustrate the problem; current platform semantics and application transaction behavior determine the solution.

### TD-20 — Verify edge controls with system chrome and real device constraints

- **Trigger:** Bottom actions, edge gestures, full-screen content, floating controls, browser chrome changes, or devices used with raised cases/bezels.
- **Rationale/source basis:** Chapter 9 describes historical browser and OS edge interception, changing viewport boundaries, and the way a raised bezel can distort contact near an edge. The author explicitly lacks enough data on newer iOS edge behavior and proposes a generic 20% sizing allowance for cases; neither establishes a current rule.
- **Application:** Use current platform safe-area/inset and viewport behavior, respect system gesture ownership, and test actual show/hide transitions for chrome, keyboard, and full-screen modes. Keep important controls operable and content readable as those boundaries change. Include a representative physical case when edge interaction is material to the product.
- **Exceptions:** Do not ban bottom bars on the web or native apps, assume all edge gestures are unavailable, or add a universal 20% margin. Current supported devices, browser versions, system navigation modes, and cases differ. Visual padding alone does not prove correct hit testing or gesture handling.
- **Review:** Exercise edge actions before/after browser or OS chrome appears, with keyboard and relevant orientations; confirm whether the first intended activation occurs. Check overlap, jumping content, accidental system actions, and physical access at the case edge. Record which device/browser combinations were actually tested.
- **Source:** Ch. 9, PDF 207–219 / printed 206–218. Figures PDF 208 and 215 visually inspected.
- **Dating:** The book's Safari first-tap and Android navigation-bar descriptions are historical examples, not assertions about the current OS. Current official guidance and actual runtime results take precedence.

### TD-21 — Give consequential meanings more than one dependable cue

- **Trigger:** Status icons, warnings, selection, charts, or controls distinguished mainly by color or a small symbol.
- **Rationale:** The author connects variation in perception and viewing conditions with the risk that a single cue is missed. His illustrated status set varies shape, symbol, color, and wording.
- **Application:** Provide meaningful text or another independent cue for important differences, with appropriate accessible names and state semantics. Test the actual rendered combinations and surrounding content, not just swatches. Treat maps, charts, or imagery as possible complements to usable textual information.
- **Exception:** The author's universality claims about shape meanings, brain subsystems, and color-vision prevalence are not established by this review. Redundant cues need not mean adding a decorative icon to every label; recognized platform controls may already convey meaning adequately.
- **Review:** Can each consequential state be identified without relying on color alone, and can intended users explain the unfamiliar symbol's meaning? Rendering/semantic inspection and participant comprehension answer different parts.
- **Source:** Chapter 10, PDF 224–228, 253–255 / printed 223–227, 252–254. Status illustration at PDF 228 / printed 227 visually inspected; master checklist PDF 381–382 / printed 380–381.

### TD-22 — Make perceived interactivity and unavailable actions match reality

- **Trigger:** Bordered status cards, minimalist inputs, selectable rows, ambiguous disabled controls, or an action that fails because a prerequisite is missing.
- **Rationale:** The author describes people mistaking emphasized static content for controls and missing visually weak actions. His unavailable-device example adds explanation and a changed symbol instead of relying solely on dimming.
- **Application:** Match the apparent clickable region to the implemented target and expected effect. Give important actions recognizable signifiers; distinguish navigation, selection, and commands. Explain relevant prerequisites and how to satisfy them without making a disabled state look enabled.
- **Exception:** Borders are one signifier, not a requirement for every action or a prohibition on static cards. Hiding all unavailable features and disabling every incomplete form are contextual author preferences, not universal solutions. Current native semantics govern implementation.
- **Review:** Predict the action from the treatment, then exercise the apparent target and prerequisite states. Can someone discover the needed action and understand why it is unavailable?
- **Source:** Chapter 10, PDF 235–243, 260–263 / printed 234–242, 259–262. Unavailable-device example at PDF 243 / printed 242 visually inspected.

### TD-23 — Check readable content in the actual viewing conditions

- **Trigger:** Compact typography, long labels, small status graphics, large-screen variants, glare, or user-selected text enlargement.
- **Rationale:** The author emphasizes viewing distance, device use, and environmental variation; nominal font size alone cannot establish usable reading. His size tables distinguish minimum visibility from comfortable reading.
- **Application:** Use the project's current platform text styles and access requirements, then inspect real content on representative devices and supported text sizes. Check glyph distinction, wrapping, hierarchy, contrast, and critical labels under relevant lighting and distance. Respect enlargement and zoom choices.
- **Exception:** Do not adopt the book's physical-point tables, conversion multipliers, upper size limits, or three-heading-level recommendation as modern requirements. Its blanket dark-mode preference, black/white contrast claim, and broad font/icon claims require separate scrutiny.
- **Review:** On the intended device and text setting, can people read necessary labels and values without clipping or loss of action access? A desktop rendering or size formula cannot establish that result.
- **Source:** Chapter 10, PDF 232–234, 244–252, 255–260 / printed 231–233, 243–251, 254–259; chapter 11, PDF 272–276 / printed 271–275. Table PDF 251 and hierarchy illustration PDF 275 visually inspected.

### TD-24 — Keep important feedback observable through touch and distraction

- **Trigger:** Selection feedback under a finger, transient notices, blinking status, actions used while moving, or adjacent consequential controls.
- **Rationale:** The author connects occlusion and imprecise movement with uncertainty about whether an action registered. Intermittent or short-lived signals can disappear at the moment a person checks them.
- **Application:** Show timely, truthful selection and operation state in a perceivable area; preserve important information long enough to consult or revisit. Check real hit regions, target separation, scrolling space, accidental repeat input, and recovery. Use sound or haptics as supplementary channels when appropriate.
- **Exception:** Do not import the example blink waveform or demand that every notice persist until explicitly dismissed. Some effects are irreversible; recovery must reflect actual system guarantees. A larger target must not overlap its neighbors or conceal content.
- **Review:** With realistic touch and interruption, can the person observe acknowledgement, distinguish pending from completed work, and recover from a mistap without unintended duplicate effects?
- **Source:** Chapter 10, PDF 257–261 / printed 256–260; chapter 13, PDF 363–364 / printed 362–363; master checklist PDF 379–382 / printed 378–381.

### TD-25 — Build reusable layouts from task priority and entry context

- **Trigger:** A product assembled from unrelated polished screens, an icon-grid landing page, competing task regions, or direct entry into deep content.
- **Rationale:** The author treats templates as a way to preserve meaning across a product. His three-zone model ranks content and controls, while deep-link examples show that visitors may need orientation without traversing the home page.
- **Application:** Rank the information and actions needed for the scenario, define repeatable semantic regions, and make the primary work discoverable. Provide appropriate location/category cues on direct entry. Compare layouts using realistic content and native behavior across supported configurations.
- **Exception:** The source's center/edge/corner arrangement and ordered hierarchy of visual attributes are heuristics to examine, not universal geography. Navigation may itself be primary content. Brand character, accessibility, landscape use, and platform conventions can justify a different arrangement.
- **Review:** On entry and after scrolling, can intended users identify the screen's role, current context, and main task without relying on a memorized route?
- **Source:** Chapter 11, PDF 266–289 / printed 265–288, especially PDF 280–287 / printed 279–286. Three-zone YouTube diagram at PDF 281 / printed 280 visually inspected.

### TD-26 — Choose disclosure by context, comparison, and content length

- **Trigger:** A proposal to tidy a screen with a modal, drawer, accordion, tabs, or hidden details.
- **Rationale:** The author compares how disclosure mechanisms preserve or lose the initiating object's context. Long expanded sections and hidden content can make orientation and comparison expensive.
- **Application:** Identify what must be seen together and what can wait. Compare inline expansion, a contextual surface, and a new destination using actual content length. Make opening, current section, dismissal, and return understandable; keep necessary comparison information available together.
- **Exception:** Do not apply a universal single-open accordion rule, a ban on scrolling dialogs, or an assumption that drawers always retain context. Modern native sheets and platform navigation require current evaluation. A visible background alone does not establish an intelligible relationship.
- **Review:** Can people reveal the needed detail, retain which object/section it belongs to, compare necessary facts, and return without losing task position?
- **Source:** Chapter 12, PDF 292–308, 339–340 / printed 291–307, 338–339. Product-detail accordion at PDF 305 / printed 304 visually inspected.

### TD-27 — Preserve the meaning of destinations, view switches, and Back

- **Trigger:** Tabs used for commands, peer-view switching, deep drilldown, or a single-page implementation with surprising Back behavior.
- **Rationale:** The author distinguishes equal-weight views from actions and warns that switching pages can lose input or context. His tab illustrations attempt to clarify which label belongs to the displayed content.
- **Application:** Define whether a control navigates, changes a peer view, selects, or performs an operation. Make current destination and affected content clear. Preserve the appropriate history, selection, scroll position, and draft data when leaving and returning through native or browser navigation.
- **Exception:** Reject the book's blanket preference for top-only tabs, ban on primary-navigation tabs, mandatory first default tab, and fixed count limits. Historical usage claims do not prove universal understanding. Current platform conventions take precedence over an illustrative tab shape.
- **Review:** Can intended users predict whether a control changes place or performs an action, and does actual Back/return restore the promised context?
- **Source:** Chapter 12, PDF 308–317 / printed 307–316. Original Quora example PDF 310 and author-modified mock-up PDF 311 / printed 309–310 both visually inspected.

### TD-28 — Preserve orientation without letting fixed controls consume the task

- **Trigger:** Long scrolling content, sticky headers, bottom action bars, batch selection, or controls competing with the keyboard and system edges.
- **Rationale:** The author uses fixed headers and contextual bottom bars to retain location and action scope, but his master checklist also cautions about browser/OS edge conflicts. These costs must be reconciled in the actual interface.
- **Application:** Keep necessary context and actions reachable using an appropriate fixed, contextual, or in-content treatment. Show the scope of batch actions. Check visible content space, keyboard, enlarged text, safe areas, browser chrome, and the final item; adapt the treatment when fixed chrome obstructs work.
- **Exception:** Neither fixed bars everywhere nor a universal ban on web bottom controls follows. The source's placement preferences and hard edge-control counts are not current platform specifications. A static picture cannot establish dynamic keyboard or scroll behavior.
- **Review:** During scrolling, selection, text enlargement, and keyboard use, can the person identify location/scope and reach both the content and required action without obscured or conflicting targets?
- **Source:** Chapter 12, PDF 322–327 / printed 321–326; master checklist PDF 381 / printed 380. Photos batch-selection pair at PDF 326 / printed 325 visually inspected.

### TD-29 — Preserve the user's comparison when simplifying a collection

- **Trigger:** A wide data table, list/card redesign, narrow viewport, or excessive attributes in a result row.
- **Rationale:** The author argues that showing every available field can obscure the decision and that turning each row into a separate record can remove direct comparison. His service-center example keeps decision attributes compact and reveals actions on demand.
- **Application:** State the decision or lookup question, retain the fields and relationships it requires, and put genuine secondary detail behind a clear route. Compare table, list, and card treatments with realistic values and names. Use appropriate native or web semantics and maintain usable label/value associations.
- **Exception:** The source's categorical rejection of horizontally scrollable tables, responsive records, and cards is not adopted. Each can fit a particular task. Removing columns is inappropriate if it hides material decision facts; list-like appearance does not imply HTML table semantics.
- **Review:** Can intended users answer the required comparison with the visible information, then retrieve relevant detail without confusing entities or losing the original set?
- **Source:** Chapter 12, PDF 327–335 / printed 326–334. Service-center display at PDF 335 / printed 334 visually inspected.

### TD-30 — Make collection previews reveal their extent and alternate routes

- **Trigger:** Horizontally scrolling category rows, image-led browsing, truncated collections, or a gesture-only carousel.
- **Rationale:** The author distinguishes exploratory category rows from rotating marketing banners. A perfectly fitted row or an unexplained subset can hide the existence of additional items.
- **Application:** Signal additional content, provide meaningful labels, and offer a clear route to the full category where useful. Support the required input methods beyond swiping. Distinguish a preview from the full available set, and retain context when opening an item and returning.
- **Exception:** Carousels suit some browsing tasks better than exact finding or simultaneous comparison. A partially visible item is one possible cue, not sufficient accessibility or an obligatory layout. Do not infer current catalog completeness or performance from historical screenshots.
- **Review:** Can people discover that more items exist, reach them without the swipe gesture, identify individual items, and return to the same context?
- **Source:** Chapter 12, PDF 336–339 / printed 335–338. Category-row example PDF 337 / printed 336 visually inspected; following prose page PDF 338 also rendered.

### TD-31 — Investigate the real device, environment, and service assumptions

- **Trigger:** A mobile brief based on the team's own phones, location-dependent work, connectivity assumptions, or a task performed outside a desk setting.
- **Rationale:** The author connects audience behavior with device capabilities, alternative inputs, physical surroundings, and service constraints. He cautions against treating laboratory Wi-Fi and a preferred handset as representative of use.
- **Application:** Record what is known about devices, access needs, carrying/holding conditions, network variation, and external work. Inspect relevant technical guarantees and data needs; use appropriate precision and transparent limits for location. Form test conditions from actual risk and audience evidence.
- **Exception:** Device-adoption statistics, technology explanations, pressure-sensing claims, and 5G predictions are dated context, not verified current facts. No authorization for recruitment, tracking, or location collection follows from a source recommendation. Coarse or aggregated location is not automatically private.
- **Review:** Which behavior depends on an untested device, network, input, or data assumption, and what observation or controlled runtime check would resolve it?
- **Source:** Chapter 13, PDF 345–355 / printed 344–354, with physical/input cautions at PDF 362–364 / printed 361–363.

### TD-32 — Carry task rationale into implementation and realistic evaluation

- **Trigger:** Design handoff, a technically polished but brittle flow, claims based on mock-ups, or a release whose behavior diverges from the brief.
- **Rationale:** The author links audience/context work, information structure, interaction, understandable content, resilience, and continued testing. His practical guidance asks teams to inspect on real devices and observe use rather than assuming the designers represent the audience.
- **Application:** Preserve shared task, structure, state, and content decisions through implementation. Choose prototype realism for the question, inspect the running result in relevant conditions, and revise based on evidence. Keep source inspection, device interaction, and participant observation distinct; verify meaningful corrections.
- **Exception:** Do not impose a rigid all-research-before-drawing process, annual documentary viewing, a particular team method, or the printed measurement templates as universal gates. A screenshot displayed on a phone can support scale inspection but cannot validate hit regions or live transitions.
- **Review:** What was actually checked on which artifact/device, did the changed path preserve the intended task, and which conclusions still need runtime or participant evidence?
- **Source:** Chapter 13, PDF 355–375 / printed 354–374. Printed measurement templates at PDF 374 / printed 373 visually inspected; no physical calibration or touch test was performed.
