# World package data

Cuspell keeps language semantics separate from world ontology.

Current machine-readable worldbuilding files:

- `core/concepts.json` — stable world concept identities and semantic types;
- `core/new_names.json` — current Name/reference relations.

Historical magical vocabulary is language history rather than current world state and lives in:

- `../language/names/old_names.json`

The default registries are intentionally empty. Populate them from corpus/worldbuilding needs rather than pre-generating an English dictionary.

See `docs/spec/NAMES_AND_WORLDBUILDING.md`.

The first broad seed is documented in `docs/world/FIRST_CIVILIZATION_VOCABULARY.md` and currently provides 62 stable world concepts plus matching Old Names. Their classifiers remain explicit future world-ontology work rather than being guessed by the language layer.
