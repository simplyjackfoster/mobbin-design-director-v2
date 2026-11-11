# Dashboards that support a decision

Use for monitoring dashboards, KPI/metric cards, analytical overviews, quantitative
comparisons and chart-heavy screens. For a scoped chart or copy fix, inspect the
affected meaning and behavior; do not require a metric audit or redesign of the
whole product. Pair with [IA](information-architecture.md) for content/retrieval
structure, [flows](flows.md) for actions, and [visual direction](visual.md) for craft.

This workflow adapts Stephen Few's [Information Dashboard Design](sources/dashboard-design.md),
first edition (2006). The source dossier distinguishes the author's arguments from
our implementation extensions. Historical product examples, perceptual limits,
colors, fonts, timing and testing prescriptions are not current platform standards.
Read only relevant source cards, retrieved with `scripts/coverage.py`; do not load
the entire book dossier or invent a dashboard-specific requirement for every UI.

Retrieve DD-01–08 for monitoring and metric context, DD-09–20 for perception and
chart encodings, and DD-21–28 for assembled layouts, drill-down and evaluation.
For example, `scripts/coverage.py show DD-04 DD-15 DD-17` retrieves metric context,
bullet-graph comparisons and miniature trends.

## Establish what must be noticed, understood and done

Name the audience, decision, viewing conditions, and action after a finding.
Distinguish strategic monitoring, analytical exploration, and operational response;
one product may serve several, but each view needs a clear job. Set refresh needs
from the decision and actual data pipeline, not the word “dashboard.” A daily source
cannot become real-time by animating its display.

Identify the comparisons needed at the same time: actual versus target, current
versus prior, changes over time, differences among entities, distribution or
relationships. Choose the question before a gauge, card grid or chart type.
Reserve attention for actionable exceptions while retaining enough normal context
to interpret them. An aggregate can hide a consequential subgroup or distribution.
Do not remove required context merely to lower the visible item count.

For a research/specification task, return a recommendation and the smallest useful
metric/display contract. Reuse a table instead of repeating the same decisions in
separate long sections. State unresolved definitions and dependencies plainly.

## Define the measures before drawing their status

For consequential metrics, establish the following from project evidence or label
it unresolved. A compact table can cover several metrics; not every field needs to
be displayed directly, but the user must be able to interpret the value correctly.

| Contract | Resolve and verify |
|---|---|
| Meaning | What event/entity is counted, population, inclusion/exclusion, aggregation and owner? |
| Measure | Unit, currency, numerator/denominator where applicable, cumulative versus interval, signed direction and precision? |
| Time and scope | Period, time zone, filter scope, partial-period status, source timestamp and refresh cadence? |
| Comparison | Target, baseline or reference distribution; same definition, unit, cohort and comparable period? |
| Status | Who defined ranges/thresholds, what makes higher/lower desirable, and what action follows? |
| Missing/uncertain state | Zero, absent, not applicable, estimated, stale, partial and failed data distinguished? |
| Evidence | Source/query definition, available fields, dependencies and an independently checkable example? |

These detailed contracts are our implementation extension of the book's context,
measure-selection and comparison arguments. Never infer thresholds or “good” from
an upward arrow. Separate absolute difference, percentage-point change and relative
percent change. Do not average subgroup rates without the appropriate denominators,
combine currencies without an explicit conversion basis, or compare a partial
current period with a complete prior period as if equivalent. If normalization is
useful, disclose the basis and preserve material magnitude somewhere accessible.

Summarize at the precision required for the decision, with access to exact values
when needed. Rounding must not reverse a meaningful ordering, hide a threshold
crossing or misstate a total. A missing value is not zero, and an absent series must
not disappear silently from a displayed total. If source freshness or completeness
is unknown, show that uncertainty rather than treating the last received value as
current. Do not expose private source/engineering details just to describe data.

## Choose the encoding for the actual question

| Question | Starting choice | Keep honest |
|---|---|---|
| Exact lookup or mixed units | Aligned table/text with explicit labels and units | Keep related fields together; charts can accompany tables when patterns matter. |
| Compare/rank magnitudes | Bars or dots on an interpretable shared scale | Length-encoded bars need a meaningful zero baseline; label units and direction. |
| Follow change over time | Line graph; sparkline for compact context | Preserve chronological order and gaps; define time span and scale. A sparkline alone may not show magnitude. |
| Actual versus target and meaningful ranges | Bullet graph or compact bar/dot plus reference | Label actual and target, use defensible ranges and desirability; do not invent poor/good bands. |
| Part-to-whole | Stacked bar or another justified composition | Check that parts form the intended whole; many slices or unrelated totals defeat the comparison. |
| Distribution or relationship | Distribution view or scatterplot appropriate to data | A mean alone can conceal variation; an association does not establish causation. |
| Geographic/spatial pattern | Map or plan when location matters to the decision | Do not use a map merely because locations exist; region size is not the measured quantity. |

These are starting choices, not a chart catalog or absolute bans. Prefer encodings
that make the required comparison easy. Length/position generally supports precise
comparison better than decorative area, angle or three-dimensional perspective.
Do not impose a universal no-pie/no-gauge rule; name the actual cost and a stronger
alternative for the task. Preserve a specialized familiar instrument when its
meaning and use justify it.

