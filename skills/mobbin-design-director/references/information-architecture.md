# Make information findable and understandable

Use for a new or revised content structure, labels, navigation, search, filters,
or an experience spanning channels. Pair with [flows](flows.md) for actions and
state transitions. Start with the affected decision; an approved label correction
or isolated visual change needs no inventory, taxonomy project, or research gate.
Keep the recommendation compact: state the decision, its critical dependencies,
and the smallest useful contract/checks. Reuse shared tables rather than restating
the same decision in the model, behavior specification, and validation plan.
These procedures adapt [Information Architecture, fourth edition](sources/information-architecture.md);
source cards explain mechanisms and limits. Normal use needs no source PDF.

Retrieve the relevant cards with `scripts/coverage.py`: IA-01–05 for information
needs and semantic context; IA-06–10 for organization and labels; IA-11–22 for
navigation, retrieval and vocabulary; IA-23–32 for research and delivery. For
example, `show IA-13 IA-17 IA-22` opens search capability, recovery, and facets.

## Frame the information problem

Connect three kinds of evidence: **context** (purpose, ownership, constraints),
**content** (actual objects, attributes, relationships, volume and condition), and
**users** (goals, vocabulary, prior knowledge and conditions of use). Mark missing
evidence as hypotheses. Organizational ownership is a constraint to accommodate,
not automatically the user's navigation model.

Identify the relevant need; several can occur in one session:

| Need | Design consequence | Concrete check |
|---|---|---|
| Known item or answer | Recognizable names, identifiers, aliases and direct paths | Can the specified item be retrieved using the words people actually have? |
| Exploration and learning | Useful groups, context, related material and progressive refinement | Can a person unfamiliar with the vocabulary discover a meaningful next path? |
| Comprehensive coverage | Explicit corpus/scope, informative results and appropriate retrieval coverage | Can the person judge what was searched and what remains excluded or unknown? |
| Re-finding | Stable identity, context and a dependable route back | Can a returning person reach the same object and understand its current state? |

Do not reduce these to fixed persona types or force everyone through a search box.
People can switch between searching, browsing, asking, and following new clues.
Completion of a single happy path does not establish findability or understanding.

## Build from real content in both directions

Inspect a representative cross-section before choosing containers: frequent and
rare types, long or ambiguous names, missing fields, duplicates, restricted or
outdated items, and items that fit multiple categories. Record what the sample
misses. For large collections, combine breadth with deeper checks of consequential
areas; do not claim a sampled audit is exhaustive.

Work top-down from purposes and destinations **and** bottom-up from content
attributes and relationships. Name content objects separately from pages or
components. A record might appear in a list, search results, a detail view and a
notification while retaining one identity. Define the attributes people need to
choose and understand it, meaningful relations, required versus optional fields,
and the authoritative source of each. A field visible in a mockup is not evidence
that the backend stores, indexes, or maintains it.

Test a direct entry into detail, not only a homepage journey. Show what the object
is, its relevant context and relationships, useful next actions, and a route to the
broader collection. Across channels preserve meanings and object relationships;
adapt priorities and navigation controls to channel tasks and platform conventions.

## Choose organization and vocabulary deliberately

Distinguish the **scheme** (the basis for grouping: topic, task, audience, time,
place, alphabet) from the **structure** (hierarchy, database relationships, links).
Use exact schemes when people know the value; use interpretive groupings when they
need to explore. Keep each visible grouping understandable. Mixed schemes can
coexist in clearly separated routes; an undifferentiated list of departments,
formats, topics, and actions makes users guess the organizing rule.

Check category overlap, ambiguous membership, balance, and expansion with actual
items. A polyhierarchy may give an item several legitimate parents without copying
it into separate records. Do not impose seven items, three clicks, or a fixed tree
depth. Broader menus can improve visibility when their labels are meaningful;
narrow menus can create repeated guessing. Evaluate the actual task and content.

Treat labels as a system. Check navigation terms, headings, contextual links,
result titles, index terms, and destination content together. Match granularity,
syntax, meaning, and user vocabulary. A label should predict its destination or
action; an isolated attractive word is insufficient. Preserve approved language
unless changing it is in scope, and distinguish a navigation rename from a domain
concept rename that affects content, search, links, or other channels.

For vocabulary-sensitive work, use a small table rather than an unbounded glossary:

| Concept / stable ID | Preferred label and scope | Alternate terms | Broader / narrower / related | Evidence / owner |
|---|---|---|---|---|
| Actual domain concept | Meaning and boundaries | Genuine equivalent user terms | Distinguish hierarchy from association | Source or hypothesis; accountable maintainer |

