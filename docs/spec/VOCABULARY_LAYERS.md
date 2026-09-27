# Vocabulary Layers and Caster Progression

_Status: working specification v0.1_

Cuspell has one semantic language but several practical vocabularies.

The layers are not separate grammars. They are subsets of the same registered lexicon.

## 1. Full language

The **full language** may contain any objectively defined lexical item useful for:

- ordinary conversation;
- technical description;
- mathematics;
- social concepts;
- information;
- magical control;
- specialized sciences;
- proper conventional Kinds.

There is no target maximum rune count.

A large dictionary is acceptable.

## 2. Magical-readable vocabulary

A lexical item is **magically readable** when the spell engine can safely interpret it as part of a Command, target description, condition, measurement, or control structure.

This does not mean the rune itself is an action.

Examples:

- Water can identify a Kind.
- Red can constrain color.
- Before can define temporal relations.
- Human can constrain a selection.
- Equal can compare measurements.

Contextual concepts are magically readable only when their standard is fixed or explicitly supplied.

## 3. Executable/control vocabulary

A smaller subset directly builds executable EventSpecs or command control structures.

Examples:

- Move
- Change
- Join
- Begin
- End
- Cause
- Each
- If
- Sequence
- Persist
- Trigger
- Repeat

Processes may still be rejected for a particular target or world state by execution capability rules.

## 4. Ordinary-only vocabulary

Some roots can be legitimate in normal conversation but are not safe as magical predicates without extra structure.

Likely examples:

- Good
- Bad
- Friend
- Enemy
- Play
- Like
- Many
- Few

This is not a defect.

The full language may use discourse context where human conversation tolerates it. Magic requires normalization to objective parameters before execution.

## 5. Beginner caster vocabulary

Beginning casters should learn enough roots to create useful spells while still having visible room for linguistic advancement.

A provisional beginner semantic set:

### Reference / basic ontology

- Self
- This
- Here
- Thing
- Matter
- Life

### Logic / contrast

- Not
- Opposite
- And

### Quantity

- @
- Zero
- More
- Equal

### Space

- At
- To
- In
- Up
- Near
- Touch

### Change / action

- Move
- Change
- Join
- Begin
- End

### Physical state

- Solid
- Liquid
- Gas
- Heat
- Light

### Color

- Red
- Green
- Blue

### Integrity

- Whole
- Damage

### Perception / information

- Sense
- Sign

### Common practical Kinds

Campaign/world-dependent beginner lexicons may additionally include a small set such as:

- Water
- Stone
- Human

The exact starting list is a gameplay/progression choice, but all beginner roots use the same full-language semantics.

## 6. Intermediate vocabulary

Intermediate casters can gain:

- additional spatial relations;
- richer material Kinds;
- measurements and Units;
- Repair/biological concepts;
- common artifact Kinds;
- quantifiers;
- collections;
- Cause;
- Sequence;
- more Sense channels;
- explicit Time relations.

This tier expands expressiveness more than raw compression.

## 7. Advanced vocabulary

Advanced roots/operators include concepts that dramatically increase compression, abstraction, or control.

Strong candidates:

### Mathematics

- Multiply
- Divide
- Add
- Ratio
- Power
- Root
- advanced Units/conversions

### Logic and collections

- If
- All
- Some
- Collect
- Each
- Count
- advanced selectors

### Relation machinery

- Converse
- functional-profile operations
- explicit comparison/tolerance operators

### Event control

- Sequence
- Cause
- Persist
- Trigger
- Repeat

### Information

- Copy
- structured Record/Memory operations

These are excellent discoveries/research rewards because learning them changes what the caster can express economically.

## 8. Hidden/lost vocabulary

Some roots may be deliberately absent from public instruction even though they are part of the language.

Possible reasons:

- extremely powerful compression;
- dangerous control semantics;
- lost mathematical knowledge;
- restricted magical technology;
- culturally guarded terminology;
- roots whose existence changes common assumptions about magic.

The language specification should still define them objectively even when player-facing materials do not reveal them.

## 9. Common words as compression

Ordinary nouns can also be valuable discoveries.

Learning the registered Water rune can be much cheaper than repeatedly spelling a technical material classifier.

Learning a Sword rune can compress a long design profile.

Therefore progression does not have to be "stronger spell verbs." Vocabulary itself is power.

## 10. Availability is metadata

Each lexicon entry should eventually carry fields such as:

- full_language: yes/no
- magical_readable: yes/no/conditional
- executable: yes/no
- beginner: yes/no
- discovery_tier
- restricted_reason
- world_specific: yes/no

This metadata is not part of the rune's semantic meaning.

## 11. Player-visible dictionary

The player dictionary should reveal only entries the character knows.

Unknown roots can still exist in the canonical lexicon.

This supports:

- deciphering ancient inscriptions;
- research;
- teaching;
- stolen spell-language knowledge;
- translation;
- partial understanding of advanced magic.

## 12. Unknown rune behavior

A character who sees an unknown rune may be able to copy its shape without understanding it.

Whether copying an unknown rune can execute magic is a gameplay rule.

Recommended baseline:

- correct inscription can still be syntactically valid;
- the caster cannot deliberately compose or safely modify meaning they do not know;
- campaigns may require semantic understanding to activate a Command.

This avoids making rune knowledge purely player-memory trivia.

## 13. No separate beginner grammar

Beginner expressions use the same parser and semantics as advanced expressions.

Do not create simplified beginner meanings that later change.

A beginner simply has fewer lexical tools and therefore writes longer or less flexible expressions.

## 14. Compression progression

A typical progression path can look like:

1. unary numbers with many @ runes;
2. learned multiplication;
3. learned ratio/division;
4. learned conventional noun roots;
5. learned quantifiers/collections;
6. learned conditionals/control;
7. learned persistence/triggers;
8. learned highly specialized semantic molecules.

At every stage, old valid expressions remain valid.

## 15. Design principle

Vocabulary progression should reward:

- understanding;
- discovery;
- precision;
- mathematical sophistication;
- semantic knowledge.

It should not require memorizing a conventional spell list.

The same grammar remains available throughout the game.
