# Current State

_Last updated: 2026-09-28_

This is the canonical short handoff for Cuspell. Detailed normative work lives under `docs/spec/`; `docs/DECISIONS.md` records decisions that should not silently regress.

## Goal

Cuspell is a formal/compositional rune language for objective freeform magic.

Players should be able to create effects that were never prewritten as spells while valid expressions have meanings determined by the language rather than negotiated with the GM.

The full language may be large. Vocabulary knowledge, semantic compression, and mathematical skill are intended to create real mechanical advantages.

## Stable design principles

- Complex commands and multiple actions are allowed when objectively expressible.
- Language semantics and magical executability are separate layers.
- Every written meaning-bearing rune costs mana.
- Pure syntax/grammar can cost zero mana.
- Genuine registered compression may reduce mana.
- Arbitrary Names/aliases do not become free magical macros.
- Do not aggressively minimize the rune inventory.
- Ordinary language may contain context-dependent words; magical execution requires objective closure.
- Not, Zero, and Opposite remain distinct operations. Converse is no longer a primitive; relation roles are written directly in the intended order.
- Broad/underspecified, contradictory, ill-typed, and non-executable are distinct outcomes.

## Current temporary surface notation

Surface syntax **v0.7** makes flat, language-like prose the canonical written form.

- exact registered roots still win first;
- adjacency may be a licensed lexical compound such as `SolidMatter` or a uniquely typed tight local application such as `MatterSelf`, `LifeThis`, or `DensityThis`;
- ordinary whitespace separates larger phrase units;
- typed frames infer application/nesting across the flat stream;
- `|` and parentheses are explicit fallback/debugging grouping, not normal prose;
- final `.` / `?` / `!` terminate the sentence and mark Assertion / Question / Command mood;
- proposition conjunction/disjunction are infix `A And B` / `A Or B`; mixed bare And/Or requires explicit grouping rather than hidden precedence;
- event `Sequence` and `Concurrent` accept flat event lists; sentence end closes them, while `SequenceEnd` / `ConcurrentEnd` close them before later material;
- binders use bare declarations such as `a:Entity` or named-Kind domains such as `a:«Know«MoveLifeThing»»`, with `$a` references;
- true Collection values, roles, numbers, and quotation remain available where their semantics are actually needed.

Canonical style now looks like:

`MatterSelf.`

`Move This Here!`

`More Evaluate MatterSelf Evaluate ThingSelf.`

`LifeThis Or MagicThis.`

`Concurrent MoveSelfHere MoveYouThere!`

`If LifeThis EndLifeThis!`

The contextual one-argument `Evaluate target` form uses the current discourse evaluator; `Evaluate evaluator target` remains the explicit form.

The explicit form `!Move|This|Here.` is still valid, but ordinary writing should not expose the semantic tree unless ambiguity requires it.

Whitespace itself still contributes no semantic And/Sequence meaning.

The parser implements v0.5 sentence-final mood punctuation plus tight local binding and automated CI checks Python 3.11 and 3.12.

## Lexical semantic architecture

The eight root Categories have survived the current stress tests:

- Entity
- Kind
- Property
- Relation
- Process
- Quantity
- Reference<T>
- Operator

Important traits/mechanisms include:

- `state-predicate`
- `attribute`
- `scalar-attribute(D)`
- `dimension(D)`
- `reversible(X)`
- `converse(...)`
- `functional(inputs -> output)`
- collection typing
- family/family-value
- exclusive/blend families
- SenseChannel
- contextual
- commutative/associative
- countable

Higher semantic structures produced by grammar include:

- Term/value
- Proposition
- EventSpec
- Event
- Command
- Collection<T>
- Sequence<T>
- Location / Region / Path
- GeometryProfile
- ColorProfile
- TimePoint / TimeInterval
- Information values

## Attributes and state

A major refinement is now stable:

- **Property** = truth-valued predicate.
- **Attribute** = functional value relation.
- **state-predicate** = persistent Property/Relation whose truth can Begin/End.

Examples:

- `Life(x)` is a state Property.
- `Have(a,b)`, `Remember(m,i)`, `In(x,r)`, and `Joined(a,b)` are state Relations.
- `Heat(x)`, `Mass(x)`, `Phase(x)`, `Form(x)`, `ColorOf(x)` are Attributes returning values/profiles.

`Begin` and `End` operate on state predicates and event boundaries.

`Change(subject, attribute, target-value)` handles value-bearing attributes.

This distinction replaced several earlier ambiguous verb/property uses.

## Important lexical resolutions

The initial 15 high-risk roots have been resolved:

- `Part` = structural mereology only.
- `Whole` = integrity/completeness Property.
- numerical proportions use `Ratio`, not Part.
- generic magical `KindOf(This)` is rejected/deferred.
- generic magical `Of`, `By`, and English-like `For` are rejected.
- `Start` is folded into `Begin`.
- `Form` returns GeometryProfile.
- `Surface` returns SurfaceRegion.
- `Volume` is measured spatial extent.
- `Magic` is an active magical-state Property.
- `Copy` initially applies to Information.
- `Disease` is a biological pathological state.
- `Memory` is Information; `Remember` is the Mind relation.
- `Name` is a many-to-many contextual Sign/referent Relation.

Joining/separating meanings are written directly as Begin/End of `Joined`; the standalone Join/Separate roots have been removed.

## Kind, world-concept, and name system

The specific-noun problem is now split across semantics, world ontology, and historical naming.

1. true semantic/ontological Kinds and roots remain in the language;
2. ordinary objects/species/Skills/etc. normally receive stable **world concept** identities and classifiers;
3. common pre-magic vocabulary normally receives descriptive **Old Names** built from roots already available when the term historically arose;
4. people, particular objects, foreign proper names, and newly coined terms use **New Names** through ordinary Name/reference relations;
5. ad-hoc restricted Kinds remain available compositionally.

