---
name: microinteraction-feedback
tags: [offline, v2]
max_turns: 20
allowed_tools: [Read, Glob, Grep, Skill]
---

Use the mobbin-design-director skill in critique mode for a web photo-upload
feature. Only this description is available; Mobbin and runtime are not. Every
upload success, including each file in a batch of 200, plays a chime, shakes the
page and shows a confetti dialog that must be dismissed. Background sync checks
every 10 seconds and shows "Up to date" each time. A failed upload retries
forever with no message. The upload button never changes while files are working;
a separate banner at the top of the page reports progress. Errors read "Oops! You
broke it 🙃". A default "Share with followers" applies silently after upload.
The team plans to measure success by confetti clicks.

Give an actionable critique and targeted verification plan. Distinguish observed
facts, predicted risks and taste. Do not implement or imply that the described
interface has been inspected live.
