# Design Decisions

This file records important decisions so later work does not accidentally regress them. Git history records wording changes; this file records the design intent.

## Accepted

### D-001 — Complex commands are allowed

Do not impose a one-action-per-spell rule.

If a complex sentence is grammatically valid, semantically objective, and meaningful, magic may execute it.

### D-002 — Language and magic are separate layers

The full language may contain concepts irrelevant to spellcasting. Starting casters do not need the complete language. Hidden and advanced runes are desirable.

### D-003 — Meaning-bearing writing costs mana

Every meaning-bearing rune written in a magical command costs mana. Pure syntax such as the current `|` separator and `.` terminator costs zero.

### D-004 — Genuine compression may reduce mana

Do not charge the expanded semantic value merely because a shorter valid linguistic/mathematical construction exists.

For example, an advanced multiplication expression may express 16 more cheaply than sixteen unary `@` runes.

Language mastery should be mechanically valuable.

### D-005 — Negation, zero, and opposition are different

- `NotX` = logical complement / does not satisfy X.
- `ZeroX` = quantity of scalar X is zero.
- `OppositeX` = formal inverse only when X has a declared reversible mapping.

Not every rune has an opposite.

### D-006 — No free minus sign

Negative values require a meaning-bearing operation, currently modeled with `Opposite` on quantities.

### D-007 — Typed composition replaces universal modification

Rejected rule: every `AB` means "B that also satisfies A."

Current rule: compounds compose only through declared semantic categories, traits, frames, family rules, and constraints.

### D-008 — Current core lexical categories

Working categories:

- Entity
- Kind
- Property
- Relation
- Process
- Quantity
- Reference<T>
- Operator

This is a working architecture, not an immutable promise. Change it only when stress tests demonstrate a real need.

### D-009 — State and axis are traits, not top-level types

State is currently represented by a `state` trait.

Semantic inversion is represented by explicit `reversible(X)` mappings rather than a general Axis category.

### D-010 — Opposite and converse are distinct

Reversing a semantic axis is not the same as exchanging relation participants.

Example: `In(A,B)`, `Contain(B,A)`, and `Outside(A,B)` are different ideas.

A future `Converse` operator/mechanism is strongly indicated.

### D-011 — Broad does not mean ambiguous

`LiquidMatter` has an objective meaning even though it does not uniquely identify Water.

The language must distinguish a broad/underspecified valid expression from an ambiguous or ill-typed one.

### D-012 — Contradiction and type error are distinct

A compound may be grammatically/type valid while its accumulated constraints are impossible.

Example: `SolidLiquidMatter` may be well-typed but contradictory if phase values are exclusive.

That differs from `OppositeMatter`, which is ill-typed.

### D-013 — RGB-like color basis

Red, Green, and Blue are current primitive color-channel candidates.

Equal RGB balance does not automatically mean White; intensity is separate.

### D-014 — Arbitrary aliases do not grant magical compression

A player cannot define a short name for an arbitrarily complex effect and thereby reduce its mana cost.

Only compression mechanisms actually recognized by the language/magic system can reduce cost.

### D-015 — Do not aggressively minimize primitives yet

Clarity and objective semantics take priority over a tiny rune inventory. Hundreds of candidate runes are acceptable during design; trimming can happen later.

## Strong working directions, not yet final

### W-001 — Typed references

Use `Reference<T>`, such as Entity, Location, Time, or Information references.

### W-002 — Dimensional measurement

Scalar values need `dimension(D)` so operations can reject incompatible measurements.

### W-003 — Functional relations

Use a `functional(A -> B)` trait for relations such as Center(region) -> location or Duration(event) -> time quantity.

### W-004 — Collections

Collection semantics are needed for Group, All, Some, Many, Few, Among, OneOf, and Sequence.

### W-005 — Proposition / Event / Command are grammar-level objects

These are expected to be produced by sentence grammar rather than treated as ordinary lexical categories.

### W-006 — Relationally defined Kinds

Kinds such as Tool, Weapon, Food, Medicine, Container, and Poison may require restrictions defined by relations/process roles, not only unary intrinsic Properties.

### W-007 — Existence should be explicit in the ontology

This would allow concepts such as Create and Destroy to be analyzed as Begin/End of existence rather than exceptional primitives.

## Rejected / superseded

- One action per magical command.
- Free zero-cost negative sign.
- Universal `AB = B that satisfies A` rule.
- Arbitrary aliases as free magical compression.
