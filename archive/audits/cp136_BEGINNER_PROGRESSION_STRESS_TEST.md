# Checkpoint 136 — Beginner Progression Stress Test

_Status: completed stress test of checkpoint-135 beginner teaching boundary_

## Trigger

Checkpoint 135 split the old 50-sign SRD-derived teaching set into:

- a 16-sign Cuspell-first beginner core;
- a retained 50-sign coverage projection.

The next task was to actively try to break the 16-sign progression before adding more modules.

The stress test checks:

1. hidden prerequisites;
2. accidental complexity cliffs between tiers;
3. whether every required sign earns its place;
4. whether the same learned grammar actually recombines across several spells;
5. whether examples introduced at a tier use only signs available at that tier;
6. whether Light/Create still hides undeclared learner concepts.

## Finding 1 — the first 11 signs are structurally clean

Checkpoint 135's first three stages were:

- 6 signs: `This There Move Begin End Whole`;
- +3 signs: `You Locked Ill`;
- +2 signs: `Self Find`.

The first six signs support three simple reusable shapes:

`Move target location!`

`Begin state!`

`End state!`

The next state words add vocabulary without adding grammar.

The Find stage adds one genuinely new semantic operation, but its beginner use remains a closed yes/no pattern with no binder:

`Find Self This Locked This!`

No hidden unit, collection, duration, programming, or grouping machinery is required through this point.

**Result: the 6→9→11 structure is sound.**

## Finding 2 — the old 11→16 tier was not actually a five-sign lesson

Checkpoint 135 then added:

`Here At Create Change Light`

and called the cumulative result a 16-sign core.

But the actual learner load also included:

- `@` as quantity notation;
- `«LightUnit»` as an Old Name;
- `x:Entity` typed binder syntax;
- `$x` bound-variable syntax;
- the distinction between a Create profile and its immediate continuation.

Those are real concepts even though they are not registered semantic entries.

So the apparent “five-sign” tier introduced at least five semantic words plus several new structural/notation concepts.

**Result: semantic-sign count was understating teaching complexity.**

## Finding 3 — split Light/Change from Create

The old final tier combined two independent lessons:

### Measured attribute change

`Change This Light «LightUnit» @!`

This teaches:

- `Change target attribute value`;
- a measured AttributeDescriptor;
- unit notation;
- `@`.

### Fresh identity creation

`Create x:Entity At $x There Change $x Light «LightUnit» @!`

This teaches:

- fresh identity allocation;
- typed binder;
- variable reference;
- creation profile;
- immediate continuation.

Those should not arrive simultaneously.

Checkpoint 136 therefore makes them two modules:

1. add `Change Light` -> 13 semantic signs;
2. add `At Create` -> 15 semantic signs.

The creation spell then reuses the already-learned Light/Change pattern.

**Result: remove the complexity cliff instead of enlarging the core.**

## Finding 4 — Here is convenience, not a prerequisite

Checkpoint 135 added `Here` because the Light example created the new Entity at the caster's location.

But the learner already knows `There`, which is a Location reference.

So the creation lesson can reuse it:

`Create x:Entity At $x There Change $x Light «LightUnit» @!`

`Here` remains useful vocabulary:

`Create x:Entity At $x Here Change $x Light «LightUnit» @!`

but it is no longer part of the required progression.

**Result: one hidden convenience dependency removed.**

## Finding 5 — Ill is useful vocabulary but weak core material

`Ill` did not teach a new structure.

Once Begin/End/Find are known, adding Ill immediately gives:

`Begin Ill You!`

`End Ill You!`

`Find Self You Ill You!`

That makes it a good example of later vocabulary expansion.

The required core instead uses `Magic`, because the same one-sign addition produces spellcraft-central effects while exercising the same grammar:

`Begin Magic This!`

`End Magic This!`

`Find Self This Magic This!`

The beginner uses only the Entity-state meaning of Magic; EventSpec/Event provenance is advanced typed reuse.

