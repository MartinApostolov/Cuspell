# Primitive vs Derived Inventory Audit

_Status: design-stage full classification of the executable core_

## Why this exists

The executable registry count is **not** the same thing as the number of primitive Cuspell roots.

The registry also contains:

- grammatical/formal constructors;
- deictic references;
- closed-domain values;
- ordinary nouns that should probably become Names;
- useful meanings that are likely compositional but have not yet been rewritten;
- unresolved convenience vocabulary.

Machine-readable source:

- `language/core/inventory_roles.json`

A regression now requires every core entry to have exactly one inventory role.

## Current counts

The executable core currently contains **284 entries**.

| Inventory role | Count | Meaning |
| --- | ---: | --- |
| semantic primitive candidate | 119 | Survives the first classification as a distinct reusable semantic/root candidate. Not frozen. |
| derived candidate | 36 | Strong candidate for systematic composition instead of an independent root. |
| unresolved candidate | 47 | Suspicious, but no exact replacement is settled yet. |
| formal constructor | 50 | Logic/arithmetic/quantification/collection/time/content/name machinery; track separately from lexical roots. |
| reference form | 16 | Deictic/anaphoric forms such as This, Self, Here, Now. |
| domain value | 10 | Closed-set values such as phase and sense-channel values, plus Zero. |
| name candidate | 6 | Ordinary direct noun Kind that should be tested for migration into the naming system. |

The key result is:

> **Only 119 of 284 entries currently look like semantic primitive candidates on the first full audit.**

That is not a final root count. Some of those 119 may still collapse after better abstractions are introduced.

## Important geometry correction

`Inside` and `Outside` remain current primitive candidates.

They are not aliases for `In` and `Not In`:

- `In` allows boundary contact;
- `Inside` requires strict interior placement;
- `Not In` merely says full containment fails;
- `Outside` requires no extent in the region interior.

Do not remove them until a smaller geometry construction can preserve those boundary distinctions.

## Name candidates

- Body
- Cat
- Hand
- Human
- Sound
- Water

These should be tested as concepts + Old/New Names instead of permanent primitive Kind roots.

## Derived candidates

- Almost
- Always
- ApproxEqual
- AwayFrom
- Between
- CertainTo
- Completed
- Continue
- Decreasing
- DirectPart
- Farthest
- Former
- Future
- Grow
- Habitual
- Highest
- Increasing
- Injured
- KnowAnswer
- Long
- Lowest
- Nearest
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
- TimeOverlap
- Whenever

Each has a derivation rationale/hint in `inventory_roles.json`.

High-value reduction families include:

- epistemic thresholds: PossibleTo / ProbableTo / CertainTo;
- rate states: Increasing / Decreasing / Stable;
- extrema selectors: Nearest / Farthest / Highest / Lowest;
- temporal/frequency wrappers: Past / Present / Future / Ongoing / Completed / Former / Habitual / Whenever / Sometimes / Often / Rarely / Always / NextOccurrence;
- exact logical/spatial compositions such as Between, DirectPart, AwayFrom, TimeOverlap, KnowAnswer;
- threshold properties such as Long and Injured.

## Unresolved candidates

- About
- Apologize
- Ask
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

These are intentionally not called derived yet. They need a better abstraction or a more exact semantic analysis before deletion.

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

These may still require written signs/runes, but they should not inflate claims about the number of lexical semantic roots.

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

These are a separate design inventory from semantic roots.

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

These are members of closed semantic families rather than open-class primitive concepts.

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

## Reduction order from here

1. migrate the six direct noun/name candidates;
2. implement one generic extrema selector to challenge four selectors;
3. make zero/tolerance dimension-aware and challenge Increasing/Decreasing/Stable;
4. consolidate epistemic confidence thresholds;
5. consolidate temporal/frequency wrappers;
6. test threshold-property machinery against Long/Injured and later Big/Small/Hungry/Sated;
7. revisit the 47 unresolved entries after those abstractions exist;
8. re-audit the 119 primitive candidates family by family.

The objective is not an arbitrary quota. It is the smallest inventory that preserves the distinctions Cuspell genuinely needs.
