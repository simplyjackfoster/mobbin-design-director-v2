# About Face — source dossier

Alan Cooper, Robert Reimann, David Cronin, and Christopher Noessel, with Jason Csizmadi and Doug LeMoine. *About Face: The Essentials of Interaction Design*. Fourth edition, John Wiley & Sons, 2014. ISBN 978-1-118-76657-6. The supplied PDF has 722 pages. Identity, checksum, chapter coverage, and visual checks are recorded in [the coverage ledger](about-face-coverage.json).

All 21 chapter bodies were studied in bounded page batches: chapters 1–17 by the core source reviewer and chapters 18–21 by a separate source agent, whose chapter notes and ledger were integrated and reviewed. Historical examples, desktop/web material, and specialized device discussions were read and assessed rather than silently skipped. Eighteen selected figure pages were rendered and visually inspected across the two reviewers. Other images were not independently visually verified. This is original synthesis, not a replacement for the book or independent verification of its cited studies.

PDF citations are **one-based file pages**. For Arabic chapter pages, printed page = PDF page minus 30. Some chapter endpoints are blank; the ledger uses a null printed endpoint and records the last numbered content page. Application and review steps below are operational adaptations, not quotations or claims that this 2014 edition specifies contemporary iOS behavior. Fetch current Apple, web, and accessibility guidance for normative requirements.

## Principles

### AF-01 — Organize the experience around goals and a coherent user model

- **Trigger:** A new product, navigation structure, or feature that mirrors services, database tables, or an organization chart.
- **Rationale:** Tasks and implementation can change while a person's desired outcome remains. Exposing internal machinery forces people to learn it before succeeding.
- **Application:** State the outcome, circumstances, meaningful objects, and relationships in the brief. Use these to organize screens and language. Explain how a person would predict the next action and its effect.
- **Boundary:** The model is a research-informed hypothesis, not a designer's assumption about all people. Technical constraints still exist; present their consequences intelligibly when relevant.
- **Review:** Trace each main screen and action to a goal. Identify internal concepts that users must unnecessarily decode.
- **Source:** Chapter 1, PDF 44–58 / printed 14–28; chapter 13, PDF 330–331 / printed 300–301. Figure 1-4, PDF 49 / printed 19, visually checked.

### AF-02 — Separate user evidence, domain knowledge, and design conjecture

- **Trigger:** Discovery, competitor research, a persona, or a claim that a screen solves a user problem.
- **Rationale:** Buyers, stakeholders, experts, and users supply different evidence. Reported behavior and observed behavior answer different questions; neither a beautiful reference nor an expert's opinion establishes user success.
- **Application:** Record who supplied each claim, context, what was observed versus said, and what remains unknown. Combine qualitative explanation with relevant quantitative evidence. Explore artifacts, exceptions, workarounds, and environmental constraints.
- **Boundary:** No fixed interview count guarantees understanding. Mobbin evidence describes an interface; AI interpretation does not become participant evidence. Avoid importing the book's stronger criticisms of particular methods as universal exclusions.
- **Review:** Find every assertion about users and attach evidence or an assumption label. Identify the next observation that could disprove the design premise.
- **Source:** Chapter 2, PDF 62–85 / printed 32–55; chapter 5, PDF 169–173 / printed 139–143.

### AF-03 — Use behavioral personas honestly, including provisional ones

- **Trigger:** Several audiences, conflicting workflows, or an ambiguous target user.
- **Rationale:** A focused behavioral model can prevent designing for a convenient imaginary person whose needs change with each design argument.
- **Application:** Ground goals, expertise, frequency, constraints, and behavior in research. Prioritize the experience while accounting for secondary needs. If research is absent, make the model explicitly provisional and list assumptions and validation questions.
- **Boundary:** Do not invent quotations, research participants, statistical precision, or demographic stereotypes. Accessibility and rare serious consequences are not disposable because a persona is secondary.
- **Review:** Check that the persona changes concrete decisions and that each substantive trait has a traceable basis. Revise it when observations conflict.
- **Source:** Chapter 3, PDF 92–108, 111–129 / printed 62–78, 81–99; provisional-persona discussion PDF 127 / printed 97.

### AF-04 — Define context scenarios and needs before committing to screens

