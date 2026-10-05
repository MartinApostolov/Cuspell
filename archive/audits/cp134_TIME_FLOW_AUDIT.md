# Checkpoint 134 — Time-Flow Manipulation Audit

_Status: advanced spellcraft gap audit 5; final checkpoint-128 family; stacked with checkpoints 132–133_

## Trigger

Checkpoint 128 found that Time Stop and physical interpretations of Haste/Slow require more than event ordering, Repeat, Rate, or Prevent.

The missing meaning is:

> one Entity/Region's local physical/process time progresses at a different rate relative to an explicit reference frame/worldline.

## Reduction audit

### Event Rate

`Rate EventSpec interval` measures occurrence frequency of one selected event family per already-defined time.

Two worlds can have the same measured frequency for a selected event while every other process in one frame evolves twice as fast.

**Not sufficient.**

### Repeat

Repeat schedules one EventSpec a specified number of times/period.

It does not alter metabolism, motion, chemistry, perception, other events, or world evolution generally.

**Not sufficient.**

### Prevent

Prevent can block specified events or event classes.

Stopping time by preventing every possible physical/mental/process event is not finitely specifiable and is not equivalent to changing the local temporal metric/scheduler.

**Not sufficient.**

### Movement/action speed

Changing Move or game action count affects selected mechanics, not all temporal evolution.

Cuspell should not define time dilation in terms of D&D action economy.

**Not sufficient.**

## Accepted result — TimeFlow

Add:

`TimeFlow(subject, reference, rate) -> StateProposition`

with Entity and Region subject frames.

The reference is an explicit SpatialValue that anchors the comparison worldline/frame.

The rate is a nonnegative dimensionless Quantity:Number.

Canonical points:

- `@` = subject progresses at the same rate as reference;
- `Zero` = subject progression stops relative to reference;
- > @ = faster;
- 0 < rate < @ = slower.

Negative factors are outside the relation. Time reversal is not silently included.

## Examples

Normal relative flow:

`TimeFlow Self ThisRegion @.`

Stopped region relative to caster/reference:

`Persist TimeFlow ThisRegion Self Zero ThisInterval!`

Faster target:

`Persist TimeFlow You Self @@ ThisInterval!`

Half-rate target:

`Persist TimeFlow You Self Divide @ @@ ThisInterval!`

## Entity versus Region

Entity TimeFlow affects that Entity's temporally evolving physical/process state.

Region TimeFlow affects world evolution whose realization footprint lies within the Region.

Boundary crossing, nested Region states, and competing TimeFlow states require deterministic world/executor rules.

The language does not hide those rules in the rune.

## Semantics not implied

TimeFlow does not directly mean:

- more/less D&D actions;
- a Move-speed bonus;
- altered event frequency for only one named EventSpec;
- altered clock labels;
- changed truth values;
- rewritten TimePoint/TimeInterval definitions;
- time travel/reversal.

Games may derive action opportunities and other consequences from physical temporal progression.

## Inventory effect

Adds:

- 1 registered entry: `TimeFlow`;
- 1 semantic primitive candidate;
- 2 semantic frames.

Totals:

- 217 registered entries;
- 136 semantic primitive candidates;
- 55 formal constructors;
- 276 semantic frames;
- 53 multi-frame entries.

Seven regressions cover Entity/Region forms, stop/faster/slower values, explicit reference typing, Persist composition, and distinction from Event Rate.

## Decision

**ADD TimeFlow as explicit nonnegative relative local temporal progression.**

Do not reduce it to Rate, Repeat, Prevent, movement speed, or game action economy.

## Checkpoint-128 advanced-family closure

All five reusable families are now structurally resolved:

1. fresh identity generation -> `Create`;
2. bounded factive acquisition -> `Find`;
3. persistent shared representation -> `Represent`;
4. generic pre-commit execution interception -> typed `Magic` + bound `Prevent`;
5. time-flow manipulation -> `TimeFlow`.

## Next

Rebuild the actual beginner spell progression around Cuspell complexity rather than D&D spell levels, and re-audit the starter recipes (including creation-based Light) against the stabilized spell semantics.
