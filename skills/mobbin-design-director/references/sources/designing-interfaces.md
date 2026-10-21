# Designing Interfaces — contextual patterns and coherent experiences

Source: Jenifer Tidwell, Charles Brewer, and Aynne Valencia, *Designing Interfaces: Patterns for Effective Interaction Design*, third edition, O’Reilly Media, January 2020, ISBN 978-1-492-05196-1. The supplied PDF has 602 pages; printed Arabic page 1 is PDF page 21. Citations below use both numbering systems.

This is an original working synthesis, not a replacement for the book. All twelve chapters were studied. The accompanying [coverage ledger](designing-interfaces-coverage.json) distinguishes text actually read, deliberately excluded historical example galleries, and figures actually inspected. Reading extracted captions does not mean inspecting their images. Chapters 2, 3, and 8 have explicit gallery exclusions; no claim of reading or visually checking every page is made. Front matter and the index were not comprehensively studied.

The application and review checks below are this skill's operational interpretation of the cited material. They are hypotheses to test against the product, audience, platform, and actual implementation, rather than proof that a particular screen will work.

## How to combine this source with Mobbin

Start with a user goal, context, content, and required state transitions. Use these principles to choose candidate patterns and articulate their tradeoffs. Then inspect current Mobbin screens and flows for how comparable products implement those patterns on the target platform. Record what was observed separately from inferred behavior and proposed adaptations. Several apps sharing a pattern demonstrates prevalence, not successful outcomes for this audience. Missing examples do not invalidate a justified design.

Research the entry, intermediate decisions, completion, return, and relevant failure states—not just the attractive destination. A reference should answer a specific question: how an iOS flow preserves context, how comparison remains possible, how commitment is communicated, or how a visual system creates emphasis. Retain the useful mechanism while developing a coherent visual language for this product. Screenshots cannot establish behavior they do not show or replace user evaluation.

## DI-01 — Define the person's outcome before the interface

- **Trigger:** Starting a screen, feature, or research brief.
- **Rationale:** Goals, prior knowledge, motivations, and context explain which information and actions matter. A feature inventory or an imagined persona cannot supply that evidence.
- **Apply/review:** Write the intended outcome, audience, usage context, existing behavior, and unknowns. Distinguish observed research from assumptions. Evaluate the flow by whether people achieve the outcome, not whether every requested component appears.
- **Applicability/limits:** Applies to iOS and web. An urgent small change can use a brief assumption record; do not invent research findings to fill it.
- **Source:** Ch. 1, printed pp. 1–11 (PDF pp. 21–31).

## DI-02 — Deliver useful value before asking for avoidable decisions

- **Trigger:** First use, onboarding, registration, setup, or a largely empty initial screen.
- **Rationale:** People often seek a satisfactory next action quickly and may abandon work whose benefit is distant. Premature configuration consumes attention before its relevance is clear.
- **Apply/review:** Identify the first useful result. Defer optional settings and explain unavoidable gates at the moment they matter. Make defaults inspectable and changeable. Check the journey with no existing data or account.
- **Applicability/limits:** Deferral is inappropriate when a choice is necessary to protect the user's interests or correctly perform the task. The goal is useful progress, not pressure to commit.
- **Source:** Ch. 1, Instant Gratification, Satisficing, Deferred Choices, printed pp. 13–16 (PDF pp. 33–36); ch. 2, Mobile Direct Access, printed pp. 51–52 (PDF pp. 71–72).

## DI-03 — Preserve context through interruption, exploration, and return

- **Trigger:** A multistep task, drilldown, switching views, backgrounding, or resuming work.
- **Rationale:** People change their minds and work in short sessions. Losing the draft, selection, or location makes them reconstruct both data and intent.
- **Apply/review:** Define what survives leaving and returning: draft values, selected item, scroll position, filters, and task status. Show enough context to resume. Walk through back, cancel, app interruption, and a change of view with partly completed work.
- **Applicability/limits:** Persistence has security and data-freshness constraints; define expiration and recovery explicitly. Preserving a stale value silently is not always helpful.
- **Source:** Ch. 1, printed pp. 15, 19–22 (PDF pp. 35, 39–42); ch. 2, Alternative Views, printed pp. 97–98 (PDF pp. 117–118); ch. 7, One-Window Drilldown, printed pp. 346–347 (PDF pp. 366–367).

