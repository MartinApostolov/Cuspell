# Checkpoint 129 — Fresh Identity Generation / Create Audit

_Status: advanced spellcraft gap audit 1 of 5_

## Trigger

Checkpoint 128's SRD level-3-to-9 pressure pass confirmed that fresh creation is not a niche conjuration problem.

The same requirement appears in effects analogous to:

- Find Familiar;
- Unseen Servant;
- Floating Disk;
- conjured creatures;
- Creation;
- Simulacrum;
- Clone;
- Demiplane;
- some uses of Gate;
- True Resurrection when no already-identifiable body/result Entity exists.

The longstanding identity specification already distinguished:

- creation = allocate a fresh Entity identity;
- transformation = modify an existing identity;
- `Begin Exist X` = reactivate/reinstate an already identifiable X;
- `End Exist X` = end active existence of X.

What was missing was executable language machinery for the first case.

## Question

Can fresh creation be reduced exactly to existing Cuspell, or does Cuspell need one productive fresh-result semantic primitive?

The audit tests:

1. `Begin Exist`;
2. `Change`;
3. Kind predication;
4. Name/New Name allocation;
5. pre-registering dormant Entities;
6. copying an existing Form/Entity;
7. world-only hidden generation metadata;
8. an explicit fresh-result Process.

## Candidate A — Begin Exist

`Begin Exist X` requires an already representable semantic subject X.

Its truth condition is:

> this known identity begins existing.

That is suitable for:

- restoring a previously inactive artifact;
- resurrection/reinstatement where the same identity remains objectively available;
- writing/instantiating an already identified Sign token.

It cannot mean:

> allocate an identity that did not exist in the identity domain before this event.

Countermodel:

- W1 and W2 contain exactly the same already identifiable Entities and the same Exist states;
- in W1 a spell reactivates dormant Entity A;
- in W2 the spell allocates fresh Entity B with an equal visible profile.

Every `Begin Exist A` proposition differs from the fresh-allocation event because A and B have different identity histories.

**Result: Begin Exist is not creation.**

## Candidate B — Change

`Change(theme, attribute, target)` preserves the theme identity.

No sequence of attribute changes can create a new identity unless a fresh identity is already supplied as the theme.

Changing every known property of A to equal B still leaves A equal to A.

**Result: Change is not creation.**

## Candidate C — Kind alone

A Kind classifies a semantic value.

`«LowExtent«MoveLifeThing»» X`

can classify X as a cat, but it does not allocate X.

Many different fresh Entities can belong to the same Kind.

A bare Kind also leaves execution-relevant details such as location, life state, ownership/control, equipment, Form variation, age, and world-specific canonical generation data unresolved.

**Result: Kind predication is not creation.**

A named Kind can, however, be a useful **binder domain** inside Create and can contribute a world-registered canonical generation profile.

## Candidate D — Name/New Name

A Name relates a Sign and referent.

The current identity spec explicitly says Names do not create identity.

Pre-naming an imaginary future result would merely assume the referent the creation operation is supposed to allocate.

Allowing New Names to allocate identities would also turn naming into a semantic/magical macro channel.

**Result: Name is not creation.**

## Candidate E — pre-register every possible future Entity

One workaround would populate the world with dormant identities and reinterpret summoning as `Begin Exist`.

This fails semantically and operationally:

- it says every future construct/familiar/copy already had identity before creation;
- it requires an unbounded catalogue of dormant possible Entities;
- repeated creation becomes reactivation of predetermined identities;
- clone/copy spells lose the distinction between creating a new identity and awakening a stored one.

**Result: reject dormant-identity preallocation.**

## Candidate F — copy an existing Entity/Form

An exemplar can specify part of a generation profile:

`Equal Form $x Form This`

But Form equality is not identity and is not a complete Entity profile.

A perfect copy still needs:

- one new identity;
- an explicit set of copied attributes/relations or a world template;
- decisions about states that should not copy, such as ownership, location, current Damage, transient Magic, or social relations.

Copying therefore presupposes the fresh-allocation operation rather than replacing it.

**Result: exemplar copying may feed Create; it does not reduce Create.**

## Candidate G — hide creation in world generation metadata

World packages already may contain canonical generation profiles.

If package metadata itself silently allocated an Entity whenever a Kind appeared in command context, it would:

- make Kind syntax secretly eventful;
- move a meaning-bearing magical operation outside the rune inventory;
- blur classification and allocation;
- make mana/type reasoning depend on hidden world hooks.

That is the same relocation-not-reduction problem rejected elsewhere in Cuspell.

**Result: world profiles may realize Create but do not replace its language-level meaning.**

## Accepted result — Create

Checkpoint 129 adds:

`Create`

as a one-frame semantic primitive candidate.

Frame:

`Create(result:Binder<Entity>, profile:Proposition) -> EventSpec`

### Freshness

Each invocation allocates exactly **one** Entity identity that has never previously been allocated.

Freshness is stronger than:

`Not Exist X`

because an old inactive Entity can satisfy Not Exist while still having a prior identity/history.

### Binder scope

The result binder is introduced by Create and is available inside the profile:

`Create x:Entity Matter $x And At $x Here!`

The binder gives the spell a handle on the new identity before the identity exists.

The profile must actually mention/constrain that binder. This is invalid:

`Create x:Entity At Self Here!`

because it allocates an otherwise unconstrained result while describing only Self.

### Named Kind binder

A registered Entity Kind may be used as the binder domain:

`Create x:«LowExtent«MoveLifeThing»» Life $x And At $x Here!`

This requests one fresh cat-classified Entity whose immediate profile also includes Life and location Here.

The Old Name in the binder still pays its ordinary frozen mana cost.

The Kind does not itself perform creation; Create does.

### Immediate profile

The Proposition profile states facts that should hold immediately after successful creation.

Useful constraints include:

- Kind membership;
- `Life $x`;
- `At $x Here`;
- `Control Self $x`;
- `Have Self $x`;
- Form/value equalities;
- Parts/structure;
- Name relations;
- Magic state.

Create itself does not automatically add any of these except active existence.

### Existence

A successfully created Entity exists.

Therefore:

`Create x:Entity ...`

does not require the redundant profile conjunct:

`Exist $x`.

This keeps creation distinct from the state-boundary expression `Begin Exist X`.

### Result recovery

The binder is lexical to the Create expression.

If later spells must identify the result, the creation profile should establish an objective recoverable relation, for example:

- a Name;
- `Control Self $x`;
- `Have Self $x`;
- a unique location/relation;
- another world-recognized identifier.

This avoids introducing a magical global variable store merely for created results.

## Determinism / world generation boundary

Create is language semantics; physical generation remains world execution.

The world layer determines:

- whether the requested Kind/profile can be instantiated;
- canonical body/material structure;
- conservation/resource requirements;
- biological viability;
- physical placement;
- RequiredPower;
- conflicts with existing matter/space;
- canonical defaults where the world explicitly defines them.

Create does **not** silently choose a random phenotype/material/body/equipment set.

If the written constraints plus registered world generation policy leave multiple execution-significant realizations with no deterministic choice rule, execution is underdetermined and must fail/decline rather than silently choose.

This is analogous to other Cuspell commands: the language states the objective target; the world engine determines physical realizability.

## Cardinality

One Create invocation creates one fresh identity.

Multiple results are explicit composition:

`Repeat @@@ Create x:Entity Matter $x And At $x Here!`

means three Create invocations and therefore three distinct identities.

This avoids hiding cardinality inside plural Kind wording.

## Why Create is a semantic primitive, not a formal constructor

The binder mechanics are formal, but **fresh allocation** changes world identity structure.

Two worlds can agree on:

- every existing Entity;
- every current Property/Attribute;
- every current Name/Kind relation;
- every possible Begin/End/Change over those known Entities;

while differing on whether a new identity is allocated.

Therefore the freshness condition is not generated by the existing formal system.

Create is tracked as a semantic primitive candidate.

## Parser/validation changes

Checkpoint 129 adds a reusable Binder-slot constraint:

`binds_type`

The Create result slot requires an Entity-typed binder.

This rejects attempts to use Create as a generic fresh Information/Sign/Time/etc. allocator.

The ordinary frame parser still supplies lexical variable scope to later slots.

Semantic validation additionally requires the Create profile to use its fresh result binder.

## Spell-system consequences

### Familiar / servant / summoned creature

The language now has the missing allocation operation.

A complete familiar spell still needs an objective generation profile plus any intended relations:

- creature Kind;
- Life;
- location;
- Control/relationship;
- duration/ending conditions if temporary.

### Simulacrum / clone

Create handles new identity.

A copy spell must additionally state or invoke world generation mappings for which traits/profile are copied.

Equal Form alone does not mean "copy the entire person."

### Demiplane / created structures

Create can allocate a fresh Entity structure if the world's ontology represents that structure as an Entity.

If the effect instead creates a new Region/topological space value with no Entity identity, that is a separate future result-type question; checkpoint 129 deliberately keeps Create's first frame Entity-only.

### True Resurrection

If the original person/entity identity remains objectively available, `Begin Life` / `Begin Exist` may be the right semantics.

If the magic instead produces a genuinely new Entity that merely copies a dead person's profile, that is Create and is **not** identity-preserving resurrection.

The spell/world metaphysics must decide which claim is true.

## Regression additions

Checkpoint 129 adds seven tests:

1. fresh Entity with objective Matter/location/control profile;
2. named-Kind result binder;
3. non-Entity result binder rejection;
4. profile must use the fresh result;
5. Create differs from BeginExist reactivation;
6. result relations can be established in the profile;
7. Repeat can invoke creation multiple times.

The parser/data validator also now validate typed Binder-slot constraints.

Suite total becomes:

- **689 -> 696 tests**.

## Inventory effect

Checkpoint 129 adds:

- 1 registered base entry: `Create`;
- 1 semantic primitive candidate;
- 1 semantic frame.

New totals:

- **214 registered base entries**;
- **133 semantic primitive candidates**;
- **55 formal constructors**;
- **268 semantic frames**;
- **49 multi-frame entries**;
- **204 Old Names**;
- **197 core world concepts**.

## Decision

**ADD Create as explicit one-Entity fresh identity allocation.**

Do not reduce it to:

- Begin Exist;
- Change;
- Kind classification;
- naming;
- hidden world metadata;
- dormant preallocated identities.

The current canonical semantic shape is:

`Create result-binder objective-profile`.

World generation rules realize the profile; they do not replace the Create meaning.

## Next work

Proceed to advanced spellcraft gap 2:

**bounded acquisition of previously unknown Information / divination.**

The key question is whether current Sense/Question/Evidence/Know machinery can be composed into a safe objective information-access operation, or whether magic needs one explicit reusable acquisition semantic that states source/domain/scope without granting omniscience.
