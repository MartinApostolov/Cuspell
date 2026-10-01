# Primitive vs Derived Inventory Audit

_Status: design-stage full classification of the executable core_

## Why this exists

The executable registry count is **not** the same thing as the number of primitive Cuspell roots.

The registry also contains formal constructors, deictic references, closed-domain values, and meanings that are likely compositional but have not yet been rewritten.

Machine-readable source:

- `language/core/inventory_roles.json`

A regression requires every current core entry to have exactly one inventory role.

## Current counts

After the current reduction checkpoints, the registered core/base inventory contains **208 entries**.

| Inventory role | Count | Meaning |
| --- | ---: | --- |
| semantic primitive candidate | 128 | Survives the current exact-reduction audit as a distinct reusable semantic/root candidate. Not frozen permanently. |
| derived candidate | 0 | No currently registered base entry remains in the derived-candidate bucket. |
| unresolved candidate | 0 | The explicit unresolved bucket is now empty after exact-reduction review. Future audits may still revisit retained candidates. |
| formal constructor | 54 | Logic/arithmetic/quantification/collection/time/content/name machinery; tracked separately from lexical roots. |
| reference form | 16 | Deictic/anaphoric forms such as This, Self, Here, Now. |
| domain value | 10 | Closed-set values such as phase and sense-channel values, plus Zero. |

The earlier direct noun/name candidate category is now empty.

The key result is:

> **128 of 208 registered base entries currently survive as semantic primitive candidates.**

That is still not a final root count.

## Completed family reduction: direct noun Kinds

The following no longer exist as primitive Kind roots:

- Cat
- Hand
- Human
- Water
- Body
- Sound

They now exist as world concepts + provisional Old Names:

- Human → `«Know«MoveLifeThing»»`
- Cat → `«LowExtent«MoveLifeThing»»`
- Water → `«LiquidMatter»`
- Body → `«LifeMatter»`
- Hand → `«Control«LifeMatter»Part»`
- Sound → `«HearingThing»`

Named Kinds are valid binder domains, e.g. `a:«Know«MoveLifeThing»»`.

## Completed family reduction: extrema selectors

The four specialized operators:

- Nearest
- Farthest
- Highest
- Lowest

have been removed.

They are replaced by two generic tie-preserving formal constructors:

- `MinBy collection binder key`
- `MaxBy collection binder key`

Examples:

- nearest to Here → `MinBy C x:Entity Distance $x Here`
- farthest from Here → `MaxBy C x:Entity Distance $x Here`
- lowest Mass → `MinBy C x:Entity Mass $x`
- highest Mass → `MaxBy C x:Entity Mass $x`

Both return the full collection of tied extrema. Use `Unique` when exactly one member is required.


## Completed family reduction: exact derived wrappers

Three more registered surfaces have been removed because the current language already expresses their complete executable meaning:

- ordered `Between(value, lower, upper)` -> `More value lower And More upper value`;
- `Ask(speaker, QuestionContent, addressee?)` -> `Say speaker QuestionContent addressee?`;
- `TimeOverlap` -> the general `Overlap` relation, which now has Event/Event and TimeInterval/TimeInterval frames.

This reduces the registered base inventory from **277 to 274** without changing the semantic-primitive-candidate count. The draft bridge Old Name was rebuilt so it no longer depends on `Between`.

Geometric/spatial betweenness is not silently equated with ordered numeric betweenness; if future corpus pressure needs a segment/geodesic relation, it should be designed as its own exact geometry construction.

## Completed family reduction: direction converse

`AwayFrom(reference)` no longer has its own root. `Toward(reference)` constructs a `Direction`, and `Opposite` now accepts `Direction`, so the exact replacement is:

`Opposite Toward reference`

This reduces the registered base inventory **274 -> 273** and the derived-candidate count **30 -> 29**.

## Completed family reduction: immediate-part relation

`DirectPart(A,B)` is compositional: `Part(A,B)` plus the absence of any distinct intermediate X with `Part(A,X)` and `Part(X,B)`. Identity guards use Entity `Equal`/`Not` when the Part model permits reflexive membership.

The parser regression uses explicit zero-mana grouping because a flat chain of `And` and `Not` has more than one legal scope.

This reduces the registered base inventory **273 -> 272** and the derived-candidate count **29 -> 28**.

## Completed family reduction: Former

`Former(P)` is now `Before(P,Now) And Not(P)`: bare state P supplies the present/reference-time reading, and the draft corpse Old Name is `«BeforeLifeNowNotLife«LifeMatter»»`.

This reduces the registered base inventory **272 -> 271** and derived candidates **28 -> 27**.

## Completed family reduction: Information type and KnowAnswer

The direct `Information` Kind root duplicated the semantic type `Information`. Removing that Kind makes `i:Information` bind abstract Information values instead of Entity instances.

`Know` now has its documented Information-content frame. Therefore `KnowAnswer(mind,Q)` is exactly `Some i:Information And {Know mind $i,AnswerFor $i Q}`.

This reduces the registered base inventory **271 -> 269**, primitive candidates **120 -> 119**, and derived candidates **27 -> 26**.

## Completed family reduction: trend direction

