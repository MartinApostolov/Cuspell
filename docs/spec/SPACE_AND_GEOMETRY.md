# Space, Geometry, and Motion

_Status: working specification v0.1_

This specification formalizes locations, regions, coordinate frames, geometry, spatial relations, and motion.

## Spatial values

Cuspell distinguishes:

- **Location** — a position/reference point.
- **Region** — a spatial subset with extent.
- **Path** — an ordered spatial trajectory.
- **CoordinateFrame** — origin plus orientation/basis rules.
- **GeometryProfile** — structured geometric information about an Entity/Region.

These are typed semantic values/domains rather than new lexical Categories.

A physical Entity has a spatial extent:

`Extent(Entity, Time?) -> Region`

## Here and frames

`Here` is `Reference<Location>`.

For magic it resolves to the Command's defined activation origin, such as a caster, inscription, or device anchor. It is not chosen contextually after execution begins.

Directions such as Up/Down and measurements such as Height require a CoordinateFrame. A casting context may provide a default local frame; otherwise the frame must be explicit.

`OppositeUp = Down` remains valid once the frame is resolved.

## At, In, and containment

`At(Entity, Location)` means the Entity's declared anchor position coincides with the Location.

`In(A, Region)` means A's spatial extent is a subset of the Region, allowing boundary contact.

`Inside(A, Region)` is stricter: A lies in the interior and does not contact the boundary.

Contain is the converse of In:

`Contain(R,A) <=> In(A,R)`

This is relation converse, not semantic Opposite.

`Outside(A,R)` is stronger than NotIn: A has no extent in the interior of R. Partial overlap therefore may satisfy NotIn while failing Outside.

## Contact and overlap

`Touch(A,B)` means their relevant boundaries/extents make contact without requiring interior intersection.

Add candidate Relation:

`Overlap(A,B)`

for nontrivial shared spatial extent.

## Distance, Near, and Far

`Distance(A,B) -> Quantity<Length>`

uses a declared distance metric and anchor rule.

Near/Far are threshold predicates over Distance. They may be a reversible semantic pair without being logical complements; an intermediate distance can satisfy neither.

Magical use requires a fixed or explicit threshold.

## To and From

Refine To/From as oriented path-role constructors.

`To(target)` constrains a movement/path goal or orientation toward target.

`From(source)` constrains the corresponding origin/away relation.

They remain a declared reversible pair:

`OppositeTo = From`


## Relative location construction

Add a functional spatial constructor:

`Offset(origin: Location, direction, distance: Quantity<Length>) -> Location`

Direction must be objectively resolved.

Useful direction constructors include:

- `Toward(reference)`
- `AwayFrom(reference)`
- Up/Down in a CoordinateFrame
- explicit vector/direction values

This closes common movement expressions such as:

- move three units away from Self;
- move two units toward a selected target;
- place something one unit Up from Here.

`Toward` and `AwayFrom` can reuse the semantic core of To/From where their argument types make the direction meaning unambiguous.

## Move

Working frame:

`Move(theme, goal?, source?, path?) -> EventSpec`

Rules:

- theme must resolve;
- the requested spatial change must be closed enough to determine the result;
- goal/source/path constraints must be compatible;
- ordinary Move requires a continuous Path unless a different movement mode is explicitly selected.

Move does not imply an Agent.

## Teleport

Teleport is a specialized Move semantic molecule:

> change the Entity's location from source to goal without requiring a continuously occupied intermediate Path.

Teleport preserves Entity identity.

A conventional Teleport rune may later provide compression.

## Path

A Path is an ordered geometric trajectory.

It can be constrained by concepts such as:

- From(source)
- To(goal)
- Through(region)
- Around(reference, distance)
- Length(path)
- Straight
- Curve

A path-selection algorithm must be explicitly defined; magic does not choose an intuitively convenient route.

## Through, Around, Between

`Through(Path/Event, Region)` constrains a path to enter/intersect a Region under a registered topological rule.

Around requires a center/reference and usually a radius/distance constraint; it is not a vague magical relation.

Spatial Between is ternary:

`Between(X,A,B)`

and uses a resolved segment/geodesic/metric rule.

A more general ordered-domain Between Operator may support numeric and spatial typed frames.

## Surface, Center, Edge, Side

Per lexical resolution:

`Surface(X) -> SurfaceRegion`

returns the boundary surface of X.

`Center(X) -> Location/Region`

uses a registered unique geometric definition, provisionally geometric centroid where defined. If no unique result exists, it fails.

`Edge(X) -> BoundaryRegion or Collection<BoundaryFeature>`

may return multiple features rather than choosing one.

A generic singular Side is underdetermined. Prefer:

`Sides(X, Frame?) -> Collection<SurfaceRegion>`

then select a side through an explicit relation or selector.

## Form and geometry profile

`Form(X) -> GeometryProfile`

A GeometryProfile can contain:

- topology;
- extents;
- surfaces/boundaries;
- curvature;
- holes;
- symmetry;
- orientation-relative measures.

Point, Line/Curve, SurfaceRegion, and Region are geometric Kinds/structures.

## Shape predicates

Straight, Curve, Flat, Round, and Symmetry are geometric predicates.

For objective magic they need exact definitions or explicit tolerances. Ordinary-language versions may remain contextual.

`Holes(X) -> Collection<HoleFeature>`

is preferable to assuming one Hole.

Symmetry should identify its transformation/axis/class rather than relying on a generic visual judgment.

## Measurement

- `Area(SurfaceRegion) -> Quantity<Length^2>`
- `Volume(Region/Entity extent) -> Quantity<Length^3>`
- `Length(Path/feature) -> Quantity<Length>`

Height is extent projected along the Up axis of a CoordinateFrame.

Width requires a selected frame axis.

Angle measures separation of directions/rays/surfaces under a resolved frame.

## Canonical Region constructors

Objective area effects benefit from registered geometric constructors. Strong candidates include:

### Sphere/Ball

`Ball(center: Location, radius: Quantity<Length>) -> Region`

Its boundary can be obtained with Surface. If the language keeps a separate Sphere word, Sphere can denote the boundary shape.

### Disk

`Disk(center, radius, plane/frame) -> Region`

### Box

`Box(center/origin, extents, CoordinateFrame) -> Region`

### Cylinder

`Cylinder(axis/path, radius, length?) -> Region`

### Cone

`Cone(origin, direction, angle, length) -> Region`

### Tube

`Tube(path, radius) -> Region`

These may be semantic molecules rather than primitive roots.

## Constructed surfaces and walls

A wall-like Region has nonzero thickness plus extent/orientation. A common Wall semantic molecule can be defined from Region geometry rather than treating every Surface as a wall.

## Occupancy

A destination may be geometrically defined but physically incompatible with the current world state.

That is an execution constraint. Magic does not silently move the destination to a nearby alternative unless a selector such as NearestValid is explicitly written.

## Spatial reference by Entity

Functions such as Distance, To, and Center may accept Entities only when their entries specify which anchor/extent rule they use.

If multiple spatial interpretations are possible, a specialized function must state which one is intended.

## Result

Spatial magic now distinguishes:

- Location;
- Region;
- Path;
- CoordinateFrame;
- containment/contact/overlap;
- geometry profile;
- measured extent;
- constructed areas.

This provides the foundation for precise movement, range, spatial selection, and shaped effects.