## DI-04 — Support growing fluency without hiding the basic route

- **Trigger:** Repeated data entry, frequent commands, or mixed novice and expert audiences.
- **Rationale:** Stable locations become learned habits, while repetition amplifies small interaction costs. Efficient shortcuts benefit experienced users only when their effect remains understandable.
- **Apply/review:** Keep frequent controls stable; support appropriate keyboard access, repeat actions, saved configurations, or batch operations. Check the first-time path and the tenth repetition separately. Make automation scope and results reviewable.
- **Applicability/limits:** Do not add macros or workspace customization to an occasional simple task merely because the pattern exists. On touch devices, shortcuts need discoverable alternatives.
- **Source:** Ch. 1, printed pp. 18, 20–25 (PDF pp. 38, 40–45); ch. 8, Macros, printed pp. 425–426 (PDF pp. 445–446).

## DI-05 — Organize objects and tasks before choosing screen furniture

- **Trigger:** New information architecture, ambiguous navigation, or screens with unrelated content.
- **Rationale:** Visual polish cannot compensate for a confusing content model. The book's layered model builds presentation on information and interaction structure.
- **Apply/review:** Identify the objects, relationships, task vocabulary, and useful organizing dimensions. Give each screen a recognizable role, such as overview, detail, creation, or action. Test categories and labels with realistic items and awkward exceptions.
- **Applicability/limits:** Exclusive categories are one organizing technique, not a mandate to eliminate legitimate facets or tags. An organization chart is not automatically the user's mental model.
- **Source:** Ch. 2, printed pp. 27–38 (PDF pp. 47–58), particularly fig. 2-1, printed p. 31 (PDF p. 51; visually inspected).

## DI-06 — Select patterns by preconditions and costs

- **Trigger:** Choosing among a wizard, settings page, modal, dashboard, list, or custom composition.
- **Rationale:** The book explains what a pattern does, when it fits, why it helps, and how to implement it. A recognizable name or a popular screenshot is insufficient selection evidence.
- **Apply/review:** Record the user problem, candidate pattern, conditions that make it fit, cost introduced, and rejected alternative. For example, compare a guided sequence with random access when dependencies and expertise differ. Search Mobbin for the specific tradeoff.
- **Applicability/limits:** Patterns can be combined or adapted. A novel arrangement needs a clear rationale and evaluation; it does not need to imitate a reference to be legitimate.
- **Source:** Ch. 2, Wizard and Settings Editor, printed pp. 86–91 (PDF pp. 106–111); ch. 3, Modal Panel, printed pp. 158–160 (PDF pp. 178–180).

## DI-07 — Make location, destination, and return understandable

- **Trigger:** Global navigation, nested content, deep links, or neighboring-item browsing.
- **Rationale:** Navigation architecture determines what is reachable and what context is lost. Orientation cues reduce the need to remember a path.
- **Apply/review:** Map important routes, including external entry and return. Distinguish a hierarchy from history and a sequence from a collection. Use labels, selection state, titles, and appropriate back/up/next actions to make that model visible. Verify the destination makes sense when opened directly.
- **Applicability/limits:** Not every screen needs every destination; focused tasks can reduce navigation. Web breadcrumbs and historical menu placements are not automatic iOS requirements.
- **Source:** Ch. 3, printed pp. 129–142, 155–156, 165–167, 193–195 (PDF pp. 149–162, 175–176, 185–187, 213–215). Hub-and-spoke diagram, fig. 3-1, printed p. 136 (PDF p. 156), visually inspected.

## DI-08 — Guide a sequence without trapping the user

- **Trigger:** Checkout, onboarding, permissions, application forms, or other dependent steps.
- **Rationale:** A sequence can reduce uncertainty and present only relevant work, but rigidity can frustrate experienced users and make correction expensive. Modal focus adds an interruption cost.
- **Apply/review:** Simplify the underlying task first. Define dependencies, progress, backward edits, exit, saved work, and completion. Explain what the current step accomplishes. Compare inline, full-screen, and modal presentations against the need for surrounding context.
- **Applicability/limits:** Do not split a simple task merely to create progress. Random-access configuration and repeated expert work may need another structure. A step indicator is different from a background-operation progress bar.
- **Source:** Ch. 2, printed pp. 86–88 (PDF pp. 106–108); ch. 3, printed pp. 158–160, 171–172, 189–190 (PDF pp. 178–180, 191–192, 209–210).

