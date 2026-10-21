# The UX Book — source synthesis

Rex Hartson and Pardha Pyla, *The UX Book: Agile UX Design for a Quality User Experience*, second edition, 2019, Morgan Kaufmann. ISBN 978-0-12-805342-3. Source: user-supplied 918-page PDF; identity and chapter coverage are recorded in [ux-book-coverage.json](ux-book-coverage.json). Citations below use **printed page / one-based PDF page**. The main text has a verified +29 PDF offset.

**Study status: complete for the extracted text of all 33 chapters.** The ledger records actual chapter ranges and selective visual checks. Full-text study does not imply exhaustive visual inspection or verification of every historical/scientific assertion. These cards are original operational syntheses, not quotations, a replacement for the book, or instructions copied from it.

In each card, **Source** describes the book's basis; **Application** and **Check** are recommendations for this skill, including adaptations for agent-assisted iOS and web work. The book supplies UX reasoning; it does not establish current Apple requirements, current accessibility thresholds, or evidence that a particular Mobbin pattern succeeds with this product's users.

## Decision principles

### UX-01 — Scale effort to uncertainty and consequences

**Trigger:** Choosing research, modeling, prototype, or review depth.
**Source:** Rigor has both completeness and fidelity dimensions; domain complexity, interaction complexity, familiarity, and delivery scope affect suitable methods (ch3, pp49–62 / PDF78–91). Methods are adapted to the design situation, and process activities overlap rather than form rigid stages (ch2, pp46–48 / PDF75–77; ch5, pp81–84 / PDF110–113).
**Application:** Identify the consequential unknowns and select the smallest set of activities capable of resolving them. Begin with a concise product statement covering audience, goal, distinguishing value, and emotional intent (ch5, pp90–92 / PDF119–121). A familiar component change can use a concise brief; a new financial or multi-role flow warrants broader investigation. Revisit research or prototypes when new evidence changes the question.
**Exception:** A short deadline does not make unresolved high-impact behavior safe to assume.
**Check:** Does each required artifact reduce a named uncertainty? Are deferred questions visible, rather than hidden behind arbitrary screenshot or interview quotas?

### UX-02 — Preserve the distinction between evidence and interpretation

**Trigger:** Turning observations, owner input, or competitor references into design claims.
**Source:** Competitive analysis identifies capabilities but does not establish usage; synthesis should preserve original meaning, context, and useful source connections (ch7, pp125–127,140–141 / PDF154–156,169–170; ch8, pp146–151 / PDF175–180).
**Application:** Label direct observation, reported experience, stakeholder constraint, reference precedent, and design hypothesis separately. Write modular notes with actor, situation, behavior, and source. Preserve contradictory evidence.
**Exception:** A useful hypothesis need not await research; it must remain a hypothesis.
**Check:** Could a reader reconstruct why a decision was made without mistaking repeated competitor UI for validated user need?

### UX-03 — Design for behavioral differences

**Trigger:** Selecting target users or resolving competing needs.
**Source:** Work roles describe responsibilities, not individual people; user classes and personas make meaningful differences explicit (ch9, pp181–187 / PDF210–216; ch14, pp303–305 / PDF332–334).
**Application:** Record goals, expertise, frequency, context, access needs, and the behavioral differences that change the design. Prefer a short evidenced role profile over invented biography.
**Exception:** A primary target guides tradeoffs; it does not justify excluding other required users or access needs.
**Check:** Name one decision affected by each profile attribute. Remove decorative attributes that do no design work.

### UX-04 — Model the journey outside the screen

**Trigger:** Designing onboarding, transactions, cross-device work, or multi-party services.
**Source:** Flow models connect roles, information, artifacts, and dependencies; ecological design considers devices and the surrounding work environment (ch9, pp187–192 / PDF216–221; ch16, pp341–348 / PDF370–377). Experience includes anticipation, use, aftermath, and cumulative effects, with service journeys extending across people and locations (ch1, pp6–7,18–23 / PDF35–36,47–52).
**Application:** Trace entry, trigger, prerequisite, user action, service response, external handoff, and real-world completion. Include support, other apps, notifications, physical artifacts, and other people when relevant.
**Exception:** A local component fix may need only the adjoining context, not a complete service map.
**Check:** Can the person finish their actual goal after leaving the last designed screen? Identify each handoff's owner and failure behavior.