`ChangeRate` now accepts a Quantity expression and returns that quantity's dimension divided by Time. `Zero` is polymorphic to the expected Quantity dimension. Therefore `Increasing` and `Decreasing` are removed in favor of explicit rate comparisons.

This reduces the registered base inventory **269 -> 267** and derived candidates **26 -> 24**.

## Completed family reduction: approximate equality

`ApproxEqual(A,B,T)` is the conjunction that neither signed difference exceeds tolerance T:

`And {Not More Add A Opposite B T, Not More Add B Opposite A T}`

This reduces the registered base inventory **267 -> 266** and derived candidates **24 -> 23**.

## Completed family reduction: existential occurrence

For EventSpec meanings, `Sometimes(event, interval?)` is the same existential occurrence claim already expressed by `Happen(event, interval?)`: at least one matching concrete Event occurs in the relevant interval/domain.

The separate `Sometimes` root is removed. This reduces the registered base inventory **266 -> 265** and derived candidates **23 -> 22**.

## Completed family reduction: group member collection

`Member` now covers both membership in an explicit Collection and membership in a group Entity. Therefore the former functional wrapper:

`Members(group)`

is exactly:

`Collect x:Entity Member $x group`

The standalone `Members` root is removed. This reduces the registered base inventory **265 -> 264** and unresolved candidates **46 -> 45**.

## Completed family reduction: stopping concrete events

The existing `End` root is output-typed for concrete Events:

- in a TimePoint context, `End E` denotes E's ending TimePoint;
- in an EventSpec context, `End E` denotes terminating that ongoing Event.

The separate `Stop` root is therefore removed. This reduces the registered base inventory **264 -> 263** and derived candidates **22 -> 21**.

## Completed family reduction: teaching

The stronger teaching meaning is successful causation of learning, not merely saying information. With the existing agentive Cause frame:

Teaching is now typed by the learner-state transition: facts/information use `Cause T Begin Know L C`; skills use `Cause T Begin Can L E`; other semantic comprehension uses `Cause T Begin Understand L C`.

The standalone `Teach` root is removed. This reduces the registered base inventory **263 -> 262** and unresolved candidates **45 -> 44**.

## Completed family reduction: ordered preference

`Evaluate(evaluator,target)` yields an ordered EvaluationValue, so:

`Prefer E A B` -> `More Evaluate E A Evaluate E B`

The EvaluationValue-specific More frame returns StateProposition, preserving the former root's state semantics. The standalone `Prefer` root is removed.

This reduces the registered base inventory **262 -> 261** and semantic primitive candidates **119 -> 118**.

## Completed family reduction: sibling relation

`SiblingOf A B` is the persistent state that A and B are distinct Entities sharing at least one parent:

`Some p:Entity And {ParentOf $p A,ParentOf $p B,Not Equal A B}`

State-preserving typing on Equal/And/Some keeps the derived form typed as StateProposition. The standalone `SiblingOf` root is removed.

This reduces the registered base inventory **261 -> 260** and semantic primitive candidates **118 -> 117**.

## Completed family reduction: contextual High thresholds

`High` is one productive contextual standard constructor over ordered values. Compounded with an AttributeDescriptor it produces a first-class PropertyDescriptor.

Therefore:

- `Long X` -> `HighLength X`;
- `Hungry X` -> `HighHunger X`;
- `Often E I` -> `High OccurrenceRate E I`.

Near-threshold use is now expressed through the general boundary-distance machinery rather than `Almost`; for example `And {Not HighHunger Self,Low Distance HighHunger Self}`. The tail draft Old Name is rebuilt as `«HighLength«LifeMatter»Part»`.

Net inventory change: **260 -> 258**. Derived candidates **21 -> 19**, unresolved candidates **44 -> 43**, formal constructors **52 -> 53**, semantic primitive candidates remain **117**.

## Completed family reduction: epistemic Confidence thresholds

The two convenience predicates now use the existing ordered Confidence degree directly:

- `PossibleTo M P` -> `More Confidence M P Zero`;
- `ProbableTo M P` -> `High Confidence M P`.

At this checkpoint `CertainTo` remained because exact certainty is not merely contextual high confidence; the later certainty-endpoint pass below completes the family.

Inventory change: **258 -> 256**. Derived candidates **19 -> 17**.

## Completed family reduction: injury threshold

`Damage(subject)` already supplies the ordered injury degree, and the productive High + AttributeDescriptor rule preserves state typing for EvaluationValue attributes. Therefore:

- `Injured X` -> `HighDamage X`.

The draft wound Old Name is rebuilt as `«HighDamage«LifeMatter»Part»`.

Inventory change: **256 -> 255**. Derived candidates **17 -> 16**.

## Completed family reduction: stable rate

`Stable` no longer needs a dedicated Relation:

- exact stability -> `Equal ChangeRate V I Zero`;
- tolerance-bounded stability -> `And {Not More ChangeRate V I T,Not More Opposite ChangeRate V I T}`.

This is the same two-sided tolerance logic already used by compositional ApproxEqual, applied to rate around zero.

Inventory change: **255 -> 254**. Derived candidates **16 -> 15**.

## Completed family reduction: contextual Low thresholds