## DI-09 — Match collection presentation to the user's collection task

- **Trigger:** Search results, catalogs, feeds, libraries, or card grids.
- **Rationale:** Browsing, exact finding, comparing, selecting, and manipulating impose different requirements. Cardinality, ordering, preview detail, and update behavior matter more than fashionable card styling.
- **Apply/review:** Specify the collection task, likely size, ordering, and recognition cues. Compare split view, drilldown, inline expansion, grid, and pagination. Keep place on return. Test empty, one-item, long, heterogeneous, and newly updated collections with real content.
- **Applicability/limits:** A carousel suits exploratory browsing better than precise finding or simultaneous comparison. Infinite loading is not a universal replacement for bounded navigation. Split view needs usable space after content and accessibility adaptations.
- **Source:** Ch. 7, printed pp. 335–358, 361–369 (PDF pp. 355–378, 381–389); ch. 6, Infinite List, printed pp. 322–323 (PDF pp. 342–343).

## DI-10 — Hide secondary detail only when the task can tolerate it

- **Trigger:** Tabs, accordions, collapsible panels, inlays, or dense forms.
- **Rationale:** Disclosure can reduce initial complexity, but hidden material cannot be scanned or compared simultaneously. Expansion can also displace context.
- **Apply/review:** Classify information as primary, optional, or needed together. Keep comparison-critical content visible together. Make disclosure controls and expanded state clear; preserve relevant state. If almost everyone expands a section immediately, reconsider its default.
- **Applicability/limits:** Module tabs fit a small stable set whose contents need not be seen together. Multiple expanded sections may be appropriate; a single-open accordion is not a universal law.
- **Source:** Ch. 4, printed pp. 242–250 (PDF pp. 262–270); ch. 7, List Inlay, printed pp. 349–351 (PDF pp. 369–371); ch. 2, Dashboard, printed pp. 78–79 (PDF pp. 98–99).

## DI-11 — Use hierarchy and spacing to communicate relationships

- **Trigger:** A screen feels cluttered, flat, disconnected, or difficult to scan.
- **Rationale:** Position, scale, contrast, alignment, and proximity make importance and grouping visible. More whitespace is not automatically clearer: evenly separating everything can erase useful relationships.
- **Apply/review:** Identify the primary content and next action. Group related content more tightly than unrelated groups; align by meaningful relationships. Check the composition at a glance and with long text. Use a grid as support, not an excuse to make all elements equally prominent.
- **Applicability/limits:** Dense expert tools and spacious editorial experiences can both work. Reading order, text size, content, and task determine useful density.
- **Source:** Ch. 4, printed pp. 209–222, 231–239 (PDF pp. 229–242, 251–259). Figs. 4-1, 4-4, 4-12 at printed pp. 210, 213, 218 (PDF pp. 230, 233, 238) visually inspected.

## DI-12 — Maintain a visual framework across the complete flow

- **Trigger:** Combining references, extending an existing product, or designing multiple screen families.
- **Rationale:** Repeated structure helps people recognize location and action conventions. Independently attractive screens can create a confusing experience when their visual meanings conflict.
- **Apply/review:** Establish stable navigation, spacing relationships, type roles, control states, and content regions. Review entry, work, success, and error screens together. Reuse meaning as well as appearance; justify a deviation by a different task or hierarchy.
- **Applicability/limits:** Consistency allows variation. A media canvas, settings page, and purchase confirmation do not need identical layouts, and platform conventions can require distinct components.
- **Source:** Ch. 4, Visual Framework, printed pp. 228–230 (PDF pp. 248–250); ch. 5, printed pp. 258, 280–282 (PDF pp. 278, 300–302); ch. 11, printed pp. 533–541 (PDF pp. 553–561).

## DI-13 — Give visual expression an intentional job

