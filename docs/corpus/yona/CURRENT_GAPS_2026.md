# Yona Current Gap Ledger — 2026-09-27

## 2026-09-27 implementation closure

The fourteen gaps below were the result of the Chapter 1/2/14/47 audit. They are now executable at the Cuspell expression-language level:

- G1: quoted Sign literals, Name, That, and They provide explicit contextual naming/anaphoric forms. This does **not** mean the checker automatically resolves English pronouns across prose; manual Cuspell translation supplies the intended contextual reference.
- G2: Past, Present, Future, Ongoing, Completed, Continue, Whenever, Sometimes, Often, and Rarely cover the identified tense/aspect/frequency distinctions.
- G3: OccurrenceRate, ChangeRate, Increasing, Decreasing, Stable and the Frequency dimension are executable.
- G4: Quantity and EvaluationValue share OrderedValue, so comparison/Between can express ordered evaluation and priority scales when the relevant scale is supplied.
- G5: Requires and SufficientFor are distinct from material If.
- G6: contextual Should provides recommendation/advice weaker than Obligated.
- G7: contextual Almost applies to gradable Property descriptors; objective measured approximation remains ApproxEqual with explicit tolerance.
- G8: Sense plus explicit channels and See/Hear/Smell/Taste, Detected, and NotDetected are executable.
- G9: Transfer is executable.
- G10: Purpose is executable and remains distinct from Use/DesignedFor.
- G11: Ratio is executable and distinct from Divide.
- G12: contextual fixed-size Partition produces nested typed collections; because grouping is underdetermined it is not a free magical selector.
- G13: UnknownValueOf and UnavailableValueOf explicitly distinguish missing knowledge/access from absence.
- G14: DistributionOf, LocalDensity, TotalAmount, and Redistribute provide the generic spatial resource-field abstraction.

Quantity value-domain enforcement is also executable: absolute nonnegative attributes/counts reject invalid static values, while signed deltas such as ChangeBy remain legal and dynamic constraints stay attached to the AST.

Additional settled prose-only core gaps closed during the same pass include ordered Sequence<T> values with First/Last, DirectPart, Group/Members, Because, Between, causation, information/sign relations, desire/planning/expectation/inference, and a broad objective space/time constructor layer.

**Next corpus rule:** do not add new grammar speculatively. Re-test Yona; any new structural failure becomes the next gap. Ordinary nouns/setting concepts are classified as lexicon/world-package work unless they expose a missing reusable semantic family.


This ledger consolidates:

- Chapter 1 current-language re-audit;
- Chapter 14 current-language re-audit;
- new Chapter 2 pass;
- new Chapter 47 "How Mana Works" pass.

The purpose is to distinguish **language architecture** from ordinary **lexicon/world data**.

## Tier 1 — repeated structural gaps

These recur across more than one chapter and should be addressed before claiming translation-complete Cuspell.

### G1 — durable discourse reference and proper names

Need:

- introduce a named discourse entity;
- retain it across sentences/paragraphs/chapters;
- resolve pronouns and definite descriptions by salience/constraints;
- preserve speaker/addressee context in dialogue;
- keep this ordinary-language mechanism separate from magical free target resolution.

Pressure:
- very strong in Chapters 1 and 2.

### G2 — aspect and graded frequency

Need compact semantics for:

- ongoing/progressive;
- continue/still;
- already/yet;
- sometimes/often/rarely;
- repeated-but-not-habitual and "kept doing".

Pressure:
- Chapter 1 strongly;
- Chapters 2/47 reinforce event continuity.

### G3 — generic rate/trend/fluctuation values

Need executable forms along the lines of:

- Rate(value/event, interval);
- ChangeRate(attribute, subject, interval);
- Increasing(value-function, interval);
- Decreasing(...);
- Stable(...);
- Fluctuating(...).

Pressure:
- Chapter 1 spawn/odor/resource trends;
- Chapter 14 digestion efficiency;
- Chapter 47 definitions of stable/volatile mana behavior.

This is one of the clearest repeated gaps.

### G4 — ordered evaluation / quality / priority

Current Evaluate produces EvaluationValue, but More/Less compare Quantities.

Need either:

- EvaluationValue to be explicitly ordered; or
- Evaluate to return a typed scalar Quantity on a declared evaluation scale.

This enables:

- better/worse;
- best time;
- more important;
- higher priority;
- better option quality.

Pressure:
- Chapters 1, 2, and 47.

### G5 — prerequisite / enabling relation

