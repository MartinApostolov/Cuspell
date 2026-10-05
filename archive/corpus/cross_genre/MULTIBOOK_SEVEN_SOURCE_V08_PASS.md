# Checkpoint 125 — Seven-Source Multi-Book Corpus Pressure Pass

_Status: broad post-v0.8 corpus discovery pass_

## Purpose

Checkpoint 124 finished current-reference reconciliation for canonical surface v0.8.

The next requested task is to stress Cuspell against several more books before beginner/glyph work.

This pass uses seven sources total:

1. the existing **Yona [Cat Girl Evolution]** corpus as the previously audited baseline;
2. **Alice's Adventures in Wonderland** — Lewis Carroll;
3. **Treasure Island** — Robert Louis Stevenson;
4. **The Time Machine** — H. G. Wells;
5. **Twenty Thousand Leagues under the Sea** — Jules Verne;
6. **On the Origin of Species** — Charles Darwin;
7. **The Wealth of Nations** — Adam Smith.

The six new sources are public-domain Project Gutenberg texts and were chosen to provide deliberately different pressure rather than six similar novels.

The goal is discovery, not complete line-by-line translation of all six books in one checkpoint. Each new book is sampled at structurally demanding passages, with deeper attention where a passage exposes a possible missing distinction.

## Sources

### Existing baseline

**Yona [Cat Girl Evolution]**, Bedivere the Mad, Royal Road.

Existing repository coverage already reaches numbered Chapters 1–168 plus the 94.5 Sally interlude.

Source index:

https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution

Current historical corpus report:

`archive/corpus/yona/CH01_168_V09_FULL_PUBLISHED_PASS.md`

### New public-domain books

**Alice's Adventures in Wonderland**, Lewis Carroll.

Project Gutenberg:

https://www.gutenberg.org/ebooks/11

Sampled pressure:

- Chapter I opening paragraph;
- Chapter V Caterpillar identity/size conversation.

**Treasure Island**, Robert Louis Stevenson.

Project Gutenberg:

https://www.gutenberg.org/ebooks/120

Sampled pressure:

- Chapter IX/X ship authority and secrecy;
- Chapter XI apple-barrel overhearing/mutiny sequence.

**The Time Machine**, H. G. Wells.

Project Gutenberg:

https://www.gutenberg.org/ebooks/35

Sampled pressure:

- Chapter I fourth-dimension/time discussion;
- the distinction between ordinary spatial motion and claimed movement through Time.

**Twenty Thousand Leagues under the Sea**, Jules Verne.

Project Gutenberg:

https://www.gutenberg.org/ebooks/164

Sampled pressure:

- Part I, Chapter XI instrument/electricity explanation;
- Part I, Chapter XII dimensions, displacement, pressure, diving, steering, and motion.

**On the Origin of Species**, Charles Darwin, first edition.

Project Gutenberg:

https://www.gutenberg.org/ebooks/1228

Sampled pressure:

- Chapter III broad/metaphorical "struggle for existence";
- Chapters IV–V heredity, variation, selection, adaptation, offspring, and population pressure.

**The Wealth of Nations**, Adam Smith.

Project Gutenberg:

https://www.gutenberg.org/ebooks/3300

Sampled pressure:

- Book I, Chapter I division of labour and pin manufacture;
- Book I exchange/barter material and later wage/price comparisons.

## Existing Yona baseline

Yona remains the broadest already-audited fictional baseline:

- first-person narration;
- dialogue;
- combat;
- explicit magic;
- body transformation;
- resource fields;
- progression systems;
- social scenes;
- nested hypothetical reasoning;
- unusual species/body ontology;
- world-specific Skills/Classes/Traits/Titles.

The existing full-published pass found no post-G16 structural gap through Chapter 168.

This pass does not re-copy or re-audit the copyrighted novel chapter by chapter. Current executable regressions and the archived full-published report remain the baseline.

## Alice's Adventures in Wonderland

### A1 — opening: inactivity, book content, internal evaluation

Semantic pressure:

- a person remains seated beside a family member;
- she lacks an activity she wants;
- another person reads a book;
- the book lacks pictures and represented conversation;
- the protagonist internally evaluates the usefulness of such a book.

Current Cuspell has the required architecture:

- persistent spatial relations;
- Want;
- Say/Question/Information;
- Book and Image historical vocabulary;
- Evaluate/Purpose/Use;
- belief/thought-state representation.

