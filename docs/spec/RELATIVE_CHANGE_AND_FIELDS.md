# Relative Change, Snapshots, Preservation, and Distributed Quantities

_Status: working specification v0.1_

This specification was forced by the magic-heavy corpus test. It handles changes defined relative to a prior state, invariants during transformation, and spatially varying resource/material quantities.

## 1. Why pre-state references are needed

Many useful instructions are relative rather than absolute:

- make it twice as dense;
- move it three units farther away;
- keep the same size while changing material;
- restore the previous color;
- increase temperature by five units.

Scalar deltas are written compositionally with Change + Add + BeforeValue, so the language needs a general way to refer to values at event boundaries.

## 2. Event boundary snapshots

For an EventSpec/Event E and value expression V, define conceptual snapshot functions:

BeforeValue(V, E) -> Value.

AfterValue(V, E) -> Value.

For an Attribute A of subject X:

BeforeValue(A(X), E)

means the value immediately before E's state transition boundary.

AfterValue(A(X), E)

means the value immediately after E.

These are functional semantic constructions.

For an EventSpec before execution, BeforeValue is resolved from the activation world state; AfterValue participates in result constraints.

## Event-local snapshot shorthand

When BeforeValue or AfterValue appears inside the result/value constraints of one uniquely enclosing EventSpec, the Event argument may be omitted.

Thus:

`BeforeValue(Density(This))`

inside the target value of a Change Event means:

`BeforeValue(Density(This), nearest-enclosing-EventSpec)`.

The parser establishes that enclosing EventSpec context as soon as it recognizes the Process head and selected frame.

This shorthand is valid only when exactly one enclosing event boundary is available.

Outside such a context, or when more than one candidate event boundary could apply, the Event argument must be explicit.

This allows compact flat expressions such as:

`Change|This|Density|Multiply|@@|BeforeValue|Density|This`

without inventing a magical meaning for "old" or guessing which previous event is meant.

## 3. Relative target values

A Change target may be computed from a snapshot.

Example meaning:

new density = 2 × old density

normalizes conceptually to:

Change(X, Density, Multiply(@@, BeforeValue(Density(X), E))).

The surface language may later provide a compact relative-change compound.

## 4. Preserve

Introduce a result/invariant constraint:

Preserve(value-expression, EventSpec) -> constrained EventSpec.

Meaning:

the selected value after the Event equals its value before the Event unless explicitly permitted tolerance is supplied.

Example:

Preserve(Volume(X), Change(X, Density, new-density))

means Density changes while Volume remains equal across the event boundary.

Preserve does not freeze natural future evolution after the Event. For that, use Persist.

## 5. Preserve versus Persist

Preserve is an event-boundary constraint.

Persist is active maintenance through a temporal interval.

Thus:

- Preserve(Color(X), Transform(...)) means the transformation leaves Color unchanged.
- Persist(Equal(Color(X),red), duration) actively prevents later Color drift for the duration.

They solve different problems.

## 6. Multiple simultaneous target constraints

An EventSpec can carry a result ConstraintSet containing several Attribute goals and Preserves.

A Transform can therefore request:

- target Form profile;
- target Density;
- preserved Volume;
- preserved Color;
- preserved identity.

The execution engine solves the joint constraints or fails if they are contradictory/unsupported.

## 7. Approximate equality

Introduce:

ApproxEqual(A, B, tolerance) -> Proposition.

A and B must be comparable under the same dimension/value metric.

Tolerance may be:

- absolute Quantity;
- relative Ratio;
- registered contextual standard in ordinary discourse.

Magical/technical use requires an explicit or registered tolerance.

This handles "about ten times as dense" without silently rounding.

## 8. Almost

Introduce ordinary-language semantic molecule:

Almost(Predicate, subject, context) -> Proposition

only when the Predicate declares a graded boundary/metric.

Almost(P,x) means:

- P(x) is currently false;
- x lies within the contextual/explicit near-boundary region on the non-P side.

Examples may include:

- almost hungry;
- almost full;
- almost at the threshold;
- almost opaque.

Almost is invalid for predicates with no declared graded boundary unless a specific approximation model is supplied.

Magical use requires the boundary/tolerance to be explicit.

## 9. Requires / prerequisite

Introduce:

Requires(outcome/state/EventSpec, prerequisite) -> Proposition/constraint.

Meaning:

the outcome/state cannot validly occur under the relevant rule unless prerequisite holds/occurs.

This encodes necessity rather than ordinary one-way sufficient condition.

Conceptually:

Requires(B,A) corresponds to B -> A.

A separate SufficientFor(A,B) can correspond to A -> B when useful.

This distinguishes:

- "if A, then B";
- "B requires A";
- "A is enough for B."

## 10. Method

A Method is an Information/Plan structure specifying how an agent/system may realize a goal/EventSpec.

Working relation:

MethodFor(method, goal/EventSpec) -> Proposition.

Open questions may bind a Method:

?[m:Method] MethodFor($m, Complete(Quest)).

This gives "How do I do X?" a concrete semantic answer type.

## 11. Control

Introduce state Relation:

Control(controller, target/process, control-domain?) -> Proposition[state-predicate].

Control means the controller can intentionally constrain/manipulate the relevant target state/process under the declared domain.

It is distinct from:

- Have: possession/control relation in social/resource sense;
- Use: an intentional Event employing an instrument;
- Command: magical instruction to reality;
- Can: general capability.

A person may Control a mana construct without owning it or using it as an instrument.

## 12. Resource amount versus spatial distribution

Some world resources behave as both a total amount and a spatial distribution.

Introduce abstract structured value:

Distribution<Resource, QuantityDimension>.

A Distribution maps locations/subregions to local amount-density values under the world model.

Useful world hooks include:

DistributionOf(resource-kind, host/region) -> Distribution.

Density(distribution, region) -> Quantity<DensityDimension>.

TotalAmount(distribution, region) -> Quantity<ResourceAmount>.

The exact integration/continuum mathematics belongs to the world model.

## 13. Homogeneous shorthand

For approximately homogeneous material/resource portions, the simpler scalar Density(Entity/portion) remains valid.

A nonuniform object can instead be partitioned into Regions/Parts and assign different local densities, or use a Distribution directly.

This lets simple spells remain simple while supporting advanced field manipulation.

## 14. Redistribution

There is no separate `Redistribute` Process in the minimized core. Redistribution is the Distribution-valued use of the general `Transfer` Process:

- `Transfer distribution source-region target-region`;
- `Transfer distribution source-region target-region :profile target-profile`.

The optional named `:profile` role constrains the destination Distribution profile. The world model may normalize the transfer to detailed Move/Change operations.

Useful constraint:

`Preserve TotalAmount distribution whole-region Transfer distribution source-region target-region`.

This captures moving mana from a construct center toward its boundary without creating/destroying the resource.

## 15. Field-like resources

A world can register resources/phenomena such as:

- Mana;
- charge density;
- temperature fields;
- pressure fields;
- light intensity fields;

as spatial Distributions when needed.

Cuspell core does not assume every scalar Attribute is uniform.

## 16. Shape-like versus Kind identity

The corpus reinforces a useful derived Relation:

SimilarFormTo(A,B, tolerance/profile) -> Proposition.

or:

ShapeLike(A, Kind/template) -> Proposition.

This compares Form/GeometryProfile without asserting InstanceOf.

A mana construct can therefore be hand-shaped while not being a biological Hand.

## 17. Corpus consequence

These additions are not specific to one story.

Snapshot values and Preserve are broadly useful magical-language tools, while Distribution and Control provide a clean way to describe fields, telekinesis-like control, shaped energy, fluids, and similar advanced effects without weakening the existing type system.