Quoted names are exact Signs and may nest: `«Yona's«SharpStick»»`.

Old Names are historically frozen vocabulary and may supply genuine magical compression. Their mana cost comes from historical name units rather than expansion size.

Later Old Names may reuse earlier Old Names as name units. The nested Old Name contributes its complete frozen cost recursively, and the dependency graph must remain acyclic. This lets vocabulary develop historically from existing words instead of rebuilding every concept directly from primitive roots.

New Names never acquire magical macro power merely by being assigned.

The former direct noun roots Human, Cat, Water, Body, Hand, and Sound have now been migrated into core world concepts + provisional Old Names. Named Kinds are valid binder domains.

Material Kind remains distinct from Phase. Biological classifiers use objective lineage/development/world rules; artifact classifiers use persistent `Purpose` plus design/function/structure evidence rather than a separate `DesignedFor` root.

A bare Kind/world concept closes Create/Transform only when its world entry supplies a deterministic generation profile or transformation mapping; otherwise a template/profile is required.

See `docs/spec/NAMES_AND_WORLDBUILDING.md`.

### First civilization vocabulary seed

The first non-corpus-specific worldbuilding vocabulary batch is now machine-readable.

It originally added a small productive root layer including Big and Small; those two were first reduced through the general Size descriptor, and Size has since folded into the general Extent family. The surviving foundational layer includes Extent, Hard, Sharp, Sleep, Sign, Rule, Region, and Path; Write and Read have since reduced compositionally, and Grow is constrained Extent change. It then builds **62 ordinary/social world concepts as Old Names rather than direct English noun roots**. Information is now represented by its semantic type rather than a duplicate Kind root.

Coverage includes:

- plants/animals and common materials;
- tools, weapons, containers, clothing, beds;
- houses, doors, walls, roads, bridges, boats/ships, wells;
- fire, food, medicine, poison, farming/storage;
- currency, markets, settlements, families, leadership/councils;
- healer/teacher/messenger/guard roles and institutions;
- words, languages, records, books, maps, calendars, contracts, letters, laws;
- basic time/length/mass measuring tools.

Nested vocabulary is used deliberately. For example, Boat is `«MoveInLiquidThing»`, while Ship is now `«HighExtent«MoveInLiquidThing»»`.

The English gloss is metadata only. The actual vocabulary is the quoted descriptive Old Name.

Old Name etymology is not a live classifier: a Ship remains a Ship even when an instance is not contextually HighExtent. The world concept's future objective classifier determines membership.

All seeded concepts currently carry `classifier_status: world-ontology-required`; reference/naming exists now, while recognition/generation physics remains future world-package work.

See `docs/world/FIRST_CIVILIZATION_VOCABULARY.md`.

### Yona current published corpus and vocabulary pass

The first corpus-specific vocabulary migration now distinguishes ordinary historical vocabulary from Yona-world current/technical naming.

Ordinary chapter pressure originally added broad reusable entries such as Body, Long, Awake, Open, Locked, Eat, Attack, Grab, Bite, Climb, Fall, Jump, Stab, Limp, and Sever. Body has since been migrated from a direct Kind root to the Old Name `«LifeMatter»`, Grab has reduced to concurrent `Begin Touch` + `Begin Control`, and Sever has reduced to agentive `Cause` of `End Whole`.

It also added **18 ordinary Old Name/world-concept pairs** for recurring anatomy, environment, tools, and work vocabulary, including eye, ear, claw, tail, mouth, skin, corpse, fish, fisher, window, spoon, scent trail, sailor, crew, captain, tree branch, and bark.


A second residual cleanup originally added **12 reusable ordinary semantic entries**—Damage, Depth, Hunger, TextureOf, Loudness, Sound, Injured, Hungry, Sated, Dodge, Reflexive, and CamouflagedAgainst—and **5 more Old Name/world-concept pairs** for organ, stomach, wrist, tendon, and wound. Sound has since moved to the Old Name `«HearingThing»`; Sated has since reduced to `LowHunger`, Injured to `HighDamage`, and Depth to the third/depth axis of the general `Extent` relation.

This closes the seven ordinary residual buckets previously called out by the Chapters 1–14 + 47 audit: dodge; injury/wound detail; reflexive body motion; camouflage/texture; hunger/satiety; sound/intensity; and the currently identified additional anatomy. A final historical-vocabulary pass also adds the reusable roots Female and Worship plus five Old Name/world-concept pairs: monster `«Attack«Know«MoveLifeThing»»Thing»`, deity `«WorshipThing»`, goddess `«Female«WorshipThing»»`, old/pre-magic mana `«Use«WorshipThing»Magic»`, and meditation `«AwakeSleep»`. Telepathy is the only still-undecided history-dependent vocabulary item from that audit.

Yona-specific material is isolated in an opt-in world package:

- `world/yona/concepts.json`
- `world/yona/new_names.json`

The package currently supplies **318 world concepts and 329 New Name entries** through the current publication boundary at Chapter 168. The post-50 pass adds later Dungeon/System ontology, Adamantium/Hero ranks, Epithets, Classes/Professions, Skill Morph/Merge/Evolution, later Skills/Traits/Titles/Soul Weapons/Event rewards, and source-backed people/places/species. Generic Cuspell vocabulary is not silently replaced by these Yona technical names.

Important examples of New rather than Old vocabulary include `«Skill»`, `«Trait»`, `«Class»`, `«Level»`, `«Tier»`, `«Ichthyoid»`, `«Blink»`, and `«External Mana Manipulation»`.

A later technical sense does not inherit Old-Name magical privilege merely because its spelling resembles an older ordinary word.

