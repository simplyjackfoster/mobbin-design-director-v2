# Microinteractions: triggers, rules, feedback, loops and modes

Use when a contained moment carries the task: a toggle, follow, save, snooze,
sync, mute, add-to-cart, pull-to-refresh, a hidden gesture or an automatic
suggestion. Start from the journey in [flows](flows.md) and the general action
contract in [input and feedback](input.md). This module adds the small-scale
specification. [Microinteractions](sources/microinteractions.md) supplies the
vocabulary and checks, with page citations and exceptions in MI-01–19. They are
design hypotheses, not evidence of user performance.

Apply only the parts the change touches. A copy tweak does not need a loop table.

## Write the rules before the frame

State the goal as an end state (signed in, woken on time), not a step. List the
rules in order: trigger, preconditions, branches, what the person can cancel or
undo, and the end state. If the rules cannot be written or sketched simply,
people will not form the model either ([MI-01](sources/microinteractions.md)).
When a mode or setting has exceptions, state them where it is set and keep a
lasting indicator after the confirmation fades ([MI-02](sources/microinteractions.md)).

Run the platform check early: background limits, notification permission, Live
Activities and widgets on iOS; tab visibility, focus and permissions on web.

## Triggers

| Decision | Check |
|---|---|
| How visible | Breadth × frequency × consequence picks persistent, contextual, menu or shortcut. No frequent action lives only in a menu or gesture ([MI-03](sources/microinteractions.md)). |
| What it shows | The one current fact people open it to check, also available without hover and to assistive technology ([MI-04](sources/microinteractions.md)). |
| Hidden trigger | A visible single-pointer equivalent; first firing explains itself and how to turn it off ([MI-05](sources/microinteractions.md)). |
| System trigger | Frequency cap, suppressing context, before/during/after indicator, failure policy, in-place off control, manual twin ([MI-06](sources/microinteractions.md)). |
| Control | Fits the state count and risk; same action every activation; every state defined on the control, including focus, working, disabled with reason and drag targets ([MI-07](sources/microinteractions.md)). |

## Rules and defaults

Start from context the product legitimately holds, and drop any inference that
could embarrass or endanger the person if shown or wrong ([MI-08](sources/microinteractions.md)).
Name the value a default applies and remove options that change nothing
([MI-09](sources/microinteractions.md)). For ranking or suggestions, write the
inputs, exclusions and tunable values, and expose the inputs people can correct
([MI-10](sources/microinteractions.md)).

## Feedback

1. Derive a feedback table from the rules: event → message → channel → location.
   Acknowledge every manual action. Announce only background events that change
   what the person can do. Say what did not happen when people fear a side
   effect ([MI-11](sources/microinteractions.md)).
2. Scale channels and intensity to consequence and frequency, and specify
   duration, dismissal, escalation and repetition. No meaning depends on sound or
   haptics alone ([MI-12](sources/microinteractions.md)).
3. Try the existing control, scroll edge or progress area as the carrier before
   adding a banner or dialog. Change the accessible name with the icon
   ([MI-13](sources/microinteractions.md)).
4. Keep personality to rare, low-stakes moments, with the plain status beside it
   ([MI-14](sources/microinteractions.md)).

## Loops and modes

- Prefer no mode, and treat more than one as a warning sign (an uncited
  heuristic; strongly signalled platform edit modes are fine). Show which mode is
  active and how to leave; leaving restores the view plus the changes. Held or single-use modes end on their own
  and have a non-hold path ([MI-15](sources/microinteractions.md)).
- For each loop write the kind, interval, end condition, per-cycle display and
  end behavior. Show time-bound windows with a way to act or extend
  ([MI-16](sources/microinteractions.md)).
- Design the third and hundredth use: visible, editable memory; suggestions that
  stop when declined; reversible reduction of guidance
  ([MI-17](sources/microinteractions.md)).

## Neighbors and evaluation

Map the moments this one hands off to or conflicts with before polishing it.
Give a signature treatment only where it serves identity without slowing frequent
work or a gateway such as sign-in ([MI-18](sources/microinteractions.md)). Test the
coupled behavior in code or a high-fidelity prototype, and trace each symptom to
its cause: nothing seemed to happen → feedback; lost in place → mode or
transition; did not know it existed → hidden trigger ([MI-19](sources/microinteractions.md)).

## Platform notes

- **iOS:** sheets or pushed views for modes with Done/Cancel; context menus and
  VoiceOver custom actions mirror swipe and long-press triggers; semantic
  feedback generators or `.sensoryFeedback` for haptics; sounds follow Silent
  mode and Focus; respect Reduce Motion.
- **Web:** `role="switch"` or native inputs with `aria-pressed`/`aria-expanded`
  state; polite live regions for arrivals; `aria-busy` on working regions;
  `prefers-reduced-motion`; listed, remappable keyboard shortcuts; no autoplaying
  sound.
