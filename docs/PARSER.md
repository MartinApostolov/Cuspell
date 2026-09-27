# Reference Parser

_Status: executable prototype v0.1_

The reference parser is the objective language referee for the current machine-readable slice of Cuspell.

It does not simulate world physics or decide RequiredPower. It currently checks surface structure, typed application, binder scope, selected normalizations, and written mana cost.

## Quick start

No installation is required if Python 3.11+ is available.

From the repository root:

```bash
python run_cuspell.py check '!Move|This|Here.'
python run_cuspell.py explain '!If|Life|This|EndLife|This.'
python run_cuspell.py mana '!Move|This|Here.'
python run_cuspell.py
```

The final command starts an interactive prompt.

Optional editable installation is also supported:

```bash
python -m pip install -e .
cuspell check '!Move|This|Here.'
```

## Commands

### check

Validates one complete sentence and prints its normalized meaning, result type, and written mana cost.

```text
$ python run_cuspell.py check '!Move|This|Here.'
VALID
Meaning: Move(theme=This,goal=Here)
Result type: EventSpec
Mana: 3
```

A type error remains specific:

```text
$ python run_cuspell.py check '!Move|This|@@.'
INVALID
TypeMismatch: Expected Location, received Quantity:Number at @@.
  expected: Location
  received: Quantity:Number
Mana (written semantic runes): 4
```

### parse

Prints the canonical semantic form. Add `--json` for the structured result.

### explain

Prints the same validation plus an AST tree. This is the most useful design/debugging mode.

### mana

Counts written semantic runes without requiring the sentence to be valid.

### interactive

Running `python run_cuspell.py` with no subcommand opens a REPL so experimental sentences can be checked repeatedly.

## Current executable language slice

The first slice intentionally covers only enough vocabulary to prove the architecture:

- This / Self / Here / There;
- Cat / Human Kind predication;
- Life;
- Move / EndLife / Change;
- Volume / Density / Heat;
- Equal / Multiply;
- BeforeValue / AfterValue / Preserve;
- If / All / Sequence;
- typed binders and variable references;
- named roles;
- finite EventSpec collections;
- unary `@` numbers;
- assertion / question / command mood;
- whitespace versus pipe-phrase boundaries;
- event-local snapshot shorthand;
- written mana counting.

The complete written lexicon is much larger. Unsupported roots currently produce `UnknownRoot`; that means the machine-readable package has not encoded them yet, not that the design specification necessarily rejects them.

## Data-driven layout

The parser reads language data from:

- `language/core/types.json`
- `language/core/lexicon_minimal.json`
- `language/syntax/surface_v0_2.json`

The implementation lives under `src/cuspell/`.

The goal is to move semantics into machine-readable data as the language grows rather than filling the Python code with one-off spell logic.

## Tests

Run the current executable regression suite without installing the package:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The first implementation milestone passes tests for:

- valid Kind predication;
- Move command parsing;
- pipe spacing;
- whitespace not creating Sequence;
- typed Move errors;
- flat nested If;
- binder scope;
- Sequence collections;
- named roles;
- deep flat relative-change parsing;
- attribute-value type mismatch;
- required sentence termination.

## Scope boundary

This parser currently answers:

> Is this sentence valid under the encoded language slice, and what typed AST does it mean?

It does not yet answer:

> Can the world realize this EventSpec, what does it target at runtime, or how much RequiredPower does it need?

Those belong to later reference-resolution/world-execution stages.