### UX-05 — Specify capabilities and reasons before widgets

**Trigger:** Converting the brief or research into requirements.
**Source:** Task sequences capture intentions, triggers, barriers, and information needs; stories describe a capability, role, and benefit, including explicit extrapolations and system implications (ch9, pp197–206 / PDF226–235; ch10, pp232–250 / PDF261–279).
**Application:** State what the user must accomplish and why, then define acceptance behavior and necessary backend support. Keep owner constraints distinct from chosen solutions. Link related stories into a coherent task.
**Exception:** An existing system or explicit request can legitimately constrain the widget.
**Check:** Does the proposed control solve the underlying need, and do save, sync, permissions, or transaction guarantees actually exist?

### UX-06 — Establish a coherent conceptual model

**Trigger:** New products, navigation overhauls, or repeated user confusion.
**Source:** Conceptual design communicates the designer's model so users can form useful predictions; metaphors can help but can also mislead (ch15, pp327–340 / PDF356–369).
**Application:** Define the main objects, relationships, actions, and state meanings in user language before polishing screens. Use metaphors only while their behavior remains consistent with the product.
**Exception:** A decorative theme need not become a literal interaction metaphor.
**Check:** Ask someone to predict what an action will change and explain where information lives. A label patch is insufficient if the underlying model remains contradictory.

### UX-07 — Treat information architecture as object structure

**Trigger:** Lists, detail views, search, filters, saved items, or shared content.
**Source:** Information models describe objects, attributes, relationships, retrieval, labeling, and manipulation, beyond a navigation tree (ch9, pp214–215 / PDF243–244; ch12, pp269–270 / PDF298–299; ch14, p307 / PDF336).
**Application:** Identify canonical objects and their important attributes, then design organization, naming, search, browsing, comparison, and editing around user tasks.
**Exception:** A small feature may inherit a suitable existing model.
**Check:** Can users locate the same object through different paths without inconsistent identity, terminology, or state? Are enough attributes visible to make the decision?

### UX-08 — Preserve meaning across devices while exposing limits

**Trigger:** iPhone/iPad/web variants, synchronization, account continuity, or constrained data.
**Source:** Ecologies need coherence across devices, while interaction varies with context and capability; incomplete availability must be communicated honestly (ch16, pp343–346 / PDF372–375; ch17, pp360–365 / PDF389–394). Cross-device evaluation probes expected consequences and resumed context (ch24, pp507–508 / PDF536–537).
**Application:** Preserve object identity and task intent while adapting navigation and layout to native platform behavior. Define what syncs, when it syncs, and what remains unavailable.
**Exception:** Different device roles can justify different capabilities.
**Check:** Does an empty result actually mean no results, or only no downloaded/authorized/recent results? Can a task move between devices without unexplained loss?

### UX-09 — Explore alternatives without treating precedent as a cage

**Trigger:** New interaction concepts or a brief that prematurely specifies a solution.
**Source:** Design integrates evidence rather than mechanically translating it; bottom-up improvement and top-down reframing have different uses and risks. Generative design alternates ideation, sketches, and critique (ch12, pp261–267 / PDF290–296; ch13, pp279–291 / PDF308–320; ch14, pp295–325 / PDF324–354).
**Application:** Explore meaningfully different ways to satisfy the same goal. Use Mobbin as a source of mechanisms and tradeoffs. Label novel ideas and evaluate them rather than rejecting them for lacking precedent.
**Exception:** Do not reopen settled constraints for novelty alone.
**Check:** Do alternatives differ in task structure or decision support, rather than only color? Critique after exploration, with a stated reason for selection.

### UX-10 — Make transitions a first-class design object

