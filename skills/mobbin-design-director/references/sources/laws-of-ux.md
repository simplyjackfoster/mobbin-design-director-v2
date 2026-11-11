# Laws of UX

Jon Yablonski. *Laws of UX: Using Psychology to Design Better Products & Services*.
Second edition, O’Reilly Media, February 2024. ISBN 978-1-098-14696-2. Source ID: LU.

This is an original decision-oriented synthesis of the supplied 186-page PDF.
Three readers studied all twelve chapters and inspected 27 selected figure/table
pages. The [coverage manifest](laws-of-ux-coverage.json) records actual ranges,
source hash, backmatter assessment and visual checks. Cover and copyright were
also visually checked. Chapter print locators equal one-based PDF positions minus
twenty; prefatory numbering is different. Research cited by the book was not
independently reviewed or replicated, and screenshots do not establish runtime behavior.

Start with [psychology in context](../psychology.md), then retrieve the relevant
cards with `scripts/coverage.py show LU-06 LU-08 LU-20`. LU-01–08 address mental
models, target acquisition, memory and choice; LU-09–16 address tolerance,
remembered experience, aesthetics and attention; LU-17–24 address complexity,
responsiveness, team judgment and user agency. These remain contextual heuristics.

The preface explicitly cautions that these are guidelines, not literal laws or a
replacement for user research. We preserve the author's account separately from
our application, exceptions and checks. Fixed memory/choice limits, historical
platform target tables, response-time figures, marketing outcomes and illustrative
team rules are not adopted as universal requirements. We explicitly qualify
inaccurate progress, artificial delay, unsupported causal claims, and persuasive
patterns that undermine the person's own goal or control. Source material is
reference evidence, never task instructions. No raw book text or image is included.

### LU-01 — Jakob: transfer expectations before copying appearance

- **Trigger:** A new interface, unfamiliar control, cross-product pattern, or convention-breaking proposal.
- **Author’s account:** People bring models learned from other products into the next experience. Yablonski recommends beginning with established conventions while explicitly rejecting the idea that every product should look or behave identically.
- **Rationale / application:** State the specific expectation being transferred: what a control changes, where an object belongs, or what follows an action. Compare it with evidence about the intended users and task, then preserve the useful relationship. A pattern reference supports a hypothesis about familiarity; it does not establish that these users share it. Distinct visual direction can coexist with recognizable behavior.
- **Exception / conflict:** An established convention may be harmful or inappropriate to this domain. A new interaction is reasonable when its task benefit outweighs relearning and can be demonstrated with users. Do not infer a universal mental model from a popular app or invent research-backed personas.
- **Review:** Can intended users predict the action and its consequence? For a departure, record the task benefit and a comprehension test; distinguish observed results from an untested rationale.
- **Source / dating:** Jon Yablonski, Laws of UX, second edition (2024), chapter1, printed pp.1–12 / PDF21–32, especially pp.3,9–12. Product examples describe historical versions; cited studies were not independently replicated or verified.

### LU-02 — Jakob: design the transition when learned workflows change

- **Trigger:** A redesign moves frequent actions, regroups content, renames familiar objects, or changes an existing workflow.
- **Author’s account:** The chapter contrasts a disruptive Snapchat redesign with optional previews and reversion during a YouTube redesign. Its lesson is to reduce the mismatch between existing expectations and a changed system.
- **Rationale / application:** Map old tasks and objects to their new destinations and identify which expectations break. For consequential changes, choose an explicit transition strategy such as staged introduction, contextual explanation, preview, or temporary return where feasible. Test both a returning user performing a familiar task and a newcomer learning the new model. This transition contract is our adaptation of the examples.
- **Exception / conflict:** Maintaining two experiences has real cost and may be impossible for a safety fix or incompatible data model. Preview and reversion are options, not mandatory release gates. Historical business outcomes in the chapter do not prove a single design change caused them.
- **Review:** Can returning users find and complete their established task with preserved data and understandable changes? If a fallback is offered, verify its actual availability and state continuity; otherwise describe the transition honestly.
- **Source / dating:** Yablonski (2024), chapter1, printed pp.4–5,11–12 / PDF24–25,31–32. Snapchat2018 and YouTube2017 are illustrative accounts, not controlled comparisons or current feature claims.

