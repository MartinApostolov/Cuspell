# Current State

_Last updated: 2026-09-27_

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
- Not, Zero, Opposite, and Converse remain distinct operations.
- Broad/underspecified, contradictory, ill-typed, and non-executable are distinct outcomes.

## Current temporary surface notation

Surface syntax **v0.6** makes flat, language-like prose the canonical written form.

- exact registered roots still win first;
- adjacency may be a licensed lexical compound such as `SolidWater` or a uniquely typed tight local application such as `CatSelf`, `LifeThis`, or `DensityThis`;
- ordinary whitespace separates larger phrase units;
- typed frames infer application/nesting across the flat stream;
- `|` and parentheses are explicit fallback/debugging grouping, not normal prose;
- final `.` / `?` / `!` terminate the sentence and mark Assertion / Question / Command mood;
- conjunction is infix `A And B`;
- event `Sequence` accepts a flat event list; sentence end closes it, while `SequenceEnd` closes it before later material;
- binders use bare `a:Human` declarations with `$a` references;
- true Collection values, roles, numbers, and quotation remain available where their semantics are actually needed.

Canonical style now looks like:

`CatSelf.`

`Move This Here!`

`More Evaluate CatSelf Evaluate HumanSelf.`

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

Additionally, Join/Separate are now Begin/End of `Joined`, not a universal Opposite pair.

## Kind and noun system

The specific-noun problem now uses several mechanisms rather than one trick:

1. ontological base Kinds;
2. canonical natural Kinds with objective world classifiers;
3. registered semantic molecules / artifact Kinds;
4. ad-hoc restricted Kinds.

This permits one-rune words such as Water, Iron, Wolf, Human, Hand, or Sword without claiming their meanings are semantic primitives.

Registered lexical compression is valid magic. User-created aliases are not.

Material Kind is distinct from Phase, so SolidWater and GasWater can remain Water.

Biological Kinds use objective lineage/development/world classifiers rather than surface-property descriptions.

Artifact Kinds use design/function/structure relations such as DesignedFor.

A bare Kind closes Create/Transform only when the Kind entry supplies a deterministic generation profile or transformation mapping; otherwise a template/profile is required.

## Identity and existence

Entity identity is stable across ordinary Change/Transform.

- `Same(A,B)` means same Entity identity.
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
- Nearest/Farthest
- Lowest/Highest
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
- In / Contain
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

Teleport is a discontinuous Move semantic molecule.

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
- a v0.6 broad first pass across Chapters 1–14 plus Chapter 47, with fresh sequential pressure on Chapters 3–13.

The corpus immediately exposed ordinary-language gaps that spell-only testing had not forced.

New working semantics now include:

- Kind predication through InstanceOf;
- UtteranceContext and nested speech contexts;
- discourse referents/anaphora/definite descriptions;
- narrative reference time;
- Past/Present/Future and aspect operators;
- Habitual and Generic distinct from All;
- Most and modal free-choice normalization;
- evaluator-relative Good/Bad/Prefer/Important;
- Intend/Plan/Obligated/Permitted distinctions;
- typed open wh-question binders;
- Stop versus Prevent;
- Concurrent EventSpecs;
- Confidence/Believe/Know separation;
- EvidenceFor/EvidenceAgainst distinct from Cause;
- Assert/Promise without outer truth commitment;
- Rate/Trend semantics;
- Requires/prerequisite semantics;
- Method as an answer type for how-questions;
- BeforeValue/AfterValue snapshots;
- Preserve event-boundary invariants;
- ApproxEqual/Almost;
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

The 2026-09-28 v0.6 first pass across Chapters 1–14 plus Chapter 47 extended fresh pressure through Chapters 3–13 and found one repeated new structural gap: **counterfactual / alternate-history conditionals (G15)**. Current `If`, `Past`, and `PossibleTo` do not compositionally preserve a known-false antecedent plus its asserted consequence in a relevant alternative history. No second new structural gap was found in Chapters 3–13. The same pass supplied surface-only evidence that `Or` should likely mirror infix `And` and `Concurrent` should likely mirror flat `Sequence`; those surface changes are not yet accepted. See docs/corpus/yona/CH01_14_47_V06_FIRST_PASS.md.

### Executable parser status

The first reference parser/type-checker slice is now implemented and runnable.

Repository components:

- `run_cuspell.py` — zero-install CLI/interactive entry point;
- `src/cuspell/` — lexer/surface handling, typed parser, AST/model, diagnostics, CLI;
- `language/core/types.json` — first machine-readable type hierarchy;
- `language/core/lexicon.json` — executable lexicon/frame slice;
- `language/core/dimensions.json` — canonical dimension vectors and registered quantity aliases;
- `language/syntax/surface_v0_6.json` — current machine-readable surface syntax metadata;
- `docs/CUSPELL_DICTIONARY.md` — human-facing dictionary of every registered entry plus the canonical writing rules;
- `tests/test_parser.py` — executable regression tests;
- `docs/PARSER.md` — usage and scope.

Current executable capabilities include:

- ordinary-space typed parsing plus pipe hard-binding and fallback grouping;
- full-consumption typed prefix parsing;
- Kind predication and dynamic registered adjacency compounds;
- Move / EndLife / Change plus Begin/End state-boundary compounds;
- possession/state-transition molecules such as Get/Lose and Join/Separate;
- scalar Attributes and measured-property compounds across Mass, Density, Heat, Light, Volume, Distance, and related dimensions;
- machine-readable dimensional arithmetic for Add, Multiply, Divide, Power, and Root, including registered results such as Length×Length=Area and Density×Volume=Mass plus stable derived dimensions;
- static dimensional Power/Root typing: dimensionful bases require exact known exponents/degrees, while runtime exponents/degrees remain legal for dimensionless Numbers;
- machine-readable Unit registration with neutral canonical constructors, exact rational scale normalization, and typed participation in arithmetic;
- distinct `DimensionMismatch` diagnostics for incompatible known quantity dimensions;
- If / And / Or / All / Some / Sequence / Concurrent / Repeat;
- binders, variables, named roles, finite collections, Collect, Filter, Each, Count, and typed selector reduction;
- Unique / Nearest / Farthest / Lowest / Highest / Random selector behavior, including explicit tie-preserving collection types;
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
- executable regressions for additional written stress distinctions such as existential non-selection, Touch vs Joined, ShapeLike vs Kind identity, event Or rejection, and Former vs Not.
The executable regression suite now passes **317 tests** under automated CI on Python 3.11 and 3.12.

The parser is still intentionally incomplete relative to the full written/world lexicon. Unsupported ordinary nouns may mean "vocabulary/world entry not encoded yet" rather than invalid Cuspell. The fourteen structural gaps from the current Yona audit are now executable at expression level. Automatic multi-sentence discourse resolution, runtime world reference resolution, world execution, and RequiredPower remain outside this parser layer.

## Current implementation target

`docs/spec/AST_AND_VALIDATION.md` defines the normalized semantic AST and diagnostic categories. The implementation/corpus loop is now mature enough that several former "next" items are already active: selector/collection coverage, state relations, measured properties, open questions, discourse/modality, corpus bridge tests, language-data validation, and deterministic fuzzing all have executable coverage.

The next major milestone remains a paired loop: **continue corpus pressure while closing the gap between the written specification and executable semantics**:

1. design and implement G15 counterfactual/alternate-history semantics without weakening actual-world If, add corpus regressions, then continue fresh Yona coverage from Chapter 15;
2. refine source-span granularity inside collection/grouped subexpressions beyond the current enclosing-phrase fallback;
3. expand ordinary/world vocabulary as corpus translation actually requires it;
4. continue data-driving frame/trait constraints instead of adding one-off parser logic;
5. revise the written spec whenever corpus or implementation failures expose a semantic hole;
6. build a minimal default world package with Units/classifiers/generation profiles;
7. add reference resolution and world-execution stages;
8. only then tune RequiredPower/balance and design final rune glyphs/player-facing materials.

Parser failures retain original-source half-open character spans and rank competing backtracking errors by parse progress. Semantic AST nodes now retain source spans as non-semantic metadata, and semantic/execution validators propagate them into diagnostics. Nested collection/group items currently fall back to the enclosing source phrase when exact inner offsets are unavailable.

## Source-of-truth order

When files conflict:

1. `docs/DECISIONS.md` for accepted/superseded design intent;
2. current domain specs under `docs/spec/`;
3. this `CURRENT_STATE.md` handoff;
4. historical audit/snapshot files only for rationale/history.

The original v0.3 snapshots remain preserved under `docs/history/`.
