# Concrete visual craft

Use when a direction is chosen but the result needs stronger hierarchy, better
proportions, or more deliberate type, color, depth and imagery. Start from
[visual direction](visual.md), real content and the existing system. Choose the
lever causing the problem; this is not an obligatory redesign checklist.
[Refactoring UI](sources/refactoring-ui.md) supplies practical techniques, with
page citations and exceptions in RU-01–12. The techniques are design hypotheses,
not evidence of user performance or permission to replace approved decisions.

## Work at a useful scale

For a new feature, resolve a useful slice before committing to speculative shell
styling; keep its entry, completion and dependencies visible ([RU-01](sources/refactoring-ui.md),
pp. 8–19). Work in low detail only while it helps decide structure. Grayscale is
an optional hierarchy diagnostic, not a mandatory phase or proof of accessibility.

Reuse existing tokens first. When a gap genuinely exists, compare meaningfully
different candidate values, narrow the interval, and keep a small role-based set.
A systematic scale reduces arbitrary choices; it does not require a fixed ratio,
a four-pixel grid, or a large new token library. Test the values in components
before treating them as settled ([RU-02](sources/refactoring-ui.md), pp. 28–33, 70–75).

## Fix competition before adding emphasis

After ranking decision content, try reducing the weight, contrast, fill or border
of competing elements before enlarging the main item. A quiet surrounding surface
can make the same foreground content more apparent. Compare icon and text optical
weight: a large filled symbol can overpower a small label even at the same color.
Try a lighter symbol treatment or stronger adjacent text while retaining required
contrast and target size ([RU-03](sources/refactoring-ui.md), pp. 36–47, 56–59).

Separate visual importance from document structure and action meaning. Keep
semantic headings even when supporting headings look small; preserve accessible
names and meaningful visible labels. Combine a redundant display label with its
value only when the meaning remains clear; emphasize the label when people scan
for a named specification. Preserve the actual context, language and
reading order. Units, reporting periods, ambiguous dates and persistent form labels
are not visual clutter. A quiet destructive entry point still needs an intelligible
label and risk-appropriate recovery/confirmation; severity alone does not make it
the main action ([RU-04](sources/refactoring-ui.md), pp. 48–62; [input](input.md)).

## Fit layout to content, then adapt its proportions

Give a focused task a suitable width; unused viewport width is not a defect.
Wide-screen supporting content may sit beside a constrained form without widening
its fields. Size columns by what they hold rather than forcing every region to
occupy a percentage of a grid. Bound a sidebar or form when useful, let other
regions flex, then reflow when content no longer fits. This critiques blind grid fractions, not CSS Grid itself. Fixed proportions do not
justify fixed clipping ([RU-05](sources/refactoring-ui.md), pp. 76–95).

Do not shrink the entire desktop composition uniformly or disable relative units
and user text scaling. Display headings, body
text, control padding, gutters and columns may need different adjustments. Test
an intermediate width, long strings and enlarged text as well as the endpoints.
Extra whitespace is a useful exploration starting point; expert comparison may
need a denser field. Preserve within/between-group distinctions at every width
([RU-05](sources/refactoring-ui.md), pp. 66–69, 92–99).

## Tune type and color through real roles

Build type roles around actual UI needs. If a mathematical scale skips a needed
size or adds near-duplicates, choose a useful intermediate role instead. Verify
font weights, glyph/language coverage and small-text rendering with real content;
a family’s weight count or popularity is only a selection clue. Reading measure,
leading and alignment work together: longer small-text lines often need more
leading; large short headings can be tighter. Do not convert the book’s sample
sizes or Latin line lengths into universal requirements ([RU-06](sources/refactoring-ui.md),
pp. 102–125, 128–135; existing [PU-12–13](sources/practical-ui.md)).

For a missing palette, select usable middle, light and dark colors from actual
roles—action, quiet surface and readable text—then add only useful intermediate
shades. Test the palette in components and states, not just isolated swatches.
Hue and saturation may need adjustment across a ramp; equal HSL lightness does
not mean equal perceived brightness. Use the project’s color tooling; HSL is one
editing aid, not a required format or contrast test. Semantic naming and supported
appearances remain the system’s responsibility ([RU-07](sources/refactoring-ui.md),
pp. 138–161; [PU-05–06](sources/practical-ui.md)).

When a low-priority badge becomes too dominant after darkening its fill for white
text, try darker colored text on a pale related background. Preserve its readable
label and meaning beyond hue. On a colored surface, choose secondary text against
that actual surface; neutral grey or reduced opacity can look muddy or fail as the
backdrop changes. Measure final combinations under the applicable standard;
priority never excuses unreadability ([RU-08](sources/refactoring-ui.md), pp. 42–45,
162–168). The book’s approximate text-size threshold is qualified in the source
card; it is not a compliance rule.

## Make depth and imagery survive real states

Use depth to explain relationships or interaction states. Keep lighting direction
coherent; a soft broad shadow and a tighter contact shadow can serve different
roles, with less contact contribution as apparent elevation increases. Higher apparent elevation need not mean an arbitrary extra shadow on every
card. Flat color offsets or overlap can also show layers. Check focus rings,
occlusion, clipping and supported appearances; follow native materials where
appropriate ([RU-09](sources/refactoring-ui.md), pp. 172–197).

Text over images needs dependable local contrast across the entire text region,
not an average judgment of the photo. Try a localized scrim, gradient or separate
surface when crops and text wrapping vary; a global tint or text shadow is not a
guarantee. Check bright, dark and busy images, responsive crops and missing-image
states ([RU-10](sources/refactoring-ui.md), pp. 200–207).

Choose assets for their rendered size. An icon designed small may look crude when
inflated; a detailed screenshot may become meaningless when shrunk. Use a suitable
asset, a legible detail crop, or an original simplified illustration that preserves
meaning. Crop photos deliberately but contain logos/diagrams when cropping loses
information. For uploads, define framing, focal treatment and subtle edge contrast
so irregular aspect ratios and background colors remain coherent. Test failures
and fallbacks instead of relying on one curated image ([RU-11](sources/refactoring-ui.md),
pp. 208–217).

## Finish the useful states

Try improving one useful detail before adding decoration everywhere: a list marker,
a status accent, or the internal composition of a repeated row. If borders compete,
compare grouping by space, surface or selective shadow while retaining control
boundaries. An empty state should explain the state and offer the actual first or
recovery action; distinguish first-use emptiness from filtered results, loading, failure and denied
access. Keep filters needed for recovery and offer creation only when permitted.
A menu or table cell can contain structured content when scan order, field headers,
independent sorting, comparison and keyboard behavior survive ([RU-12](sources/refactoring-ui.md), pp. 220–247).

After each consequential refinement, inspect the real render and the neighboring
state that could break it. Record the mechanism and tradeoff. A more attractive
screen remains subject to [review](review.md); style counts and agent preference
do not establish task success.
