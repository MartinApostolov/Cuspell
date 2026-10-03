# Core Historical Vocabulary

_Status: current maintainer index; machine-readable Old Name registry is normative_

The original first-civilization vocabulary pass has been archived at `archive/world/FIRST_CIVILIZATION_VOCABULARY_PRE_CP98.md` because it accumulated superseded root names and historical spellings during minimization.

Current machine truth for established core vocabulary is:

- `language/names/old_names.json` — Old Name signs, historical name units, meanings, and dependencies;
- `world/core/concepts.json` — referenced world concepts/classifiers;
- `language/core/units.json` — typed Unit metadata for Unit-valued Old Names.

The player-facing list is generated/checked in `player/names/OLD_NAMES.md`.

## Current scope

The core Old Name registry contains **169 entries**:

- **162 concept/Kind Old Names**;
- **6 canonical Unit Old Names**;
- **1 parameterized expression Old Name** (`«TransferHave»` = give).

It includes migrated ordinary nouns, civilization vocabulary, anatomy/environment vocabulary exposed by corpus testing, and the six typed canonical Unit names.

Examples:

- human — `«Know«MoveLifeThing»»`
- cat — `«LowExtent«MoveLifeThing»»`
- water — `«LiquidMatter»`
- body — `«LifeMatter»`
- hand — `«Control«LifeMatter»Part»`
- sound — `«HearingThing»`
- boat — `«MoveInLiquidThing»`
- ship — `«HighExtent«MoveInLiquidThing»»`
- food — `«TransferLifeMatter»`
- currency — `«TransferBeginHaveThing»`
- contract — `«Obligated«PersistSignThing»»`

## Coverage status

The 169-entry registry is a **foundation**, not a declaration that the historical civilization vocabulary is complete.

Checkpoint 106's systematic coverage audit finds that the language can already express most civilization-scale distinctions through roots + composition + Names, but the established Old Name list is uneven because it grew partly under corpus pressure. Examples of the imbalance include:

- Checkpoint 111 corrects the earlier anatomy imbalance: Head, Face, Arm, Leg, Foot, Finger, Nose, Tooth, Tongue, Heart, Brain, and Hair now join the pre-existing Body/Hand/Eye/Ear/Mouth/Skin/Bone/Flesh/Blood/Organ/Stomach/Wrist/Tendon/Wound layer;
- Checkpoint 114 corrects the earlier craft/transport imbalance by adding Knife, Axe, Saw, Pot, Needle, Wheel, Cart/Wagon, Plow, Loom, Furnace/Kiln, Anvil, Sail, Oar, Anchor, Port, Building, Roof, Room, Floor, Workshop, Mill, and Fortification;
- Sailor, Crew, and Captain are named while ordinary land/military vocabulary is sparse;
- Checkpoint 112 corrects the earlier natural-world imbalance: River, Lake, Sea/Ocean, Mountain, Hill, Island, Shore/Coast, Forest, Sky, Cloud, Rain, Ice, Snow, Wind, Storm, Land, Soil, and Sand are now named; broad art/music and several later civilization domains remain sparse.

This is not evidence that the existing names should be removed. It means future additions should be audited in **domain batches** rather than chosen randomly.

High-priority historical-vocabulary families are currently:

- war/public institutions;
- art/ritual/shared culture;
- calendar/daily life.

Not every concept in those families should become an Old Name. Keep a concept compositional when its description is short and natural; use world-package concepts/New Names for setting-specific species, technologies, institutions, materials, ranks, proper places, and similar local vocabulary.

The complete checkpoint-106 reasoning is preserved historically in `archive/audits/cp106_CIVILIZATION_VOCABULARY_COVERAGE_AUDIT.md`. Checkpoints 111–114 are the current balanced domain expansions; the accepted machine-readable registry now contains 169 Old Names.

## Basic anatomy batch

Checkpoint 111 adds twelve common pre-magic anatomy concepts as **world Kinds + Old Names**, not semantic roots:

- head — `«Know«LifeMatter»Part»`;
- face — `«VisionSaySurface«Know«LifeMatter»Part»»`;
- arm — `«ControlMove«LifeMatter»Part»`;
- leg — `«Move«LifeMatter»Part»`;
- foot — `«MoveTouch«LifeMatter»Part»`;
- finger — `«ControlPart«Control«LifeMatter»Part»»`;
- nose — `«Olfaction«LifeMatter»Part»`;
- tooth — `«HardEat«LifeMatter»Part»`;
- tongue — `«SayEat«LifeMatter»Part»`;
- heart — `«Move«LiquidLifeMatter»«Use«LifeMatter»Part»»`;
- brain — `«Know«Use«LifeMatter»Part»»`;
- hair — `«ChangeExtentSurface«LifeMatter»Part»`.

These spellings are historical etymologies, not live anatomical definitions. Exact morphology, homology, species applicability, digit count, organ physiology, and similar facts belong to the world classifiers.

The batch deliberately does **not** add every ordinary anatomy noun. Neck, shoulder, elbow, knee, chest, back, abdomen, muscle, joint, nail, lip, genital/reproductive anatomy, and finer internal anatomy remain deferred until corpus/world pressure shows which are common enough to justify historical lexicalization.

No semantic-language gap was found in this batch.

## Natural geography and weather batch

Checkpoint 112 adds eighteen common natural-world concepts as **world Kinds + Old Names**, not semantic roots:

- land — `«SolidMatterRegion»`;
- soil — `««ChangeExtentLifeMatter»HaveMatter»`;
- sand — `«LowExtent«HardMatter»»`;
- river — `«Move«LiquidMatter»Path»`;
- lake — `«LowExtent«LiquidMatter»Region»`;
- sea/ocean — `«HighExtent«LiquidMatter»Region»`;
- mountain — `«HighExtent«HardMatter»Region»`;
- hill — `«LowExtent«HighExtent«HardMatter»Region»»`;
- island — `««SolidMatterRegion»In«LiquidMatter»»`;
- shore/coast — `«Touch«LiquidMatter»«SolidMatterRegion»»`;
- forest — `«Group«HighExtentHard«ChangeExtentLifeMatter»»Region»`;
- sky — `«High«LifeGasMatter»Region»`;
- cloud — `««LiquidMatter»In«LifeGasMatter»Thing»`;
- rain — `«Fall«LiquidMatter»Thing»`;
- ice — `«Solid«LiquidMatter»Thing»`;
- snow — `«Fall«Solid«LiquidMatter»Thing»»`;
- wind — `«Move«LifeGasMatter»Thing»`;
- storm — `«HighExtent«Move«LifeGasMatter»Thing»»`.

The historical components are etymology and mana history, not current physical definitions. A huge Lake does not become a Sea because it is contextually large; a calm River remains a River; an exotic Storm need not literally be high-extent Wind if the world classifier includes it.

Geographic features and weather phenomena are modeled as world-feature/phenomenon Entities whose spatial presence can be described with existing `Extent`, `In`, `At`, `Move`, `Fall`, and other spatial/event machinery. Proper names of individual rivers, mountains, storms, etc. remain **New Names**. When Kind membership matters, the world package should normally name the feature Entity; its occupied Region is then available through `Extent`.

This batch does **not** add Rain/Wind/Storm process roots. Creating or simulating weather still requires the world execution model to define the relevant matter, motion, distribution, energy, and thresholds. The noun vocabulary does not pretend to solve fluid dynamics.

`Field` is deliberately deferred to the agriculture batch because its ordinary civilization meaning is primarily cultivated/open land use rather than a universal natural feature.

No semantic-language gap was found that requires a new core root merely to name these concepts.

## Food, agriculture, and common-materials batch

Checkpoint 113 adds fourteen common concepts as **world Kinds + Old Names**, not semantic roots:

- field — `«ChangeExtent«TransferLifeMatter»Region»`;
- seed — `«BeginLifePart«ChangeExtentLifeMatter»»`;
- leaf — `«SurfacePart«ChangeExtentLifeMatter»»`;
- fruit — `««TransferLifeMatter»Part«ChangeExtentLifeMatter»»`;
- crop/cultivated plant — `«Control«ChangeExtentLifeMatter»Thing»`;
- grain — `««BeginLifePart«ChangeExtentLifeMatter»»«TransferLifeMatter»»`;
- milk — `«Female«MoveLifeThing»«TransferLifeMatter»Matter»`;
- egg — `«BeginLife«MoveLifeThing»Thing»`;
- salt — `«Gustation«HardMatter»»`;
- clay — `«ChangeForm««ChangeExtentLifeMatter»HaveMatter»»`;
- cloth/textile — `«JoinedLowExtentMatter»`;
- leather/hide — `«Matter«Surface«LifeMatter»Part»»`;
- glass — `«HeatChange«LowExtent«HardMatter»»»`;
- fuel — `«Preserve«HeatLightThing»Matter»`.

As elsewhere, these are frozen historical etymologies. Fruit does not cease to be Fruit if it is inedible; Leather remains Leather after leaving an animal; Glass is not live-classified by whether it was actually made from Sand.

### Farm and field

The earlier Farm concept mixed “place” and “establishment” language. Checkpoint 113 tightens it to a **persistent agricultural Entity/holding or cultivation site**. Its fields, buildings, workers, ownership, and organization relations are represented separately.

A Field is the cultivated land-parcel/feature family. That keeps the land feature distinct from the broader Farm Entity.

### Culture-relative staples

The audit deliberately does **not** add a universal `StapleFood` core Kind.

“Staple food” depends on a community, ecology, era, and diet. Bread, rice, porridge, maize preparations, tubers, or fantasy equivalents should be world/history concepts and Old/New Names when that civilization actually lexicalizes them.

Likewise, specific crop species, named grains, oils, spices, beverages, and recipes belong in world packages unless later evidence shows a genuinely universal core category is needed.

### No hidden agriculture/process roots

Seed, Crop, Grain, Milk, Fuel, and the material names do not add Grow, Harvest, Cook, Weave, Tan, Smelt, or similar process roots.

Existing semantic machinery can state many exact state changes, while culturally/technically specific production processes require their own later audit. Historical noun vocabulary must not be used to pretend that a missing process distinction has already been formalized.

No semantic-language gap was found in this batch.

## Craft, manufacturing, and transport batch

Checkpoint 114 adds twenty-two common artifact/infrastructure concepts as **world Kinds + Old Names**:

- knife — `«LowLength«Sharp«EndJoinedMatter«UseThing»»»»`;
- axe — `««MatterPart«HighExtentHard«ChangeExtentLifeMatter»»»«EndJoinedMatter«UseThing»»»`;
- saw — `«Repeat«EndJoinedMatter«UseThing»»»`;
- pot/cooking vessel — `«Heat«InThing»»`;
- needle — `«SharpBeginJoined«UseThing»»`;
- wheel — `«RotatePartThing»`;
- cart/wagon — `«Have«RotatePartThing»MoveThing»`;
- plow — `«Change««ChangeExtentLifeMatter»HaveMatter»«UseThing»»`;
- loom — `«BeginExist«JoinedLowExtentMatter»«UseThing»»`;
- furnace/kiln — `«HighHeat«InThing»»`;
- anvil — `«HardChange«HeatChangeHardMatter»«UseThing»»`;
- sail — `««Move«LifeGasMatter»Thing»Part«MoveInLiquidThing»»`;
- oar — `«Move«MoveInLiquidThing»«UseThing»»`;
- anchor — `«PreventMove«MoveInLiquidThing»Thing»`;
- port/harbor facility — `«Have«MoveInLiquidThing»Region»`;
- building/constructed structure — `«JoinedInThing»`;
- roof — `«Prevent«Fall«LiquidMatter»Thing»Part«JoinedInThing»»`;
- room — `«In«JoinedInThing»Region»`;
- floor — `«MoveSurfacePart«JoinedInThing»»`;
- workshop — `«Use«UseThing»«JoinedInThing»»`;
- mill — `«Change««BeginLifePart«ChangeExtentLifeMatter»»«TransferLifeMatter»»«JoinedInThing»»`;
- fortification — `«PreventAttack«JoinedInThing»»`.