`Low` is the productive counterpart to `High`: it means below the relevant contextual standard and is not the logical negation of `High`.

Therefore:

- `Rarely E I` -> `Low OccurrenceRate E I`.

This pass removes one derived convenience root while adding one reusable formal constructor, so the registered inventory remains **254**. Derived candidates **15 -> 14** and formal constructors **53 -> 54**.

## Completed family reduction: satiation threshold

Because `Hunger(subject)` is an ordered EvaluationValue AttributeDescriptor, the same Low + AttributeDescriptor machinery yields a state Property:

- `Sated X` -> `LowHunger X`.

LowHunger is not `Not HighHunger`; middle hunger values can satisfy neither threshold. Registered inventory **254 -> 253**. Unresolved candidates **43 -> 42**.

## Completed family reduction: evaluator-relative importance

`Evaluate(evaluator,target)` already provides the ordered EvaluationValue used for preference. Importance is its contextual high-threshold predicate:

- `ImportantTo target evaluator` -> `High Evaluate evaluator target`.

Registered inventory **253 -> 252**. Unresolved candidates **42 -> 41**.

## Completed family reduction: certainty endpoint

Canonical Confidence now has explicit normalized endpoints:

- `Zero` = complete rejection;
- `«ConfidenceUnit» @` = complete confidence/certainty.

Therefore:

- `CertainTo M P` -> `Equal Confidence M P «ConfidenceUnit» @`.

This removes the last standalone epistemic confidence-threshold convenience root. Registered inventory **252 -> 251**. Derived candidates **14 -> 13**.

## Completed family reduction: continuation boundary

The concrete-event reading of Continue is already expressible with the generic event-boundary and prevention machinery:

- `Continue E` at the present boundary -> `Prevent End E Interval Now Now`.

`End(E)` is selected in its EventSpec “terminate this Event” frame because Prevent requires an EventSpec. The zero-width current interval scopes prevention to the present boundary rather than forbidding the event from ever ending.

The contextual EventSpec reading first resolves the uniquely ongoing occurrence to an EventRef in ordinary discourse; objective magic must identify that Event explicitly.

Registered inventory **251 -> 250**. Derived candidates **13 -> 12**.

## Completed family reduction: recurrence period

`Period` is the reciprocal of occurrence frequency rather than an independent temporal primitive:

- contextual: `Period E` -> `Divide @ OccurrenceRate E`;
- explicit scope: `Divide @ OccurrenceRate E I`.

Because Frequency has dimension Time^-1, the reciprocal is exactly Quantity<Time>. A zero/undefined occurrence rate gives no finite period rather than requiring another lexical meaning.

Registered inventory **250 -> 249**. Unresolved candidates **41 -> 40**.

## Completed family reduction: present reference time

`Present` does not need a dedicated Operator once unmarked state semantics are made explicit:

- state: `Present P` -> bare `P`;
- event: `Present E` -> `During E Now`.

A bare StateProposition is evaluated at the active discourse/evaluation reference time. This is the same reference that Present previously selected explicitly. EventSpecs are not truth-bearing states, so their present reading remains an explicit ongoing-occurrence test at Now.

Registered inventory **249 -> 248**. Derived candidates **12 -> 11**.

## Completed family reduction: completed-event aspect

`Completed` duplicates the EventSpec reading of `Past`. Past is extended with explicit TimePoint and TimeInterval reference/scope frames, so all former Completed forms remain expressible:

- `Completed E` -> `Past E`;
- `Completed E T` -> `Past E T`.

Registered inventory **248 -> 247**. Derived candidates **11 -> 10**.

## Completed family reduction: ongoing-event aspect

`During` now accepts EventSpecs directly:

- `Ongoing E T` -> `During E T`;
- contextual present occurrence -> `During E Now`.

For an EventSpec, During means at least one matching occurrence is active across the supplied point/interval. Registered inventory **247 -> 246**. Derived candidates **10 -> 9**.

## Completed family reduction: Big threshold

A single contextual ordered `Size(subject) -> EvaluationValue` descriptor now supplies holistic ordinary size comparison.

- `Big X` -> `HighSize X`.

This pass adds Size while removing Big, so the registered total remains **246**. Unresolved candidates remain **40**.

## Completed family reduction: Small threshold

The same Size scale supplies the low threshold:

- `Small X` -> `LowSize X`.

Registered inventory **246 -> 245**. Unresolved candidates **40 -> 39**.

## Completed family reduction: Past as Before

`Before` now accepts EventSpec/StateProposition patterns against a TimePoint (and EventSpec against an explicit TimeInterval scope):

- `Past X` -> `Before X Now`;
- `Past E T` -> `Before E T`.

The pattern/state frames are contextual, so this does not silently make discourse-time claims objective magic. The corpse draft Old Name is rebuilt from Past to Before + Now.

Registered inventory **245 -> 244**. Derived candidates **9 -> 8**.

## Completed family reduction: Future as reversed Before

The converse temporal reading is already available by reversing the generalized Before relation:

- `Future X` -> `Before Now X`.

For EventSpecs this means a matching occurrence begins after the reference point; for states it means the state holds at a relevant later time.

