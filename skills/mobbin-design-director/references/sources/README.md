# Source index and provenance

These are original decision-oriented syntheses of the user's supplied editions,
not reproductions of the books. Read the operational topic module first; open a
source dossier when a rationale, limitation, or citation matters. Normal skill
use does not require the PDFs.

| Dossier / IDs | Best for | Coverage manifest |
|---|---|---|
| [The UX Book](ux-book.md), UX | Process, discovery, modeling, emotional experience, prototyping, evaluation | [JSON](ux-book-coverage.json) |
| [About Face](about-face.md), AF | Goals, personas/scenarios, conceptual models, flow, excise, interaction | [JSON](about-face-coverage.json) |
| [Designing Interfaces](designing-interfaces.md), DI | Context-qualified patterns, IA, navigation, visual framework, input | [JSON](designing-interfaces-coverage.json) |
| [Designing with the Mind in Mind](mind-in-mind.md), JJ | Attention, perception, memory, learning, decisions, responsiveness | [JSON](mind-in-mind-coverage.json) |
| [User Interface Inspection Methods](inspection-methods.md), WI | Walkthroughs, independent inspection, evidence, findings, evaluation limits | [JSON](inspection-methods-coverage.json) |
| [Touch Design for Mobile Interfaces](touch-design.md), TD | Grip/context, actual hit regions, occlusion, neighboring actions, mobile disclosure | [JSON](touch-design-coverage.json) |
| [Interaction Design, sixth edition](interaction-design.md), ID | Conceptual models, emotional and contextual interaction, evidence, prototype fidelity and evaluation | [JSON](interaction-design-coverage.json) |
| [Practical UI, second edition](practical-ui.md), PU | Hierarchy, color, typography, grouping, composition, controls and forms | [JSON](practical-ui-coverage.json) |

The eight coverage manifests together are the source manifest. Each records title,
authors, edition/year, PDF page count and SHA-256; chapter boundaries, actual read
ranges and justified exclusions; extraction caveats and rendered figure checks.
PDF page numbers are one-based. Printed labels can differ and are only supplied
when verified. Hashes identify the exact source files without exposing local paths.

## How to interpret coverage

- `full-study`: substantive chapter text studied; any excluded pages are enumerated
  with reasons. It does not imply every historical screenshot was visually inspected.
- `assessed-excluded`: chapter assessed and deliberately omitted for a stated reason.
- `partial-study`: work remains; never advertise this as complete study.
- `figure_checks`: actual rendered pages inspected because their visual evidence
  affects interpretation. Text extraction is not visual inspection.

Reading ranges reflect what readers consumed, not merely what a parser extracted.
Blank pages, dividers, references, and repeated historical screenshot galleries
may be excluded explicitly. Source notes explain what that limits.

## Synthesis boundaries

Goals precede solution choice; patterns have contexts and costs; visual character
is legitimate; inspection predicts problems while participant observation supplies
different evidence. These shared themes inform the runtime modules. Agreement
between books is not a vote or proof for a particular product.

Preserve differences: expert-efficient interaction can conflict with novice
learnability; fewer steps can increase thinking; consistency can conflict with a
useful contextual exception; emotional expression can help identity while harming
attention if overused. Explain the relevant audience/task tradeoff.

The newer sources sharpen rather than replace earlier guidance. Interaction
Design's metaphor benefits coexist with About Face's warnings about misleading
metaphors. Practical UI's simplification and restrained color recommendations
coexist with useful expressive detail; keep information and character that serve
the task. Its example measurements, web layouts and 2024 contrast claims are not
current native requirements. The exact qualifications remain beside each lesson.

Before/after illustrations demonstrate a design argument, not a controlled
experiment. Some supplied examples change multiple variables or even content.
Extract the mechanism and limitations; do not turn an author's checkmark into
measured proof that a treatment improves this product.

Historical platform, security, performance, and numeric prescriptions require
current authoritative verification. The book named Bottom Navigation does not
necessarily mean an iOS tab bar. Treat dated examples as illustrations of reasoning,
not implementation requirements. Specific limitations live beside each source card.

Operational templates, routing, confidence categories, and review thresholds are
this skill's synthesis, not quotations or claims that all authors prescribe them.
Only independently supported lessons belong here. Product preferences stay in
the relevant project's memory.