The idiom "tired of" in this passage is closer to boredom/dissatisfaction than objective physical fatigue. Translating it literally as low physical energy would be wrong.

The clean semantic rendering is therefore contextual dissatisfaction / Want-to-end-or-change the current activity.

**Classification: PASS-LONG + STYLE-LOSS.**

No Bored/Tired root is added from this idiom alone.

### A2 — Chapter V: unstable identity and repeated size changes

Pressure includes:

- "who are you?" as a context-dependent identity question;
- knowing a previous identity/state but uncertainty about the present;
- repeated bodily size change during one day;
- self-understanding failure;
- conversational requests for explanation.

Current machinery covers:

- Name/reference questions when a naming answer is intended;
- Kind/property questions when classification is intended;
- Know, Believe, Confidence, Understand;
- Change over Extent;
- Happen + TimeInterval;
- Explain/Explains;
- discourse speaker/addressee roles.

An important language property becomes visible here:

> English "who are you?" underspecifies which identity dimension is wanted.

Cuspell intentionally requires the translator to choose whether the question asks for a Name, Kind/role, relation, or some other identity information.

That is not a Cuspell defect; the source utterance is pragmatically underspecified.

The literary idea "I am not myself" is also metaphorical rather than literal Entity non-identity.

**Classification: PASS + SOURCE-AMBIGUOUS + STYLE-LOSS.**

No identity grammar change is justified.

## Treasure Island

### T1 — ship authority, secrecy, mutiny risk

Pressure includes:

- captain/crew institutional roles;
- recognized authority;
- information intentionally kept secret;
- fear of coordinated mutiny;
- plans to change who controls the ship;
- weapons and defended areas.

Current Cuspell already has:

- Captain, Crew, Sailor, Ship, Map, Weapon Old Names;
- Authority;
- Control;
- Plan/Intend;
- Obligated/Permitted;
- Know/Not Know;
- Say/Information;
- Attack/Prevent.

A mutiny can be represented as coordinated crew planning/action against recognized ship authority/control.

The English noun "mutiny" is useful compression, but the sampled material does not show an independent semantic primitive.

It remains a possible historical/world event-category lexicalization if repeated corpus pressure warrants it.

**Classification: PASS-LONG / possible Old Name or event-Kind candidate.**

### T2 — apple-barrel overhearing

The sampled paragraph requires:

- being spatially inside a container;
- another person speaking;
- hearing the speech without being its intended addressee;
- fear;
- intentionally remaining unseen;
- acquiring/holding the information.

All are directly representable.

Canonical semantic sample, using discourse references:

- `Self` = Jim;
- `This` = apple barrel;
- `That` = Silver;
- `ThisInformation` = the relevant speech;
- `ThisInterval` = the scene interval.

Cuspell:

`In Self Extent This.`

`Happen Say That ThisInformation ThisInterval.`

`Happen Sense Self Hearing ThisInformation ThisInterval.`

`Want Self Not Happen Sense That Vision Self.`

`Fear Self That.`

`Know Self ThisInformation.`

This does not attempt to reproduce Stevenson's style. It preserves the sampled paragraph's propositional/event core.

**Classification: PASS.**

## The Time Machine

### TM1 — reported scientific theory

The opening scientific dialogue stresses:

- nested reported speech;
- disagreement;
- explanation;
- dimensional geometry;
- models/representations;
- claims about Time and Space;
- questions challenging a theory.

Speech, belief, confidence, evidence, explanation, and questions are already expressible.

The exact mathematical theory, however, is world/model content.

The current core has intentionally distinct semantic families for:

- spatial Location/Region/CoordinateFrame;
- TimePoint/TimeInterval.

A fictional theory identifying Time with another geometric dimension should therefore be represented by an appropriate world mathematical ontology / Information model rather than by forcing the core semantic types to become identical.

**Classification: PASS for discourse; WORLD for exact four-dimensional geometry.**

### TM2 — time travel

The book's central physical premise requires a world in which one Entity can persist while appearing at very different temporal locations/history states.

Current Cuspell can state:

- temporal ordering;
- event occurrence within intervals;
- before/after;
- identity persistence;
- causes and state changes.

It does not need a universal `MoveThroughTime` root merely because one fictional machine implements time travel.

The execution rule that makes such a transition physically possible belongs to the active world.

**Classification: PASS-LONG + WORLD.**