- **Trigger:** Starting a flow, choosing an interaction framework, or jumping directly into polished mockups.
- **Rationale:** A narrative of intent, context, sequence, and outcome exposes requirements that a static inventory of features misses.
- **Application:** Write a short scenario in the person's terms; derive required information, actions, and context. Sketch relationships and transitions cheaply before refining controls. Include business and technical constraints without letting them replace the user goal.
- **Boundary:** The book's aspirational “magic” exercise is an ideation device, not permission to hide consequences or automate actions without intent. A scenario is not a usability test.
- **Review:** Walk the sketch from trigger to outcome. Ask what the person must know, decide, and do at each transition and whether the necessary information is available.
- **Source:** Chapter 4, PDF 132–147 / printed 102–117; chapter 5, PDF 150–159 / printed 120–129. Framework sketch on PDF 156 / printed 126 visually checked.

### AF-05 — Validate the main path, alternatives, and consequential exceptions

- **Trigger:** A proposed flow appears complete because its ideal sequence looks convincing.
- **Rationale:** The main scenario establishes coherence, but real use includes alternative entry, interruptions, mistaken decisions, missing information, and necessary exceptional tasks.
- **Application:** Build a flow/state map with the common path, meaningful branches, recovery, and termination. Check each against context scenarios. Use realistic prototypes for formative feedback while changes are still practical.
- **Boundary:** Low frequency is not low importance when harm, exclusion, or loss is high. The book's preference for probable cases must not erase such situations. Expert walkthrough findings remain predictions until tested with users.
- **Review:** Attempt interruption and return, backtracking, cancellation, partial completion, and relevant failures. State which behaviors the prototype cannot test.
- **Source:** Chapter 4, PDF 136 / printed 106; chapter 5, PDF 160, 169–173 / printed 130, 139–143; chapter 6, PDF 188–191 / printed 158–161.

### AF-06 — Develop visual direction alongside behavior and emotional intent

- **Trigger:** Selecting a visual style, comparing references, or producing screens that look unrelated across a flow.
- **Rationale:** Visual form communicates the product's character and supports behavior; polishing a disconnected screen can conceal unresolved structure.
- **Application:** Define a small set of experience attributes in concrete terms. Explore meaningfully different directions, apply a chosen direction to a representative screen, then test it across the flow and content extremes. Preserve the behavioral rationale through refinement.
- **Boundary:** Attributes are decision criteria, not a substitute for measurable usability or access. A style guide alone does not establish a coherent design language. Do not claim one universally optimal visual or behavioral framework.
- **Review:** Explain how typography, hierarchy, imagery, motion, and language support the attributes and task. Check whether visual refinement has obscured an action or relationship.
- **Source:** Chapter 5, PDF 161–169 / printed 131–139; chapter 17, PDF 442–443, 461–462 / printed 412–413, 431–432. Refined-screen example PDF 168 / printed 138 visually checked.

### AF-07 — Keep design, implementation, and validation in a continuing conversation

- **Trigger:** Delegating agents, handing off a design, or discovering feasibility constraints during development.
- **Rationale:** Complementary generation and synthesis improve coverage, while shared rationale helps preserve the experience when details change.
- **Application:** Assign clear responsibilities for proposal, evidence gathering, implementation, and independent critique. Integrate findings into one coherent design. Invite technical feedback early and validate evolving work rather than treating approval as the end of design.
- **Boundary:** The book discusses human teams; agent roles are this skill's adaptation, not evidence that AI reviewers represent users. It explicitly revises an earlier belief that all design must precede coding.
- **Review:** Require dissent and evidence before consensus. Track which implementation compromises affect user goals and recheck the affected flow.
- **Source:** Chapter 6, PDF 177–191 / printed 147–161; especially PDF 188–191 / printed 158–161.

### AF-08 — Transfer a pattern's reasoning, not just its appearance

- **Trigger:** Choosing Mobbin references or reusing a familiar component.
- **Rationale:** A useful pattern joins a problem, context, constraints, and relationships. Its visible arrangement is only part of the solution.
- **Application:** For every adopted reference, record the relevant user job, entry state, behavior, tradeoff, and reason it fits this product. Compare alternatives and preserve only the mechanism that serves the current task.
- **Boundary:** Adoption by a polished product is not evidence of success. Historical screenshots, such as the book's drawer examples, are neither current platform requirements nor universal defaults.
- **Review:** Explain when the pattern would fail, what adaptation is needed, and which observed behavior remains unverified from a screenshot.
- **Source:** Chapter 7, PDF 198–208 / printed 168–178; especially PDF 205–206 / printed 175–176; chapter 17, PDF 458–461 / printed 428–431.

