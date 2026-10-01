# Roadmap

_Status: current work only; completed milestones are archived_

## Current milestone — language stabilization

The semantic root-minimization sweep has reached practical closure at **205 registered entries / 125 semantic primitive candidates**. Current work is no longer a blind deletion sweep.

### 1. Finish current grammar/spec normalization

Bring the remaining current grammar documents and examples into agreement with surface v0.7 and the player-facing rules.

Required outcomes:

- no normative section teaches legacy leading mood as current syntax;
- no normative section teaches bracketed binders as current syntax;
- migrated noun roots are not used as current canonical examples;
- historical/test notation is clearly labeled when retained;
- `SequenceEnd` / `ConcurrentEnd` stay canonical linear closure;
- current specs do not point to archived files as if they were normative.

### 2. Resolve player-facing grouping policy

Decide whether pipe remains:

- an advanced player-facing hard-binding device; or
- parser/debug compatibility only.

Parentheses may remain an explicit fallback either way. The decision should preserve the flat-language goal and avoid making normal Cuspell look like pseudocode.

### 3. Resolve the three remaining multi-frame lexical irregularities

Checkpoint 99 audited all 51 checkpoint-98 multi-frame entries. Only three roots still cross a genuine lexical semantic boundary:

- `Sense` — raw channel-based perception versus the contextual interpreted-Sign form inherited from the former Read meaning;
- `Name` — nonfunctional naming relation versus contextual one-argument inverse reference resolution;
- `Distance` — physical/general metric Length versus contextual Property/EventSpec boundary-distance EvaluationValue.

Resolve these deliberately rather than reopening a global reduction sweep.

Required outcomes:

- preserve current compatibility until replacement syntax/semantics and migrations are executable;
- prefer composition or a clearly distinct lexical operation when the truth conditions differ;
- keep reference resolution deterministic rather than making `Name` globally functional;
- decide whether boundary-distance deserves its own operation or an explicit generic metric abstraction;
- update player advanced grammar after each redesign.

### 4. Define beginner Cuspell

Build a deliberately small teaching subset:

- minimum writing rules;
- a useful starter rune set;
- basic Old Names;
- examples that let a player cast useful effects without advanced binders, selectors, or mathematics.

Then test actual learnability with people rather than estimating it only from rule count.

### 5. Strengthen repository/player drift checks

Keep `player/` a projection, not a second source of truth.

Automate where practical:

- rune count/list agreement;
- Old Name list/cost agreement;
- current syntax-file uniqueness;
- repository layer invariants;
- broken internal-link checks.

### 6. Continue targeted corpus pressure

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
