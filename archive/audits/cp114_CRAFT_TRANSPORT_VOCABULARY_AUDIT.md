# Checkpoint 114 — Craft, Manufacturing, and Land-Transport Vocabulary Audit

_Status: fourth balanced civilization-vocabulary batch + one semantic repair_

## Purpose

Checkpoint 106 identified craft/manufacturing and land transport as an uneven vocabulary domain. Existing Cuspell already had Tool, Cutting Tool, Blade, Sword, Hammer, Shovel, Container, Bucket, Rope, Clothing, House, Road, Bridge, Boat, Ship, and basic material vocabulary.

Checkpoint 114 audits the next common layer while keeping artifact names separate from productive manufacturing/motion semantics.

## Semantic finding — rigid rotation

The artifact audit exposed one genuine semantic-language gap.

Cuspell had:

- `Move` for translational motion;
- `Form` for intrinsic geometry/shape;
- CoordinateFrame and Direction values;
- spatial Region/Path/Location machinery.

But it had no exact way to state:

> rotate this rigid Entity around this axis.

That cannot be reduced to `Move`: translation does not encode orientation change.

It also cannot be reduced to `Change Form`: a rigid wheel that turns has not changed its intrinsic shape.

### Accepted root

Checkpoint 114 adds:

`Rotate(theme,pivot,axis,turns) -> EventSpec`

where:

- theme: Entity;
- pivot: Location;
- axis: Direction;
- turns: Quantity:Number.

The pivot and oriented Direction define the axis line. `turns` is signed and measured in full revolutions, so 1 is one full turn and no separate Angle dimension is required for the core operation.

The world/frame convention fixes positive rotational direction.

If the pivot is not on the Entity's anchor, the rotation may also move the anchor along the appropriate arc.

**Classification:** semantic primitive candidate.

This is a general geometric operation, not a Wheel-specific convenience root.

## Accepted artifact / infrastructure vocabulary

The batch adds twenty-two **world Kinds + Old Names**.

### Knife

`«LowLength«Sharp«EndJoinedMatter«UseThing»»»»`

Cost: 8.

A historically shorter/smaller Blade family. Exact knife classification is frozen world ontology, not a current length threshold.

### Axe

`««MatterPart«HighExtentHard«ChangeExtentLifeMatter»»»«EndJoinedMatter«UseThing»»»`

Cost: 14.

Historically a Wood-associated Cutting Tool. Modern/world membership is not limited to cutting wood.

### Saw

`«Repeat«EndJoinedMatter«UseThing»»»`

Cost: 6.

Repeated-action Cutting Tool family.

### Pot / cooking vessel

`«Heat«InThing»»`

Cost: 3.

Container family historically associated with Heat.

### Needle

`«SharpBeginJoined«UseThing»»`

Cost: 5.

Sharp joining/sewing Tool family.

### Wheel

`«RotatePartThing»`

Cost: 3.

Rotating-part artifact family. Exact circular/axle/bearing geometry belongs to world ontology.

### Cart / wagon

`«Have«RotatePartThing»MoveThing»`

Cost: 6.

Wheeled land-transport vehicle family.

### Plow

`«Change««ChangeExtentLifeMatter»HaveMatter»«UseThing»»`

Cost: 9.

Soil-changing agricultural Tool family.

### Loom

`«BeginExist«JoinedLowExtentMatter»«UseThing»»`

Cost: 8.

Textile-forming Tool/frame family.

### Furnace / kiln

`«HighHeat«InThing»»`

Cost: 4.

Broad high-heat chamber family. Furnace, kiln, and setting-specific subtypes may later split in world packages if needed.

### Anvil

`«HardChange«HeatChangeHardMatter»«UseThing»»`

Cost: 8.

Hard metal-forming support/tool family.

### Sail

`««Move«LifeGasMatter»Thing»Part«MoveInLiquidThing»»`

Cost: 10.

Wind-associated Boat part family.

### Oar

`«Move«MoveInLiquidThing»«UseThing»»`

Cost: 7.

Boat-moving Tool family.

### Anchor

`«PreventMove«MoveInLiquidThing»Thing»`