Need a relation distinct from material If:

- completion of X enables/unlocks Y;
- X is prerequisite for Y;
- capability/state unavailable until X.

Pressure:
- Chapter 1 System unlocks;
- Chapter 2 Quest completion;
- Chapter 47 affinities/upgrade constraints.

### G6 — recommendation/advice modality

Current Obligated is too strong for ordinary "should", advice, or recommendation.

Need a weaker modality such as Recommended/Advisable or a clearly specified Should relation.

Pressure:
- Chapter 1;
- Chapter 47 repeatedly.

### G7 — generic near-threshold Almost

ApproxEqual handles measured quantities with explicit tolerance, but ordinary language needs:

- almost hungry;
- nearly tired;
- near control limit;
- approximately satisfying a qualitative threshold.

Pressure:
- Chapters 1, 2, 14, 47.

## Tier 2 — useful reusable semantic molecules

These are important, but they fit the current architecture rather than changing it.

### G8 — Sense / perception family

Need a canonical structure separating:

- sensory event/channel;
- produced Information;
- detected value/source;
- failure to detect;
- objective zero/absence.

Likely roots/channels:
Sense, See, Hear, Smell, Taste, ManaSense.

Pressure:
- all four chapters.

### G9 — Transfer / Flow

A reusable Process:

Transfer(resource, amount, source, destination)

or equivalent.

Pressure:
- Chapter 14 mana movement/absorption;
- Chapter 47 mana redistribution/reabsorption.

### G10 — Purpose / goal relation

Need clean event-purpose semantics distinct from merely having an intention.

Pressure:
- Chapter 1 and ordinary action descriptions.

### G11 — executable Ratio

Ratio is already in the written measurement design but not yet executable in the reference lexicon.

Pressure:
- Chapter 47 damage composition/proportions;
- future mixture/color/resource examples.

## Tier 3 — genuinely new findings from Chapter 2

### G12 — fixed-size collection partition

Need to partition a collection into subcollections, e.g.:

Partition(crew, size=2) -> Collection<Collection<Entity>>

This is different from Filter/Each/Collect and should not invent an implicit ordering unless an ordering is supplied.

Use cases:
- "split into pairs";
- teams of N;
- batches/groups.

### G13 — known record with unavailable/unknown field value

Need a way for Information to assert:

- entity/type is known;
- a field exists;
- its value is unknown/unreadable/unavailable.

This is different from asking an open question and different from asserting no value.

Chapter 2's displayed unknown level is the motivating example.

## Tier 4 — Yona-specific but architecturally important world abstraction

### G14 — spatial resource Field / Distribution

Need a representation for a quantity/resource varying over Region/space:

- mana density at different points;
- center depleted while edge is dense;
- ambient field across air/meat/construct;
- potentially temperature/light/etc. fields later.

This is the main surviving Chapter 14 magic-model gap and is reinforced by Chapter 47.

It should probably be a general semantic value, not a Yona-specific rune.

## Lexicon/world work that should NOT be mistaken for grammar gaps

A translation-complete corpus still needs many roots/data packages, but these can be added mechanically once their semantic family is known:

### Ordinary prose

- names and social roles;
- family/occupation terms;
- food and household objects;
- emotions;
- anatomy;
- travel/maritime objects;
- weapons;
- animals/monsters;
- buildings/places;
- common actions such as climb, grab, dodge, listen, smell, bite.

### Yona game/system ontology

- System / Quest;
- Skill / Class / Species / Trait / Affinity;
- Level / Tier / Proficiency;
- Unlock / Upgrade / Evolve;
- specific Skills and spell categories.

### Yona mana ontology

Scalar AttributeDescriptors can encode, without new grammar:

- Stability;
- Volatility;
- Potency;
- Flow;
- Resilience;
- Flexibility;
- Thickness;
- ManaAmount;
- capability/performance measures.

## What the four-chapter audit says

The key result is **convergence**.

Chapter 1 historically discovered many foundational defects. Most are now resolved.

Chapter 14's biggest old defects around BeforeValue, Preserve, dimensional density arithmetic, ShapeLike versus Kind identity, Touch versus Joined, and Control are now executable.

Chapter 2 introduced only a small number of genuinely new structural needs, with fixed-size collection partition being the clearest.

Chapter 47 describes a fairly detailed foreign magic system, yet mostly reuses gaps already found by Chapters 1/14 rather than requiring a new grammar architecture.

Therefore the next language-completeness work should focus on G1-G14 rather than broad speculative expansion.