### LU-03 — Fitts: evaluate acquisition paths and effective targets

- **Trigger:** Frequent pointing or touch actions are slow, imprecise, or located far from the work they complete.
- **Author’s account:** The chapter connects target acquisition to movement distance and target size, then discusses label activation, nearby form submission, and cursor boundaries at desktop screen edges.
- **Rationale / application:** Inspect the whole sequence: current focus or pointer location, intended target, effective activation region, nearby alternatives, and feedback. Associate labels with their controls and keep completion actions meaningfully related to their task. Verify activation at target boundaries and with keyboard or assistive input where supported. Compare total task performance, not merely button dimensions.
- **Exception / conflict:** The historical pointing model is not an end-to-end usability formula. A screenshot cannot establish the hit region. Desktop cursor-edge benefits depend on actual pointer boundaries and do not transfer automatically to touch, multi-display layouts, or embedded windows. Do not enlarge or move a control at the expense of meaning, safety, or readable content.
- **Review:** Does the visible control match the actual interactive area, and can each supported input method acquire it without activating a neighboring action? Record geometry in its real units and test the task sequence.
- **Source / dating:** Yablonski (2024), chapter2, printed pp.15–24 / PDF35–44, especially label and submission examples pp.20–21. The1954 model and2023 platform screenshots are historical evidence; use the skill’s touch/platform guidance for adopted requirements.

### LU-04 — Fitts: investigate conditions behind target errors

- **Trigger:** Adjacent opposing actions, reach complaints, repeated misselection, or a design justified by one ideal grip.
- **Author’s account:** The chapter uses human-factors history, neighboring accept/deny controls, changing phone grips, and contextual inquiry to show why errors should be examined in the circumstances of use rather than attributed to careless people.
- **Rationale / application:** Inspect which near miss occurs and its consequence, the hand or input available, device position, distraction, and obscured feedback. Separate incompatible actions or add proportionate recovery. Observe representative work when research access exists, ask about unusual variations and external aids, and let participants correct the interpretation. Without observation, label environmental assumptions explicitly.
- **Exception / conflict:** One center-accuracy illustration, one grip, or an author anecdote cannot certify comfort or predict this product’s error rate. The chapter’s minimum-size table combines distinct units and contexts; do not copy its WCAG row as a universal requirement. Follow the adopted current standard and platform guidance, then test actual conditions. Never stage distracting field research in unsafe conditions.
- **Review:** Which errors remain possible in the relevant use context, what happens after each, and what evidence supports the assumed grip, reach, or attention conditions? Distinguish simulator inspection from real-device or participant evidence.
- **Source / dating:** Yablonski (2024), chapter2, printed pp.17–26 / PDF37–46. Table2-1 on p.18 and center-accuracy illustration on p.20 are contextual historical material, not a current conformance checklist.

### LU-05 — Miller: make chunks meaningful to the task

- **Trigger:** Dense text, toolbars, product lists, or mixed controls are difficult to scan or interpret.
- **Author’s account:** Yablonski emphasizes chunking as the useful design lesson: group related material and express hierarchy so people can locate and understand it. His examples include formatted numbers, article hierarchy, product attributes and toolbar groups.
- **Rationale / application:** Group items by a relationship the reader can explain, using headings, proximity, alignment and appropriate separation. Check whether a heading predicts its contents and whether product attributes stay associated with the right product. Keep comparisons visible when splitting them would create recall work. Formatting a familiar identifier may help reading, but preserve its exact value and allow ordinary paste/edit behavior.
- **Exception / conflict:** A decorative card is not automatically a meaningful chunk. Expertise, content familiarity, language and task affect what forms a useful unit. Do not force every group to the same size or substitute a numeric quota for information architecture.
- **Review:** Can people locate the relevant group, understand the relationship, and compare what the task requires without repeatedly reconstructing context? Inspect real content and long labels, not only tidy placeholders.
- **Source / dating:** Yablonski (2024), chapter3, printed pp.29–37 / PDF49–57, especially chunking pp.32–36. The computational memory-buffer illustration is explanatory metaphor, not an implementation model of cognition.

### LU-06 — Miller: distinguish visible choice from memory demand

