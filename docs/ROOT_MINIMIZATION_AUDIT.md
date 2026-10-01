# Core Root Minimization Audit

_Status: first-pass audit complete; second-pass family reductions active_

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
| NotDetected A X C | Not Happen Sense A C X |
| Never P I | During Not P I |
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

At that first-pass checkpoint, the geometry layer could not reproduce those stricter predicates compositionally, so Inside and Outside were correctly restored. Second-pass checkpoint 89 later supersedes that retention by adding typed Region frames to Touch and Overlap while preserving the same boundary distinctions.

## Old Names do not block reduction during the design phase

Pass 2 demonstrates this rule in practice. Contain, Join, Separate, Get, Tell, See, Hear, Smell, and other roots were removed even though draft Old Names used them; the affected names were rebuilt from the surviving language.

`Big` and `Small` are now `HighSize` and `LowSize` over one contextual Size descriptor. `Injured` is `HighDamage`, and `Sated` is `LowHunger`.

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

Learn is now removed by making the acquired state explicit: Begin Know for facts/information, Begin Can for skills/EventSpecs, and Begin Understand for other semantic comprehension.

### Selection operators

Completed: Nearest, Farthest, Highest, and Lowest are removed.

They are replaced by the smaller general tie-preserving family:

- MinBy(collection, binder, ordered-key)
- MaxBy(collection, binder, ordered-key)

This preserves tie semantics while allowing distance, attributes, and future ordered keys to share the same machinery.

### Change helpers

ChangeBy is now removed in favor of Change + Add + BeforeValue.

`Redistribute` is now removed as the Distribution-valued overload of `Transfer`, with an optional named `:profile` for the destination profile.

Stable is now removed: exact stability is equality of ChangeRate with typed Zero, and tolerance-bounded stability is a two-sided rate bound.

### Modal/probability convenience

The Confidence family is fully reduced into one normalized ordered scale:

- PossibleTo -> More Confidence ... Zero;
- ProbableTo -> High Confidence ...;
- CertainTo -> Equal Confidence ... «ConfidenceUnit» @.

The canonical scale fixes Zero as complete rejection and one ConfidenceUnit as complete confidence/certainty.

### Frequency convenience

`Rarely` is reduced to `Low OccurrenceRate ...`. Holding throughout an interval remains distinct from frequency thresholds, but the separate `Always` root is no longer needed: it is the Proposition+TimeInterval frame of `During`.

### Social/cognitive convenience

The recent cross-genre pass added useful distinctions, but some processes may still be compositional:


These should be tested for readability and truth-condition preservation before keeping them as primitive roots.

## Direct noun migration completed

Human, Cat, Water, Body, Hand, and Sound have been migrated from direct Kind roots into world concepts + provisional Old Names. They remain usable as Kinds, including in binder domains, through their registered Names.

## Families that should not be collapsed casually

Reduction must preserve real semantic distinctions.

Examples already proven important:

- Same vs Equal — resolved: Same is removed; Entity Equal is identity equality
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

All **206** current registered base entries are classified in `language/core/inventory_roles.json`:

- 126 semantic primitive candidates;
- 0 derived candidates;
- 0 unresolved reduction candidates;
- 54 formal constructors;
- 16 reference forms;
- 10 closed-domain values;
- 0 direct noun/name migration candidates.

See `docs/PRIMITIVE_DERIVED_INVENTORY.md`.

A regression requires complete classification coverage, so newly added core entries cannot silently inflate the primitive inventory without being assigned a role.

The 126 current semantic primitive candidates are not frozen permanently. Sixteen of them—Meaning, About, DistributionOf, TotalAmount, Beneficiary, Bite, CamouflagedAgainst, Climb, Contrast, Dodge, Fall, Forgive, Reflexive, Jump, Limp, and Stab—have now survived an explicit exact-reduction review; the explicit unresolved-candidate bucket is now empty, and all retained candidates remain open to later analysis if stronger machinery appears.


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

This changed the raw rune/base-entry count from 282 (276 core + six special constructors) to 277 core/base entries. The later reduction checkpoints, including Rate consolidation, temporal Extent, and topology composition, reduce the current total further to **206**. The typed unit metadata remains executable without inflating the primitive rune inventory.


## Reduction checkpoint 5 — direction converse

`AwayFrom` is removed as a standalone root.

`Toward(reference)` already returns a typed `Direction`. `Opposite` now accepts `Direction` as well as Quantity, so the exact form is:

`Opposite Toward reference`

No Old Name depended on `AwayFrom`. Net registered base inventory change: **274 -> 273**. Semantic primitive candidates remain **120**; derived candidates fall **30 -> 29**.


## Reduction checkpoint 6 — immediate Part

`DirectPart` is removed as a standalone root.

Its exact structural meaning is `Part(A,B)` together with the negation of any distinct intermediate X for which `Part(A,X)` and `Part(X,B)`. `Some`, `Not`, and Entity `Equal` express that condition; explicit grouping resolves surface-scope ambiguity without mana cost.

No Old Name depended on `DirectPart`. Net registered base inventory change: **273 -> 272**. Semantic primitive candidates remain **120**; derived candidates fall **29 -> 28**.


## Reduction checkpoint 7 — Former

`Former` is removed as a standalone root. With Present now also removed, its current exact meaning is `Before(P,Now) And Not(P)`, where bare P is the present/reference-time state.

The draft corpse Old Name at that checkpoint used `Past`; it is later rebuilt again as `«BeforeLifeNowNotLife«LifeMatter»»` when Past is removed. Net registered base inventory change: **272 -> 271**. Semantic primitive candidates remain **120**; derived candidates fall **28 -> 27**.

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

Teaching is typed as agentive Cause of the learner-state transition: `Cause T Begin Know L C`, `Cause T Begin Can L E`, or `Cause T Begin Understand L C`.