No time-travel root is added.

## Twenty Thousand Leagues under the Sea

### V1 — instruments and engineering quantities

The Nautilus chapters stress:

- Heat/temperature;
- atmospheric/weather measurements;
- direction/navigation;
- speed/rate;
- depth;
- Length/Volume/Mass/Density;
- machinery and tools;
- causal use of electricity;
- measurement instruments.

Existing Cuspell is unexpectedly strong here:

- Heat;
- Length;
- Volume;
- Mass;
- Density;
- Extent by coordinate-frame axis;
- Rate;
- Direction / CoordinateFrame;
- Move / Rotate;
- Tool and craft vocabulary;
- Use/Purpose/Cause.

Depth remains compositional as third-axis Extent rather than a separate root.

Speed remains a rate of movement/distance rather than a dedicated semantic primitive.

Electricity itself is a physical/world phenomenon and technology resource, not evidence for a new universal grammatical family.

**Classification: PASS-LONG + WORLD/LEXICON.**

### V2 — pressure exposes a real boundary

The diving explanation repeatedly reasons about water pressure as a measurable ordered physical quantity varying with depth.

Current Cuspell does **not** contain:

- a Pressure AttributeDescriptor;
- a Quantity:Pressure dimension;
- a generic mechanism by which a world package can declare a new callable measured AttributeDescriptor with a new Quantity dimension.

This is not merely missing English vocabulary.

Without a pressure semantic dimension, Cuspell cannot state the exact quantitative content of the passage in the same way it can state Length, Mass, Density, Heat, or Volume.

However adding one isolated `Pressure` rune now would be the wrong response.

The broader issue is:

> how world/physics packages introduce additional objective measured attributes and dimensions without bloating the universal rune basis one quantity at a time.

This belongs with the already-deferred concrete-physics/world-execution milestone.

**Classification: DEFERRED STRUCTURAL/PHYSICS GAP.**

Checkpoint 125 records the issue but does not prematurely choose among:

- a universal Pressure root;
- a generalized world-defined AttributeDescriptor registry;
- extensible Quantity dimensions;
- a smaller physical basis from which Pressure can be derived once Force/Area dynamics exist.

This is the strongest genuinely new finding of the pass.

## On the Origin of Species

### D1 — "struggle for existence" is deliberately metaphorical

Darwin explicitly broadens "struggle" to include:

- direct competition;
- environmental dependence;
- reproductive success;
- dependence on other organisms.

This is useful pressure against blindly lexicalizing English words.

One universal `Struggle` Process would actually be less exact than the current semantic basis.

The examples can instead use:

- Requires;
- Life;
- Want;
- Prevent;
- ParentOf;
- Rate;
- Count;
- Cause;
- environmental/world conditions.

**Classification: PASS-LONG.**

Do not add a Struggle root from the metaphor.

### D2 — species, variation, heredity, selection

Pressure includes:

- species/variety categories;
- parent/offspring relations;
- recurring trait similarity;
- variations in Form/other Attributes;
- differential survival/reproduction;
- population-level rates;
- causal explanations over many generations.

Current architecture can express the semantics compositionally:

- world Kinds represent species/taxa;
- Kind inclusion can be stated extensionally with typed quantification rather than requiring a Subkind root;
- ParentOf represents lineage edges;
- Attribute values / Form / ShapeLike represent trait similarity;
- Change represents variation;
- Count/Ratio/Rate/Most/All/Some represent population claims;
- Requires/SufficientFor/Cause/Explains represent scientific dependency/explanation.

"Heredity", "adaptation", and "natural selection" are extremely useful scientific terms, but the sampled prose treats them as theory/world concepts whose internal claims remain expressible.

They may justify scientific historical vocabulary later; they do not yet justify new primitive runes.

**Classification: PASS-LONG + WORLD/LEXICON.**

## The Wealth of Nations

### W1 — division of labour / pin manufacture

Pressure includes:

- workers;
- specialization;
- partitioning a process among people;
- skill/capability;
- machinery as instrument;
- production;
- output per unit time;
- causal claims that specialization changes productivity.

Current Cuspell can decompose this into:

- collections/groups of workers;
- Partition;
- Can;
- Use;
- Purpose;
- Cause;
- Begin Exist for produced artifacts;
- Count;
- Rate;
- More/Less.

