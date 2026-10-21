# User Interface Inspection Methods — source dossier

Chauncey Wilson. *User Interface Inspection Methods: A User-Centered Design Method*. First edition, Morgan Kaufmann / Elsevier, 2014. ISBN 978-0-12-410391-7. The supplied PDF has 132 pages. This is Wilson's six-method handbook, **not** the Nielsen and Mack volume with a similar title. Identity, checksum, coverage, and visual checks are in [the coverage ledger](inspection-methods-coverage.json).

All six chapter bodies were read in bounded batches. Selected tables and the screenshot walkthrough example were visually inspected where layout mattered. Citations use **one-based PDF pages**, with printed labels separately. The recommendations below synthesize the book in original words; iOS cases, agent orchestration, and evidence labels are adaptations for this skill, not methods validated by the book for language models.

## Choose the method for the question

| Method | Best contribution | Important limit |
|---|---|---|
| Heuristic evaluation | Broad inspection against understandable general and domain-specific principles; can mix task and exploratory review | Reviewer expertise, task selection, and evaluator variation affect findings; false positives and missed problems remain |
| Individual expert review | Practical synthesis of tasks, principles, product experience, and existing evidence | One reviewer cannot establish comprehensive usability or replace actual user evidence |
| Perspective-based inspection | Deliberate coverage of different goals and risks, such as initial learning, repeated use, errors, or accessibility | A role description does not confer expertise or lived experience; perspective selection has limited empirical guidance |
| Cognitive walkthrough | Inspect whether a new or infrequent user can discover an action, connect it to the goal, and understand the result | Hypothetical users; focused mainly on initial learnability, not complete UX or expert efficiency |
| Pluralistic usability walkthrough | Actual or potential users and product participants independently choose actions on a prepared sequence, then discuss | Predetermined path, facilitated group effects, and limited exploration; not unrestricted end-to-end use |
| Formal usability inspection | Explicit preparation, roles, defect records, rework, verification, and process learning | Heavy process with limited direct usability ROI evidence; adapt useful parts rather than mandate the entire ceremony |

Sources: chapters 1–6, especially PDF 10–18, 42–45, 58–62, 73–76, 88–91, 105–110. The book's staffing ranges and durations are contextual guidance, not required numbers of agents or universal study sample sizes.

## Principles

### WI-01 — Define scope, tasks, users, and risk before inspecting

- **Trigger:** Starting research, design critique, implementation review, or release assessment.
- **Rationale:** A review of convenient screens can miss the tasks and conditions that matter. Frequent tasks and rare consequential tasks both deserve consideration.
- **Application:** Specify intended users and evidence about them, task goals, relevant variants, realistic content, environment, and coverage limits. Include transitions between features. For iOS, consider permissions, interruption, keyboard, offline behavior, and assistive interaction where relevant.
- **Boundary:** Do not invent user research or choose only paths that flatter the design. A task script that reveals every control can hide discoverability problems.
- **Review:** Compare planned coverage with actual coverage and explain omissions. Preserve a list of unanswered questions.
- **Source:** Chapter 1, PDF 10–13 / printed 2–5, PDF 21–22 / printed 13–14; chapter 4, PDF 78–85 / printed 71–78; chapter 6, PDF 111–115 / printed 106–110.

### WI-02 — Combine realistic task traversal with broader exploration

- **Trigger:** A review that currently examines isolated screenshots or only one scripted happy path.
- **Rationale:** Task-oriented inspection reveals goal and transition problems; exploratory inspection can expose features, edge conditions, and global inconsistencies omitted from the script.
- **Application:** Traverse priority tasks first, then inspect uncovered states and recurring components. Use realistic volumes and content. Explore plausible errors, alternate inputs, backtracking, cancellation, resumption, and empty results in a safe test environment.
- **Boundary:** Label capabilities unavailable in a static mockup as unverified. A screenshot cannot demonstrate input retention, latency, focus, or successful recovery.
- **Review:** Maintain task/state coverage and a separate list of exploratory findings. Do not count inspecting one instance as exhaustive coverage of a repeated pattern.
- **Source:** Chapter 1, PDF 10–12, 29–34 / printed 2–4, 21–26; chapter 2, PDF 50–52 / printed 42–44; chapter 5, PDF 101–102 / printed 95–96.

