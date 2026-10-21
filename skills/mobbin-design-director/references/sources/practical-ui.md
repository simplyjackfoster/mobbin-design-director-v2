# Practical UI — contextual source lessons

Adham Dannaway. *Practical UI*, second edition, 2024. ISBN978-0-6456766-1-7.
Edition and year are verified from the supplied interior copyright page (PDF2),
not the archive filename or PDF creation metadata. One-based PDF page numbers
match printed page labels on inspected body pages. [Coverage manifest](practical-ui-coverage.json).

All373 pages were read or assessed in sequential bounded full-text batches,
including all eight chapters, exercises, captions, introduction, and closing pages.
Forty-six selected figure pages and one additional prose page were rendered and
inspected. This is full text coverage, not exhaustive inspection of every figure
or an independent audit of the author's cited studies. Raw extraction, PDF, and
rendered pages remain outside Git; the archive's Figma files were not used.

These concise cards paraphrase the source and distinguish it from operational
recommendations. Use the topic modules for normal work and retrieve a card when
its trigger applies. The book's teaching comparisons illustrate possible design
improvements; they are not controlled experiments or evidence of user outcomes.
Some change copy, layout, color, typography, and imagery at once. Compare matched
content and report changed variables when evaluating our own directions.

## Reconcile before applying

Preserve the book's reasoning while qualifying its fixed counts, font sizes,
spacing ratios, target dimensions, and beginner defaults. Prefer current Apple
behavior for native iOS; WCAG and web patterns require their own platform path.
Do not promote the source's future-WCAG3/APCA statement, universal pure-black
warning, left-alignment preference, or initial-destructive-red prohibition into
mandatory rules. Exact contradictions and current-source corrections appear in
the relevant cards. Expressive imagery and type are allowed when they contribute
to the intended experience while task information remains clear.


### PU-01 — Explain design decisions and component usage

- **Trigger:** Creating a visual system, extending components, or reconciling inconsistent screens.
- **Author’s account:** The author frames design as reasoned choices and distinguishes reusable styles, reusable components, and guidance for using them. Accessibility includes temporary and situational limitations as well as permanent disabilities.
- **Rationale / application:** Document the purpose and appropriate context of a component, its information hierarchy, content conventions, and relevant states. Include expressive choices when they support the intended experience; visual taste need not masquerade as an empirically proven law.
- **Exception / conflict:** The book’s sample palette, shadow count, radii, and left-alignment conventions describe its own system. They are not requirements for every product. Reuse native controls and approved project decisions where they fit.
- **Review:** Can another implementer choose and populate this component appropriately, including its disabled, pressed, focus, and error behavior?
- **Source / dating:** Ch. 1, PDF/printed pp. 19–20, 26–39, 40–52. Touch has no dependable hover state. Historical platform screenshots are examples, not current specifications.


### PU-02 — Simplify without deleting necessary information

- **Trigger:** A sparse screen is difficult to understand, or decoration and repeated content compete with the task.
- **Author’s account:** The author distinguishes minimal appearance from ease of use. Examples remove redundant text or styling while preserving labels, selected states, and action visibility; progressive disclosure can reduce cognitive burden despite adding an interaction.
- **Rationale / application:** Remove duplication and irrelevant decoration before removing explanatory labels, comparison data, or recovery controls. Disclose genuinely conditional input at the moment it becomes relevant. Preserve enough visible structure to predict what can be done.
- **Exception / conflict:** A decorative element can establish character or delight. The book explicitly permits such purposes; it does not justify a blanket ban on gradients, rounded cards, illustration, or mascots. Important terms must not be hidden merely to tidy a financial screen.
- **Review:** After simplification, can someone still identify the current state, main task, actionable elements, and any decision-changing information?
- **Source / dating:** Ch. 2, pp. 56–65; visually inspected pp. 57, 63, 65. The photo-editor comparison at63 changes several affordances together; it illustrates a design hypothesis, not measured improvement.


### PU-03 — Reduce choice effort without manufacturing a preferred answer