See `docs/world/YONA_PUBLISHED_THROUGH_168_VOCABULARY.md` and `docs/corpus/yona/CH01_168_V09_FULL_PUBLISHED_PASS.md`.

### Cross-genre anti-overfitting pass

A full pass over Jane Austen's _Pride and Prejudice_ and the 1818 edition of Mary Shelley's _Frankenstein_ deliberately stresses Cuspell outside Yona's LitRPG/action profile.

The result is **still no G17/new grammar or semantic-type gap**. Both novels are structurally expressible with the existing G1–G16 architecture.

They do expose a genuine core-dictionary imbalance: the executable language was rich in magic/action/formal semantics but thin in ordinary social, emotional, kinship, and learning vocabulary.

A cross-genre core pass originally added **33 productive general entries**, including Love/Hate/Trust/Respect, gratitude/compassion/jealousy/fear/grief/remorse/shame, FriendOf/ParentOf/SiblingOf/SpouseOf/EngagedTo/Own, Understand/Remember/ResponsibleFor/Reputation, Consent/Refuse/Forgive/Deceive/Learn/Teach/Apologize/Thank, and Happy/Sad/Angry. Later minimization removes Teach as agentive `Cause` of a learner-state transition, Learn itself as typed `Begin Know` / `Begin Can` / `Begin Understand`, Thank as addressed `Say` of `GratefulTo`, Apologize as addressed `Say` of `RemorseFor`, Consent/Refuse as addressed permission assertion/denial, and Deceive as causation of a false belief state.

These are general roots/relations/processes, not Austen/Shelley packages or magical macros. Historically specific institutions such as Regency entail law, courts, marriage law, social titles, and Frankenstein's method of creating life remain world/history data.

See `docs/corpus/cross_genre/PRIDE_PREJUDICE_FRANKENSTEIN_V10_PASS.md`.

## Identity and existence

Entity identity is stable across ordinary Change/Transform.

- `Equal(A,B)` means same Entity identity when A and B are Entities.
- `Exist(x)` is a state predicate.
- `Create` creates a fresh identity.
- `Transform` preserves identity by default.
- `Begin(Exist(x))` can reinstate an already identifiable non-active Entity where world metaphysics permits.
- `Destroy` ends Existence.
- EndLife is not Destroy.

Process results can be bound with zero-mana result binders inside larger expressions.

## Collections, quantifiers, and selection

The language now separates:

- All/Some -> Propositions
- Collect/Filter -> Collections
- Each -> explicit distributed EventSpecs
- selectors -> explicit target reduction

A Kind never silently selects one member, Some never exports a target witness, and a singular Process never silently distributes over a Collection.

Selectors include working semantics for:

- Unique
- MinBy/MaxBy over arbitrary ordered key expressions (replacing specialized Nearest/Farthest/Lowest/Highest)
- First/Last
- Random

Ties are explicit rather than GM-resolved.

Trigger has a pattern-binding form when the matching witness must be used in the action.

## Space, geometry, and motion

Current spatial values:

- Location
- Region
- Path
- CoordinateFrame
- GeometryProfile

Key relations/functions include:

- At
- In (containment is the same relation with item/region roles stated directly)
- Inside / Outside
- Touch / Overlap
- Distance
- To / From
- Up / Down
- Offset
- Toward / AwayFrom
- Surface
- Center
- Edge / Sides
- Extent
- Form

Move uses explicit spatial constraints and ordinary continuous Path semantics.

Teleportation is now written as a discontinuous `At`-state boundary transition: `And {End At X source,Begin At X goal}` (or just `Begin At X goal` when the source is omitted), rather than as a separate Move root.

Canonical Region constructors such as Ball, Disk, Box, Cylinder, Cone, and Tube are strong working entries for precise area effects.

## Time and events

Time now distinguishes:

- TimePoint
- TimeInterval
- EventSpec
- concrete Event / EventRef
- Duration

Before/After, During, Simultaneous, and temporal overlap have distinct semantics.

`Happen(EventSpec, interval)` produces a Proposition about occurrence.

`Sequence` is ordered; `And` over EventSpecs is unordered/joint.

`Again` is contextual ordinary language; magic uses explicit Repeat/Event references.

Repeat is finite by default and can carry an explicit period.

Zero-time recursive control loops are non-executable unless temporal progress/well-foundedness is proven.

## Number and measurement

The numeric system preserves the original unary beginner notation and advanced compression.

- `@` = 1
- `Zero` = 0
- `Opposite@@` = -2
- Multiply/Divide/Add/Power/Root are typed arithmetic
- dimensions and Units are checked
- equivalent arithmetic can have different mana costs based on written length
- Ratio is distinct from Divide
- vectors include direction + magnitude/frame

Scalar Attributes use dimensions, so incompatible arithmetic fails mechanically.

## Color

The current Color model uses:

- RGB channel proportions;
- separate visible Light intensity;
- `ColorOf(subject) -> ColorProfile`.

Unweighted compounds such as `RedGreen` mean equal included proportions.

Weighted chroma uses explicit Ratio associations.

Balanced RGB does not automatically mean White; exact visible intensity matters.

Visibility is observer-sensitive through `VisibleTo`; black color is not invisibility.

## Mind and information

The language now distinguishes:

- Information from Sign;
- Sign detection from Meaning interpretation;
- Know from Believe;
- Memory content from Remember;
- Question from information acquisition;
- Command-content from active Command;
- Name from identity;
- numeral Sign from Quantity.

Hidden facts require explicit Sense/Find/Reveal-like capability. Grammar and References do not provide free divination.

## Magical execution

A spell is a Command over an EventSpec/control structure.

Execution is staged:

1. lexical parse;
2. type/frame validation;
3. semantic closure;
4. reference resolution;
5. constraint consistency;
6. magic-capability check;
7. RequiredPower computation;
8. mana/resource payment;
9. world-state commit.