**Result: replace Ill with Magic in the required semantic core.**

## Finding 6 — every core state word now proves the same reusable pattern

The three core state words are:

- `Whole`;
- `Locked`;
- `Magic`.

Each has a parser-valid Begin, End, and yes/no Find example:

`Begin Whole This!`
`End Whole This!`
`Find Self This Whole This!`

`Begin Locked This!`
`End Locked This!`
`Find Self This Locked This!`

`Begin Magic This!`
`End Magic This!`
`Find Self This Magic This!`

This is stronger teaching evidence than simply having many unrelated spell recipes.

**Result: the core demonstrates productive grammar rather than memorized spells.**

## Finding 7 — Light creation remains world-realization dependent, not language-incomplete

The current creation example:

`Create x:Entity At $x There Change $x Light «LightUnit» @!`

is language-valid and correctly allocates a fresh Entity before changing its Light output.

Cuspell still does not silently invent:

- orb shape;
- material;
- size;
- color;
- other physical properties.

If a setting wants this spell to produce a canonical glowing orb, world generation must deterministically realize this profile that way, or a more specific generation profile/Kind must be used.

That is not another language root requirement.

It is a world/execution realization requirement already implied by Create semantics.

**Result: keep the language example, but do not pretend “orb” is free hidden semantics.**

## Current progression

### Semantic core — 11 signs

Stage 1 — 6:

`This There Move Begin End Whole`

Stage 2 — 9:

add `You Locked Magic`

Stage 3 — 11:

add `Self Find`

### Module 1 — measured Light change

Add:

`Change Light`

Cumulative semantic count: **13**.

Also teach:

- `@`;
- `«LightUnit»`.

### Module 2 — fresh creation

Add:

`At Create`

Cumulative semantic count: **15**.

Also teach:

- `x:Entity`;
- `$x`;
- Create profile/continuation scope.

Optional convenience vocabulary can then add `Here`, `Ill`, or other ordinary state words independently.

## Regression additions

The checkpoint adds executable checks that:

1. the semantic core has exactly 11 entries at cumulative 6/9/11 stages;
2. all core/module entries are registered;
3. every core spell uses only signs available at its declared stage;
4. every core sign appears in the core spellbook;
5. Whole/Locked/Magic each support the same Begin/End/Find teaching matrix;
6. Magic, not Ill, occupies the required core;
7. core Find examples remain binder-free yes/no acquisition;
8. core examples contain no binders, Old Names, quantities, or advanced control signs;
9. the Light module adds only Change + Light;
10. the Create module adds only At + Create and reuses There/Change/Light;
11. Here is optional rather than required;
12. all required core/module examples parse.

## Repository cleanup

The checkpoint-135 v0.2 manifest is preserved under:

`archive/design/cp135_SPELLCRAFT_BEGINNER_V0_2.json`

The current machine-readable teaching truth becomes:

`language/subsets/spellcraft_beginner_v0_3.json`

The retained 50-sign coverage truth remains:

`language/subsets/spellcraft_beginner_v0_1.json`

## Inventory effect

None.

The semantic inventory remains:

- 217 registered entries;
- 136 semantic primitive candidates;
- 55 formal constructors;
- 276 semantic frames;
- 53 multi-frame entries.

## Decision

**REDUCE THE REQUIRED SEMANTIC CORE FROM 16 TO 11 SIGNS.**

**TEACH LIGHT/ATTRIBUTE CHANGE AND FRESH CREATE AS TWO SEPARATE TWO-SIGN MODULES.**

**REPLACE ILL WITH MAGIC IN THE REQUIRED CORE.**

**MAKE HERE OPTIONAL BY REUSING THERE IN THE CREATE LESSON.**

**COUNT GRAMMAR/NOTATION BURDEN SEPARATELY FROM REGISTERED SEMANTIC SIGNS.**

## Next

Build the next small duration/protection module without changing the 11-sign semantic core.
