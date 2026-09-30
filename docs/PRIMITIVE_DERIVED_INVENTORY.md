# Primitive vs Derived Inventory Audit

_Status: design-stage full classification of the executable core_

## Why this exists

The executable registry count is **not** the same thing as the number of primitive Cuspell roots.

The registry also contains formal constructors, deictic references, closed-domain values, and meanings that are likely compositional but have not yet been rewritten.

Machine-readable source:

- `language/core/inventory_roles.json`

A regression requires every current core entry to have exactly one inventory role.

## Current counts

After the third reduction checkpoint, the registered core/base inventory contains **266 entries**.

| Inventory role | Count | Meaning |
| --- | ---: | --- |
| semantic primitive candidate | 119 | Survives the first classification as a distinct reusable semantic/root candidate. Not frozen. |
| derived candidate | 23 | Strong candidate for systematic composition instead of an independent root. |
| unresolved candidate | 46 | Suspicious, but no exact replacement is settled yet. |
| formal constructor | 52 | Logic/arithmetic/quantification/collection/time/content/name machinery; tracked separately from lexical roots. |
| reference form | 16 | Deictic/anaphoric forms such as This, Self, Here, Now. |
| domain value | 10 | Closed-set values such as phase and sense-channel values, plus Zero. |

The earlier direct noun/name candidate category is now empty.

The key result is:

> **Only 119 of 266 registered base entries currently look like semantic primitive candidates.**

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
- Cat → `«Small«MoveLifeThing»»`
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

`DirectPart(A,B)` is compositional: `Part(A,B)` plus the absence of any distinct intermediate X with `Part(A,X)` and `Part(X,B)`. Identity guards use `Same`/`Not` when the Part model permits reflexive membership.

The parser regression uses explicit zero-mana grouping because a flat chain of `And` and `Not` has more than one legal scope.

This reduces the registered base inventory **273 -> 272** and the derived-candidate count **29 -> 28**.

## Completed family reduction: Former

`Former(P)` is exactly `Past(P) And Not Present(P)`. The standalone wrapper is removed, and the draft corpse Old Name is rebuilt as `«PastLifeNotLife«LifeMatter»»`.

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

## Important geometry distinction

`Inside` and `Outside` remain current primitive candidates because their strict boundary semantics are not equivalent to `In` and `Not In`.

## Derived candidates

- Almost
- Always
- CertainTo
- Completed
- Continue
- Future
- Grow
- Habitual
- Injured
- Long
- NextOccurrence
- Often
- Ongoing
- Past
- PossibleTo
- Present
- ProbableTo
- Rarely
- Redistribute
- Sometimes
- Stable
- Stop
- Whenever

## Unresolved candidates

- About
- Apologize
- Because
- Beneficiary
- Big
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
- Height
- Hungry
- ImportantTo
- Jump
- Learn
- Limp
- LocalDensity
- Meaning
- Members
- Period
- Promise
- Read
- Reflexive
- Refuse
- Sated
- Sever
- Should
- Small
- Stab
- Teach
- Teleport
- Thank
- TotalAmount
- Using
- Width
- Write

## Formal constructors

- Add
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
- Detected
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
- MethodFor
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
- Prefer
- Purpose
- Region
- Remember
- RemorseFor
- Reputation
- Respect
- ResponsibleFor
- Rule
- Sad
- Same
- Say
- Sense
- ShameAbout
- ShapeLike
- Sharp
- SiblingOf
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

1. explicit/contextual tolerance semantics for Stable and other threshold predicates;
2. Confidence thresholds for PossibleTo / ProbableTo / CertainTo;
3. temporal/frequency wrappers;
4. threshold-property machinery for Long / Injured and later Big / Small / Hungry / Sated;
5. the 46 unresolved candidates after those general mechanisms exist;
6. another audit of the 120 primitive candidates themselves.

The objective is the smallest inventory that preserves the distinctions Cuspell genuinely needs.
