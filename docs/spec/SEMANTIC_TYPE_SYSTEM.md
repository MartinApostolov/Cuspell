# Semantic Type System

_Status: working specification v0.3_

This is the current lexical semantic architecture. It replaces the old universal rule that adjacent roots always mean "B satisfying A."

## 1. Purpose

For every expression, the language must mechanically determine:

1. whether the construction is legal;
2. its semantic structure;
3. its resulting type;
4. whether its constraints are satisfiable, broad, contradictory, or invalid.

Human plausibility is not a composition rule.

## 2. Semantic record

Every registered root/derived expression carries:

- **Category**
- **Domain**
- **Traits**
- **Frame**
- **Constraints**
- optional normalization/derivation rules
- lexical/magical availability metadata

These entries belong to the language definition.

## 3. Core lexical Categories

### Entity

A particular individual identity.

Concrete world objects normally enter expressions through References or Process results rather than bare Entity roots.

### Kind

A class of Entities.

Examples: Thing, Matter, Water, Human.

A Kind never silently selects one member.

### Property

A truth-valued unary predicate/constraint.

Examples: Life, Whole, Solid, Open.

Some Properties are family-member shorthands for Attribute values.

### Relation

A truth-valued predicate connecting typed participants, and/or a registered functional relation when marked functional.

Examples: Equal, In, Before, Have, Name, Distance.

### Process

An event type/state-change operation.

Examples: Move, Change, Sense, Attack, Eat.

Applying a Process frame yields an EventSpec.

### Quantity

A numeric value carrying dimension/value-domain information.

Examples: @, Zero, measured quantities.

### Reference<T>

A context-resolution expression with an explicit result type.

Examples:

- Self : Reference<Entity>
- Here : Reference<Location>
- Now : Reference<TimePoint>
- This : Reference<T> when a typed deictic referent exists

### Operator

A semantic transformer/combinator.

Examples:

- Not
- Opposite
- Begin
- End
- logical/quantifier/control Operators
- arithmetic Operators

These eight Categories remain sufficient for lexical roots so far. Derived semantic values may have more specific result types such as GeometryProfile, PhaseValue, Collection<T>, or TimeInterval without becoming new root Categories.

## 4. Domains

Domains constrain applicability but are not grammatical Categories.

Current broad domains include:

- Thing
- Matter
- Life
- Mind
- Space
- Time
- Event
- Information
- Geometry
- Magic

Domains can overlap and form hierarchies.

## 5. Traits

### state-predicate

A Property or Relation whose truth can persist and undergo Begin/End transitions.

Examples:

- Life(x)
- Have(a,b)
- Know(m,p)
- In(x,region)

The trait normally applies to the entry's state-valued frames. An overloaded entry may explicitly mark a particular frame `state_predicate: false` when that typed overload is a pure Proposition rather than a persistent state. For example, Entity/Entity `Touch` is state-valued, while Region/Region `Touch` is a topological boundary-contact Proposition used by strict-containment composition.

### attribute

Marks a functional Relation that returns a value/profile for a subject.

Examples:

- Phase(x) -> PhaseValue
- Form(x) -> GeometryProfile
- Color(x) -> ColorProfile

### scalar-attribute(D)

An Attribute returning Quantity with dimension D.

Examples:

- Mass(x)
- Heat(x)
- Light(x)
- Extent(event) for temporal extent
- Distance(a,b)

This supersedes the earlier loose idea that every scalar such as Heat/Light is an ordinary Boolean Property.

### dimension(D)

Quantity dimension for arithmetic/measurement typing.

### reversible(X)

Declares one formal semantic inverse for Opposite.

Examples:

- To <-> From
- Up <-> Down

### functional(inputs -> output)

A Relation returns one typed output from specified inputs.

Examples:

- Center(Region) -> Location
- Surface(Entity) -> SurfaceRegion
- Form(Entity) -> GeometryProfile
- Extent(Event) -> Quantity<Time>

The output must be unique or the function fails. Relations such as Name are intentionally not functional.

### collection<T>

Typed collection value/Kind semantics.

### family(F) / family-value(V)

Used by Attribute value families.

Example:

- Phase Attribute
- Solid Property with family=Phase, family-value=Solid

### exclusive-family(F)

Family members cannot simultaneously describe the same selected single-valued subject under that model.

### blend-family(F)

Components combine through a registered family-specific blend rule.

RGB-like color uses this.

### SenseChannel

Declares perception interaction/stimulus semantics.

### contextual

Requires discourse standard or explicit magical standard/threshold.

Examples may include Near, Far, Many, Few, Good, Bad.

### commutative / associative

Composition algebra traits used only when explicitly declared.

### countable

Denotation supports discrete Count.

## 6. Higher semantic structures

Grammar constructs semantic objects above lexical Categories.

### Term/value

A typed argument result: Entity reference, Quantity, Location, Region, Information, GeometryProfile, Collection, etc.

### Proposition

Truth-bearing semantic structure.

### EventSpec

A typed description of an event that could occur.

### Event

A concrete occurrence of an EventSpec with identity, participants, time, result, etc.

### Command

Executable command-mood structure submitted to magic.

### Collection<T>

Typed multi-value set/list structure.

### Sequence<T>

Ordered Collection.

These are grammar/semantic structures, not reasons to multiply root Categories.

## 7. Core compound/application rules

### Property restricts Kind

`Property + Kind -> restricted Kind`