Meaning-bearing rune count controls linguistic mana.

A separate working `Power` quantity represents how strongly the Command can impose its exact semantic result. RequiredPower is objectively computed by game/world rules.

Underpowered exact requests fail rather than becoming arbitrary weaker effects.

Natural consequences do not require Persist. Persist actively maintains a state and creates an active Magic condition.

Trigger, Repeat, Dispel, and enchantment now have working semantic definitions.

## World-model boundary

The core language no longer tries to hard-code one fantasy world's physics/metaphysics.

A versioned world package supplies:

- material classifiers;
- biological/anatomical classifiers;
- Mind/metaphysics model;
- Units;
- geometry/time defaults;
- physical consequences;
- artifact/cultural Kinds;
- generation profiles;
- magical capability restrictions;
- resistance and RequiredPower calibration.

This lets Cuspell remain one formal language while different campaigns provide objective setting data.

## Current validation status

A first semantic regression suite has been written in `docs/spec/STRESS_TESTS.md`.

It initially found eight concrete architecture gaps:

- Phase Attribute;
- relative-location construction;
- deterministic/tie-aware selection;
- Trigger witness binding;
- zero-time recursion;
- Create/Transform closure;
- observer-relative visibility;
- weighted color syntax.

All eight now have working specification-level resolutions.

No current stress test requires abandoning the eight-category typed architecture.

## Corpus translation testing

A real-prose corpus phase is now active alongside parser preparation.

The first corpus is **Yona [Cat Girl Evolution]** by Bedivere the Mad on Royal Road. The repository stores semantic paraphrases, Cuspell analyses, back-translation findings, and source locators rather than mirroring full copyrighted chapters.

Completed corpus work now includes:

- Chapter 1 opening/general prose, market/investigation, and System/dialogue passes;
- a 2026 current-language re-audit of the full Chapter 1 findings;
- Chapter 2 sequential adventure/discourse pass;
- Chapter 14 targeted mana-manipulation/body-construction pass plus 2026 current-language re-audit;
- Chapter 47 "How Mana Works" pass testing Cuspell against a detailed foreign magic system;
- a consolidated current Yona gap ledger;
- a v0.6 broad first pass across Chapters 1–14 plus Chapter 47, with fresh sequential pressure on Chapters 3–13;
- a fresh full-source v0.7 rerun of Chapters 1–14 plus Chapter 47, which exposed and closed Attempt/goal-directed-effort semantics.

The corpus immediately exposed ordinary-language gaps that spell-only testing had not forced.

New working semantics now include:

- Kind predication through InstanceOf;
- UtteranceContext and nested speech contexts;
- discourse referents/anaphora/definite descriptions;
- narrative reference time;
- temporal ordering through `Before` and temporal holding through `During`; present state is bare state, present event is `During ... Now`;
- generic statements are contextual high prevalence over the relevant collected domain, distinct from strict All and fixed-majority Most; habitual recurrence is `High OccurrenceRate ...`;
- Most and modal free-choice normalization;
- evaluator-relative Good/Bad/Important; ordered preference is `More Evaluate evaluator A Evaluate evaluator B`;
- Intend/Plan/Obligated/Permitted distinctions;
- Attempt as a real goal-directed effort EventSpec distinct from Intend and goal success;
- typed open wh-question binders;
- Stop versus Prevent;
- Concurrent EventSpecs;
- Confidence/Believe/Know separation;
- EvidenceFor/EvidenceAgainst distinct from Cause;
- Assert and compositional Promise speech acts without outer truth commitment;
- Rate/Trend semantics;
- Requires/prerequisite semantics;
- Method as an answer type for how-questions;
- BeforeValue/AfterValue snapshots;
- Preserve event-boundary invariants;
- ApproxEqual and general boundary-distance composition for former `Almost`;
- Control as a first-class relation;
- optional spatial Distribution values for nonuniform resources/fields;
- ShapeLike/Form similarity without Kind identity.

The prose corpus has strongly confirmed earlier distinctions such as:

- Form is not Kind;
- Touch is not Joined;
- Dead is not merely NotLife;
- not detecting a phenomenon is not proof of zero phenomenon;
- Name is not identity;
- reported assertions/beliefs must not become narrator/world truth.

Corpus files live under docs/corpus/.

The current re-audit shows stronger convergence than the historical files suggested. Most of Chapter 1's original architecture defects are now resolved. Chapter 14's major relative-change defects (BeforeValue, Preserve, dimensional arithmetic, ShapeLike versus Kind identity, Touch versus Joined, Control) are executable. Chapter 2 exposed only a small number of genuinely new structural needs, most clearly fixed-size collection partitioning and an explicit unknown/unavailable Information field value. Chapter 47 mostly repeated already-known gaps rather than forcing another top-level grammar redesign.

For the language-translation goal, Chapters 1, 2, 14, and 47 still have no known structural translation gap after the 291-test rerun. Their remaining needs are ordinary/world-specific vocabulary, compression conveniences, and style/pragmatics. See docs/corpus/yona/RERUN_291_2026.md and CURRENT_GAPS_2026.md.

The 2026-09-28 v0.6 first pass across Chapters 1–14 plus Chapter 47 extended fresh pressure through Chapters 3–13 and found one repeated new structural gap: **counterfactual / alternate-history conditionals (G15)**. Surface v0.7 closes that gap with contextual `Counterfactual(antecedent, consequent)` while leaving actual-world `If` unchanged. The same v0.7 change accepts the corpus-backed surface cleanup: proposition `Or` is infix like `And`, and `Concurrent` is flat like `Sequence`, with `ConcurrentEnd` only when needed before later material. Mixed bare And/Or requires explicit grouping. See docs/corpus/yona/CH01_14_47_V06_FIRST_PASS.md and CURRENT_GAPS_2026.md.

