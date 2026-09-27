# Structure, Parts, Joining, and Wholeness

_Status: working specification v0.1_

This specification formalizes structural Part relations, composites, joining/separating, and integrity.

## 1. Part

`Part(part, whole)`

is the registered structural/mereological relation.

Meaning:

> part is included as a constituent of whole under the applicable structural decomposition.

This is not numerical Ratio.

## 2. Part transitivity

The broad Part relation is transitive where the structural domain permits:

if A Part B and B Part C, A can be Part C.

Some applications need the immediate relation rather than transitive closure.

Add candidate:

`DirectPart(A,B)`

meaning A is an immediate constituent of B in the selected structural model.

## 3. Part versus spatial containment

Part is not In.

An organ can be Part of a body and also spatially In it, but these are separate relations.

A coin can be In a box without being Part of the box.

## 4. Part versus membership

Part is not generic set membership.

Group/Collection membership uses Member/Members.

A person can be Member of a team without being a structural Part in the mereological sense unless the ontology explicitly models that social structure.

## 5. Joined

Introduce a persistent structural Relation:

`Joined(A,B)`

meaning A and B currently participate in a registered physical/structural join relation.

The relation can carry join-type metadata where needed:

- attached;
- fused;
- hinged;
- linked;
- bonded;
- etc.

A generic Joined predicate may abstract over these for ordinary use.

## 6. Join

`Join(A,B, join-profile?) -> EventSpec`

normalizes conceptually to:

`Begin(Joined(A,B))`

plus any explicit structural transformation required by the join profile.

Join therefore does not need Opposite semantics.

## 7. Separate

`Separate(A,B) -> EventSpec`

normalizes conceptually to:

`End(Joined(A,B))`

when the specified join can be ended.

This is more precise than declaring `OppositeJoin` universally.

The earlier candidate OppositeJoin=Separate is therefore not adopted as a general rule.

## 8. Join reversibility

Some specific join types may have reversible physical Processes.

Others may not.

The semantic boundary pair Join/Separate can still exist even when undoing the join requires major reconstruction/Damage.

RequiredPower/capability handles physical difficulty.

## 9. Composite identity

Joining Entities does not automatically create a new Entity identity.

There are at least two outcomes:

1. existing Entities become Joined while retaining their identities;
2. the Event additionally creates/recognizes a composite Entity with those participants as Parts.

A Process frame must say which result occurs.

## 10. Composite result binder

A Join variant that creates a composite can declare:

`:result Collection/Entity`

according to its guaranteed output.

The new composite identity is distinct from each Part identity.

## 11. Whole

`Whole(x)`

means x satisfies the required Parts and structural relations of its selected integrity/profile model.

Whole is truth-valued, not the converse of Part.

## 12. Required versus optional Parts

A structural Kind/profile can declare:

- required Parts;
- optional Parts;
- cardinality constraints;
- required Part relations;
- tolerated Damage/missing material.

This determines Whole objectively.

A sword missing its pommel may or may not remain Whole depending on the registered Sword profile.

## 13. Damage through structural loss

Removing/severing a required Part can entail:

- Damage;
- NotWhole;
- changed function;
- possible Kind changes if identity-essential structure is lost.

These consequences are profile rules, not arbitrary GM judgment.

## 14. Split

Physical division is not merely Separate if one Entity becomes several identities.

A candidate `Split` Process can:

- change/destroy the original composite identity as defined;
- produce multiple fresh/result Entities;
- preserve material continuity/Parts.

Cut may often cause Split but is not identical to it.

## 15. Merge/fusion

Likewise a deep fusion that creates one new material identity may be stronger than ordinary Join.

A future Merge Process can distinguish:

- structural attachment;
- identity-forming fusion.

## 16. Material composition

"Made of" should not be hidden inside generic Of.

Material composition can use explicit Parts/material fractions.

Possible relation:

`MaterialPart(material-kind/portion, entity)`

or composition Attribute returning weighted Material Kinds.

This will be useful for alloys/mixtures and can reuse Ratio.

## 17. Collections and physical structures

A Collection of Parts is Information/semantic grouping.

A physical composite requires actual structural Relations.

Therefore merely writing a collection `{A,B,C}` does not physically Join them.

## 18. Result

Cuspell now distinguishes:

- Part;
- Member;
- In;
- Joined;
- Whole;
- Join/Separate;
- Split/Merge.

This avoids using one English word such as "with" or "of" to carry unrelated structural meanings.
