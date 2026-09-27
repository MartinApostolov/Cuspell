# World Model Interface

_Status: working specification v0.1_

Cuspell's grammar should be portable across settings, but objective execution needs setting data.

## Core language responsibilities

The language core defines:

- semantic Categories and Traits;
- composition and sentence grammar;
- quantities and dimensions;
- reference and selection rules;
- Event/Command structures;
- mana accounting;
- execution-result categories.

## Setting responsibilities

A campaign/world package supplies the concrete ontology used by those rules.

### Materials

Register material Kinds, elements/substances, phase behavior, mixtures, and relevant physical attributes.

Examples can include Water, Iron, Stone, and setting-specific materials.

### Biology

Register organism/taxon Kinds, anatomy, developmental profiles, Life requirements, disease models, and heredity/lineage rules.

This supplies classifiers for Human, Wolf, Oak, Hand, Blood, etc.

### Mind model

State how Mind relates to biological Entities and identity.

The language does not force every setting to use the same metaphysics.

### Space and time

Register:

- geometry/metric;
- dimensionality;
- CoordinateFrame defaults;
- local Up rule;
- time ordering/resolution;
- calendar mappings if used.

### Units

For each measurement dimension, register:

- canonical internal Unit;
- conventional lexical Units;
- conversion rules.

### Physical behavior

Provide rules used to determine ordinary consequences of Events, such as motion, thermal transfer, phase changes, optics, acoustics, and structural behavior.

### Artifact/cultural Kinds

Register common designed Kinds and their classifiers, such as Tool, Door, House, Sword, or setting-specific technology.

Ordinary cultural names do not automatically become magical semantic roots.

## Magical capability package

The game rules declare which meaningful EventSpecs magic can realize.

This can include:

- supported Process families;
- creation/transformation restrictions;
- movement/teleport rules;
- information-access capabilities;
- persistence/trigger support;
- protected attributes/Kinds;
- accessible spatial/temporal domains.

A sentence can therefore be meaningful language but unsupported magic.

## RequiredPower

RequiredPower calibration belongs to the game/world rules rather than grammar.

It can depend on:

- mass/extent;
- distance;
- state-change size;
- resistance/stability;
- duration;
- target count;
- competing active Magic.

The rule must be documented/objective rather than decided from narrative impressiveness.

## Casting context

The activation environment supplies typed context values such as:

- Self;
- Here;
- Now;
- designated This;
- default CoordinateFrame;
- activation origin;
- accessible reference/search domain.

These are formal inputs, not interpretation guesses.

## Generation profiles

Kind entries may supply setting-specific:

- canonical generation profiles;
- transformation mappings;
- intact/healthy templates.

A bare Kind closes Create/Transform only when such data is sufficient.

## Hidden facts

The world state can contain objective facts unknown to characters.

Find/Sense/information-acquisition capability controls access to those facts.

Reference grammar does not grant automatic omniscience.

## Versioning

A running game should identify:

- Cuspell language/spec version;
- world-model version;
- magic/balance rules version.

This lets the grammar remain stable while a setting changes physics, biology, vocabulary, or balance constants.

## Result

Cuspell can have one formal semantic language while different settings provide concrete ontology and execution data through an explicit interface.