- **Trigger:** A long list, comparison, onboarding sequence, or menu demands substantial search and decision work.
- **Author’s account:** Interaction cost includes looking, searching, reading, waiting, typing, thinking, and remembering. The author proposes removing irrelevant choices, grouping alternatives, sequencing decisions, and recommending a suitable option.
- **Rationale / application:** Reduce the actual effort of the scenario, not just the tap count. Group by the user’s decision criteria, preserve alternatives, and explain a recommendation using real task fit. Separate a known-item search from exploratory browsing.
- **Exception / conflict:** More steps can improve comprehension or make recovery harder. A recommendation must not invent popularity, conceal costs, or bias an equally valid choice toward the business. The book’s illustrative cost arithmetic is not a validated universal metric.
- **Review:** What information must be found, remembered, or re-entered, and is the suggested option justified for this person’s task?
- **Source / dating:** Ch. 1, pp. 21–25; ch. 2, pp. 67–71; ch. 8, pp. 353–355, 361–362. Fixed choice counts are starting heuristics, not thresholds.


### PU-04 — Check current contrast requirements and actual legibility

- **Trigger:** Selecting text, control, or state colors; inspecting light and dark appearances.
- **Author’s account:** The author emphasizes sufficient text and non-text contrast and demonstrates that thin typography can remain difficult to read even when a nominal contrast test passes. The book discusses WCAG2.1 and presents APCA as a future WCAG3 contrast method.
- **Rationale / application:** Use the current applicable standard and platform guidance for compliance; inspect actual rendered text weight, size, backgrounds, and states as well as computed contrast. Keep supplemental perceptual analysis separate from conformance claims.
- **Exception / conflict:** Dated correction verified 2026-10-21: the W3C WCAG3 Working Draft dated2026-09-10 says its contrast algorithm is not yet determined and draft publication is not endorsement. APCA is supplemental, not a substitute for WCAG2.2 web conformance. Native iOS follows current Apple accessibility guidance and the project’s requirements. The book’s blanket concern about pure black on white is not adopted as a universal ban; do not reduce contrast automatically.
- **Review:** Is every contrast claim tied to the applicable standard and measured rendered colors, and does small or thin text remain readable in the supported appearance?
- **Source / dating:** Ch. 1, pp. 17–18; ch. 3, pp. 79–84, 92–93; ch. 5, pp. 257, 259–263. Visual checks:18,80,261. Current correction: https://www.w3.org/TR/wcag3/ and https://www.w3.org/TR/WCAG22/ (checked by integrating lead2026-10-21). Book pixel/point and simplified threshold wording must not be copied into normative tests.


### PU-05 — Give color a stable role and a second channel for meaning

- **Trigger:** Brand colors, status badges, links, selected items, or warnings appear in the same experience.
- **Author’s account:** The author recommends consistent action color, restrained use of competing hues, semantic status colors, and non-color cues. Examples distinguish informational content from clickable content and adapt text color to a light brand fill.
- **Rationale / application:** Assign color by role: interaction, status, structure, brand expression. Add an appropriate label, shape, symbol, or other perceivable cue for important state. Keep brand illustration expressive while maintaining clear action semantics.
- **Exception / conflict:** A single brand color is a useful starting constraint, not a ban on multicolor brands or mascots. Color associations vary culturally. Static colored content need not be prohibited if it cannot reasonably be mistaken for a control. The p85 color-blindness comparison removes an error label in one grayscale image; it is not a controlled color-only demonstration.
- **Review:** Can important state be understood without hue, and can someone distinguish an action from decorative or informational color?
- **Source / dating:** Ch. 3, pp. 85–102, 146–151. Visual checks:85,99. Treat named color-psychology associations as contextual design hypotheses, not universal emotional effects.


### PU-06 — Test semantic colors across layers and interaction states

