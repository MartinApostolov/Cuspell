# Collections, Quantifiers, and Binding

_Status: current working specification_

This file defines semantic Collections, quantification, selection, distribution, binders, and variable scope.

## 1. Collection values

A `Collection<T>` is a typed semantic value whose members have type T.

A Collection is not automatically a physical Entity or Group.

Examples:

- Collection<Entity>
- Collection<Information>
- Collection<Region>
- Sequence<EventSpec>

A world/social Group is a distinct Entity concept even when its current members can be collected.

## 2. Binders are grammar

Canonical binder declaration:

`a:Domain`

Variable reference:

`$a`

The variable label and binder punctuation are zero-mana grammar. The semantic domain itself carries its normal meaning/cost.

A variable cannot escape its binder scope. A magical Command with a free variable is invalid.

Legacy `[a:Domain]` spelling may remain parser-compatible but is not canonical.

## 3. Universal quantification

`All` is meaning-bearing.

Conceptual semantics:

`All(domain/binder, predicate) -> Proposition`

Canonical example:

`All a:Entity Exist $a.`

A named Kind may be the binder domain:

`All a:«Know«MoveLifeThing»» Life $a.`

All produces a Proposition; it does not produce one arbitrary target Entity.

## 4. Existential quantification

`Some` is meaning-bearing.

Example:

`Some c:«LowExtent«MoveLifeThing»» At $c Here.`

This states that at least one bound Cat satisfies the proposition.

It does not export an arbitrary witness into a later singular Process unless another construction explicitly binds/selects that witness.

## 5. Binder domains

A binder domain may be:

- a semantic type;
- a Kind / named Kind;
- a Collection-compatible domain required by the consuming frame.

A Kind can therefore participate in logic without being coerced into one arbitrary member.

## 6. Collection construction

`Collect` constructs a Collection from a binder/predicate under the relevant accessible scope.

Conceptually:

`Collect binder predicate -> Collection<T>`

Example shape:

`Collect a:Entity In $a ThisRegion`

The exact collection must still be resolvable under information/search/world capability rules.

## 7. Selection scope

A globally meaningful Kind does not imply magical omniscience.

Collection construction/selection may require an explicit or already-resolved scope, such as:

- a Region;
- a known finite Collection;
- a connected structure;
- a recognized finite Group;
- a world-domain search supported by explicit sensing/information capability.

Failure to access the domain is a capability/reference problem, not permission to guess.

## 8. Distribution over collections

A singular Process never silently distributes over a Collection.

`Each` explicitly distributes an EventSpec template across members.

Conceptually:

`Each collection binder EventSpec-template -> EventSpec`

The result requires one instantiated component event per resolved member.

Default Each semantics do not imply a Sequence unless ordering is explicitly supplied.

## 9. Selection is explicit

A multi-member Collection cannot fill a singular Entity slot without an explicit selector.

Current selector machinery includes:

- `Unique`;
- `MinBy`;
- `MaxBy`;
- `First` / `Last` for ordered sequences;
- `Random`.

Tie behavior is part of selector semantics. `MinBy` / `MaxBy` preserve ties; `Unique` is needed when exactly one result is required.

The earlier generic OneOf-style “pick something” shortcut is not accepted for magical targeting.

## 10. Membership

`Member value group` represents current group membership under its registered frames.

Semantic Collection membership and world Group identity remain distinct concepts.

## 11. Count and ratios

`Count Collection` returns a nonnegative integer quantity.

Proportional/generic statements can combine Count, Ratio, comparisons, and contextual High/Low thresholds instead of requiring one primitive word per English quantifier.

## 12. Ordered collections

A `Sequence<T>` is an ordered collection/value.

Sequence values may support:

- First;
- Last;
- ordered comparison/access where registered.

The EventSpec form of `Sequence` uses ordered event semantics and has canonical flat surface syntax:

`Sequence E1 E2 E3!`

## 13. Finite collection literals

`{A,B,C}` is a Collection value when all members are type-compatible.

Braces and commas are zero-mana structure.

This syntax should not be used just to expose the internal collection backing canonical And/Or or Sequence/Concurrent.

## 14. Binder nesting

Binders may nest.

Each variable reference resolves to its valid lexical binder scope.

Conceptually:

`All a:Entity Some b:Entity ParentOf $a $b`

The actual head/frame structure determines the scopes; no discourse plausibility is used.

## 15. Collection typing

Collection operations preserve/refine member types where possible.

Examples:

- Filter(Collection<Entity>, predicate) -> Collection<Entity>
- Partition(Collection<T>, n) -> Collection<Collection<T>>
- selector over Collection<T> -> T or Collection<T>, according to selector semantics.

Parser constraints may bind a selector's key binder to the member type of the collection being inspected.

## 16. Open questions use the same binder machinery

Open questions are not a second variable system.

`p:Entity ParentOf $p Self?`

introduces an Entity variable and asks for bindings that satisfy the query.

`g:Location At This $g?`

asks for Location bindings.

## 17. Anaphora is separate

Bound variables solve identity within a formal expression.

Cross-sentence pronouns/references such as This, That, They, or a proper Name belong to discourse/reference semantics rather than binder scope.

Magical Commands should only execute when those contextual references are sufficiently resolved.

## 18. Mana

Meaning-bearing roots such as All, Some, Collect, Each, Count, Filter, Partition, MinBy, MaxBy, and Random cost normally when written.

Binder labels, `:` declaration punctuation, and `$` variable references are zero-mana grammar.

## 19. Result

The collection/binding architecture prevents three dangerous shortcuts:

- a Kind silently choosing one member;
- existential quantification silently exporting a target;
- a singular Process silently distributing across a Collection.

All three require explicit structure.
