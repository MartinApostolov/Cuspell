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

Directions and axis-relative measurements require a CoordinateFrame. The minimized core represents frame-relative scalar extent with `Extent(subject,frame,axis-index)`. A casting context may provide a default local frame for ordinary interpretation only where a construction explicitly permits it.

`OppositeUp = Down` remains valid once the frame is resolved.

## Rigid rotation

Cuspell distinguishes **translation** from **rotation**.

`Move(theme,...)` changes an Entity's spatial position along/relative to a goal or Path.

`Rotate(theme,pivot,axis,turns) -> EventSpec`

rigidly rotates an Entity about the oriented axis line through an explicit pivot Location by a signed number of **full turns**.

- `pivot` fixes a point on the rotation axis;
- `axis` is a Direction giving the oriented axis;
- `turns` is a dimensionless Quantity:Number, where 1 is one full revolution and sign chooses rotational direction under the world/frame orientation convention.

Rotation preserves intrinsic `Form`/shape. It changes pose/orientation, and if the chosen pivot is not on the Entity's anchor then the anchor may also travel along the corresponding circular arc.

This is not reducible to `Change Form`: rotating a rigid wheel does not reshape the wheel. It is also not reducible to ordinary `Move`, which constrains translational position/path but does not state rigid orientation change.

Checkpoint 114 therefore adds `Rotate` as one semantic primitive candidate. Checkpoint 121 re-runs the exact reduction test after the later geometry/Attribute work and retains it. `Offset` constructs translated Locations, CoordinateFrame/Direction values describe spatial references, and `Form` remains intrinsic geometry; none supplies the missing Entity pose/orientation transform. Reconstructing a rigid turn by separately moving all Parts would require a shared pivot/axis/angle plus preservation of all rigid relative geometry—effectively re-implementing Rotate as hidden constraints. Angle-specific units are not required for the core operation because signed full-turn quantities are dimensionless; a world may later provide culturally convenient angle units/names if needed.

## At, In, and containment

`At(Entity, Location)` means the Entity's declared anchor position coincides with the Location.

`In(A, Region)` means A's spatial extent is a subset of the Region, allowing boundary contact.

Strict interior containment is compositional rather than a separate root:

`In A R And Not Touch Extent A R`

Here `Touch(Region,Region)` means the two Region boundaries contact. The `In` term supplies containment; the negated boundary-contact term excludes the boundary cases.

A separate Contain root is unnecessary. The containment perspective is the same underlying relation written with its actual roles:

`In(A,R)`

If prose says “R contains A”, Cuspell still writes the item/region relation directly rather than paying for a Converse or Contain synonym.

Strict outside is also compositional:

`Not Overlap Extent A R`

where `Overlap(Region,Region)` means the Region interiors share nontrivial spatial extent. This is stronger than `Not In A R`: partial overlap can satisfy Not In while still failing the Outside composition, whereas boundary-only contact has no interior overlap and therefore counts as outside.

## Contact and overlap

`Touch(A,B)` means relevant boundaries make contact without requiring interior intersection. Typed frames include Entity/Entity contact state and Region/Region boundary contact.

`Overlap(A,B)` means nontrivial shared interior/extent under the registered topology. Typed frames cover Entity, Region, Event, and TimeInterval domains.

## Distance

`Distance(A,B) -> Quantity<Length>`

is now strictly a physical/spatial separation operation.

Both arguments must be `SpatialValue`. The current type family includes:

- Entity;
- Location;
- Region.

The world model must fix the spatial metric plus any anchor/set-distance convention needed for non-point carriers. Those conventions are physical semantics of Distance, not logical “distance from satisfying a proposition.”

Threshold descriptions such as “near” or “far” can be represented by comparing the resulting Length to an explicit/contextual physical threshold where the relevant world model supplies one.

### Almost is not Distance

Checkpoint 105 removes the former contextual `Distance(PropertyDescriptor, Entity)` and `Distance(EventSpec)` frames.

Those frames had been introduced to replace `Almost`, but an ordered property/event state does not automatically supply a numerical metric. “Almost true” or “almost happened” can depend on different domain-specific notions of progress/nearness.

`Almost` is therefore restored as its own contextual operator over Proposition and EventSpec. It is valid ordinary language but remains non-executable in magic while its near-satisfaction/near-occurrence criterion is contextual.

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

## Teleportation

There is no separate `Teleport` root in the minimized core.

Teleportation is a discontinuous boundary change in the persistent `At` state:

- with explicit source: `End At X source And Begin At X goal`;
- when the source is not stated: `Begin At X goal`.

This preserves Entity identity while deliberately introducing no `Move` EventSpec and no continuously occupied intermediate Path. Ordinary continuous relocation still uses `Move`.

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

## Through, Around, and betweenness

`Through(Path/Event, Region)` constrains a path to enter/intersect a Region under a registered topological rule.

Around requires a center/reference and usually a radius/distance constraint; it is not a vague magical relation.

The former executable `Between` root covered ordered values and is now written compositionally as:

`More X A And More B X`

for the strict ordered case A < X < B.

Geometric betweenness is a different relation: "X lies on/near the segment, corridor, or geodesic between A and B." The removed ordered root never implemented that geometry exactly. If Cuspell needs geometric betweenness, it should be added only after its frame/metric semantics are specified rather than overloading numeric ordering.

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

CoordinateFrames expose an ordered basis for axis-relative measurement.

`Extent(subject, frame, @)` is extent projected along the frame's primary/up axis; this is the old Height meaning.

`Extent(subject, frame, @@)` is extent along the frame's designated width axis; this is the old Width meaning.

`Extent(subject, frame, @@@)` is the frame's designated depth/third axis. The former `Depth` and `Span` roots are removed. Ordinary discourse may omit the frame as `Extent(subject, @@@)` when the world/discourse context provides the reference frame or inward/depth orientation; objective magical geometry should supply the frame explicitly.

Further positive axis indices remain frame-defined.

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

Distance accepts current SpatialValue carriers (Entity, Location, Region); its world model must specify the applicable metric and any Entity/Region anchor or set-distance rule. Other spatial functions still declare their own carrier/anchor semantics.

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
