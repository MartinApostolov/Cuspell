# Checkpoint 124 — Surface v0.8 Current-Reference Reconciliation

_Status: language-stabilization reference cleanup_

## Purpose

Checkpoint 103 established canonical surface v0.8 and checkpoints 104–105 finalized grouping and remaining lexical surface policy.

Later semantic/vocabulary work correctly used the new surface in most player material, but the current maintainer/spec layer still contained a few stale examples and one stale machine-metadata claim.

Checkpoint 124 performs the planned current-reference reconciliation before the next corpus phase.

The target is **current truth only**:

- `docs/`;
- `docs/spec/`;
- `player/`;
- `language/syntax/surface_v0_8.json`;
- repository drift tests.

Historical examples under `archive/` remain historical evidence and are not rewritten.

Parser compatibility with older syntax also remains intentional. The purpose is not to delete compatibility parsing; it is to stop current reference material from teaching compatibility syntax as normal Cuspell.

## Canonical v0.8 invariants re-checked

Current player-facing syntax remains:

- sentence-final `.`, `?`, `!` mood/termination;
- head before typed positional arguments;
- tight adjacency for local application;
- infix spoken-order `And` / `Or`;
- flat `Sequence` / `Concurrent` event lists;
- `SequenceEnd` / `ConcurrentEnd` only when later material follows before the sentence boundary;
- genuine Collection values keep `{...}`;
- binders use `name:Domain`;
- variables use `$name`;
- optional positional slots use `_`;
- parentheses remain the player-facing explicit grouping fallback;
- pipe remains debug/legacy only.

The parser may continue accepting:

- leading `!` / `?` + final period;
- bracketed binders;
- collection-backed Sequence/Concurrent;
- pipe hard-binding;
- other explicitly preserved compatibility forms.

Those are not canonical examples.

## Stale current examples found

The audit found six genuine current-reference mismatches.

### Magical execution

`docs/spec/MAGIC_EXECUTION.md` still described a spell as:

`! EventSpec .`

This was the old leading-command surface.

It now states:

`EventSpec!`

and explicitly records that final `!` is both mood and terminator.

### Named role selectors

Checkpoint 103 removed free English `:role` selectors from current Cuspell, but four current spec references still used or described them as active:

- Distribution Transfer `:profile`;
- promise/obligation `:context`;
- GratefulTo `:basis`;
- Cause `:instrument`.

They are corrected to positional-v0.8 wording.

Where a later optional slot must be reached past an omitted earlier one, the ordinary omission marker is used.

Redistribution now shows:

`Transfer distribution source destination _ targetDistribution`

where `_` skips the optional amount before the optional profile.

Promise composition now shows the context as the ordinary third `Obligated` argument.

Cause's instrument is described as its optional third positional argument.

GratefulTo's historical frame cleanup is described as an optional positional basis rather than a named surface selector.

## Machine metadata mismatch

`language/syntax/surface_v0_8.json` already correctly specified:

- infix And/Or;
- flat Sequence/Concurrent;
- legacy collection-backed control forms as compatibility.

However its `collections` section still contained:

`canonical_for_variadic_heads: true`.

That phrasing conflicts with the dedicated v0.8 control surfaces and could imply that visible collection syntax is canonical for Sequence/Concurrent.

Checkpoint 124 changes it to false and records the actual rule:

> collection punctuation is canonical for genuine Collection values; And/Or and Sequence/Concurrent use their dedicated flat surfaces.

No parser behavior changes.

## Repository drift-check defect

The existing repository test intended to reject free current `:role` markers in docs/player/syntax data.

Its final regex boundary was accidentally written as a literal escaped `\\b` instead of regex word-boundary `\b`.

As a result, the test did not detect the stale role-selector references above.

Checkpoint 124 fixes the regex.

A second current-reference guard is added for code examples in `docs/` and `player/`.

Unless the same line explicitly labels the material as legacy/older/historical/debug/compatibility/noncanonical, the guard rejects code spans containing:

- leading legacy mood + final period;
- bracketed binders;
- collection-backed `Sequence`, `Concurrent`, `And`, or `Or`;
- pipe syntax.

This keeps compatibility documentation possible while preventing accidental teaching drift.

## Why compatibility tests are not globally rewritten

Many executable semantic regressions were authored before v0.8 and intentionally exercise parser compatibility while checking semantics.

Checkpoint 124 does not rewrite every historical-style test input merely for visual uniformity.

The current boundary is:

- normative/player examples must be canonical;
- dedicated compatibility behavior remains executable;
- semantic regressions may preserve accepted compatibility input when the test is not presented as player reference;
- new corpus translations and new player-facing examples use v0.8.

This avoids conflating syntax-history cleanup with removal of backwards compatibility.

## Corpus handoff

The user's next requested phase is additional-book stress testing.

Checkpoint 124 therefore updates the current corpus protocol:

- new translations must use canonical v0.8;
- broad discovery should sample several structurally different books before one source dominates design pressure;
- each pressure point must be classified before changing the language;
- verbosity is not automatically a semantic gap;
- source/world-specific facts are not automatically language primitives;
- real defects become executable regressions;
- completed prose-pass reports are archived.

This happens **before** the beginner subset and glyph-design phases.

## Regression effect

One new repository-layout regression is added.

Suite size becomes:

- **666 -> 667 tests**.

The existing role-selector drift regression is repaired rather than counted as a new test.

## Inventory effect

No semantic or vocabulary inventory changes.

The repository remains:

- **212 registered base entries**;
- **131 semantic primitive candidates**;
- **55 formal constructors**;
- **265 semantic frames**;
- **48 multi-frame entries**;
- **204 Old Names**;
- **197 core world concepts**.

## Result

**CURRENT SURFACE v0.8 REFERENCE RECONCILIATION COMPLETE.**

Checkpoint 124 concludes:

1. current player and normative surface remain v0.8;
2. the remaining active leading-mood example is corrected;
3. stale named-role examples are corrected to positional/omission syntax;
4. Collection machine metadata is aligned with flat control syntax;
5. the broken role-selector drift test is repaired;
6. current docs/player now gain an explicit guard against unlabeled legacy examples;
7. parser compatibility remains intact rather than being confused with canonical style;
8. the next active design-pressure phase is a multi-book corpus stress test.

## Next work

Run several additional books through the corpus protocol.

The purpose is to answer:

> What objective meanings or reusable grammatical/discourse structures can those books require that current Cuspell still cannot preserve?

Do not begin by adding their vocabulary.

First attempt exact composition, world concepts/Names, and current discourse machinery; add or restore productive semantics only when the source exposes an independently necessary distinction.
