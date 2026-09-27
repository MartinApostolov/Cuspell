# Collections, Quantifiers, and Binding

_Status: working specification v0.1_

This file resolves the collection/binding problem left open by the first sentence-grammar pass.

## 1. Collection values

A Collection is a typed semantic value:

`Collection<T>`

where T is the member type.

A Collection is not automatically a physical Entity. It is a semantic set/list of references or values.

Examples:

- Collection<Entity>
- Collection<Human>
- Collection<Information>
- Sequence<EventSpec>

## 2. Bound variables are grammar, not semantic runes

Quantification requires repeated reference to the same participant.

Cuspell therefore uses **bound-variable marks** as zero-mana grammar.

Temporary transliteration:

- `[a:Human]` introduces binder a constrained to Human.
- `$a` refers to that bound value inside its scope.

The letters a/b/c are transcription labels, not meaning-bearing roots and have no mana cost.

The final rune script can use graphical binder marks rather than variable names.

A bound variable cannot escape its scope.

A magical Command with an unbound variable is invalid.

## 3. Why variable reuse is zero mana

A binder does not introduce a new world concept each time the variable is referenced. It preserves identity inside a structure already written.

This is analogous to grouping punctuation and case marking.

Semantic roots that determine the domain/predicate still cost mana.

## 4. Universal quantification

`All` is a meaning-bearing logical Operator.

Abstract form:

`All([a:Domain], Proposition($a)) -> Proposition`

Example conceptual structure:

`All([a:Human], Life($a))`

= every Human in the quantified domain satisfies Life.

All produces a Proposition. It does not produce one giant Entity target.

## 5. Existential quantification

`Some` is a meaning-bearing logical Operator.

`Some([a:Domain], Proposition($a)) -> Proposition`

= at least one member of Domain satisfies the Proposition.

`None` can normalize to:

`Not(Some(...))`

unless a conventional None rune is retained as lexical compression.

## 6. Quantifier domain

A binder domain may be:

- a Kind;
- an existing Collection;
- a restricted Collection.

A Kind can therefore be used logically without selecting one arbitrary member.

This resolves the earlier problem where a Process expecting an Entity must not silently accept Human and choose a human.

## 7. Collection construction

Introduce/retain a meaning-bearing Operator provisionally called `Collect`.

`Collect([a:Domain], predicate?) -> Collection<T>`

It constructs the members of Domain satisfying the predicate.

Example:

`Collect([a:Human], In($a, RoomRef))`

= Collection of Humans in the referenced room.

If no predicate is written, Collect denotes all accessible/resolvable members of the Domain under the supplied selection scope.

## 8. Selection scope

Collection construction must define the search/selection domain sufficiently for the reference system.

Possible scopes include:

- a spatial region;
- an explicitly known collection;
- a connected structure;
- a recognized finite group;
- a world-domain search when a magical detection capability explicitly supports it.

A global Kind is semantically objective but may be non-resolvable/non-executable without an information/search capability.

This is a capability failure, not ambiguity.

## 9. Distribution over collections

A singular Process does not automatically distribute over a Collection.

Introduce/retain `Each` as a meaning-bearing distribution Operator:

`Each(collection, [a], EventSpec($a)) -> CompositeEventSpec`

The resulting composite contains one instantiated EventSpec per resolved member.

Default Each semantics are unordered/concurrent conjunction, not Sequence.

If ordered iteration is needed, use an ordered Sequence plus an explicit iteration operator.

## 10. Example distribution

Conceptually:

`Each(Collect([a:Human], In($a, Region)), [b], EndLife($b))`

creates a composite EventSpec containing EndLife for every selected Human.

This may be extraordinarily difficult to execute, but its meaning is objective.

RequiredPower and collection scaling are execution-layer questions.

## 11. No arbitrary existential target selection

`Some(Human, ...)` is a Proposition.

It does **not** mean:

"choose whichever Human reality wants."

A command requiring one member of a Collection needs an explicit selection policy.

Possible selectors:

- First under an explicit ordering;
- Nearest to a reference;
- Random;
- Lowest/Highest by scalar attribute;
- uniquely matching predicate.