- **Trigger:** Choosing a visual direction, imagery, texture, illustration, or degree of ornament.
- **Rationale:** Style communicates personality, expectation, and emotional tone alongside utility. Removing all decoration does not guarantee clarity or a distinctive experience.
- **Apply/review:** State the intended feeling and audience fit, then connect typography, palette, imagery, shape, and density to it. Compare coherent alternatives using representative content. Preserve action clarity and reading comfort while refining the distinctive details.
- **Applicability/limits:** Cultural associations and aesthetic preferences vary. Long-use work tools may need a quieter treatment than a short promotional experience. A beautiful reference does not demonstrate improved trust or conversion for this product.
- **Source:** Ch. 5, printed pp. 255–258, 274–294 (PDF pp. 275–278, 294–314). Figs. 5-1 and 5-18, printed pp. 257, 275 (PDF pp. 277, 295), visually inspected as style/density comparisons, not outcome evidence.

## DI-14 — Make visual distinctions readable and semantically reliable

- **Trigger:** Type selection, color roles, icons, status indicators, or visual polish.
- **Rationale:** Legibility and consistent visual meaning let people read and act without decoding the interface. Color and unfamiliar symbols alone can make information inaccessible or ambiguous.
- **Apply/review:** Test real names, numbers, long labels, and easily confused glyphs. Reinforce meaningful color differences with text, shape, or another cue. Keep icon families coherent and label unfamiliar actions. Check the actual rendered content in relevant themes and sizes.
- **Applicability/limits:** The book's point-size suggestions and broad font/color associations are not current accessibility specifications. Verify platform requirements and contrast separately. Never reduce helper text to illegibility merely to make it visually secondary.
- **Source:** Ch. 5, printed pp. 258–274, 278–280 (PDF pp. 278–294, 298–300); ch. 10, printed pp. 525–526 (PDF pp. 545–546).

## DI-15 — Design mobile around context and capabilities

- **Trigger:** An iOS screen, an adaptive interface, or a web concept being translated to mobile.
- **Rationale:** Attention, environment, input effort, interruption, and available space change the interaction. Device capabilities can reduce work when they actually serve the task.
- **Apply/review:** Identify mobile-critical tasks; prioritize useful content and reachable actions. Preserve reentry context, accommodate touch, and avoid unnecessary typing. Evaluate camera, location, sharing, and other device integrations only with a clear benefit and an appropriate consent path. Research native iOS implementation separately from mobile web.
- **Applicability/limits:** Do not blindly remove needed functionality. The book contains obsolete device assumptions and dimensions; it cannot define today's iOS APIs, safe areas, text behavior, or target-size requirements. Its Bottom Navigation pattern is a mobile-web footer, not an iOS tab bar.
- **Source:** Ch. 6, printed pp. 295–300, 307–314, 316–317, 325–332 (PDF pp. 315–320, 327–334, 336–337, 345–352).

## DI-16 — Make actions discoverable and their scope explicit

- **Trigger:** Toolbars, contextual actions, gestures, menus, or a crowded action area.
- **Rationale:** People need to recognize what is actionable, what it affects, and what result to expect. Proximity and meaningful labels clarify scope; hidden interaction idioms require prior knowledge.
- **Apply/review:** Group commands by task and affected object. Name primary actions with specific verbs. Expose important actions without requiring hover or an undisclosed gesture. Check keyboard/focus and touch alternatives as appropriate, including the action's enabled and disabled states.
- **Applicability/limits:** Contextual controls can reduce clutter for occasional expert actions. They should not make an essential route unavailable on another input method or obscure why an action is unavailable.
- **Source:** Ch. 8, printed pp. 375–382, 384–392, 396–397, 402 (PDF pp. 395–402, 404–412, 416–417, 422).

## DI-17 — Make commitment and recovery part of the action model

- **Trigger:** Saving, submitting, deleting, purchasing, or performing a costly operation.
- **Rationale:** Preview, cancel, undo, and history address different moments and risks. An apparent escape is harmful when the operation has already committed or the user's work disappears unexpectedly.
- **Apply/review:** Specify the exact commit point, affected objects, reversibility, cancellation boundary, and recovery route. Preview consequential output when it helps prediction; label the final action clearly. Test cancellation during work and meaningful undo after completion.
- **Applicability/limits:** Not every action needs a confirmation or preview. Do not promise transactional reversibility the backend cannot provide. The book's examples of irreversible actions and undo-stack sizes are contextual, not universal policies.
- **Source:** Ch. 8, printed pp. 396–397, 404–405, 415–423 (PDF pp. 416–417, 424–425, 435–443).

