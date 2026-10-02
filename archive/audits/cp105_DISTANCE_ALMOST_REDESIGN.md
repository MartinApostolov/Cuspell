# Checkpoint 105 — Distance / Almost Redesign

_Status: implemented targeted lexical redesign_

## Trigger

Checkpoint 99 identified `Distance` as the last genuine multi-frame lexical irregularity after later work resolved `Sense` and `Name`.

Before this checkpoint, one rune combined:

1. physical/spatial distance between two values -> `Quantity:Length`;
2. contextual distance from an Entity to satisfying a Property -> `EvaluationValue`;
3. contextual distance from an EventSpec to occurring -> `EvaluationValue`.

The latter two frames were introduced during root minimization to replace `Almost`.

## Audit finding

That reduction was not semantically valid.

An ordered value supplies only an ordering. It does **not** automatically supply:

- subtraction;
- a numerical metric;
- a satisfaction boundary represented as a value;
- a tolerance/near band;
- a progress metric for arbitrary EventSpecs.

Therefore:

`Low Distance LifeThis`

or

`Low Distance MoveThisHere`

did not actually derive “almost alive” / “almost moved here” from existing semantics. The old boundary-Distance frames hid a new domain-specific metric behind the physical word `Distance`.

## Alternatives considered

### Keep the overload

Rejected.

Physical Length and contextual logical/event nearness differ in semantic space, arity, output type, and objective-closure conditions.

### Add a generic explicit metric system

A fully honest generic abstraction would need some combination of:

- Metric/Scale values;
- explicit boundaries/targets;
- tolerance values;
- operations that produce a distance/gap in that metric.

That machinery may eventually be useful, but it is not present today. Adding it only to preserve the earlier deletion of `Almost` would be more language machinery than the recovered meaning warrants.

### Restore Almost

Chosen.

`Almost` directly names the contextual meaning that the attempted reduction failed to derive. It is meaning-bearing and therefore costs one rune.

This increases registered surface count, but semantic exactness outranks minimizing the raw count.

## New Distance

`Distance` now has exactly one frame:

`Distance(SpatialValue, SpatialValue) -> Quantity:Length`

It is physical/spatial separation only.

`SpatialValue` is a new **non-rune semantic type family** currently covering:

- Entity;
- Location;
- Region.

The applicable world model must fix the metric and any anchor/set-distance convention for non-point carriers.

Old Property/EventSpec boundary frames are removed.

## Restored Almost

`Almost` is restored as a formal Operator with two typed frames:

- `Almost(Proposition) -> Proposition`;
- `Almost(EventSpec) -> Proposition`.

Both have one semantic core:

> the target does not yet hold/occur but is close under the applicable domain-specific near-satisfaction/near-occurrence criterion.

Both frames are contextual.

Consequently ordinary assertions such as:

`Almost LifeThis.`

`Almost HighHunger Self.`

`Almost MoveThisHere.`

are grammatically/semantically valid.

But a magical command that depends on contextual Almost remains `SemanticallyIncomplete` until later world/execution machinery supplies an objective explicit criterion.

## Inventory effect

Before checkpoint 105:

- 205 registered entries;
- 125 semantic primitive candidates;
- 54 formal constructors;
- 256 frames;
- 48 multi-frame entries;
- 1 genuine multi-frame lexical irregularity.

After checkpoint 105:

- **206 registered entries**;
- **125 semantic primitive candidates**;
- **55 formal constructors**;
- **256 frames**;
- **48 multi-frame entries**;
- frame distribution: 22 zero-frame / 136 one-frame / 36 two-frame / 12 three-or-more;
- **0 genuine multi-frame lexical irregularities**.

`Almost` is classified as a formal constructor, not a semantic primitive candidate.

The registered count rises by one because checkpoint 105 reverses an invalid over-reduction rather than inventing a new distinction.

## Learning-complexity result

After checkpoint 104 made pipe debug-only and checkpoint 105 resolves Distance:

> **7 universal writing rules, 7 reusable player-facing structural constructions, 0 genuinely irregular multi-frame lexical cases.**

## Compatibility / history

Historical checkpoint-51 style tests that encoded:

`Almost P ≈ Not P + Low Distance P`

are migrated to `Almost P`.

Archived audits remain unchanged as historical evidence; this checkpoint explicitly supersedes their temporary boundary-Distance solution.

## Follow-up

Do not build a generic Metric/Boundary/Tolerance subsystem unless later corpus/game requirements independently justify it.

The next stabilization task is the beginner Cuspell subset, alongside remaining current-spec normalization/drift checks.