**Trigger:** Any screen sequence or consequential action.
**Source:** Storyboards and wireflows include the causes and context of transitions; the interaction cycle links planning, selecting an action, acting, and interpreting outcomes (ch17, pp369–377 / PDF398–406; ch20, pp411–413 / PDF440–442; ch31, pp695–705 / PDF724–734).
**Application:** For each transition record trigger, prerequisites, action, intermediate state, outcome, feedback, next available action, and failure/recovery path. Include asynchronous events as well as taps. Distinguish acknowledgement, work in progress, and actual completion; keep action and destination terminology aligned (ch32, pp790–804 / PDF819–833).
**Exception:** Not every transition needs animation; feedback can be stable content or a state change.
**Check:** Can users know what to do, perform it, perceive the outcome, and tell whether their goal advanced? A backend success without understandable feedback is incomplete.

### UX-11 — Support interruption and re-entry

**Trigger:** Long forms, authentication detours, permission prompts, error recovery, app switching, or multi-step decisions.
**Source:** Secondary tasks force users to retain and restore primary-task context; working-memory limits make unsupported restoration fragile (ch31, pp706–707 / PDF735–736; ch32, pp713–715,719–721 / PDF742–744,748–750). Task continuity includes plausible next steps and retaining work and preferences (ch32, pp771–777 / PDF800–806).
**Application:** Preserve appropriate progress, selections, draft data, and return destination. Make pending versus completed work distinguishable; show what remains after returning. When suggesting a remedy, provide a path to perform it. Avoid unexpected focus changes or forcing repeated setup.
**Exception:** Privacy or shared-device constraints can require expiry or clearing; explain this and offer appropriate recovery.
**Check:** Interrupt at a realistic point, return, and complete the task without reconstructing everything from memory. Do not signal completion before the consequential final step.

### UX-12 — Audit all five affordance roles

**Trigger:** Reviewing a control, feedback message, or interaction mechanism.
**Source:** Cognitive, physical, sensory, functional, and emotional affordances provide distinct support and must cooperate (ch30, Table30-1, pp654–655,685–689 / PDF683–684,714–718).
**Application:** Ask whether it serves the goal, communicates its meaning, can be perceived, can be operated, and fits the desired emotional experience. Diagnose which role fails before proposing a fix.
**Exception:** Emotional appropriateness can mean quiet competence; every button does not need delight.
**Check:** A larger target does not fix an ambiguous label; a clearer label does not fix a hidden control; beautiful feedback does not fix missing functionality.

### UX-13 — Make appearance and actual behavior agree

**Trigger:** Custom controls, cards, links, gestures, inactive actions, or action labels.
**Source:** False cognitive affordances mislead users about available actions or outcomes; feedforward and feedback require meaningful communication (ch30, pp655–661 / PDF684–690).
**Application:** Match the perceived target to its hit area and the action label to its consequence. Show important prerequisites, scope, or destructive effects before commitment. Group controls to convey their true scope, expose eligibility constraints early, and reserve confirmation for consequential actions where protection outweighs interruption (ch32, pp747–748,792–794 / PDF776–777,821–823).
**Exception:** Established platform conventions can communicate some meaning implicitly; verify the intended audience recognizes them.
**Check:** Tap anywhere the visual treatment suggests is interactive. Predict the outcome from the label alone. Identify misleading decoration, unexplained disabled actions, and unsupported promises.

### UX-14 — Optimize physical interaction for real conditions

**Trigger:** Touch targets, maps, sliders, repeated actions, reach, and gesture-heavy iOS flows.
**Source:** Physical affordance depends on users and context, including dexterity, fatigue, movement distance, neighboring targets, and overshoot (ch30, pp661–672 / PDF690–701; practical table at p670 / PDF699).
**Application:** Use current platform sizing guidance, appropriate spacing, feasible reach, and alternatives for precision gestures. Support fine adjustment where a broad gesture can overshoot.
**Exception:** Bigger alone is not better when it creates accidental neighboring activation or obstructs content.
**Check:** Exercise actual hit regions under realistic hand and device conditions. Include access needs and repeated-use fatigue; do not infer touch success from a desktop screenshot.

### UX-15 — Distinguish visible, noticeable, readable, and distinguishable