A subsequent **fresh full-source v0.7 reread** of all Chapters 1–14 and 47 found one further semantic-molecule omission: `Attempt(agent, goal)`. Earlier notes had treated Try/Attempt as compression, but Intend does not entail that any effort event occurred and the goal EventSpec would incorrectly entail success. Attempt is now executable and explicitly does not entail its goal. After this G16 closure, no additional semantic-core or ordinary-language completeness blocker was found in the audited chapters. See docs/corpus/yona/CH01_14_47_V07_FULL_RERUN.md.

A **full Chapters 1–50 v0.8 corpus pass** then revalidated Chapters 1–14 + 47 and applied fresh source pressure to Chapters 15–46 and 48–50. It found **no G17/new grammar or semantic-architecture gap**. Later pressure is predominantly Yona-specific names and world ontology. Telepathic speech in Chapter 50 confirms a real communication-channel lexical need, but its pre-magic history remains undecided, so no speculative core Telepathy Old Name was added. See `docs/corpus/yona/CH01_50_V08_FULL_PASS.md`.

A **v0.9 pass across every currently published numbered chapter through 168, plus Chapter 94.5**, again found **no G17**. Later chapters stress souls, Wraith/Revenant reanimation, curses, divine intervention, Dungeon identity/reconstruction, Skill Morph, Epithets, probability, Event rewards, Connection/Telepathy, demonic corruption and regeneration without requiring new grammar or semantic types. This is strong evidence of convergence, but it does **not** mean the language is finished or that world/game execution should become the next milestone. The broader corpus also exposes future world-history questions around Soul, undead/reanimation, Curse/Blessing/Sacred/Divine and generic Telepathy; none are promoted to core vocabulary without their history being settled. See `docs/corpus/yona/CH01_168_V09_FULL_PUBLISHED_PASS.md`.

### Executable parser status

The first reference parser/type-checker slice is now implemented and runnable.

Repository components:

- `run_cuspell.py` — zero-install CLI/interactive entry point;
- `src/cuspell/` — lexer/surface handling, typed parser, AST/model, diagnostics, CLI;
- `language/core/types.json` — first machine-readable type hierarchy;
- `language/core/lexicon.json` — executable lexicon/frame slice;
- `language/core/dimensions.json` — canonical dimension vectors and registered quantity aliases;
- `language/syntax/surface_v0_7.json` — current machine-readable surface syntax metadata;
- `language/names/old_names.json` — frozen historical Old Name vocabulary;
- `world/core/concepts.json` — stable world concept identities/types;
- `world/core/new_names.json` — current New Name/reference data;
- `docs/CUSPELL_DICTIONARY.md` — human-facing dictionary of every registered entry plus the canonical writing rules;
- `tests/test_parser.py` — executable regression tests;
- `docs/PARSER.md` — usage and scope.

Current executable capabilities include:

- ordinary-space typed parsing plus pipe hard-binding and fallback grouping;
- exact nested quoted Signs, typed Old Name resolution/expansion, world-concept references, and frozen historical-name mana costs;
- full-consumption typed prefix parsing;
- Kind predication and dynamic registered adjacency compounds;
- Move / EndLife / Change plus Begin/End state-boundary compounds;
- possession/state transitions through `BeginHave` / `EndHave` and `BeginJoined` / `EndJoined`;
- scalar Attributes and measured-property compounds across Mass, Density, Heat, Light, Volume, Distance, and related dimensions;
- machine-readable dimensional arithmetic for Add, Multiply, Divide, Power, and Root, including registered results such as Length×Length=Area and Density×Volume=Mass plus stable derived dimensions;
- static dimensional Power/Root typing: dimensionful bases require exact known exponents/degrees, while runtime exponents/degrees remain legal for dimensionless Numbers;
- machine-readable Unit registration with neutral canonical constructors, exact rational scale normalization, and typed participation in arithmetic;
- distinct `DimensionMismatch` diagnostics for incompatible known quantity dimensions;
- If / Counterfactual / And / Or / All / Some / Sequence / Concurrent / Repeat plus Attempt goal-directed effort;
- binders, variables, named roles, finite collections, Collect, Filter, Each, Count, and typed selector reduction;
- Unique / MinBy / MaxBy / Random selector behavior, including explicit tie-preserving collection types;
- collection-bound binder type checking for Filter/Each;
- BeforeValue / AfterValue event-local snapshots and Preserve;
- state, spatial, and temporal Relations used by current stress/corpus cases;
- typed open questions plus epistemic/information, discourse, and modality slices;
- mana counting and normalization/equivalence checks;
- illegal-compound diagnostics distinct from unknown roots;
- exclusive-family and direct P + NotP contradiction checking;
- command semantic-closure checking and distinct INCOMPLETE output for meaningful but underconstrained Commands;
- machine-readable language-data validation;
- deterministic fuzz-smoke coverage;
- backtracking diagnostics ranked by completed parse progress rather than raw token wander;
- original-source character spans carried through parser diagnostics, semantic AST nodes, semantic validation, and execution-closure diagnostics; collection/group subexpressions conservatively fall back to their enclosing source phrase when an exact inner range is unavailable;
- executable regressions for additional written stress distinctions such as existential non-selection, Touch vs Joined, ShapeLike vs Kind identity, event Or rejection, and compositional former-state meaning vs Not.
The executable regression suite now passes **509 tests** under automated CI on Python 3.11 and 3.12.

The parser is still intentionally incomplete relative to the full written/world lexicon. Unsupported ordinary nouns may mean "vocabulary/world entry not encoded yet" rather than invalid Cuspell. The G1–G16 corpus gap set, including G15 counterfactual reasoning and G16 Attempt semantics, is now executable at expression level. Automatic multi-sentence discourse resolution, runtime world reference resolution, world execution, and RequiredPower remain outside this parser layer.