Connecting lines need meaningful continuity; a cumulative curve over ordered
categories can be valid, while an arbitrary line across unrelated categories
implies a relationship that is absent. Stacked segments without a common baseline
make fine component comparison difficult. Define distribution/box-plot conventions
explicitly, including population, sample count and what whiskers/outliers represent.

Use comparable axes for panels intended to compare magnitudes. Independently scaled
sparklines can reveal each series' shape, but must not imply equal amplitude or
cross-series magnitude; make the scale distinction clear. A deliberately narrowed
line or point scale can reveal small changes if the range is explicit; a truncated
bar still misrepresents length. Mark negative values and the meaningful origin.
Dual axes can manufacture an apparent relationship through arbitrary scaling:
prefer aligned panels or an explicitly defined normalization unless the task and
clear axis association justify another treatment. Do not infer correlation from
line steepness, imply causality from co-movement, or describe a median as a range's
midpoint. Review unusual chart types against the data and question rather than the
prestige of the reference.

## Compose an overview without sacrificing legibility

Group by meaningful function/entity and actual use, not the shape of the widgets.
Co-locate information that must be compared and align it where comparison benefits.
Separate unrelated measures so proximity does not imply a false relationship.
Use restrained consistent encoding: same meanings keep the same visual treatment;
meaningful differences should be distinguishable. Use spacing, headings and
alignment before heavy panels, borders or repeated decoration when they suffice.

Reduce visual noise without removing interpretive support. Axis labels, reference
lines, units, legends, error/uncertainty cues, accessible focus and controls may be
essential even when they are not data marks. Do not optimize a literal data-ink
ratio or copy faint text/gridlines that fail the project's contrast requirements.
Brand character may remain; show which element competes with task information
before recommending removal. Use current [web](web.md)/[iOS](ios.md) guidance for
implementation rather than book-era pixel sizes, font families or color recipes.

Few's single-screen dashboard definition protects concurrent monitoring and
comparison. Apply that purpose to the actual viewport: prioritize a coherent
summary and keep critical comparison groups together; disclose detail through
intentional routes. Do not shrink text, disable scrolling, defeat text enlargement,
or hide important exceptions to force desktop content onto an iPhone. Scrolling or
separate views can suit independent tasks; avoid splitting interdependent evidence
across tabs merely to fit it. Keep an accessible text/table route where the chart
cannot convey the needed meaning to everyone, and test it on the actual platform.

## Make exceptions, updates and drill-down trustworthy

Use a small, deliberate emphasis hierarchy. Strong color, size, contrast or motion
should communicate priority, not decorate every widget. Add text, shape, position
or another dependable channel for color-coded states. A grayscale/color-vision
check can reveal a failure but does not prove accessibility or screen-reader use.
Never make a red/green lamp the only source of meaning.

For monitoring, specify the difference between a metric threshold, a missing/stale
signal, and a service failure. A blank feed must not produce an all-clear state.
If alerts are in scope, define trigger/clear behavior, severity, ownership and next
action from real requirements; state unavailable notification/acknowledgment support.
Do not assume blinking, audio or an exact alert-count limit is appropriate. Preserve
attention and user control, with reduced-motion and nonvisual equivalents where
needed. Acknowledgment is not resolution. These state/action rules extend the book
and must fit the actual product.

Keep recurring monitoring locations dependable while changing emphasis for new
exceptions. An explicitly ranked exception queue may reorder; avoid arbitrary
whole-dashboard rearrangement on refresh, especially during interaction.

Make the overview a useful entry to investigation. Link a summary to the relevant
entity/detail with its time range, filters, selected item and comparison context.
Back should restore the useful monitoring state; specify what refresh changes and
avoid stale navigation responses replacing newer choices. Chart interactions need
keyboard/touch/assistive access as relevant; hover-only tooltips cannot carry the
only values, definitions or actions. Do not claim a live integration from a mock
chart or promise drill-down into data the system does not hold.

## Check the realized question, not just its appearance

Use representative data and consequential counterexamples: long labels, extremes,
negative/zero values, missing/stale/partial data, no exceptions, multiple exceptions,
and changed filters when relevant. Verify calculations and aggregation against
known examples; inspect scales, units, ordering, thresholds, scope and refresh
labels in the rendered result. A formula check cannot prove that the chart tells
the truth, and a polished screenshot cannot prove its data or interaction.

For actual implementation, exercise refresh/failure, filter/detail/return and
accessible input at supported viewport/text sizes. For a design-only request,
review the proposed contract and mark runtime checks as future work. For a meaningful
comparison, hold data, question and conditions constant; changing the numbers as
well as the encoding cannot isolate an effect of visual design.

When participant work is authorized, use realistic neutral tasks: notice what
needs attention, interpret its context, compare relevant values and choose a next
action. Record initial unaided interpretation before any instruction; coached
feedback answers a different question. Prototype fidelity should fit the question,
and competing designs can be compared when that is useful. Agent walkthroughs and
book critiques are expert assessments, not measured evidence of faster or better
user decisions. Preserve these limits in the [review](review.md) and
[design packet](../templates/design-packet.md).
