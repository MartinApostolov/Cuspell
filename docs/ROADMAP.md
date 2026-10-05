# Roadmap

_Status: current work only; completed milestones are archived_

## Current milestone — language stabilization

The semantic root-minimization sweep reached practical closure before checkpoint 106, but the civilization audit then exposed independently necessary meanings omitted by the reduced basis. Checkpoints 107–108 restore health/sex distinctions, checkpoint 114 adds objective rigid `Rotate`, and checkpoint 115 adds recognized social `Authority`. Checkpoint 118 performs the promised exact reduction test and retains `Authority`: current deontic, capability, control, rule, and causal facts do not determine recognized normative standing. Checkpoint 119 likewise re-tests and retains `Health`, `Pain`, and `Ill`: the generic Attribute/evaluation/sensing/world-Kind machinery operates on or classifies already identified meanings and does not reconstruct those three independent biological dimensions. Checkpoint 120 re-tests `Male`/`Female` and retains both positive persistent Properties: negation does not supply converse classification, a universal Sex attribute adds and overconstrains machinery, and current world-Kind predication would lose StateProposition/Begin/End semantics. Checkpoint 121 re-tests `Rotate` and retains it: the current geometry system has translation and spatial references but no separate Entity pose/orientation state, and a per-Part reconstruction would simply hide the rigid transform in constraints. Checkpoint 122 audits typed world-Kind `classifies_types` and retains it as the minimal category-domain mechanism while fixing binder typing and package validation and removing redundant explicit Entity metadata. Checkpoint 123 then re-audits parameterized expression Old Names and retains the mechanism as controlled historical lexical compression: Give stays reduced rather than returning as a root, `«TransferHave»` remains the sole current pilot, and frozen templates are now semantically compiled during registry validation. Checkpoint 124 completes the current surface-v0.8 reference reconciliation and adds drift guards for legacy syntax in current reference material. The current inventory is now **214 registered entries / 133 semantic primitive candidates** after checkpoint 129 adds fresh-identity `Create`. Current work is evidence-driven stabilization, not a blind deletion or noun-adding sweep.

### 1. Physical-measurement finding resolved

Checkpoint 126 closes the Pressure question raised by the seven-source pass.

Result:

- `Pressure` is a distinct scalar physical AttributeDescriptor because no existing semantic construction identifies the pressure field/value itself;
- `Quantity:Pressure` is **not** a new base dimension: it aliases the derived vector Mass · Length^-1 · Time^-2;
- no `PressureUnit` Old Name is required because a pressure quantity can be built dimensionally from the existing Mass/Length/Time units;
- matching a derived dimension does not make an arbitrary quantity the Pressure of an Entity or Location;
- world packages supply actual Pressure values, material behavior, gradients, and causal laws, but do not silently mint new callable semantic rune meanings;
- Force, Energy, charge, voltage, acceleration, etc. are **not** added speculatively. Each future candidate must still pass its own exact semantic/compositional test.

The pressure case therefore does not justify a generic world-registerable AttributeDescriptor macro system.

### 2. Civilization vocabulary status

The balanced civilization-vocabulary sweep through checkpoints 111–117 is complete, and checkpoints 118–123 completed its reduction/structural follow-up. The current inventory remains evidence-driven and may still change if the new book pass demonstrates a missing or redundant distinction.

### 3. Spell-focused beginner Cuspell v0.1 — active

Checkpoint 127 defines the first teaching subset around Cuspell's original purpose: writing spells.

Machine truth lives in `language/subsets/spellcraft_beginner_v0_1.json`; player teaching material lives in `player/BEGINNER_SPELLCRAFT.md`.

Current starter:

- **49** existing registered signs; checkpoint 130 adds `Matter` and `Create` to the teaching projection without changing the semantic inventory;
- `«HeatUnit»`, `«LightUnit»`, cat `«LowExtent«MoveLifeThing»»`, and arrow `«SharpMoveAttackThing»` as starter Old Names;
- command-final `!`, grouping, `@`, and only the binder machinery needed for triggered, multi-target, and fresh-result examples;
- **48** parser-validated analogous effects selected from SRD 5.1 level 0–2 spells.

The benchmark is effect diversity, not D&D compatibility. Spell slots, action economy, saving throws, attack rolls, damage dice, schools, and exact D&D conditions are not copied.

Important outcome: spell-first teaching excludes context-only `That` from executable starter examples because current magic requires objective references. It prefers `This`, `You`, `Self`, selected locations, and explicit binders.

Checkpoint 128 extends the spell corpus through SRD levels 3–9.

The main result is that high-level spell power does not require spell-name roots. Current Cuspell already covers large parts of:

- teleportation via flat concurrent At-state boundaries;
- state/control/memory/life/existence transitions;
- Trigger-based wards;
- capability grants;
- phase/Form changes;
- selected dispelling.

The canonical spell surface remains flat: `Concurrent EndAtSelfHere BeginAtSelfThere!` is parser-valid, and curated beginner spell examples are guarded against parentheses.

Checkpoint 129 resolves the first family: fresh identity generation is an independently necessary semantic Process, not `Begin Exist`.

`Create result-binder profile` now:

- allocates exactly one never-before-allocated Entity identity;
- scopes that fresh result through an objective Proposition profile and an optional immediate continuation EventSpec;
- permits a named Entity Kind as the binder domain;
- relies on the world generation layer only for deterministic physical realization;
- never implies random unspecified features, Life, Magic, control, ownership, or a default body/material.

Checkpoint 130 runs the promised post-Create starter re-audit. It fixes two accidental semantic collapses: Faerie Fire is now explicit group illumination rather than a duplicate of Light, and Magic Missile now allocates fresh projectile identities before moving them. It also adds a Find Familiar-like creation example and guards every remaining exact duplicate recipe as an intentional shared objective effect slice.

That pass also finds one real composition gap in checkpoint-129 Create: a profile-only binder cannot immediately participate in a later action. Create therefore gains an optional continuation EventSpec whose lexical scope includes the fresh result. No root or frame count is added.

Four reusable pressure families remain:

1. bounded acquisition of previously unknown Information;
2. persistent multi-observer illusion/representation;
3. generic magical-execution interception/suppression;
4. time-flow manipulation.

Next:

- audit bounded unknown-information acquisition/divination;
- then continue the remaining families one at a time rather than adding spell-specific roots;
- keep game-stat modifiers outside Cuspell unless an objective world meaning independently warrants them;
- test learnability with people in parallel.


### 4. Strengthen repository/player drift checks

Keep `player/` a projection, not a second source of truth.

Automate where practical:

- rune count/list agreement;
- Old Name list/cost agreement;
- current syntax-file uniqueness;
- repository layer invariants;
- broken internal-link checks.

### 5. Maintain ongoing targeted corpus pressure

After the immediate multi-book pass, continue using diverse corpus pressure periodically. A prose pass should become an executable regression when it exposes a real structural defect.

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