Registered inventory **244 -> 243**. Derived candidates **8 -> 7**.

## Completed family reduction: Always as proposition During

`During` now has a Proposition + TimeInterval frame whose semantics are “the proposition holds throughout the supplied interval.” Therefore:

- `Always P I` -> `During P I`;
- `Never P I` remains compositional as `During Not P I`.

Registered inventory **243 -> 242**. Derived candidates **7 -> 6**.

## Completed family reduction: LocalDensity into Density

`Density` now has a Distribution + Region frame:

- `LocalDensity D R` -> `Density D R`.

The one-argument entity Density AttributeDescriptor remains unchanged.

Registered inventory **242 -> 241**. Unresolved candidates **39 -> 38**.

## Completed family reduction: Height into Span

Introduce one general axis-indexed extent relation:

- `Span X F @` = extent of X along the frame's primary/up axis.

Therefore `Height X F` is exactly `Span X F @`.

This pass removes Height while adding Span, so the registered total remains **241**. Unresolved candidates remain **38**.

## Completed family reduction: Width into Span

The same relation selects the frame's designated width axis with `@@`:

- `Width X F` -> `Span X F @@`.

Registered inventory **241 -> 240**. Unresolved candidates **38 -> 37**.

## Completed family reduction: Grow into constrained Size change

`Change` now accepts a Proposition constraint over event-local BeforeValue/AfterValue snapshots. Growth is therefore:

`Grow X` -> `Change X Size More AfterValue Size X BeforeValue Size X`.

This states exactly that X undergoes a Size change whose after-value exceeds its before-value; it does not invent a hidden target size.

Registered inventory **240 -> 239**. Derived candidates **6 -> 5**.

## Completed family reduction: Promise as speech plus commitment transition

A successful Promise already consists of two independently represented facts: a speech act conveying the commitment and the beginning of the commitment state.

`Promise S A E` -> `And {Say S CommittedTo S E A A,Begin CommittedTo S E A}`.

Because `Say` does not entail the truth of its content while `Begin CommittedTo` establishes the state transition, the composition preserves the performative semantics without making the promised Event happen.

Registered inventory **239 -> 238**. Unresolved candidates **37 -> 36**.

## Completed family reduction: Same into Equal

`Equal` is typed equality for all compatible semantic values. Entity equality is identity equality, so a separate Same relation duplicates that exact case:

- `Same A B` -> `Equal A B`.

Equal now yields a StateProposition, preserving the state typing required by SiblingOf and other identity-constrained state compositions.

Registered inventory **238 -> 237**. Semantic primitive candidates **117 -> 116**.

## Completed family reduction: Detected into Happen Sense

Sense already denotes successful information-acquisition/perception events. Detection is therefore occurrence of the corresponding Sense EventSpec:

- explicit channel: `Detected A X C` -> `Happen Sense A C X`;
- channel omitted: `Some c:SenseChannel Happen Sense A $c X`.

Registered inventory **237 -> 236**. Semantic primitive candidates **116 -> 115**.

## Completed family reduction: MethodFor into Purpose

A Method is a semantic/procedural value, and Purpose already relates any SemanticValue to an intended EventSpec goal:

- `MethodFor M E` -> `Purpose M E`.

Registered inventory **236 -> 235**. Semantic primitive candidates **115 -> 114**.

## Completed family reduction: Using into Use

The general Use root now carries both its Process frame and instrument-role relation frames:

- process: `Use agent instrument goal` -> EventSpec;
- participant relation: `Use event-or-EventSpec instrument` -> Proposition.

Therefore `Using E I` is exactly `Use E I`.

Registered inventory **235 -> 234**. Unresolved candidates **36 -> 35**.

## Completed family reduction: habitual recurrence threshold

The standalone contextual `Habitual` operator duplicated the frequency machinery already used by `Often`/`Rarely`. A habitual event is now written as the event's occurrence rate crossing the relevant contextual habituality threshold:

- `Habitual E I` -> `High OccurrenceRate E I`.

The threshold remains contextual in ordinary discourse, so this does not make habituality objective magic. Registered inventory **234 -> 233**. Derived candidates **5 -> 4**.

## Completed family reduction: depth into Span

`Span` now supports a contextual frame shorthand as well as the explicit coordinate-frame form. The frame's third/depth axis is `@@@`:

- explicit: `Depth X F` -> `Span X F @@@`;
- contextual ordinary-language shorthand: `Depth X` -> `Span X @@@`.

Objective magic should supply the coordinate frame explicitly. Registered inventory **233 -> 232**. Unresolved candidates **35 -> 34**.

## Completed family reduction: thanking as speech of gratitude

`Thank` is an expressive speech act, not a separate physical event primitive. It is represented by saying a gratitude proposition to the addressee:

- `Thank S A` -> `Say S (GratefulTo S A) A`;
- an explicit reason can be carried as `:basis` on `GratefulTo`.

Because `Say` does not entail the truth of its content, insincere thanks remain representable. Registered inventory **232 -> 231**. Unresolved candidates **34 -> 33**.

## Completed family reduction: apology as speech of remorse

`Apologize` is represented as an addressed utterance expressing remorse:

- contextual offense: `Apologize S A` -> `Say S (RemorseFor S) A`;
- explicit offense/basis: `Apologize S A :offense X` -> `Say S (RemorseFor S X) A`.

The one-argument `RemorseFor` frame is contextual ordinary-language shorthand; objective use should state the basis explicitly. Again, `Say` does not entail sincere remorse. Registered inventory **231 -> 230**. Unresolved candidates **33 -> 32**.

## Completed family reduction: recurring conditionals into During + SufficientFor

`Whenever` did not need a separate recurring-conditional root. The existing sufficiency relation can be required to hold throughout an interval:

- explicit interval: `Whenever C K I` -> `During SufficientFor C K I`;
- contextual interval: `Whenever C K` -> `During SufficientFor C K ThisInterval`, where `ThisInterval` supplies the active discourse interval.

When the interval is omitted in ordinary discourse, `ThisInterval` must resolve from context; objective magic may use the same form only when that interval reference is formally resolved. Registered inventory **230 -> 229**. Derived candidates **4 -> 3**.

## Completed family reduction: next occurrence into First(EventSpec)

`First` already means selection of the earliest member in an ordered domain. It now has a contextual EventSpec frame:

- `NextOccurrence E` -> `First E`.

In EventSpec use, `First E` means the next/first matching occurrence after the active temporal reference. The occurrence domain/reference remains contextual, preserving the former magic restriction. Registered inventory **229 -> 228**. Derived candidates **3 -> 2**.

## Completed family reduction: Redistribute into Transfer

`Transfer` is the general resource/value movement process. A Distribution is such a value, so redistribution is the Distribution-specific use of the same process:

- `Redistribute D S T` -> `Transfer D S T`;
- `Redistribute D S T P` -> `Transfer D S T :profile P`.

The optional named `:profile` role constrains the destination distribution profile. Registered inventory **228 -> 227**. Derived candidates **2 -> 1**.

## Completed family reduction: Because into contextual Explains

The generic English `Because` root mixed physical cause, evidence, and discourse explanation. The exact typed alternatives already exist: `Cause`, `EvidenceFor`, and `Explains`.

For ordinary clause-linking explanation:

- `Because target reason` -> `Explains reason target`.

`Explains(Proposition,Proposition)` is contextual, so this does not turn ordinary discourse explanation into objective magical causation or evidence. Registered inventory **227 -> 226**. Unresolved candidates **32 -> 31**.

## Completed family reduction: Almost into boundary distance

`Distance` now has contextual boundary-distance frames in addition to physical distance. For a gradable PropertyDescriptor P:

- `Almost P X` -> `And {Not P X,Low Distance P X}`.

For a near-but-nonoccurring EventSpec E:

- `Almost E` -> `And {Not Happen E,Low Distance E}`.

The `Not` term fixes the non-satisfying side of the boundary; `Low Distance ...` supplies the near-boundary condition. Objective magical use requires a registered boundary metric and explicit/non-contextual threshold model. Registered inventory **226 -> 225**. Derived candidates **1 -> 0**.

## Completed family reduction: Should into contextual evaluation

The weaker recommendation reading is the high end of the existing evaluator-relative scale:

- `Should A E` -> `High Evaluate A E`.

This remains contextual and distinct from `Obligated`. Registered inventory **225 -> 224**. Unresolved candidates **31 -> 30**.

## Completed family reduction: DesignedFor into Purpose

`Purpose` already means a persistent intended function/goal rather than current use. Artifact design supplies the objective grounding for that same relation:

- `DesignedFor X E` -> `Purpose X E`.

A temporary `Use` event still does not establish Purpose. Registered inventory **224 -> 223**. Unresolved candidates **30 -> 29**.

## Completed family reduction: Learn into typed state acquisition

The old generic `Learn` Process bundled several different state transitions. The minimized language now states the acquired state directly:

- fact/proposition or Information: `Learn L C` -> `Begin Know L C`;
- skill/capability EventSpec: `Learn L E` -> `Begin Can L E`;
- other semantic comprehension: `Learn L C` -> `Begin Understand L C`.

`Can` is now explicitly a StateProposition relation, so `Begin Can` is well typed. Teaching remains agentive `Cause` of whichever acquisition transition is intended. Registered inventory **223 -> 222**. Unresolved candidates **29 -> 28**.

## Completed family reduction: Generic into contextual prevalence

A generic statement is neither strict `All` nor fixed-majority `Most`. The existing collection/count/ratio machinery can state its actual contextual prevalence reading:

`Generic [x:D] P(x)` -> `High Ratio Count Collect [x:D] P(x) Count Collect [y:D]`.

`High` now accepts Ratio values. Its threshold remains contextual/world-standard, preserving the characteristic/normal reading without turning it into universal or strict-majority quantification. Registered inventory **222 -> 221**. Unresolved candidates **28 -> 27**.

## Completed family reduction: Size into Extent

The former `Size(subject) -> EvaluationValue` is the contextual holistic-evaluation frame of the more general `Extent` family:

- ordinary comparison: `Size X` -> `Extent X` when an EvaluationValue is expected;
- `HighSize X` / `LowSize X` -> `HighExtent X` / `LowExtent X`;
- directional growth uses event-local `Extent` before/after values.

