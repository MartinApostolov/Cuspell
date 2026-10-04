# Checkpoint 121 — Rotate Exact-Reduction Audit

_Status: post-civilization reduction/redundancy audit, target 4_

## Purpose

Checkpoint 114 added:

`Rotate(theme,pivot,axis,turns) -> EventSpec`

after the craft/transport vocabulary audit exposed a gap for rigid orientation change.

Checkpoint 121 re-tests that addition against the **current** geometry system:

- `Move`;
- `At`;
- `Offset`;
- CoordinateFrame / Direction references;
- `Form`;
- `Change`;
- Part relations and separately constrained motion.

The question is whether rigid rotation can now be expressed exactly without a productive Rotate meaning.

## Current semantics

`Rotate(theme,pivot,axis,turns)`

takes:

- theme: Entity;
- pivot: Location;
- axis: Direction;
- turns: Quantity:Number;

and returns EventSpec.

The axis is the oriented line through pivot in the supplied Direction. The signed turns value is measured in full revolutions.

The operation is rigid:

- intrinsic Form is preserved;
- Entity pose/orientation changes;
- if pivot is off the Entity anchor, the anchor may move along the corresponding circular arc.

## Candidate 1 — Move

`Move(theme,goal?,source?,path?)`

constrains translational relocation.

That is not rigid orientation change.

### Rotation without translation

A rigid object can rotate around an axis through its anchor.

Then:

- anchor location may stay fixed;
- intrinsic Form stays fixed;
- orientation changes.

A Move description based only on anchor position/path has no changed location to state.

### Translation without rotation

An Entity can Move along a path while preserving orientation.

So Move does not entail Rotate either.

The two operations therefore have independent truth conditions.

**Result: Move is not an exact reduction.**

## Candidate 2 — At boundary changes

`At(Entity,Location)` records persistent anchor location.

Ending one At state and beginning another can express discontinuous relocation, but still says nothing about orientation.

A same-location rotation would leave the relevant At proposition unchanged.

**Result: At cannot encode rotation.**

## Candidate 3 — Offset

`Offset(origin,direction,distance) -> Location`

constructs a translated Location.

It is useful for:

- destinations;
- axes-relative positions;
- geometric point construction.

But it does not represent:

- an Entity pose;
- an orientation state;
- a rigid transform;
- an angular relation.

Multiple Offsets could generate points lying on a rotated object, but the language would still need to state that all such points belong to the same rigid transform.

**Result: Offset is a location constructor, not rotation.**

## Candidate 4 — CoordinateFrame / Direction

CoordinateFrames and Directions provide reference geometry.

They can tell the language what an axis means.

They do not currently provide a functional Entity attribute such as:

`Orientation(Entity) -> OrientationProfile`

or:

`Pose(Entity) -> Transform`.

Therefore there is no existing expression like:

`Change entity Orientation ...`

that could replace Rotate.

Adding a new Orientation/Pose Attribute plus transformation algebra would be a **larger new semantic subsystem**, not a reduction of the existing root.

It might be useful in a future advanced geometry model, but current evidence does not justify introducing it merely to eliminate one clear Process.

**Result: reference frames do not reconstruct the operation.**

## Candidate 5 — Change Form

`Form(Entity) -> GeometryProfile`

describes intrinsic geometry/shape.

A rigid rotation does not reshape the object.

Using:

`Change entity Form target`

for a turn would therefore change the wrong semantic dimension.

This distinction is especially obvious for:

- a rigid wheel spinning on an axle;
- a door rotating on hinges;
- a lever turning about a pivot;
- a rigid sculpture being reoriented in space.

The GeometryProfile can stay identical throughout.

**Result: Change Form is not exact.**

## Candidate 6 — Move all Parts

The strongest compositional proposal is to decompose an Entity into Parts and move every Part along the path induced by the desired rotation.

This does not produce a smaller semantic basis.

To define the intended event exactly, the construction must ensure that every material point/Part:

1. uses the same pivot;
2. uses the same oriented axis;
3. uses the same signed turn amount;
4. follows the appropriate circular trajectory for its radius from the axis;
5. preserves all pairwise rigid relative geometry;
6. remains part of the same Entity;
7. completes the transform coherently.

Those constraints are precisely the mathematical content of a rigid rotation transform.

Writing or hiding them individually would recreate Rotate as an implicit higher-order operator while making ordinary casting much longer and more error-prone.

The current Part relation also does not enumerate every material point or supply a general rigid-body constraint solver as language semantics.

**Result: per-Part motion is not a legitimate exact reduction.**

## Candidate 7 — world physics only

A world model may know that a wheel attached to an axle tends to rotate when pushed.

That does not let Cuspell state the requested geometric result:

> rotate this Entity around this axis by this amount.

Relying on physics to guess the intended turn from a force/motion description would make semantics world-dependent and indirect.

The language should state the transform; the world decides whether and how it can execute.

**Result: physics can realize Rotate, not replace its meaning.**

## Why no Angle root is required

Rotate uses signed Quantity:Number full turns.

Therefore:

- 1 = one complete revolution;
- 1/2 = half revolution;
- sign chooses direction under the resolved world/frame convention.

The operation does not require a separate primitive Angle unit family merely to remain objective.

A world may add conventional angle Units/names later.

## Old Name dependency check

Checkpoint 114 created the Wheel Old Name:

`«RotatePartThing»`

and later vocabulary such as Cart depends on Wheel.

These historical dependencies are not a reason to preserve Rotate by themselves; design-stage Old Names could be rewritten if an exact reduction existed.

No exact replacement exists, so the current historical chain remains valid.

## Regression change

Checkpoint 121 adds one regression that parses both:

`Rotate This Here Up @!`

and:

`Move This Here!`

as EventSpecs and confirms they remain distinct canonical events.

The suite therefore rises from **655 to 656 tests**.

## Result

**KEEP AS IRREDUCIBLE SEMANTIC BASIS: `Rotate`.**

No base entry, frame, type, Old Name, New Name, or world concept is added or removed.

Inventory remains:

- **212 registered base entries**;
- **131 semantic primitive candidates**;
- **55 formal constructors**;
- **265 semantic frames**;
- **48 multi-frame entries**;
- **204 Old Names**;
- **197 core world concepts**.

Executable suite:

- **656 tests**.

## Productive-root audit status

The post-civilization re-check of productive meanings added/restored in checkpoints 107–117 is now complete:

- Authority — keep;
- Health — keep;
- Pain — keep;
- Ill — keep;
- Male — keep;
- Female — keep;
- Rotate — keep.

No productive meaning from that set reduced away under exact semantics.

## Next structural target

Audit checkpoint 116's typed world-Kind:

`classifies_types`

Check whether the mechanism is:

- the minimal general solution;
- constrained enough;
- duplicated by another classifier/type mechanism;
- correctly applied to all current world concepts.

Then audit parameterized expression Old Names from checkpoint 110.
