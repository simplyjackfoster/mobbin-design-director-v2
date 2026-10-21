# Task playbooks

Use the shared loop and only the questions relevant to the request.

| Task | Questions that change the design | Minimum useful verification |
|---|---|---|
| New feature / journey | Real trigger, outcome, required information, first useful value, commitment, alternate/returning path | Key path plus consequential recovery, cancellation, and state continuity |
| Improve a screen | What works now? Which observed or hypothesized problem matters? Does this require a structural change? | Current vs revised with same content, plus affected neighboring transitions |
| Navigation / IA | User goals and objects, frequency, destinations versus actions, discoverability, alternate entry | Find common tasks; Back/return context; direct entry where supported |
| Onboarding / permission | What value precedes each ask? What can be deferred? What happens after skip/denial/return? | First meaningful outcome, returning user, missing permission/data, resume |
| Forms / editing | Necessary input, safe defaults, meaningful grouping, correction, draft ownership, commitment | Valid/invalid input, keyboard, cancellation, retry, saved versus draft state |
| Paywall / purchase | Timing, clear costs/terms, comparison, eligibility, dismissal, restoration where supported | Actual commitment boundary, failure/restore paths, understandable outcome |
| Home / dashboard | Frequent goal, first priority, meaningful next action, new/returning user, information density | Empty/populated/partial states, hierarchy with realistic content |
| Detail / result / comparison | Decision to make, explanation, confidence/uncertainty, comparable units, supporting detail | Correct context/qualifications, next action, return state, long content |
| Search / collection | Object vocabulary, recognition, filters, relevance, selection state, zero results | Query and position restoration, empty/error states, correction and selection |

A playbook proposes questions, not extra features. Do not add authentication,
payment, analytics, offline behavior, or a new navigation system unless the user's
scope and product needs call for them. See [flows](flows.md), [input](input.md),
and [review](review.md) for the corresponding method.