- **Trigger:** Someone proposes a seven-item navigation limit, fixed chunk quota, or redesign based on a claimed memory capacity.
- **Author’s account:** Although the chapter opens with the familiar7±2 formulation, its explanation explicitly rejects using it to cap visible navigation. It describes variability and competing later accounts of memory capacity, and shows a grouped menu with more than seven links.
- **Rationale / application:** Identify precisely what must be remembered, for how long, and across which interruption or screen change. Keep needed selections, constraints or comparison data accessible. Judge a visible menu by its labels, grouping, findability and task success rather than a recall experiment’s item count. Search and filtering may suit a known target; grouping may suit exploration.
- **Exception / conflict:** Do not replace seven with four or another universal quota. A large visible menu can still fail through poor information scent, crowded targets or excess search effort; visibility alone does not guarantee usability. Reducing choices requires a task-specific reason.
- **Review:** Is the claimed burden recall, search, interpretation or comparison? What information disappears, and does the proposed change reduce that burden without hiding useful options?
- **Source / dating:** Yablonski (2024), chapter3, printed pp.29–31,36–37 / PDF49–51,56–57. Chapter references Miller1956 and later research; those papers were not independently reviewed for this source integration.

### LU-07 — Hick: reduce decision effort for the actual choice

- **Trigger:** A choice-heavy flow is slow, a team wants to remove options, or onboarding exposes many possibilities at once.
- **Author’s account:** Yablonski connects choice-response research with minimizing unnecessary decisions, presenting options when useful, and scaffolding initial learning. The chapter also describes card sorting to understand how people organize topics.
- **Rationale / application:** First identify the decision: known-item retrieval, comparison, exploration, or rapid response. Remove irrelevant alternatives, improve labels and grouping, or disclose later decisions when their prerequisites exist. Keep needed comparison information and legitimate alternatives reachable. If recommending an option, explain its basis and preserve meaningful control. Evaluate completion quality and errors as well as time.
- **Exception / conflict:** The historical stimulus-response formula does not predict an arbitrary purchase, search or expert workflow. More steps can add navigation and memory costs; fewer visible choices can conceal the right answer. The book’s jam-study and streaming examples are accounts, not a universal conversion guarantee. Do not invent measured time savings.
- **Review:** Can users find or choose the option that fits their goal, understand relevant differences, and change direction? Explain how the chosen grouping/disclosure reduces this task’s burden rather than merely lowering the option count.
- **Source / dating:** Yablonski (2024), chapter4, printed pp.39–47 / PDF59–67. The1952 model and product examples are contextual; task-type distinctions, outcome checks and noncoercive recommendation contract are this skill’s operational adaptation.

### LU-08 — Hick: keep the cues that make simplicity understandable

- **Trigger:** A cleaner-looking proposal removes labels, replaces actions with icons, hides controls, or collapses categories into vague terms.
- **Author’s account:** The chapter warns that oversimplification can increase mental effort by removing cues about available actions and destinations. It highlights variable icon meanings and the value of accompanying labels.
- **Rationale / application:** Check what interpretive work each removed cue performed. Retain enough language, state and context to distinguish actions and consequences; use text alongside unfamiliar or consequential icons where it helps. A smaller control set may transfer complexity elsewhere, so inspect the complete path and return behavior. Card sorting can explore grouping expectations; task-based findability checks are a separate adaptation.
- **Exception / conflict:** More text is not always better: familiar compact controls may work when meaning and accessibility remain clear. Do not prescribe labels for every decorative mark or preserve redundant explanation indefinitely. The chapter’s adjacent app screenshots are examples, not a controlled labeled/unlabeled experiment.
- **Review:** Can a person identify the intended action and likely destination before activating it? Where did the removed complexity go, and can the full task still be completed without guessing?
- **Source / dating:** Yablonski (2024), chapter4, printed pp.42–50 / PDF62–70, especially oversimplification pp.48–50. Figure4-8 on p.49 already includes icon labels; it must not be described as an unlabeled before-state.

### LU-09 — Apply Postel’s law through explicit input boundaries