No Old Name depended on `Teach`. Net registered base inventory change: **263 -> 262**. Semantic primitive candidates remain **119**; derived candidates remain **21**; unresolved candidates fall **45 -> 44**.


## Reduction checkpoint 15 — Prefer

The subjective-evaluation model already gives `Evaluate(evaluator,target) -> EvaluationValue`, and EvaluationValue is ordered.

Therefore `Prefer E A B` is exactly `More Evaluate E A Evaluate E B`. A specific `More(EvaluationValue,EvaluationValue)` frame returns StateProposition so the temporal/state behavior of preference is preserved.

No Old Name depended on `Prefer`. Net registered base inventory change: **262 -> 261**. Semantic primitive candidates fall **119 -> 118**; derived candidates remain **21**; unresolved candidates remain **44**.


## Reduction checkpoint 16 — SiblingOf

Siblinghood is derivable from ParentOf plus identity distinction:

`Some p:Entity And {ParentOf $p A,ParentOf $p B,Not Equal A B}`

The logical machinery preserves StateProposition through Equal, And, and Some in this composition, so the derived relation retains the former root's state semantics.

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

`CertainTo` was deliberately retained until the exact certainty endpoint existed; it is now `Equal Confidence ... «ConfidenceUnit» @`, not contextual `High`.

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

## Reduction checkpoint 24 — certainty endpoint

The Confidence scale now has explicit normalized endpoints. `Zero` is complete rejection and `«ConfidenceUnit» @` is complete confidence/certainty. Internal world or mind models may compute confidence however they wish, but they expose their result on this normalized scale.

`CertainTo M P` -> `Equal Confidence M P «ConfidenceUnit» @`.

Registered base inventory **252 -> 251**. Derived candidates fall **14 -> 13**.

## Reduction checkpoint 25 — continuation as boundary prevention

For a concrete ongoing Event E, continuing through the present boundary is exactly the prevention of its termination EventSpec at that boundary:

`Continue E` -> `Prevent End E Interval Now Now`.

The expected EventSpec type selects the stop-event overload of `End(E)`, while `Interval Now Now` prevents only termination at the current boundary. A contextual EventSpec must first be resolved to the concrete ongoing Event; magic cannot leave that resolution implicit.

No Old Name depends on Continue.

Registered base inventory **251 -> 250**. Derived candidates fall **13 -> 12**.

## Reduction checkpoint 26 — recurrence period as reciprocal frequency

`Period` carries no independent semantic distinction once OccurrenceRate is dimensioned as Frequency.

`Period E` -> `Divide @ OccurrenceRate E`.

When an objective measurement scope is needed, use `Divide @ OccurrenceRate E I`. The dimension algebra gives Time exactly because Number / Frequency = Time.

No Old Name depends on Period.

Registered base inventory **250 -> 249**. Unresolved candidates fall **41 -> 40**.

## Reduction checkpoint 27 — Present as the unmarked reference time

A StateProposition without a tense wrapper is evaluated at the active discourse/evaluation reference time, so a dedicated Present operator duplicates the default state reading.

- `Present P` -> `P`;
- `Present E` -> `During E Now` for EventSpec E.

This also shortens the already-derived Former meaning from `Past P And Not Present P` to `Past P And Not P`.

No Old Name depends on Present.

Registered base inventory **249 -> 248**. Derived candidates fall **12 -> 11**.

## Reduction checkpoint 28 — Completed folds into Past

Past now carries explicit EventSpec + TimePoint/TimeInterval frames with the same completed-before-reference semantics formerly carried by Completed.

`Completed E [T]` -> `Past E [T]`.

Registered base inventory **248 -> 247**. Derived candidates fall **11 -> 10**.

## Reduction checkpoint 29 — Ongoing folds into During

During now accepts EventSpecs as well as concrete Events:

`Ongoing E T` -> `During E T`.

The EventSpec frame means at least one matching occurrence is active across the supplied point/interval. Present-event shorthand is therefore `During E Now`.

Registered base inventory **247 -> 246**. Derived candidates fall **10 -> 9**.

## Reduction checkpoint 30 — Big becomes HighSize

Introduce one contextual ordered Size AttributeDescriptor. Big adds no meaning beyond the high threshold on that scale:

`Big X` -> `HighSize X`.

Because Size is added while Big is removed, the registered total remains **246**.

## Reduction checkpoint 31 — Small becomes LowSize

`Small X` -> `LowSize X`.

This removes the second duplicated threshold property. Draft Old Names using Big/Small are rebuilt around High + Size / Low + Size.

Registered base inventory **246 -> 245**. Unresolved candidates fall **40 -> 39**.

## Reduction checkpoint 32 — Past folds into Before

Generalized contextual Before frames cover state/event-pattern ordering against the reference time:

`Past X` -> `Before X Now`.

The existing explicit EventSpec reference/scope form becomes `Before E T`. This also rebuilds the corpse draft Old Name around Before + Now.

Registered base inventory **245 -> 244**. Derived candidates fall **9 -> 8**.

## Reduction checkpoint 33 — Future is reversed Before

`Future X` -> `Before Now X`.

The StateProposition and EventSpec overloads remain contextual just as Future was.

Registered base inventory **244 -> 243**. Derived candidates fall **8 -> 7**.

## Reduction checkpoint 34 — Always folds into During

A new Proposition + TimeInterval overload of `During` means that the proposition holds throughout the interval.

`Always P I` -> `During P I`.

Registered base inventory **243 -> 242**. Derived candidates fall **7 -> 6**.

## Reduction checkpoint 35 — LocalDensity folds into Density

The existing Density family now includes:

`Density(distribution, region) -> Quantity:Density`.

Therefore `LocalDensity D R` is exactly `Density D R`.

Registered base inventory **242 -> 241**. Unresolved candidates fall **39 -> 38**.

## Reduction checkpoint 36 — Height becomes primary-axis Span

A new `Span(subject,frame,axis-index)` relation measures projected extent along an ordered CoordinateFrame basis.

