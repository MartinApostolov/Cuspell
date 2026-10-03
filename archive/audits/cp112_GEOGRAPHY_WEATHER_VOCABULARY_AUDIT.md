# Checkpoint 112 — Natural Geography and Weather Vocabulary Audit

_Status: second balanced civilization-vocabulary expansion batch_

## Purpose

Checkpoint 106 identified natural geography/weather as one of the thinnest civilization-vocabulary domains. Checkpoint 112 applies the same classification-first method used by checkpoint 111 anatomy.

Before this pass Cuspell already had Water, Air, Stone, Fire, Tree/Bush, Region/Path, spatial relations, motion, phase, measurement, and event machinery. What was missing was ordinary stable vocabulary for the world features and weather phenomena speakers repeatedly refer to.

## Accepted batch

The following are accepted as **world Kinds + Old Names**, not productive semantic roots:

- land — `«SolidMatterRegion»` — cost 3;
- soil — `««ChangeExtentLifeMatter»HaveMatter»` — cost 6;
- sand — `«LowExtent«HardMatter»»` — cost 4;
- river — `«Move«LiquidMatter»Path»` — cost 4;
- lake — `«LowExtent«LiquidMatter»Region»` — cost 5;
- sea/ocean — `«HighExtent«LiquidMatter»Region»` — cost 5;
- mountain — `«HighExtent«HardMatter»Region»` — cost 5;
- hill — `«LowExtent«HighExtent«HardMatter»Region»»` — cost 7;
- island — `««SolidMatterRegion»In«LiquidMatter»»` — cost 6;
- shore/coast — `«Touch«LiquidMatter»«SolidMatterRegion»»` — cost 6;
- forest — `«Group«HighExtentHard«ChangeExtentLifeMatter»»Region»` — cost 9;
- sky — `«High«LifeGasMatter»Region»` — cost 5;
- cloud — `««LiquidMatter»In«LifeGasMatter»Thing»` — cost 7;
- rain — `«Fall«LiquidMatter»Thing»` — cost 4;
- ice — `«Solid«LiquidMatter»Thing»` — cost 4;
- snow — `«Fall«Solid«LiquidMatter»Thing»»` — cost 5;
- wind — `«Move«LifeGasMatter»Thing»` — cost 5;
- storm — `«HighExtent«Move«LifeGasMatter»Thing»»` — cost 7.

These spellings are historical etymologies and mana histories, not live classifiers. A huge Lake does not become a Sea because it is contextually large; a calm River remains a River; an exotic Storm need not literally satisfy the historical high-extent-Wind description.

## Why these are world concepts rather than roots

The productive language already has the reusable machinery needed to state facts about these things: Matter/phase, Region/Path, Extent/Area/Distance, In/At/Touch/Overlap, Move/Fall/Change, Distribution/Rate, Heat, and general event/state logic.

River, Mountain, Forest, Cloud, Rain, etc. are recognized categories of world features or phenomena. Their exact membership is world ontology. Adding them as base runes would confuse common vocabulary with irreducible semantics.

## Geographic feature Entities and Regions

Geographic features are modeled as feature Entities whose occupied space is available through `Extent(feature) -> Region`.

This lets an individual river or mountain keep persistent identity, Kind membership, Parts, history, ownership/use relations, and a spatial extent at the same time. Proper names of specific geographic features should normally be New Names for the feature Entity when that identity matters. Purely spatial named areas may still be Region New Names.

This is a world-model convention, not a new grammar rule.

## Weather nouns do not become hidden process roots

Cloud, Rain, Snow, Wind, and Storm are weather-phenomenon Kinds. Checkpoint 112 does not add Rain/Wind/Storm Processes or a generic Flow root.

Existing semantics can describe a particular phenomenon's existence, location, extent, motion, falling, material, distribution, rate, and change. Creating or simulating weather magically still requires later world-execution physics: air/water distributions, velocity/flow models, heat/pressure/energy rules, thresholds, and RequiredPower.

A noun Old Name must not pretend to solve fluid dynamics.

## Elevation and direction

Mountain/Hill vocabulary does not require a new universal Elevation root. Exact vertical position and navigation can be grounded by world CoordinateFrames, Direction values, spatial references, and named reference levels. The historical High/Low/Extent elements are etymology only.

If later executable spatial work proves that coordinate-component/elevation access is independently missing, that should be audited as a semantic operation rather than smuggled in through geography vocabulary.

## Field is deferred

`Field` is deliberately moved to the food/agriculture batch. In ordinary civilization use it is primarily cultivated/open land-use vocabulary, not one universal natural feature.

## Deferred natural-world vocabulary

Checkpoint 112 does not automatically add valley, plain, desert, swamp/marsh, cave, spring, waterfall, glacier, volcano, cliff, beach, reef, current, fog/mist, hail, lightning, thunder, drought, or flood.

Those are not rejected. They remain evidence-driven candidates. Several are processes/conditions whose semantics should be audited before lexicalizing them.

## Semantic result

No new base semantic operation is required by this batch. There is no change to grammar, types, constructors, or callable frames.

## Inventory effect

Before checkpoint 112:

- 210 registered base entries;
- 129 semantic primitive candidates;
- 55 formal constructors;
- 263 semantic frames;
- 48 multi-frame entries;
- 115 Old Names;
- 108 core world concepts.

After checkpoint 112:

- **210 registered base entries**;
- **129 semantic primitive candidates**;
- **55 formal constructors**;
- **263 semantic frames**;
- **48 multi-frame entries**;
- **133 Old Names**;
- **126 core world concepts**.

Old Name meanings are now 126 concept/Kind Old Names, 6 Unit Old Names, and 1 parameterized expression Old Name.

## Next work

The next balanced civilization domain is **food/agriculture and common materials**.

That pass should include the deferred Field concept and audit seed, leaf, fruit, crop/grain, staple food, milk, salt, clay, cloth/textile, leather/hide, glass, fuel, and culturally important materials without assuming every English material noun belongs in the universal core.
