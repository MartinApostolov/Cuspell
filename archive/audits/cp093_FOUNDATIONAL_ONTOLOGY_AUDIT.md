# Foundational Ontology and Classification Second-Pass Audit

_Status: checkpoint 93 — family-level reduction experiment complete; no net-safe reduction found_

## Scope

This audit tests the fourteen-root foundational ontology/classification family:

- `Group`
- `Matter`
- `Path`
- `Region`
- `Rule`
- `Sign`
- `Thing`
- `Unit`
- `Exist`
- `Female`
- `Life`
- `Magic`
- `Whole`
- `Member`

The family mixes language-level ontology anchors, world-classification predicates,
semantic-domain nouns, and one generic membership relation. Because many later
roots depend on these distinctions, this pass treats a move into metadata, a
metalanguage type, or a one-value world classifier as a relocation rather than a
reduction unless the old distinction is actually generated from a smaller basis.

## Reduction rule

A candidate deletion must preserve the same truth conditions and typing without
silently making semantic type names or world-model labels into free meaning-bearing
syntax.

In particular:

- a semantic type such as `Entity`, `Region`, `Path`, `Sign`, or `Unit`
  is part of the implementation/type metalanguage unless a written Cuspell
  expression deliberately denotes it;
- moving `Female` or `Matter` into a world table under one new atomic classifier
  does not reduce the semantic alphabet;
- rebuilding draft Old Names is allowed and does not protect a root;
- a structural definition is acceptable only if it is extensionally exact,
  including empty, historical, inactive, and edge cases.

## Experiment A — Thing versus the Entity metalanguage type

`Thing` is the general language-level Kind for entities.

The type checker also has the semantic type `Entity`, but treating that type name
as a free substitute for the written root would move meaning into zero-mana
grammar. The distinction matters because type annotations constrain parser/runtime
values, while `Thing` is a first-class Kind that can participate in ordinary Kind
predication and lexical construction.

`Exist` is not a replacement either. An identifiable Entity can fail `Exist`
while still remaining the same ontology identity, so:

`Thing(x)` does not mean `Exist(x)`.

**Result: retain Thing.**

## Experiment B — Matter from Thing, Phase, Mass, or other physical descriptors

`Matter` marks the broad physical material/substance domain. It is not exactly:

- `Thing` plus a positive Mass;
- a subject with a Phase value;
- a subject with spatial Extent;
- a subject participating in Part/Whole structure.

Those criteria either admit non-matter entities in some world models or exclude
material entities whose current model does not expose the chosen descriptor.
Conversely, changing phase does not change material identity.

A world package supplies the exact boundary, but replacing the root with a
`MatterClassifier` world atom would preserve the same irreducible distinction
under another name.

**Result: retain Matter.**

## Experiment C — Group from Member or Collection

A semantic `Collection<Entity>` is not a Group Entity.

Collections are semantic values without world identity. A Group is a world/social
Entity that can persist through membership changes and can have history, ownership,
location, obligations, or other Entity relations.

Defining:

`Group(g) = Some x Member x g`

is not exact because an empty recognized group can still be a Group, and the
definition would make classification depend on current non-emptiness.

Likewise `Member` cannot be removed in favor of `Part`, `In`, or `Have`:

- Part is mereological structure;
- In is spatial containment;
- Have is possession/state;
- Member is set/group membership.

**Result: retain Group and Member.**

## Experiment D — Path and Region from semantic types

The implementation already distinguishes semantic value types `Path` and
`Region`. That typed distinction is required by Move, Through, In, geometry,
Region constructors, and spatial references.

The written Kind roots are not thereby free. Replacing a meaning-bearing Path or
Region noun with an implementation type token would violate the rule that
meaning-bearing distinctions cost runes. A generic written `IsType(x,T)` would
also fail the count test if `Path` and `Region` remain irreducible semantic type
labels supplied as its arguments.

The two domains are not mutually derivable:

- a Region is an unordered spatial subset with extent;
- a Path is an ordered trajectory.

**Result: retain Path and Region.**

## Experiment E — Sign from Meaning, and Rule from Information

`Sign` is not exactly "something that currently has a Meaning relation."

A representation/token can be an unknown, untranslated, ambiguous, damaged, or
currently uninterpreted Sign. Meaning relates a Sign to Information in a context;
it does not define the Sign ontology itself.

