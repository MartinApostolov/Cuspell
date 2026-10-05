# Roadmap

_Status: current work only; completed milestones are archived_

## Current milestone — language stabilization

The semantic root-minimization sweep reached practical closure before checkpoint 106, but the civilization audit then exposed independently necessary meanings omitted by the reduced basis. Checkpoints 107–108 restore health/sex distinctions, checkpoint 114 adds objective rigid `Rotate`, and checkpoint 115 adds recognized social `Authority`. Checkpoint 118 performs the promised exact reduction test and retains `Authority`: current deontic, capability, control, rule, and causal facts do not determine recognized normative standing. Checkpoint 119 likewise re-tests and retains `Health`, `Pain`, and `Ill`: the generic Attribute/evaluation/sensing/world-Kind machinery operates on or classifies already identified meanings and does not reconstruct those three independent biological dimensions. Checkpoint 120 re-tests `Male`/`Female` and retains both positive persistent Properties: negation does not supply converse classification, a universal Sex attribute adds and overconstrains machinery, and current world-Kind predication would lose StateProposition/Begin/End semantics. Checkpoint 121 re-tests `Rotate` and retains it: the current geometry system has translation and spatial references but no separate Entity pose/orientation state, and a per-Part reconstruction would simply hide the rigid transform in constraints. Checkpoint 122 audits typed world-Kind `classifies_types` and retains it as the minimal category-domain mechanism while fixing binder typing and package validation and removing redundant explicit Entity metadata. Checkpoint 123 then re-audits parameterized expression Old Names and retains the mechanism as controlled historical lexical compression: Give stays reduced rather than returning as a root, `«TransferHave»` remains the sole current pilot, and frozen templates are now semantically compiled during registry validation. Checkpoint 124 completes the current surface-v0.8 reference reconciliation and adds drift guards for legacy syntax in current reference material. The current inventory is now **217 registered entries / 136 semantic primitive candidates** after checkpoint 134 adds explicit relative `TimeFlow`. Current work is evidence-driven stabilization, not a blind deletion or noun-adding sweep.

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

### 3. Spell-focused beginner Cuspell v0.2 — active

Checkpoint 135 separates **teaching** from **coverage**.

Current machine truth for the actual first lesson lives in `language/subsets/spellcraft_beginner_v0_2.json`; player teaching material lives in `player/BEGINNER_SPELLCRAFT.md`.

Current beginner core:

- **16 registered signs**, introduced cumulatively at 6 / 9 / 11 / 16 signs;
- one starter Old Name, `«LightUnit»`;
- command-final `!`, `@`, and exactly one fresh-Entity binder pattern;
- 12 parser-validated Cuspell-first starter spells;
- no `And`, `Repeat`, `Concurrent`, `Each`, `Collect`, `Member`, `Trigger`, `Persist`, `Prevent`, `Represent`, or `TimeFlow` in lesson one.

The retained `language/subsets/spellcraft_beginner_v0_1.json` file is now explicitly a **50-sign coverage projection**, with player reference in `player/SPELLCRAFT_COVERAGE.md`. Its 48 SRD level-0-to-2 analogues remain a stress test for effect diversity rather than a learning target.

The active beginner selection rule is Cuspell complexity, not D&D spell level. The first progression teaches immediate movement, Begin/End state transitions, simple yes/no `Find`, and one fresh-`Create` continuation pattern.

Checkpoint 135 also corrects Light: the desired spell creates a new light source rather than changing a pre-existing target. The canonical beginner example is `Create x:Entity At $x Here Change $x Light «LightUnit» @!`.

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

Checkpoint 130 runs the promised post-Create starter re-audit. It fixes two accidental semantic collapses: Faerie Fire now illuminates an objectively collected Group membership set rather than duplicating Light or relying on contextual `They`, and Magic Missile now allocates fresh projectile identities before moving them. It also adds a Find Familiar-like creation example and guards every remaining exact duplicate recipe as an intentional shared objective effect slice.

That pass also finds one real composition gap in checkpoint-129 Create: a profile-only binder cannot immediately participate in a later action. Create therefore gains an optional continuation EventSpec whose lexical scope includes the fresh result. No root or frame count is added.

Checkpoint 131 resolves the second family: bounded acquisition of previously unknown Information is an independently necessary semantic Process rather than a side effect of Question, Sense, Collect, Infer, Know, If, Trigger, or reference resolution.

`Find mind scope proposition` performs a factive yes/no acquisition.

`Find mind scope binder proposition` performs a factive open-query acquisition.

The explicit scope must participate in the query, and every otherwise unavailable information dependency must be licensed by that scope/world capability. Successful false/empty answers are distinct from blocked or incomplete access.

Checkpoint 132 resolves the third family. Persistent shared illusion is built from an objective `Represent(carrier,content,channel)` StateProposition plus existing `Create`, `Persist`, `Trigger`, movement, and state-transition machinery. A fresh representation carrier need not be Matter, so visual/auditory projections do not silently become solid physical objects.

Checkpoint 133 resolves the fourth family without a new root. Magical EventSpec/Event provenance is exposed through typed `Magic` frames, and `Prevent` gains a bound EventSpec matcher evaluated before commit with optional Region footprint scope. Counterspell/Antimagic-style effects are therefore generic execution interception rather than spell-name semantics.

Checkpoint 134 resolves the fifth and final checkpoint-128 pressure family with `TimeFlow(subject,reference,rate)`: an explicit nonnegative relative temporal-progression state for Entity/Region subjects. It is not event frequency, Repeat, Prevent, or action-economy metadata.

All five reusable advanced spellcraft gaps from checkpoint 128 are now structurally closed:

1. fresh generation -> `Create`;
2. bounded unknown-information acquisition -> `Find`;
3. persistent shared representation -> `Represent`;
4. generic execution interception -> typed `Magic` + bound `Prevent`;
5. time-flow manipulation -> `TimeFlow`.

Checkpoint 135 completes that redesign.

The actual first teaching progression is now **16 signs**, introduced cumulatively at 6 / 9 / 11 / 16 signs:

- first actions: `This There Move Begin End Whole`;
- explicit target/condition: `You Locked Ill`;
- bounded yes/no discovery: `Self Find`;
- creation/light: `Here At Create Change Light`.

The old 50-sign set remains as a broad SRD coverage projection, not lesson one.

Light is now correctly in the creation family:

`Create x:Entity At $x Here Change $x Light «LightUnit» @!`

while `Change This Light «LightUnit» @!` remains the distinct operation of making an already-existing target luminous.

Next:

- stress-test the 16-sign progression for learnability and hidden prerequisites;
- build small optional follow-on modules instead of enlarging the first set;
- keep game-stat modifiers outside Cuspell unless an objective world meaning independently warrants them.


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