The batch separates persistent artifacts/facilities from the processes performed with them. A Loom does not create a universal Weave process root; a Pot does not create Cook; a Workshop does not create Make/Build; a Cart does not create Drive/Ride. Those process distinctions remain compositional where exact or require their own evidence-driven semantic audit.

### Rotation gap exposed by Wheel

Wheel vocabulary revealed one genuine semantic gap: Cuspell could translate an Entity with `Move` but could not state a rigid orientation change around an axis.

Checkpoint 114 therefore adds:

`Rotate(theme,pivot,axis,turns)`

as a productive semantic Process. The pivot Location + oriented Direction define the rotation axis, and `turns` is a signed dimensionless number of full revolutions.

`Rotate` is not hidden Wheel vocabulary. It is a general geometric operation useful for wheels, doors/hinges, tools, machinery, bodies, astronomy, and magic.

### Facilities and spaces

Building, Room, Workshop, Mill, Port, and Fortification are persistent world-feature/facility Entities. Their occupied space is available through normal `Extent`/Region semantics.

A Room is modeled as a persistent interior-space feature Entity with an Extent Region rather than as a bare anonymous Region, so it can have identity, Parts, ownership/use, damage, Names, and history.

Port/harbor here means the transport facility/site. A purely natural sheltered harbor remains geography/world vocabulary if a setting needs that distinction.

### Technology boundary

These are broad preindustrial/common technology families, not a declaration that every world must contain them. A world package may simply have no members of Loom, Furnace, Mill, Sail, Cart, etc.

More specialized machines, vehicle types, craft professions, materials, and production methods remain setting vocabulary.

## Historical verbs and parameterized Old Names

Checkpoint 110 closes the noun-bias in the historical vocabulary system.

When a common pre-magic verb/relation is already an **exact Cuspell composition**, an Old Name may freeze that composition with required typed parameters instead of forcing a new semantic root.

The first pilot is:

`«TransferHave» giver theme recipient` = **give**

Its frozen meaning is concurrent `End Have(giver,theme)` plus `Begin Have(recipient,theme)`. It deliberately does not imply ownership transfer, permission, payment, or gift motive.

This mechanism is not a general escape hatch for ordinary English verbs. If the current semantic basis cannot express the distinction exactly—for example generic dance, cook, read, teach, or heal—an Old Name template cannot make an approximate definition exact.

## Historical spelling rule

An Old Name's exact Sign is fossilized historical vocabulary. Its `name_units` record the current historical-cost/dependency model and may differ textually from an obsolete root name that survives inside the fossilized Sign.

Therefore the Sign itself is **not reparsed as current productive Cuspell**.

Example: a historical spelling may retain old-looking text while its registered name-unit history has been rebuilt from surviving roots. The Old Name still resolves to its recorded world concept and pays its registered recursive cost.

## Etymology is not classification

Old Name components explain historical formation and mana cost. They do not act as a live classifier every time the name is used.

A Ship named from a high-extent boat description remains a Ship world concept even if one instance is contextually small.

Actual membership belongs to the world concept's classifier/profile.

## Editing rule

Old Names are still design-stage vocabulary. They may be rewritten while Cuspell semantics/history are not frozen.

When changing an Old Name:

1. update `language/names/old_names.json`;
2. update any dependent world/unit data;
3. keep the dependency graph acyclic;
4. preserve/adjust tests intentionally;
5. regenerate/check the player-facing Old Name index.

Do not preserve a redundant semantic root merely because an Old Name currently depends on it.