### WI-03 — Match inspection criteria to the product and make them testable

- **Trigger:** A generic checklist, vague quality claim, or imported design rule.
- **Rationale:** Reviewers need shared meanings and concrete examples. Broad principles alone may miss domain-specific behavior; excessively long lists are hard to apply consistently.
- **Application:** Select a small relevant set of general principles, domain rules, current platform requirements, and product constraints. Give each a trigger and an observable review question. Use previous verified issues to improve criteria.
- **Boundary:** Do not turn contextual examples into universal restrictions, such as a fixed two-click limit. Exact platform and accessibility requirements require current authoritative verification.
- **Review:** Ask whether another reviewer can apply the criterion to the same behavior and explain the outcome. Record where the criterion is uncertain or inapplicable.
- **Source:** Chapter 1, PDF 19–27 / printed 11–19; chapter 3, PDF 64–69 / printed 56–61; chapter 6, PDF 112–116 / printed 107–111.

### WI-04 — Review independently before merging findings

- **Trigger:** Multiple agents or people reviewing the same proposed flow or implementation.
- **Rationale:** Different evaluators notice different problems. Independent preparation preserves opportunities to discover issues before group discussion anchors attention.
- **Application:** Give reviewers the same artifact version and task evidence, plus distinct risk perspectives. Require their own observations and assumptions before they see other findings. Merge duplicates afterward while retaining affected locations and dissent.
- **Boundary:** Several agents sharing a model and source material are not independent human participants or a statistically independent sample. Repeated agreement is not validation. Do not equate a named agent role with domain credentials.
- **Review:** Confirm independent first passes, meaningful coverage differences, and resolution of disagreements using evidence rather than vote count.
- **Source:** Chapter 1, PDF 12–14, 24–25, 29–31 / printed 4–6, 16–17, 21–23; chapter 3, PDF 62–66 / printed 54–58; chapter 6, PDF 117–119 / printed 112–114.

### WI-05 — Use perspectives tied to goals and known constraints

- **Trigger:** Important risks are repeatedly missed, or a complex product serves different use patterns.
- **Rationale:** A focused lens can increase attention to issues otherwise lost in a broad review. Useful perspectives reflect actual goals, context, skills, or constraints.
- **Application:** Assign learnability, frequent-use efficiency, recovery, accessibility, language, or visual hierarchy as explicit lenses with task questions. Mark unverified audience assumptions and request actual evidence when consequential.
- **Boundary:** Do not simulate disability or demographics and claim lived-experience evidence. Age alone does not establish technology skill. The source itself notes limited guidance for choosing the most effective perspectives.
- **Review:** Verify that each lens changes the questions or coverage; remove redundant roles and retain findings outside a reviewer's assigned lens.
- **Source:** Chapter 3, PDF 58–65, 67–71 / printed 50–57, 59–63.

### WI-06 — Walk through every meaningful action and system response

- **Trigger:** New or infrequent use, onboarding, a key transition, or an uncertain action label.
- **Rationale:** Learnability depends on the chain from intent to discovered action to understood result. A screen can look clear while requiring knowledge the intended user does not have.
- **Application:** For each meaningful step record goal, prior knowledge, visible cues, possible action, system response, and next state. Ask whether the person would pursue the intended subgoal, notice the action, connect it to the desired effect, and recognize progress. Record credible success/failure reasoning and assumptions.
- **Boundary:** These are predictions about hypothetical users. A walkthrough does not establish actual completion rates, expert efficiency, or every valid alternative path. Choose action granularity appropriate to the task.
- **Review:** Flag unsupported success stories and explicit knowledge gaps; include the point of failure and the evidence needed to resolve it.
- **Source:** Chapter 4, PDF 73–81 / printed 66–74; limits and reporting PDF 82–86 / printed 75–79.