### AF-09 — Make assistance considerate, transparent, and recoverable

- **Trigger:** Defaults, remembered settings, automation, drafts, sharing, or background work.
- **Rationale:** Repeated setup, lost input, unpredictable changes, and unclear audience undermine trust and increase effort.
- **Application:** Preserve appropriate work and preferences, disclose consequential defaults, make correction possible, and show meaningful scope and status. Respect privacy and the user's chosen audience. Define what cancellation actually stops or reverses.
- **Boundary:** Do not translate suggestions to remember everything or work proactively into unrestricted collection or action. Incomplete drafts must remain distinguishable from valid committed records. Compute, battery, bandwidth, and privacy constrain assistance.
- **Review:** Check restart, interruption, account change, changed defaults, canceled work, and accidental sharing for relevant flows.
- **Source:** Chapter 8, PDF 211–228, 231–234 / printed 181–198, 201–204; chapter 14, PDF 358–362 / printed 328–332.

### AF-10 — Choose structure for the actual platform and use posture

- **Trigger:** Moving a web design to iOS, adding tablet support, or choosing density and navigation.
- **Rationale:** Attention, duration, frequency, input, physical surroundings, and available space affect what an interface should expose and how it should behave.
- **Application:** Describe the use posture before choosing a layout. Let frequent complex work, brief focused tasks, and background processes have appropriate access and feedback. Reassess posture by feature when necessary.
- **Boundary:** A phone does not guarantee a brief session, nor does desktop imply fullscreen. The book's 2014 device ratios, multitasking limits, and platform predictions are historical.
- **Review:** Test realistic content and interruption conditions on the intended device class. Check whether density, input effort, and required attention match the task.
- **Source:** Chapter 9, PDF 235–265 / printed 205–235; chapter 19, PDF 538–548, 583–598 / printed 508–518, 553–568.

### AF-11 — Support learning and fluency without hiding essential actions

- **Trigger:** A feature serves first-time, occasional, frequent, and expert users.
- **Rationale:** Familiarity is task-specific. Visible explanations help discovery; practiced users benefit from quicker routes to frequent actions.
- **Application:** Establish the real working set from evidence. Keep essential actions discoverable, disclose advanced complexity when useful, and offer contextual bridges from visible commands to efficient shortcuts or gestures.
- **Boundary:** Do not assume every novice becomes expert, impose a fixed click limit, or expose dangerous commands as effortless shortcuts. Progressive disclosure can create search and navigation costs.
- **Review:** Check first encounter, return after absence, and repeated use. A shortcut should supplement an understandable route when the task requires it.
- **Source:** Chapter 10, PDF 267–277 / printed 237–247; chapter 16, PDF 410–414 / printed 380–384; chapter 18, PDF 479–492 / printed 449–462.

### AF-12 — Remove unnecessary work while preserving orientation

- **Trigger:** A flow has repeated detours, reentry, unclear location, or a deceptively minimal screen.
- **Rationale:** Cognitive, memory, visual, and physical effort all matter. Fewer visible controls or clicks can still demand more remembering and searching.
- **Application:** Identify work that serves the goal and work imposed by the interface. Keep related information and controls near the decision; provide stable location cues and meaningful overviews. Map each control clearly to its target and result.
- **Boundary:** Not all navigation, hierarchy, confirmation, or scrolling is waste. Deliberate steps may support understanding or consequential decisions. Reject universal pane counts and mechanically copied physical limitations.
- **Review:** Trace the task and mark context changes, memory demands, unnecessary typing, ambiguous targets, and recovery costs. Compare total effort rather than click totals.
- **Source:** Chapter 11, PDF 280–297 / printed 250–267; chapter 12, PDF 301–323, 327 / printed 271–293, 297. Mapping examples PDF 322 / printed 292 visually checked.

### AF-13 — Make manipulation discoverable and its effects perceivable

- **Trigger:** Gestures, custom controls, drag-and-drop, hidden actions, or a novel visual metaphor.
- **Rationale:** Learned conventions and visible cues help people predict manipulation; immediate feedback connects an action to its result. Touch lacks the hover clues available to pointer interaction.
- **Application:** Provide meaningful labels and signifiers, feedback during and after action, appropriate precision aids, and an alternative when discovery or motor demands warrant it. Teach uncommon gestures in context and avoid conflicts with navigation.
- **Boundary:** Direct manipulation is not always easiest. Do not assume one exposure guarantees learning or force every interaction into a physical metaphor. Tutorials cannot compensate for all hidden controls; current platform conventions govern long press and gestures.
- **Review:** Inspect first-use discovery, cancellation, precision, one-handed use where relevant, and accessible alternatives. Distinguish screenshot observation from verified live behavior.
- **Source:** Chapter 13, PDF 333–353 / printed 303–323; chapter 19, PDF 568–573, 579–583 / printed 538–543, 549–553. Figures PDF 346 / printed 316 and PDF 573 / printed 543 visually checked.

