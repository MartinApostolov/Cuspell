# Current Lexicon Source

_Status: current specification index_

The old hand-maintained candidate table that previously lived here is archived at `archive/spec/WORKING_LEXICON_PRE_CP98.md`.

The **normative current lexical registry** is machine-readable:

- `language/core/lexicon.json`
- `language/core/compounds.json`
- `language/core/inventory_roles.json`
- `language/core/dimensions.json`
- `language/core/units.json`

The complete internal human-facing dictionary is:

- `docs/CUSPELL_DICTIONARY.md`

The player-facing rune index is:

- `player/RUNES.md`

## Current counts

The base registry contains **205 entries**:

- **125 semantic primitive candidates**;
- **54 formal constructors**;
- **16 reference forms**;
- **10 domain values**;
- **0 derived candidates**;
- **0 unresolved candidates**.

These inventory roles are classification metadata, not separate grammatical categories.

## Lexicon rule

One surface label may have several typed frames only when they represent one coherent semantic core.

If two meanings merely share an English gloss, they should not be hidden as one rune.

Frame typing, traits, value domains, contextual flags, and normalization behavior belong in machine-readable data wherever practical.

## Multi-frame audit status

Checkpoint 99 audited all **51** entries that were multi-frame at checkpoint 98.

- **33** are same-operation typed generalizations;
- **15** contain contextual/shorthand forms of the same operation;
- checkpoint 99 found **3** genuine lexical semantic splits: `Distance`, `Sense`, and `Name`.

The audit also removed one redundant frame pair: `GratefulTo` now represents optional named `:basis` through one normal frame instead of a separate overload.

Checkpoint 100 removes the interpreted-Sign `Sense` overload. Checkpoint 101 supersedes the temporary `Interpret` addition and removes the inverse-resolution `Name` overload by generalizing `Collect` to preserve binder type. The live registry now contains **256 semantic frames** and **48 multi-frame entries**. Only `Distance` remains a genuine lexical-semantic split.

## Reduction status

The current 125 semantic primitive candidates are reduction-closed **for now**, not permanently frozen. Checkpoint 101 records the stronger precedent: first restore distinctions when necessary, then remove any temporary root once an exact general composition exists.

A future deletion must preserve the full registered truth conditions, typing, and execution closure. Moving the same atomic meaning into a new enum/value/world classifier does not count as semantic reduction.

Historical candidate/derived tables and completed reduction audits are preserved under `archive/`.
