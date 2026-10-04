# Roadmap

_Status: current work only; completed milestones are archived_

## Current milestone — language stabilization

The semantic root-minimization sweep reached practical closure before checkpoint 106, but the civilization audit then exposed independently necessary meanings omitted by the reduced basis. Checkpoints 107–108 restore health/sex distinctions, checkpoint 114 adds objective rigid `Rotate`, and checkpoint 115 adds recognized social `Authority`. Checkpoint 118 performs the promised exact reduction test and retains `Authority`: current deontic, capability, control, rule, and causal facts do not determine recognized normative standing. Checkpoint 119 likewise re-tests and retains `Health`, `Pain`, and `Ill`: the generic Attribute/evaluation/sensing/world-Kind machinery operates on or classifies already identified meanings and does not reconstruct those three independent biological dimensions. Checkpoint 120 re-tests `Male`/`Female` and retains both positive persistent Properties: negation does not supply converse classification, a universal Sex attribute adds and overconstrains machinery, and current world-Kind predication would lose StateProposition/Begin/End semantics. Checkpoint 121 re-tests `Rotate` and retains it: the current geometry system has translation and spatial references but no separate Entity pose/orientation state, and a per-Part reconstruction would simply hide the rigid transform in constraints. Checkpoint 122 audits typed world-Kind `classifies_types` and retains it as the minimal category-domain mechanism while fixing binder typing and package validation and removing redundant explicit Entity metadata. The current inventory remains **212 registered entries / 131 semantic primitive candidates**. Current work is evidence-driven stabilization, not a blind deletion or noun-adding sweep.

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

Checkpoint 111 completes **basic anatomy**, checkpoint 112 the first **natural geography/weather** batch, and checkpoint 113 **food/agriculture/common materials**.

Checkpoint 114 completes **craft/manufacturing and land transport** with twenty-two world Kinds + Old Names and adds objective rigid `Rotate`.

Checkpoint 115 completes the first **war/public-institutions** batch with thirteen world Kinds + Old Names and adds `Authority(holder,scope)` as a productive social Relation. Checkpoint 118 later re-audits that addition and retains it as irreducible recognized normative standing rather than a synonym for permission.

Checkpoint 116 completes **art/ritual/shared culture** with sixteen world Kinds + Old Names and generalizes registered world Kinds to explicit classified-value types.

Checkpoint 117 completes the planned **calendar/daily-life** batch with six world Kinds + Old Names: day/calendar day, night, season, year, month/calendar month, and date/calendar date. Day/Night/Season/Year/Month classify `TimeInterval`; Date classifies `Information`. No new semantic root, type, or frame is needed.

Age remains compositional as elapsed temporal extent from an explicitly chosen birth/creation/start point to a reference point. Weeks, named eras, hours/minutes, holidays, and specific calendar systems remain world/history vocabulary rather than universal core assumptions.

The planned balanced civilization-vocabulary sweep is now complete.

The productive-root portion of the dedicated **reduction/redundancy audit** is complete. Checkpoint 122 also closes the typed world-Kind `classifies_types` structural audit. Continue with the remaining recent structural mechanism: **parameterized expression Old Names** from checkpoint 110.

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
