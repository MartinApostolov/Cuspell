# Measurement and Descriptor Second-Pass Audit

_Status: checkpoint 86 — family audit complete; Duration folds into Extent_

## Scope

This audit tests the measurement/descriptor family after the successful Rate consolidation.

Current targets before this checkpoint:

- `Damage`
- `Density`
- `DistributionOf`
- `Duration`
- `Form`
- `Heat`
- `Hunger`
- `Light`
- `Loudness`
- `Mass`
- `Phase`
- `TextureOf`
- `Volume`
- `Area`
- `CamouflagedAgainst`
- `Rate`
- `Distance`
- `Extent`
- `Length`
- `TotalAmount`
- `Hard`
- `Sharp`

The goal is to find genuine shared measurement operations without replacing each old
root by an equally primitive descriptor-kind value.

## Accepted reduction — Duration is temporal Extent

`Duration(Event) -> Quantity<Time>` carries no distinction beyond the temporal
extent of a concrete Event.

The existing `Extent` root is already the general extent family:

- occupied spatial Region of an Entity;
- contextual holistic size/extent;
- projected spatial Length along a CoordinateFrame axis.

Adding a type-distinct frame:

`Extent(Event) -> Quantity<Time>`

is therefore an exact generalization rather than a new abstraction.

There is no ambiguity because Event is disjoint from Entity/Region inputs and the
result is explicitly Time-valued.

The standalone `Duration` root is removed.

The historical `«DurationUnit»` Old Name remains usable but is rebuilt from
`Extent + Unit`; its frozen unit meaning remains the canonical Time unit.

**Net result: 1 root removed, no root added.**

## Why the other obvious merges do not yet work

### Mass, Heat, Light, Volume, Length

These are typed AttributeDescriptors, not merely names for Quantity dimensions.

A proposal such as:

`Measure(subject, MassKind)`

does not reduce anything if `MassKind` is still an atomic semantic value meaning
exactly Mass.

Their descriptor identity is also used by generic machinery such as `Change`,
`BeforeValue`, `AfterValue`, `UnknownValueOf`, and threshold/property
construction.

They remain until a descriptor system can genuinely derive several attribute
identities from fewer independent semantics.

### Length versus Extent

Spatial `Extent` already subsumes Size, Span, Height, Width, and Depth-style
meanings, but `Length` still has a separate AttributeDescriptor identity and a
Path measurement frame.

Simply moving `Length(Entity)` and `Length(Path)` onto `Extent` would lose the
current Length descriptor used by attribute-aware constructions unless the
descriptor architecture itself becomes multi-typed.

So the callable readings overlap conceptually, but the full registered semantics do
not yet reduce losslessly.

### Area and Volume

Area and Volume are different dimensional measures of geometry.

For arbitrary shapes they are not exact powers/products of one axis length, so
`Power Length ...` or multiplying projected Extents would only work for restricted
geometries.

Moving them to type-selected `Extent` frames would also not preserve their
AttributeDescriptor identities without additional descriptor machinery.

Retain.

### Density

For a simple homogeneous physical Entity:

`Divide Mass X Volume X`

has the Density dimension and often equals the intended physical density.

But the current `Density` root also has a Distribution + Region frame used for
local field density. `DistributionOf` can represent general resources, and
`TotalAmount` is a generic aggregate Quantity whose dimension depends on the
resource/world model.

The current core has no general integration/region-measure type mechanism that
makes every Distribution density exactly `TotalAmount / Volume` while preserving
the current typing.

Retain Density for now.

### Damage, Hunger, Loudness

All three return ordered `EvaluationValue`, but they are independent scales:
physical injury, hunger state, and acoustic/perceived loudness.

A generic `Level(subject, DamageKind)` design only moves the three primitive
identities into three enum values.

No smaller shared semantic basis currently derives one from another.

Retain.

### Hard and Sharp

Both are contextual PropertyDescriptors, but their standards are different:
resistance to deformation versus edge/point concentration.

A generic threshold operator is already supplied by `High`/`Low`; what is
missing is an objective underlying scalar descriptor for each property.

Inventing `Hardness` and `Sharpness` would replace two primitive properties by
two primitive attributes and would not lower the count.

Retain.

### Form and TextureOf

Both return structured profiles, but the profile types are intentionally distinct:

- `Form` -> `GeometryProfile`;
- `TextureOf` -> `TextureProfile`.

Texture is not exactly the complete geometric Form of an Entity, and Form is not
surface texture.

A generic `Profile(subject, ProfileKind)` would again require one irreducible kind
per old root.

Retain.

### Phase

`Phase` is a discrete AttributeDescriptor whose values are the registered phase
family (Solid/Liquid/Gas/Plasma). It is not an ordered scalar and does not reduce to
Heat: phase transitions depend on material/world rules, pressure, composition, and
other conditions.

Retain.

### Distance

Physical `Distance(A,B)` is a binary metric relation. `Length(Path)` is the
length of an already supplied path; the current language has no universal
shortest/geodesic-path constructor whose Length is definitionally Distance.

The contextual property/event-boundary Distance frames are also not ordinary
spatial Length.

Retain.

### DistributionOf and TotalAmount

These already survived exact review:

- `DistributionOf` constructs/retrieves a Distribution field;
- `TotalAmount` aggregates/integrates a Distribution over a domain/Region.

Neither local Density nor ordinary arithmetic provides the missing general field
construction or integration operation.

Retain.

### CamouflagedAgainst

Camouflage is observer/background-sensitive perceptual similarity/effectiveness.
Color/texture/profile measurements are inputs to possible world-model decisions but
do not by themselves entail camouflage.

Retain.

### Rate

The newly generalized `Rate` already represents the successful reusable
per-Time operation for both Quantity change and EventSpec occurrence.

It is the example of what a valid family reduction should look like and remains.

## Result

Checkpoint 86 makes one exact reduction:

- `Duration(Event)` -> `Extent(Event)`.

Counts become:

- registered base entries: **209 -> 208**;
- semantic primitive candidates: **129 -> 128**;
- formal constructors: **54**;
- reference forms: **16**;
- domain values: **10**;
- unresolved candidates: **0**;
- derived candidates: **0**.

The measurement/descriptor family becomes **21 current primitive candidates**.

## Next target

The next high-leverage family is **social/affective structure**.

That audit should first separate:

- affective attitudes/states;
- institutional/social relations;
- social evaluation/repair;

and reject any design that merely replaces `Love`, `Hate`, `Trust`, etc. with
one atomic attitude-kind value each.