**Trigger:** Status, errors, actions, dense content, or subtle aesthetic treatments.
**Source:** Sensory affordance separates visibility, noticeability, discernibility, legibility, distinguishability, and timing; similar issues apply to auditory and haptic signals (ch30, pp672–683 / PDF701–712).
**Application:** Place relevant feedback near the task's focus, use adequate contrast and type, separate confusing alternatives, and provide cues when needed. Treat sound and haptics as optional channels with visual/accessibility equivalents where required.
**Exception:** More visual salience everywhere destroys hierarchy.
**Check:** Review with relevant text size, lighting, motion, sound, and accessibility conditions. Can users tell states apart without relying on one fragile cue?

### UX-16 — Define emotional intent and express it coherently

**Trigger:** Visual direction, onboarding, trust-sensitive moments, repeated work, and product identity.
**Source:** Emotional needs extend beyond pleasure to identity, connection, pride, and long-term meaningfulness; mood boards can develop a coordinated visual, linguistic, motion, and auditory vocabulary (ch18, pp385–395 / PDF414–424). Meaningfulness requires longitudinal evidence (ch24, pp526–532 / PDF555–561). Novelty and fun can undermine concentration in demanding work (ch6, pp109–110 / PDF138–139).
**Application:** State the appropriate desired feeling and derive concrete typography, color, imagery, copy, and motion choices. Evaluate emotional intent separately from whether tasks merely complete.
**Exception:** Avoid surprise or entertainment when it disrupts concentration or gravity. A mood board is direction, not proof of user response.
**Check:** Do major states express the same intended character? Are claims about trust or enduring attachment supported by suitable user evidence?

### UX-17 — Maintain a behavioral design system

**Trigger:** Reusable components or repeated implementation by multiple agents.
**Source:** A living style guide includes terminology, layout, defaults, errors, widgets, and their states; Figure17-14 illustrates selected, indeterminate, disabled, and invalid states (ch17, pp381–383 / PDF410–412).
**Application:** Capture semantics, variants, state behavior, content rules, accessibility expectations, and tokens together. Reuse the same object and action vocabulary across flows.
**Exception:** Platform differences and different task meanings can justify documented variants. Consistency supports prediction, but distinguishing dangerous actions or preserving context can matter more than identical appearance (ch32, pp810–814 / PDF839–843).
**Check:** Are loading, empty, error, selection, disabled, and focus behaviors defined when applicable? Can implementation reuse the pattern without inventing missing interaction rules?

### UX-18 — Choose prototype fidelity by the question

**Trigger:** Selecting what to sketch, mock, build, or test next.
**Source:** Breadth, depth, and fidelity are different dimensions; prototypes can explore a whole architecture or deeply test one risky path (ch20, pp408–425 / PDF437–454).
**Application:** Name the question first, then select enough realism to answer it. Use rough flows for structure, richer visuals for perception and emotional direction, and realistic behavior for timing, gesture, or recovery questions.
**Exception:** High fidelity is useful when low fidelity would obscure the phenomenon under investigation.
**Check:** What can this prototype establish, and what is still simulated? Do not treat an attractive static mockup as evidence of successful task performance.

### UX-19 — Keep prototypes honest enough to expose failure

**Trigger:** Preparing a usability session or interactive review.
**Source:** A prototype that makes only the intended path appear available can distort results; pilot testing should reveal prototype failures before participants encounter them (ch20, p423 / PDF452; ch23, p503 / PDF532; ch24, pp534–537 / PDF563–566).
**Application:** Make plausible task choices behave plausibly, include necessary exception states, reset prior-session data, and record prototype limitations separately from design problems.
**Exception:** A deliberately narrow prototype is valid if its evaluation claims stay equally narrow.
**Check:** Try wrong turns, backtracking, corrections, and alternate successful routes. The facilitator or simulated system must not silently rescue incorrect actions.

### UX-20 — Name the evaluation and its evidence limits