### AF-14 — Accept meaningful input without silently changing intent

- **Trigger:** Forms, structured fields, numerical settings, or incomplete records.
- **Rationale:** Real information arrives in varied formats and stages. Rigid syntax and premature validation obstruct work; silent correction can introduce a different error.
- **Application:** Fit controls to the domain, show units and valid choices, allow useful suggestions, preserve entered content, and distinguish editable draft state from final validation. Explain ambiguity or rejection near the field at a useful moment.
- **Boundary:** Flexibility never removes necessary security or data-integrity checks. Do not silently clamp material values, guess addresses, replace user meaning, or apply the book's fixed validation timing to every field.
- **Review:** Try paste, locale variations, partial values, unusual valid data, corrections, missing information, and interrupted entry. Check what is retained after failure.
- **Source:** Chapter 14, PDF 356–362 / printed 326–332; chapter 21, PDF 633–650 / printed 603–620.

### AF-15 — Make persistence, copies, and versions match the user's intention

- **Trigger:** Editing, autosave, document creation, export, or collaborative work.
- **Rationale:** Internal distinctions between memory, storage, and copies should not force people to gamble with their work.
- **Application:** Design explicit semantics for draft persistence, synchronization, duplicate, rename, move, export, and version restore as relevant. Preserve work automatically when appropriate and give truthful status. Make restoration itself recoverable where feasible.
- **Boundary:** Autosave is not publication or consent to send; local persistence is not confirmed remote synchronization. Versioning must respect privacy, retention, collaboration, and backend constraints. Do not promise unlimited history or effortless selective undo.
- **Review:** Interrupt connectivity and editing, reopen work, restore an earlier version, and verify which copy is active. State exactly what the system has saved and what remains pending.
- **Source:** Chapter 14, PDF 367–374 / printed 337–344; chapter 15, PDF 396, 403–405 / printed 366, 373–375.

### AF-16 — Let people retrieve and refine by what they remember

- **Trigger:** Search, catalogs, history, filters, or large collections.
- **Rationale:** People may remember content, time, relationships, or purpose without remembering a filename or location. Query formulation often develops through interaction.
- **Application:** Offer relevant attributes, suggestions, synonyms, categories, and visible active constraints. Preserve query and selection state through refinement; provide a useful no-results route. Distinguish filtering from ranking even when adjacent.
- **Boundary:** Avoid unrestricted history retention or invisible query changes. The book's database limitations and natural-language pessimism are historical assertions, not current technical constraints. Search does not eliminate a useful browse structure.
- **Review:** Search with partial and alternative wording; refine multiple constraints; recover from no results; return from an item without losing context.
- **Source:** Chapter 14, PDF 375–385 / printed 345–355; chapter 19, PDF 574–578 / printed 544–548; chapter 20, PDF 607–610 / printed 577–580. Search/refinement figures PDF 578 / printed 548 visually checked.

### AF-17 — Prevent predictable mistakes and provide honest reversibility

- **Trigger:** Destructive actions, exploration, adjustment, history, or a decision whose effect is hard to foresee.
- **Rationale:** Clear feedback, preview, and recoverability reduce uncertainty and make exploration safer than relying on repetitive warnings.
- **Application:** Expose relevant state and consequences before action; provide useful preview or comparison; label undo scope and maintain consistent recovery semantics. For external or recorded transactions, distinguish cancellation, delay, correction, and compensating action.
- **Boundary:** Some effects cannot be undone. Selective history reversal can have dependencies. Do not suppress necessary consent or replace critical failure cues with silence; visual and audible feedback must have accessible equivalents.
- **Review:** Undo after intervening actions, save, navigation, and selection changes. Verify exactly what is restored and what external effects remain.
- **Source:** Chapter 15, PDF 388–407 / printed 358–377; especially PDF 395–405 / printed 365–375.

### AF-18 — Build inclusion, localization, and useful help into the flow