- **Trigger:** A design system introduces dark mode, layered surfaces, tinted cards, or translucent fills.
- **Author’s account:** The author distinguishes primitive swatches from semantic roles, uses relative surface lightness and shadow to convey layering, and demonstrates transparent fills that adapt to different backgrounds.
- **Rationale / application:** Define roles for text emphasis, structural borders, decorative separators, surface levels, and states. Inspect the resulting composite wherever a translucent foreground, nested surface, scrim, and text overlap. Preserve the intended hierarchy in each supported appearance.
- **Exception / conflict:** The author’s HSB recipe, five-color examples, and overlay percentages are construction methods, not guarantees of accessible contrast. Opaque fills can be more predictable. Dark mode is not automatically more comfortable for every person. Native materials and states should follow platform behavior.
- **Review:** Does the same semantic role remain distinguishable and legible on every actual surface and in every relevant state?
- **Source / dating:** Ch. 3, pp. 103–151, especially120–141 and146–151. Visual checks:128,138. Hover overlays are web examples and do not mandate a touch interaction.


### PU-07 — Use imagery coherently without obscuring content or misrepresenting it

- **Trigger:** Choosing illustrations, photos, mascots, or text overlays as part of a direction.
- **Author’s account:** The author suggests coherent image temperature and demonstrates gradients, scrims, and solid surfaces that separate text from variable photographs. Composition and cropping influence where attention falls.
- **Rationale / application:** Give imagery a specific emotional or informational role, crop around the subject and neighboring content, and inspect text on the actual most challenging image region. A mascot should clarify, orient, or acknowledge a meaningful state while financial information remains easy to read.
- **Exception / conflict:** Image warmth is an optional art-direction choice, not a universal rule. Do not recolor images when fidelity is material. A fixed50% overlay cannot guarantee contrast. The rule of thirds is a composition option, not a proven universal attention map.
- **Review:** Does this image contribute to the intended experience, and can the message and action still be read on the actual crop at supported sizes?
- **Source / dating:** Ch. 3, pp. 152–153; ch. 4, pp. 217–218; ch. 5, pp. 254–256. Visual checks:153,255. The mascot application is our recommendation, not the author’s financial-product example.


### PU-08 — Make grouping and appearance describe ownership and behavior

- **Trigger:** Cards, rows, captions, icons, or badges seem attached to the wrong content or suggest nonexistent interactions.
- **Author’s account:** The author presents common region, proximity, similarity, and continuity as grouping cues. Comparisons use containers to resolve ownership ambiguity, spacing to group without containers, and differentiated treatment for static badges and controls.
- **Rationale / application:** Choose the lightest grouping cue that makes relationships unambiguous. Keep an item’s title, value, context, and local action perceptually related. When two elements look alike, verify that the implied behavior or meaning is also alike.
- **Exception / conflict:** Container borders are one solution, not a requirement to put every section into a card. A decorative icon can remain expressive if its treatment does not imply a tappable button. Similarity sometimes intentionally denotes a shared category rather than identical behavior.
- **Review:** Can a viewer tell which explanation or action belongs to which item, and does any static element look tappable?
- **Source / dating:** Ch. 4, pp. 164–178. Visual checks:167,168,172,173. Static comparisons establish appearance, not actual hit regions or interaction results.


### PU-09 — Rank decision content before assigning visual emphasis

- **Trigger:** Designing a screen composition or correcting competition among values, actions, illustrations, and metadata.
- **Author’s account:** The author recommends ranking sections and their contents, then using size, position, contrast, and depth to create hierarchy. A property example emphasizes decision information and the main action over supporting metadata.
- **Rationale / application:** State what the person must understand and decide first. Then assign typographic scale, weight, placement, color, and whitespace to that order. Use a quick squint or blur inspection to detect competing emphasis, followed by normal-size reading and task checks.
- **Exception / conflict:** The largest or brightest element need not always be the call to action. Material costs, risk, deadlines, or eligibility may deserve prominence before commitment. A blur check reveals salience; it does not prove comprehension, accessibility, or emotional success.
- **Review:** What attracts attention first, second, and third, and does that order support an informed decision in this scenario?
- **Source / dating:** Ch. 4, pp. 179–188. Visual check:181. Claims about a universally best bottom action location are not adopted; evaluate reach, context, native conventions, and content occlusion separately.


