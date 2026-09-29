# World package data

Cuspell keeps language semantics separate from world ontology.

Current machine-readable worldbuilding files:

- `core/concepts.json` — stable world concept identities and semantic types;
- `core/new_names.json` — current Name/reference relations.

Historical magical vocabulary is language history rather than current world state and lives in:

- `../language/names/old_names.json`

The default registries are populated only from explicit worldbuilding/corpus pressure rather than by pre-generating an English dictionary.

See `docs/spec/NAMES_AND_WORLDBUILDING.md`.

The first broad seed is documented in `docs/world/FIRST_CIVILIZATION_VOCABULARY.md` and provides 62 stable world concepts plus matching Old Names. The audited Yona vocabulary passes plus the later historical monster/divine/mana/meditation pass add 28 more ordinary core concepts/Old Names, bringing the core registry to 90. Their classifiers remain explicit future world-ontology work rather than being guessed by the language layer.

## Optional setting packages

World-specific vocabulary should not be dumped into `world/core`.

A setting package may provide:

- `world/<package>/concepts.json`
- `world/<package>/new_names.json`

and can be loaded with:

`Language.load(root, world_package="<package>")`

The first package is `world/yona`, covering New Names and world concepts exposed by the audited Yona chapters. It currently contains 318 concepts and 329 New Name entries through numbered Chapter 168, including later Dungeon/System ontology, ranks, Epithets, Named types, Titles, Soul Weapons, Classes, Professions, species/evolution labels, Event rewards and exact source-visible Skill progression. See `docs/world/YONA_PUBLISHED_THROUGH_168_VOCABULARY.md`.
