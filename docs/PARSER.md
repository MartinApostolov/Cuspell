# Reference Parser

_Status: executable prototype v0.3_

The reference parser is the objective language referee for the current machine-readable slice of Cuspell.

It does not simulate world physics or decide RequiredPower. It currently checks surface structure, typed application, binder scope, selected normalizations, and written mana cost.

## Quick start

No installation is required if Python 3.11+ is available.

From the repository root:

```bash
python run_cuspell.py check '!Move This Here.'
python run_cuspell.py explain '!If Life This EndLife This.'
python run_cuspell.py mana '!Move This Here.'
python run_cuspell.py
```

The final command starts an interactive prompt.

Optional editable installation is also supported:

```bash
python -m pip install -e .
cuspell check '!Move This Here.'
```

## Commands

### check

Validates one complete sentence and prints its normalized meaning, result type, and written mana cost.

```text
$ python run_cuspell.py check '!Move This Here.'
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
- `language/core/lexicon.json`
- `language/syntax/surface_v0_3.json`

The implementation lives under `src/cuspell/`.

The goal is to move semantics into machine-readable data as the language grows rather than filling the Python code with one-off spell logic.

## Tests

Run the current executable regression suite without installing the package:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The executable suite now covers the original parser/compound milestones plus broader semantic slices, including:

- Kind predication, dynamic adjacency compounds, and compound Kinds as binder domains;
- Move and execution-closure checks, including incomplete nested Events;
- whitespace/pipe hard-binding, named roles, binder scope, and typed open questions;
- If / And / Or / All / Some / Sequence / Concurrent / Repeat control structures;
- Collect / Filter / Each / Count and selector behavior for Unique, Nearest/Farthest, Lowest/Highest, and Random;
- collection/member binder consistency for Filter and Each;
- state boundaries, possession/change molecules, BeforeValue/AfterValue, Preserve, Persist, Prevent, Trigger, and Stop;
- scalar Attributes, dimensional comparisons, and measured-property compounds;
- dimension-vector arithmetic for Add/Multiply/Divide/Power/Root, with registered aliases, stable derived dimensions, static dimensional exponent checks, and `DimensionMismatch` diagnostics;
- data-driven quantity value domains with `ValueDomainMismatch` for statically illegal values and retained dynamic AST constraints;
- registered Unit constructors loaded from machine-readable data and normalized to canonical rational scale before further arithmetic;
- spatial/time relations used by the current specification slice;
- Not/Opposite/Converse normalization and semantic equivalence checks;
- contradiction checks for exclusive families and direct Property/NotProperty pairs;
- epistemic/information, discourse, modality, and corpus-bridge examples;
- machine-readable language-data validation;
- deterministic parser fuzz smoke tests.

The executable suite currently contains **298 passing tests**, and GitHub Actions runs them on Python 3.11 and 3.12.

Parser failures rank competing backtracking diagnostics by completed parse progress. Parsed semantic nodes carry half-open `source_span` character ranges over the original sentence as diagnostic metadata, and semantic/execution-closure validators propagate those spans to their diagnostics. The CLI renders diagnostic ranges with carets and JSON output includes `{start,end}`. For nested items parsed inside collection/group syntax, diagnostics currently fall back to the enclosing source phrase when an exact inner range is unavailable.

## Scope boundary

This parser currently answers:

> Is this sentence valid under the encoded language slice, and what typed AST does it mean?

It does not yet answer:

> Can the world realize this EventSpec, what does it target at runtime, or how much RequiredPower does it need?

Those belong to later reference-resolution/world-execution stages.


## Compound parsing

The parser now distinguishes three lexical outcomes:

- exact registered root;
- valid derived compound under `language/core/compounds.json`;
- known-root concatenation with no licensed composition rule.

For example:

```text
SolidWater|This.
```

normalizes to a Water Kind restricted by Solid.

```text
OppositeMatter|This.
```

returns `IllegalCompound`, because both roots are known but Matter has no declared reversible mapping.

For the temporary ASCII transliteration, an exact registered root label takes precedence over attempting to split the same text into smaller roots. The eventual rune script will distinguish one glyph from several adjacent glyphs directly.

## Static contradiction checking

After typed parsing, the validator now checks the first constraint families.

Examples:

- `SolidLiquidMatter|This.` -> `ContradictoryConstraint` because Phase is single-valued;
- `LifeNotLife|This.` -> `ContradictoryConstraint`;
- `NotNotLife|This.` normalizes back to Life while retaining the mana cost of every written rune.

This is intentionally separate from type checking: contradictory expressions may be well-typed.


## Command semantic closure

The parser now distinguishes a typed EventSpec from an EventSpec that is closed enough to execute as a magical Command.

For example:

```text
!Move|This.
```

is structurally meaningful, but the current Move frame leaves the destination/path unconstrained. In command mood the checker reports:

```text
INCOMPLETE
SemanticallyIncomplete: Move requires at least one of: goal, path.
```

Both of these are complete:

```text
!Move This Here.
!Move|This|:path|ThisPath.
```

Closure checks recurse into nested command structures, so an incomplete Move inside If or Sequence also makes the containing Command incomplete.

This is deliberately separate from type errors and contradictions.


## Surface syntax v0.4

Ordinary application does not require pipes, and short local expressions may be tightly joined.

Preferred:

```text
CatSelf.
SolidWater This.
!Move This Here.
More Evaluate CatSelf Evaluate HumanSelf.
!If LifeThis EndLifeThis.
```

When an unregistered concatenation can be segmented into registered roots, the parser accepts it as tight local application only if the whole token has one complete typed meaning. Exact roots and licensed lexical compounds take priority.

Pipe is explicit hard binding:

```text
!Move|This|Here.
```

is equivalent to the ordinary-space form, but:

```text
!Move|This Here.
```

hard-binds `Move This` before the outer token Here is considered, so it is not interpreted as `Move This Here`.

The parser still requires one unique full typed parse; whitespace never implies free Sequence/And. Parentheses and pipe remain legal hard-grouping tools, but canonical prose prefers the flat form.
