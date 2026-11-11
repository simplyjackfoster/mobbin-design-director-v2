# Refactoring UI — source dossier

Adam Wathan and Steve Schoger. Supplied 252-page PDF; edition and publication date
are not stated in this copy and are not inferred from PDF tooling metadata.
The cover and closing signature identify the authors. The [official site](https://refactoringui.com/)
corroborates the title/authors and thematic contents, not the date of this file.
All page references below are one-based **PDF pages, matching printed numbered
body pages** in the inspected examples. See the [coverage manifest](refactoring-ui-coverage.json)
for the file hash, read ranges and actual visual checks.

This is original synthesis, not extracted text or a reproduction of illustrations.
Three bounded readers studied all substantive text, and inspected selected
rendered examples. Static before/after pairs explain craft arguments, not measured
usability improvements. The book is especially useful for concrete visual decisions;
it is not stronger evidence for user needs, accessibility compliance or interaction
behavior than the methods already used by this skill. The [craft workflow](../visual-craft.md)
operationalizes the incremental lessons without requiring the PDF during use.

## What is retained without a duplicate principle

| Source pages | Existing home / distinction |
|---|---|
| 20–27: personality | [Visual direction](../visual.md), ID-06 and PU-12 retain coherent character. Color associations are contextual; p. 24 changes more than radius, so it cannot isolate its effect. |
| 36–41, 60–62: hierarchy and actions | PU-09/17/20 own task rank, fair choices and destructive safety. RU-03/04 add concrete rebalancing and semantic-versus-visual distinctions. |
| 66–75, 96–99: space and grouping | PU-08/10 own relationships. RU-02/05 add bounded comparisons and content-led responsive proportions. |
| 108–135: font, baseline, measure, leading, tracking | PU-10/12/13 own the general checks. RU-06 adds role gaps and actual computed-size diagnosis. Latin alignment, line length and font popularity are not universal requirements. |
| 138–168: color meaning and accessibility | PU-04–06 own contrast, semantic states and non-hue meaning. RU-07/08 add palette construction and contrast-preserving emphasis changes. |
| 200–207: image purpose and quality | PU-07 owns purpose and representation; RU-10 supplies variable local-background checks. Stock or professional photography is not required for every task. |
| 220–241: ornament, borders, empty states | Existing visual/flow guidance already permits purposeful expression. RU-12 retains the specific component-operation and empty-cause distinctions, not another decoration checklist. |
| 250–252: continued learning | [Research](../research.md) already asks what to retain, improve or reject. Notice an unexpected decision and its mechanism; private reconstruction can teach detail but is not a required workflow, a product copy, or evidence of original behavior. |

## Contextual source cards

### RU-01 — Resolve a useful feature slice before speculative shell styling

- **Trigger:** A new feature is stalled on app chrome or many speculative mockups.
- **Authors’ account:** The authors begin with a concrete capability and its required content/actions, keep initial detail low, and alternate design with implementation to expose constraints early.
- **Rationale / application:** Use a real task slice to inform shell decisions. Keep entry, completion, recovery and shared dependencies visible, then test the risky assumptions in the appropriate medium. Do not represent future functionality as available.
- **Exception / conflict:** This is not a ban on up-front information architecture, journey modeling or approved navigation. Grayscale and paper are optional tools; low fidelity is useful only while it answers the question.
- **Review:** Does the slice complete a useful task, and are consequential cross-feature dependencies still represented?
- **Source / dating:** Part 1, pp. 8–19. The p. 13 grayscale example contains placeholder-only fields; the hierarchy exercise does not endorse that form-label treatment.

### RU-02 — Compare bounded choices in the real component

- **Trigger:** Spacing, sizing or token choices are drifting through nearly indistinguishable adjustments.
- **Authors’ account:** The authors constrain available values, compare noticeably different alternatives, and use coarser steps at larger sizes. They explicitly allow defining systems incrementally.
- **Rationale / application:** Start with nearby existing tokens; compare smaller/larger candidates on identical content, narrow the choice, and introduce a new value only when a real role needs it. This gives a practical decision procedure rather than merely asking for consistency.
- **Exception / conflict:** The sample base size, progression and approximate percentage step are examples, not invariants. Reuse the approved system; do not impose a new grid, prohibit fractional values, or require a complete token library before work begins.
- **Review:** Can the selected value be explained by its role and compared in context, rather than by an arbitrary pixel nudge?
- **Source / dating:** Part 1, pp. 28–33; part 3, pp. 70–75. The p. 73 sample itself does not maintain a strict 25% minimum step.

### RU-03 — Rebalance competing visual weight before enlarging the focus

- **Trigger:** The main task loses attention despite large type, or icons and surfaces overpower adjacent content.
- **Authors’ account:** The authors vary weight and contrast as well as size, reduce competing emphasis, and balance the visual mass of symbols and text. Removing a surrounding fill can strengthen foreground content without changing it.
- **Rationale / application:** Try quieter inactive siblings, surfaces or decorative strokes before making the focal item bigger. Judge icons optically beside labels, not only by bounding boxes; choose a lighter icon variant or strengthen adjacent text when appropriate.
- **Exception / conflict:** Supporting content still needs contrast, readability and discoverability. Required control boundaries cannot disappear. The book’s claim that icon weight cannot be changed is not universal; style families and native symbols may provide weight variants.
- **Review:** Does the task become clearer while supporting content and control states remain readable and recognizable?
- **Source / dating:** Part 2, pp. 36–47, 56–59. Figures at 47 and 57 illustrate reduced competition, not deletion of navigation or measured usability gains.

### RU-04 — Separate visual prominence from semantic structure

- **Trigger:** Utility headings, label/value pairs or destructive actions dominate solely because of their type.
- **Authors’ account:** The authors separate HTML heading meaning from default visual size, simplify redundant display labels, and make label-versus-value prominence depend on the lookup task. Their action discussion concerns visual emphasis, not abandonment of semantics.
- **Rationale / application:** Keep meaningful heading structure, accessible names and visible orientation while styling importance for the task. In a specification lookup the label may lead; in a summary the value may lead. Combine redundant display wording only if context still supplies the meaning.
- **Exception / conflict:** Do not remove persistent form labels, units, periods, distinguishing terms or important visible headings. A quiet destructive entry still needs intelligible meaning and risk-appropriate handling; the example confirmation is not mandatory for every reversible action. Equally valid choices must not be hidden.
- **Review:** Can a reader find the relevant field and understand its meaning, and can assistive navigation still identify headings and actions?
- **Source / dating:** Part 2, pp. 48–62, especially the label-first exception at 51 and semantic heading discussion at 54–55.

### RU-05 — Size content constraints and responsive proportions independently

- **Trigger:** A form stretches across a wide viewport, a sidebar changes impractically, or a mobile view is a uniformly shrunk desktop.
- **Authors’ account:** The authors constrain task widths, combine bounded and flexible regions, question blindly proportional grids, and show that heading, body and padding relationships can need different adjustments at different sizes.
- **Rationale / application:** Choose usable content widths, flexible remaining space and reflow points. Inspect intermediate sizes, not just endpoints. Tune display type, control padding and group gaps separately; keep within-group association intact.
- **Exception / conflict:** The grid critique is not a prohibition on CSS Grid. The relative-sizing critique is not a ban on rem/em, fluid layout or user text scaling. Fixed widths must yield to available space and content. Generous whitespace is a starting exploration; dense comparison may be appropriate.
- **Review:** Do the layout and relationships survive intermediate widths, longer strings and enlarged text without shrinking necessary copy or targets?
- **Source / dating:** Part 3, pp. 66–69, 76–99. Figures 86 and 89 expose proportional-column and breakpoint problems; 93 and 95 show independently adjusted relationships.

### RU-06 — Fit typography scales to actual roles and font behavior

- **Trigger:** A geometric type scale skips a needed UI role or nested components produce unintended text sizes.
- **Authors’ account:** The authors prefer a useful constrained scale over mathematical purity, distinguish text/display font use, and relate leading to actual size and line length. Mixed inline sizes often benefit from baseline alignment.
- **Rationale / application:** Judge actual role combinations; add a justified intermediate role instead of forcing a large gap. Inspect actual glyphs, language coverage and computed sizes in nested web components. Existing PU-12–13 own the broader font, leading and line-length guidance.
- **Exception / conflict:** No mandatory font weight count, geometric ratio, integer size, Latin line-length range or system font stack. Parent-relative units can compound but are not prohibited. Optical tracking and tight heading leading must preserve scripts, accents and enlarged text. Quiet links still need persistent discoverability and focus behavior.
- **Review:** Do the chosen roles render as intended with actual fonts, nested contexts, supported languages and text scaling?
- **Source / dating:** Part 4, pp. 102–135. Scale gaps: 104–107; font selection: 108–113; baseline/leading: 118–125; hover suggestion at 127 is not adopted as a default.

### RU-07 — Construct color ramps through real component roles

- **Trigger:** A brand palette lacks useful text, surface, border or interaction-state shades.
- **Authors’ account:** The authors choose useful middle and endpoint colors in components, fill intermediate steps and revise in application. Hue and saturation adjustments can maintain character because equal HSL lightness is not equal apparent brightness.
- **Rationale / application:** Reuse semantic tokens first. When building a missing ramp, test an action midtone and readable light/dark pairings, then add only useful intervening values. Test states and supported appearances. Keep color editing separate from contrast verification.
- **Exception / conflict:** Palette counts and hue-rotation limits are examples. HSL is an editing aid, not a required format or perceptual/compliance model. The brightness formula on pp. 153–154 is not WCAG relative luminance. Do not forbid true black, recolor meaningful categories, or replace approved color tooling.
- **Review:** Do the light, middle and dark choices solve actual component roles across states rather than only form an attractive swatch strip?
- **Source / dating:** Part 5, pp. 138–161, especially construction at 142–151 and brightness/hue reasoning at 152–157.

### RU-08 — Reconcile readable contrast with secondary emphasis

- **Trigger:** A secondary colored badge becomes dominant, or muted text fails on a colored surface.
- **Authors’ account:** The authors demonstrate dark colored text on a pale related fill as an alternative to white text on a strongly saturated fill. They also choose supporting text relative to its colored backdrop instead of assuming neutral grey or transparency will work.
- **Rationale / application:** Change the treatment and surrounding visual mass before reducing readable text contrast. Test final foreground/background combinations, including patterned surfaces and actual compositing. Preserve meaningful status labels and cues beyond hue.
- **Exception / conflict:** The p. 162 approximation of an 18px large-text boundary is inaccurate. WCAG 2.2 SC 1.4.3 uses 18pt regular or 14pt bold (or equivalent); apply the project’s current requirements and exceptions. Sample ratios and hue shifts are not reusable guarantees. Lightness differences can be useful cues, but the chart illustration does not establish accessible category mapping.
- **Review:** Can secondary information remain readable while yielding attention to the primary task, with meaningful distinctions independently understandable?
- **Source / dating:** Part 2, pp. 42–45; part 5, pp. 162–168. Current correction checked 2026-11-11 against [W3C contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html); [W3C use-of-color guidance](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) qualifies lightness as an additional distinction in some contexts.

### RU-09 — Make visual depth agree with layer order and state

- **Trigger:** A shadow looks muddy or arbitrary, or raised/inset styling conflicts with interaction state.
- **Authors’ account:** The authors explain coherent light direction, raised and recessed surfaces, state-dependent elevation, and two shadow roles: a soft cast shadow and tighter contact shadow whose contribution weakens with separation. Color offsets and overlap offer other layer cues.
- **Rationale / application:** Decide layer relationships first, then tune the light, cast/contact contribution or flat offset. A dragged item and pressed control should express coherent states. Inspect occlusion and surrounding composition rather than styling each card independently.
- **Exception / conflict:** No mandatory light direction, five-shadow scale or photorealistic rendering. Preserve native materials and project conventions. Depth does not supply accessible state semantics or prove behavior; overlap must not obscure controls, focus or essential content.
- **Review:** Do visual elevation and actual state agree, with coherent layer order and unobscured content in supported appearances?
- **Source / dating:** Part 6, pp. 172–197; state/elevation at 180–185, cast/contact mechanics at 186–189, alternative depth at 190–197.

### RU-10 — Validate image text contrast across local variation

- **Trigger:** Text overlays a photograph, a variable crop or user imagery.
- **Authors’ account:** The authors show that competing bright/dark regions make text unpredictable and compare overlays, image adjustments, colorization and subtle text support.
- **Rationale / application:** Test the complete text region against representative bright, dark and busy crops, including responsive wrapping. Prefer a dependable local surface or scrim where a uniform tint fails. This is a targeted stress check extending PU-07, not another general image-purpose rule.
- **Exception / conflict:** An overlay, global tint, glow or shadow is only a candidate treatment, not contrast proof. Preserve faithful evidence/product imagery; do not recolor it just to match a brand. Decorative photography cannot substitute for explanatory content.
- **Review:** Is text readable over the actual worst relevant crop and wrapping, including missing or changed images?
- **Source / dating:** Part 7, pp. 200–207, especially local contrast treatments at 202–207.

### RU-11 — Choose image detail and framing for actual rendered use

- **Trigger:** An optical asset-size mismatch makes a sharp vector look coarse when enlarged, a screenshot loses detail, or an upload crop loses meaning or breaks visual framing.
- **Authors’ account:** The authors distinguish intended optical size from technical scalability, suggest legible screenshot crops or simplified illustrations, and normalize uploaded image framing with attention to aspect ratio and edge separation.
- **Rationale / application:** Pick an asset whose detail works at the rendered size; inspect it there. For uncontrolled images define crop/contain behavior, focal preservation and subtle boundary treatment. Test tall/wide content and backgrounds matching the UI. Missing-image checks and fallback behavior are our operational extension.
- **Exception / conflict:** Do not reduce hit targets to match small glyphs, crop meaningful logos/diagrams indiscriminately, or universally convert semantic images to CSS backgrounds. An illustrative reconstruction is not a capture of shipped behavior. Use size-aware scalable families where they fit; the book’s pixel examples are not limits.
- **Review:** Do key details and subjects survive the actual display size and varied uploads, with honest representation and appropriate fallback?
- **Source / dating:** Part 7, pp. 208–217; intended size at 208–213 and upload framing/edge examples at 214–217.

### RU-12 — Refine component composition without losing its task contract

- **Trigger:** Default menus, table cells with independent sorting, or empty-state fixtures restrict a useful composition.
- **Authors’ account:** The authors enrich existing details, use selective accents and grouping alternatives, design first-use emptiness, and reorganize menu/table/selection content. Their combined table-cell example explicitly depends on whether fields need independent sorting.
- **Rationale / application:** Improve an existing useful element before accumulating decoration. Combine fields only when comparison, headers and independent operations remain clear. Design the genuine first-use state; distinguish it from zero filtered results, loading, permission denial and failure. Keep recovery controls where needed.
- **Exception / conflict:** Custom appearance must retain keyboard, focus, selection and assistive behavior. A rich navigation popover is not automatically an ARIA menu. Do not hide filters needed to recover results or invite creation without permission. Border removal is optional when other cues preserve boundaries and grouping.
- **Review:** Does the refined component retain its sorting/comparison/selection contract, and does each empty cause offer an appropriate next action?
- **Source / dating:** Part 8, pp. 220–247; first use at 234–237, border alternatives at 238–241, structured components at 242–247 (sorting qualification at 244).

