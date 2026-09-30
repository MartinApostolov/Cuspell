# Core Root Minimization Audit

_Status: pass 2 — reduction-first cleanup_

## Goal

Cuspell accumulated executable entries while closing corpus gaps. That was useful for discovering semantic distinctions, but it should not be mistaken for a final primitive-root inventory.

The current cleanup rule is now:

> A standalone core root must earn its place. If the same meaning can be expressed exactly and reasonably through existing composition, prefer composition.

This audit distinguishes:

- **primitive/root-worthy semantics**;
- **derived meanings that should be written compositionally**;
- **roots currently embedded inside draft Old Names, which may be redesigned during cleanup**;
- **temporary direct noun roots that should eventually migrate into the naming system**;
- **convenience vocabulary that may remain only if corpus readability justifies it**.

## Pass 1 result

The executable core had **306 entries** before this audit.

Pass 1 removes **11 exact-redundancy entries**, leaving **295**.

These removed forms do not carry unique semantics:

| Removed root | Canonical composition |
| --- | --- |
| After A B | Before B A |
| Less A B | More B A |
| AtLeast A B | More A B Or Equal A B |
| AtMost A B | More B A Or Equal A B |
| EvidenceAgainst I P | EvidenceFor I Not P |
| NotDetected E S | Not Detected E S |
| Never P I | Always Not P I |
| False | Not True |
| Claim S P | Assert S P |
| Lose A B | EndHave A B |
| Destroy X | EndExist X |

The corresponding standalone roots are removed rather than retained as aliases, because retaining aliases would not actually reduce the rune/root inventory.

### Inside/Outside correction

The first pass initially treated Inside as In and Outside as Not In. The detailed spatial specification disproved that simplification:

- In allows boundary contact;
- Inside requires strict interior placement without boundary contact;
- Not In merely says full containment fails;
- Outside requires no extent in the region interior.

Because the current geometry layer cannot reproduce those stricter predicates compositionally, Inside and Outside remain primitive Relations for now.

## Old Names do not block reduction during the design phase

Pass 2 demonstrates this rule in practice. Contain, Join, Separate, Get, Tell, See, Hear, Smell, and other roots were removed even though draft Old Names used them; the affected names were rebuilt from the surviving language.

Remaining descriptive roots such as `Big`, `Small` and others are still open to reduction if a smaller general mechanism can preserve their meanings. `Injured` has been reduced to `HighDamage`, and `Sated` to `LowHunger`.

Draft Old Names are **not protected compatibility surfaces**. When a root is removed, rebuild the affected names as needed. During language design, their spellings, etymologies, nesting, and mana costs are allowed to change.

The historical freeze rule applies only after the language/history reaches an explicit freeze point.

## Pass 2 result

Pass 2 removes **11 additional compositional entries**, leaving **284** executable core entries.

| Removed root | Canonical composition |
| --- | --- |
| Contain R X | In X R |
| Get A B | BeginHave A B |
| Join A B | BeginJoined A B |
| Separate A B | EndJoined A B |
| Tell S I A | Say S I A |
| See E X | Sense E Vision X |
| Hear E X | Sense E Hearing X |
| Smell E X | Sense E Olfaction X |
| Taste E X | Sense E Gustation X |
| ChangeBy X Attr D | Change X Attr Add BeforeValue Attr X D |
| Converse Relation | write Relation directly with the intended role/argument order |

This means the corrected first two passes reduce the core from **306 to 284**, a reduction of **22 registered entries** without deleting a semantic distinction.

Affected draft Old Names were rebuilt from the surviving language. Some became longer and more expensive; that is acceptable during language design because the goal is a cleaner primitive system rather than preserving provisional compression.

## Tier 3 — candidates requiring real design work

These are not removed in the first two passes, but should be challenged next.

### Generalized state-boundary vocabulary

The exact wrappers Get, Join, and Separate are now removed.

Remaining candidates such as some readings of Learn would require proving that no extra acquisition/process meaning is lost before replacing them with BeginUnderstand / BeginKnow.

### Selection operators

Completed: Nearest, Farthest, Highest, and Lowest are removed.

They are replaced by the smaller general tie-preserving family:

- MinBy(collection, binder, ordered-key)
- MaxBy(collection, binder, ordered-key)

This preserves tie semantics while allowing distance, attributes, and future ordered keys to share the same machinery.

### Change helpers

ChangeBy is now removed in favor of Change + Add + BeforeValue.

Remaining candidate:

- Redistribute as an explicit change to DistributionOf.