## DI-18 — Show honest progress while keeping useful work available

- **Trigger:** Loading, saving, search, upload, refresh, or other asynchronous work.
- **Rationale:** Timely feedback distinguishes an accepted action from a frozen interface. Local progress can preserve context and allow independent tasks to continue.
- **Apply/review:** Define initial, partial, working, success, failure, retry, and cancellation states. Show determinate progress only when it corresponds to known work. Keep indicators close to the affected content, explain blocking waits, and preserve already usable content where appropriate.
- **Applicability/limits:** Background concurrency must not imply that stale or uncommitted data is final. Partial content is useful only when its incompleteness is clear. Avoid treating the book's timing examples as universal thresholds.
- **Source:** Ch. 6, Loading Indicators, printed pp. 328–330 (PDF pp. 348–350); ch. 8, Spinners and Loading Indicators and Cancelability, printed pp. 409–410, 415–416 (PDF pp. 429–430, 435–436).

## DI-19 — Design data displays around the question and comparison

- **Trigger:** A dashboard, report, chart, metric card, or analytical overview.
- **Rationale:** The useful representation depends on whether people need an exact value, trend, outlier, relationship, or comparison. Decoration and mismatched scales can obscure the question.
- **Apply/review:** Write the question each display answers. Choose structure, encoding, ordering, labels, and precision accordingly. Compare values using an appropriate common baseline or consistent small multiples. Check whether a table is more useful for exact lookup.
- **Applicability/limits:** A shared time axis with stacked separate plots is different from an arbitrary overlaid dual-axis chart. Small multiples need enough room for their information to remain legible; not every desktop analysis transfers unchanged to a phone.
- **Source:** Ch. 9, printed pp. 433–446, 462–468 (PDF pp. 453–466, 482–488). Figs. 9-9 and 9-27, printed pp. 443, 468 (PDF pp. 463, 488), visually inspected.

## DI-20 — Let people narrow data without losing orientation

- **Trigger:** Search filters, datatips, linked charts, dynamic queries, or dense analytical content.
- **Rationale:** Filtering, highlighting, and selection can reduce complexity while preserving a useful overview. Their behavior must make the relationship between query and result understandable.
- **Apply/review:** Show current constraints and selected entities; provide a clear way to reset. Give responsive feedback without disrupting typing. Distinguish hiding from highlighting. Keep detailed values available through an appropriate touch, keyboard, or focus interaction and preserve their connection to the source mark.
- **Applicability/limits:** Hover-only details do not translate to touch. Multi-view brushing requires space and consistent entity identity. An empty filtered result needs a recovery path, not an unexplained blank canvas.
- **Source:** Ch. 9, printed pp. 443–460 (PDF pp. 463–480), especially Datatips, Spotlight, Dynamic Queries, and Brushing.

## DI-21 — Treat every form field as work to justify

- **Trigger:** Registration, checkout, profile editing, settings, or information collection.
- **Rationale:** Fields cost attention and invite misunderstandings about terminology, purpose, and acceptable answers. A shorter form helps only if the remaining questions are clear and sufficient.
- **Apply/review:** Explain the exchange of effort for value, remove unnecessary questions, group related work, and use persistent labels. Indicate required/optional status consistently. Check localization, writing direction, long labels, keyboard behavior, and what happens after success.
- **Applicability/limits:** A placeholder is not a substitute for a persistent label. Top-aligned labels are an option, not a universal layout rule. A sentence-style input can clarify a relationship but may need restructuring in another language.
- **Source:** Ch. 10, printed pp. 471–477, 485–486, 489–495 (PDF pp. 491–497, 505–506, 509–515).

## DI-22 — Assist entry without overruling intent