Cost: 7.

Boat station-keeping/anti-movement object family.

### Port / harbor facility

`«Have«MoveInLiquidThing»Region»`

Cost: 6.

Transport site/facility for watercraft. A natural sheltered harbor is a different geography classifier if a world needs that distinction.

### Building / constructed structure

`«JoinedInThing»`

Cost: 3.

Broad constructed enclosure/structure family.

### Roof

`«Prevent«Fall«LiquidMatter»Thing»Part«JoinedInThing»»`

Cost: 9.

Protective Building-part family, historically named around preventing Rain/weather entry.

### Room

`«In«JoinedInThing»Region»`

Cost: 5.

Persistent interior-space feature family. Room is represented as a feature Entity whose spatial extent is a Region.

### Floor

`«MoveSurfacePart«JoinedInThing»»`

Cost: 6.

Walkable/movement-support Building-surface part family.

### Workshop

`«Use«UseThing»«JoinedInThing»»`

Cost: 6.

Craft/tool-use space or facility family.

### Mill

`«Change««BeginLifePart«ChangeExtentLifeMatter»»«TransferLifeMatter»»«JoinedInThing»»`

Cost: 14.

Material-processing facility family historically centered on Grain processing.

### Fortification

`«PreventAttack«JoinedInThing»»`

Cost: 5.

Defensive constructed-work family.

## Artifact nouns do not create hidden process roots

Checkpoint 114 deliberately does **not** add:

- Build;
- Make;
- Cook;
- Weave;
- Sew;
- Smelt;
- Grind;
- Drive;
- Ride;
- Carry;
- Push;
- Pull.

Some of those meanings may be exact compositions in particular contexts; others may carry genuine manner/agency distinctions.

The existence of Pot, Loom, Mill, Cart, etc. is not evidence that those processes have already been semantically formalized.

If later corpus or magical execution needs them, audit them independently.

## Why Rotate is different

Rotate is not being added because English has a short verb.

It survives the same irreducibility test used during root minimization:

- orientation change can occur with no change of intrinsic Form;
- a rigid turn can occur with little/no net anchor translation;
- translational Move can occur with no orientation change;
- expressing rigid rotation by moving every Part separately would require hidden geometric constraints equivalent to a rotation operator.

Therefore a general objective rotation operation earns a productive root.

## Room / building modeling

A Building is a persistent constructed Entity.

A Room is a persistent interior-space feature Entity with an `Extent -> Region`.

This allows ordinary facts such as:

- Name;
- Part;
- ownership/use;
- Damage;
- containment/history;
- spatial extent;

without forcing generic Room vocabulary to be a bare anonymous Region.

## Technology boundary

These core Kinds are broad historically common technology families, but the core does not assert that every world has instances of them.

World packages determine:

- whether carts/looms/furnaces/mills exist;
- exact technology level;
- traction/power source;
- construction/material;
- specialized subtypes;
- named individual artifacts/facilities.

Specific named vehicles, workshops, ports, buildings, etc. remain New Names.

## Inventory effect

Before checkpoint 114:

- 210 registered base entries;
- 129 semantic primitive candidates;
- 55 formal constructors;
- 263 semantic frames;
- 48 multi-frame entries;
- 147 Old Names;
- 140 core world concepts.

After checkpoint 114:

- **211 registered base entries**;
- **130 semantic primitive candidates**;
- **55 formal constructors**;
- **264 semantic frames**;
- **48 multi-frame entries**;
- **169 Old Names**;
- **162 core world concepts**.

Old Name meanings become:

- **162 concept/Kind Old Names**;
- **6 Unit Old Names**;
- **1 parameterized expression Old Name**.

## Result

The craft/manufacturing/transport noun layer is substantially more balanced, and the audit also repairs the independent rigid-rotation gap instead of hiding it inside Wheel vocabulary.

The next civilization domain is:

**war and public institutions**.

That pass should audit soldier, army, armor, shield, spear, bow, arrow, prison, judge, trial, polity/state/government, citizen/member-of-polity, temple, priest, and related public roles/institutions, while keeping legal processes and military actions separate from mere noun vocabulary.