Stable is now removed: exact stability is equality of ChangeRate with typed Zero, and tolerance-bounded stability is a two-sided rate bound.

### Modal/probability convenience

The Confidence family is now partly reduced:

- PossibleTo -> More Confidence ... Zero;
- ProbableTo -> High Confidence ...;
- CertainTo remains registered until its exact upper/registered certainty standard is represented.

The first two were removed only after their threshold semantics became explicit.

### Frequency convenience

`Rarely` is now reduced to `Low OccurrenceRate ...` after adding the general contextual Low standard. `Always` remains distinct: holding throughout an interval is temporal quantification, not merely a low/high occurrence-rate threshold.

### Social/cognitive convenience

The recent cross-genre pass added useful distinctions, but some processes may still be compositional:

- Learn
- Thank
- Apologize
- Deceive

These should be tested for readability and truth-condition preservation before keeping them as primitive roots.

## Direct noun migration completed

Human, Cat, Water, Body, Hand, and Sound have been migrated from direct Kind roots into world concepts + provisional Old Names. They remain usable as Kinds, including in binder domains, through their registered Names.

## Families that should not be collapsed casually

Reduction must preserve real semantic distinctions.

Examples already proven important:

- Same vs Equal
- If vs Counterfactual
- Intend vs Attempt
- Property vs Attribute
- Not vs Opposite
- Zero vs Not
- Life vs Exist
- Can vs epistemic possibility
- Old Name vs New Name

The goal is **fewer primitives**, not fewer meanings.

## Pass-2 method

For every candidate root:

1. write an exact compositional replacement;
2. verify that its truth conditions are identical;
3. verify parser/type correctness;
4. translate representative corpus examples both ways;
5. identify affected Old Names and redesign them if the root is removed;
6. compare rune cost/readability;
7. remove the root only if the composition remains clear enough.

This process should continue family by family rather than deleting dozens of roots merely because they look similar.

## Design-stage rule

The current Old Name inventory is provisional. Do not retain a primitive root merely to avoid editing an Old Name. Root minimization takes precedence; historical vocabulary is rebuilt afterward from the surviving language.


## Full inventory classification

The reduction work now distinguishes the raw executable registry from the actual primitive-root problem.

All **252** current registered base entries are classified in `language/core/inventory_roles.json`:

- 117 semantic primitive candidates;
- 14 derived candidates;
- 41 unresolved reduction candidates;
- 54 formal constructors;
- 16 reference forms;
- 10 closed-domain values;
- 0 direct noun/name migration candidates.

See `docs/PRIMITIVE_DERIVED_INVENTORY.md`.

A regression requires complete classification coverage, so newly added core entries cannot silently inflate the primitive inventory without being assigned a role.

The 117 semantic primitive candidates are not frozen. They are simply the entries for which this audit has not yet demonstrated a smaller exact analysis.


## Reduction checkpoint 3 — noun migration + extrema generalization

This checkpoint removes six ordinary direct Kind roots and four specialized extrema selectors, while adding two generic formal constructors.

Removed direct Kinds:

- Human
- Cat
- Water
- Body
- Hand
- Sound

Their concepts now use provisional Old Names.

Removed specialized selectors:

- Nearest
- Farthest
- Highest
- Lowest

Replacement:

- `MinBy collection binder key`
- `MaxBy collection binder key`

Both preserve all tied extrema; `Unique` remains the explicit singularity requirement.

Net executable registry change: **284 → 276**.



## Reduction checkpoint 4 — exact derived wrappers

A third direct-composition batch removes three more registered surfaces:

| Removed root | Canonical composition |
| --- | --- |
| Between V L U | More V L And More U V |
| Ask S Q A | Say S Q A, where Q is QuestionContent |
| TimeOverlap A B | Overlap A B |

`Overlap` now has temporal Event/Event and TimeInterval/TimeInterval frames in addition to its spatial/entity frame. This is one topological relation with typed domains, not a time-only duplicate.

The draft bridge Old Name was rebuilt from `MoveBetweenSidesThing` to `MoveSidesThing`; draft Old Names remain editable during minimization.

Net registered base inventory change: **277 -> 274**. Semantic primitive candidates remain **120**; derived candidates fall **32 -> 30** and unresolved candidates **47 -> 46**.

The removed ordered `Between` root did not implement geometric segment/geodesic betweenness. That geometry meaning remains separate and must not be recreated by pretending an arbitrary spatial domain is linearly ordered.

## Unit-family reduction

The six temporary typed Unit constructors have been collapsed into one productive `Unit` root.

