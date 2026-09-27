# Selection and Reference Resolution

_Status: working specification v0.1_

This file defines deterministic and explicitly nondeterministic selection from Collections and refines singular Reference resolution.

## 1. Selection is not quantification

Quantifiers answer logical questions.

Collections represent multiple values.

Selectors reduce a Collection according to an explicit policy.

None of these may be silently substituted for another.

## 2. Unique

`Unique(collection) -> member`

succeeds only when the Collection contains exactly one member.

Otherwise it produces a reference-resolution failure.

This is the preferred way to turn a predicate result into a singular target when uniqueness is expected.

## 3. Nearest

`Nearest(collection, reference) -> Collection`

returns every member with the minimum registered Distance to the reference.

It returns a Collection deliberately because ties are possible.

To require one target:

`Unique(Nearest(collection, reference))`

A tie therefore fails rather than being broken by GM preference.

## 4. Farthest

Farthest is the corresponding maximum-Distance selector and likewise returns all tied maxima.

If Near/Far remain a reversible semantic pair, Farthest need not automatically be OppositeNearest because the lexical categories/functions differ.

## 5. Lowest and Highest

`Lowest(collection, scalar-function) -> Collection`

`Highest(collection, scalar-function) -> Collection`

return all tied extrema after dimension-valid comparison.

Examples can select by:

- Mass;
- Distance;
- Damage magnitude;
- age/time;
- other ordered Attributes.

Singular selection again uses Unique if required.

## 6. First and Last

First/Last require an ordered `Sequence<T>`.

They are invalid on an unordered Collection.

This prevents accidental use of hidden database/order implementation details.

## 7. Random

An explicitly nondeterministic selector may exist:

`Random(collection) -> member`

Its meaning is objective even though the selected result is not predictable: choose one member according to the magical system's registered random distribution.

Random is meaning-bearing and costs mana.

It must never be inserted implicitly to resolve ambiguity.

## 8. Filter

`Filter(collection,[x],predicate($x)) -> Collection`

is equivalent in role to Collect over an existing Collection and can be a conventional semantic molecule/operator.

This separates search domain from predicate restriction.

## 9. Search versus selection

`Find` acquires otherwise unavailable reference Information.

`Collect/Filter` constructs collections from resolvable semantic domains.

Selectors choose from an already resolved Collection.

A selector does not grant detection ability.

## 10. Name lookup

Selecting by Name requires:

- naming context/language;
- collection/search domain;
- Name Relation.

If several Entities share the Name, the result is a Collection.

No Name automatically functions as a globally unique ID.

## 11. Reference pipeline

A singular target expression can conceptually follow:

1. establish accessible search domain;
2. Find/Collect matching values;
3. Filter by predicates;
4. apply selectors;
5. Unique if singular role required.

The parser can compress common cases, but the semantic structure remains explicit.

## 12. This

`This` is valid only when the command context contains an explicitly designated referent of the required type.

Pointing/selection mechanics are gameplay input to the Reference.

This does not perform a search.

## 13. You

`You` resolves to the formally defined addressee/target participant in the speech/casting context.

If no unique addressee is established, You fails for magic.

## 14. Self

Self resolves to the Command issuer/caster identity according to casting context.

It remains stable during the Command unless identity semantics explicitly change.

## 15. Here

Here resolves to activation-origin Location as defined in the spatial specification.

## 16. OtherThan

Relative "other" semantics are:

`OtherThan(collection/value, reference)`

or filtering by NotSame.

A bare Other without a comparison set/reference is not a magical selector.

## 17. Tie behavior

Selectors do not contain hidden tie-breaking rules unless the lexical entry states one.

Default extrema semantics return all ties.

If a game wants a deterministic tie-breaker, it must be a registered selector such as:

- earliest;
- lexically ordered;
- nearest then lowest mass;
- Random.

## 18. Empty collections

Selectors on an empty Collection return no result/reference failure.

They do not manufacture a default Entity.

## 19. Selector composition

Selectors can compose.

Example abstractly:

`Unique(Lowest(Nearest(collection,Self),Mass))`

means:

1. find nearest tied members;
2. among those, keep lowest Mass;
3. require one unique result.

This is objective even when compacted into advanced vocabulary later.

## 20. Result

Target choice now has explicit semantics for uniqueness, ties, ordering, extrema, and randomness.

The magic engine never resolves multiple matches by guessing which one the caster intended.
