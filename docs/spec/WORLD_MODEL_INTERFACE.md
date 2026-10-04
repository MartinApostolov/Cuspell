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
- calendar mappings if used;
- objective membership/boundaries for Day, Night, Season, Year, Month, and other setting period Kinds;
- Date/era/calendar Information mappings to TimePoints/TimeIntervals;
- conventional time Units separately from calendar-period categories.

A world may omit Months, Seasons, Weeks, or other period families entirely. Calendar categories do not silently impose Earth durations or astronomy.

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

### Social and institutional authority

Register the world facts that make `Authority(holder,scope)` objectively true or false:

- jurisdiction/scope;
- source of authority;
- delegation;
- succession/appointment;
- revocation;
- conflicts or precedence;
- institutional recognition.

The language supplies the Authority relation; the setting supplies what counts as recognized authority. Factual Control alone is not a substitute.

### Typed world-category classifiers

World `Kind` concepts may declare explicit `classifies_types` metadata.

The default remains `["Entity"]`. A setting may register a Kind that instead classifies:

- Events/EventSpecs;
- Information;
- or another explicit known semantic type when the ontology genuinely requires it.

For example, ritual and festival categories classify Event/EventSpec values, story and musical-composition categories classify Information, and calendar-period categories classify TimeInterval.

The setting supplies the objective classifier; the language/parser enforces the registered target type. Do not broaden a category to `SemanticValue` merely for convenience.

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

A bare Kind is never an implicit fresh-generation instruction. Any future/world generation or transformation operation using a Kind is closed only when its registered profile/mapping makes the requested result deterministic enough for execution.

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