Specific typed units are now Old Names, not independent roots:

`ConfidenceUnit`, `HeatUnit`, `LengthUnit`, `LightUnit`, `MassUnit`, and `DurationUnit`.

This changed the raw rune/base-entry count from 282 (276 core + six special constructors) to 277 core/base entries. The later reduction checkpoints reduce the current total further to **252**. The typed unit metadata remains executable without inflating the primitive rune inventory.


## Reduction checkpoint 5 — direction converse

`AwayFrom` is removed as a standalone root.

`Toward(reference)` already returns a typed `Direction`. `Opposite` now accepts `Direction` as well as Quantity, so the exact form is:

`Opposite Toward reference`

No Old Name depended on `AwayFrom`. Net registered base inventory change: **274 -> 273**. Semantic primitive candidates remain **120**; derived candidates fall **30 -> 29**.


## Reduction checkpoint 6 — immediate Part

`DirectPart` is removed as a standalone root.

Its exact structural meaning is `Part(A,B)` together with the negation of any distinct intermediate X for which `Part(A,X)` and `Part(X,B)`. `Some`, `Not`, and `Same` already express that condition; explicit grouping resolves surface-scope ambiguity without mana cost.

No Old Name depended on `DirectPart`. Net registered base inventory change: **273 -> 272**. Semantic primitive candidates remain **120**; derived candidates fall **29 -> 28**.


## Reduction checkpoint 7 — Former

`Former` is removed as a standalone root. For a state proposition P, its exact meaning is `Past(P) And Not Present(P)`.

The draft corpse Old Name is rebuilt as `«PastLifeNotLife«LifeMatter»»`. Net registered base inventory change: **272 -> 271**. Semantic primitive candidates remain **120**; derived candidates fall **28 -> 27**.

## Reduction checkpoint 8 — Information type and KnowAnswer

The direct `Information` Kind root is removed because Information already exists as an abstract semantic type. No draft Old Name depended on the Kind root.

`Know` now accepts Information content as documented. With `i:Information` unambiguously binding the semantic type, `KnowAnswer` becomes `Some i:Information And {Know mind $i,AnswerFor $i question}` and is removed.

Net registered base inventory change: **271 -> 269**. Semantic primitive candidates fall **120 -> 119** and derived candidates **27 -> 26**.


## Reduction checkpoint 9 — trend direction

`ChangeRate` is generalized to a Quantity-valued function over an interval, and `Zero` can inhabit the expected Quantity dimension. `Increasing` and `Decreasing` therefore reduce to explicit comparisons against typed zero and are removed.

Net registered base inventory change: **269 -> 267**. Semantic primitive candidates remain **119**; derived candidates fall **26 -> 24**.

## Reduction checkpoint 10 — approximate equality

`ApproxEqual(A,B,T)` is represented by two bounded signed differences: neither `A-B` nor `B-A` may be greater than T. This uses `Add`, `Opposite`, `More`, `Not`, and `And`.

Net registered base inventory change: **267 -> 266**. Semantic primitive candidates remain **119**; derived candidates fall **24 -> 23**.


## Reduction checkpoint 11 — Sometimes

`Sometimes(EventSpec, interval?)` duplicates the existing existential occurrence meaning of `Happen(EventSpec, interval?)`: at least one matching concrete Event occurs in the relevant temporal domain.

The standalone `Sometimes` root is removed. Net registered base inventory change: **266 -> 265**. Semantic primitive candidates remain **119**; derived candidates fall **23 -> 22**.


## Reduction checkpoint 12 — Members

`Member` is generalized to accept group Entity membership as well as explicit Collection membership.

`Members(group)` is then exactly `Collect x:Entity Member $x group`, so the standalone functional root is removed.

No Old Name depended on `Members`. Net registered base inventory change: **265 -> 264**. Semantic primitive candidates remain **119**; derived candidates remain **22**; unresolved candidates fall **46 -> 45**.


## Reduction checkpoint 13 — Stop

`End` gains an EventSpec-output frame for a concrete Event while retaining its existing TimePoint-output frame.

Thus `End E` means “terminate E” in an EventSpec context and “the ending time of E” in a TimePoint context. The typed parser distinguishes the two meanings without a second root.

`Stop` is removed. No Old Name depended on it. Net registered base inventory change: **264 -> 263**. Semantic primitive candidates remain **119**; derived candidates fall **22 -> 21**.


## Reduction checkpoint 14 — Teach

The written information spec already defines Teach as stronger than Say, with successful acquisition by the learner as its intended result.

