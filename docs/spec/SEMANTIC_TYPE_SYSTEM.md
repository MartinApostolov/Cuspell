# Semantic Type System

_Status: working specification v0.2_

This specification replaces the earlier idea that every adjacent pair of roots composes through one universal modifier rule.

## 1. Purpose

The type system must determine, without GM interpretation:

1. whether two or more roots may combine;
2. the semantic structure of a legal compound;
3. the resulting expression type;
4. whether the result is satisfiable, contradictory, broad, or ill-typed.

A human being able to imagine a meaning is not sufficient for a compound to be valid.

## 2. Semantic record

Every root and every derived expression carries a semantic record:

- **Category** — what kind of expression it is.
- **Domain** — what portion of reality it concerns or can apply to.
- **Traits** — capabilities/restrictions used by semantic operations.
- **Frame** — typed attachment/argument slots and their roles.
- **Constraints** — logical/physical restrictions accumulated by the expression.

Example sketch:

`Red : Property <domain=visible-physical, blend-family=Color, channel=Red>`

`To : Relation <domain=spatial, reversible=From>`

These declarations belong to the language definition, not to caster intent.

## 3. Core lexical categories

### Entity

A particular individual thing.

Lexical roots will rarely denote bare Entities directly; References normally resolve to them.

### Kind

A class/set of entities.

Examples: Thing, Matter, Human.

A Kind is not one particular member.

### Property

A predicate/condition/quality that can hold of an appropriate subject.

Examples: Red, Solid, Life, Heat.

State is currently a trait on a Property rather than its own category.

### Relation

A predicate connecting two or more arguments.

Examples: To, In, Before, Near, Same.

### Process

Something that happens or can be caused to happen.

Examples: Move, Join, End, Sense.

A Process describes an event type; sentence grammar can instantiate it as an Event.

### Quantity

A numerical value or magnitude.

Examples: `@` = 1, Zero = 0.

### Reference<T>

An expression that resolves to a contextually identified semantic object of type T.

Examples:

- Self : Reference<Entity>
- Here : Reference<Location>
- Now : Reference<Time>
- This : Reference<T>, with T determined by explicit reference context

### Operator

An expression whose semantics transform or combine other expressions.

Examples: Not, Opposite, mathematical operators.

## 4. Domains

Domains are not grammatical categories.

Initial domains include:

- general Thing
- Matter
- Life
- Mind
- Space
- Time
- Event
- Information
- perceptual/physical phenomena
- Magic

Domains may overlap or form hierarchies.

A living body, for example, may satisfy Matter and Life constraints.

## 5. Important traits

The current architecture requires at least these traits:

### state

The expression denotes a state that can begin, persist, or end.

### scalar

The expression admits magnitude/comparison.

### dimension(D)

The scalar belongs to a measurement dimension such as Length, Time, Mass, Mana, Pressure, Charge, etc.

Dimensional typing prevents meaningless arithmetic between incompatible magnitudes.

### reversible(X)

The expression has one explicitly declared semantic inverse X.

This replaces a general Axis category.

### functional(A -> B)

A Relation behaves functionally from specified input roles to an output.

Examples may include:

- Center(Region) -> Location
- Duration(Event) -> Quantity[Time]
- Name(Entity) -> Sign
- Kind(Entity) -> Kind

### collection<T>

The expression denotes a collection of members of type T.

Needed by Group, All, Some, Among, OneOf, Sequence, etc.

### exclusive-family(F)

Only one ordinary value in family F can simultaneously apply under the relevant interpretation.

Example: Solid/Liquid/Gas/Plasma in Phase, if the finalized physical ontology treats them as exclusive.

### blend-family(F)

Members combine through a family-specific composition rule rather than ordinary conjunction.

Example: RGB color channels.

### perceptible / SenseChannel

Perception-related semantics.

The earlier rule `perceptible + Sense` was too narrow because touch, smell, and taste may depend on relations/interactions rather than a free-standing phenomenon.

A SenseChannel can declare stimulus domain and required interaction.

### contextual

The expression depends on an implicit comparison standard unless one is explicitly supplied or magically standardized.

Examples may include Near, Far, Many, Few, Hot, Cold, Bright, Dark, Good, Bad.

### commutative

The relevant composition can reorder without changing semantic normal form.

### countable

The denotation admits discrete counting.

## 6. Higher semantic objects

Sentence grammar is expected to construct objects that are not ordinary lexical categories.

### Proposition

A truth-bearing semantic structure.

Needed for:

- True / False
- If
- Because
- Believe
- Know (in propositional uses)
- questions/answers
- conditions

### Event