### Core root minimization pass 1

The reduction-first cleanup has now completed three direct/compositional batches plus foundational noun migration, extrema-family consolidation, Unit consolidation, and later family-by-family resolution checkpoints through pass 83. The registered base inventory is still **210 entries**.

Pass 1 removed eleven exact redundancies: After, Less, AtLeast, AtMost, EvidenceAgainst, NotDetected, Never, False, Claim, Lose, and Destroy.

Pass 2 removed eleven more compositional entries: Contain, Get, Join, Separate, Tell, See, Hear, Smell, Taste, ChangeBy, and Converse. Their meanings are written using the surviving general machinery: In, Begin/End state relations, Say, Sense + channel, Change + Add + BeforeValue, and direct relation-role order.

Pass 3 removes Between, Ask, and TimeOverlap. Ordered betweenness is written with two More comparisons, questions are addressed with Say carrying QuestionContent, and temporal overlap uses the general Overlap relation with typed temporal frames.

The next direction-family cleanup removes AwayFrom: Toward(reference) already yields a Direction, and Opposite now accepts Direction, so AwayFrom is written `Opposite Toward reference`.

DirectPart is now written compositionally as Part(A,B) plus the absence of a distinct intermediate Part. No separate immediate-part root remains.

The temporal wrapper Former has also been removed: its current exact meaning is `Before(P,Now) And Not(P)`, because a bare StateProposition is evaluated at the active present/reference time. The draft corpse Old Name is now `«BeforeLifeNowNotLife«LifeMatter»»`.

The duplicate Information Kind root is removed because Information already exists as the semantic content type. That makes `i:Information` an unambiguous semantic-type binder and allows `KnowAnswer` to reduce to existential `Know + AnswerFor`.

Increasing and Decreasing are now comparisons between a generalized `ChangeRate(value, interval)` and typed `Zero`. `ApproxEqual` is the conjunction of the two tolerance-bounded signed differences. `Stable` is also removed: exact stability is `Equal ChangeRate value interval Zero`, while tolerance-bounded stability uses the corresponding two-sided rate bound.

`Sometimes` is now the existing existential occurrence relation: `Happen(EventSpec, interval?)`. The separate convenience root is removed.

`Members(group)` is now derived as `Collect x:Entity Member $x group`. `Member` itself accepts either a collection or a group Entity, so the separate functional `Members` root is removed.

`Stop` is now the EventSpec use of the existing `End` root on a concrete Event. `End(Event)` still returns the ending TimePoint when a TimePoint is expected, and returns an EventSpec meaning “terminate this event” when an EventSpec is expected.

`Teach` remains compositional, but after Learn removal its effect is written directly: `Cause teacher Begin Know learner information/proposition`, `Cause teacher Begin Can learner EventSpec`, or `Cause teacher Begin Understand learner content`.

`Prefer` is now ordered evaluation: `More Evaluate evaluator preferred Evaluate evaluator other`. `More` has a specific EvaluationValue frame returning `StateProposition`, preserving preference's state semantics while generic ordered comparisons remain ordinary Propositions.

`SiblingOf` is shared-parent composition: `Some p:Entity And {ParentOf $p A,ParentOf $p B,Not Equal A B}`. `Equal`, `And`, and `Some` preserve `StateProposition` typing in this form, so siblinghood keeps its temporal/state behavior without a separate root.

`High` is now the general contextual above-standard constructor. It can apply directly to ordered values (`High OccurrenceRate ...`) and productively form first-class threshold Properties from AttributeDescriptors (`HighLength`, `HighHunger`). Near-threshold use no longer needs `Almost`: for example `And {Not HighHunger Self,Low Distance HighHunger Self}`.

The epistemic convenience roots are now all written from normalized `Confidence`: possibility is `More Confidence mind proposition Zero`, ordinary contextual probability is `High Confidence mind proposition`, and certainty is `Equal Confidence mind proposition «ConfidenceUnit» @`. The canonical Confidence scale fixes Zero as complete rejection and one ConfidenceUnit as complete confidence.

`Continue` is no longer a standalone Process root. For a resolved concrete ongoing Event E, “continue at the present boundary” is `Prevent End E Interval Now Now`: the generic End EventSpec already denotes termination, and Prevent blocks that termination at the current boundary. Ordinary discourse may first resolve an ongoing EventSpec to its concrete EventRef; magical use must supply the resolved Event.

`Period` is also removed. For any recurrence with a well-defined frequency, its period is the reciprocal `Divide @ OccurrenceRate event`; an explicit interval may be supplied to OccurrenceRate when the measurement scope must be objective.

`Present` is removed as a standalone temporal wrapper. For a StateProposition, the unmarked proposition itself is the present/reference-time reading. For an EventSpec, present occurrence is `During event Now`.

The temporal/aspect cleanup removes `Completed` and `Ongoing`: a completed EventSpec is expressed by ordering it before the reference boundary (`Before event Now` or `Before event T`), while an ongoing EventSpec at a point or across an interval is `During event time`.

The contextual size pair is now the holistic EvaluationValue frame of `Extent`. `Big X` is `HighExtent X`, while `Small X` is `LowExtent X`. This contextual extent scale is not a substitute for explicit axis Length/Volume in objective magic.

The next temporal/generalization batch removes four more specialized roots. `Past X` is `Before X Now`, `Future X` is `Before Now X`, and `Always P I` is `During P I` using a Proposition+TimeInterval overload meaning “P holds throughout I.” `LocalDensity D R` is now the Distribution+Region overload `Density D R`. Pattern/state overloads of `Before` remain contextual, preserving the old non-objective discourse behavior.