- **Trigger:** A form rejects culturally valid names, addresses or harmless formatting, or automation converts ambiguous human input into a consequential value.
- **Author’s account:** The chapter adapts the network robustness principle to human–computer interaction: request necessary information, tolerate variable human input, translate it into structured output and provide clear feedback. Names and address formats expose the limits of assuming one culture’s conventions. Focused, nonleading interviews help uncover actual contexts instead of assuming them.
- **Rationale / application:** Define each field’s meaning, acceptable variation, safe normalization and ambiguity boundary. Accept harmless formatting where meaning is retained; preserve the original value or make material transformations inspectable and correctable. Ask for disambiguation before committing competing interpretations. Interview prompts should ask about a recent real task and constraint, not ask people to endorse the proposed form.
- **Exception / conflict:** Tolerance is not permission to guess identity, dates, destinations or amounts, weaken required validation, or accept malformed data at a security boundary. Author’s network analogy is not a parser-security prescription. Avoid redundant research for an approved routine correction.
- **Review:** Can representative valid variants be entered and recovered after error, while ambiguous input receives a clear resolution path rather than a silent guess?
- **Source / dating:** Yablonski, Laws of UX, 2nd ed., 2024, ch.5, printed53–56,60–63 (PDF73–76,80–83). Explicit normalization and ambiguity contracts are this skill’s adaptation, extending AF-14.

### LU-10 — Preserve a usable baseline when capabilities or content change

- **Trigger:** Voice, biometrics, responsive layout or other enhancement is introduced, or the design assumes one locale, text size, device or connection.
- **Author’s account:** Postel’s law is illustrated through responsive design and progressive enhancement: add supported capabilities while retaining access to core content and functionality. The chapter also considers translated-text expansion, writing direction and user-selected font sizes as design-resiliency cases.
- **Rationale / application:** Specify the essential action without the enhancement, then exercise enhanced, unavailable, denied and failed states. Test realistic long translations, supported direction changes and enlarged text; keep essential controls reachable through reflow or a discoverable alternative. A voice shortcut must not become the only usable way to search.
- **Exception / conflict:** A feature can legitimately require a capability; explain that dependency and a viable alternative where one exists. The book’s Amazon example removes lower-priority links as text grows; this does not justify losing essential actions. Its text-expansion ratio is an illustration, not a universal layout multiplier. Do not claim a baseline works for everyone without evidence.
- **Review:** With the optional capability absent and content expanded, can the intended user still find, complete and recover the essential task?
- **Source / dating:** Yablonski, 2024, ch.5, printed56–63 (PDF76–83), figures5-3,5-5,5-6 visually checked at PDF79,82. Examples describe historical implementations; current platform behavior requires separate verification.

### LU-11 — Use the peak–end rule to locate evidenced journey risks

- **Trigger:** A team wants to improve remembered experience, add delight, or prioritize emotionally intense moments in a journey.
- **Author’s account:** The chapter describes studies in which intense and final moments disproportionately influenced retrospective evaluation, then uses journey mapping to locate possible opportunities. Its map combines a person and scenario, expectations, actions, thoughts and emotions, opportunities, metrics and ownership; real-user research should ground the map.
- **Rationale / application:** Separate in-the-moment difficulty from later recollection. Link an asserted emotional peak to participant evidence or label it a hypothesis; do not infer an emotional curve from screen styling. Record the person’s goal, actual service stages, pain point, proposed improvement, responsible owner and evidence needed. When research is authorized, examine observed task outcomes and retrospective accounts as distinct measures.
- **Exception / conflict:** The laboratory and medical studies summarized in the book do not prove a fixed averaging formula for every digital journey. A beautiful ending cannot establish that earlier difficulty was harmless, and an invented persona or emotional curve is not participant evidence. Use a compact annotation when a full map adds no decision value.
- **Review:** Which evidenced or explicitly hypothesized moment is being improved, what outcome should change, and how will that be distinguished from a favorable retrospective rating?
- **Source / dating:** Yablonski, 2024, ch.6, printed65–73,76 (PDF85–93,96); figure6-5 inspected at PDF92. Cited primary studies were not independently reviewed; evidence distinctions are operational adaptations.

### LU-12 — Repair negative peaks and make endings truthful