The existing `Extent(entity) -> Region` frame remains available when a Region is expected. Registered inventory **221 -> 220**. Unresolved candidates **27 -> 26**.

## Completed family reduction: Span into Extent

Projected axis length is another exact extent reading, so `Extent` now carries the former Span frames:

- `Span X F @` -> `Extent X F @`;
- `Span X F @@` -> `Extent X F @@`;
- `Span X F @@@` -> `Extent X F @@@`;
- contextual no-frame forms remain available for ordinary discourse.

This consolidates occupied region, holistic size evaluation, and projected axis length under one extent family without collapsing their output types. Registered inventory **220 -> 219**. Unresolved candidates **26 -> 25**.

## Completed family reduction: CommittedTo into contextual Obligation

The social commitment state used by promises is a persistent deontic/social responsibility with an interpersonal context. `Obligated` now has an optional named `:context` role:

- `CommittedTo S E A` -> `Obligated S E :context A`.

The Promise composition is correspondingly `And {Say S (Obligated S E :context A) A,Begin (Obligated S E :context A)}`. This preserves the difference between the commitment state and the promise event while removing the duplicate state relation. Registered inventory **219 -> 218**. Unresolved candidates **25 -> 24**.

## Completed family reduction: Teleport into At-state boundaries

Teleportation is a discontinuous location-state transition rather than ordinary path-following Move:

- with explicit source: `Teleport X G S` -> `And {End At X S,Begin At X G}`;
- when the source is not stated: `Teleport X G` -> `Begin At X G`.

Because no `Move` or `Path` event is introduced, this keeps the discontinuous reading and preserves entity identity. Registered inventory **218 -> 217**. Unresolved candidates **24 -> 23**.

## Completed family reduction: Write into agentive Sign creation

The executable `Write` frame only required an agent and a Sign. Writing is therefore expressed as the agent causing that Sign's existence state to begin:

`Write A S` -> `Cause A Begin Exist S`, where S is typed Sign.

`Exist` now accepts semantic values such as Sign tokens as well as ordinary entities. Beginning existence supplies the persistent created-sign state unless separately ended. Registered inventory **217 -> 216**. Unresolved candidates **23 -> 22**.

## Completed family reduction: Read into interpreted Sign Sense

`Sense` now has a contextual two-argument Sign frame meaning successful perception plus semantic interpretation of the Sign:

`Read A S` -> `If Sign S (Sense A S)`.

The explicit `Sign S` condition preserves the former Sign typing. The two-argument Sense frame supplies successful perception plus interpretation, while channel/language mapping remains context-resolved in ordinary discourse. Registered inventory **216 -> 215**. Unresolved candidates **22 -> 21**.

## Completed family reduction: Grab into Touch + Control onset

`Touch` is now explicitly state-typed. Taking hold is the concurrent beginning of contact and control:

`Grab A T` -> `And {Begin Touch A T,Begin Control A T}`.

This preserves both physical contact and the acquisition-of-control component that plain Touch or Control alone would lose. The draft Hand Old Name is rebuilt as `«Control«LifeMatter»Part»`, and Wrist follows that rebuilt Hand name. Registered inventory **215 -> 214**. Unresolved candidates **21 -> 20**.

## Completed family reduction: Consent into addressed permission assertion

`Permitted` now has an EventSpec+`:authority` frame in addition to the agent-permission frame. Giving consent is represented as communicating that the event is permitted by the consenter:

- `Consent C E` -> `Say C (Permitted E :authority C)`;
- with requester/addressee R -> `Say C (Permitted E :authority C) R`.

This does not imply that C wants or intends E; it only communicates permission/consent. Registered inventory **214 -> 213**. Unresolved candidates **20 -> 19**.

## Completed family reduction: Refuse into addressed denial of permission

Explicit refusal is the communicative dual of consent:

- `Refuse R E` -> `Say R (Not (Permitted E :authority R))`;
- with requester/addressee Q -> `Say R (Not (Permitted E :authority R)) Q`.

Because `Say` does not entail truth beyond the speech-act content, this remains a communicative act rather than silently rewriting intention. Registered inventory **213 -> 212**. Unresolved candidates **19 -> 18**.

## Completed family reduction: Deceive into causation of false belief

`Cause` now accepts a persistent StateProposition as its caused effect. Successful deception concerning proposition P is:

`Deceive D T P` -> `If (Not P) (Cause D (Believe T P))`.

The composition preserves the two defining truth conditions encoded by the old root: P is false, and D successfully causes T to hold the corresponding belief state. The method remains unconstrained. Registered inventory **212 -> 211**. Unresolved candidates **18 -> 17**.

## Completed family reduction: Sever into causative loss of Whole

`Whole` is explicitly a persistent StateProposition, and agentive `Cause` gains an optional named `:instrument` role. Severing is therefore structural integrity loss:

- `Sever A T` -> `Cause A (End Whole T)`;
- with instrument I -> `Cause A (End Whole T) :instrument I`.

This preserves successful loss of structural wholeness while leaving narrower cutting/material physics to the world model. Registered inventory **211 -> 210**. Unresolved candidates **17 -> 16**.