The geometry/change/social batch first made `Height` and `Width` axis selections of a general projected-extent relation; that relation is now `Extent(subject,frame,axis)`, with `@` primary/up and `@@` width. `Grow X` is constrained `Change` whose event-local Extent after-value is greater than its before-value. `Promise S A E` is now `And {Say S (Obligated S E :context A) A,Begin (Obligated S E :context A)}`, preserving the speech act and commitment/obligation-state transition.

The next consolidation batch removes four more specialized relations. Entity `Same` is now ordinary typed `Equal`; `Equal` returns a StateProposition and Entity equality is identity equality. `Detected A X C` is `Happen Sense A C X`, while channel-omitted detection existentially quantifies a SenseChannel. `MethodFor M E` is the already-general intended-goal relation `Purpose M E`. Finally, `Using E I` becomes the Event/EventSpec instrument-role overload `Use E I`, while the three-argument `Use agent instrument goal` Process remains unchanged.

`Injured` is now the productive threshold property `HighDamage`. The draft wound Old Name is rebuilt as `«HighDamage«LifeMatter»Part»`.

The next four reductions remove another contextual/ordinary-language convenience layer. `Habitual E I` is `High OccurrenceRate E I`; `Depth` is the third (`@@@`) axis of `Extent`, with a contextual no-frame shorthand for ordinary discourse; `Thank` is addressed `Say` of a `GratefulTo` proposition; and `Apologize` is addressed `Say` of a `RemorseFor` proposition. `GratefulTo` now accepts an optional explicit `:basis`, while `RemorseFor` has a contextual one-argument frame for ordinary apology wording. Neither speech composition entails sincerity.

The following four reductions consolidate the remaining temporal/change wrappers that already have exact general machinery. `Whenever C K I` is `During SufficientFor C K I` (with contextual `ThisInterval` supplying the interval when omitted); `NextOccurrence E` is the contextual EventSpec overload `First E`; `Redistribute` is Distribution-valued `Transfer`, with optional named `:profile`; and generic discourse `Because target reason` is contextual `Explains reason target`, leaving physical `Cause` and epistemic `EvidenceFor` distinct.

The next four passes eliminate the final registered derived candidate and three unresolved conveniences. `Almost P X` is false-side contextual low boundary distance, `And {Not P X,Low Distance P X}`, with the analogous EventSpec form using `Not Happen E`; `Should A E` is `High Evaluate A E`; artifact `DesignedFor X E` is the already-persistent function relation `Purpose X E`; and `Learn` is replaced by the typed state transition actually acquired—`Begin Know`, `Begin Can`, or `Begin Understand`. `Can` is therefore explicitly state-typed.

The following four passes consolidate higher-level families rather than introduce new roots. `Generic` becomes contextual high prevalence via `High Ratio Count Collect ...`; `Size` becomes the contextual EvaluationValue frame of `Extent`; `Span` becomes the axis-indexed Length frame of the same `Extent` root; and `CommittedTo` becomes `Obligated ... :context ...`. The Promise composition and affected draft Old Names are rebuilt accordingly.

The next four remove more lexicalized event wrappers. `Teleport` is `End At` + `Begin At` without a continuous Move path; `Write A S` is `Cause A Begin Exist S` for a Sign; `Read A S` is `If Sign S (Sense A S)`, using the contextual interpreted-Sign Sense overload; and `Grab A T` is `And {Begin Touch A T,Begin Control A T}`. Touch is now explicitly state-typed, Exist accepts semantic values such as Sign tokens, and the Hand/Wrist draft Old Names are rebuilt around `Control`.

The following four reductions consolidate explicit social acts and structural integrity. `Consent C E` is `Say C (Permitted E :authority C)`; `Refuse R E` is `Say R (Not (Permitted E :authority R))`; `Deceive D T P` is `If (Not P) (Cause D (Believe T P))`; and `Sever A T` is `Cause A (End Whole T)`, with optional `:instrument`. `Permitted` therefore gains an event-level authority frame, `Cause` gains StateProposition effects and an optional instrument role, and `Whole` is explicitly state-typed.

The next four audit passes are retention decisions rather than forced deletions. `Meaning` remains the Sign-to-content interpretation relation; `About` remains Information topicality; `DistributionOf` remains the resource/host-to-Distribution constructor; and `TotalAmount` remains the aggregate/integral amount function over a Distribution. None currently has an exact reduction through the surviving roots without losing semantics.

The following four audit passes are also retention decisions. `Beneficiary` remains the Event/EventSpec beneficiary role; `Bite` remains an oral-action manner not captured by generic Attack/Eat/Touch/Damage; `CamouflagedAgainst` remains observer/background-sensitive camouflage; and `Climb` remains a locomotion manner not equivalent to generic Move plus direction/contact constraints.

The next four audit passes also retain their entries. `Contrast` keeps discourse concession/tension beyond plain conjunction; `Dodge` keeps evasive threat-avoidance action rather than generic Move/Prevent/Attempt; `Fall` keeps non-agentive gravity/context-governed motion; and `Forgive` keeps the social transition of relinquishing blame/resentment without erasing responsibility, memory, or every negative emotion.

The final four unresolved audit entries also survive. `Reflexive` keeps involuntary/reflex execution status beyond mere absence of intention; `Jump` and `Limp` keep distinct locomotion manners not encoded by generic Move; and `Stab` keeps a puncturing/thrust action manner not reducible to Attack/Damage/Touch/Use. The unresolved-candidate bucket is therefore now empty.

`Low` is now the symmetric contextual below-standard constructor. It is deliberately not defined as `Not High`; a middle band may exist. This removes `Rarely` as `Low OccurrenceRate ...` and `Sated` as the first-class state Property `LowHunger`.

`ImportantTo target evaluator` is now evaluator-relative high evaluation: `High Evaluate evaluator target`. The generated result is a StateProposition, matching its persistent evaluative reading.

