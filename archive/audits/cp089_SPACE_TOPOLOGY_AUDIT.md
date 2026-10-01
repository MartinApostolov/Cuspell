# Space, Topology, and Geometry Second-Pass Audit

_Status: checkpoint 89 — family-level audit complete; Inside and Outside reduce compositionally_

## Scope

This audit tests the 16-root space/topology/geometry family:

- `At`
- `Center`
- `Edge`
- `In`
- `Inside`
- `Joined`
- `Offset`
- `Outside`
- `Overlap`
- `Part`
- `ShapeLike`
- `Sides`
- `Surface`
- `Through`
- `Touch`
- `Toward`

The main goal is to see whether a smaller topological basis can preserve strict
containment and boundary behavior without returning to the incorrect first-pass
simplification `Inside = In` and `Outside = Not In`.

## Topological basis

The current geometry already distinguishes:

- `In(A,R)` — A's spatial extent is a subset of R, allowing boundary contact;
- `Touch(X,Y)` — boundary contact;
- `Overlap(X,Y)` — nontrivial interior/shared extent;
- `Extent(A)` — the occupied Region of A.

The missing piece was not a new root. It was typed Region support on the existing
topological relations.

Checkpoint 89 therefore adds:

- `Touch(Region,Region) -> Proposition`, meaning the two Region boundaries contact;
- `Overlap(Region,Region) -> Proposition`, meaning their interiors share nontrivial
  spatial extent.

These are direct type-generalizations of the existing contact/overlap relations, not
new semantic tags.

## Reduction 1 — Inside

The former primitive meant strict interior containment: A is contained by R and does
not contact R's boundary.

That is exactly:

`And {In A R,Not Touch Extent A R}`

The two parts preserve the distinction that caused the earlier restoration:

- `In A R` keeps subset containment and allows boundary contact;
- `Not Touch Extent A R` removes the boundary-contact cases.

So `Inside` is **not** being collapsed into plain `In`; it is being reconstructed
from the exact topological basis that was previously missing.

**Result: remove Inside.**

## Reduction 2 — Outside

The former primitive meant that A has no spatial extent in the interior of R.
Boundary-only contact is allowed.

With Region overlap defined as nontrivial interior/shared extent, that is exactly:

`Not Overlap Extent A R`

This also preserves the old distinction from `Not In`:

- partial overlap fails `In`, so `Not In` is true;
- the same partial overlap still satisfies `Overlap Extent A R`, so the composed
  Outside proposition is false;
- pure boundary contact has no interior overlap, so the composed Outside proposition
  is true.

**Result: remove Outside.**

## Why this does not repeat the first-pass mistake

The earlier failed reduction tried:

- `Inside -> In`;
- `Outside -> Not In`.

Those lose strict boundary semantics.

Checkpoint 89 instead keeps the stricter semantics explicitly:

- strict Inside = containment **and no boundary contact**;
- Outside = **no interior overlap**.

The new composition therefore preserves the exact cases that disproved the original
simplification.

## Remaining family audit

### At

`At(Entity,Location)` is anchor-position coincidence. It is not the same as
containment in a Region and cannot be derived from `In`, `Center`, or `Offset`
without changing the declared anchor semantics.

**Retain.**

### Center

`Center(Region) -> Location` uses the Region's registered unique center definition,
provisionally a centroid where defined.

It is not generally the same as an arbitrary minimum-distance point, midpoint of two
selected points, or average of axis extrema. Non-convex and irregular Regions make
those substitutions non-equivalent.

**Retain.**

### Edge

`Edge(Entity/Region) -> Collection<Region>` returns boundary features.

It does not collapse into `Surface`: Surface returns the complete boundary surface
Region of an Entity, while Edge returns a collection of lower-dimensional or
segmented boundary features.

A generic Boundary root would need an additional dimensional/feature-selection
distinction to recover both meanings, so 2 -> 1 is not yet established.

**Retain.**

### Joined

Structural joining is not mere contact. Two things can Touch without being Joined,
and a registered join can encode attachment/bond/hinge/fusion structure beyond
topological contact.

**Retain.**

### Offset

`Offset(origin,direction,distance) -> Location` is a constructive location
operation. Neither `At`, `Distance`, nor `Toward` alone yields the resulting
Location.

**Retain.**

### Overlap

Overlap is now more reusable, not less: the same root covers Entity, Region, Event,
and TimeInterval domains with typed frames.

It is the exact basis used to eliminate Outside.

**Retain.**

### Part

Structural/mereological Part is independent of spatial containment. A coin may be In
a box without being Part of it; a constituent Part relation carries structural
decomposition rather than location alone.

**Retain.**

### ShapeLike

`ShapeLike(entity,Kind)` compares geometry to a template/profile without asserting
Kind identity. `Form` returns a GeometryProfile but there is no current exact
profile-comparison composition that reconstructs ShapeLike and its tolerance/model
semantics.

**Retain.**

### Sides

`Sides(entity,frame?) -> Collection<Region>` partitions/selects oriented surface
regions relative to a CoordinateFrame. It is not the same as the whole Surface or
the set of Edges.

A generic Boundary selector would still need a distinct side-partition operation.

**Retain.**

### Surface

`Surface(entity) -> Region` returns the complete boundary surface. Edge gives
features and Sides gives an oriented partition; neither is equivalent.

**Retain.**

### Through

`Through(Path,Region)` constrains path traversal/intersection, and the EventSpec
frame constrains an event to realize through that Region.

Plain Region overlap cannot replace the EventSpec-transforming frame, and a Path is
not currently represented as an occupied Region whose overlap proposition would
carry the same traversal semantics.

**Retain.**

### Touch

Touch is now the shared boundary-contact basis for both Entity contact state and
Region topology. It is used directly in the Inside reduction.

**Retain.**

### Toward

`Toward(reference) -> Direction` constructs a direction. Its inverse
`AwayFrom` has already been removed as `Opposite Toward reference`.

No existing remaining root constructs the toward-direction value itself.

**Retain.**

## Count result

Two roots are removed and no new root is added.

The space/topology/geometry family changes:

- **16 -> 14 semantic primitive candidates**.

Whole-core inventory changes:

- **208 -> 206 registered base entries**;
- **128 -> 126 semantic primitive candidates**;
- **54 formal constructors** unchanged;
- **16 reference forms** unchanged;
- **10 domain values** unchanged;
- **0 unresolved candidates**;
- **0 derived candidates**.

## Design conclusion

The earlier decision to restore Inside and Outside was correct at the time: `In`
and `Not In` alone did not preserve their boundary semantics.

The second pass succeeds because the language now uses a genuinely smaller
topological basis:

- subset containment via `In`;
- boundary contact via typed `Touch`;
- interior/shared-extent intersection via typed `Overlap`;
- entity-to-Region conversion via `Extent`.

That basis removes two lexical primitives while preserving the exact distinctions
that originally required them.

The next second-pass family should be **communication, information, epistemics, and
discourse**.