### PU-10 — Use spacing and alignment to express relationships

- **Trigger:** A screen is evenly spaced but its sections still feel disconnected or difficult to scan.
- **Author’s account:** The author recommends smaller distances within a related group than between groups, consistent alignment, and baseline alignment for mixed-size text such as prices and units. Grids provide a repeatable starting structure.
- **Rationale / application:** Design relative spacing according to semantic nesting, then map it to project tokens. Align comparable values and maintain stable scan edges. Inspect optical relationships and baselines rather than merely matching bounding boxes.
- **Exception / conflict:** An8-point grid, twelve web columns, and four mobile columns are optional frameworks. Do not force every relationship into one numerical gap. Leading alignment depends on writing direction; numeric comparison may use a shared trailing or decimal alignment. The p191 explanation conflates linear2x scale with four physical pixels of area; do not adopt that unit conversion.
- **Review:** Are within-group gaps visibly smaller than the relevant between-group gaps, and do related labels and values share intentional alignment?
- **Source / dating:** Ch. 4, pp. 189–215, especially194–200 and207–212. Visual checks:194,196,209. Physical pixels, logical points, and CSS pixels are distinct.


### PU-11 — Preserve meaningful distinctions when content grows

- **Trigger:** Long account names, large balances, localization, or text scaling stress the layout.
- **Author’s account:** The author demonstrates that identical prefix truncation can conceal the differences between items and suggests wrapping, resizing, or alternative truncation strategies. Whitespace must balance clarity and visible information.
- **Rationale / application:** Use realistic and adversarial content while composing. Preserve identifiers and decision-critical units or suffixes; reflow or expand when needed. Keep a route to full information and verify the layout at supported text sizes.
- **Exception / conflict:** Shrinking text is not a general solution and must not defeat Dynamic Type or legibility. Middle truncation only helps when the surviving parts are meaningful. Do not abbreviate precise financial amounts solely for visual neatness.
- **Review:** Can users still distinguish every relevant item and read the full decision-critical information with long content and enlarged text?
- **Source / dating:** Ch. 4, pp. 201–202, 216; ch. 6, pp. 281–284. Visual check:216. Our native text-scaling and full-detail requirements extend the author’s static examples.


### PU-12 — Choose typography for both legibility and character

- **Trigger:** Starting an art direction or extending a project’s type system.
- **Author’s account:** The author recommends a restrained, legible type family and weight set, discusses glyph clarity and language support, and demonstrates how display type can contribute to different moods.
- **Rationale / application:** Use actual headings, numbers, labels, and multilingual content when choosing type. Keep repeated UI text reliably readable and let a suitable display face carry character where appropriate. Match icon optical weight to nearby text.
- **Exception / conflict:** A single sans-serif family and two weights are beginner-friendly defaults, not bans on serif display faces or native semantic weights. The mood panels at238 also change imagery, color, and shape, so they cannot isolate a font-only emotional effect. Assess a complete direction and identify which variables changed.
- **Review:** Does the type support the intended character without compromising glyph distinction, language coverage, small labels, or numeric comparison?
- **Source / dating:** Ch. 5, pp. 230–240; ch. 7, pp. 320–321. Visual checks:235,238,240,320. The generalization that sans serif is always best is not adopted.


### PU-13 — Tune type scale, leading, and line length together