### WI-07 — Keep expert inspection distinct from evidence from people

- **Trigger:** Reporting a critique, agent walkthrough, automated check, or user session.
- **Rationale:** Inspections predict potential usability problems; actual users can supply different evidence. Automated checks cover only some barriers. No method finds everything.
- **Application:** Label method, artifact, participant/reviewer type, task, conditions, and limitations. For pluralistic walkthroughs, collect each person's proposed action independently before discussion, let users speak first, and preserve their responses separately from team interpretation.
- **Boundary:** A multiagent review is not a pluralistic user study. A facilitated choice on a screenshot is not observed successful use of a working flow. If surrogates replace actual users, say so and limit conclusions.
- **Review:** Audit every use of “tested,” “validated,” “users,” and “accessible.” Ensure the evidence supports the scope of the claim.
- **Source:** Chapter 2, PDF 51, 54 / printed 43, 46; chapter 4, PDF 73–75 / printed 66–68; chapter 5, PDF 88–98, 102–103 / printed 82–92, 96–97. Table 5.4 on PDF 96 / printed 90 was visually checked.

### WI-08 — Triangulate findings without treating repetition as proof

- **Trigger:** A speculative critique, disputed issue, incomplete access to users, or prioritization under uncertainty.
- **Rationale:** Support records, observed behavior, research, implementation evidence, and inspection can reveal complementary problems. Convergence can strengthen confidence, while absence from a method may reflect its limits.
- **Application:** Attach available evidence sources to each finding and note their independence, recency, and task fit. Look for contradictions and counterexamples. Use future user research to resolve consequential uncertainty.
- **Boundary:** Several agents repeating one heuristic are one evidence lineage. Do not dismiss a severe observed failure because other methods missed it, or assume all reported complaints describe the same root cause.
- **Review:** Build a compact finding-by-evidence matrix for contested issues. Keep confidence separate from estimated consequence.
- **Source:** Chapter 1, PDF 35–37 / printed 27–29; chapter 2, PDF 47–48, 54–55 / printed 39–40, 46–47. Table 2.1 on PDF 55 / printed 47 was visually checked.

### WI-09 — Write findings that can be reproduced and acted on

- **Trigger:** Converting critique into a decision or implementation task.
- **Rationale:** A defect list loses value when reviewers disagree about location, granularity, expected behavior, or severity. Preference is not automatically a usability problem.
- **Application:** Record task/state, location, actual behavior, expected behavior or principle, consequence, evidence, uncertainty, scope, and a proposed verification. Distinguish observed constraint failures, supported usability hypotheses, and aesthetic preferences. Preserve each instance before grouping global causes.
- **Boundary:** Severity and confidence are separate judgments; neither is established by consensus alone. A typo can be critical if it changes meaning. Avoid inflated counts from duplicate instances or multiple descriptions of the same failure.
- **Review:** Have a reviewer unfamiliar with the finding reproduce or inspect it and understand what would resolve it.
- **Source:** Chapter 1, PDF 27–32, 38–40 / printed 19–24, 30–32; chapter 2, PDF 55–56 / printed 47–48; chapter 6, PDF 115–123 / printed 110–118.

### WI-10 — Preserve strengths and examine tradeoffs when fixing

- **Trigger:** Redesigning after critique or resolving a conflict between principles.
- **Rationale:** One feature can help one task or audience and hinder another. Removing a defect can damage a useful property or create a new problem.
- **Application:** Record successful aspects that the change should preserve. Inspect the proposed correction across related tasks, audiences, and states. Retain disagreements until the underlying assumptions are visible.
- **Boundary:** Positive findings should identify behavior worth preserving, not merely soften criticism. A global redesign is not justified by one local problem without checking the broader pattern.
- **Review:** Compare before and after on the original failure and neighboring successful paths; explicitly check regressions and newly introduced knowledge demands.
- **Source:** Chapter 1, PDF 17–18, 37–38 / printed 9–10, 29–30; chapter 5, PDF 101 / printed 95; chapter 6, PDF 121–122 / printed 116–117.