`Height X F` -> `Span X F @`.

Adding Span while deleting Height leaves the registered total at **241**.

## Reduction checkpoint 37 — Width becomes secondary-axis Span

`Width X F` -> `Span X F @@`.

The same primitive now handles both frame-relative scalar extents. Registered base inventory **241 -> 240**. Unresolved candidates fall **38 -> 37**.

## Reduction checkpoint 38 — Grow becomes constrained Change(Size)

The general Change event receives a constraint form that can reference event-local BeforeValue and AfterValue snapshots.

`Grow X` -> `Change X Size More AfterValue Size X BeforeValue Size X`.

Registered base inventory **240 -> 239**. Derived candidates fall **6 -> 5**.

## Reduction checkpoint 39 — Promise is a compound speech/commitment EventSpec

`Promise S A E` -> `And {Say S CommittedTo S E A A,Begin CommittedTo S E A}`.

The first conjunct is the addressed speech act; the second is the social-state transition. The promised EventSpec itself is not asserted to occur.

The contract draft Old Name is rebuilt around CommittedTo rather than Promise.

Registered base inventory **239 -> 238**. Unresolved candidates fall **37 -> 36**.

## Reduction checkpoint 40 — Same folds into Equal

Entity equality is identity equality, so `Same A B` adds no truth-conditional distinction beyond `Equal A B`. Equal now returns StateProposition to preserve persistent identity/state compositions.

Registered base inventory **238 -> 237**. Semantic primitive candidates fall **117 -> 116**.

## Reduction checkpoint 41 — Detected is Happen Sense

`Detected A X C` -> `Happen Sense A C X`.

Without an explicit channel, existentially quantify a SenseChannel. This preserves the distinction between detecting a stimulus and interpreting its meaning.

Registered base inventory **237 -> 236**. Semantic primitive candidates fall **116 -> 115**.

## Reduction checkpoint 42 — MethodFor is Purpose(Method,...)

Methods are SemanticValues with intended EventSpec goals, already covered by Purpose:

`MethodFor M E` -> `Purpose M E`.

Registered base inventory **236 -> 235**. Semantic primitive candidates fall **115 -> 114**.

## Reduction checkpoint 43 — Using folds into Use

Use now has Event/EventSpec instrument-role frames in addition to the existing three-argument instrument Process frame:

`Using E I` -> `Use E I`.

Registered base inventory **235 -> 234**. Unresolved candidates fall **36 -> 35**.

## Reduction checkpoint 44 — Habitual is contextual High OccurrenceRate

The former `Habitual` operator used contextual recurrence frequency rather than a separate event ontology. The same meaning is expressed by the existing frequency scale:

`Habitual E I` -> `High OccurrenceRate E I`.

The relevant threshold remains contextual in ordinary discourse and therefore remains unsuitable as an implicit magical condition. Registered base inventory **234 -> 233**. Derived candidates fall **5 -> 4**.

## Reduction checkpoint 45 — Depth is the third Span axis

Height and Width already use the first two axes of `Span`. Depth now uses the third/depth axis:

- explicit frame: `Depth X F` -> `Span X F @@@`;
- ordinary contextual frame: `Depth X` -> `Span X @@@`.

The contextual shorthand is not sufficient for objective magical geometry; an explicit CoordinateFrame should be supplied there. Registered base inventory **233 -> 232**. Unresolved candidates fall **35 -> 34**.

## Reduction checkpoint 46 — Thank is addressed Say of gratitude

Thanking does not require a separate Process root:

`Thank S A` -> `Say S (GratefulTo S A) A`.

`GratefulTo` gains an optional explicit `:basis` role when the reason for thanks is stated. Because `Say` does not entail the truth of its content, this composition allows both sincere and insincere thanks. Registered base inventory **232 -> 231**. Unresolved candidates fall **34 -> 33**.

## Reduction checkpoint 47 — Apologize is addressed Say of remorse

An apology is represented as an utterance expressing remorse:

- contextual offense: `Apologize S A` -> `Say S (RemorseFor S) A`;
- explicit offense: `Apologize S A :offense X` -> `Say S (RemorseFor S X) A`.

`RemorseFor` therefore gains a contextual one-argument ordinary-language frame. Objective use should state the remorse basis explicitly. `Say` again does not entail sincere remorse. Registered base inventory **231 -> 230**. Unresolved candidates fall **33 -> 32**.

## Reduction checkpoint 48 — Whenever is During(SufficientFor...)

Recurring conditional truth does not need a dedicated wrapper:

- explicit interval: `Whenever C K I` -> `During SufficientFor C K I`;
- contextual interval: `Whenever C K` -> `During SufficientFor C K ThisInterval`.

`ThisInterval` supplies the active discourse interval. Ordinary discourse may resolve it contextually; objective magic requires a formally resolved interval reference. Registered base inventory **230 -> 229**. Derived candidates fall **4 -> 3**.

## Reduction checkpoint 49 — NextOccurrence is First(EventSpec)

`First` is generalized from ordered Sequences to contextual occurrence ordering:

`NextOccurrence E` -> `First E`.

The EventSpec frame means the next/first matching occurrence after the active temporal reference and retains contextual metadata, so it is not an implicit objective magical selector. Registered base inventory **229 -> 228**. Derived candidates fall **3 -> 2**.

## Reduction checkpoint 50 — Redistribute is Transfer over a Distribution

The general `Transfer` Process now covers Distribution movement:

- `Redistribute D S T` -> `Transfer D S T`;
- target-profile form -> `Transfer D S T :profile P`.

The named profile role is meaningful when the transferred value is a Distribution. Registered base inventory **228 -> 227**. Derived candidates fall **2 -> 1**.

## Reduction checkpoint 51 — Because is typed contextual Explains

A generic English `Because` mixes physical causation, epistemic evidence, and discourse explanation. Those exact families are already separate.

For ordinary discourse explanation:

`Because target reason` -> `Explains reason target`.

The Proposition+Proposition `Explains` frame is contextual. Technical/magical expressions should continue to use `Cause`, `EvidenceFor`, or an explicit Explanation as appropriate. Registered base inventory **227 -> 226**. Unresolved candidates fall **32 -> 31**.

## Reduction checkpoint 52 — Almost is false-side low boundary distance

`Distance` now has general contextual boundary-distance frames over gradable PropertyDescriptors and EventSpecs.

- property: `Almost P X` -> `And {Not P X,Low Distance P X}`;
- event: `Almost E` -> `And {Not Happen E,Low Distance E}`.

This preserves both parts of “almost”: the condition did not hold, but it was close to the relevant boundary. Objective magic must provide a registered metric/threshold rather than inherit contextual `Low`. Registered base inventory **226 -> 225**. Derived candidates fall **1 -> 0**.

## Reduction checkpoint 53 — Should is High Evaluate

The ordinary weaker recommendation modality is the contextual high region of the existing evaluation scale:

`Should A E` -> `High Evaluate A E`.

This does not collapse `Obligated`: recommendation remains contextual evaluation rather than a deontic duty relation. Registered base inventory **225 -> 224**. Unresolved candidates fall **31 -> 30**.

## Reduction checkpoint 54 — DesignedFor is Purpose

`Purpose` already denotes a persistent intended goal/function relation and remains distinct from current `Use`. For artifacts, the world classifier may ground Purpose in recognized design/construction evidence:

`DesignedFor X E` -> `Purpose X E`.

Registered base inventory **224 -> 223**. Unresolved candidates fall **30 -> 29**.

## Reduction checkpoint 55 — Learn is typed Begin-state acquisition

The generic `Learn` root bundled several acquisition results that the state vocabulary already distinguishes:

- facts/Information -> `Begin Know learner content`;
- skill/EventSpec -> `Begin Can learner event`;
- other semantic comprehension -> `Begin Understand learner content`.

`Can` is now explicitly state-typed so `Begin Can` is a proper EventSpec. Teaching is correspondingly agentive `Cause` of the appropriate acquisition transition. Registered base inventory **223 -> 222**. Unresolved candidates fall **29 -> 28**.

## Reduction checkpoint 56 — Generic is contextual high prevalence

The existing formal collection machinery expresses the actual generic reading without a dedicated quantifier:

`Generic [x:D] P(x)` -> `High Ratio Count Collect [x:D] P(x) Count Collect [y:D]`.

`High` gains a Ratio frame. The threshold is contextual/world-standard, so this remains distinct from strict `All` and fixed-majority `Most`. Registered base inventory **222 -> 221**. Unresolved candidates fall **28 -> 27**.

## Reduction checkpoint 57 — Size is the contextual evaluation frame of Extent

The ordinary holistic size scale is one reading of the general extent family:

- `Size X` -> `Extent X` where an EvaluationValue is expected;
- `HighSize` / `LowSize` -> `HighExtent` / `LowExtent`;
- Grow's before/after comparison uses `Extent`.

The pre-existing `Extent(entity) -> Region` frame remains type-distinct. Registered base inventory **221 -> 220**. Unresolved candidates fall **27 -> 26**.

## Reduction checkpoint 58 — Span is axis-indexed Extent

Projected frame-axis length is also an extent reading. The former Span frames move intact onto `Extent`:

- primary/up axis: `Extent X F @`;
- width axis: `Extent X F @@`;
- depth/third axis: `Extent X F @@@`;
- contextual frame shorthand remains available in ordinary discourse.

Registered base inventory **220 -> 219**. Unresolved candidates fall **26 -> 25**.

## Reduction checkpoint 59 — CommittedTo is contextual Obligation

The social commitment state established by a promise is represented as deontic/social responsibility with an interpersonal context:

`CommittedTo S E A` -> `Obligated S E :context A`.

`Obligated` gains the optional named `:context` role. Promise remains a speech event plus the beginning of this state:

`And {Say S (Obligated S E :context A) A,Begin (Obligated S E :context A)}`.

Registered base inventory **219 -> 218**. Unresolved candidates fall **25 -> 24**.

## Reduction checkpoint 60 — Teleport is a discontinuous At-state transition

Teleportation does not need an independent motion root. It is the boundary transition between spatial states without introducing a continuous Move Path:

- explicit source: `Teleport X G S` -> `And {End At X S,Begin At X G}`;
- source omitted: `Teleport X G` -> `Begin At X G`.

Because the composition uses At-state boundaries rather than Move, it retains the discontinuous relocation reading. Registered base inventory **218 -> 217**. Unresolved candidates fall **24 -> 23**.

## Reduction checkpoint 61 — Write is agentive Begin Exist for a Sign

The executable Write frame required only an agent and a Sign token. Its truth conditions are represented as:

`Write A S` -> `Cause A Begin Exist S`, with S typed Sign.

Exist is generalized to semantic values so Sign tokens can participate directly in existence-state transitions. The begun existence state persists until separately ended. Registered base inventory **217 -> 216**. Unresolved candidates fall **23 -> 22**.

## Reduction checkpoint 62 — Read is interpreted Sign Sense

The general Sense root now has a contextual Sign frame:

`Read A S` -> `If Sign S (Sense A S)`.

The explicit Sign condition preserves the former typed role; the two-argument Sense frame means successful perception plus semantic interpretation. Raw sensing continues to use the explicit channel form, and channel/language mapping remains context-resolved unless stated separately. Registered base inventory **216 -> 215**. Unresolved candidates fall **22 -> 21**.

## Reduction checkpoint 63 — Grab is concurrent onset of Touch and Control

Touch is explicitly state-typed so grabbing can be represented as the simultaneous acquisition of contact and control:

`Grab A T` -> `And {Begin Touch A T,Begin Control A T}`.