`Rule` is a recognized class of Information expressing conditional, normative, or
general structure. Plain Information is broader. Replacing Rule with an
`InformationKind = Rule` value would only move the classification atom.

The existing information type system therefore supplies useful surrounding
structure but no smaller exact definition for either root.

**Result: retain Sign and Rule.**

## Experiment F — Unit from the Unit semantic type and typed unit registry

Specific measurement units are already registered typed Old Names, and the runtime
has a semantic `Unit` value type plus unit metadata.

That does not make the general written `Unit` Kind semantically empty. It denotes
the class/concept of registered scale constructors, while the implementation type is
a typing discipline. Rewriting `«LengthUnit»`, `«MassUnit»`, and the other draft
historical names to omit the word Unit would only alter etymology; it would not
derive the generic Unit concept from another root.

No second meaning-bearing unit-class token is introduced simply to hide this root.

**Result: retain Unit.**

## Experiment G — Exist, Life, Magic, and Whole as one generic state family

These four are all persistent state predicates, but their truth conditions are
independent:

- `Exist` means active ontological participation;
- `Life` means biological living state;
- `Magic` means active magical state/effect;
- `Whole` means integrity/completeness relative to a structural profile.

Counterexamples keep every pair apart:

- a corpse can Exist and Not Life;
- a living damaged organism can be Life and Not Whole;
- a mundane object can Exist and Not Magic;
- an active magical effect can be Magic without being Life;
- an identifiable inactive entity can be Not Exist while retaining historical Kind
  identity.

A generic `State(subject, state-kind)` wrapper with Exist/Life/Magic/Whole values
would add a wrapper while preserving one atom per old root.

Their shared transition abstraction already exists through `Begin` and `End`.

**Result: retain Exist, Life, Magic, and Whole.**

## Experiment H — Whole from Part or Damage

`Whole` is not the converse of `Part`. It states that the required parts and
relations of a recognized structural profile are sufficiently present/intact.

Nor is it exactly `Not HighDamage`. Damage is a descriptor/degree; structural
profiles can define integrity using required topology, parts, and relations that are
not reducible to one damage threshold.

This distinction is already used by the minimized severing expression
`Cause agent End Whole target`.

**Result: retain Whole.**

## Experiment I — Female as world ontology rather than a core Property

`Female` is the strongest apparent world-specific relocation candidate in this
family because its exact classifier belongs to world ontology.

However, merely replacing the root with one world-level `female` classifier is not
semantic reduction. The classification distinction is still atomic. The current
entry is also a persistent Property, not a stable natural-Kind identity, so changing
it into a Kind-valued Old Name would alter its typing and Begin/End behavior.

If later ontology work discovers a genuinely smaller biological feature basis that
compositionally generates this classification together with other classifications,
the root can be revisited. That basis does not exist today.

**Result: retain Female.**

## Old Name check

Draft Old Names do not protect any root in this family.

Several are heavily reused in historical vocabulary, especially `Thing`, `Matter`,
`Life`, `Group`, and `Unit`. Their spellings could be rebuilt if a root were
removed.

That dependency does not change the audit result. No candidate deletion survives on
its own semantics, so no Old Name rewrite is necessary at checkpoint 93.

## Count result

No root is removed and no replacement ontology/state/type wrapper is added.

Current inventory remains:

- **206 registered base entries**;
- **126 semantic primitive candidates**;
- **54 formal constructors**;
- **16 reference forms**;
- **10 domain values**;
- **0 unresolved candidates**;
- **0 derived candidates**.

The foundational ontology/classification family remains **14 semantic primitive
candidates**.

## Design conclusion

The apparent compression opportunities in this family mostly confuse three layers:

1. implementation semantic types;
2. world-model classifiers;
3. written language-level meanings.

Using a type name or a one-value world classifier to replace a root does not remove
the distinction; it only hides where the distinction lives. The surviving roots
also separate important ontology axes such as identity/existence, life/integrity,
collections/groups, representation/information, and trajectories/regions.

Checkpoint 93 therefore makes **no inventory change**.

The next second-pass target should be the compact
**change / causation / transfer / control** family:
`Change`, `Cause`, `Give`, `Transfer`, and `Control`.
