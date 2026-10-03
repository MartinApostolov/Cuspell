# Roadmap

_Status: current work only; completed milestones are archived_

## Current milestone — language stabilization

The semantic root-minimization sweep reached practical closure before checkpoint 106, but the civilization audit then exposed independently necessary meanings omitted by the reduced basis. Checkpoint 107 restores `Health`, `Pain`, and `Ill`; checkpoint 108 adds positive `Male` alongside `Female`. The current inventory is **210 registered entries / 129 semantic primitive candidates**. Current work is evidence-driven stabilization, not a blind deletion or noun-adding sweep.

### 1. Finish current grammar/spec normalization

Bring the remaining current grammar documents and examples into agreement with surface v0.8 and the player-facing rules.

Required outcomes:

- no normative section teaches legacy leading mood as current syntax;
- no normative section teaches bracketed binders as current syntax;
- migrated noun roots are not used as current canonical examples;
- historical/test notation is clearly labeled when retained;
- `SequenceEnd` / `ConcurrentEnd` stay canonical linear closure;
- current specs do not point to archived files as if they were normative.

### 2. Expand civilization vocabulary in balanced domain batches

Checkpoints 107–110 resolve the structural findings from the civilization audit:

- health/pain/illness distinctions are explicit;
- Male/Female are positive biological classifiers rather than negated converses;
- referenced TimeIntervals expose Begin/End/finite Extent;
- exact pre-magic compositional verbs/relations may use **typed parameterized expression Old Names** without becoming semantic roots or modern user macros.

Checkpoint 110 pilots the mechanism with `«TransferHave»` = give. Parameterized Old Names currently use required typed positional parameters only; they are lexically scoped and cannot capture caller binders.

The next work is **balanced historical vocabulary expansion**, not another structural grammar pass.

Start with **basic anatomy**, then continue:

- natural geography and weather;
- food/agriculture and common materials;
- craft/manufacturing and land transport;
- war/public institutions;
- art/ritual/shared culture;
- calendar/daily-life vocabulary.

For every candidate, classify it before adding anything: compositional only, Old Name candidate, New Name category, semantic-language gap, or world-model concept. Species, specific materials, named institutions, cultural calendars, technologies, and setting-specific magical terms should remain world-package concepts/New Names where appropriate.

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