- **Trigger:** Waiting, validation, failure or completion is being dressed with animation, celebration, humor or a reassuring message.
- **Author’s account:** Examples connect avoidable friction, understandable wait status, achievements and recovery tone to remembered experience. The chapter cautions that humor can worsen an already negative event and that its appropriateness depends on context.
- **Rationale / application:** Resolve the source of difficulty before decorating it: surface necessary constraints at a useful moment, explain a delay, preserve work and offer recovery. At the ending, state what actually completed, what remains pending, the next step and available correction. Celebration should follow a real meaningful accomplishment and suit the task; maintain important receipts or follow-up instructions.
- **Exception / conflict:** Do not deliberately prolong work, manufacture an emotional peak, conceal service failure or celebrate an unconfirmed outcome to improve recall. The password example illustrates visible constraint feedback, not an endorsement of its historical password policy. Humor and gamification are optional expressive choices, not remedies for loss or distress.
- **Review:** Can the person tell success from pending or failed work, recover without unnecessary repetition, and finish with the needed outcome and next step clearly available?
- **Source / dating:** Yablonski, 2024, ch.6, printed69–76 (PDF89–96), figure6-6 inspected at PDF94. Honest completion and avoidance of manufactured delay are this skill’s adaptations; historical brand examples are not measured evidence for the current product.

### LU-13 — Treat aesthetic–usability as a perception effect to investigate

- **Trigger:** A polished option is assumed to be easier, trustworthy or more successful because it looks appealing or receives enthusiastic feedback.
- **Author’s account:** The chapter distinguishes apparent usability from inherent ease of use and describes studies relating visual attractiveness to perceived usability. It also reports a phone-simulation study that found differences in task time; aesthetics can affect experience, but the examples do not establish one universal style.
- **Rationale / application:** Preserve deliberate visual craft while separating attractiveness, perceived ease, perceived trust, observed task success and error recovery. Evaluate matched alternatives using the same task, content and starting state; state which aesthetic variables changed. Use a positive visual response as useful evidence about appeal, then investigate the relevant behavioral claim separately.
- **Exception / conflict:** Do not conclude that attractive products are objectively safe or usable, that disliked styling causes every task failure, or that all interfaces should imitate the book’s Braun/Apple examples. The reported rapid first-impression timing is not a current acceptance threshold, and correlation of ratings is not proof that ornament improves completion.
- **Review:** Which claim is supported by appeal ratings, which by observed behavior, and which remains a hypothesis after the comparison?
- **Source / dating:** Yablonski, 2024, ch.7, printed79–86,90–91 (PDF99–106,110–111); figures7-2 and7-6 inspected at PDF102,110. Studies and historical examples are reported through the book, not independently replicated.

### LU-14 — Look past praise when testing a polished interface

- **Trigger:** Participants call a design beautiful or easy while hesitating, misinterpreting, failing or needing assistance; visual polish may dominate a usability review.
- **Author’s account:** The chapter warns that aesthetically pleasing design can make people more tolerant of usability issues. Its testing technique calls for representative participants, realistic neutral tasks, observing performance as well as statements, and synthesizing observations before jumping to solutions or premature themes.
- **Rationale / application:** Capture what happened alongside what was said: completion, misunderstanding, error, assistance, recovery and relevant time observations. Follow up neutrally on a specific action without asking the participant to criticize the styling. Separate an observation from its inferred cause, keep counterexamples visible, and use the discrepancy between praise and difficulty to guide the next design iteration.
- **Exception / conflict:** Neither praise nor a single hesitation should be discarded to fit a theory. Think-aloud, observation and task wording can influence behavior; record these conditions. Agent inspection and scripted checks cannot become participant findings, and testing does not authorize recruitment or external contact without the user’s request.
- **Review:** Does the report retain material task failures even when satisfaction is high, and connect each proposed fix to observed evidence or an explicitly labeled inference?
- **Source / dating:** Yablonski, 2024, ch.7, printed87–91 (PDF107–111), including usability-testing and synthesis sections. This focused guard against aesthetic masking supplements the existing review method rather than replacing it.

### LU-15 — Use von Restorff distinctiveness in service of the user’s decision

