# Beginner Spellcraft

_Status: stress-tested beginner progression v0.3 — checkpoint 136_

The first Cuspell lesson is now an **11-sign semantic core**.

Checkpoint 135's 16-sign set was much better than the old 50-sign starter, but stress testing found that its final step still bundled too many new ideas together: measured attributes, an Old Name unit, `@`, a typed binder, bound-variable reuse, fresh creation, a creation profile, and an immediate continuation all arrived at once.

So the progression is now split into:

- **11-sign core** — movement, state change, and simple yes/no discovery;
- **2-sign Light module** — measured attribute change;
- **2-sign Create module** — fresh identity and binder scope.

That gives a **15-sign first course**, but only 11 semantic signs are required before the first follow-on module.

The old 50-sign SRD coverage set remains in `SPELLCRAFT_COVERAGE.md`.

## 1. First six signs

`This There Move Begin End Whole`

A magical command ends in:

`!`

With only these six signs:

`Move This There!`

Move the designated Entity to the designated Location.

`Begin Whole This!`

Begin structural wholeness.

`End Whole This!`

End structural wholeness.

The first lesson therefore teaches only three reusable shapes:

- `Move target destination!`
- `Begin state!`
- `End state!`

No binders, units, collections, timing, or programming are needed.

## 2. Add three reusable words

Add:

`You Locked Magic`

Cumulative total: **9 signs**.

The grammar does not change.

`Move You There!`

`Begin Locked This!`

`End Locked This!`

`Begin Magic This!`

`End Magic This!`

The point of this step is that new state vocabulary reuses the same Begin/End machinery.

`Magic` here means the Entity's magical state. The more advanced EventSpec/Event provenance uses of `Magic` are not part of the beginner lesson.

## 3. Add bounded yes/no discovery

Add:

`Self Find`

Cumulative total: **11 signs**.

The beginner only learns the simple yes/no Find form:

`Find Self This Whole This!`

`Find Self This Locked This!`

`Find Self This Magic This!`

The repeated `This` is deliberate.

The first `This` supplies the explicit information-access scope. The final `This` is the subject inside the queried proposition.

So:

`Find Self This Locked This!`

means:

> within the explicitly designated subject/scope, determine truthfully whether that subject is Locked and make Self know the answer.

Open-query binders and broad searches are later material.

## 4. The complete 11-sign core

`Self This You There`

`Move Begin End Find`

`Whole Locked Magic`

That is the semantic core.

It supports eleven curated first spells:

| Spell idea | Cuspell |
| --- | --- |
| Move something | `Move This There!` |
| Move a person | `Move You There!` |
| Mend | `Begin Whole This!` |
| Break | `End Whole This!` |
| Lock | `Begin Locked This!` |
| Unlock | `End Locked This!` |
| Mark magical | `Begin Magic This!` |
| End selected Magic state | `End Magic This!` |
| Check integrity | `Find Self This Whole This!` |
| Check a lock | `Find Self This Locked This!` |
| Detect Magic state | `Find Self This Magic This!` |

This is intentionally small enough that every semantic sign appears in the first spellbook.

## 5. First follow-on module — Light and measured attributes

Add only:

`Change Light`

Cumulative semantic vocabulary: **13 signs**.

This module also teaches two pieces of notation:

- `@` = the positive unit number 1;
- `«LightUnit»` = the established Light unit Old Name.

Now:

`Change This Light «LightUnit» @!`

sets an already-existing Entity's Light output to one LightUnit.

This module is separate because `Change` has a new three-part pattern:

`Change target attribute value!`

and measured quantities are a new idea even though only two new semantic signs are added.

## 6. Second follow-on module — fresh creation

Add only:

`At Create`

Cumulative semantic vocabulary: **15 signs**.

Creation now introduces the first binder syntax:

`x:Entity`

means “bind a fresh Entity as x,” and:

`$x`

refers to that bound Entity.

The creation example deliberately reuses `There`, `Change`, `Light`, `«LightUnit»`, and `@` instead of introducing more vocabulary at the same time:

`Create x:Entity At $x There Change $x Light «LightUnit» @!`

Meaning:

1. allocate one fresh Entity;
2. establish it at the already-designated Location `There`;
3. keep that fresh identity in scope;
4. immediately set its Light output.

This is the beginner Light creation spell.

The exact visible Form is still a world-realization question. If a setting's generation rules deterministically realize this profile as a glowing orb, it is an orb. Cuspell does not silently invent shape/material details.

## 7. Why `Here` and `Ill` left the required set

Checkpoint 135 required both.

The stress test found neither was a prerequisite.

### `Here`

Creation can reuse the already-known `There`:

`Create x:Entity At $x There Change $x Light «LightUnit» @!`

So `Here` is useful convenience vocabulary, not a required teaching sign.

If learned later:

`Create x:Entity At $x Here Change $x Light «LightUnit» @!`

is the caster-local version.

### `Ill`

`Ill` adds useful vocabulary, but no new grammar.

Once Begin/End/Find are understood, adding `Ill` immediately gives:

`Begin Ill You!`

`End Ill You!`

`Find Self You Ill You!`

That makes it a good example of **ordinary vocabulary expansion**, not a sign everyone must memorize in the core.

`Magic` replaces it in the core because the same single sign supports Begin/End/Find while being more central to spellcraft.

## 8. What remains deferred

The core and first two modules still do **not** require:

`And Repeat Concurrent Each Collect Member Trigger Persist Prevent Represent TimeFlow`

Those introduce additional mental models:

- conjunction/composite profiles;
- repetition or simultaneity;
- collections and distribution;
- triggers;
- duration and prevention;
- shared representation;
- altered temporal progression.

They should remain small modules rather than collapsing back into one large “beginner set.”

## 9. Teaching rule

Count semantic signs separately from syntax.

The 11-sign core really does use only 11 registered semantic signs, but the later modules also teach grammar/notation such as:

- `@`;
- Old Names;
- `name:Type` binders;
- `$name` variables;
- Create profile/continuation scope.

Those are genuine things a learner must understand even though they are not additional semantic rune entries.

That distinction is why the old 16-sign count understated the difficulty of its final tier.

For the broader 50-sign SRD stress test, see `SPELLCRAFT_COVERAGE.md`.
