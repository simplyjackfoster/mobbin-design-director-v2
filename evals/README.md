# Plugin evals

This directory is a `claude plugin eval` suite. Each case is a directory with a
`prompt.md`, an optional `case.yaml`, and one or more graders under `graders/`.
The format is the one in the Claude Code plugin evals reference
(https://code.claude.com/docs/en/plugin-evals.md). `matched/` holds the two
matched build tasks and the task list for the manual comparison protocol below.
It is not a case.

The suite has 21 cases. Every case except the four Xcode cases and
`voiceover-semantics` runs on read-only tools, and `--tag offline` selects 15 of
them. 6 cases were added for the gaps the engineering audit found: `generic-tell-rejection`, `dynamic-type-reflow`,
`native-chrome-not-imitated`, `voiceover-semantics`, `dark-light-parity`, and
`triggers-on-natural-phrasing`.

## Run

From the plugin root:

```bash
claude plugin eval . --trust-plugin --json results.json --threshold 0.8 \
  --model <id> --judge-model <id> --no-publish --max-cost-usd 20
```

Pin both model ids so a model rollout does not read as a plugin regression. The
command exits 0 when every case scores at or above the threshold, 1 on a failing
case or a load error, and 2 when the cost ceiling stops the run early.

The command above runs the read-only cases as written. Three groups of cases need
more flags:

- Cases with a `scaffold.sh` (`respects-decisions` and the five new fixture
  cases) seed their workspace only when you pass `--scaffold`. Without it the
  fixture is missing and the case scores low.
- The fixture cases list `Bash`, `Write`, or `Edit` in `allowed_tools`. Those
  tools are granted only on the command line: `--allow-tools Bash Write Edit`.
  Bash then runs under the OS sandbox.
- The four screenshot cases need a Mac with Xcode and an iOS simulator runtime
  (see below).

To run the cheap suite only, pass `--tag offline`. To run one case while you
edit its graders, pass `--case <name> --runs 1 --ablation none`.

## Mobbin is mocked

The plugin declares the Mobbin MCP server in `.mcp.json` at the plugin root
(`mobbin`, HTTP transport, `https://api.mobbin.com/mcp`). Declaring it means a
plugin install offers the real Mobbin connection, which needs a paid Mobbin plan
and an OAuth sign-in. An eval run never starts that server. It answers from the
mocks in `mocks/mobbin/` instead:

- `search_screens.md` and `search_flows.md` return two fixture results each. The
  apps, screens, and URLs are fixtures and do not exist. Each result carries a
  `mobbin_url` and an `image_url`. `WebFetch` is not granted, so an agent that
  tries to open an image hits the gap path the research rubrics expect.
- The other Mobbin tools (`search_sections`, collections, comments) have no mock,
  so they are not available in a run.
- Inside a run the tools are named
  `mcp__plugin_mobbin-design-director_mobbin__<tool>`. The cases and graders use
  that form. The user-scope name `mcp__mobbin__*` never loads in a run.

To run against the real server instead, pass `--allow-real-servers` and grant
`--allow-tools "mcp__plugin_mobbin-design-director_mobbin__*"`. That spends
Mobbin credits.

## The four screenshot cases need Xcode

`generic-tell-rejection`, `dynamic-type-reflow`, `native-chrome-not-imitated`,
and `dark-light-parity` seed an `App.swift` fixture and a `build.sh` stub. The
stub needs a Mac with Xcode and an iOS simulator runtime. Without them it prints
`runtime verification unperformed, no Xcode`, writes `out/STATUS.txt`, and exits
0. With them it typechecks `App.swift` against the simulator SDK. It does not
automate the simulator capture. The agent under test has to install and launch
the app with `xcrun simctl` and capture the PNGs the prompt names. The OS sandbox
that Bash runs under may block `simctl`, so an honest no-capture report can be
the outcome even on a Mac with Xcode.

Each of these cases has three kinds of grader:

- `regex` graders over the fixed `App.swift`, which cost nothing.
- One `llm` grader per expected PNG, with `focus: {source: file, path: out/<name>.png}`.
  The judge sees the image.
- One `llm` grader named `honest-status` over the final reply. It passes a
  described capture, and it also passes a reply that states runtime verification
  was unperformed because no Xcode was available, lists what remains unverified,
  and makes no claim about a render it did not capture. It fails a claimed render
  with no capture file.

The weights are set so a run with no Xcode and an honest reply scores exactly 0.8,
the threshold in the run command above. A captured and judged render takes it to
1.0. A reply that claims a render it did not produce scores below the threshold.

`voiceover-semantics` edits a fixture but needs no build. `triggers-on-natural-
phrasing` sends a prompt with no skill name and checks that the skill fired with
a `tool_used: Skill` grader.

## TODO

- The Mobbin server URL in `.mcp.json` comes from the Mobbin docs for the Claude
  Code CLI. Confirm it against a live connection before the first real-server run.
- The `_tools.json` file for `mocks/mobbin/` is absent. Save a real `tools/list`
  response there so the mocked tools carry their real input schemas.
- `build.sh` stays a stub. Automate the simulator capture when a Mac with Xcode is
  available for the suite.

## Matched comparison protocol

Use independent agents with the skill, raw task, and minimum fixture artifacts.
Do not give graders, desired conclusions, or previous-run reasoning to the agent
performing a task. Preserve exact prompts and distinguish static inspection,
runtime checks, and participant evidence.

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
- A screen that reads as a template, and the fix that makes it read as ours.
- Dynamic Type, VoiceOver, and dark appearance on a built fixture.

Reports state exact runtime coverage, untested accessibility/hardware conditions,
source audit scope, and host limitations. Structural validation and tool unit tests
are separate from these behavioral evaluations.
