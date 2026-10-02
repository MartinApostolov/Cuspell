# Roadmap

_Status: current work only; completed milestones are archived_

## Current milestone — language stabilization

The semantic root-minimization sweep reached practical closure before checkpoint 106, but the civilization audit then exposed independently necessary meanings omitted by the reduced basis. Checkpoint 107 restores `Health`, `Pain`, and `Ill`, bringing the current inventory to **209 registered entries / 128 semantic primitive candidates**. Current work is evidence-driven stabilization, not a blind deletion or noun-adding sweep.

### 1. Finish current grammar/spec normalization

Bring the remaining current grammar documents and examples into agreement with surface v0.8 and the player-facing rules.

Required outcomes:

- no normative section teaches legacy leading mood as current syntax;
- no normative section teaches bracketed binders as current syntax;
- migrated noun roots are not used as current canonical examples;
- historical/test notation is clearly labeled when retained;
- `SequenceEnd` / `ConcurrentEnd` stay canonical linear closure;
- current specs do not point to archived files as if they were normative.

### 2. Resolve civilization-vocabulary structural findings

Checkpoint 107 resolves the health-state finding: `Health`, `Pain`, `Ill`, `Damage`, and `Life` now remain explicitly independent, while Heal stays compositional.

Before adding large Old Name batches, resolve the remaining checkpoint-106 issues that affect how later vocabulary should be modeled:

- provide a positive, symmetric biological-sex classification path instead of relying on `Female` plus negation;
- generalize existing `Begin`, `End`, and `Extent` semantics so an already-referenced `TimeInterval` can expose its boundaries/duration without reconstructing its original constructor;
- decide whether common pre-magic parameterized verbs/relations such as buy/sell/read/write/pray remain transparent multi-rune compositions or can participate in a safe historical lexicalization mechanism without becoming arbitrary player macros.

Then expand Old Names by **balanced civilization domains**, not by translating an English noun list. First candidate batches should emphasize:

- basic anatomy;
- natural geography and weather;
- food/agriculture and common materials;
- craft/manufacturing and land transport;
- war/public institutions;
- art/ritual/shared culture;
- calendar/daily-life vocabulary.

Species, specific materials, named institutions, cultural calendars, technologies, and setting-specific magical terms should remain world-package concepts/New Names where appropriate.

### 3. Define beginner Cuspell

Build a deliberately small teaching subset:

- minimum writing rules;
- a useful starter rune set;
- basic Old Names;
- examples that let a player cast useful effects without advanced binders, selectors, or mathematics.

Then test actual learnability with people rather than estimating it only from rule count.

### 4. Strengthen repository/player drift checks

Keep `player/` a projection, not a second source of truth.

Automate where practical:

- rune count/list agreement;
- Old Name list/cost agreement;
- current syntax-file uniqueness;
- repository layer invariants;
- broken internal-link checks.

### 5. Continue targeted corpus pressure

New corpus work should be diverse and evidence-driven. A prose pass should become an executable regression when it exposes a real structural defect.

Do not re-open general grammar simply because one source has unusual wording.

## Later milestone — glyph/rune system

Only after the player-facing writing system is stable enough:

- design root glyph families;
- map grammatical case/grouping/binders visually;
- test legibility and confusion risk;
- ensure every written form maps uniquely to the same semantic structures;
- create font/assets if useful.

Glyph aesthetics must not alter semantics.

## Later milestone — game/world execution

After the language is deliberately frozen enough and an actual game/use case supplies requirements:

- concrete world classifiers/physics;
- generation/transformation profiles;
- magic capability restrictions;
- RequiredPower computation/calibration;
- resistance and execution behavior.

## Later milestone — player/GM supplement

Produce final teaching/reference material from the stable `player/` layer:

- quick start;
- rune dictionary;
- grammar;
- spell construction;
- examples;
- progression/learning;
- world integration;
- diagnostics/troubleshooting.

## Working rule

Do not treat completed history as current work. Archive completed passes and keep this file limited to unresolved/current priorities.