### WI-11 — Track corrections through verification, not just recommendation

- **Trigger:** A review produces issues, a designer proposes a fix, or an implementation claims completion.
- **Rationale:** Finding problems is only an intermediate result. Useful inspection leads to appropriate changes and evidence that those changes resolved the problem.
- **Application:** Track accepted, deferred, disputed, implemented, and verified states; name the responsible role when known. Verify the original failure and adjacent behavior on the actual artifact. Retain rationale for accepted limitations.
- **Boundary:** Issue counts and a clean checklist are not proof of usability. Changes in counts can reflect reviewer coverage or reporting granularity rather than improved quality. Do not claim the book establishes a general ROI for formal usability inspections.
- **Review:** Report actual inspected scope, unresolved consequential risks, verified fixes, and remaining validation needs. Judge the result against task outcomes.
- **Source:** Chapter 1, PDF 32, 37, 39–40 / printed 24, 29, 31–32; chapter 3, PDF 63, 67 / printed 55, 59; chapter 6, PDF 120–126 / printed 115–121. Table 6.5 on PDF 124 / printed 119 was visually checked.

### WI-12 — Scale review formality to risk and maturity

- **Trigger:** Choosing how much review to run for a small screen change, a new flow, or a consequential release.
- **Rationale:** Formal roles, preparation, and verification improve accountability, but heavy meetings and exhaustive forms can consume effort without proportionate coverage. Rough artifacts may need rapid iteration first.
- **Application:** Use lightweight task and heuristic review for early work; add independent review, explicit criteria, traceable issue records, and verification as complexity or consequence grows. Limit sessions to coherent tasks and declare incomplete inspection honestly.
- **Boundary:** Do not import the whole formal process, rigid staffing, or historical meeting times as mandatory agent ceremony. The book reports limited direct empirical validation of formal usability inspection effectiveness and ROI.
- **Review:** Explain why the chosen method can answer the current question, what it cannot establish, and what should happen next if uncertainty remains.
- **Source:** Chapter 4, PDF 83–86 / printed 76–79; chapter 6, PDF 105–114, 123–126 / printed 100–109, 118–121.

## Suggested skill review sequence

1. Define task outcomes, audience evidence, artifact version, scope, and risks. Mark assumptions and unavailable behavior.
2. Review priority flows with action/response/state records. Use a cognitive walkthrough for initial learning and other lenses for efficiency, accessibility, recovery, and visual structure.
3. When parallel review is justified, have agents inspect independently before synthesis. Give each a concrete question and require evidence, causal reasoning, coverage, and limitations.
4. Merge repeated root causes while retaining instances. Separate confirmed failures, hypotheses, and preferences; preserve useful behavior and unresolved dissent.
5. Correct accepted findings, then recheck the original conditions and nearby paths. Report the artifact actually verified.
6. Where uncertainty requires people, prepare a suitable study plan and recruit through an authorized process. Do not fabricate results or describe proxy review as real-user validation.

This sequence is a modern adaptation assembled from the methods, not a protocol whose effectiveness the book tested. For mobile work, use a real device or faithful runtime when the question involves touch, keyboard, system UI, assistive technology, interruption, or latency. Screenshots are useful evidence for visible design and prepared walkthroughs; they cannot substantiate every interaction claim.

## Coverage and exclusions

All method chapters were studied, including their weaknesses, variants, planning, conduct, reporting, and follow-up sections. Old website examples illustrate the method rather than prescribe current UI. Historical headcounts, meeting durations, task counts, sample heuristics, and empirical percentages are not copied as universal requirements. Organizational advice about public reports, invitations, recruiting, or distributing findings is source material, not authorization to communicate externally or publish anything. References were inventoried as bibliography rather than treated as independently read research.
