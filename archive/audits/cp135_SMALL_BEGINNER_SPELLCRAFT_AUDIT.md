# Checkpoint 135 — Small Beginner Spellcraft Progression

_Status: completed teaching-boundary redesign_

## Trigger

The original spell-focused teaching work used SRD 5.1 level 0–2 effects as an external pressure set.

That was useful for coverage, but by checkpoint 130 the projection had reached 50 signs and had started teaching collections, triggers, persistence, prevention, transformation, repeat/concurrency, and fresh creation all inside one nominal beginner set.

After checkpoints 131–134 closed the remaining advanced spellcraft families, the user asked to rebuild the actual starting set around **Cuspell simplicity**, not D&D spell level.

The user also corrected the intended Light effect: the spell should create a new light source/orb rather than mutate an existing object's Light attribute.

## Decision 1 — teaching and coverage are different artifacts

Keep the existing 50-sign file as a broad coverage projection.

It continues to answer:

> how many D&D-like low-level effects can a relatively small fixed slice of Cuspell approximate?

It no longer answers:

> what should a new learner memorize first?

The current first-lesson truth moves to:

`language/subsets/spellcraft_beginner_v0_2.json`

The 50-sign projection remains in the v0.1 manifest and `player/SPELLCRAFT_COVERAGE.md`.

## Decision 2 — 16-sign actual beginner core

The new teaching progression is cumulative.

### Step 1 — 6 signs

`This There Move Begin End Whole`

This immediately supports:

- `Move This There!`
- `Begin Whole This!`
- `End Whole This!`

The learner sees one direct Process and one state that can begin/end.

### Step 2 — 9 signs

Add:

`You Locked Ill`

This supports:

- `Move You There!`
- `End Locked This!`
- `Begin Ill You!`
- `End Ill You!`

The learner reuses Begin/End instead of learning new spell-specific verbs.

### Step 3 — 11 signs

Add:

`Self Find`

Only the simple factive yes/no Find form is introduced:

- `Find Self This Locked This!`
- `Find Self You Ill You!`

Open-query binders and broad search are deferred.

### Step 4 — 16 signs

Add:

`Here At Create Change Light`

The first creation pattern is:

`Create x:Entity At $x Here Change $x Light «LightUnit» @!`

Only this stage introduces a binder.

## Light correction

Checkpoint 130 retained:

`Change This Light «LightUnit» @!`

as the Light analogue.

Checkpoint 135 corrects that conclusion for the intended Cuspell spell.

The two meanings are now explicitly different:

### Create a new light source

`Create x:Entity At $x Here Change $x Light «LightUnit» @!`

### Make an existing target luminous

`Change This Light «LightUnit» @!`

The former is the beginner Light spell.

The latter remains useful as a Faerie-Fire-like / luminous-mark building block.

The exact orb/Form is not guessed by language semantics. If a setting wants a canonical glowing orb, the world generation profile must deterministically supply that realization or a more specific profile must be written.

## Why these 16 signs

The set was chosen for semantic reuse and surface simplicity.

It deliberately excludes first-lesson machinery that requires additional mental models:

- conjunction/profiles with multiple simultaneous constraints;
- duration/persistence;
- event prevention/interception;
- collection construction and distribution;
- triggers;
- repeat/concurrency;
- shared representation;
- time-flow manipulation.

Those features remain fully available in Cuspell and become follow-on modules.

## Deferred module order

A reasonable next progression is:

1. Magic state/dispelling — add `Magic`;
2. duration/protection — add `ThisInterval Persist Prevent`;
3. shared representation — add `Represent` plus sensory/channel vocabulary;
4. programming/multi-target — add `And Repeat Concurrent Each Collect Member Trigger`;
5. time manipulation — add `TimeFlow`.

This order is a teaching proposal, not a semantic dependency graph.

## Regression effect

The old 50-sign projection retains all 48 SRD reference-effect regressions.

The current beginner manifest adds 12 Cuspell-first spell examples and nine dedicated regression checks covering:

- exact 16-sign size;
- cumulative 6/9/11/16 progression;
- registered-sign closure;
- one starter Old Name;
- parser validity;
- flat parenthesis-free surface;
- explicit deferral of programming/advanced-control signs;
- yes/no-only beginner Find;
- creation-based Light;
- binder use only in the two Create-light examples.

## Inventory effect

None.

Checkpoint 135 changes teaching projections and one coverage recipe only.

The semantic inventory remains:

- 217 registered entries;
- 136 semantic primitive candidates;
- 55 formal constructors;
- 276 semantic frames;
- 53 multi-frame entries.

## Result

**THE ACTUAL BEGINNER CORE IS 16 SIGNS, NOT 50.**

**THE 50-SIGN SET IS A COVERAGE PROJECTION.**

**LIGHT IS TAUGHT AS FRESH CREATION.**

## Next

Stress-test the 16-sign progression before designing the small follow-on modules.