- **Trigger:** Text hierarchy is weak, paragraphs are tiring, or headings feel detached from their content.
- **Author’s account:** The author builds type scales from a base size, varies scale ratios for dense and expressive interfaces, and treats font size, line height, and line length as interdependent. Examples use tighter leading for large headings than body text.
- **Rationale / application:** Choose a small set of meaningful type roles, then inspect actual wrapping, paragraph rhythm, and heading-to-body grouping. Dense comparison screens and expressive introductions can need different scale contrasts. Preserve readable units and align monetary values deliberately.
- **Exception / conflict:** The book’s pixel sizes, ratios, character counts, and leading ranges are starting heuristics, not universal thresholds or substitutes for native text styles. Avoid overriding a font’s spacing without inspection. Justification and center alignment have contextual uses; writing direction and script matter.
- **Review:** Can readers follow lines, recognize headings, and compare values without the type system disrupting the task at supported sizes?
- **Source / dating:** Ch. 5, pp. 241–253; ch. 4, pp. 207–212. Visual checks:246,247,209. The F-scan description is a contextual scanning tendency, not a universal layout law.


### PU-14 — Front-load the message without concealing material details

- **Trigger:** Writing headings, onboarding explanations, permission prompts, or a dense financial summary.
- **Author’s account:** The author recommends concise plain language and placing the benefit or most important information early. Examples replace vague headings and redundant sentences with clearer information hierarchy.
- **Rationale / application:** Lead with what the person needs to understand or decide; keep necessary conditions nearby. Edit repetition and jargon before cutting important meaning. Use clear headings so a quick scan still exposes the essential message.
- **Exception / conflict:** Fixed sentence lengths, reading-grade targets, and omission of articles or punctuation are editing aids rather than universal rules. A benefit-led permission heading must not bury what data will be stored or shared. Long content can be appropriate when comprehension requires it.
- **Review:** Does a scan reveal both the benefit and the material commitment, and has shortening removed any information needed for an informed choice?
- **Source / dating:** Ch. 6, pp. 267–277. Visual checks:267,273,277. The contact-sync example at273 places the benefit in the heading and persistence details below; our recommendation is to assess whether that detail remains sufficiently prominent.


### PU-15 — Use precise labels, stable vocabulary, and meaningful numbers

- **Trigger:** Naming navigation, links, buttons, statuses, or financial values.
- **Author’s account:** The author recommends descriptive headings and links, consistent terminology and voice, outcome-oriented button labels, and numerals that are easier to scan. Labels should remain useful outside their immediate visual context.
- **Rationale / application:** Use the same term for the same concept and different terms where behavior actually differs. Give actions a clear outcome and links a recognizable destination. Include units, appropriate precision, and locale-aware number formatting.
- **Exception / conflict:** Delete and remove may represent different operations and should not be collapsed automatically. My versus your depends on perspective, not an absolute ban. Do not pad text to equal length or abbreviate balances at the expense of meaning. Small uppercase labels are not universally prohibited.
- **Review:** Can the label be understood on its own, and do its wording and numeric precision accurately predict the result?
- **Source / dating:** Ch. 6, pp. 274–286; ch. 7, p.317. Visual check:285. Broad word-shape explanations for uppercase readability are not treated as current universal cognition theory.


### PU-16 — Explain failure and offer an honest recovery route

- **Trigger:** A payment, lookup, save, or connection fails.
- **Author’s account:** The author replaces vague technical error text with an explanation of the problem and an action the person can take. Error messages should be clear rather than blaming.
- **Rationale / application:** State the known failure, preserve work, and offer a recovery that matches the actual cause and available capability. Say when the cause is unknown. A mascot can acknowledge the moment or point to help but must not substitute for a useful message or button.
- **Exception / conflict:** The p287 example recommends updating payment details after a failed payment; that advice is appropriate only if the system has evidence that those details are the cause. Do not promise a retry, refund, successful save, or recovered state unless implemented.
- **Review:** Can the user understand what happened, what was preserved, and what to do next without being given an invented cause?
- **Source / dating:** Ch. 6, p.287; ch. 8, pp. 364–368. Visual checks:287,367. Work preservation and mascot guidance are our operational extensions.


### PU-17 — Use action emphasis without biasing equally valid choices

