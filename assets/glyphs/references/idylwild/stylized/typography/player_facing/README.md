# Player-facing Cuspell punctuation — editable SVG drafts

**Stage 2 visual prototypes**, not a compiled font. Every shape uses the Cuspell 600×1000 canvas with 66-unit round-cap strokes and a common dark ink.

Existing user-selected design sources retained: `R105` → `.` (period), `R106` → `:` (colon), `A054` → `?` (question). We use derivatives for punctuation baseline/spacing while retaining all original source SVGs. `!` is a **new independent design**; `R076` remains a magic candidate.

Other actual player-facing grammar characters: `« »` for quoted Signs and Names, `$` for binder references, `( )` for explicit grouping, `_` for positional omission, `{ }` and `,` for collections. See `manifest.json` for the 13 filenames and codepoints.

Not included: debug-only `|`, compatibility-only `[ ]`, and optional non-core prose marks `;`, hyphens, em dashes, ellipses and straight quotes. `@` is a special numeric-one magic sign and **not** punctuation; it still occupies one of 218 required magic/numeric slots. Whitespace is a later font spacing metric.

All shapes are drafts until visual sign-off; character advance widths, vertical metrics, Unicode cmap, font building, parser changes and final bindings are deliberately untouched. Source grammar: `docs/CUSPELL_DICTIONARY.md` §§7–13.

See `../../analysis/PUNCTUATION_SYMBOL_SIDEBAR_AUDIT.md` and `../../analysis/potential_overlap_groups.json` for recorded decisions.
