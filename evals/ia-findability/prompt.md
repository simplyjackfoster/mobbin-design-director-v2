Use $mobbin-design-director research web to recommend a redesign of our internal
resource library. Deliver a concise design recommendation and a buildable behavior
specification. Do not implement code or contact anyone.

The library has 8,400 resources. Current top-level navigation mixes departments
(People, Engineering), formats (Videos), and tasks (Get access). Staff report in
support tickets that they cannot find things. Some know a document title; new
hires often know only the problem; auditors need all applicable policies; returning
staff follow old links. We have no participant study. Mobbin is unavailable.

Sample content:
- R17: "Away from work", a policy people call "vacation policy"; owner People;
  region missing; review date 2023; current status not verified.
- R18: "Paid time off request", a transaction guide, not the policy; region US.
- R19: "Equipment access", a task guide jointly owned by IT and Engineering.
- R20: "Design systems", a video with no transcript or topic metadata.

The current API searches titles only, has no synonym expansion, and returns up to
100 matches without a total or completeness flag. Department is present on all
records; region on 40%; topic on 20%. There is no favorites service. Someone
suggested treating "vacation", "leave", and "absence" as equivalent, adding
region/topic filters with counts, and making search the whole homepage. A prototype
shows those controls, but they are not wired up. Keep working document IDs and
existing access restrictions. Explain what we should ship first and how to check it.
