# Primitive vs Derived Inventory Audit

_Status: design-stage full classification of the executable core_

## Why this exists

The executable registry count is **not** the same thing as the number of primitive Cuspell roots.

The registry also contains formal constructors, deictic references, closed-domain values, and meanings that are likely compositional but have not yet been rewritten.

Machine-readable source:

- `language/core/inventory_roles.json`

A regression requires every current core entry to have exactly one inventory role.

## Current counts

After the current reduction checkpoints, the registered core/base inventory contains **234 entries**.

| Inventory role | Count | Meaning |
| --- | ---: | --- |
| semantic primitive candidate | 114 | Survives the first classification as a distinct reusable semantic/root candidate. Not frozen. |
| derived candidate | 5 | Strong candidate for systematic composition instead of an independent root. |
| unresolved candidate | 35 | Suspicious, but no exact replacement is settled yet. |
| formal constructor | 54 | Logic/arithmetic/quantification/collection/time/content/name machinery; tracked separately from lexical roots. |
| reference form | 16 | Deictic/anaphoric forms such as This, Self, Here, Now. |
| domain value | 10 | Closed-set values such as phase and sense-channel values, plus Zero. |

The earlier direct noun/name candidate category is now empty.

The key result is:

> **Only 114 of 234 registered base entries currently look like semantic primitive candidates.**

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
- Cat → `«LowSize«MoveLifeThing»»`
- Water → `«LiquidMatter»`
- Body → `«LifeMatter»`
- Hand → `«Grab«LifeMatter»Part»`
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

`Teach T L C` -> `Cause T Learn L C`

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

This preserves descriptor use such as `Almost HighHunger Self`. The tail draft Old Name is rebuilt as `«HighLength«LifeMatter»Part»`.

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

## Important geometry distinction

`Inside` and `Outside` remain current primitive candidates because their strict boundary semantics are not equivalent to `In` and `Not In`.

## Derived candidates

- Almost
- Habitual
- NextOccurrence
- Redistribute
- Whenever

## Unresolved candidates

- About
- Apologize
- Because
- Beneficiary
- Bite
- CamouflagedAgainst
- Climb
- CommittedTo
- Consent
- Contrast
- Deceive
- Depth
- DesignedFor
- DistributionOf
- Dodge
- Fall
- Forgive
- Generic
- Grab
- Jump
- Learn
- Limp
- Meaning
- Read
- Reflexive
- Refuse
- Sever
- Should
- Stab
- Teleport
- Thank
- TotalAmount
- Write

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
2. reduce Redistribute and other remaining derived candidates where exact event/change semantics are available;
3. revisit the 35 unresolved candidates after those general mechanisms exist;
4. continue the audit of the 114 semantic primitive candidates themselves.

The objective is the smallest inventory that preserves the distinctions Cuspell genuinely needs.
