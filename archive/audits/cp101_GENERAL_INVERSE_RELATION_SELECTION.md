# Checkpoint 101 — General Inverse-Relation Selection

_Status: completed stabilization audit; supersedes the current semantic conclusion of checkpoint 100 while preserving checkpoint 100 as historical rationale_

## Question

Can the temporary `Interpret` root and the irregular one-argument `Name(Sign) -> Entity` resolver be replaced by machinery Cuspell already has?

## Existing machinery found

Cuspell already had all of the surface pieces:

- typed binders such as `e:Entity` and `i:Information`;
- `Collect binder predicate` set comprehension;
- polymorphic `Unique collection`, whose result type is the collection member type;
- ordinary relations such as `Name(sign, referent)` and `Meaning(sign, content)`.

The only blocker was an implementation/type declaration accident: `Collect` was hard-coded to return `Collection:Entity` even though binders already support arbitrary semantic types.

## Generalization

`Collect` now preserves the binder's declared semantic type.

Conceptually:

`Collect x:T P($x) -> Collection:T`

No new rune or new player-facing syntax is introduced.

The parser gains one generic output-typing rule, `output_collection_of_binder_arg`, used by the existing `Collect` frame.

## Inverse relation selection

A relation stays a relation. To obtain a value from its inverse direction, explicitly collect values satisfying it and select a unique member when uniqueness is justified.

Examples:

`Unique Collect e:Entity Name «Yona» $e`

`Unique Collect r:Region Name «Oakville» $r`

`Unique Collect i:Information Meaning «mark» $i`

This does not make `Name` or `Meaning` globally functional. Zero or multiple candidates remain non-unique until context or additional predicates narrow the set.

## Name resolution

The contextual `Name(Sign) -> Entity` frame is removed.

This fixes two problems at once:

1. `Name` returns to one coherent nonfunctional naming relation;
2. New Names are no longer artificially limited to Entity referents—typed selection can return Regions, Kinds, Information, or other supported semantic values.

## Interpretation and reading

Checkpoint 100 correctly removed semantic interpretation from raw `Sense`, but then temporarily introduced `Interpret` as a separate Process root.

Checkpoint 101 finds that `Interpret` still bundles distinctions already represented elsewhere.

For a candidate content I:

- `Meaning S I` states the actual Sign-to-content relation;
- `Understand A (Meaning S I)` states that A comprehends that mapping;
- `Sense A channel S` states the sensory acquisition event.

A familiar successful reading can therefore use a `Sense` event conditioned on the real mapping being understood.

If A did not previously understand the mapping and learns it through decoding, that is genuinely a state transition and is written with `Begin Understand`.

Those are different truth conditions. A single `Interpret` Process would hide whether comprehension was pre-existing or newly acquired.

The temporary `Interpret` root is therefore removed.

## Inventory effect

Checkpoint 100 state:

- 206 registered base entries;
- 126 semantic primitive candidates;
- 258 semantic frames;
- 49 multi-frame entries;
- 2 genuine irregular overloads: `Name` and `Distance`.

Checkpoint 101 state:

- **205 registered base entries**;
- **125 semantic primitive candidates**;
- **256 semantic frames**;
- **48 multi-frame entries**;
- **1 genuine irregular overload**: `Distance`.

Frame distribution:

- 22 entries with no callable frame;
- 135 with exactly one frame;
- 35 with exactly two frames;
- 13 with three or more.

## Learning-complexity consequence

The player learns no additional grammatical construction. Typed binders, `Collect`, and `Unique` were already general language machinery.

The current summary is therefore:

**7 universal writing rules, 8 reusable structural constructions, and 1 genuinely irregular multi-frame lexical case.**

If pipe becomes debug-only, the player-facing structural count becomes 7.