The existing agentive Cause frame makes that exact composition writable:

`Teach T L C` -> `Cause T Learn L C`

No Old Name depended on `Teach`. Net registered base inventory change: **263 -> 262**. Semantic primitive candidates remain **119**; derived candidates remain **21**; unresolved candidates fall **45 -> 44**.


## Reduction checkpoint 15 — Prefer

The subjective-evaluation model already gives `Evaluate(evaluator,target) -> EvaluationValue`, and EvaluationValue is ordered.

Therefore `Prefer E A B` is exactly `More Evaluate E A Evaluate E B`. A specific `More(EvaluationValue,EvaluationValue)` frame returns StateProposition so the temporal/state behavior of preference is preserved.

No Old Name depended on `Prefer`. Net registered base inventory change: **262 -> 261**. Semantic primitive candidates fall **119 -> 118**; derived candidates remain **21**; unresolved candidates remain **44**.


## Reduction checkpoint 16 — SiblingOf

Siblinghood is derivable from ParentOf plus identity distinction:

`Some p:Entity And {ParentOf $p A,ParentOf $p B,Not Same A B}`

The logical machinery now preserves StateProposition through Same, And, and Some in this composition, so the derived relation retains the former root's state semantics.

No Old Name depended on `SiblingOf`. Net registered base inventory change: **261 -> 260**. Semantic primitive candidates fall **118 -> 117**; derived candidates remain **21**; unresolved candidates remain **44**.


## Reduction checkpoint 17 — High threshold constructor

The missing contextual-standard abstraction is now explicit as `High`.

`High(value)` means that an ordered value is above the relevant contextual standard. `High + AttributeDescriptor` productively forms a first-class threshold PropertyDescriptor, so the composition remains usable inside higher-order property operators.

This yields exact replacements:

- `Long X` -> `HighLength X`;
- `Hungry X` -> `HighHunger X`;
- `Often E I` -> `High OccurrenceRate E I`.

The draft tail Old Name is rebuilt from High + Length. Net registered base inventory change: **260 -> 258**. Semantic primitive candidates remain **117**; derived candidates fall **21 -> 19**; unresolved candidates **44 -> 43**; formal constructors rise **52 -> 53**.

## Reduction checkpoint 18 — Confidence convenience predicates

`PossibleTo` and `ProbableTo` are removed as independent roots:

- `PossibleTo M P` -> `More Confidence M P Zero`;
- `ProbableTo M P` -> `High Confidence M P`.

`CertainTo` is deliberately retained because contextual `High` does not mean exact certainty.

Net registered base inventory change: **258 -> 256**. Derived candidates fall **19 -> 17**.

## Reduction checkpoint 19 — Injury threshold

`Damage` is already an ordered EvaluationValue AttributeDescriptor, and `HighDamage` is therefore generated by the productive threshold-property machinery with StateProposition typing.

`Injured X` -> `HighDamage X`.

The draft wound Old Name becomes `«HighDamage«LifeMatter»Part»`.

Net registered base inventory change: **256 -> 255**. Derived candidates fall **17 -> 16**.

## Reduction checkpoint 20 — Stable rate

`Stable` is removed in favor of explicit rate constraints:

- exact: `Equal ChangeRate V I Zero`;
- tolerance-bounded: `And {Not More ChangeRate V I T,Not More Opposite ChangeRate V I T}`.

Net registered base inventory change: **255 -> 254**. Derived candidates fall **16 -> 15**.

## Reduction checkpoint 21 — Low frequency threshold

A general `Low` operator now expresses “below the relevant contextual standard” for ordered values. Unlike `Not High`, it permits an intermediate band.

`Rarely E I` -> `Low OccurrenceRate E I`.

One derived root is replaced by one reusable formal constructor, so the registered total remains **254**. Derived candidates fall **15 -> 14** and formal constructors rise **53 -> 54**.

## Reduction checkpoint 22 — Sated as LowHunger

Low + AttributeDescriptor productively forms first-class threshold Properties just as High does. Because Hunger returns EvaluationValue, `LowHunger` remains a StateProposition.

`Sated X` -> `LowHunger X`.

Registered base inventory **254 -> 253**. Unresolved candidates fall **43 -> 42**.

## Reduction checkpoint 23 — ImportantTo as high evaluation

Importance is an evaluator-relative threshold over the already registered EvaluationValue:

`ImportantTo target evaluator` -> `High Evaluate evaluator target`.

Registered base inventory **253 -> 252**. Unresolved candidates fall **42 -> 41**.
