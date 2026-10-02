# Active Cuspell Decisions

_Status: current cross-spec design invariants. Historical decision log through D-179 is archived at `archive/decisions/DECISIONS_D001_D179.md`._

This file contains only decisions that a maintainer should treat as **currently active**. Detailed semantics live in `docs/spec/`; this file is a compact set of cross-cutting rules that should not silently regress.

## Language purpose

Cuspell is a formal, compositional language for objective freeform magic. A valid magical command must have a mechanically determinable meaning rather than rely on what the caster or GM probably intended.

## Language and magic are separate layers

A sentence may be grammatically and semantically valid without being magically executable. Parsing, typing, semantic closure, reference resolution, world capability, RequiredPower, and resource payment remain separate checks.

## Mana follows written meaning-bearing signs

Every meaning-bearing rune/sign occurrence written in a magical command costs mana. Pure grammatical structure may cost zero. Semantic normalization does not refund written cost.

Legitimate registered linguistic compression may reduce mana. Arbitrary player-created aliases/New Names do not become free magical macros.

## Canonical surface is flat Cuspell v0.8

Normal Cuspell should look like a foreign language, not a printed AST.

- sentence-final `.`, `?`, and `!` mark assertion, question, and command;
- heads normally precede their arguments;
- typed frames resolve flat left-to-right application;
- adjacency may form a registered lexical compound or one uniquely typed tight local application;
- ambiguity is rejected rather than guessed;
- parentheses are the explicit player-facing fallback for grouping when flat typing/tight adjacency are insufficient;
- pipe hard-binding is parser/debug and historical compatibility only, not player-facing Cuspell.

Older surface forms remain parser-compatible only where current tests intentionally preserve them.

Checkpoint 104 closes the grouping-policy question: pipe adds no semantic capability beyond tight adjacency plus parentheses, so keeping it player-facing would create a second binding system to learn without increasing expressive power.

## Sequence and Concurrent stay language-like

`Sequence E1 E2 ...` and `Concurrent E1 E2 ...` are flat variadic constructions.

Sentence end closes the group. If later sentence material must follow, `SequenceEnd` or `ConcurrentEnd` closes it first. These are canonical zero-mana grammatical boundary markers and are retained specifically to avoid requiring pseudocode-style tree notation in normal prose.

## Argument omission is not inference

Every Relation and Process has registered frames. Required roles must be present. Optional roles may be omitted, but omission means unspecified/unconstrained, not “infer what the caster wanted.”

Checkpoint 103 removes English `:role` selectors from current Cuspell. Optional arguments are positional. A trailing optional slot may simply be absent; `_` advances over exactly one optional slot when a later slot or outer argument must follow. `_` costs zero mana because it carries no role identity or world meaning. It is invalid for required slots. Internal frame labels such as source, authority, context, and instrument are implementation/specification metadata only.

## Types carry most grammatical regularity

Multiple typed frames are allowed only when they instantiate a coherent semantic core. Different English meanings that merely share a label should not be hidden as one rune.

The parser never chooses a reading because it sounds more plausible.

## Negation, zero, opposites, and converse remain distinct

`Not`, numeric `Zero`, and typed `Opposite` are separate operations. Relation converse is expressed by writing the same underlying relation with its actual roles/arguments in the intended order rather than by a generic Converse rune.

## Names are layered

- semantic roots and formal constructors belong to the language;
- world concepts provide stable identities/classifiers for ordinary concepts;
- Old Names are historically established vocabulary with frozen name-unit cost;
- New Names are ordinary naming/reference relations and do not gain magical macro power.

Draft Old Names remain redesignable while the language is not frozen.

## Current semantic inventory is reduction-closed for now

Checkpoint 95 closed the global reduction sweep at **205 registered base entries** and **125 semantic primitive candidates**, with **0 unresolved** and **0 derived** candidates. Checkpoint 100 temporarily added `Interpret`; checkpoint 101 superseded it and returned the totals to **205 / 125**. Checkpoint 105 deliberately restores `Almost` as a formal constructor after proving the attempted boundary-Distance reduction semantically invalid. Checkpoint 107 restores three independently necessary civilization/body-state distinctions—`Health`, `Pain`, and `Ill`—after checkpoint 106 showed they are not exactly reducible to `Damage`, `Life`, or each other. Checkpoint 108 adds positive `Male` alongside `Female` rather than treating logical negation as a biological converse. Current totals are **210 registered entries / 129 semantic primitive candidates / 55 formal constructors**.

Further semantic deletion or addition is evidence-triggered, not sweep-driven. Exact semantics outrank minimizing the raw root count, but a new root should not survive when an existing general construction can preserve the same distinctions.

## Health-state distinctions remain independent

