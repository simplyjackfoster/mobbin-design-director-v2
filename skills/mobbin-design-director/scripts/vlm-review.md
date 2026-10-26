# VLM review prompt: pairwise screenshot check

A template for a vision model that compares two screenshots of the same screen.
Fill the `{{...}}` slots, send the prompt twice (once per image order), then
merge the two answers by the rules at the end. The model is a flagger. It
names tells for a human to verify. It does not score, rank, or pick a winner.

## Before you send it

- Same content in both images. Same data, same state, same step of the flow.
- Same scale. Same device, same content size, same appearance. Crop nothing.
- Add one anchor image: a reference screen from the same category, at the same
  scale, that the project already accepts as its bar. A Mobbin capture from the
  cache works. The anchor gives the model a fixed point, so its answer is about
  distance from a known screen and not about taste on the day.
- No overlays. No arrows, boxes, labels or marks drawn on any image. Overlays
  inflate scores (research/04 step 10, arxiv 2505.15249).
- Send both orders. Run A then B, then B then A. Keep only the tells the model
  names in both runs. MobileForge (arxiv 2607.28645) measured 23.3 percent
  position bias in pairwise judgments, so one order is not a result.

## Prompt

```
You review two iPhone screenshots of the same screen. Image 1 is {{image_1_label}}.
Image 2 is {{image_2_label}}. Image 3 is the anchor: a reference screen from the
same category that the team accepts as its bar. Treat the anchor as a fixed
point, not as a third candidate.

Screen: {{screen_name}}
Flow step: {{flow_step}}
Capture state: {{appearance}}, content size {{content_size}}, {{other_settings}}

Task 1. Name every tell you can see in Image 1 and in Image 2. A tell is a
pattern from the defaults-detector tell list (defaults-detector.md in this
skill's references). Use these names where they fit:
{{tell_list}}
For each tell give: the image number, the tell name, the location on the screen
in plain words, and what you see that makes it a tell.

Task 2. Classify each tell as exactly one of:
- verified defect: a rule of the platform or of accessibility is broken, and
  you can point at the pixels that break it (clipped text, a control under 44
  points, contrast too low to read, a missing label).
- usability risk: a person may misread or miss something, but no rule is
  broken. State who is at risk and in what situation.
- aesthetic preference: the screen works. You would do it differently. Say so,
  and do not weigh it against the two classes above.

Task 3. State what you cannot see. Haptics, sound, motion and timing do not
appear in a still image. Say "not visible" for each of these. Do not guess.

Rules:
- Do not score, rate, rank, or say which image is better.
- Do not count tells as a verdict. Three aesthetic preferences do not add up to
  one defect.
- Name no tell you cannot locate on the screen.
- Say "none found" when an image has no tell of a kind.
- If Image 1 and Image 2 differ only in the anchor's direction, say so once.

Answer in this shape:

Image 1
- <tell name> | <class> | <location> | <what you see>

Image 2
- <tell name> | <class> | <location> | <what you see>

Not visible: <list>
```

## After both runs

1. Keep a tell only when both orders name it for the same image. A tell named in
   one order only is a position bias candidate; drop it or re-run with a second
   anchor.
2. A verified defect still needs a human check against the pixels. The model
   flags. The reviewer verifies.
3. Record the kept tells with the capture file names (step-NN_<cfg>.png) so the
   finding points at a file, not at a memory of a screenshot.

## Limits (research/04 step 10)

- Position bias: 23.3 percent on mobile UI pairs (MobileForge, arxiv 2607.28645).
  Hence both orders.
- Overlays inflate scores (arxiv 2505.15249). Hence clean images only.
- Pairwise VLM preference is near random on UI quality (UIClip, arxiv 2404.12500).
  Hence the model flags tells and does not score.
- A still image carries no motion, sound, haptics or timing. Those come from the
  proxy grep and the hitch metrics, not from this prompt.