- **Trigger:** Any user-facing flow, particularly compact screens, time limits, customization, or unfamiliar features.
- **Rationale:** Variation in abilities, language, familiarity, and context changes how people perceive, operate, and understand the same interface.
- **Application:** Support system accessibility tools and settings, appropriate keyboard routes, redundant feedback, meaningful text equivalents, flexible time, and consistent task structure. Check translation in context. Provide concise contextual help, recoverable customization, and a way to revisit instruction.
- **Boundary:** Do not default to a separate accessibility mode or assume accessibility personas are secondary. The book's contrast percentages, timing multiples, flash rates, and tour lengths are not current standards. Placeholder hints do not replace persistent labels.
- **Review:** Test enlarged text, assistive navigation, focus, alternative input, relevant locales, prolonged tasks, and return after interruption. Treat automated checks as partial evidence.
- **Source:** Chapter 16, PDF 415–433 / printed 385–403; especially PDF 428–433 / printed 398–403.

### AF-19 — Make hierarchy, grouping, and visual language express the task

- **Trigger:** Screen composition, system tokens, charts, visual critique, or inconsistent screens.
- **Rationale:** Relative position, scale, contrast, spacing, and repeated treatment communicate priority and relationships. Unnecessary variation makes interpretation harder.
- **Application:** Rank content by the scenario, align and group related elements, use a flexible grid, and reserve emphasis for what matters. Keep icons and behavior consistent. Show comparable data with useful context, direct labels, and numerical values where needed.
- **Boundary:** Visual restraint must not erase discoverability or legibility. A fixed grid, golden ratio, font minimum, or muted palette is not a universal recipe. Correlation is not causation, despite the source's loose language; its numerical geometry typo is excluded.
- **Review:** Check hierarchy at a glance, then verify it with actual tasks and content. Recheck long labels, expanded text, empty/loaded/error states, and visual differences that imply different behavior.
- **Source:** Chapter 17, PDF 435–461 / printed 405–431; especially PDF 443–458 / printed 413–428. Grid and path figures PDF 445, 448 / printed 415, 418 visually checked.

### AF-20 — Keep task controls in context and define dialog commitment

- **Trigger:** Editors, secondary panes, sheets, dialogs, or repeated adjustment.
- **Rationale:** Separate controls can hide the object of work and force repeated context switches. Immediate effects and confirm-on-completion are different interaction contracts.
- **Application:** Compare an adjacent contextual surface with a sheet or focused flow for the actual device. Make the affected object, draft status, commit point, and exit behavior explicit. Avoid nested dialogs with ambiguous cancellation scopes.
- **Boundary:** Modeless controls are not always preferable; space, focus, and consequences matter. Do not impose historical fullscreen, close-button, or OK/Cancel conventions on modern iOS or web.
- **Review:** Walk repeated edits, changed selection, back, cancel, dismiss, and commit. Verify what persists after each exit.
- **Source:** Chapter 18, PDF 474–478, 493–495 / printed 444–448, 463–465; chapter 19, PDF 543–546 / printed 513–516; chapter 21, PDF 655–671 / printed 625–641. Figures PDF 475–476 / printed 445–446 visually checked.

### AF-21 — Make command scope, state, and activation unmistakable

- **Trigger:** Selection, bulk actions, toggles, active tools, or drag-and-drop.
- **Rationale:** A command is predictable only when people understand what it affects, the current state, and when its effect becomes final.
- **Application:** Distinguish selection from activation, current state from the available action, and one-shot commands from persistent modes. Show relevant selected scope including offscreen objects. Give valid-destination and completion feedback, escape, and a usable alternate route.
- **Boundary:** Use contemporary platform behavior rather than hand-implementing historical drag thresholds or modifier keys. Common media conventions need not be replaced because the author prefers another representation.
- **Review:** Test accidental movement, canceled drag, mixed selection, offscreen selections, and selection changes while contextual properties remain open.
- **Source:** Chapter 18, PDF 504–527 / printed 474–497; chapter 21, PDF 623–628, 633–635 / printed 593–598, 603–605. Figures PDF 520, 626, 635 / printed 490, 596, 605 visually checked.

### AF-22 — Adapt mobile structure while preserving each destination's place

