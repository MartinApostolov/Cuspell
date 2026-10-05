# Checkpoint 140 — TimeFlow Teaching Module Audit

_Status: completed final planned modular beginner extension_

## Trigger

Checkpoint 139 completed the programming/multi-target teaching stages and left one planned module:

`TimeFlow`

The audit asks whether a useful first time-manipulation lesson actually needs additional semantic signs such as `Zero`, `Divide`, or a Region reference.

## Finding 1 — TimeFlow itself is enough for the required lesson

The learner already knows:

- `Self`;
- `You`;
- positive integer `@` notation;
- `Persist`;
- `ThisInterval`.

Therefore the first relative-time command can add only one semantic sign:

`TimeFlow`

Cumulative semantic count: **29**.

Canonical example:

`Persist TimeFlow You Self @@ ThisInterval!`

Meaning:

> over the designated interval, maintain You's local physical/process temporal progression at factor 2 relative to Self.

The inverse subject/reference arrangement is independently meaningful:

`Persist TimeFlow Self You @@ ThisInterval!`

The reference is explicit in both cases.

## Finding 2 — stopped time is useful but not a prerequisite

Exact stopped local progression requires the registered quantity sign:

`Zero`

Example:

`Persist TimeFlow You Self Zero ThisInterval!`

That is a useful extension, but a learner does not need Zero in order to understand the relation itself.

TimeFlow can already demonstrate altered local temporal progression with a positive factor such as `@@`.

Therefore Zero remains optional vocabulary rather than increasing the required path to 30 signs.

## Finding 3 — slower time is ordinary arithmetic

A factor between Zero and @ represents slower progression.

The current language can express one-half through:

`Divide @ @@`

Example:

`Persist TimeFlow You Self Divide @ @@ ThisInterval!`

This requires `Divide`, but no new TimeFlow frame or special SlowTime root.

Fractional arithmetic is therefore optional follow-on material.

## Finding 4 — Region TimeFlow is not required for the first lesson

TimeFlow also accepts Region subjects, but the first required module does not add `ThisRegion`.

Region-wide temporal progression brings boundary/crossing and realization-footprint rules into the execution model.

Entity-relative examples already teach the core relation cleanly.

Region TimeFlow remains advanced.

## Finding 5 — TimeFlow remains distinct from other programming constructs

TimeFlow does not mean:

- Repeat one EventSpec more often;
- change event-frequency Rate;
- change only Move speed;
- grant extra game actions;
- travel to another TimePoint;
- reverse historical ordering.

The relation changes the subject's whole locally evolving physical/process progression relative to an explicit SpatialValue reference.

Negative factors remain invalid.

## Current modular progression

Semantic core:

- 6 signs;
- 9 signs;
- 11 signs.

Follow-on modules:

1. `Change Light` -> 13;
2. `At Create` -> 15;
3. `ThisInterval Persist` -> 17;
4. `Prevent` -> 18;
5. `Vision Represent` -> 20;
6. `And` -> 21;
7. `Sequence Concurrent` -> 23;
8. `Repeat` -> 24;
9. `Collect Member Each` -> 27;
10. `Trigger` -> 28;
11. `TimeFlow` -> 29.

The required semantic core remains **11 signs**.

## Repository changes

Current machine truth becomes:

`language/subsets/spellcraft_beginner_v0_7.json`

Checkpoint-139 v0.6 is preserved under:

`archive/design/cp139_SPELLCRAFT_BEGINNER_V0_6.json`

The 50-sign v0.1 projection remains a coverage benchmark rather than a teaching target.

## Inventory effect

None.

No root, frame, constructor, Old Name, or world concept is added.

The semantic inventory remains:

- 217 registered entries;
- 136 semantic primitive candidates;
- 55 formal constructors;
- 276 semantic frames;
- 53 multi-frame entries.

## Decision

**KEEP THE REQUIRED SEMANTIC CORE AT 11 SIGNS.**

**ADD ONLY TIMEFLOW TO THE REQUIRED TIME-MANIPULATION MODULE.**

**KEEP ZERO, DIVIDE, AND REGION TIMEFLOW OPTIONAL/ADVANCED.**

**REQUIRE AN EXPLICIT RELATIVE REFERENCE.**

**KEEP NEGATIVE/TIME-REVERSAL SEMANTICS OUTSIDE TIMEFLOW.**

## Next

Stress-test the complete 29-sign modular progression for hidden prerequisites, redundant stages, ordering, and total learner load. Then decide where the actual beginner/intermediate/advanced teaching boundaries belong.
