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

## Reduction status

The current 125 semantic primitive candidates are reduction-closed **for now**, not permanently frozen.

A future deletion must preserve the full registered truth conditions, typing, and execution closure. Moving the same atomic meaning into a new enum/value/world classifier does not count as semantic reduction.

Historical candidate/derived tables and completed reduction audits are preserved under `archive/`.
