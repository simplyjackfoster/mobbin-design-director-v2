# Behavioral and artifact evaluations

Use independent agents with the skill, raw task, and minimum fixture artifacts.
Do not give graders, desired conclusions, or previous-run reasoning to the agent
performing a task. Preserve exact prompts and distinguish static inspection,
runtime checks, and participant evidence.

The existing per-case `prompt.md` / `graders/` format remains compatible with the
repository's prior Claude evaluation packaging. The Claude runner and Mobbin
availability must be verified locally; a file's existence is not a passing run.
Codex can run the same tasks using independent child agents or an available CLI.
No specific model is required; record the actual environment used.

## Matched comparison protocol

1. Freeze v1 and v2 skill snapshots. Give fresh agents the same user task, fixture
   content, constraints, allowed tools, and resource budget. Keep outputs separate.
2. For native/browser tasks, build each artifact using the same harness and inspect
   the actual render and relevant transitions. Preserve logs and screenshots outside
   the skill source tree. Grade plans as plans, implementations as implementations.
3. Give a separate evaluator anonymized artifacts and the original task. Judge
   goal clarity, interaction completeness/recovery, cognitive effort, visual
   coherence/character, platform fit, evidence honesty, and process proportionality.
4. Use explicit examples and artifact pointers for conclusions. Do not claim a
   measured user improvement from agent preference. Owner visual preference is a
   separate evidence source and may remain pending.
5. Repair supported failures, then rerun affected cases. Record changes to prompts,
   harnesses, or resource availability so improvements are not falsely attributed
   entirely to the skill.

The runtime pilot uses deterministic local fixtures, not live financial services.
No production files, databases, accounts, or remote repositories are
modified by evaluation. An isolated prototype is not a shipping product change.

## Required scenarios

- Sample iPhone reading-list journey with approved content/design constraints.
- Unrelated iPhone setup with interruption and permissions.
- Dense web comparison with keyboard/browser behavior.
- Expressive design without an existing system.
- Routine approved edit without extra process.
- Missing Mobbin, missing user research, and missing native runtime.
- Attractive UI with reproduced flow failures.

Reports state exact runtime coverage, untested accessibility/hardware conditions,
source audit scope, and host limitations. Structural validation and tool unit tests
are separate from these behavioral evaluations.
