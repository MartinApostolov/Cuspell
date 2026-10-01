# Identity, Existence, and State Transition

_Status: working specification v0.1_

This file formalizes Entity identity, creation/destruction, transformations, Process results, and Begin/End over stateful relations.

## 1. Entity identity

Every concrete Entity has an identity independent of its current Properties.

`Same(A,B)`

is true only when A and B resolve to the same Entity identity.

Equal Properties, Equal Form, same Kind, or copied structure do not imply Same identity.

## 2. Existence

Introduce an objective state predicate:

`Exist(Entity)`

Traits:

- state-predicate
- ontology domain

Existence means the Entity currently participates in the active world state accessible to the ontology.

Historical Information about an Entity can remain after Exist becomes false.

## 3. Create is not merely BeginExistence

The earlier idea:

`Create = BeginExistence`

is incomplete for genuinely new things because Begin requires an already identifiable subject.

Therefore retain `Create` as a Process with a fresh-result frame.

Conceptually:

`Create(profile/kind, location?, initial-properties?) -> EventSpec :result Entity`

Create allocates a **new identity** satisfying the requested initial profile.

The magical execution layer may restrict what Kinds can be created and what material/source rules apply.

## 4. Reinstating an existing identity

`BeginExist` / Begin(Exist(X)) is meaningful when X already has a resolvable non-active identity in the ontology.

Examples might include setting-specific restoration, summoning from an inaccessible state, or metaphysical resurrection.

It is not the same as Create because it preserves identity.

Whether non-existing identities remain referenceable is world-metaphysics data.

## 5. Destroy

`Destroy(Entity)`

can normalize to:

`End(Exist(Entity))`

when the magic system supports direct existence termination.

Destroy preserves historical identity records but removes the Entity from active existence.

This is stronger than:

- Damage;
- breaking structure;
- EndLife.

A destroyed object and a broken object are not equivalent.

## 6. Life versus existence

Life is a biological state, not existence itself.

Therefore:

- EndLife does not imply EndExist;
- a corpse may continue to Exist;
- a dead organism can retain historical/biological Kind relations;
- BeginLife can be meaningful on an existing dead body if biological constraints are satisfied.

This makes resurrection distinct from creation.

## 7. Transform preserves identity by default

A transformation Process changes Properties, structure, or Kind membership while preserving the Entity identity unless explicitly defined otherwise.

Conceptually:

`Transform(theme, target-profile) -> EventSpec`

Same(theme_before, theme_after) remains true.

This matters for:

- ownership;
- Names;
- memories;
- curses/enchantments;
- identity-sensitive magic.

## 8. Replacement is different from transformation

Destroying A and creating B with Equal Form does not make B Same as A.

A replacement/copy can be indistinguishable under selected Properties while remaining a new identity.

Magic must not silently choose between transformation and replacement.

## 9. State predicates include Relations

A state need not be a unary Property.

Many Relations represent ongoing states:

- Have(A,B)
- Know(A,P)
- Remember(A,Info)
- In(A,Region)
- Name(Sign,Entity,Context)
- Friend(A,B), if treated as a persistent social relation

Add trait:

`state-predicate`

to any Property/Relation whose truth can persist and undergo boundary transitions.

## 10. Begin and End over state predicates

Generalize boundary semantics:

`Begin(Proposition[state-predicate]) -> EventSpec`

`End(Proposition[state-predicate]) -> EventSpec`

Examples:

- Begin(Have(A,B)) -> acquisition of possession relation.
- End(Have(A,B)) -> loss/transfer away.
- Begin(Know(A,P)) -> learning/coming to know.
- End(Remember(A,M)) -> forgetting/loss of retrievable memory relation.
- Begin(In(A,R)) -> entry.
- End(In(A,R)) -> exit.

This greatly reduces the need for primitive verbs while keeping their semantics objective.

## 11. Conventional verbs may lexicalize state transitions

Common Processes can still exist as registered compression.

Examples:

- Get may lexicalize Begin(Have(...)).
- Lose may lexicalize End(Have(...)).
- learning is now written as the typed transition `Begin(Know(...))`, `Begin(Can(...))`, or `Begin(Understand(...))`; the generic Learn root has been removed.
- Forget may lexicalize End(Remember(...)).
- Enter may lexicalize Begin(In(...)).
- Exit may lexicalize End(In(...)).

A short registered rune legitimately costs less than the expanded construction.

## 12. Giving as coordinated possession transition

There is no separate `Give` root in the minimized core.

Giving is written as the coordinated possession transition:

- `End(Have(source, theme))`
- `Begin(Have(recipient, theme))`

Canonical minimized form:

`Concurrent EndHave source theme BeginHave recipient theme`

Optional control/location consequences remain separate unless another world rule entails them. Generic `Transfer` is not substituted here because Transfer's source/destination roles do not themselves assert possession.

## 13. Event results

Some Processes produce a new Entity/value as part of their semantics.

Examples:

- Create -> new Entity;
- Copy Information -> new Information token/record;
- Join -> possibly new composite Entity;
- Divide physical object -> multiple result Entities;
- Find/Measure -> Information/value result if modeled as Processes.

Process frames may declare **result roles**.

## 14. Result binders

Sentence grammar gains zero-mana result-binding syntax.

Temporary abstract notation:

`Create(Water,...):result [w]`

introduces bound variable `$w` for the created Entity in the containing scope.

Example:

`Sequence(Create(Water,...):result [w], Move($w,Here))`

The binder mark is grammar and costs zero mana.

The semantic roots Create, Water, Move, etc. still cost mana.

## 15. Result binding requires guaranteed cardinality

A singular result binder is legal only when the Process frame guarantees one result.

If a Process may produce multiple results, it must bind:

- a Collection;
- explicitly indexed results;
- or a structure whose cardinality is known.

Magic does not arbitrarily choose one output.

## 16. Fresh identity guarantee

Create-result binders are fresh:

the resulting identity is not Same as any currently existing Entity unless the Process explicitly restores/reinstates an existing identity rather than creating.

This is part of Create semantics.

## 17. Kind membership and identity

Kind membership can change without identity changing.

However a canonical Kind may declare identity-essential constraints.

A Transform into/out of such a Kind changes classification while preserving Entity identity if the transformation is permitted.

This does not imply that the Entity's historical Kind membership is erased.

Temporal queries can still refer to former classifications.

## 18. Historical state

The ontology can record state transitions as Events.

Therefore concepts such as:

- FormerLife;
- former Name;
- previous Form;
- prior owner

should normalize to temporal relations over recorded Events/states rather than vague memory.

Magical access to historical truth may still require an Information/detection capability.

## 19. Names do not create identity

Assigning a Name creates a naming Relation.

It does not create, merge, or overwrite Entity identity.

Two Entities can share a Name without becoming Same.

Changing a Name does not Transform the named Entity.

## 20. Copies

Information Copy creates a distinct token/record with Equal informational content.

If physical copying is later defined, the copied Entity also receives a distinct identity.

"Perfect copy" means equality across a declared profile, not identity.

## 21. Result

Identity is now stable across ordinary change, while creation, destruction, transformation, restoration, and copying have distinct formal meanings.

Begin/End also generalize cleanly from unary state Properties to persistent state Relations.