This is more precise than either Begin Touch or Begin Control alone. The draft Hand Old Name is rebuilt as `«Control«LifeMatter»Part»`; Wrist follows that rebuilt Hand name. Registered base inventory **215 -> 214**. Unresolved candidates fall **21 -> 20**.

## Reduction checkpoint 64 — Consent is Say of explicit permission

`Permitted` gains an EventSpec+`:authority` frame. Consent is the communicative act of asserting that the proposed EventSpec is permitted by the consenter:

- no addressee: `Say C (Permitted E :authority C)`;
- addressed consent: `Say C (Permitted E :authority C) R`.

This remains distinct from Want/Intend and from agent-scoped permission. Registered base inventory **214 -> 213**. Unresolved candidates fall **20 -> 19**.

## Reduction checkpoint 65 — Refuse is Say of permission denial

Refusal is represented as communicating the negation of that same authority-scoped permission:

- no addressee: `Say R (Not (Permitted E :authority R))`;
- addressed refusal: `Say R (Not (Permitted E :authority R)) Q`.

The construction encodes the explicit rejection act without reducing it to mere absence of intention. Registered base inventory **213 -> 212**. Unresolved candidates fall **19 -> 18**.

## Reduction checkpoint 66 — Deceive is causation of false belief

Agentive `Cause` now accepts a StateProposition effect. Successful deception about proposition P is:

`If (Not P) (Cause D (Believe T P))`.

The false-content condition and successful caused-belief state are explicit, while the method remains unconstrained. Registered base inventory **212 -> 211**. Unresolved candidates fall **18 -> 17**.

## Reduction checkpoint 67 — Sever is causative End Whole

`Whole` is now explicitly state-typed. Agentive `Cause` also accepts optional named `:instrument`.

- `Sever A T` -> `Cause A (End Whole T)`;
- `Sever A T :instrument I` -> `Cause A (End Whole T) :instrument I`.

This preserves structural integrity loss while delegating narrower cutting/material mechanics to the world model. Registered base inventory **211 -> 210**. Unresolved candidates fall **17 -> 16**.

## Resolution checkpoint 68 — Meaning survives as a primitive candidate

`Meaning(Sign, content)` cannot be replaced by `About`, `Equal`, `EvidenceFor`, `Part`, or `Purpose` without changing the semantic relation. Meaning connects a representation token to conveyed content and explicitly permits language/context-sensitive ambiguity.

Registered base inventory remains **210**. Semantic primitive candidates rise **114 -> 115**; unresolved candidates fall **16 -> 15**.

## Resolution checkpoint 69 — About survives as a primitive candidate

`About(Information, topic)` is topicality of semantic content. It is not Sign interpretation, evidence, purpose, or mereological containment. Information may be about a topic independently of which Sign carries it.

Registered base inventory remains **210**. Semantic primitive candidates rise **115 -> 116**; unresolved candidates fall **15 -> 14**.

## Resolution checkpoint 70 — DistributionOf survives as a primitive candidate

`DistributionOf(resource, host)` is the core constructor/accessor that yields a `Distribution`. Existing `Density` consumes a Distribution and cannot construct the same field object; Transfer manipulates one but also does not create the resource/host distribution relation.

Registered base inventory remains **210**. Semantic primitive candidates rise **116 -> 117**; unresolved candidates fall **14 -> 13**.

## Resolution checkpoint 71 — TotalAmount survives as a primitive candidate

`TotalAmount(distribution, region?)` represents aggregate/integrated quantity over a Distribution. A general replacement using `Density` would require integration over arbitrary world-model geometry, which the current arithmetic/collection operators do not provide.

Registered base inventory remains **210**. Semantic primitive candidates rise **117 -> 118**; unresolved candidates fall **13 -> 12**.

## Resolution checkpoint 72 — Beneficiary survives as a primitive candidate

`Beneficiary(event, entity)` is the event-role relation for who benefits. It cannot be replaced exactly by recipient, `Give`/`Transfer`, `Have`, or `Purpose`: benefit need not involve receipt or possession, and it may be unintended.

Registered base inventory remains **210**. Semantic primitive candidates rise **118 -> 119**; unresolved candidates fall **12 -> 11**.

## Resolution checkpoint 73 — Bite survives as a primitive candidate

`Bite(agent, target)` encodes oral action manner. Generic `Attack`, `Eat`, `Touch`, and `Damage` cover possible consequences or contexts of a bite, not the same event type. The current core has no general exact manner/body-part operator that would recover biting.

Registered base inventory remains **210**. Semantic primitive candidates rise **119 -> 120**; unresolved candidates fall **11 -> 10**.

## Resolution checkpoint 74 — CamouflagedAgainst survives as a primitive candidate

`CamouflagedAgainst(subject, background, observer?)` is contextual perceptual camouflage. Concrete `ColorOf`/`TextureOf` values do not by themselves define camouflage, and the current `Contrast` relation is discourse contrast rather than a perceptual similarity metric.

Registered base inventory remains **210**. Semantic primitive candidates rise **120 -> 121**; unresolved candidates fall **10 -> 9**.

## Resolution checkpoint 75 — Climb survives as a primitive candidate

`Climb(agent, target)` is a locomotion manner rather than a directional synonym for `Move`. A climb may be upward, downward, across, or over a target and carries supported/contact traversal semantics that generic `Move`, `Up`, `Touch`, and `Surface` do not jointly encode as an exact event type.

Registered base inventory remains **210**. Semantic primitive candidates rise **121 -> 122**; unresolved candidates fall **9 -> 8**.

## Resolution checkpoint 76 — Contrast survives as a primitive candidate

`Contrast(a, b)` is a contextual discourse concession/contrast relation. Replacing it with `And` would preserve co-truth but erase the represented tension/expectation relation. The core has no general discourse-coherence or expectation-violation operator that restores that meaning exactly.

Registered base inventory remains **210**. Semantic primitive candidates rise **122 -> 123**; unresolved candidates fall **8 -> 7**.

