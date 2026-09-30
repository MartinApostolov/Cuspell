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

This audit classifies every current entry so future reduction work can target the real primitive inventory rather than the raw registry size.

Machine-readable source:

- `language/core/inventory_roles.json`

## Current counts

After removing the accidentally reintroduced `Inside` and `Outside` aliases, the executable core contains **282 entries**.

| Inventory role | Count | Meaning |
| --- | ---: | --- |
| semantic primitive candidate | 117 | Survives the first classification as a distinct reusable semantic/root candidate. Not frozen. |
| derived candidate | 36 | Strong candidate for systematic composition instead of an independent root. |
| unresolved candidate | 47 | Suspicious, but no exact replacement is settled yet. |
| formal constructor | 50 | Logic/arithmetic/quantification/collection/time/content/name machinery; track separately from lexical roots. |
| reference form | 16 | Deictic/anaphoric forms such as This, Self, Here, Now. |
| domain value | 10 | Closed-set values such as phase and sense-channel values, plus Zero. |
| name candidate | 6 | Ordinary direct noun Kind that should be tested for migration into the naming system. |

The key result is:

> **Only 117 of 282 entries currently look like semantic primitive candidates on the first full audit.**

That is not a final target. Some of those 117 may still collapse after better abstractions are introduced.

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

These entries have a plausible systematic decomposition or family-level replacement. Their exact derivation hints are stored in `inventory_roles.json`.

Especially high-value families:

### Graded/threshold states

- Long
- Injured

The likely direction is ordered attribute + threshold rather than separate primitive state.

### Epistemic thresholds

- PossibleTo
- ProbableTo
- CertainTo

The likely direction is `Confidence` plus thresholds.

### Change-rate states

- Increasing
- Decreasing
- Stable

The likely direction is `ChangeRate` compared against typed zero/tolerance.

### Extrema selectors

- Nearest
- Farthest
- Highest
- Lowest

The likely direction is one generic minimum/maximum selector over a measure/key.

### Frequency/time wrappers

- Past
- Present
- Future
- Ongoing
- Completed
- Former
- Habitual
- Whenever
- Sometimes
- Often
- Rarely
- Always
- NextOccurrence

These should be challenged against explicit occurrence/time relations and frequency machinery instead of being accepted as unrelated primitives.

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

These remain open design work. The audit intentionally does not pretend that a vague English paraphrase is an exact Cuspell derivation.

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

These are executable and may still require written signs/runes, but they should not inflate claims such as “Cuspell has 282 semantic roots.”

A later rune-design pass can separately decide whether some formal constructors are punctuation/grammar rather than runes.

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

These are a separate inventory problem from semantic roots.

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

These are members of closed semantic families, not independent open-class concepts.

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

“Primitive candidate” means only:

> no cleaner exact reduction has been demonstrated yet.

It does **not** mean the entry is protected from later removal.

## Reduction order from here

The next cleanup should attack families rather than isolated English words:

1. migrate the six direct noun/name candidates;
2. implement a generic extrema selector to replace four selectors;
3. build typed-zero/tolerance support and reduce Increasing/Decreasing/Stable;
4. consolidate epistemic confidence thresholds;
5. consolidate temporal/frequency wrappers;
6. test graded-property thresholds such as Long/Injured;
7. revisit the 47 unresolved entries after the new abstractions exist;
8. re-audit the 117 primitive candidates after each family reduction.

The objective is not an arbitrary numerical quota. The objective is the smallest inventory that preserves the distinctions the language genuinely needs.