- **Trigger:** Native iOS navigation, phone/tablet variants, or an interrupted mobile task.
- **Rationale:** Compact drilldown and adjacent detail have different costs. Independent destinations remain understandable when their navigation and work survive switching and return.
- **Application:** Define top-level destinations versus contextual actions, preserve appropriate per-destination state, and adapt groups to available space and input. Use transitions consistently to explain relationships. Consider current inter-app facilities when they reduce manual bridging.
- **Boundary:** Mobile is not uniformly transient or subordinate to desktop. Old tab counts, placements, aspect ratios, drawer conventions, and integration limits require contemporary evidence. Do not retain sensitive state indiscriminately.
- **Review:** Switch destinations, return after interruption, change width/orientation where supported, and enlarge text. Check location, selection, and work continuity.
- **Source:** Chapter 19, PDF 538–570, 583–588 / printed 508–540, 553–558. Historical tab examples PDF 559 / printed 529 visually checked; preservation behavior is supported by prose, not inferred from the image.

### AF-23 — Preserve orientation through scrolling, reflow, and return

- **Trigger:** Responsive web pages, infinite collections, long documents, or content that changes size.
- **Rationale:** Scrolling and adaptation are navigation. Users need a comprehensible location, reachable actions, and a dependable route back.
- **Application:** Adapt content groups and navigation rather than merely scaling them. Preserve return position where appropriate; show meaningful extent or overview cues. Check deep items, keyboard access, end conditions, footer reachability, and changing content.
- **Boundary:** Infinite loading suits some browsing tasks and harms others. Not every page needs a sticky header, parallax, or an overview. The source's fixed breakpoint and historical browser assumptions are not specifications.
- **Review:** Open a deep item and return, resize the layout, navigate without a pointer, and attempt to reach the final content and persistent actions.
- **Source:** Chapter 20, PDF 599–616 / printed 569–586; chapter 21, PDF 651–654 / printed 621–624. Responsive and navigator figures PDF 616, 654 / printed 586, 624 visually checked.

### AF-24 — Communicate progress and failure with a concrete recovery route

- **Trigger:** Loading, offline work, failed saving, notifications, or confirmation dialogs.
- **Rationale:** Routine interruption trains dismissal, while vague feedback leaves people unsure what happened or whether their work is safe.
- **Application:** Give honest operation status, distinguish known progress from indeterminate activity, preserve appropriate partial work, and explain the next useful action. State what cancel or pause can actually do. Keep important messages reviewable after interruption.
- **Boundary:** A spinner is not proof of server progress. Do not hide material failures, promise rollback that the backend cannot provide, or remove appropriate informed confirmation because the source argues against dialogs.
- **Review:** Simulate the relevant failure and inspect lost versus retained work, duplicate-action risk, retry behavior, and cancellation after partial completion.
- **Source:** Chapter 21, PDF 662–666, 671–684 / printed 632–636, 641–654. Network-save recovery figure PDF 678 / printed 648 visually checked; it illustrates communication, not verified implementation safety.

## Critical use of this edition

The book is particularly useful for connecting research, goals, behavior over time, and visual expression. It is opinionated and historical. Its strongest slogans must be interpreted in context rather than turned into universal gates. The chapter 6 discussion explicitly revises the authors' earlier all-design-before-coding position; use its iterative, collaborative qualifications.

Retain current platform standards as the default and require an evidenced advantage for departures. Do not import the 2014 OS galleries, phone/tablet limits, fullscreen preferences, tiny targets, old typography or numerical accessibility prescriptions. The chapter 17 square-root ratio is erroneous, and its chart language sometimes conflates correlation with causation. The chapter 18 paste shortcut contains a typo. Chapters 14 and 19 include outdated technology limitations and predictions. These were read and assessed but are excluded from normative recommendations.

Specialized 3D, embedded, kiosk, TV, automotive, and audible-interface discussions inform context questions only. They do not establish a validated implementation or safety playbook for those domains. No chapter or historical gallery was skipped; only selected figure pages received visual inspection.

## How this source changes the skill

Use these principles to connect the brief, evidence record, scenario, flow/state map, visual direction, and implementation review. A Mobbin reference needs a contextual transfer argument. A proposed screen needs neighboring states and credible recovery. An agent critic should assess coherence, evidence, cognition, access, visual craft, and implementation behavior independently before integration. It must distinguish an expert prediction from a measured user outcome.

For future evaluation, have an independent reviewer sample citations and coverage, challenge the boundary conditions, and apply the principles to a realistic iOS flow and a web flow without seeing the author's preferred design. Compare concrete defects found and fixed; do not use agreement among agents or a checklist score as proof of usability. Test high-risk assumptions with representative users and working behavior when available.
