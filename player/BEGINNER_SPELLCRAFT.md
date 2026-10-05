# Beginner Spellcraft

_Status: current 16-sign beginner core v0.2 — checkpoint 135_

This is the actual first Cuspell spellcraft progression.

The older 50-sign set was useful for proving coverage against many D&D-like effects, but it asked a new learner to absorb too much at once. Checkpoint 135 separates those goals:

- **16 signs** for the real first lessons;
- the older **50-sign** set as a broader coverage projection in `SPELLCRAFT_COVERAGE.md`.

The first set is chosen by **Cuspell complexity**, not by D&D spell level.

## 1. First rule: a spell is a command

A magical command ends in:

`!`

The first examples stay flat and parenthesis-free.

### First 6 signs

`This There Move Begin End Whole`

With only these six signs:

`Move This There!`

Move the designated subject to the designated destination.

`Begin Whole This!`

Restore structural wholeness.

`End Whole This!`

Break structural wholeness.

That is enough for a first lesson: one Process and one state that can begin or end.

## 2. Add explicit targets and simple conditions

Add three signs:

`You Locked Ill`

Cumulative total: **9 signs**.

Now:

`Move You There!`

`End Locked This!`

`Begin Ill You!`

`End Ill You!`

These teach that the same Begin/End machinery works across different persistent states.

## 3. Add bounded discovery

Add:

`Self Find`

Cumulative total: **11 signs**.

The beginner only learns the simplest yes/no Find form.

`Find Self This Locked This!`

means: determine truthfully whether the designated subject is Locked and make Self know the answer.

`Find Self You Ill You!`

means: determine truthfully whether the designated target is Ill.

This introduces divination without collections, open binders, remote world search, or hidden omniscience.

## 4. Add creation and Light

Add five signs:

`Here At Create Change Light`

Cumulative total: **16 signs**.

The first Old Name used by the course is:

`«LightUnit»`

and `@` is the positive unit number 1.

### Light is a creation spell

The earlier coverage set treated Light as changing an existing object's Light value. That was the wrong semantic family for the spell we want.

The beginner Light spell is now:

`Create x:Entity At $x Here Change $x Light «LightUnit» @!`

Meaning:

1. allocate one fresh Entity;
2. place it at Here;
3. immediately set that same fresh Entity's Light output to one LightUnit.

The binder `x:Entity` / `$x` is taught here for the first time because creation genuinely needs a way to refer to the fresh identity.

The exact visible shape is **not guessed by Cuspell**. If the world uses a deterministic standard glowing orb for this creation profile, the result is an orb; otherwise the spell needs a more specific generation profile. The important language distinction is already correct: a new light source is created.

The same pattern can place it at the designated destination:

`Create x:Entity At $x There Change $x Light «LightUnit» @!`

### Changing an existing thing is a different spell

`Change This Light «LightUnit» @!`

does not create anything. It makes an already designated Entity luminous.

That distinction is useful early because it demonstrates one of Cuspell's main design goals: similar-looking magical outcomes can still have different exact meanings.

## 5. The complete 16-sign core

`Self This You Here There`

`Move Begin End Change Create Find`

`At Whole Locked Ill Light`

That is the whole first set.

It deliberately does **not** require:

`And Repeat Concurrent Each Collect Member Trigger Persist Prevent Represent TimeFlow`

Those are useful, but they add programming, binding, duration, interception, shared-representation, or temporal-model complexity that a learner does not need on day one.

## 6. First spellbook

| Spell idea | Cuspell |
| --- | --- |
| Move something | `Move This There!` |
| Move a person | `Move You There!` |
| Mend | `Begin Whole This!` |
| Break | `End Whole This!` |
| Unlock | `End Locked This!` |
| Cause illness | `Begin Ill You!` |
| Remove illness | `End Ill You!` |
| Check a lock | `Find Self This Locked This!` |
| Diagnose illness | `Find Self You Ill You!` |
| Make an existing thing glow | `Change This Light «LightUnit» @!` |
| Create light here | `Create x:Entity At $x Here Change $x Light «LightUnit» @!` |
| Create light there | `Create x:Entity At $x There Change $x Light «LightUnit» @!` |

These are not meant to be balanced game spells yet. They are teaching examples for composing exact meanings.

## 7. What comes next

The next modules should be added only after the 16-sign core is comfortable.

A natural order is:

1. **Magic state and dispelling** — add `Magic`;
2. **duration/protection** — add `ThisInterval Persist Prevent`;
3. **shared representation** — add `Represent` and sensory/channel vocabulary;
4. **programming/multi-target magic** — add `And Repeat Concurrent Each Collect Member Trigger`;
5. **time manipulation** — add `TimeFlow`.

The important change is that these are now modules, not prerequisites for being called a beginner.

For the old 50-sign SRD coverage stress test, see `SPELLCRAFT_COVERAGE.md`.