**Trigger:** A review report, subagent critique, or quality claim.
**Source:** Analytic inspection predicts problems; empirical evaluation observes participants. Objective/subjective and quantitative/qualitative are separate distinctions (ch21, pp437–445 / PDF466–474; ch25, pp545–551 / PDF574–580). Evaluators can disagree and inspections can miss problems or produce false positives (ch28, pp602–606 / PDF631–635).
**Application:** Label heuristic review, scenario walkthrough, implementation verification, or participant test accurately. Independent critics can reveal different risks; agreement among AI agents does not establish real-user success.
**Exception:** Inspection is valuable when participant access is unavailable; preserve its limitations.
**Check:** Separate observed behavior, participant opinion, evaluator interpretation, and untested hypotheses. Avoid invented scores, sample sizes, and statistical confidence.

### UX-21 — Connect goals to measures without false precision

**Trigger:** Defining success, comparing alternatives, or reporting a UX score.
**Source:** UX goals, measures, instruments, and targets must align; the approach can be reduced to qualitative task observation when metrics would add little value (ch22, pp455–460,474–481 / PDF484–489,503–510).
**Application:** Specify the goal, observable outcome, audience/context, instrument, and basis for any target. Distinguish perceived ease from task success and user time from system wait.
**Exception:** Numerical targets are optional when unsupported. Keep validated questionnaire wording and scoring intact unless explicitly reporting a modified instrument.
**Check:** Would the measured result actually answer the decision? Can the claimed comparison survive differences in prototype, task, participants, or method?

### UX-22 — Test representative complete tasks

**Trigger:** Planning evaluation coverage.
**Source:** Benchmarks should reflect frequent and critical work, task combinations, recovery, user expertise, and environment; participant selection depends on the evaluation rather than a universal small-number rule (ch22, pp460–470 / PDF489–499; ch23, pp488–494 / PDF517–523). Discovery-rate models depend on assumptions about detectability, tasks, system scope, and participants that often do not hold (ch28, pp608–614 / PDF637–643; Fig28-1 and formula visually checked at PDF638–639).
**Application:** Include the primary journey, important alternative, consequential failure, and realistic interruption when relevant. Recruit the required user types; do not train first-time participants into experts before testing learnability.
**Exception:** A targeted study may isolate one issue, but cannot validate the whole flow.
**Check:** Does coverage reach beyond the easy happy path and include real-world completion? Explain what remains untested.

### UX-23 — Avoid teaching the answer in the test

**Trigger:** Writing a task script or facilitating a session.
**Source:** Task descriptions should state outcomes without UI labels or instructions that reveal the path; evaluator intervention can alter what the session measures (ch22, pp465–469 / PDF494–498; ch23, p488 / PDF517; ch24, pp535–536 / PDF564–565).
**Application:** Give a realistic goal and starting context. Keep evaluator instructions separate. Record assistance, design changes, and prompts that affect performance; distinguish unassisted completion from assisted exploration.
**Exception:** Collaborative co-design can use active discussion, clearly labeled as such.
**Check:** Could someone succeed by following the script without understanding the interface? Are task timing and conclusions valid after prompting or think-aloud interruptions?

### UX-24 — Diagnose problems before prioritizing fixes

**Trigger:** Synthesizing critique or participant observations into a backlog.
**Source:** Critical incidents capture intent, action, expectation, actual outcome, and recovery; analysis separates underlying problems, merges duplicates, and considers importance separately from fix cost (ch24, pp508–510 / PDF537–539; ch26, pp565–584 / PDF594–613).
**Application:** Record evidence, interpretation, cause hypothesis, affected users/tasks, consequence, proposed fix, and confidence. Prioritize blocking or harmful issues before low-cost polish. Keep severity distinct from effort. Reports should make the usage context and actionable consequence understandable to the recipient; preserve a problem's decision, implementation, and retest history (ch27, pp589–599 / PDF618–628; ch28, pp620–621 / PDF649–650).
**Exception:** A speculative diagnosis may require another observation instead of immediate redesign.
**Check:** Does the finding describe a problem rather than merely demand a solution? Are repeated symptoms one systemic issue? Are expensive critical defects still visible?

### UX-25 — Preserve coherence through delivery and retesting