- **Trigger:** A screen contains several buttons, repeated row actions, or a consequential choice.
- **Author’s account:** The author uses filled, outlined, and lighter button treatments to create hierarchy and reduces the prominence of repeated actions. He recommends a single primary action when the task has one.
- **Rationale / application:** Identify the real primary action, then distinguish it by more than hue where appropriate. Keep repeated local actions subordinate to the page task. For equally legitimate alternatives, use comparable prominence rather than manufacturing a preferred answer.
- **Exception / conflict:** Native button roles and styles can express hierarchy differently. Do not turn one-primary-action into a quota or demote cancel and privacy choices to serve conversion. The book’s simplified button contrast wording is not an independent compliance standard.
- **Review:** Does the action hierarchy match the user’s task, and are all meaningful alternatives still discoverable and understandable?
- **Source / dating:** Ch. 7, pp. 296–306; ch. 4, pp. 179–186. Visual check:304. Current platform and accessibility requirements govern implementation.


### PU-18 — Explain unavailable actions instead of leaving a silent dead end

- **Trigger:** An action is disabled because of missing input, permissions, eligibility, or unavailable capability.
- **Author’s account:** The author argues that disabled buttons can obscure requirements and proposes alternatives such as validating after an attempted submission or explaining why an action is unavailable.
- **Rationale / application:** Make the missing prerequisite visible and reachable. If an attempt can safely produce useful validation, consider that route; otherwise retain the unavailable state with an explanation. Expose state and reason accessibly.
- **Exception / conflict:** Do not enable an unsafe or impossible operation merely to avoid gray UI. A lock icon is ambiguous between permission, privacy, and paid access unless explained. Native disabled semantics remain appropriate in many contexts.
- **Review:** Can someone determine why the action is unavailable and how to proceed, including with assistive technology?
- **Source / dating:** Ch. 7, pp. 307–311. Visual checks:307,310. The screenshots do not establish actual validation or permission behavior.


### PU-19 — Keep actions close to their context and make targets dependable

- **Trigger:** Placing form actions, menus, dismiss controls, or dense row controls.
- **Author’s account:** The author relates action proximity to effort, emphasizes usable target size, and explains competing left- and right-alignment conventions. Icon/text pairs should have balanced visual weight.
- **Rationale / application:** Place actions where their scope and relationship are clear. Inspect the actual hit region, neighboring targets, keyboard occlusion, scroll position, and accessible name. Follow the intended platform’s conventions while preserving the user’s context.
- **Exception / conflict:** The author’s preferred left-aligned actions and bottom placement are not universal iOS requirements; p314 explicitly permits right-aligned dialogs. Book point/pixel and target-size examples must not be copied as current cross-platform thresholds. A large invisible hit area does not always fix a tiny perceived control.
- **Review:** Can the intended action be found and activated reliably without accidental neighboring activation or losing the content it affects?
- **Source / dating:** Ch. 4, pp. 213–215; ch. 7, pp. 312–321. Visual checks:314,320. Resolve current dimensions against Apple guidance or the applicable web standard and test the actual runtime.


### PU-20 — Match destructive friction to consequences and provide real undo

- **Trigger:** Deleting, removing, replacing, or committing a difficult-to-reverse change.
- **Author’s account:** The author proposes increasing friction with severity, reducing accidental prominence of destructive row actions, explaining consequences, and supporting reversal where possible.
- **Rationale / application:** Evaluate reversibility and likely harm before choosing confirmation, delayed completion, or undo. Name the affected object and consequence. Ensure any undo actually restores the relevant state and remains available long enough for its intended use.
- **Exception / conflict:** The author’s blanket advice against red initial destructive actions is not adopted over native destructive roles. Repeated confirmations can teach automatic dismissal. A checkbox confirmation is one option for high consequence, not a requirement for every deletion.
- **Review:** Is the protection proportional to the consequence, and has the recovery been exercised rather than merely drawn?
- **Source / dating:** Ch. 7, pp. 322–324. Visual checks:322,324. The illustrated restore message demonstrates presentation, not implemented restoration.


### PU-21 — Structure forms around necessary information and logical groups

