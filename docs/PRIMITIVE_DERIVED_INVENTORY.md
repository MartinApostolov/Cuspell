# Primitive vs Derived Inventory Audit

_Status: design-stage full classification of the executable core_

## Why this exists

The executable registry count is **not** the same thing as the number of primitive Cuspell roots.

The registry also contains formal constructors, deictic references, closed-domain values, and meanings that are likely compositional but have not yet been rewritten.

Machine-readable source:

- `language/core/inventory_roles.json`

A regression requires every current core entry to have exactly one inventory role.

## Current counts

After noun migration, extrema consolidation, Unit-family consolidation, and the exact-composition batch, the executable core contains **270 entries**.

| Inventory role | Count | Meaning |
| --- | ---: | --- |
| semantic primitive candidate | 120 | Survives the first classification as a distinct reusable semantic/root candidate. Not frozen. |
| derived candidate | 26 | Strong candidate for systematic composition instead of an independent root. |
| unresolved candidate | 46 | Suspicious, but no exact replacement is settled yet. |
| formal constructor | 52 | Logic/arithmetic/quantification/collection/time/content/name machinery; tracked separately from lexical roots. |
| reference form | 16 | Deictic/anaphoric forms such as This, Self, Here, Now. |
| domain value | 10 | Closed-set values such as phase and sense-channel values, plus Zero. |

The earlier direct noun/name candidate category is now empty.

The key result is:

> **120 of 270 executable entries currently look like semantic primitive candidates.**

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

## Completed family reduction: exact compositions

Seven entries have now been removed because their current executable meanings are exactly expressible through surviving machinery:

- `Between(v, lo, hi)` → `More v lo And More hi v`;
- `Former(P)` → `Past P And Not Present P`;
- `KnowAnswer(mind, q)` → some Information `i` such that `Know mind i And AnswerFor i q`;
- `Ask(speaker, q, addressee?)` → `Say` with `QuestionContent`;
- `AwayFrom(r)` → `Opposite Toward r`;
- `TimeOverlap(a,b)` → polymorphic `Overlap a b`;
- `DirectPart(a,b)` → `Part(a,b)` with no distinct intermediate Part.

This batch adds no new root. It broadens existing `Know`, `Opposite`, and `Overlap` frames where the normative semantics already required those domains. Draft bridge and corpse Old Names were rebuilt rather than protecting `Between` or `Former`.

## Important geometry distinction

`Inside` and `Outside` remain current primitive candidates because their strict boundary semantics are not equivalent to `In` and `Not In`.

## Derived candidates

- Almost
- Always
- ApproxEqual
- CertainTo
- Completed
- Continue
- Decreasing
- Future
- Grow
- Habitual
- Increasing
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
- Unit

“Primitive candidate” means only that no cleaner exact reduction has been demonstrated yet.

## Next reduction order

The highest-value next families are:

1. typed-zero/tolerance support for Increasing / Decreasing / Stable;
2. Confidence thresholds for PossibleTo / ProbableTo / CertainTo;
3. temporal/frequency wrappers;
4. threshold-property machinery for Long / Injured and later Big / Small / Hungry / Sated;
5. the 47 unresolved candidates after those general mechanisms exist;
6. another audit of the 120 primitive candidates themselves.

The objective is the smallest inventory that preserves the distinctions Cuspell genuinely needs.
