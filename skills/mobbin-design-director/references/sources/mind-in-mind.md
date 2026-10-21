# Designing with the Mind in Mind — source dossier

Jeff Johnson. *Designing with the Mind in Mind: Simple Guide to Understanding User Interface Design Guidelines*. Second edition, Morgan Kaufmann / Elsevier, 2014. ISBN 978-0-12-407914-4. The supplied PDF has 236 pages. Its identity, chapter coverage, checksum, and visual checks are recorded in [the coverage ledger](mind-in-mind-coverage.json).

All 14 chapter bodies were read in bounded page batches, including rereading truncated output. The epilogue and appendix were also read. Selected illustrations supporting retained principles were visually inspected; the ledger distinguishes those from text/caption study. This is a synthesis in original language, not a reproduction of the book or a claim to have checked every cited experiment.

PDF citations below are **one-based file pages**; printed pages are supplied separately because omitted blank pages make a single offset unreliable. “Application” and “Review” are this skill's operational adaptations, including the iOS examples. They are not claims that the 2014 book specifies current Apple behavior. Use current platform and accessibility sources for normative requirements and measurements.

## Principles

### JJ-01 — Design for the task the person expects to perform

- **Trigger:** Navigation, a first-use screen, a changing interface, or a potentially ambiguous control.
- **Rationale:** People interpret what they see through their goal, experience, and nearby context. A technically visible control can still be misunderstood or overlooked.
- **Application:** State the current task in the flow brief. Keep the meaning and placement of recurring actions stable; make unexpected state changes explicit. Use task language when comparing Mobbin references.
- **Boundary:** Familiarity varies by audience. Consistency does not justify preserving an established error or misleading label. Repeated confirmations can become habitual rather than protective.
- **Review:** Explain what a first-time and returning user could reasonably expect here, then identify evidence and assumptions separately.
- **Source:** Chapter 1, PDF 11–22, printed 1–12; especially PDF 19–22, printed 9–12.

### JJ-02 — Make visual groups match functional relationships

- **Trigger:** Forms, grouped controls, lists, dashboards, or a screen with several competing regions.
- **Rationale:** Proximity, similarity, continuity, enclosure, and shared movement imply relationships before someone reads the copy. Accidental groups can contradict the intended interaction.
- **Application:** Use spacing and alignment to associate labels, values, and actions; add enclosure when it clarifies hierarchy. Check whether repeated visual styling implies a shared behavior that really exists.
- **Boundary:** No universal ban on borders or nested containers follows from Gestalt principles. Strong grouping can also hide meaningful differences.
- **Review:** Inspect the screen without reading every word. Mark unintended rows, columns, or action groups. Check the same relationships after text enlargement and wrapping.
- **Source:** Chapter 2, PDF 23–37, printed 13–27. Figures 2.3–2.4 on PDF 25 / printed 15 were visually checked.

### JJ-03 — Structure information around the comparison or decision

- **Trigger:** Summaries, account details, results, prices, or long blocks of instructions.
- **Rationale:** Structured information reduces the work of locating related values; repeated decoration and words add noise. Position must not associate a value with the wrong label.
- **Application:** Establish a clear heading hierarchy, align comparable values, remove repeated boilerplate, and present numbers in readable groups. Preserve meaningful differences and necessary context.
- **Boundary:** Visual chunking is not a reason to fragment a text field or impose one culturally specific number/date format. Input flexibility and assistive reading order still matter.
- **Review:** Ask the intended comparison question using the actual content. Check whether it can be answered without guessing label/value relationships or calculating hidden totals.
- **Source:** Chapter 3, PDF 38–45, printed 29–36. Figures 3.4–3.5 on PDF 40 / printed 31 were visually checked.

### JJ-04 — Give important color meanings another perceivable cue

- **Trigger:** Validation, status, selection, charts, or color-coded categories.
- **Rationale:** Color discrimination changes with the observer, saturation, size, separation, background, display, and environment. A tiny colored mark is weak evidence of a distinct state.
- **Application:** Pair important color with a label, icon, shape, position, or pattern. Make state distinctions survive bright light, low contrast, and reduced color discrimination. Use measured current contrast requirements where applicable.
- **Boundary:** A grayscale or color-vision simulation is a diagnostic aid, not proof of accessibility. Avoid inferring universal cultural meanings or accessibility from color names.
- **Review:** Identify every fact conveyed only by color and supply an equivalent cue. Test actual content and state combinations, not just palette swatches.
- **Source:** Chapter 4, PDF 46–56, printed 37–47; especially PDF 49–56, printed 40–47. Figures 4.4–4.6 on PDF 50 / printed 41 were visually checked.