- **Trigger:** A call to action, warning, recommended plan or notification needs emphasis, or many elements compete for attention.
- **Author’s account:** The chapter relates distinctive items to memory and visual attention, then explains that selective attention, banner blindness and change blindness can defeat simple attempts to make content noticeable. Distinction can use position, scale, shape, space, color or motion; excessive emphasis dilutes it.
- **Rationale / application:** Identify the decision and the information the person must notice, then reserve meaningful contrast for that purpose. Keep the reason for emphasis legible and preserve competing legitimate choices and qualifications. Check the emphasized item in its surrounding task context, including whether ad-like treatment or placement makes it easier to ignore.
- **Exception / conflict:** A memorable or clicked element is not necessarily understood, appropriate or beneficial. Do not hide cheaper plans, manufacture popularity or urgency, or turn destructive action into the visually preferred choice merely because it is important. The book’s red Delete example illustrates differentiation; it is not evidence that that treatment prevents accidental deletion in the current flow.
- **Review:** Can the person identify the relevant action and its consequences while still seeing legitimate alternatives, and does the emphasis clarify a user need rather than bias an uninformed choice?
- **Source / dating:** Yablonski, 2024, ch.8, printed93–100,104 (PDF113–120,124), figures8-1,8-3,8-4 inspected at PDF117,119. Benefit and noncoercion checks are operational qualifications to the historical examples.

### LU-16 — Verify attention cues without equating gaze with understanding

- **Trigger:** Color or animation carries critical status, an important change is missed, or eye-tracking output is offered as proof of comprehension or emotion.
- **Author’s account:** The chapter asks for noncolor cues, sufficient contrast, moderation and care for motion sensitivity. Its eye-tracking technique starts with a research question and representative participants, describes calibration and analysis, and recommends complementary methods because gaze studies have contextual and technical limits.
- **Rationale / application:** Pair critical visual distinction with meaningful labels or suitable shape/position cues; retain meaning with reduced motion and supported assistive interaction. Verify relevant current platform requirements through the skill’s platform paths. If gaze data exists, define what was measured, under which task and conditions, and combine it with task behavior and participant explanation before inferring why attention went there.
- **Exception / conflict:** A fixation, heatmap or glance does not by itself establish understanding, preference, emotion, consent or task success. An agent’s visual scan is not eye tracking. Do not require expensive gaze research when a simpler observation answers the question, or remove all useful emphasis in the name of restraint.
- **Review:** Does the cue retain its meaning under the relevant accessibility conditions, and are claims about attention, comprehension and emotion limited to the evidence actually collected?
- **Source / dating:** Yablonski, 2024, ch.8, printed95–96,100–104 (PDF115–116,120–124). Gaze-to-meaning limits are explicit operational safeguards; historical accessibility figures are not a substitute for current requirements.

### LU-17 — Tesler’s law: assign complexity without hiding consequential choices

- **Trigger:** People repeatedly enter known information, reconstruct system state, or perform work the product can reliably do.
- **Author’s account:** Yablonski uses Tesler’s conservation-of-complexity framing to ask who bears the necessary work, illustrating prefilled sender details, address reuse, assisted composition and intent-based interfaces.
- **Rationale / application:** List the information and decisions the task actually requires, remove accidental work, and assign remaining work to the party best able to handle it. Reuse reliable known values while exposing their source and a correction path. For inferred or generated results, keep consequential assumptions and the eventual commitment inspectable; reduced typing does not remove the need to understand what will happen.
- **Exception / conflict:** Conservation is a design heuristic, not a measured quantity or proof that complexity cannot be eliminated by changing the process. Automation can add verification and recovery work. Historical AI/retail examples do not establish present capability or reliability; do not assume a natural-language interface makes expertise unnecessary.
- **Review:** Can a person see and correct a wrong reused or inferred value before commitment, and does the complete task require less work including recovery?
- **Source / dating:** Ch. 9, printed107–114,117 / PDF127–134,137; second edition2024. Implementation safeguards are our adaptation; cited product examples date mainly to2023.

### LU-18 — Preserve discoverability when disclosing complexity progressively

