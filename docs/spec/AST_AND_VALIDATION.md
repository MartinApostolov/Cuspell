# Semantic AST and Validation Model

_Status: implementation-facing specification v0.1_

This file defines the normalized structures a reference parser/type-checker should produce. It is not player-facing syntax.

## 1. Design goal

Two independent implementations given the same:

- Cuspell language version;
- lexicon;
- world ontology;
- source expression;

should produce the same semantic AST or the same validation failure class.

If they do not, the written specification is incomplete.

## 2. Common node metadata

Every semantic node can carry:

- source span;
- written semantic rune count;
- normalized type;
- domain constraints;
- traits;
- child nodes;
- lexicon entry IDs used;
- diagnostic notes.

Source cost is kept separate from normalized meaning.

## 3. Lexical node

`Root(entry_id)`

points to one registered lexicon entry.

A surface label is never the semantic identity; the lexicon entry ID is.

## 4. Compound node

`Compound(rule_id, components, normalized_value)`

records which registered composition rule licensed adjacency.

The parser must not create a generic "modifier" edge.

## 5. Term/value nodes

Representative Term nodes include:

- EntityRef
- KindRef
- QuantityValue
- LocationValue
- RegionValue
- PathValue
- GeometryProfile
- ColorProfile
- InformationValue
- CollectionValue
- TimePointValue
- TimeIntervalValue
- EventRef

The implementation can use tagged structures rather than new language Categories.

## 6. Reference node

`Reference(kind, context_parameters, expected_type)`

Examples:

- Self
- This
- Here
- Now
- selector-based references

Reference resolution occurs after static typing.

## 7. Functional application

`FunctionCall(function_entry, arguments) -> Term`

Used for functional Relations/Attributes such as:

- Distance
- Center
- Surface
- Form
- Duration
- ColorOf
- Phase

The output type is declared by the lexicon frame.

## 8. Property proposition

`PropertyApply(property, subject) -> Proposition`

Stores the normalized predicate/constraints.

Family-member Properties may normalize to equality over an Attribute.

Example:

Solid(x) -> Equal(Phase(x), SolidValue).

## 9. Relation proposition

`RelationApply(relation, role_map) -> Proposition`

Role order is normalized to named roles regardless of surface positional/case syntax.

## 10. Process/EventSpec

`ProcessApply(process, role_map) -> EventSpec`

The EventSpec contains:

- Process identity;
- participant bindings;
- output/result declarations;
- spatial/temporal constraints;
- state-change constraints;
- execution traits.

It is not an Event yet.

## 11. Proposition operators

Normalized nodes include:

- Not(P)
- And([P...])
- Or([P...])
- If(P,Q,Else?)
- All(binder, domain, P)
- Some(binder, domain, P)
- temporal quantifiers

Operator type rules are explicit.

## 12. EventSpec operators

Normalized nodes include:

- AndEvents([E...])
- Sequence([E...])
- IfEvent(condition,E,Else?)
- Each(collection,binder,E)
- Repeat(count,E,period?)
- Persist(state/E,lifetime)
- Trigger(binders,condition,E,lifetime,rearm)

These structures preserve distinctions such as simultaneous versus ordered actions.

## 13. Binder node

A Binder has:

- internal unique ID;
- declared type/domain;
- optional Kind restriction;
- lexical source label for diagnostics only.

Variable references point to Binder IDs rather than textual variable names.

This prevents capture/shadowing bugs.

## 14. Command node

`Command(event_spec, power, context_requirements)`

stores:

- executable EventSpec;
- supplied Power expression/value;
- written mana cost;
- reference requirements;
- persistent-control metadata if relevant.

Question/Assertion are separate sentence node types.

## 15. Assertion node

`Assertion(proposition)`

represents a declarative sentence.

It does not automatically query reality or produce Information.

## 16. Question node

`Question(proposition/query_shape)`

represents an interrogative speech act/information structure.

It does not itself perform Find/Sense.

## 17. Quantity AST

Numeric nodes can include:

- LiteralOne / unary count
- Zero
- Opposite
- Add
- Multiply
- Divide
- Power
- Root
- UnitApply
- Ratio

Normalization computes exact value/dimension when possible while preserving source-cost metadata.

## 18. Constraint set

Each expression can accumulate a normalized ConstraintSet containing:

- type/domain constraints;
- equality/inequality;
- family membership;
- spatial relations;
- temporal relations;
- identity conditions;
- state requirements;
- world-ontology classifier references.

Constraint satisfiability is checked after structural typing.

## 19. Failure classes

Static validation should distinguish:

- UnknownRoot
- InvalidRootSegmentation
- IllegalCompound
- AmbiguousCompound
- SyntaxError
- TypeMismatch
- InvalidRole
- MissingRequiredRole
- FreeVariable
- DimensionMismatch
- InvalidUnit
- ContradictoryConstraint
- SemanticallyIncomplete

Execution adds:

- ReferenceNotFound
- ReferenceNotUnique
- ReferenceInaccessible
- CapabilityUnsupported
- RequiredPowerTooHigh
- ResourceInsufficient
- TemporalCycle
- RuntimeConstraintFailure
- ContestLost/Tied

Exact diagnostic labels may change, but distinct causes should not collapse into "spell fails."

## 20. Normalization

Normalization is meaning-preserving.

Examples:

- OppositeBefore -> After
- Not(Not(P)) -> P where logical model permits
- Solid(x) -> Phase equality representation
- semantic molecule -> canonical definition/reference
- arithmetic -> exact canonical value
- Ratio(3,5) -> normalized 3:5
- ConverseIn -> Contain

Normalization does not change written mana cost.

## 21. Semantic molecule handling

A registered one-rune semantic molecule may normalize to a complex AST definition.

The AST records:

- source lexical cost = 1;
- normalized semantic expansion = complex.

This is the implementation mechanism for legitimate linguistic compression.

## 22. Alias handling

Ordinary Name/alias Information never substitutes a lexicon entry ID during magical parsing unless a separate explicit quotation/reference operation is being performed.

This prevents macro-like mana exploits.

## 23. World model hooks

AST constraints/functions can reference world-model IDs for:

- Kind classifiers;
- Units;
- generation profiles;
- physics rules;
- resistance;
- coordinate frames.

The parser does not hard-code every setting fact.

## 24. Determinism tests

The reference implementation should test:

- parse round-trips;
- normalization idempotence;
- type-check determinism;
- equivalent expression normalization;
- mana-cost preservation;
- binder scope;
- selector ties;
- contradiction classification;
- stress-test corpus results.

## 25. Canonical serialization

Every validated AST should serialize to a stable machine-readable representation.

This enables:

- regression tests;
- comparing parser versions;
- spell storage;
- tooling;
- independent implementation checks.

The serialization is not itself the rune language and does not grant magical compression.

## 26. Result

The semantic AST gives the project an implementation target precise enough to expose hidden ambiguity rather than letting a future parser invent meaning.


## 27. Discourse and epistemic nodes

The corpus test adds implementation-facing structures for connected prose.

### UtteranceContext

Stores:

- speaker;
- addressees;
- utterance time/location;
- discourse reference time;
- discourse referents/salience;
- naming/language context.

Nested quotation/speech pushes a child UtteranceContext so Self/You/Here/Now resolve correctly.

### DiscourseRef

Represents an anaphoric/definite/proper-name reference before final resolution.

It must resolve to one typed discourse referent or remain ordinary-language ambiguous.

Magical commands require the resolved identity to be frozen before execution.

### Temporal/aspect nodes

Add normalized nodes such as:

- Past(X)
- Present(X)
- Future(X)
- Ongoing(EventSpec)
- Completed(EventSpec)
- Habitual(pattern, context)
- Generic(domain, predicate, context)

Contextual nodes carry explicit non-magical/contextual metadata.

### OpenQuestion

OpenQuestion(binders, proposition/query-shape)

Binders may range over Entity, Quantity, Location, Event, Method, Explanation, Information, or other typed semantic values.

### Epistemic nodes

Represent:

- Confidence(mind,P)
- Believe(mind,P)
- Know(mind,P)
- EvidenceFor(info,P)
- EvidenceAgainst(info,P)
- Expect(mind,P/E)
- Assert(speaker,P)
- Promise(speaker,addressee,E)
- Explanation

These nodes must never normalize a belief/assertion directly into truth of its embedded Proposition.

## 28. Relative-change nodes

Add:

- BeforeValue(value-expression,event)
- AfterValue(value-expression,event)
- Preserve(value-expression,event)
- ApproxEqual(a,b,tolerance)
- Almost(predicate,subject,context)
- Requires(outcome,prerequisite)

A Preserve node contributes equality between pre/post snapshots to the EventSpec ConstraintSet.

## 29. Distribution and control nodes

World packages may provide structured Distribution values with functions such as:

- DistributionOf
- LocalDensity
- TotalAmount

Control(controller,target/process) is a state Relation.

Redistribute creates an EventSpec over a Distribution and may carry Preserve(TotalAmount(...)) constraints.

These structures are optional world capabilities, but the AST must be able to represent them without hard-coded mana physics.