- **Trigger:** Building onboarding, card entry, settings, or another multi-field task.
- **Author’s account:** The author favors a simple vertical sequence, collects only necessary information, reveals conditional fields, and makes required status understandable. Short, closely related fields may share a row.
- **Rationale / application:** Specify why each field is needed now. Group by the person’s task, use an order that supports completion, and clearly identify what can be deferred. Make progress and final review truthful; preserve answers across navigation.
- **Exception / conflict:** Single-column layout and labels above inputs are useful defaults but not a ban on native forms or compact related fields. The author qualifies marking every required field for familiar or single-question flows. Do not make every question a separate step automatically.
- **Review:** Is each field necessary at this point, is completion status clear, and can users correct a previous answer without starting over?
- **Source / dating:** Ch. 8, pp. 331–345, 361–362. Visual checks:332,339,344. Field width can suggest expected input but must accommodate localization and real formats.


### PU-22 — Keep labels available and help visible when it is needed

- **Trigger:** A person must remember an input’s purpose or discover a formatting requirement.
- **Author’s account:** The author warns that placeholder-only labels disappear during entry and may look like existing values. He places essential hints before inputs, where they are less likely to be missed or covered by the keyboard.
- **Rationale / application:** Keep a persistent and accessible label, put essential constraints where they will be encountered before an avoidable error, and associate help with its field. Verify the focused state with keyboard, autofill, and enlarged text.
- **Exception / conflict:** A familiar search field may use a compact presentation while retaining an accessible name. Optional elaboration can be disclosed. Native layout may place help differently if it remains discoverable and available; the goal is timely comprehension, not copying a web stack mechanically.
- **Review:** While typing or reviewing a filled form, can the user still identify the field, its requirements, and how to correct it?
- **Source / dating:** Ch. 8, pp. 348–352. Visual checks:348,350. The author’s assertion that placeholder contrast is almost always insufficient is not a measured universal property.


### PU-23 — Choose controls for the selection task and commitment model

- **Trigger:** Selecting an item from a long set, changing a quantity, or editing a binary setting.
- **Author’s account:** The author favors visible options for small sets, autocomplete for long known-item lists, steppers for incremental quantities, and control treatments that make selection recognizable. He distinguishes immediate toggle effects from choices submitted later.
- **Rationale / application:** Match the control to whether the person knows the item, needs to compare alternatives, or is exploring. Provide browsing when a search term may be unknown. Make selection, saving, and commitment separate where the domain requires it; expose loading, no-result, and recovery paths.
- **Exception / conflict:** A ten-item threshold is not a law. Steppers can be inefficient for large values. Native toggles can participate in a draft form; preserve the actual commit contract instead of enforcing a web checkbox rule. Custom card selection should retain clear semantics and state.
- **Review:** Can the intended item be found without prior vocabulary, and is it clear whether a selection is tentative or already applied?
- **Source / dating:** Ch. 8, pp. 346–347, 353–360. Visual check:354. Runtime behavior, keyboard interaction, and VoiceOver semantics are our required verification beyond the static book examples.


### PU-24 — Choose validation timing that supports correction

- **Trigger:** An input has format, eligibility, cross-field, or server-side constraints.
- **Author’s account:** The author compares validation on submission, after leaving a field, and while typing; each has timing and implementation tradeoffs. Errors should be removed when resolved, and multiple failures should be findable.
- **Rationale / application:** Choose timing by the constraint and interaction. Avoid interrupting incomplete input with premature errors, preserve entered data, and offer a clear route to each problem. Separate local formatting success from server confirmation or financial completion.
- **Exception / conflict:** Validation on blur can interrupt focus switching and works poorly for some grouped choices. Immediate checks may be suitable after a known error, but must handle asynchronous stale responses. A green mark must not imply an account or transaction is verified when only syntax was checked.
- **Review:** Can users find, understand, correct, and confirm resolution of every error without losing valid work or receiving premature success?
- **Source / dating:** Ch. 8, pp. 364–368. Visual check:367; rendered prose check364. Asynchronous state and preservation requirements are our operational extensions.