- **Trigger:** A simplified interface hides advanced functions, setup, context, or explanation until later.
- **Author’s account:** Chapter9 connects progressive disclosure with the active-user paradox: people often begin their immediate task before studying how the system works, so useful guidance belongs within the experience.
- **Rationale / application:** Defer less relevant detail behind a recognizable route while retaining information required to choose or understand consequences. Place guidance at the actual point of uncertainty, including alternate entry paths; preserve expert access. Test an initial visit, a return visit and a deep link rather than assuming everyone completed onboarding.
- **Exception / conflict:** People sometimes do read documentation; the author’s absolute wording is not a universal trait. Hiding choices can move effort into search or recall. The illustrated hover menu is a historical example, not a complete keyboard, touch or assistive-technology specification.
- **Review:** Without a prior tutorial, can the intended person find the needed advanced control and understand its consequence, including from an alternate entry and supported input method?
- **Source / dating:** Ch.9, printed115–116 / PDF135–136; second edition2024. Entry-path and input-method checks are operational adaptations.

### LU-19 — Doherty threshold: measure response stages in the actual task

- **Trigger:** An interaction feels unresponsive or a team proposes a universal400ms performance target.
- **Author’s account:** Yablonski presents the historical Doherty response-time argument and describes prompt feedback, stable loading placeholders and progressive image loading as ways to sustain task continuity.
- **Rationale / application:** Distinguish input acknowledgment, useful content, usable controls and durable completion. Set budgets for those stages using the actual task, supported devices and network conditions; measure them separately. Reserve stable layout space where it helps and optimize the real bottleneck as well as the visible wait.
- **Exception / conflict:** The book’s400ms,100ms and10-second examples are contextual historical guidance, not universal acceptance thresholds or proof of productivity gains. A fast acknowledgment does not establish completed work. Skeletons can mislead if they imply unavailable content, and animation must respect applicable motion/accessibility needs.
- **Review:** Under representative slow conditions, when is input acknowledged, useful work available and the outcome committed; does feedback preserve context without misrepresenting completion?
- **Source / dating:** Ch.10, printed119–126 / PDF139–146; second edition2024, referring to older response-time research and2023 examples. Stage-specific measurement is our adaptation; cited research was not independently replicated.

### LU-20 — Keep perceived progress and optimistic updates truthful

- **Trigger:** Loading, background saves, optimistic updates, or a proposed artificial wait are used to make a process seem faster or more trustworthy.
- **Author’s account:** Chapter10 discusses progress bars, estimated duration, optimistic comments and added delay. It argues that perceived performance can change the experience of waiting, and also recommends deliberate friction in some situations.
- **Rationale / application:** Show pending, confirmed and failed states distinctly. Use determinate progress only when backed by real work, label estimates as estimates, and use indeterminate status otherwise. For optimistic actions, define rollback or correction, preserve input and prevent duplicate submission on retry. If deliberation is valuable, expose the consequence and a real review opportunity instead of staging fictitious processing.
- **Exception / conflict:** This adaptation deliberately limits the book’s favorable statements about inaccurate progress and artificial delay. Do not fabricate work, completion or precision to manufacture trust. Optimism is unsuitable where a false success indication could cause serious loss or irreversible action; a persistent confirmation can make a fast result understandable without delaying it.
- **Review:** Do slow, failed, canceled and retried requests show the actual state, with a workable correction path and no fabricated progress or hidden extra commitment?
- **Source / dating:** Ch.10, printed123–129 / PDF143–149; second edition2024. Truthful feedback and risk-based optimism are explicit skill adaptations, not claims that the author imposed these restrictions.

### LU-21 — Turn psychological explanations into revisable product decisions

- **Trigger:** A team invokes a named UX law to justify a design rule, or proposes a fixed choice/character limit.
- **Author’s account:** Yablonski connects an explicit team value to a relevant psychological observation and then a concrete product rule. Useful principles resolve real questions, take a stance and remain memorable; the chapter’s three-choice and80-character rules are illustrative examples.
- **Rationale / application:** Record the user goal, observed problem or assumption, proposed mechanism, competing cost, scoped rule and the check that could overturn it. Keep the explanation close to the decision so a reviewer can distinguish product policy, a research finding and an untested heuristic. Prefer a conditional rule tied to real content over a catchy number.
- **Exception / conflict:** A named law is not evidence that this design will work for this audience, and matching a law does not validate a team’s chosen limit. The illustrative numbers are not source-derived standards. Routine approved changes do not require a principles workshop or a new document.
- **Review:** Can the team name a real decision the principle changes, its scope and tradeoff, and the observation that would make it revise the rule?
- **Source / dating:** Ch.11, printed133–138 / PDF153–158; second edition2024. Hypothesis, falsification and record format are our operational adaptation of the goal–observation–rule framework.

