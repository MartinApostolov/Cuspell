# Checkpoint 108 — Positive Biological-Sex Classification

_Status: implemented targeted semantic repair from the civilization vocabulary audit_

## Trigger

Checkpoint 106 found an asymmetry in the reusable biological vocabulary:

- `Female` existed as a positive Property;
- no corresponding positive Male classification existed.

Using:

`Not Female X`

as the meaning of “Male X” would make an unjustified logical assumption.

## Why negation is insufficient

The complement of Female is simply “does not satisfy the Female classifier.”

That does not by itself identify a specific positive biological category.

Depending on the applicable world ontology, an entity may:

- satisfy Male;
- satisfy Female;
- satisfy both;
- satisfy neither;
- satisfy another biological classification;
- not be an entity for which those classifiers apply meaningfully.

Therefore:

`Male X != Not Female X`

and:

`Female X != Not Male X`.

Cuspell must not turn English-looking opposites into Boolean complements unless the semantics actually establish exhaustiveness.

## Alternatives considered

### Define Male as Not Female

Rejected.

This erases worlds/classifiers with non-exhaustive, overlapping, transformed, atypical, or additional biological categories.

### Add a Sex attribute plus enum values

A design such as:

`Sex(X) -> SexValue`

with Male/Female values could be appropriate for a world whose biology truly forms one functional exclusive axis.

It is not justified as the universal Cuspell core.

Introducing a generic descriptor plus atomic values would also add machinery without reducing the underlying distinctions, and it would prematurely force all worlds into the same ontology.

### Independent positive properties

Chosen.

Cuspell now keeps:

- `Male(Entity) -> StateProposition`;
- `Female(Entity) -> StateProposition`.

Both are positive biological classifiers grounded by the applicable world model.

The core language imposes no universal exhaustiveness or mutual-exclusion rule.

## Female semantic clarification

The old description called Female an ordinary “sex/gender” classification.

Checkpoint 108 narrows the core meaning to **biological-sex classification**.

This prevents one root from conflating:

- biological classification;
- social gender identity;
- cultural role;
- title;
- presentation.

Those other meanings can use world concepts, Names, social relations, or later independently justified semantics.

## Old Name compatibility

The existing Goddess Old Name remains historically built from Female plus the earlier Deity Old Name:

`«Female«WorshipThing»»`

Its frozen meaning and recursive mana cost are unchanged.

Adding Male does not rewrite that history.

Future civilization vocabulary may plausibly use Male/Female while forming Old Names for culturally common concepts such as man, woman, mother, father, husband/wife distinctions, animal breeding terms, etc., but checkpoint 108 does not add those names automatically.

## Regression requirements

The language must prove that:

- Male and Female are both positive PropertyDescriptors;
- `Male X` differs semantically from `Not Female X`;
- `Female X` differs semantically from `Not Male X`;
- the core parser/type system does not itself reject combinations solely because of assumed binary exclusivity;
- the existing Goddess Old Name continues to resolve.

A particular world package may impose additional biological constraints during world validation/execution.

## Inventory effect

Before checkpoint 108:

- 209 registered entries;
- 128 semantic primitive candidates;
- 55 formal constructors;
- 259 semantic frames;
- 48 multi-frame entries;
- 102 Old Names.

After checkpoint 108:

- **210 registered entries**;
- **129 semantic primitive candidates**;
- **55 formal constructors**;
- **260 semantic frames**;
- **48 multi-frame entries**;
- **102 Old Names**.

Frame distribution becomes:

- 22 zero-frame entries;
- 140 one-frame entries;
- 36 two-frame entries;
- 12 three-or-more-frame entries.

No grammar rule, semantic type family, Old Name, New Name, or world concept is added.

## Civilization-audit progress

Checkpoint 108 resolves the second structural issue from checkpoint 106.

Still open before large Old Name expansion:

1. TimeInterval Begin/End/Extent access;
2. policy for historical lexicalization of parameterized verbs/relations.

## Result

Cuspell can now state positive biological Male and Female classification without abusing logical negation or forcing a universal binary ontology.