- **Trigger:** Formatting rules, autocomplete, default values, or complex selection controls.
- **Rationale:** Good assistance reduces typing and memory burden. Bad guesses create correction work or silently substitute the system's assumptions for the person's choice.
- **Apply/review:** Accept harmless formatting variations, expose ambiguous interpretations, and keep suggestions rejectable. Derive defaults only from a defensible context; make them easy to inspect and change. Test paste, correction, unusual valid values, and repeated rejection of a suggestion.
- **Applicability/limits:** Structured entry fits genuinely fixed formats; names, addresses, and international telephone numbers often are not fixed. Avoid defaults for sensitive assumptions or consequential consent. Suggestions must not interfere with ordinary typing.
- **Source:** Ch. 10, printed pp. 477–483, 502–505, 510–511, 519–520 (PDF pp. 497–503, 522–525, 530–531, 539–540).

## DI-23 — Keep error correction beside the work

- **Trigger:** Validation, rejected submission, conflicting values, or an interrupted form.
- **Rationale:** Errors are easier to resolve when the field, explanation, and corrective action remain together. Premature errors and disappearing instructions waste attention.
- **Apply/review:** Prevent avoidable errors with examples and appropriate controls. When an error is meaningful, identify the field and explain a concrete correction in ordinary language; preserve other entered values. Use cues beyond color and confirm successful completion. Test the actual failure-to-recovery sequence.
- **Applicability/limits:** Do not show an invalid-state message simply because someone has started typing a potentially valid value. Disabled submission is not a universal solution; users still need to understand unmet requirements. Password examples in this book are not current security requirements.
- **Source:** Ch. 10, printed pp. 473–474, 497–499, 524–531 (PDF pp. 493–494, 517–519, 544–551). Fig. 10-49, printed p. 527 (PDF p. 547), visually inspected as a three-state form example with local and summary feedback.

## DI-24 — Build a design system that preserves intent across platforms

- **Trigger:** Implementing several screens, coordinating agents, or extending a component library.
- **Rationale:** Shared components and visual rules prevent accidental divergence and free attention for difficult interactions. Their value lies in supporting coherent real experiences, not maximizing reuse at all costs.
- **Apply/review:** Define reusable styles, components, compositions, states, and screen roles. Evaluate assembled pages with realistic content and complete flows. Keep platform-specific interaction variants when needed. For a system extension, document the user need, semantic role, and reusable behavior before adding another visual exception.
- **Applicability/limits:** Web framework examples are historical illustrations, not technology recommendations or native iOS specifications. Consistent identity need not mean identical widgets. A library should enable a justified experience rather than prohibit it.
- **Source:** Ch. 11, printed pp. 533–543, 556 (PDF pp. 553–563, 576). Cross-platform Fluent picker examples, figs. 11-3/11-4, printed p. 537 (PDF p. 557), visually inspected.

## Boundaries and source-age checks

- **Platform currency:** The mobile chapter mixes native, mobile-web, and older device assumptions. Do not retain its historical market shares, screen dimensions, top-screen pixel budgets, inter-app restrictions, or exact touch/motion values as current requirements. Verify iOS behavior and accessibility through current platform sources at implementation time.
- **Prescriptive examples:** Fixed font sizes, fixed undo depths, a default maximum count of items, mandatory disabled submit, password composition examples, and specific library recommendations are not universal rules. The source contains internally useful examples alongside recommendations that need current scrutiny.
- **Terminology:** Bottom Navigation in ch. 6 is footer navigation; Progress Indicator in ch. 3 is sequence orientation; Multi-Y Graph in ch. 9 uses separate stacked plots with a common horizontal dimension. Preserve meaning rather than matching a pattern name superficially.
- **Evidence:** A book illustration and a Mobbin screenshot demonstrate a design choice, not its causal effect on usability, trust, retention, or conversion. Appearance, prevalence, and successful user outcomes are different observations.
- **Beyond the screen:** Ch. 12 was read in full. Its short overview of connected, anticipatory, assistive, and natural interfaces informs scenario awareness, but supplies no adequate implementation or evaluation method for current AI/IoT systems. No separate automation principle is asserted from it.
- **Coverage:** Some historical screenshot galleries in chs. 2, 3, and 8 were intentionally excluded after their surrounding pattern explanations were read. All text was read in chs. 1, 4–7, and 9–12, including the text/captions of their historical examples; only the figures listed in the ledger were visually inspected. No book text, extracted image, or PDF is distributed with these notes.
