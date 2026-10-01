# Core Historical Vocabulary

_Status: current maintainer index; machine-readable Old Name registry is normative_

The original first-civilization vocabulary pass has been archived at `archive/world/FIRST_CIVILIZATION_VOCABULARY_PRE_CP98.md` because it accumulated superseded root names and historical spellings during minimization.

Current machine truth for established core vocabulary is:

- `language/names/old_names.json` — Old Name signs, historical name units, meanings, and dependencies;
- `world/core/concepts.json` — referenced world concepts/classifiers;
- `language/core/units.json` — typed Unit metadata for Unit-valued Old Names.

The player-facing list is generated/checked in `player/names/OLD_NAMES.md`.

## Current scope

The core Old Name registry contains **102 entries**:

- **96 concept/Kind Old Names**;
- **6 canonical Unit Old Names**.

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