Do not treat a competitor name, adjacent concept, or broader/narrower term as an
exact synonym merely to increase hits. Disambiguate homonyms. Localized labels may
need separate equivalents and cultural context, not word-for-word translation.

## Design navigation, search, and metadata together

Choose relevant global, local, and contextual navigation. Supplement with a site
map, index, guide, or other route only when it serves the information need. Make
current location, scope, and destinations comprehensible. Breadcrumbs represent
an information relationship, not necessarily browser history. Preserve meaningful
Back/deep-link behavior using the actual platform path.

Before proposing search, establish that the collection and task warrant it and
that usable content, indexing, and ongoing support exist. Search complements
browsing; it cannot repair missing content or incoherent structure by itself.
It can still be a useful interim route across fragmented collections when a
structural repair is not currently feasible; state the remaining limits.
For search-heavy tasks, define a compact retrieval contract:

- **Corpus and scope:** included objects, fields, formats, permissions, freshness,
  excluded areas, and whether a section search differs from global search.
- **Query interpretation:** terms, identifiers, spelling, ambiguity and justified
  synonyms; distinguish proposed behavior from available backend capabilities.
- **Results:** relevant identifying/context fields, grouping, sorting versus ranking,
  result limits, partial/loading states, and meaningful query/scope feedback.
- **Refinement and recovery:** visible active constraints, intentional combination
  rules, ways to broaden or remove filters, too many results and no-result paths.
  Preserve enough context to revise a query or return from a result.
  Distinguish a successful query with no matches from a service or index failure;
  offer recovery appropriate to the actual condition.
- **Evidence:** representative real queries and expected relevant items, observed
  failures, untested cases, and service/data dependencies.

Choose facets from useful independent dimensions that the content actually
supports. Specify single/multiple selection, within/across-facet combination,
missing values, changing counts and zero combinations when consequential. Counts
must reflect the stated scope and actual data. Hidden or sparse metadata can make
an attractive filter misleading; acknowledge the gap or choose a supported route.
Do not invent search-engine behavior to make a prototype appear complete.

Match ranking and result density to the need. A known-item task can favor precise
matches; exploratory or comprehensive work may need broader recall and context.
Precision is the share of retrieved items judged relevant; recall is the share of
all relevant items retrieved. Report a recall measurement only with a defensible
reference set. These often trade off, but improving both is possible. A low result
count, click rate, or polished results page alone proves neither quality nor
completeness. Validate authorization and freshness claims with the actual system.
If saving is in scope, distinguish saved items from a saved query whose results can
change. Identify paid placement separately from relevance or popularity signals.

## Validate the question, then make the handoff buildable

Use a method suited to the uncertainty; do not perform every method by default:

| Question | Useful evidence | Limit |
|---|---|---|
| How do people name and group these items? | Authorized participant card sorting, vocabulary elicitation, existing inquiries/logs | A grouping exercise is input to a structure, not proof of navigation success. |
| Can people find a destination under the proposed structure? | Neutral task-based structure testing; a text-only tree when isolating hierarchy/labels | Adapts the book's stripped-down hierarchy testing; a tree test omits visual and interaction cues. |
| Do content and metadata support the design? | Sampled inventory, content analysis, schema/index inspection | Record sampling coverage; screenshots do not establish data completeness. |
| Can users navigate and refine in the realized interface? | Task-based usability evaluation; runtime checks for actual state and retrieval behavior | Agent walkthroughs predict user risks; they are not participant findings. |
| What happens in ongoing use? | Authorized logs, queries, support evidence, longitudinal observation | Logs show recorded behavior, not motives or all unmet needs. |

For consequential architecture changes, connect a finding to a design decision,
content/engineering dependency, owner, and verification criterion. Keep the needed
artifacts in the [design packet](../templates/design-packet.md): a structural map
for relationships, a wireflow for transitions, a wireframe for page requirements,
and a content model for reusable fields/relations. Choose only what the team needs;
none of these artifacts replaces the others or proves implementation.

When migration is in scope, map old content/identifiers to new destinations,
including splits, merges, retirement, and unmapped items. Define who supplies and
checks missing metadata, maintains labels, and handles future additions. Preserve
useful links or specify redirects where supported. Do not delete, rename production
objects, publish, or recruit participants merely because an IA recommendation
calls for it; the user's task and authorization still govern execution.

A useful acceptance criterion names an actual information need and evidence:
“Searching the supported alias returns the intended record; narrowing by region
shows the active scope; opening detail and returning restores that query and
filter.” Separate observable behavior from the still-unproven hypothesis that the
labels make sense to intended users. For a spec-only task, inspect the contract and
record runtime/participant checks as future work, not passes.