Checkpoint 107 treats `Damage`, `Health`, `Pain`, `Ill`, and `Life` as distinct meanings.

- `Damage` is ordered physical injury/damage.
- `Health` is ordered overall biological functional condition.
- `Pain` is ordered experienced pain/nociceptive suffering.
- `Ill` is a persistent pathological-state Property.
- `Life` is the biological alive/living state.

Do not derive one from another by default. A world model may correlate them, but Cuspell must permit damage without pain, pain without damage, illness with little damage, low health without illness, and similar combinations.

There is no standalone `Heal` root. Healing/recovery must state the actual result, such as reducing Damage, ending Ill, improving Health, restoring structure, or an explicit combination.

## Biological sex uses positive classifiers, not negated converse

`Male` and `Female` are independent positive biological-sex Properties.

Neither is defined as logical negation of the other. The core language does not declare them universally exhaustive or mutually exclusive; exact biological classification rules belong to the world ontology.

These roots are biological classifiers, not a universal social-gender system. Do not overload them with every cultural identity, role, or title.

## Multi-frame overloads must preserve one semantic core

Checkpoint 99 audited all 51 entries that were multi-frame at checkpoint 98.

- 33 are straightforward same-operation typed generalizations;
- 15 contain contextual or shorthand forms of the same operation;
- checkpoint 99 found 3 lexical semantic boundary crossings: `Distance`, `Sense`, and `Name`.

Checkpoint 100 resolves the hidden `Sense` overload: `Sense` now has only the explicit-channel sensory-acquisition frame. Checkpoint 101 supersedes the temporary `Interpret` root by keeping the underlying pieces explicit: `Meaning` supplies the real Sign-to-content relation, `Understand` supplies comprehension of that mapping, `Sense` supplies perception, and `Begin Understand` remains distinct when a new mapping is actually learned.

Checkpoint 101 also resolves `Name`. `Name` now has only its nonfunctional naming-relation frame. Inverse relation lookup uses the existing `Collect` + `Unique` construction, with `Collect` generalized to preserve the binder's semantic type. This mechanism is general: it can select an Entity named by a Sign, a Region named by a Sign, or Information uniquely related by `Meaning` without pretending those relations are globally functions.

Checkpoint 105 resolves the remaining `Distance` irregularity. Physical `Distance` is spatial-only and returns Length. Contextual near-satisfaction/near-occurrence is represented by the distinct `Almost` operator. `Almost` has Proposition and EventSpec frames with one semantic core, so **no genuine multi-frame lexical irregularity remains** from the checkpoint-99 audit.

New overloads should be accepted only when their frames share one semantic core.

An optional role does not by itself justify a second frame. `GratefulTo` uses one frame with an optional positional basis value; omission is handled by the general frame/omission grammar.

## Referenced TimeIntervals expose their own boundaries and finite extent

`Begin`, `End`, and `Extent` apply to `TimeInterval` as well as their existing Event/state meanings.

- `Begin(TimeInterval) -> TimePoint`;
- `End(TimeInterval) -> TimePoint`;
- finite `Extent(TimeInterval) -> Quantity:Time`.

This lets named/referenced intervals be inspected without reconstructing the syntax that originally created them.

For explicitly unbounded intervals, missing boundaries or non-finite duration are unavailable values; Cuspell does not invent a boundary or finite Quantity.

## Inverse relation selection is explicit

Relations such as `Name` and `Meaning` remain nonfunctional. To obtain a value from the inverse direction, bind the desired type, `Collect` values satisfying the relation, then apply `Unique` only when exactly one value is objectively available under the stated constraints. This is selection over a relation, not a hidden function frame.

## Current project phase is language stabilization

Before glyph design or game/world execution becomes primary work, Cuspell should have:

- one clean current repository layout;
- one clean player-facing grammar;
- current specs that agree with the parser;
- stable regression/corpus coverage.

## Repository layers are deliberately separated

Checkpoint 98 establishes a repository invariant:

- current machine truth lives in `language/` and `world/`;
- current maintainer/design truth lives in `docs/` and `docs/spec/`;
- current executable regression truth lives in `tests/`;
- player/PC reference lives in `player/` and must remain a checked projection of current truth;
- superseded snapshots, completed audits, historical corpus passes, old syntax/test fixtures, and the long decision history live in `archive/`.

Do not put completed audit snapshots back into the current-doc root merely because they are useful history. Preserve them in the archive and summarize only their current consequences in state/decisions/specs.

## Source-of-truth boundary

Current truth lives in `language/`, `world/`, `docs/spec/`, this file, `docs/CURRENT_STATE.md`, and executable `tests/`.

`player/` is a player-facing projection of current truth and must not invent semantics.

`archive/` is historical evidence only. If archive material conflicts with current files, the current files win.
