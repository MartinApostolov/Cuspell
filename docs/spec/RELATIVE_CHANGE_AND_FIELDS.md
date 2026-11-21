# Relative Change, Snapshots, Preservation, and Distributions

_Status: current working specification_

This file defines event-boundary values, relative Change, preservation constraints, tolerance, and nonuniform resource fields.

## 1. Event-boundary snapshots

`BeforeValue` and `AfterValue` retrieve a semantic value at the beginning/end boundary of an Event.

Explicit conceptual form:

`BeforeValue value event`

`AfterValue value event`

Inside one uniquely enclosing EventSpec, the Event argument may be omitted and resolved from event-local context.

Example:

`Change This Density Multiply @@ BeforeValue Density This!`

sets Density to twice its pre-change value.

## 2. Relative change

There is no separate ChangeBy root.

A delta is ordinary target-value arithmetic:

`Change X Mass Add BeforeValue Mass X delta!`

A multiplicative relative change likewise computes the target from BeforeValue.

This keeps Change as one general target/constraint mechanism.

## 3. Constraint-frame Change

Change also has a frame whose target is a Proposition over event-local snapshots.

This supports directional/result constraints such as growth without inventing a new Process root.

The world execution layer must solve the resulting constraints or reject them if unsupported/contradictory.

## 4. Preserve

`Preserve value event` means the selected value is equal across the event boundary.

Example:

`Preserve Volume This Change This Density Multiply @@ BeforeValue Density This!`

Preserve is about the result constraint of one EventSpec.

## 5. Preserve versus Persist

`Preserve` constrains a value through an event transition.

`Persist` actively maintains a state through a temporal interval.

They are not synonyms.

## 6. Multiple simultaneous constraints

An EventSpec may carry several compatible result constraints:

- target Attribute values;
- preserved values;
- geometry/profile requirements;
- identity-preserving ordinary change.

If the joint constraints are inconsistent or not executable under the world model, execution fails rather than silently weakening them.

## 7. Tolerance

There is no standalone ApproxEqual root.

Approximate/tolerance equality is written as explicit bounds over the relevant metric.

For numeric A, B, tolerance T, a symmetric two-sided pattern is:

`Not More Add A Opposite B T And Not More Add B Opposite A T.`

Technical/magical use requires an explicit or objectively registered tolerance.

## 8. Near-boundary semantics

The removed Almost convenience meaning uses boundary Distance plus falsity and contextual Low.

For a gradable PropertyDescriptor P:

`Not P X And Low Distance P X.`

For a non-occurring EventSpec E:

`Not Happen E And Low Distance E.`

The relevant metric/threshold must be registered for objective magical use.

## 9. Requires and SufficientFor

`Requires outcome prerequisite` represents necessity under the relevant rule.

`SufficientFor condition outcome` represents sufficiency.

They are not collapsed into ordinary conversational “because.”

## 10. Method as Information

`Method` is a semantic Information subtype, not a primitive MethodFor relation.

The current general purpose/goal relation is `Purpose`.

An open “how?” question can bind a Method and ask for one whose Purpose is the goal, for example conceptually:

`:«This»:ThisMethod Purpose $«This» Life Self?`

`ThisMethod` is the registered `Method`-typed rune, so the question uses a Cuspell witness instead of an English type. `Life Self` is an illustrative goal Proposition; a different question should supply its own objective goal.

Exact goal spelling depends on the represented EventSpec/content.

## 11. Control

`Control controller target` is a persistent controller-target state relation.

It remains distinct from:

- Have;
- Own;
- Can;
- Use;
- Cause;
- magical Command itself.

A grab-like meaning is represented by concurrent onset of Touch and Control.

## 12. Distribution values

`DistributionOf resource host` constructs/retrieves a Distribution describing a resource/value over a host/domain.

`Density distribution region` can read local density.

`TotalAmount distribution region?` returns an aggregate amount.

Distribution and TotalAmount remain primitive candidates because local Density alone cannot reconstruct general field construction/integration.

## 13. Homogeneous shorthand

For a sufficiently homogeneous Entity, the ordinary Entity frame of Density remains convenient:

`Density This`

A nonuniform resource can use a Distribution instead.

## 14. Redistribution

There is no Redistribute root.

Distribution transfer uses the general `Transfer` Process:

`Transfer distribution source destination`

Optionally:

`Transfer distribution source destination _ targetDistribution`

Here `_` skips the optional amount slot so the following value fills the optional destination-profile slot.

Conservation can be stated separately with `Preserve TotalAmount ...` when needed.

## 15. Field-like world resources

A world model may expose Mana, charge, heat, pressure, light intensity, or other phenomena as spatial Distributions.

Cuspell core does not assume every scalar Attribute is spatially uniform.

## 16. Shape resemblance versus Kind identity

`ShapeLike entity template` expresses geometric resemblance without asserting that the entity is actually an instance of the template Kind.

This distinction remains important for body/tool/camouflage descriptions.

## 17. Result

Relative change is built from general mechanisms:

- BeforeValue / AfterValue;
- Change;
- arithmetic/comparison;
- Preserve;
- explicit constraints;
- DistributionOf / Density / TotalAmount / Transfer.

No special wrapper is required for each English phrase.