## Resolution checkpoint 77 — Dodge survives as a primitive candidate

`Dodge(agent, threat?)` is evasive action intended to avoid a threat. `Move` does not encode avoidance intent, `Prevent` suppresses an EventSpec rather than merely avoiding its contact/effect on the agent, and `Attempt` does not supply the evasive-action manner.

Registered base inventory remains **210**. Semantic primitive candidates rise **123 -> 124**; unresolved candidates fall **7 -> 6**.

## Resolution checkpoint 78 — Fall survives as a primitive candidate

`Fall(theme)` is a non-agentive, context-governed motion manner. Generic `Move` does not encode gravity/down-frame or uncontrolled-fall semantics and requires an objective goal or Path for magical execution; `At`, `Offset`, and direction constructors do not recover that missing event meaning.

Registered base inventory remains **210**. Semantic primitive candidates rise **124 -> 125**; unresolved candidates fall **6 -> 5**.

## Resolution checkpoint 79 — Forgive survives as a primitive candidate

`Forgive(forgiver, offender, :offense?)` means relinquishing blame/resentment toward an offender. It is not exactly `End Hate`, `End Angry`, or `Not ResponsibleFor`: forgiveness can coexist with anger, remembered wrongdoing, and continued attribution of responsibility.

Registered base inventory remains **210**. Semantic primitive candidates rise **125 -> 126**; unresolved candidates fall **5 -> 4**.

## Resolution checkpoint 80 — Reflexive survives as a primitive candidate

`Reflexive(event)` marks an EventSpec as an involuntary/reflex response. `Not Intend` is broader than reflexivity, while `Cause` says why an event occurs rather than whether its execution mode is reflexive. The current core has no general agency/control-mode relation that reconstructs this exactly.

Registered base inventory remains **210**. Semantic primitive candidates rise **126 -> 127**; unresolved candidates fall **4 -> 3**.

## Resolution checkpoint 81 — Jump survives as a primitive candidate

`Jump(agent, goal?)` encodes launch/airborne locomotion manner. Generic `Move` captures displacement but not that manner, and the current Path/direction machinery does not provide a general motion-manner constructor that would make Jump compositional without reintroducing the same distinction elsewhere.

Registered base inventory remains **210**. Semantic primitive candidates rise **127 -> 128**; unresolved candidates fall **3 -> 2**.

## Resolution checkpoint 82 — Limp survives as a primitive candidate

`Limp(agent)` encodes asymmetric/impaired gait manner. `Move` does not encode gait, and `Damage` is only a graded damage attribute: damaged entities need not limp, and limping can have causes other than current Damage.

Registered base inventory remains **210**. Semantic primitive candidates rise **128 -> 129**; unresolved candidates fall **2 -> 1**.

## Resolution checkpoint 83 — Stab survives as a primitive candidate

`Stab(agent, target, instrument?)` encodes a directed puncturing/thrust action manner. `Attack`, `Damage`, `Touch`, and `Use` can all participate in descriptions of individual stabbings but do not preserve the same event type or truth conditions.

Registered base inventory remains **210**. Semantic primitive candidates rise **129 -> 130**; unresolved candidates fall **1 -> 0**.

The explicit unresolved-candidate audit is now complete. This does not freeze the 130 retained semantic primitive candidates; future generalizations may still reduce them.

## Reduction checkpoint 84 — ChangeRate and OccurrenceRate become Rate

The repeated-label audit found one real shared semantic operation rather than an English-only naming coincidence.

Both former roots measure something **per Time**:

- `ChangeRate(value: Quantity, interval)` returned value-dimension / Time;
- `OccurrenceRate(event: EventSpec, interval?)` returned occurrence Frequency, i.e. Time^-1.

They are now typed frames of one semantic primitive:

- `Rate(value: Quantity, interval: TimeInterval)` -> Quantity<value-dimension/Time>;
- `Rate(event: EventSpec, interval: TimeInterval)` -> Quantity:Frequency;
- `Rate(event: EventSpec)` -> contextual Quantity:Frequency.

The input type makes the intended frame exact. No separate rate-kind enum is introduced, so this removes a genuine duplicated primitive distinction rather than hiding it behind a value.

Current examples therefore use `Rate Density This ThisInterval`, `High Rate Move This Here ThisInterval`, and `Divide @ Rate Move This Here`.

Registered base inventory **210 -> 209**. Semantic primitive candidates **130 -> 129**. Unresolved candidates remain **0**.

The next high-leverage experiment remains motion/action manner.

## Audit checkpoint 85 — motion/action-manner family does not yet yield a net reduction

The detailed family experiment is recorded in `docs/MOTION_ACTION_MANNER_AUDIT.md`.

The current general machinery can express facts around the seven target roots but not their exact missing event distinctions:

- Bite needs oral/teeth-closing interaction;
- Climb needs supported surface traversal;
- Dodge needs evasive realization relative to a threat;
- Fall needs gravity/world-force-driven uncontrolled motion;
- Jump needs self-launch and unsupported/airborne motion;
- Limp needs asymmetric/impaired gait;
- Stab needs directed puncturing/thrust interaction.

A generic `Manner` operator with one unique value per old root would replace seven roots with at least eight registrations. Factoring the strongest apparent overlaps also loses: Jump/Fall require a shared airborne feature plus distinct launch vs gravity/control semantics, while Bite/Stab require a shared penetration/contact feature plus distinct oral vs thrust semantics.

No root is removed and no new manner layer is added. Registered base inventory remains **209**; semantic primitive candidates remain **129**; unresolved candidates remain **0**.

The next second-pass family is measurement/descriptor architecture.

## Reduction checkpoint 86 — Duration is temporal Extent

The measurement/descriptor family audit is recorded in `docs/MEASUREMENT_DESCRIPTOR_AUDIT.md`.