### JJ-05 — Put feedback where attention is likely to be

- **Trigger:** Form errors, success messages, warnings, asynchronous results, or a small change elsewhere on screen.
- **Rationale:** Peripheral vision does not provide detailed reading of the whole screen. A message can be nearby and still blend into its surroundings or appear outside the user's attention.
- **Application:** Connect feedback to the triggering control and affected content. On iOS, consider the keyboard, sheet, focused field, and visible viewport; specify an accessible announcement when needed. Reserve interruption for consequences that require it.
- **Boundary:** Do not prescribe blinking, shaking, sound, or a modal for every error. Repetition causes habituation; animation may distract or cause discomfort. Current platform semantics govern implementation.
- **Review:** Reproduce the action while attending to its target. Confirm that status and recovery are noticeable without requiring a scan of unrelated regions.
- **Source:** Chapter 5, PDF 57–74, printed 49–66; especially PDF 62–69, printed 54–61. Figures 5.6–5.7 on PDF 64 / printed 56 were visually checked.

### JJ-06 — Reduce reading work without removing meaning

- **Trigger:** Onboarding, help, error text, empty states, settings, or dense content.
- **Rationale:** Reading proficiency and language familiarity differ. Poor typography, repetition, unfamiliar wording, and avoidable instructions consume attention needed for the task.
- **Application:** Prefer recognizable task words, informative headings, concise sentences, readable text, and a stable reading order. Simplify the interaction before adding a paragraph explaining it. Keep essential instructions available at the point of use.
- **Boundary:** Brevity does not justify ambiguous labels, cryptic icons, missing consequences, or inaccessible tiny text. Do not adopt the discredited whole-word-outline account of reading discussed in the book.
- **Review:** Check scanning, understanding, enlargement, and localization with realistic content. Expert copy review produces a hypothesis; comprehension requires evidence from the intended audience.
- **Source:** Chapter 6, PDF 75–93, printed 67–85; reading explanation PDF 75–83 and design implications PDF 83–93.

### JJ-07 — Keep task state outside the user's memory

- **Trigger:** Multi-step input, editing, search, modes, comparisons, or returning to a task.
- **Rationale:** Working memory is limited and vulnerable to distraction; long-term recollection is incomplete. Hidden state forces the person to remember information the product already has.
- **Application:** Show current mode, selections, relevant constraints, progress, and prior input. Preserve search terms and editable values. Let people consult instructions without losing their place.
- **Boundary:** There is no justified universal seven-item menu limit. Externalizing state must respect privacy and avoid overwhelming the screen with irrelevant detail. Historical password-hint/security-question examples are not current authentication advice.
- **Review:** List every fact a person must carry across screens. Remove unnecessary recall, and test resumption after an interruption.
- **Source:** Chapter 7, PDF 94–112, printed 87–105; especially PDF 100–107, printed 93–100.

### JJ-08 — Make interruption and resumption part of the flow

- **Trigger:** Notifications, app switching, backgrounding, permission detours, multi-step work, or delayed completion.
- **Rationale:** Attention is selective. Changes may go unnoticed, and an interruption can displace the user's task position and next intended action.
- **Application:** Preserve work, distinguish completed from pending steps, and show meaningful changes when someone returns. For iOS, specify behavior after foregrounding, a permission trip to Settings, and a network interruption.
- **Boundary:** These iOS scenarios are adaptations of the attention principle, not platform prescriptions from the book. Avoid excessive badges or repeated announcements that compete with the task.
- **Review:** Pause at each consequential transition, resume later, and determine what changed, what remains, and how to proceed without reconstructing history.
- **Source:** Chapter 8, PDF 113–117, printed 107–111; chapter 7, PDF 104–107, printed 97–100.

### JJ-09 — Make the next action's destination and consequence clear

- **Trigger:** Navigation labels, menu items, destructive actions, or ambiguous dialogs.
- **Rationale:** People follow cues that appear related to their goal. Vague category names or conflicting uses of “cancel” require inference and encourage wrong turns.
- **Application:** Describe destinations and actions in the user's terms. When a dialog interrupts another operation, make clear which operation each button affects. Carry the same concept names across screens.
- **Boundary:** A longer literal label is not automatically better; space, localization, familiarity, and accessibility must be assessed together. Novel symbols need a discoverable meaning.
- **Review:** Predict the destination or effect from the label alone, then compare it with actual behavior. Record uncertainty as a usability hypothesis.
- **Source:** Chapter 8, PDF 118–120, printed 112–114; chapter 11, PDF 164–171, printed 159–166.

### JJ-10 — Optimize mental effort as well as action count

