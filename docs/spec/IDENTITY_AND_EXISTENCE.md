# Identity, Existence, and State Transition

_Status: current working specification_

This file records the current identity/existence model after root minimization.

## 1. Entity identity

Concrete Entities have persistent identity independent of their current Properties, Form, Name, location, or other state.

Current Entity identity equality is the Entity frame of:

`Equal A B`

This replaces the former standalone `Same` root.

Equal Form, equal Properties, or membership in the same Kind does not imply Entity identity.

## 2. Existence

`Exist subject` is a persistent state predicate.

The current executable core supports Exist over Entities and other semantic values such as Sign tokens.

Therefore state-boundary machinery applies normally:

`Begin Exist X`

`End Exist X`

Ending Exist is the current compositional destruction meaning; there is no standalone Destroy root.

## 3. Begin/End require an identifiable subject

`Begin Exist X` changes the existence state of an already representable semantic subject X.

It does **not** allocate a new identity.

Fresh identity allocation is now the distinct `Create` Process:

`Create x:Entity profile`

`Create` allocates exactly one Entity identity that has never previously been allocated, binds it as `$x` inside the supplied profile, and realizes the new Entity so the binder domain plus objective profile hold immediately after creation.

Examples:

`Create x:Entity Matter $x And At $x Here!`

`Create x:«LowExtent«MoveLifeThing»» Life $x And At $x Here!`

The second form uses the existing historical Cat Kind as the result-binder domain. The quoted Kind still pays its normal written Old Name cost.

The profile must actually constrain or relate the fresh result. A command such as `Create x:Entity AtSelfHere!` is invalid because its profile says nothing about `$x`.

Creation itself implies the new result Exists; writing `Begin Exist $x` is therefore unnecessary.

## 4. Life versus existence

`Life X` and `Exist X` are distinct state predicates.

Therefore:

- `End Life X` does not entail `End Exist X`;
- a corpse may still Exist;
- historical information about an Entity may remain after Exist ends;
- restoring Life and restoring Exist are distinct world/metaphysical operations.

## 5. Identity across ordinary change

A `Change` EventSpec changes a registered Attribute/family value of an existing theme. It does not allocate a replacement identity.

Likewise, ordinary movement, possession change, state boundaries, and other EventSpecs do not silently replace the participant with a new Entity.

If a future world operation explicitly destroys one Entity and creates another, identity is not preserved merely because their profiles are equal.

## 6. Persistent Relations are state predicates

State boundaries apply to registered persistent Relations as well as unary Properties.

Examples:

- `Begin Have A B`;
- `End Have A B`;
- `Begin Know A P`;
- `End Remember A I`;
- `Begin In A R`;
- `End At A L`;
- `Begin Joined A B`.

This is the general mechanism behind many removed convenience verbs.

## 7. Giving

There is no standalone Give root.

Exact possession-giving is the coordinated transition:

`Concurrent EndHave giver theme BeginHave recipient theme`

Generic `Transfer` remains distinct because its source/destination roles do not inherently assert possession.

## 8. Names do not create identity

`Name sign referent` establishes or queries a naming relation under the applicable context.

A Name:

- does not create an Entity;
- does not merge two Entities;
- does not overwrite identity;
- does not make two same-named Entities equal.

Changing a name likewise does not replace the named Entity.

## 9. Information copies and physical identity

Equivalent Information content may exist in distinct records/tokens.

If a future world package supports physical duplication, the copy receives its own Entity identity unless the world operation is explicitly identity-preserving.

“Perfect copy” means equality across a declared profile, not Entity identity.

## 10. Fresh-result boundary

Checkpoint 129 closes the previously deferred fresh-identity gap with one explicit Process rather than an implicit consequence of Kind syntax.

`Create` has one current frame:

`Create(result:Binder<Entity>, profile:Proposition) -> EventSpec`

The semantics are:

- **cardinality:** exactly one fresh Entity per Create invocation;
- **freshness:** the result identity has never previously been allocated; Create is not resurrection/reactivation;
- **scope:** the result binder is scoped through the creation profile;
- **profile:** the binder domain and profile describe the result's immediate post-creation state;
- **world capability:** the active world must be able to realize that profile objectively.

The result binder can be used to establish relations that make the new identity usable after creation, for example `At $x Here`, `Control Self $x`, `Have Self $x`, or a naming relation.

Create does not silently add:

- Life;
- consciousness;
- Magic;
- ownership/control;
- a default material/body;
- a random appearance;
- a universal species template.

Those must come from the written profile/binder domain or from an explicit deterministic world generation profile associated with that domain.

If multiple execution-significant realizations remain and the world has no canonical deterministic generation rule, execution is underdetermined rather than randomly choosing one.

`Repeat @@@ Create ...` invokes Create three times and therefore allocates three distinct identities.

## 11. Result

Current identity rules are therefore compact:

- Entity identity equality uses `Equal`;
- existence is the persistent `Exist` state;
- state changes use `Begin` / `End`;
- ordinary `Change` preserves the participant identity;
- Names do not create identity;
- `Create` explicitly allocates exactly one fresh Entity identity under an objective generation profile.