Example:

`SolidWater`

= Water members satisfying Solid.

### Compatible Property conjunction

`Property A + Property B -> Property(A AND B)`

only when domains/family constraints permit it.

### Quantity + ScalarAttribute

`Quantity + ScalarAttribute<D> -> Property`

means the Attribute equals that Quantity after dimension/unit normalization.

Example:

`ZeroLight`

= Property whose Light measurement is zero.

### Family-member Property

A family member such as Solid can normalize to:

`Equal(Phase(x), SolidValue)`

without exposing SolidValue as a separate written root.

### Opposite

`Opposite + X[reversible(Y)] -> Y`

No reversible declaration means ill-typed.

Quantities also permit arithmetic sign inversion.

### Not

`Not + predicate -> logical complement`

Not never means semantic inverse.

### Converse

`Converse + Relation[converse mapping] -> mapped Relation`

Example:

`ConverseIn = Contain`

if the mapping is registered.

A Relation without a declared converse is invalid under Converse.

### Begin / End

Begin/End operate on state predicates/boundaries.

`Begin(P[state-predicate]) -> EventSpec/Process meaning P becomes true`

`End(P[state-predicate]) -> EventSpec/Process meaning P becomes false`

For an Event reference:

- Begin(Event) -> TimePoint
- End(Event) -> TimePoint

Typed input determines the coherent boundary frame.

### Registered compound frames

Roots can define special attachment slots.

Example Sense accepts a SenseChannel specialization.

Compounds are valid only through registered typed frames/family rules.

## 8. Attributes and Change

An Attribute is functional, not Boolean.

`Change(subject, attribute, target-value/profile) -> EventSpec`

Family-member shorthand can infer its Attribute:

`Change(x,Solid)`

normalizes to setting Phase(x)=Solid.

This keeps value-changing semantics distinct from Begin/End of truth-valued state predicates.

## 9. Relation operations are three distinct concepts

For a Relation R:

- `Not R` = R does not hold.
- `Opposite R` = formal semantic-axis inverse, only if reversible.
- `Converse R` = registered role permutation.

Example:

- NotIn(A,B)
- strict outside is `Not Overlap Extent A B` (stronger than Not In; boundary-only contact remains outside)
- Contain(B,A) = ConverseIn(A,B)

None are interchangeable by intuition.

## 10. Color

Red, Green, Blue remain registered Color blend-family components/constraints.

Unweighted adjacency represents equal included component proportions.

- RedGreen
- GreenBlue
- RedBlue
- RedGreenBlue

Color profile also includes total visible Light/intensity.

Balanced RGB does not automatically mean White.

Weighted chroma uses Ratio, not the structural Part rune.

Repeated channel roots do not secretly encode weights.

## 11. Kind lexicalization

A Kind can be:

- general ontology Kind;
- canonical natural Kind;
- registered semantic molecule;
- ad-hoc restricted Kind.

One-rune lexicalization does not imply semantic primitiveness.

Arbitrary Names/aliases do not become magical Kind roots.

A generic lexical `Kind(This)` is deferred because one Entity normally belongs to many Kinds.

## 12. Constraint outcomes

The semantic checker distinguishes:

### Valid and satisfiable

Example: RedMatter.

### Valid but broad

Example: LiquidMatter.

The set is objective but not singular.

### Well-typed but contradictory

Example: one homogeneous subject required to be both exact Solid and exact Liquid.

### Ill-typed

Example: OppositeMatter when Matter has no reversible mapping.

### Semantically incomplete for execution

A meaningful EventSpec/description may leave execution-relevant values unbound.

Example: Move(This) with no destination/path constraint.

This is different from ill-typed.

## 13. Parsing and normalization

The parser considers only registered composition/frame rules.

- no legal parse -> invalid;
- multiple parses with same normal form -> valid;
- multiple parses with different meanings -> ambiguous/invalid until grouped or rewritten.

Zero-mana grouping syntax may disambiguate structure.

Normalization never refunds mana.

## 14. Lexical polysemy rule

One rune may support multiple typed frames only when they instantiate one coherent semantic core.

English translation is not evidence of semantic identity.

Resolved examples:

- Part reserved for structural mereology, not Ratio.
- Whole reserved for completeness/integrity.
- Of and By rejected as generic magical relations.
- Start folded into Begin.
- Volume reserved for measured spatial extent.
- physical/information duplication is not currently a universal base root; any future copy operation must declare exactly what content/profile is preserved.
- Name is a Relation, not a globally functional lookup.

## 15. Collections and binders

Quantifiers operate over Kind/Collection domains through explicit binders.

Bound-variable marks are grammar and cost zero.

- All/Some -> Proposition
- Collect/Filter -> Collection
- Each -> distributed CompositeEventSpec
- selectors -> reduce Collections under explicit policies

A Kind never silently selects an Entity.

## 16. References

References resolve under formal context rules.

A singular slot accepts exactly one typed result.

Zero/multiple/wrong-type results fail unless an explicit Collection/selector construction is used.

Reference resolution is not omniscient Find/search.

## 17. Current stability

The original eight-category architecture survived the inventory audit and subsequent grammar/measurement stress tests.

Most new needs have been handled through:

- typed traits;
- functional relations;
- state predicates;
- structured outputs;
- grammar-level objects;
- explicit selection/binding.

Future work should add a new top-level Category only when these mechanisms cannot model a concept without distortion.