- **Trigger:** Choosing between a familiar multi-step flow and a compact novel interaction; expert shortcuts; redesigns.
- **Rationale:** Familiar actions can be easier than fewer actions that require problem solving. Repeated practice creates expectations that inconsistent mappings disrupt.
- **Application:** Keep predictable core interactions and add efficient routes for frequent use. Evaluate first-use comprehension and repeated-use efficiency separately. Preserve learned gestures unless a justified improvement outweighs migration cost.
- **Boundary:** Do not use a fixed tap budget, assume every shorter flow is better, or preserve complexity merely because experts learned it. Current iOS conventions constrain gesture design.
- **Review:** Compare competing flows by decisions, uncertainty, errors, recovery, and repeated-use effort—not taps alone.
- **Source:** Chapter 8, PDF 121–124, printed 115–118; chapter 10, PDF 136–153, printed 131–148; chapter 11, PDF 161–163, printed 156–158.

### JJ-11 — Complete the whole job, including the ending

- **Trigger:** Submission, checkout, saving, sharing, authentication, or leaving a task.
- **Rationale:** After the apparent goal is reached, people may forget secondary cleanup or retrieval actions. An attractive success screen can conceal unfinished work.
- **Application:** Define the true terminal state and remaining obligations. Complete safe housekeeping automatically, preserve the result, and clearly show any required next action. Distinguish submitted, processing, and completed.
- **Boundary:** Automation must not silently commit consequential choices. Completion feedback must reflect the real system state.
- **Review:** Trace what happens after the primary action. Check receipt, destination, pending work, safe exit, and return behavior, including late failure.
- **Source:** Chapter 8, PDF 124–126, printed 118–120; chapter 14, PDF 212–214, printed 209–211.

### JJ-12 — Prefer recognition where recall adds no value

- **Trigger:** Commands, selection, history, settings, unfamiliar icons, or infrequent tasks.
- **Rationale:** Recognizing a visible option or familiar context often requires less memory than producing its exact name or command unaided.
- **Application:** Expose important actions with intelligible labels, show useful recent selections, and offer relevant choices. Retain shortcuts for experienced users without making them the only route.
- **Boundary:** A long option list can be harder than expressive search. Icons are not universally recognizable. Do not apply the book's historical visual-authentication examples as security designs.
- **Review:** Identify places requiring exact recall. Compare a visible choice, search, example, or history against the task's scale and vocabulary.
- **Source:** Chapter 9, PDF 127–135, printed 121–129; core recognition applications PDF 130–134, printed 124–128.

### JJ-13 — Let the system calculate and explain what it knows

- **Trigger:** Totals, eligibility, comparisons, configuration, constraints, and error diagnosis.
- **Rationale:** Novel reasoning and calculation take effort. Making people derive information already available to the system adds avoidable uncertainty.
- **Application:** Present relevant totals, consequences, dependencies, and actionable error causes. Reduce needless interacting settings and explain why an action is unavailable.
- **Boundary:** Expose assumptions and allow correction; a confident calculated answer based on hidden or stale data is worse than visible uncertainty. Do not treat simplified neuroscience in the explanatory chapters as a design requirement.
- **Review:** List every inference or calculation the flow asks the person to make; identify which the product can safely perform or clarify.
- **Source:** Chapter 10, PDF 149–153, printed 144–148; chapter 12, PDF 179–180, printed 175–176.

### JJ-14 — Establish a coherent conceptual model and vocabulary

- **Trigger:** New product concepts, information architecture, overlapping features, or terminology drift.
- **Rationale:** Learning becomes harder when interface concepts do not map coherently to tasks or the same concept has competing names.
- **Application:** Before detailed screens, define the user's goals, objects, operations, outputs, frequency, context, and error cases. Maintain a small vocabulary tied to those concepts; use it in navigation, feedback, and help.
- **Boundary:** A conceptual model is an explicit design hypothesis until supported by research. Internal implementation terminology and a familiar visual metaphor can both be poor fits.
- **Review:** Ask whether every exposed concept earns its place in a real task and whether names remain consistent across the entire flow.
- **Source:** Chapter 11, PDF 154–172, printed 149–167; model PDF 157–160 / printed 152–155; vocabulary PDF 164–171 / printed 159–166.

### JJ-15 — Make safe exploration possible

- **Trigger:** First use, editing, experimentation, deletion, configuration, or unfamiliar controls.
- **Rationale:** Fear of making an unrecoverable mistake discourages learning by doing. Preventing mistakes and supporting recovery reduce that cost.
- **Application:** Use reversible changes, previews, preserved input, clear scope, and useful undo where appropriate. For irreversible actions, make the consequence intelligible at the decision point.
- **Boundary:** An undo promise must actually restore the relevant state. Confirmation alone is weak protection against habitual action; not every reversible edit needs a dialog.
- **Review:** Try a plausible mistake, then verify detection, recovery, and retained work. Identify irreversible edges explicitly in the flow model.
- **Source:** Chapter 11, PDF 171–172, printed 166–167; chapter 1, PDF 19–22, printed 9–12.

