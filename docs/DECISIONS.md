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

## Canonical surface is flat Cuspell v0.7

Normal Cuspell should look like a foreign language, not a printed AST.

- sentence-final `.`, `?`, and `!` mark assertion, question, and command;
- heads normally precede their arguments;
- typed frames resolve flat left-to-right application;
- adjacency may form a registered lexical compound or one uniquely typed tight local application;
- ambiguity is rejected rather than guessed;
- parentheses and pipe are fallback/debug grouping, not the normal visual style.

Older surface forms remain parser-compatible only where current tests intentionally preserve them.

## Sequence and Concurrent stay language-like

`Sequence E1 E2 ...` and `Concurrent E1 E2 ...` are flat variadic constructions.

Sentence end closes the group. If later sentence material must follow, `SequenceEnd` or `ConcurrentEnd` closes it first. These are canonical zero-mana grammatical boundary markers and are retained specifically to avoid requiring pseudocode-style tree notation in normal prose.

## Argument omission is not inference

Every Relation and Process has registered frames. Required roles must be present. Optional roles may be omitted, but omission means unspecified/unconstrained, not “infer what the caster wanted.” Named role markers may supply skipped or explicit optional roles.

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

Checkpoint 95 closed the global reduction sweep at **205 registered base entries** and **125 semantic primitive candidates**, with **0 unresolved** and **0 derived** candidates.

Further semantic deletion is evidence-triggered, not sweep-driven. A root should be reopened only when a concrete exact replacement preserves its full truth conditions, typing, and execution closure.

## Current project phase is language stabilization

Before glyph design or game/world execution becomes primary work, Cuspell should have:

- one clean current repository layout;
- one clean player-facing grammar;
- current specs that agree with the parser;
- targeted review of multi-frame lexical irregularity;
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
