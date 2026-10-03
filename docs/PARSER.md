# Reference Parser

_Status: current executable reference implementation_

The parser/type checker is the objective referee for the machine-readable Cuspell layer. It checks surface structure, typed frames, binding, semantic normalizations, execution closure, and written mana cost.

It does **not** yet simulate world physics or compute final RequiredPower.

## Quick start

With Python 3.11+ from the repository root:

```bash
python run_cuspell.py check 'Move This Here!'
python run_cuspell.py explain 'If LifeThis EndLifeThis!'
python run_cuspell.py mana 'Move This Here!'
python run_cuspell.py
```

Optional editable installation:

```bash
python -m pip install -e .
cuspell check 'Move This Here!'
```

## Commands

### check

Validates one complete sentence and prints normalized meaning, result type, diagnostics, and written mana.

### parse

Prints canonical semantic form. Add `--json` for structured output.

### explain

Shows validation plus the AST tree. This is primarily a maintainer/debugging view; it is not player-facing Cuspell syntax.

### mana

Counts written semantic signs without requiring the sentence to be valid.

### interactive

Running `python run_cuspell.py` without a subcommand opens the interactive checker.

## Current surface

Canonical surface is v0.8.

Examples:

`MatterSelf.`

`LifeThis?`

`Move This Here!`

`If LifeThis EndLifeThis!`

`LifeThis And MagicThis.`

`Sequence MoveSelfHere MoveSelfThere!`

`Permitted You Sequence MoveYouHere MoveYouThere SequenceEnd Self.`

`g:Location At This $g?`

Parentheses remain the current explicit grouping fallback. Pipe hard-binding is accepted only for parser/debug and historical compatibility, alongside legacy leading mood, bracketed binders, and older collection-backed control forms.

## Data-driven layout

Current machine-readable inputs include:

- `language/core/types.json`
- `language/core/lexicon.json`
- `language/core/compounds.json`
- `language/core/dimensions.json`
- `language/core/units.json`
- `language/core/inventory_roles.json`
- `language/syntax/surface_v0_8.json`
- `language/names/old_names.json`
- `world/core/concepts.json`
- `world/core/new_names.json`
- optional `world/<package>/concepts.json`
- optional `world/<package>/new_names.json`

The implementation lives under `src/cuspell/`.

## Executable coverage

The suite currently contains **631 tests** and runs on Python 3.11 and 3.12.

Coverage includes:

- flat/tight surface parsing and legacy compatibility;
- typed frames with positional optional arguments and the `_` omission marker;
- sentence-final mood;
- And/Or and Sequence/Concurrent;
- binders, open questions, typed set comprehensions, selectors, and collection typing;
- type-preserving `Collect` plus `Unique` for explicit inverse-relation selection;
- Old Names, New Names, world concepts, and Unit normalization;
- state boundaries, Change, possession, Cause, Transfer, Control;
- dimensional arithmetic/value-domain checks;
- geometry/time relations;
- epistemic, discourse, social, and deontic semantics;
- execution-closure checks;
- diagnostic source spans;
- language/world data validation;
- deterministic parser fuzz smoke tests;
- post-minimization book-corpus regressions;
- root-minimization/stabilization invariants.

Run:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Parsing policy

The parser keeps all legal typed candidates until full consumption.

- no complete parse -> invalid;
- one semantic normal form -> valid;
- multiple parses with the same normal form -> valid;
- multiple distinct normal forms -> ambiguous.

It does not choose the “most natural” interpretation.

## Compound/tight parsing

Resolution priority is:

1. exact registered root;
2. licensed lexical compound;
3. uniquely typed tight local application.

Examples:

`SolidMatter This.`

`LifeThis.`

`MoreDensityThisDensityThat.`

Known roots concatenated without a licensed or unique typed meaning fail rather than being guessed.

## Command semantic closure

A structurally typed EventSpec may still be incomplete for magical execution.

For example, an unconstrained Move without a goal/path can be meaningful as an ordinary EventSpec but rejected as an executable Command.

Closure checks recurse through If, Sequence, Concurrent, Trigger, Repeat, and other nested structures.

## Names/world boundary

Old Names can provide registered typed meanings and historical name-unit costs.

New Names remain contextual naming/reference data and do not become compile-time magical macros.

World concept identity and classification are separate from the parser's language grammar; physical recognition/generation belongs to later world execution.

## Repository boundary

Current executable tests/fixtures live under `tests/`.

Historical written stress cases and stale surface fixtures are preserved under `archive/tests/`.

Player-facing language instructions live under `player/`; this file is maintainer/tooling documentation.
