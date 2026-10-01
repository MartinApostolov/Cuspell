# Vocabulary Layers and Learning Progression

_Status: current design guidance_

Cuspell has one semantic language. Beginner/intermediate/advanced layers are **teaching/progression choices**, not separate dialects with different meanings.

Player-facing material lives under `player/`.

## 1. One language, staged knowledge

Learning progression may control which signs, Old Names, mathematics, selectors, or control structures a caster knows.

A sign means the same thing at every tier.

The language must not introduce beginner-only semantic shortcuts that later change truth conditions.

## 2. Beginner goal

A beginner subset should let a player construct useful simple commands after learning:

- sentence-final mood;
- head-first typed arguments;
- tight local adjacency;
- no guessing/ambiguity;
- a small practical sign set;
- a small set of common Old Names.

Advanced binders, collections, selectors, discourse machinery, and dimensional mathematics can wait.

The actual beginner set is still to be designed/tested rather than inferred from English frequency.

## 3. Useful beginner families

Likely teaching candidates include a subset of current signs such as:

### References / space

- Self
- This
- Here
- There

### Basic state / ontology

- Thing
- Matter
- Life
- Whole
- Exist

### Basic change/action

- Move
- Begin
- End
- Change
- Touch
- In

### Logic/control

- Not
- And
- If
- Sequence / Concurrent as needed

### Basic comparison/measurement

- Zero / @
- Equal
- More
- Length or another useful Attribute
- canonical Unit Old Names as needed

### Perception

- Sense
- selected SenseChannels

Common object/species words such as human, cat, water, body, hand, tools, etc. are **Old Names/world concepts**, not primitive beginner roots.

## 4. Intermediate material

Intermediate teaching can add:

- named optional roles;
- richer spatial/topological relations;
- Cause / Transfer / Control;
- more measured Attributes and Units;
- quantifiers and binders;
- Collections;
- selectors;
- Time/Event relations;
- broader ordinary/social vocabulary;
- additional Old Names.

## 5. Advanced material

Advanced learning can emphasize machinery that increases abstraction or compression:

### Mathematics

- Add
- Multiply
- Divide
- Ratio
- Power
- Root
- dimensional reasoning

### Collections / selection

- All / Some
- Collect / Filter / Each
- Count / Partition
- MinBy / MaxBy / Unique / Random

### Event control

- Cause
- Persist
- Trigger
- Repeat
- complex Sequence / Concurrent nesting

### Information / epistemics

- Confidence
- EvidenceFor
- Infer
- Question / AnswerFor
- Meaning / About / Explains

These are current registered meanings, not speculative roots.

## 6. Restricted/lost knowledge

A campaign may withhold known Cuspell signs or Old Names for world reasons:

- lost scholarship;
- dangerous control semantics;
- secret mathematical techniques;
- institutional restriction;
- undiscovered historical vocabulary.

This affects character knowledge, not language truth.

## 7. Old Names and progression

Knowing an Old Name can provide real linguistic compression because its historical mana cost is registered.

New Names do not gain that privilege.

A campaign can therefore make vocabulary discovery mechanically meaningful without allowing arbitrary player aliases to bypass cost.

## 8. Learning-speed target

The current design target is a very small **starter literacy**, not mastery of all 205 entries.

The next progression task is to build a candidate starter set and test it with real learners.

Useful measures include:

- time to write a first valid command;
- error rate after a short explanation;
- number of rules remembered without reference;
- ability to infer a new composition from known signs;
- time to diagnose an ambiguous/ill-typed example.

Do not claim a precise learning time until actual user testing exists.

## 9. Player documentation boundary

The player folder should teach only current usable material:

- `player/QUICK_START.md`
- `player/RULES.md`
- `player/RUNES.md`
- `player/ADVANCED_GRAMMAR.md`
- `player/names/`

Maintainer rationale, historical alternatives, parser internals, and old syntax stay out of that layer.

## 10. Result

Progression should come mostly from **learning more vocabulary and more powerful general mechanisms**, not from accumulating irregular grammar exceptions.