## Retained primitive candidate: Meaning

`Meaning(Sign, content)` survives the current exact-reduction audit. Sign interpretation is not the same relation as Information topicality, equality, evidence, structural Part, or Purpose. Ambiguity and language/context sensitivity are part of the semantics, so replacing Meaning with those relations would lose truth conditions.

Registered inventory remains **210**. Semantic primitive candidates **114 -> 115**; unresolved candidates **16 -> 15**.

## Retained primitive candidate: About

`About(Information, topic)` survives independently of Meaning. Information can be about a topic without being a Sign that means that topic, and a Sign can mean Information whose topic is represented separately.

Registered inventory remains **210**. Semantic primitive candidates **115 -> 116**; unresolved candidates **15 -> 14**.

## Retained primitive candidate: DistributionOf

`DistributionOf(resource, host)` is the surviving Distribution-valued field constructor. None of the other current roots creates or retrieves the same Distribution object; Density consumes a Distribution rather than replacing it.

Registered inventory remains **210**. Semantic primitive candidates **116 -> 117**; unresolved candidates **14 -> 13**.

## Retained primitive candidate: TotalAmount

`TotalAmount(distribution, region?)` is an aggregate/integral over a Distribution. Local `Density` and ordinary arithmetic cannot reproduce this in the general continuum/world-model case without introducing a separate integration abstraction.

Registered inventory remains **210**. Semantic primitive candidates **117 -> 118**; unresolved candidates **13 -> 12**.

## Retained primitive candidate: Beneficiary

`Beneficiary(event, entity)` is a semantic role stating who benefits from an Event or EventSpec. Recipient, transfer, possession, and intended `Purpose` are all narrower or different relations; a beneficiary may receive nothing and may benefit unintentionally.

Registered inventory remains **210**. Semantic primitive candidates **118 -> 119**; unresolved candidates **12 -> 11**.

## Retained primitive candidate: Bite

`Bite(agent, target)` preserves an oral action manner that is not entailed by `Attack`, `Eat`, `Touch`, or `Damage`. Some bites are attacks or feeding acts and some cause damage, but none of those relations is equivalent to biting.

Registered inventory remains **210**. Semantic primitive candidates **119 -> 120**; unresolved candidates **11 -> 10**.

## Retained primitive candidate: CamouflagedAgainst

`CamouflagedAgainst(subject, background, observer?)` is observer/background-sensitive perceptual camouflage. `ColorOf` and `TextureOf` provide concrete appearance components, but the current core has no general visual/perceptual similarity metric that makes their conjunction equivalent to camouflage; discourse `Contrast` is a different relation.

Registered inventory remains **210**. Semantic primitive candidates **120 -> 121**; unresolved candidates **10 -> 9**.

## Retained primitive candidate: Climb

`Climb(agent, target)` is a locomotion manner, not simply upward motion. Climbing can be up, down, across, or over a target and characteristically depends on supported/contact traversal that generic `Move` does not encode.

Registered inventory remains **210**. Semantic primitive candidates **121 -> 122**; unresolved candidates **9 -> 8**.

## Retained primitive candidate: Contrast

`Contrast(a, b)` is a contextual discourse concession/contrast relation. Plain `And` can preserve that both sides hold, but it loses the represented expectation/tension relation; the current core has no general discourse-coherence or expectation-violation operator that reconstructs it exactly.

Registered inventory remains **210**. Semantic primitive candidates **122 -> 123**; unresolved candidates **8 -> 7**.

## Retained primitive candidate: Dodge

`Dodge(agent, threat?)` is evasive action intended to avoid a threat. Generic `Move` gives no avoidance intent, `Prevent` prevents an event rather than merely avoiding its effect/contact on the agent, and `Attempt` alone does not specify the evasive action family.

Registered inventory remains **210**. Semantic primitive candidates **123 -> 124**; unresolved candidates **7 -> 6**.

## Retained primitive candidate: Fall

`Fall(theme)` is non-agentive, context-governed falling motion. Generic `Move` requires a goal or Path for objective execution and does not encode the applicable gravity/down frame or uncontrolled motion manner; `At`/Offset/direction machinery likewise does not supply those semantics.

Registered inventory remains **210**. Semantic primitive candidates **124 -> 125**; unresolved candidates **6 -> 5**.

## Retained primitive candidate: Forgive

`Forgive(forgiver, offender, :offense?)` is the transition of relinquishing blame/resentment toward an offender. It is not `End Hate`, `End Angry`, or denial of `ResponsibleFor`: forgiveness may occur without hatred, may leave anger or responsibility intact, and does not erase memory of the offense.

Registered inventory remains **210**. Semantic primitive candidates **125 -> 126**; unresolved candidates **5 -> 4**.

## Retained primitive candidate: Reflexive

`Reflexive(event)` marks an EventSpec as occurring through an involuntary/reflex response rather than conscious choice. `Not Intend` is too broad: accidents, externally forced actions, habits, and unknown intentions need not be reflexes. `Cause` also describes causal dependence rather than agency/control mode.

Registered inventory remains **210**. Semantic primitive candidates **126 -> 127**; unresolved candidates **4 -> 3**.