### JJ-16 — Support informed decisions without exploiting framing

- **Trigger:** Pricing, plans, defaults, permission requests, recommendations, and data presentation.
- **Rationale:** Wording, framing, and presentation affect choices; a mathematically equivalent description can produce a different impression.
- **Application:** Make alternatives comparable, show material consequences, separate facts from assumptions, and calculate helpful comparisons. Choose visual encodings that answer the user's decision question.
- **Boundary:** This skill's commitment to informed choice is an adaptation, not an endorsement of every persuasive example in the chapter. Do not encode a universal loss-aversion ratio, treat every person as irrational, or import old population statistics as current evidence.
- **Review:** Compare the treatment of accepting, declining, and changing a choice. Check whether omitted context or visual prominence biases a consequential decision.
- **Source:** Chapter 12, PDF 173–189, printed 169–185; framing PDF 175–178, decision support PDF 179–184, persuasion PDF 185–189.

### JJ-17 — Design the actual target and movement path

- **Trigger:** Small controls, dense rows, drag gestures, sliders, menus, and one-handed interaction.
- **Rationale:** Acquisition becomes harder as targets shrink or movement grows; constrained paths demand additional precision. The visible icon alone does not define the hit region.
- **Application:** Provide forgiving hit areas, meaningful spacing, tappable associated labels, and alternatives to precision gestures. Evaluate reach and occlusion on the intended device. Verify current platform target guidance separately.
- **Boundary:** Desktop pointer-edge advantages do not transfer directly to touchscreens. Enlarging invisible targets must not create overlapping ambiguous hit regions.
- **Review:** Inspect implemented hit areas and traverse the entire gesture path, including adjacent destructive targets and cancellation.
- **Source:** Chapter 13, PDF 190–197, printed 187–194. Figure 13.11 on PDF 197 / printed 194 was visually checked.

### JJ-18 — Preserve responsiveness and honest progress

- **Trigger:** Network requests, processing, transitions, long lists, loading, cancellation, or retry.
- **Rationale:** Perceived responsiveness depends on acknowledgement, useful feedback, and continued control as well as computation time. Unexplained delay interrupts thought.
- **Application:** Acknowledge actions promptly, show meaningful progress when knowable, keep useful work available, prioritize cancellation, and explain stalled or failed operations. Load the most useful content first when appropriate.
- **Boundary:** Historical timing ranges are context-sensitive approximations, not current universal budgets. Do not copy obsolete frame-rate targets, fake inert controls, fabricated progress, or cost-free-prefetch assumptions. Mobile energy, data, and privacy constrain speculative work.
- **Review:** Exercise slow, failed, retried, canceled, and late-success cases. Confirm state accuracy, preserved input, and prevention of duplicate consequential actions.
- **Source:** Chapter 14, PDF 198–219, printed 195–216; especially PDF 199–200, 211–217. Epilogue PDF 220–221 / printed 217–218 reinforces contextual tradeoffs.

## Use in research, design, and review

Use the principles to formulate questions before searching Mobbin: what must be understood, remembered, selected, noticed, or recovered? A reference screen is an example of a treatment, not evidence that the treatment works for this product. Compare complete action/state sequences wherever a principle concerns transitions or recovery.

Attach a principle ID to a concrete decision or finding only when the causal explanation fits the situation. Distinguish an observed implementation failure, a cognitive usability hypothesis, and an aesthetic preference. Record affected task, evidence, uncertainty, consequence, proposed change, and how to check it. A second agent can independently challenge the causal argument and inspect a different risk perspective; agreement between agents is not a user study.

For actual validation, choose methods matched to the uncertainty: comprehension with intended users; task completion and recovery in a usable prototype; assistive interaction on the target platform; repeated use when learning or efficiency matters. An expert's quick glance is an inspection, not a timed user test. For method selection and independence, use [Wilson's inspection dossier](inspection-methods.md).

## Historical and interpretive boundaries

The enduring contribution is the explanation of perceptual, attentional, learning, memory, decision, and motor constraints. Old product screenshots illustrate mechanisms; they do not set today's visual direction. The dossier excludes password-hint, security-question, and SiteKey examples as current security advice; simplified brain models as literal implementation requirements; historical performance numbers as fixed modern thresholds; and historical persuasive adoption statistics as present-day facts. These passages were read and assessed, not silently skipped. Full chapter accounting is in the ledger.
