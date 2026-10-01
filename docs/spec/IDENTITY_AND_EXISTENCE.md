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

It does **not** by itself solve the problem of allocating a completely fresh Entity identity from only a vague Kind label.

Fresh identity generation is a world/generation-profile capability problem. The minimized base lexicon currently has no standalone Create root.

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

## 10. Result/fresh-identity boundary

The current parser/type system has generic semantic machinery for values, binders, Collections, and EventSpecs, but the base language does not currently expose a universal “create fresh object of Kind K” root.

Any future fresh-result Process must specify:

- result type/cardinality;
- freshness/identity guarantees;
- generation profile;
- world capability requirements.

That work belongs to world execution/generation semantics, not an implicit grammatical shortcut.

## 11. Result

Current identity rules are therefore compact:

- Entity identity equality uses `Equal`;
- existence is the persistent `Exist` state;
- state changes use `Begin` / `End`;
- ordinary `Change` preserves the participant identity;
- Names do not create identity;
- fresh Entity allocation is explicit future world machinery rather than a hidden consequence of Kind syntax.