### LU-22 — Build shared design judgment through concrete cases and feedback

- **Trigger:** Reviewers repeatedly disagree about what good means, or design decisions bottleneck on one gatekeeper.
- **Author’s account:** Chapter11 proposes visible principles, recurring knowledge sharing and collaborative definition of team priorities. It describes aligning success criteria, generating and grouping ideas, refining principles, and circulating them to support consistent decisions.
- **Rationale / application:** Use a few representative decisions and contrasting cases to explain what the team prioritizes and where exceptions apply. Include affected disciplines, keep the resulting guidance accessible beside existing project decisions, and revise it after observed failures. When useful, share a brief case that connects a decision to its actual result rather than adding more slogans.
- **Exception / conflict:** Workshop agreement and dot voting express team preference, not participant evidence or scientific validation. Do not let consistency preserve a harmful pattern, replace research or create an approval gate for every reversible change. Adopt only as much process as recurring coordination problems justify.
- **Review:** Can two reviewers use the guidance to explain the same consequential tradeoff, while still recording disagreement and evidence that warrants an exception?
- **Source / dating:** Ch.11, printed131–136,138 / PDF151–156,158; second edition2024. Case-based calibration and lightweight documentation are our adaptations.

### LU-23 — Judge engagement mechanisms against the person’s goal and control

- **Trigger:** A design uses defaults, notifications, autoplay, endless feeds, personalization, social pressure or rewards to increase engagement.
- **Author’s account:** Chapter12 examines how persuasive mechanisms can shape behavior and argues that business engagement measures can diverge from people’s objectives. It calls for accountability for intended and unintended effects.
- **Rationale / application:** State the person’s desired outcome and who benefits from each behavioral nudge. Inspect whether defaults are understandable and changeable, stopping and declining are practical, and the UI accurately represents optional permissions or purchases. Keep useful convenience while preserving a deliberate route to pause, leave or choose differently; measure completion or value alongside engagement.
- **Exception / conflict:** Do not infer addiction, neurological effects or intent from a screenshot, nor treat old platform examples or reported usage counts as present facts. The presence of a reward or feed alone does not establish harm; examine its actual function, context, and user evidence. Increased time spent is not automatically success.
- **Review:** Can a person understand and decline the nudge, finish and leave, change the default, or stop the loop without losing unrelated functionality?
- **Source / dating:** Ch.12, printed139–152 / PDF159–172; second edition2024. Named services illustrate the author’s2023-era critique; causal and clinical claims are not adopted as design diagnoses.

### LU-24 — Test consequential nonideal scenarios and retain useful friction

- **Trigger:** A proposal removes all friction or optimizes a happy-path metric while consequential effects on other people or situations remain unclear.
- **Author’s account:** Chapter12 recommends looking beyond idealized scenarios, broadening experience represented in the design process, combining quantitative and qualitative evidence, and retaining friction where it protects deliberation or prevents unwanted consequences.
- **Rationale / application:** Identify plausible high-consequence situations relevant to the change, such as mistaken sharing, unwanted exposure, coercive use, or an accidental commitment. Include affected perspectives when available and mark missing evidence. Use a clear consequence preview, correction route or proportionate confirmation where it helps the person decide; investigate whether metric gains conceal confusion, regret or exclusion.
- **Exception / conflict:** This is targeted review, not a demand for every conceivable edge case or an automatic approval step. Extra friction can itself exclude people or obstruct cancellation. The book’s broad mental-health claims are not a basis for diagnosing users or asserting causal effects in this product; actual research is required for such claims.
- **Review:** For each relevant consequential scenario, does the design preserve understanding and a feasible escape or correction path, and is retained friction proportionate to the consequence?
- **Source / dating:** Ch.12, printed150–154 / PDF170–174; second edition2024. Scenario selection and proportionality are our operational adaptation.