A universal `Work` or `Labour` root would not make these truth conditions clearer: different kinds of work are different Events/EventSpecs connected by social/economic context.

The ordinary word may eventually deserve historical lexicalization, but its absence is compression pressure rather than semantic incompleteness.

**Classification: PASS-LONG.**

### W2 — exchange, price, wages

Exchange is already structurally available through Transfer and the historical Give composition.

Core world vocabulary already includes:

- Currency;
- Market;
- Own/Have.

Price/wage claims can be represented as quantities/ratios/transfers under a market/employment world model.

The exact institutional meaning of legal tender, wages, contracts, employment, debt, and market price belongs to world/social ontology.

A primitive `Price` relation is therefore not added from this pass.

**Classification: PASS-LONG + WORLD.**

## Cross-source findings

### No new grammar/type family

Across the six new books, no passage required:

- a new sentence mood;
- a new binder family;
- a new tense/aspect family;
- a new discourse-content type;
- a new generic event-control operator;
- a new semantic root solely to preserve the sampled truth conditions.

This is strong convergence evidence after Yona, Pride and Prejudice, and Frankenstein.

### Compression pressure remains real

The new sources produce useful lexical candidates, especially:

- boredom/tired-of style;
- mutiny;
- work/labour;
- species/taxon terminology;
- heredity;
- adaptation;
- natural selection;
- electricity;
- engineering instruments;
- price/wage vocabulary.

These are not all the same design class.

Most are candidates for:

- historical Old Names;
- typed world event/content Kinds;
- setting/scientific New Names;
- institutional world facts.

They should not be promoted en masse into semantic roots.

### Physical-attribute extensibility is the one real new structural pressure

Verne exposes the clearest current boundary:

the language has several built-in physical AttributeDescriptors, but world packages cannot yet add an arbitrary new measured descriptor/dimension with the same first-class usability.

Pressure is the first concrete example in this pass, but the same future mechanism would matter for other physics quantities such as force, charge, voltage, energy, or acceleration if/when the execution model needs them.

This finding should be carried into the concrete-physics/world-execution milestone rather than solved piecemeal during vocabulary work.

## Executable regressions

Checkpoint 125 adds six regression tests corresponding to the six new books.

They protect:

- Alice: uncertainty + repeated Extent change;
- Treasure Island: the apple-barrel semantic paragraph;
- The Time Machine: reporting temporal claims without a special time-travel root;
- The Wealth of Nations: capability + production-rate composition;
- On the Origin of Species: dependency + population/count pressure;
- Twenty Thousand Leagues: geometry/measurement + movement rate.

The tests intentionally use generic contextual references rather than registering book-specific proper names.

Suite size:

- **667 -> 673 tests**.

## Inventory effect

No language/world vocabulary is added in this broad discovery checkpoint.

Inventory remains:

- **212 registered base entries**;
- **131 semantic primitive candidates**;
- **55 formal constructors**;
- **265 semantic frames**;
- **48 multi-frame entries**;
- **204 Old Names**;
- **197 core world concepts**.

## Result

**BROAD MULTI-BOOK PASS: STRUCTURALLY STRONG, ONE DEFERRED PHYSICS EXTENSIBILITY GAP.**

The seven-source picture is now:

- Yona — magic/combat/progression baseline: structurally covered;
- Alice — identity/change/dialogue: covered;
- Treasure Island — secrecy/naval authority/action: covered;
- The Time Machine — temporal/scientific discourse: covered at language level, world-model dependent physically;
- Twenty Thousand Leagues — engineering/measurement: mostly covered, but exposes physical Pressure/extensible-measured-attribute gap;
- Origin of Species — taxonomy/heredity/population causal reasoning: covered compositionally/world-wise;
- Wealth of Nations — labour/productivity/exchange/economics: covered compositionally/world-wise.

No evidence from this pass supports restoring a removed semantic root.

## Next work

Before beginner/glyph work, resolve the one new structural question deliberately:

> Should objective physical dimensions such as Pressure become core runes/dimensions individually, or should world packages be able to register first-class measured AttributeDescriptors and Quantity dimensions?

Do not decide this from Pressure alone.

Audit the current physical Attribute/Quantity architecture as a family, using the Verne passage as the regression case, and choose the smallest mechanism that can support future world physics without turning every scientific quantity into a universal rune.

After that decision, the multi-book corpus can be considered closed for this round unless another selected passage is deliberately deepened.
