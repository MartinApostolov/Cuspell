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
- Extent (including temporal Event extent)
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

AST argument order is normalized to internal role labels regardless of surface positional syntax. Those labels are implementation metadata, not Cuspell words.

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
- ValueDomainMismatch
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

- After-meaning -> `Before` with reversed arguments
- Not(Not(P)) -> P where logical model permits
- Solid(x) -> Phase equality representation
- semantic molecule -> canonical definition/reference
- arithmetic -> exact canonical value
- Ratio(3,5) -> normalized 3:5
- containment perspective -> the same `In(item,region)` Relation with direct role order

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

Connected prose introduces implementation-facing context/reference structures.

### UtteranceContext

Stores values such as speaker, addressees, utterance time/location, discourse reference time, discourse referents/salience, and naming/language context.

Nested speech can push a child UtteranceContext so Self/You/Here/Now resolve against the represented utterance rather than the outer narrator.

### DiscourseRef

Represents a contextual/anaphoric/name-based reference before final resolution.

Ordinary discourse may remain ambiguous; magical execution requires the relevant reference to resolve objectively enough for the Command.

### Temporal/discourse nodes

Current normalized forms include ordinary nodes such as:

- Before(value/event, reference)
- During(EventSpec/Proposition/value, temporal target)
- Rate(value/EventSpec, interval?)
- High(Rate(...)) for contextual habitual frequency
- Counterfactual(antecedent, consequent)

Removed convenience roots do not require dedicated AST node kinds when their meanings normalize to surviving structures.

### OpenQuestion

`OpenQuestion(binders, query)`

Binders may range over any registered semantic type/Kind domain accepted by the parser, including Entity, Quantity, Location, Event, Method, Explanation, and Information.

### Epistemic nodes

Represent current semantics such as:

- Confidence(mind,P)
- Believe(mind,P)
- Know(mind,P/Information)
- EvidenceFor(info,P)
- Expect(mind,P/EventSpec)
- Assert(speaker,P)
- AnswerFor(info,question)
- Explains(explanation/reason,target)
- Meaning(sign,content)

A belief/assertion node never normalizes directly into truth of its embedded Proposition.

Promises are represented compositionally through Say plus a Begin Obligated transition rather than a Promise AST primitive.

## 28. Relative-change structures

Current structures include:

- BeforeValue(value,event)
- AfterValue(value,event)
- Preserve(value,event)
- Change(theme,attribute,target/constraint)
- Distance(spatial-a,spatial-b) -> Quantity<Length>
- Almost(Proposition/EventSpec) for contextual near-satisfaction/near-occurrence
- Requires(outcome,prerequisite)

Approximate equality is ordinary bound/comparison composition rather than a dedicated ApproxEqual node.

A Preserve node contributes equality between pre/post snapshots to the EventSpec constraint structure.

## 29. Distribution and control structures

Current Distribution values/functions include:

- DistributionOf(resource,host)
- Density(distribution,region)
- TotalAmount(distribution,region?)

`Control(controller,target)` is a persistent StateProposition-producing Relation.

Redistribution uses the general Transfer EventSpec over a Distribution, optionally supplying its positional destination-profile slot; there is no dedicated Redistribute AST primitive.

## 30. Surface-source structure

Canonical surface syntax is v0.10.

Whitespace, tight adjacency, sentence punctuation, the omission marker, rune-native binders, standalone `:` group closure, and player-facing parentheses are source structure/metadata rather than semantic AST concepts unless they introduce semantic values/operators.

Diagnostics retain source spans even when purely grammatical marks disappear after parsing.

Pipe remains a parser/debug compatibility mechanism rather than current player syntax:

- `Move|A|B` is one independently parsed debug/legacy group;
- outer tokens cannot leak into that group;
- new player-facing Cuspell should use ordinary typing, tight adjacency, or parentheses instead.

Whitespace never creates an AST Sequence/And node by itself.

## 31. Typed prefix application

The AST builder uses registered output/argument types to infer nested application boundaries.

Example:

`Equal Extent ThisEvent «DurationUnit» @@.`

can build equality between `Extent(ThisEvent)` and a typed Time quantity without explicit AST-like grouping in the source.

Parentheses/pipe may force source grouping, but unnecessary grouping does not change normalized semantics.

## 32. Descriptor/invocation distinction

A lexical entry can appear as:

- a descriptor/reference to the function/Attribute itself when a frame expects a descriptor;
- a functional invocation when the frame expects its output value.

Example:

`Change This Density Q`

uses Density as an AttributeDescriptor.

`BeforeValue Density This`

invokes Density(This).

The expected slot type determines which reading is legal.

## 33. Event-local snapshot resolution

When unary BeforeValue/AfterValue occurs inside one uniquely enclosing EventSpec result context, normalization inserts that EventSpec's boundary context.

Thus a local:

`BeforeValue Density This`

inside a Change target can normalize to:

`BeforeValue(Density(This), EnclosingEvent)`.

Outside a unique enclosing event context, the omitted Event argument is invalid.