A deeper specification check restored **Inside** and **Outside** after the first pass: they are not aliases for In / Not In. Inside excludes boundary contact; Outside excludes interior overlap. This correction preserves the semantic distinction while keeping the net reduction at 22 entries.

Affected draft Old Names were rebuilt around the smaller root set. Historical Signs and mana costs remain editable until an explicit language/history freeze.

See `docs/ROOT_MINIMIZATION_AUDIT.md`.

### Unit root consolidation

The six canonical typed Unit constructors are no longer separate rune entries.

A single productive `Unit` root now combines historically with measurement roots to form typed Old Names: `«ConfidenceUnit»`, `«HeatUnit»`, `«LengthUnit»`, `«LightUnit»`, `«MassUnit»`, and `«DurationUnit»`.

Unit consolidation first reduced the raw base-sign inventory to **277**; later reductions bring the current total to **210**.

### Primitive-vs-derived full inventory audit

Every one of the **210 registered base entries** now has an explicit inventory role in `language/core/inventory_roles.json`.

Current classification:

- **130 semantic primitive candidates**;
- **0 derived candidates**;
- **0 unresolved reduction candidates**;
- **54 formal constructors**;
- **16 reference forms**;
- **10 closed-domain values**;
- **0 direct noun/name migration candidates**; the six earlier candidates have been migrated.

This means the executable registry count is no longer treated as the root count. **130 entries currently survive as semantic primitive candidates**. The explicit unresolved-candidate bucket is now empty after exact-reduction review through Reflexive, Jump, Limp, and Stab; every retained candidate remains revisitable if stronger general machinery appears.

`Inside` and `Outside` remain primitive candidates because the spatial spec gives them strict boundary semantics not preserved by `In` / `Not In`.

See `docs/PRIMITIVE_DERIVED_INVENTORY.md`.

### Second-pass primitive family audit

The 130 surviving semantic primitive candidates have now been regrouped by reusable semantic family rather than treated as an alphabetical list. The complete map is in `docs/SECOND_PASS_PRIMITIVE_FAMILY_MAP.md`.

The family map covers all 130 candidates and identifies repeated abstraction pressure in ten areas. The clearest first target is **motion/action manner**: Bite, Climb, Dodge, Fall, Jump, Limp, and Stab all survived the first audit because generic Move/Attack/Touch/etc. do not encode their manner of realization.

No language change has been made at this checkpoint. The next design experiment should test whether a smaller reusable event-manner feature basis can define several of those roots exactly. A rewrite that merely replaces each old root with one equally primitive manner value does not count as a reduction.

The post-minimization regression over Yona, Pride and Prejudice, and Frankenstein remains the required safety net for any second-pass deletion.

### Foundational noun migration and extrema consolidation

Six ordinary direct Kind roots are removed:

- Human → `«Know«MoveLifeThing»»`
- Cat → `«LowExtent«MoveLifeThing»»`
- Water → `«LiquidMatter»`
- Body → `«LifeMatter»`
- Hand → `«Control«LifeMatter»Part»`
- Sound → `«HearingThing»`

Their concepts remain available as named Kinds, and binder syntax now accepts named Kind domains.

The four special extrema operators Nearest/Farthest/Highest/Lowest are replaced by two general tie-preserving formal constructors, `MinBy` and `MaxBy`, parameterized by a bound ordered key expression.

Generic/current Cuspell New Names now have a dedicated human-facing index at `docs/world/NEW_NAMES.md`. It intentionally excludes Yona and future book/campaign packages. The generic registry currently contains **0** New Names.

## Current implementation target

`docs/spec/AST_AND_VALIDATION.md` defines the normalized semantic AST and diagnostic categories. The implementation/corpus loop is now mature enough that several former "next" items are already active: selector/collection coverage, state relations, measured properties, open questions, discourse/modality, corpus bridge tests, language-data validation, and deterministic fuzzing all have executable coverage.

The current Old Name inventory is provisional. It models the intended historical layer but may be rewritten freely while roots and semantics are still being designed. Do not preserve a root solely because an existing draft Old Name uses it.

The current milestone is **language stabilization**, not game/world simulation. Corpus pressure has become regression evidence, but the language is not yet declared finished or frozen.

1. keep future corpus pressure diverse and targeted rather than Yona-only;
2. audit and clean the root inventory, including overlap, awkward decompositions, and missing ordinary-language families;
3. continue testing Old Name/New Name boundaries and historical naming rules;
4. expand ordinary vocabulary when diverse corpus pressure justifies it;
5. continue stress-testing syntax, ambiguity, grouping, reference forms, discourse, and compositional semantics;
6. refine source-span granularity and keep parser/type behavior aligned with the written specification;
7. continue data-driving frame/trait constraints instead of adding one-off parser logic;
8. define explicit criteria for a language-stable / v1 semantic freeze before designing gameplay execution.

Objective world classifiers, runtime world execution, concrete physics, generation profiles, and RequiredPower remain **future magic-system/game-engine work**. They are useful design notes, but they are not the current implementation target because the eventual game, simulation model, and required abstraction level are not yet known.

Parser failures retain original-source half-open character spans and rank competing backtracking errors by parse progress. Semantic AST nodes now retain source spans as non-semantic metadata, and semantic/execution validators propagate them into diagnostics. Nested collection/group items currently fall back to the enclosing source phrase when exact inner offsets are unavailable.

## Source-of-truth order

When files conflict:

1. `docs/DECISIONS.md` for accepted/superseded design intent;
2. current domain specs under `docs/spec/`;
3. this `CURRENT_STATE.md` handoff;
4. historical audit/snapshot files only for rationale/history.

The original v0.3 snapshots remain preserved under `docs/history/`.