**Trigger:** Implementation handoff, parallel agents, iteration, or release review.
**Source:** Some overarching conceptual design is needed before feature slices; UX and implementation must communicate, inspect fidelity, and revisit fixes because they can expose deeper problems (ch4, pp74–80 / PDF103–109, Fig4-3; ch12, pp276–277 / PDF305–306; ch26, pp584–587 / PDF613–616; ch29, pp638–647 / PDF667–676, including Table29-1 at PDF673).
**Application:** Give builders shared objects, terminology, flow/state contracts, and acceptance behavior. Inspect the running result, retest changed paths and relevant adjacent paths, and update the shared design record.
**Exception:** Do not impose the book's exact sprint schedule, software tools, or complete-test repetition on every minor change.
**Check:** Did implementation preserve behavior and emotional intent? Did the fix cause a regression or merely move the blockage? Keep unresolved issues and untested assumptions explicit.

## Interpretive boundaries

- Historical product screenshots and tools illustrate mechanisms; they are not current iOS or web implementation guidance.
- The book explicitly does not comprehensively cover accessibility or internationalization (ch32, p710 / PDF739). Those need dedicated, current guidance.
- Do not turn contextual numerical suggestions into universal rules: screenshot counts, participant counts, memory item limits, sprint lengths, or informal estimates of issue frequency.
- Do not adopt questionable cognitive explanations as scientific facts, including the discussion of muscle memory on p716 / PDF745. The useful operational lesson is learned interaction consistency, without that mechanism claim.
- Do not promote blanket palette, color-meaning, or physiological claims (ch32, pp818–822 / PDF847–851), the preference for pop-up feedback (p793 / PDF822), or categorical claims about anthropomorphic interfaces (pp815–818 / PDF844–847) into universal rules. Preserve context, current accessibility guidance, truthful capability, and task suitability.
- Historical accident narratives are not verified causal evidence. Do not repeat them as established facts, including the aviation examples in ch1 and ch32. Historical product behavior and organizational roles are likewise not contemporary specifications.
- The distinction between diagnostic learning and population-level inference is useful; the source's blanket restrictions on reporting informal results (ch28, pp601–602 / PDF630–631) are not adopted. Report the actual method, context, sample, limitations, and appropriate claim strength.
- Facial movement and physiological measures do not identify a person's emotion or its cause reliably by themselves (ch28, pp616–619 / PDF645–648). Do not infer trust, frustration, or intent from an image; use relevant behavior and voluntary participant reports.
- The book's broad treatment of questionnaire modification and aggregate scoring (ch24, pp520–525 / PDF549–554; ch26, p563 / PDF592) is not a scoring specification for standardized instruments. Verify the original instrument, version, licensing, validation, and scoring before using it.
- Do not adopt business-directed friction from the discussion of slanty design (ch16, pp350–352 / PDF379–381) as a license to frustrate user goals. Evaluate user impact and transparency.
- Classroom exercises, including role-play participants and requested counts of incidents, are pedagogical prompts. They do not authorize fabricated user research or mandatory discovery of a quota of problems.
- Research recruitment, recording, consent, retention, and review-board descriptions are source context, not a universal legal workflow. Use the actual study's policy and current requirements; do not contact people or collect data merely because the book describes doing so.

## Coverage and maintenance

The JSON ledger is authoritative for actual coverage and visual inspection. All 33 chapters were studied as extracted text, including the reference/background chapters; no chapter text was excluded. Front matter, bibliography, index, blank pages, and part dividers are outside chapter-study coverage. Historical passages and exercises were read but are not converted into operational requirements merely to increase coverage.

Full-study does not imply a page-by-page visual audit. The ledger records 14 selected rendered-page inspections: process funnel (PDF104), phone workflow (PDF404), component states (PDF412), emotional-input map and mood board (PDF417,419), wireflow/state progression (PDF441), discovery graph and formula (PDF638–639), affordance table (PDF683), interaction-cycle and return-context diagrams (PDF728,736), action-scope grouping comparison (PDF776–777), and departure/arrival label mismatch (PDF831). Table29-1 at PDF673 supports the delivery discussion through text study, without a separate visual check.

For future updates, re-open the cited passage and inspect additional figures when a decision depends on visual detail. Preserve stable IDs, distinguish the book's statements from skill recommendations, and record any new checks in the ledger. Keep full text, book images, and source PDFs outside the repository.
