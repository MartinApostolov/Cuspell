# Core Historical Vocabulary

_Status: current maintainer index; machine-readable Old Name registry is normative_

The original first-civilization vocabulary pass has been archived at `archive/world/FIRST_CIVILIZATION_VOCABULARY_PRE_CP98.md` because it accumulated superseded root names and historical spellings during minimization.

Current machine truth for established core vocabulary is:

- `language/names/old_names.json` — Old Name signs, historical name units, meanings, and dependencies;
- `world/core/concepts.json` — referenced world concepts/classifiers;
- `language/core/units.json` — typed Unit metadata for Unit-valued Old Names.

The player-facing list is generated/checked in `player/names/OLD_NAMES.md`.

## Current scope

The core Old Name registry contains **115 entries**:

- **108 concept/Kind Old Names**;
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

The 115-entry registry is a **foundation**, not a declaration that the historical civilization vocabulary is complete.

Checkpoint 106's systematic coverage audit finds that the language can already express most civilization-scale distinctions through roots + composition + Names, but the established Old Name list is uneven because it grew partly under corpus pressure. Examples of the imbalance include:

- Checkpoint 111 corrects the earlier anatomy imbalance: Head, Face, Arm, Leg, Foot, Finger, Nose, Tooth, Tongue, Heart, Brain, and Hair now join the pre-existing Body/Hand/Eye/Ear/Mouth/Skin/Bone/Flesh/Blood/Organ/Stomach/Wrist/Tendon/Wound layer;
- Spoon is named while basic cooking/craft tools such as Knife, Pot, and Needle are not;
- Sailor, Crew, and Captain are named while ordinary land/military vocabulary is sparse;
- Scent Trail and several fantasy/religious concepts are named while River, Rain, Wind, Forest, and broad art/music vocabulary are absent.

This is not evidence that the existing names should be removed. It means future additions should be audited in **domain batches** rather than chosen randomly.

High-priority historical-vocabulary families are currently:

- natural geography/weather;
- agriculture/common materials;
- craft/manufacturing/land transport;
- war/public institutions;
- art/ritual/shared culture;
- calendar/daily life.

Not every concept in those families should become an Old Name. Keep a concept compositional when its description is short and natural; use world-package concepts/New Names for setting-specific species, technologies, institutions, materials, ranks, proper places, and similar local vocabulary.

The complete checkpoint-106 reasoning is preserved historically in `archive/audits/cp106_CIVILIZATION_VOCABULARY_COVERAGE_AUDIT.md`. Checkpoint 111 is the first balanced domain expansion and intentionally changes the accepted machine-readable registry to 115 Old Names.

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
