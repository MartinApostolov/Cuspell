# Core Historical Vocabulary

_Status: current maintainer index; machine-readable Old Name registry is normative_

The original first-civilization vocabulary pass has been archived at `archive/world/FIRST_CIVILIZATION_VOCABULARY_PRE_CP98.md` because it accumulated superseded root names and historical spellings during minimization.

Current machine truth for established core vocabulary is:

- `language/names/old_names.json` — Old Name signs, historical name units, meanings, and dependencies;
- `world/core/concepts.json` — referenced world concepts/classifiers;
- `language/core/units.json` — typed Unit metadata for Unit-valued Old Names.

The player-facing list is generated/checked in `player/names/OLD_NAMES.md`.

## Current scope

The core Old Name registry contains **182 entries**:

- **175 concept/Kind Old Names**;
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

The 182-entry registry is a **foundation**, not a declaration that the historical civilization vocabulary is complete.

Checkpoint 106's systematic coverage audit finds that the language can already express most civilization-scale distinctions through roots + composition + Names, but the established Old Name list is uneven because it grew partly under corpus pressure. Examples of the imbalance include:

- Checkpoint 111 corrects the earlier anatomy imbalance: Head, Face, Arm, Leg, Foot, Finger, Nose, Tooth, Tongue, Heart, Brain, and Hair now join the pre-existing Body/Hand/Eye/Ear/Mouth/Skin/Bone/Flesh/Blood/Organ/Stomach/Wrist/Tendon/Wound layer;
- Checkpoint 114 corrects the earlier craft/transport imbalance by adding Knife, Axe, Saw, Pot, Needle, Wheel, Cart/Wagon, Plow, Loom, Furnace/Kiln, Anvil, Sail, Oar, Anchor, Port, Building, Roof, Room, Floor, Workshop, Mill, and Fortification;
- Checkpoint 115 corrects the earlier land/military/public-institution imbalance by adding Soldier, Army, Armor, Shield, Spear, Bow, Arrow, Prison, Prisoner, Judge, Polity/State, Government, and Citizen/Member of Polity;
- Checkpoint 112 corrects the earlier natural-world imbalance: River, Lake, Sea/Ocean, Mountain, Hill, Island, Shore/Coast, Forest, Sky, Cloud, Rain, Ice, Snow, Wind, Storm, Land, Soil, and Sand are now named; broad art/music and several later civilization domains remain sparse.

This is not evidence that the existing names should be removed. It means future additions should be audited in **domain batches** rather than chosen randomly.

High-priority historical-vocabulary families are currently:

- art/ritual/shared culture;
- calendar/daily life.

Not every concept in those families should become an Old Name. Keep a concept compositional when its description is short and natural; use world-package concepts/New Names for setting-specific species, technologies, institutions, materials, ranks, proper places, and similar local vocabulary.

The complete checkpoint-106 reasoning is preserved historically in `archive/audits/cp106_CIVILIZATION_VOCABULARY_COVERAGE_AUDIT.md`. Checkpoints 111–115 are the current balanced domain expansions; the accepted machine-readable registry now contains 182 Old Names.

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

## War and public-institutions batch

Checkpoint 115 adds thirteen common military/civic concepts as **world Kinds + Old Names**:

- soldier — `«AttackObligated«Know«MoveLifeThing»»»`;
- army — `«Group«AttackObligated«Know«MoveLifeThing»»»»`;
- armor — `«PreventAttack««Know«MoveLifeThing»»SurfaceThing»»`;
- shield — `«PreventAttack«UseThing»»`;
- spear — `«HighLengthSharp«EndLife«UseThing»»»`;
- bow — `«DistanceAttack«EndLife«UseThing»»»`;
- arrow — `«SharpMoveAttackThing»`;
- prison — `«PreventMove«Know«MoveLifeThing»»«JoinedInThing»»`;
- prisoner — `«In«PreventMove«Know«MoveLifeThing»»«JoinedInThing»»«Know«MoveLifeThing»»»`;
- judge — `«Authority«EvaluateObligatedGroup»«Know«MoveLifeThing»»»`;
- polity/state — `«Authority«ObligatedPermittedRule»Group«Know«MoveLifeThing»»»`;
- government — `«Authority«Authority«ObligatedPermittedRule»Group«Know«MoveLifeThing»»»Group»`;
- citizen/member of polity — `«Member«Authority«ObligatedPermittedRule»Group«Know«MoveLifeThing»»»«Know«MoveLifeThing»»»`.

The historical components remain etymology rather than live definitions. A Soldier can remain a Soldier while off duty; a Prisoner can temporarily leave a prison under guard; a Citizen does not cease to be one merely because they are physically outside the polity.

### Authority is productive semantics

The public-institution audit exposes a real semantic distinction:

`Authority(holder,scope)`

is recognized social/institutional standing to issue or validate binding rules, permissions, obligations, or decisions for a scope.

It is **not** the same as:

- physical/factual `Control`;
- being `Permitted` to do one thing;
- ownership or possession;
- causing an outcome.

A jailer may Control a prisoner without legitimate Authority. A judge or government may have Authority without physically controlling every subject in scope.

The world ontology supplies jurisdiction, legitimacy, succession, delegation, revocation, and conflicts of authority.

### Prison does not secretly add a confinement primitive

Prison and Prisoner are world classifications. Checkpoint 115 does not add `Imprison`, `Confined`, or `Free` merely because those nouns are useful.

Physical confinement can involve location, capability, barriers, control, and prevention; legal detention adds law/authority/permission. If later corpus or magical execution requires a single exact confinement state/process, audit that semantic distinction independently.

### Event-category classifier pressure

The audit deliberately does **not** add Trial, Battle, War, Crime, or Punishment as ordinary Entity Kinds.

These are naturally categories of Events/EventSpecs or extended processes. The current core world-concept layer is primarily Kind-valued and its ordinary Kind predication applies to Entities. Pretending that a Trial or Battle is an Entity just so it fits the noun registry would hide a type-model problem.

Named individual events can already use New Names because Name facts can refer to semantic values. What remains unresolved is a **generic world classifier for event categories**.

That is a world-model/type-system pressure, not evidence for five new lexical roots. It should be addressed when art/ritual/calendar work reaches ceremony, festival, performance, holiday, and similar event-heavy vocabulary.

### Market cleanup

Checkpoint 115 also resolves the earlier Market ontology ambiguity. Core Market now means a persistent trading institution or trading-site Entity. An individual market-day gathering/event is modeled separately rather than making one Kind alternate between Entity and Event readings.

### Culture-specific ranks and political forms

The core does not automatically add king, queen, emperor, senator, officer, general, duke, noble, police, specific military branches, or citizenship grades.

Those depend strongly on a setting's institutions and should normally be world-package concepts/Old Names or New Names where historically appropriate.

Temple/priest vocabulary is deferred to the next art/ritual/shared-culture batch so religious institutions can be audited together with worship, ritual, ceremony, shrine, music, and related concepts.

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
