# Current State

_Last updated: 2026-09-27_

This file is the canonical short handoff for the Cuspell project. Read the detailed specs under `docs/spec/` for normative definitions.

## Goal

Build a genuine formal/compositional rune language for a D&D-style freeform magic system.

A caster should be able to construct effects that were never prewritten as spells, while the meaning of every valid magical command is determined by the language rather than negotiated with the GM.

The full language may be much larger than the magical subset. Do not aggressively minimize the rune inventory yet.

## Current notation

- `|` — word separator; syntax; 0 mana.
- `.` — mandatory sentence/command terminator; syntax; 0 mana.
- Adjacent roots form one compound word: `RedGreen`.
- `@` — one quantity/magnitude unit; meaning-bearing; costs 1 mana.
- `Opposite` — semantic inversion operator where a formal reversible mapping exists; costs 1 mana.
- Advanced `x` — multiplication/compression operator candidate; costs 1 mana.

Every meaning-bearing rune written in a magical command costs mana.

A shorter valid expression may genuinely cost less mana than a longer equivalent expression. This is intentional: mastery of the language is mechanically valuable.

## Locked / strong design principles

- Complex commands and multiple actions are allowed when grammatically valid, semantically objective, and meaningful.
- Language and magical execution are separate layers.
- The complete language, magical vocabulary, beginner vocabulary, and hidden/advanced vocabulary may differ.
- Arbitrary user-defined aliases do not automatically provide mana compression.
- `NotX`, `ZeroX`, and `OppositeX` are distinct.
- A free zero-cost minus sign was rejected; negative values require a meaning-bearing operation.
- Not every concept has an opposite.
- Compound meaning is determined by formal typing and composition rules, not by a universal English-like modifier rule.
- Context-dependent interpretation may be acceptable in ordinary conversation, but magical commands must resolve objectively.

## Current semantic architecture

The working lexical system uses eight core categories:

- Entity
- Kind
- Property
- Relation
- Process
- Quantity
- Reference<T>
- Operator

Other notions that once looked like candidate categories are currently modeled elsewhere:

- State → trait on a Property or other expression.
- Axis → `reversible(X)` trait.
- Phenomenon → domain/traits.
- Information → domain/Kind.
- Location and Time-reference → typed references.
- Form → domain/structured property rather than top-level category.

Important traits/mechanisms now indicated by the inventory audit:

- `state`
- `scalar`
- `dimension(D)`
- `reversible(X)`
- `functional(A -> B)`
- `collection<T>`
- `exclusive-family(F)`
- `blend-family(F)`
- `perceptible`
- `SenseChannel`
- `contextual`
- `commutative`
- `countable`

Sentence grammar is expected to produce higher semantic objects such as:

- Proposition
- Event
- Command

These are not currently treated as ordinary lexical categories.

## Compound principles

A compound is valid only when declared categories, traits, frames, and constraints determine a unique meaning.

The language should distinguish:

1. valid and satisfiable;
2. valid but broad/underspecified;
3. well-typed but contradictory;
4. ill-typed.

Examples:

- `RedMatter` — valid restricted Kind.
- `LiquidMatter` — valid but broad; not automatically Water.
- `SolidLiquidMatter` — typeable but contradictory if Solid and Liquid are exclusive Phase values.
- `OppositeMatter` — ill-typed because Matter has no declared reversible mapping.
- `OppositeBefore` — valid if Before declares `reversible(After)`.
- `NotBefore` — logical complement; not the same as After.
- `LightSense` / `SoundSense` — specialized Sense via a declared sense-channel/stimulus frame.
- `EndLife` — process terminating the Life state, if Life is a state Property and End accepts states.

Semantic normalization may make differently ordered compatible modifiers equivalent, but normalization does not refund mana.

## Color

The current basis is RGB-like:

- Red
- Green
- Blue

Color channels use a family-specific blend rule.

`RedGreenBlue` means equal channel balance, not automatically White. Brightness/intensity is separate. Zero visible Light is the leading model for Black.

## Current audit result

The full candidate rune inventory was checked against the type architecture.

The eight-category system broadly survived. Most problems require orthogonal mechanisms rather than additional top-level categories.

The largest missing mechanisms are:

- typed references;
- measurement dimensions;
- functional relations;
- collections/quantification;
- Proposition semantics;
- Event semantics;
- contextual predicates;
- generalized Sense channels;
- relationally defined Kinds;
- explicit existence semantics;
- relation converse distinct from opposite.

## High-priority troublesome roots

Resolve these before committing to the full sentence grammar:

1. Part
2. Whole
3. Kind
4. Of
5. By
6. End
7. Start / Begin
8. Form
9. Surface
10. Volume
11. Magic
12. Copy
13. Disease
14. Memory
15. Name

The primary danger is accidental English polysemy. A rune may have multiple typed frames only if they instantiate one coherent semantic core. If two meanings merely share an English word, they must be separate runes.

## Next work

The recommended next step is to resolve the troublesome roots and update the type system accordingly. Then:

1. define sentence grammar and semantic roles;
2. solve specific Kinds/nouns such as Water, Iron, Oak, Wolf, Human, Hand, Sword;
3. formalize numbers and measurement;
4. formalize magical execution and failure states;
5. split vocabulary into full / magical / beginner / hidden-advanced layers;
6. eventually design actual rune glyphs;
7. implement a parser/type-checker to stress-test whether the specification is truly objective.

## Source-of-truth rule

Current files under `docs/spec/`, plus this file and `docs/DECISIONS.md`, take precedence over historical snapshots.

If a future design pass reverses a major decision, update the spec and decision log rather than silently editing history.