Until such a selector is specified, a multi-member Collection cannot fill a singular Entity role.

## 12. `OneOf`

The earlier candidate `OneOf` is rejected as a generic magical selector because it leaves choice policy unspecified.

It may survive in ordinary logical language meaning membership in a set, but selection for magic must be deterministic or explicitly random.

## 13. Membership

Use a typed Relation conceptually equivalent to:

`Member(value, collection) -> Proposition`

The earlier `Among` candidate can be defined as a spatial/social special relation if useful, but should not carry generic set-membership semantics by accident.

## 14. Count

Define:

`Count(Collection) -> Quantity<dimensionless integer>`

This supports exact cardinality.

Many/Few remain contextual threshold predicates over Count unless fixed standards are defined.

## 15. Ordered collections

A `Sequence<T>` is an ordered Collection<T>.

Sequence preserves order and may support:

- First
- Last
- index access
- ordered iteration

The EventSpec constructor `Sequence(E1,E2,...)` uses this ordered semantics and executes events in order.

## 16. Pair and finite literal collections

Grammar may support zero-mana structural delimiters for finite collection literals while semantic inclusion still comes from the listed values.

Conceptual:

`{A,B,C}`

The braces/commas are syntax.

This is useful for And/Join/Ratio structures without requiring a dedicated Pair rune.

Exact surface notation remains provisional.

## 17. Both and Either

`Both(A,B)` can be a conventional short form for a two-member conjunction/collection.

`Either` is ambiguous between:

- logical Or;
- a two-member collection;
- selection of one branch.

Therefore no magical Either selector is accepted until the intended semantic frame is explicit.

Logical disjunction uses Or.

## 18. Other

`Other` is not a global unary Property.

It is relative identity exclusion:

`OtherThan(value, reference/set)`

and can be derived from NotSame/member exclusion.

A future compact Other rune must carry/bind its comparison referent through grammar.

## 19. Group

Distinguish:

- semantic Collection<T>;
- a Group Entity recognized by the world/social ontology.

A Group Entity can have a functional relation:

`Members(GroupEntity) -> Collection<Entity>`

This allows parties, organizations, swarms, teams, etc. to be first-class Entities while their membership is represented as a collection.

## 20. Collection identity

Two Collections can have:

- Equal membership;
- Same collection identity, if they are first-class collection objects;
- Equal Sequence order;
- different construction expressions that normalize to the same membership.

The language must distinguish value equality from Entity identity as elsewhere.

## 21. Collection mutation

Adding/removing a member is a Process over a collection/group structure.

Do not overload Join automatically for set membership unless the collection's frame declares that structural meaning.

Possible future Processes:

- Include
- Exclude
- Insert
- Remove

They can later be derived or lexicalized.

## 22. Quantification inside Kind definitions

Relationally defined Kinds may use quantifiers.

For example, an artifact definition may require:

- Some opening;
- All required structural Parts;
- at least one grip;
- no gap above a threshold.

This allows semantic molecules to be formally rich without adding special grammar.

## 23. Binder nesting

Binders may nest.

Variable labels must resolve to the nearest matching binder or otherwise use unique marks.

Example abstractly:

`All([a:Human], Some([b:Tool], Have($a,$b)))`

No discourse inference is needed.

## 24. Anaphora is separate

Bound variables solve identity *inside* a formal expression.

Cross-sentence pronouns such as "he," "it," "they," or "the former one" are a separate discourse/anaphora system.

Magical commands should prefer explicit References/binders rather than context-heavy anaphora.

## 25. Information cost

The roots:

- All
- Some
- Collect
- Each
- Count

are meaning-bearing and cost mana when written.

Binder marks and variable references are grammar and cost zero.

This rewards structural fluency without permitting arbitrary semantic aliases.

## 26. Result

Quantifiers now produce Propositions, collection constructors produce Collection values, and distribution over many targets is explicit.

The system therefore avoids three dangerous shortcuts:

- Kind silently selecting an instance;
- Some silently choosing a target;
- Process silently distributing across a collection.
