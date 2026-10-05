# Checkpoint 137 — Duration and Protection Teaching Module

_Status: completed modular beginner extension_

## Trigger

Checkpoint 136 reduced the required beginner semantic core to 11 signs and separated Light/attribute change from fresh creation.

The next roadmap item was to add duration/protection without undoing that modularity.

The proposed vocabulary was:

`ThisInterval Persist Prevent`

The audit asks whether those three signs should arrive as one block, whether they introduce hidden concepts, and which Prevent semantics are appropriate for a beginner.

## Finding 1 — duration should be learned before protection

`Persist` and `Prevent` both require a TimeInterval.

Teaching both at once would introduce:

- a new temporal reference;
- active magical maintenance;
- nested EventSpec blocking.

Those are distinct ideas.

So checkpoint 137 splits the work into two stages:

1. `ThisInterval Persist`;
2. `Prevent`.

The 11-sign core remains unchanged.

## Stage 1 — designated duration + Persist

Add:

`ThisInterval Persist`

Cumulative semantic count after Light/Create modules: **17**.

Examples:

`Persist Whole This ThisInterval!`

`Persist Locked This ThisInterval!`

`Persist Magic This ThisInterval!`

This reuses StatePropositions the learner already knows.

### ThisInterval is not a magic duration literal

`ThisInterval` must resolve to one objectively designated TimeInterval supplied by the command/casting environment.

It does not mean:

- “for a while”;
- an arbitrary caster-chosen duration that was never specified;
- forever.

No omitted duration means forever.

A later time-construction lesson may teach explicit Interval/Now/quantity construction. This module only teaches applying an already designated interval.

### Persist is not Begin

`Begin Whole This!`

means to begin the Whole state.

`Persist Whole This ThisInterval!`

means to actively maintain Whole against ordinary evolution over the interval.

The teaching material therefore does not call Persist “mend for a duration.”

Establishing a missing state and maintaining a state are separate meanings.

## Stage 2 — exact-event Prevent

Add:

`Prevent`

Cumulative semantic count: **18**.

The beginner form is:

`Prevent event interval!`

Examples:

`Prevent Move This There ThisInterval!`

`Prevent End Whole This ThisInterval!`

`Prevent Begin Locked This ThisInterval!`

This teaches that an EventSpec can itself be the object of protection.

The meaning is exact.

Preventing `End Whole This` does not silently prevent every physical process that could lead to a non-Whole result. The protected EventSpec must match under the ordinary execution semantics.

## Advanced Prevent remains deferred

Checkpoint 133 added the bound pre-commit matcher:

`Prevent e:EventSpec predicate region? interval`

For example:

`Prevent e:EventSpec Magic $e _ ThisInterval!`

That is deliberately not taught in this module because it introduces:

- EventSpec binders;
- predicate matching;
- the omission marker for optional Region;
- generic execution interception;
- Magic(EventSpec) provenance.

The language supports those semantics, but beginner protection starts with the simpler exact-event frame.

## Current modular progression

Semantic core:

- 6 signs;
- 9 signs;
- 11 signs.

Follow-on modules:

1. `Change Light` -> 13;
2. `At Create` -> 15;
3. `ThisInterval Persist` -> 17;
4. `Prevent` -> 18.

The module count is not treated as total learning complexity. The earlier Light/Create modules still add notation/binder concepts, and the duration module adds the requirement that a contextual TimeInterval be objectively resolved.

## Repository changes

Current machine truth becomes:

`language/subsets/spellcraft_beginner_v0_4.json`

Checkpoint-136 v0.3 is preserved under:

`archive/design/cp136_SPELLCRAFT_BEGINNER_V0_3.json`

The v0.1 50-sign SRD projection remains unchanged in role: coverage benchmark, not learner starter.

## Inventory effect

None.

No root, constructor, frame, or world concept is added.

The semantic inventory remains:

- 217 registered entries;
- 136 semantic primitive candidates;
- 55 formal constructors;
- 276 semantic frames;
- 53 multi-frame entries.

## Decision

**KEEP THE REQUIRED CORE AT 11 SIGNS.**

**TEACH THISINTERVAL + PERSIST BEFORE PREVENT.**

**TEACH ONLY SIMPLE EXACT-EVENT PREVENT IN THE BEGINNER PROGRESSION.**

**KEEP BOUND ANTIMAGIC/INTERCEPTION PREVENT ADVANCED.**

**DO NOT LET THISINTERVAL HIDE AN UNSPECIFIED OR INFINITE DURATION.**

## Next

Design the shared-representation teaching module without changing the 11-sign semantic core.