A situated occurrence of a Process.

An Event can possess:

- participants
- location
- time
- duration
- cause
- result

Needed for Before, During, Again, Cause, Repeat, Trigger, etc.

### Command

An executable directive constructed by magical grammar.

A Command may contain multiple actions if the language can represent them objectively.

## 7. Core composition rules

### 7.1 Property restriction of Kind

`Property + Kind -> restricted Kind`

Semantic form:

`{x in K | P(x)}`

Examples:

`RedMatter` = Matter satisfying Red.

`LiquidMatter` = Matter satisfying Liquid.

The second is broad but objective; it does not automatically mean Water.

### 7.2 Compatible Property conjunction

`Property A + Property B -> Property(A AND B)`

only when their domains and family rules permit conjunction.

This is not a universal adjacency rule.

### 7.3 Quantity applied to scalar Property

Conceptual rule:

`Quantity + Property[scalar, dimension=D] -> measured Property[D]`

Example:

`ZeroLight` = Light magnitude 0.

The finalized surface syntax for units and dimensions remains open.

### 7.4 Opposite

`Opposite + X[reversible(Y)] -> Y`

Examples:

- OppositeTo = From
- OppositeBefore = After
- OppositeMore = Less
- OppositeUp = Down

If no reversible mapping is declared, the compound is ill-typed.

Therefore OppositeMatter and OppositeLife are invalid unless later definitions explicitly make them reversible.

Quantities support arithmetic sign inversion, so Opposite@@ can represent -2.

### 7.5 Not

`Not + predicate -> logical complement predicate`

Not does not require reversibility.

Therefore:

- NotBefore = Before does not hold; may include simultaneous.
- OppositeBefore = specifically After.

These are distinct.

### 7.6 Compound frames

Some roots declare typed attachment frames rather than using ordinary Property conjunction.

Example:

`Sense` can declare a channel/stimulus slot.

Then:

- LightSense
- SoundSense

receive defined specialized perception meanings because the frame says how the left component binds.

Likewise End may declare a State target frame:

`End + Property[state] -> Process`

making EndLife a Process that causes the Life state to cease.

## 8. Relation converse

Semantic opposite and participant-role reversal must remain separate.

For:

`In(A,B)`

the converse may be:

`Contain(B,A)`

This is not the same as:

`NotIn(A,B)`

and is not automatically the same as:

`Outside(A,B)`

A formal converse operator/mechanism is strongly indicated but not yet finalized.

## 9. Color family

Red, Green, and Blue are current Color blend-family members.

Unquantified combinations denote equal included-channel contribution.

Examples:

- RedGreen
- GreenBlue
- RedBlue
- RedGreenBlue

The Color rule is explicitly commutative/associative where declared.

RedGreenBlue means equal RGB balance, not automatically White.

Brightness/intensity is separate.

Repeated identical channels should not silently encode weighting. Unequal ratios belong to the future ratio/Part machinery.

## 10. Constraint outcomes

The semantic checker must distinguish at least four outcomes.

### Valid and satisfiable

Example: RedMatter.

### Valid but broad / underspecified

Example: LiquidMatter.

The denotation is objective but contains many possible members.

### Well-typed but contradictory

Example candidate: SolidLiquidMatter if Solid and Liquid are mutually exclusive Phase values.

The grammar composes, but no ordinary object can satisfy the accumulated constraints.

### Ill-typed

Example: OppositeMatter or RedTo when no legal frame/rule applies.

No meaning is invented.

## 11. Compound parsing and normalization

The parser considers only composition rules registered by the language.

A compound is valid when its legal parses reduce to one semantic normal form.

- No legal parse -> invalid.
- Multiple parses, same normal form -> valid.
- Multiple parses, different meanings -> grammatically ambiguous and invalid until disambiguated.

A future zero-mana grouping mark may be added if needed. It would be syntax rather than a meaning-bearing rune.

Normalization never refunds mana.

If two written forms normalize to the same meaning but one uses more meaning-bearing runes, the longer one costs more.

## 12. Lexical polysemy rule

A rune may have multiple typed frames only if those frames instantiate one coherent semantic core.

If two meanings merely share an English translation, they must be separate runes.

This rule is essential because accidental English polysemy would reintroduce hidden ambiguity.

## 13. Known required extensions

Before the type system is considered stable, formalize:

- typed reference resolution;
- collection/quantifier semantics;
- Proposition construction;
- Event construction;
- relation converse;
- relationally defined Kind restrictions;
- existence semantics;
- measurement dimensions/units;
- contextual predicates and comparison standards;
- sense channels;
- scope/grouping.