## Retained primitive candidate: Jump

`Jump(agent, goal?)` preserves launch/airborne locomotion manner. Generic `Move` can describe displacement but not the jumping manner, and the core has no general motion-manner/trajectory constructor that makes the two exact equivalents.

Registered inventory remains **210**. Semantic primitive candidates **127 -> 128**; unresolved candidates **3 -> 2**.

## Retained primitive candidate: Limp

`Limp(agent)` preserves an asymmetric/impaired gait manner. It is not equivalent to `Move` plus `Damage`: Damage is a graded condition and neither causes nor entails limping, while limping can arise from multiple causes.

Registered inventory remains **210**. Semantic primitive candidates **128 -> 129**; unresolved candidates **2 -> 1**.

## Retained primitive candidate: Stab

`Stab(agent, target, instrument?)` preserves a directed puncturing/thrust action manner. `Attack`, `Damage`, `Touch`, and `Use` may describe intent, consequence, contact, or instrumentation around a stab, but none is equivalent to the stabbing event itself.

Registered inventory remains **210**. Semantic primitive candidates **129 -> 130**; unresolved candidates **1 -> 0**.

## Second-pass reduction: Rate consolidation

The repeated-English-subword audit found one genuine shared semantic abstraction:

- `ChangeRate(value, interval)`;
- `OccurrenceRate(event, interval?)`.

Both are per-Time rates. Their argument types already separate the two meanings, so one typed `Rate` root preserves both exactly:

- `Rate Quantity Interval` -> input dimension / Time;
- `Rate EventSpec Interval` -> Frequency;
- `Rate EventSpec` -> contextual Frequency.

The old `ChangeRate` and `OccurrenceRate` surfaces are removed rather than retained as aliases.

Registered inventory **210 -> 209**. Semantic primitive candidates **130 -> 129**.

## Important geometry distinction

`Inside` and `Outside` remain current primitive candidates because their strict boundary semantics are not equivalent to `In` and `Not In`.

## Derived candidates

None remain in the registered core.

## Unresolved candidates


## Formal constructors

- Add
- High
- AfterValue
- All
- And
- Ball
- BeforeValue
- Begin
- Collect
- Concurrent
- Count
- Counterfactual
- Directive
- Divide
- Each
- End
- Equal
- Filter
- First
- If
- Interval
- IntervalFor
- Last
- MaxBy
- MinBy
- More
- Most
- Multiply
- Name
- Not
- Opposite
- Or
- Partition
- Persist
- Power
- Preserve
- Prevent
- Question
- Random
- Ratio
- Repeat
- Requires
- Root
- Sequence
- Some
- SufficientFor
- Trigger
- True
- Tube
- UnavailableValueOf
- Unique
- UnknownValueOf
- When

## Reference forms

- Here
- Now
- Self
- That
- ThatEvent
- There
- They
- This
- ThisEvent
- ThisExplanation
- ThisInformation
- ThisInterval
- ThisMethod
- ThisPath
- ThisRegion
- You

## Domain values

- Gas
- Gustation
- Hearing
- Liquid
- Olfaction
- Plasma
- Solid
- TouchChannel
- Vision
- Zero

## First-pass semantic primitive candidates

- Admire
- Angry
- AnswerFor
- Area
- Assert
- At
- Attack
- Attempt
- Awake
- Before
- Believe
- Can
- Cause
- Center
- Change
- ChangeRate
- CompassionFor
- Confidence
- Control
- Damage
- Density
- Distance
- Duration
- During
- Eat
- Edge
- EngagedTo
- Evaluate
- EvidenceFor
- Exist
- Expect
- Explains
- Extent
- Fear
- Female
- Form
- FriendOf
- Give
- GratefulTo
- GrieveFor
- Group
- Happen
- Happy
- Hard
- Hate
- Have
- Heat
- Hunger
- In
- Infer
- Information
- Inside
- Intend
- JealousOf
- Joined
- Know
- Length
- Life
- Light
- Like
- Locked
- Loudness
- Love
- Magic
- Mass
- Matter
- Member
- Move
- Obligated
- OccurrenceRate
- Offset
- Open
- Outside
- Overlap
- Own
- ParentOf
- Part
- Path
- Permitted
- Phase
- Plan
- Purpose
- Region
- Remember
- RemorseFor
- Reputation
- Respect
- ResponsibleFor
- Rule
- Sad
- Say
- Sense
- ShameAbout
- ShapeLike
- Sharp
- Sides
- Sign
- Simultaneous
- Sleep
- SpouseOf
- Surface
- TextureOf
- Thing
- Through
- Touch
- Toward
- Transfer
- Trust
- Understand
- Use
- Volume
- Want
- Whole
- Worship

“Primitive candidate” means only that no cleaner exact reduction has been demonstrated yet.

## Next reduction order

The highest-value next families are:

1. temporal/frequency wrappers;
2. continue the unresolved-family audit now that no registered derived candidates remain;
3. the explicit unresolved-candidate bucket is now empty;
4. continue the deeper audit of the 128 semantic primitive candidates themselves as stronger general mechanisms appear.

The objective is the smallest inventory that preserves the distinctions Cuspell genuinely needs.