`Duration(Event) -> Quantity<Time>` carries no semantic distinction beyond the temporal extent of a concrete Event. The existing `Extent` root already covers spatial Region extent, holistic size/extent, and frame-axis Length. It now gains the type-distinct frame:

`Extent(Event) -> Quantity:Time`.

Because Event is a separate input type and the result is Time-valued, this introduces no ambiguity and no new selector/value atom.

The standalone `Duration` root is removed. The historical `«DurationUnit»` Old Name remains available, rebuilt from `Extent + Unit` while retaining its canonical Time-unit meaning.

The rest of the measurement family remains for now: descriptor identities such as Mass/Heat/Light/Volume/Length are used by generic attribute machinery; arbitrary Area/Volume are not products of one axis; Density still carries field/distribution semantics; Damage/Hunger/Loudness are independent ordered scales; Hard/Sharp lack reusable underlying scalar descriptors; Form/TextureOf have different profile types; and DistributionOf/TotalAmount preserve field construction/integration operations.

Registered base inventory **209 -> 208**. Semantic primitive candidates **129 -> 128**. Unresolved candidates remain **0**.

The next second-pass family is social/affective structure.

## Audit checkpoint 87 — social/affective family does not yet yield a net reduction

The detailed family experiment is recorded in `docs/SOCIAL_AFFECTIVE_AUDIT.md`.

The audit tests generic attitude/social-relation wrappers, evaluator-based reductions, a one-dimensional affect-valence model, Opposite pairs, epistemic reconstructions of Trust, compositional analyses of fear/jealousy/compassion/gratitude/grief/remorse/shame, institutional relation factoring, Reputation aggregation, and the existing Forgive alternatives.

No exact net reduction survives:

- one `Attitude` or `SocialRelation` root plus one atomic kind per old root increases semantic inventory;
- `Evaluate` does not preserve affection, admiration, respect, hatred, or trust truth conditions;
- Happy/Sad and Love/Hate are not exact semantic-axis inverses;
- Trust is interpersonal reliance rather than one unspecified Believe/Confidence/Expect proposition;
- the directed appraisal emotions require different basis/target content;
- ParentOf, FriendOf, SpouseOf, EngagedTo, Have, Own, and ResponsibleFor remain different relations;
- Reputation lacks an exact current aggregation over community Evaluate values;
- Forgive remains distinct from End Angry, End Hate, or Not ResponsibleFor.

No root is removed and no generic social/attitude layer is added. Registered base inventory remains **208**; semantic primitive candidates remain **128**; unresolved candidates remain **0**.

The next second-pass family is agency/mental stance/deontics/event roles.

## Audit checkpoint 88 — agency/deontic/event-role family does not yet yield a net reduction

The detailed family experiment is recorded in `docs/AGENCY_DEONTIC_AUDIT.md`.

The audit tests a generic Stance wrapper, Plan into Intend, Want into Intend/Evaluate, Expect into Believe/Confidence, Can into Permitted/epistemic possibility, Permitted/Obligated deontic duality, Purpose into Intend/Plan, Beneficiary into Purpose/transfer/possession, Attempt into intention plus occurrence, and Reflexive into Not Intend/Cause.

No exact reduction survives:

- Want, Expect, Intend, and Plan preserve different desire, anticipation, commitment, and represented-course content;
- Can is capability whereas Permitted is authorization;
- current Cuspell has no exact EventSpec negation/deontic axioms that make Permitted and Obligated logical duals;
- Purpose can belong to artifacts, Methods, and other non-agent semantic values;
- Beneficiary can be indirect or unintended;
- Attempt is an actual effort event;
- Reflexive is a specific involuntary execution mode.

A generic Stance/Modal/Role layer would need one atomic mode for each of these distinctions and would increase the inventory.

No root is removed. Registered base inventory remains **208**; semantic primitive candidates remain **128**; unresolved candidates remain **0**.

The next second-pass family is space/topology/geometry.

## Reduction checkpoint 89 — Inside and Outside reduce through exact Region topology

The detailed family experiment is recorded in `docs/SPACE_TOPOLOGY_AUDIT.md`.

The first-pass correction remains semantically valid: Inside is **not** plain In, and Outside is **not** Not In.

The second pass succeeds by generalizing already-existing topological roots rather than erasing the missing distinctions:

- `Touch(Region,Region)` means boundary contact;
- `Overlap(Region,Region)` means nontrivial shared interior extent.

That gives exact compositions:

- `Inside A R` -> `And {In A R,Not Touch Extent A R}`;
- `Outside A R` -> `Not Overlap Extent A R`.

The Inside composition keeps subset containment and explicitly excludes boundary contact. The Outside composition permits boundary-only contact but rejects partial or full interior overlap. Therefore the old distinction from In / Not In is preserved.

No new topology-kind enum or replacement root is introduced. Inside and Outside are removed.

The remaining spatial roots retain distinct semantics: At is anchor location, Center/Edge/Sides/Surface are different geometry selectors, Joined is structural rather than mere contact, Part is mereological rather than spatial containment, Through constrains path/event traversal, ShapeLike carries template comparison, and Offset/Toward construct location/direction values.

Registered base inventory **208 -> 206**. Semantic primitive candidates **128 -> 126**. Unresolved candidates remain **0**.

The next second-pass family is communication/information/epistemics/discourse.

## Audit checkpoint 90 — communication/epistemic/discourse family does not yet yield a net reduction

The detailed family experiment is recorded in `docs/EPISTEMIC_DISCOURSE_AUDIT.md`.

The audit tests Believe through Confidence thresholds, Know as true belief, Remember through temporal/persistent Know, Understand through Know, Assert through Say, Infer through EvidenceFor plus belief-state change, EvidenceFor through About/Meaning/Cause, Explains through EvidenceFor/Cause, AnswerFor through topicality/evidence, Sense through interpretation, and Contrast through conjunction/expectation.

No exact reduction survives:

- Believe is a persistent mind-model state, while High Confidence is a contextual Quantity threshold and already serves probability-standard language;
- Know remains factive and is not defined as mere true belief;
- Remember and Understand cover memory/retention and comprehension rather than Know aliases;
- Assert carries assertion force beyond generic Say;
- Infer is an actual reasoning EventSpec;
- About, Meaning, EvidenceFor, and Explains preserve different semantic relations;
- AnswerFor is the typed relation between Information and QuestionContent;
- Sense is perceptual acquisition, not sign Meaning;
- Contrast is discourse tension/concession, not And or a particular mind's Expect state.

A generic EpistemicRelation/SpeechForce/DiscourseRelation wrapper would need one atom per surviving distinction and therefore would not reduce the inventory.

No root is removed. Registered base inventory remains **206**; semantic primitive candidates remain **126**; unresolved candidates remain **0**.

The next second-pass family is time/event occurrence.

## Audit checkpoint 91 — temporal core is already a compact four-root basis

The detailed family experiment is recorded in `docs/TIME_EVENT_AUDIT.md`.

The audit tests Simultaneous through Overlap and Equal/Begin/End, Before through endpoint comparison, During through temporal boundaries, and Happen through During or generic existential event matching.

No exact reduction survives:

- Overlap is weaker than Simultaneous;
- TimePoint Simultaneous can be written as Equal, but Event Simultaneous retains timing/tolerance semantics not captured by equal starts, exact coextensive boundaries, or overlap;
- expressing Event Before through `End A` and `Begin B` still needs primitive TimePoint Before;
- During covers EventSpec activity and Proposition holding across supplied temporal targets in addition to concrete containment;
- Happen is the EventSpec existential-occurrence bridge and is weaker/different from being active across an interval.

No new temporal tolerance/matching root is introduced merely to hide an existing distinction.

No root is removed. Registered base inventory remains **206**; semantic primitive candidates remain **126**; unresolved candidates remain **0**.

The next second-pass family is operational/body states.

## Audit checkpoint 92 — operational/body states do not collapse to two Boolean axes

The detailed family experiment is recorded in `docs/OPERATIONAL_STATE_AUDIT.md`.

The audit tests Awake/Sleep as negations or one consciousness dimension, Open/Locked as negations or one accessibility dimension, and Locked through Can/Control/Permitted.

No exact reduction survives:

- Not Awake is broader than Sleep because a subject can be unconscious, anesthetized, comatose, or otherwise non-awake without sleeping;
- Not Sleep is broader than Awake for the same reason;
- Locked is a mechanism/security state, not Not Open;
- Open is a contextual configuration state, not Not Locked;
- capability, authorization, and control do not reconstruct the lock state;
- generic state dimensions would need one atomic value per current distinction and therefore would not reduce the inventory.

The shared transition abstraction already exists: `Begin` / `End` supplies wake/sleep/open/close/lock/unlock event meanings over the persistent states.

No root is removed. Registered base inventory remains **206**; semantic primitive candidates remain **126**; unresolved candidates remain **0**.

The next second-pass family is foundational ontology/classification.

## Audit checkpoint 93 — foundational ontology/classification remains a language-level basis

The detailed family experiment is recorded in `docs/FOUNDATIONAL_ONTOLOGY_AUDIT.md`.

The audit tests whether the fourteen foundational roots can be reduced through semantic types, world classifiers, collections/mereology, or generic state machinery.

No exact reduction survives:

- implementation types such as Entity, Path, Region, Sign, and Unit are metalanguage/typing constraints, not free meaning-bearing replacements for written roots;
- Thing is not Exist: an identifiable Entity may retain identity while not actively existing;
- Group is not a semantic Collection and cannot be defined by current non-empty membership; Member is distinct from Part, In, and Have;
- Path and Region preserve ordered-trajectory versus spatial-subset semantics;
- Sign is not equivalent to currently having Meaning, and Rule is narrower than generic Information;
- Matter and Unit retain generic classification distinctions not generated by the surviving descriptor/type machinery;
- Exist, Life, Magic, and Whole are independent persistent state predicates rather than values of a smaller generated state basis;
- moving Female into one atomic world classifier would merely relocate the same irreducible distinction and would alter its current Property typing if converted to a Kind-valued name.

Draft Old Names may still be rebuilt, but none of their dependencies changes this result.

No root is removed. Registered base inventory remains **206**; semantic primitive candidates remain **126**; unresolved candidates remain **0**.

The next second-pass family is **change / causation / transfer / control**: `Change`, `Cause`, `Give`, `Transfer`, and `Control`.

## Audit checkpoint 94 — Give reduces to coordinated possession boundaries

The detailed family experiment is recorded in `docs/CHANGE_TRANSFER_CONTROL_AUDIT.md`.

The audit tests `Change`, `Cause`, `Give`, `Transfer`, and `Control` as one event-structure family.

One exact reduction survives.

`Give giver theme recipient` is not simply generic `Transfer theme giver recipient`, because Transfer does not inherently assert possession. However, the possession specification already defines Give completely as:

`Concurrent EndHave giver theme BeginHave recipient theme`

The former Give frame contributes no extra manner, ownership, permission, location, beneficiary, or control semantics. The root is therefore removed.

The other four roots remain:

- Change is the generic value-bearing Attribute transition;
- Cause is causal relation/agentive causation;
- Transfer is generic resource/value source-to-destination transfer, including amount and Distribution-profile semantics;
- Control is a persistent controller-target relation distinct from Have/Own/Can/Cause/Prevent.

Give-dependent draft Old Names are rebuilt with Transfer wording at unchanged costs.

Registered base inventory **206 -> 205**; semantic primitive candidates **126 -> 125**; unresolved candidates remain **0**; derived candidates remain **0**.

Checkpoint 94 completes the second-pass audit of all ten primitive families.

The next reduction stage is a **global cross-family closure pass** over the remaining 125 semantic primitive candidates.

