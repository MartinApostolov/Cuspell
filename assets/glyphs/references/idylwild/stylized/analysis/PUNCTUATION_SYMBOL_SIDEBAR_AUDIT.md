# Stage 2 — punctuation-like and familiar-symbol glyph audit

Status: **candidate audit / recommendation only**. No user-selected glyph has been removed or reclassified by this document. Current Stage 2 ledger and all historical SVG sources remain unchanged. Started at 116 reviewed groups / 257 normalized unexcluded candidate designs.

## Reason for this pass

User asked to identify signs that should not occupy magic-root glyph slots because they look like ordinary punctuation, such as a lone dot or a question mark. User also suggested a separate sidebar of **font punctuation marks**, so these images could be preserved and potentially used as punctuation instead of counted toward the mandatory distinctive root-sign inventory.

Cuspell's player-facing grammar already uses final `.`, `?`, `!` as sentence mood and terminators. These markers cost no mana; they should be styled and available in a font but **do not count** among the 217 registered semantic roots plus one number-1 symbol (minimum 218 magic signs). The dictionary is the source for this distinction.

## Group A — clear punctuation forms: recommend font punctuation reserve, not root glyphs

| Source ID | Actual stylized design | Proposed use | Related archived source |
| --- | --- | --- | --- |
| **R105** | A single round dot | full stop `.` (adjust baseline when typesetting) | R217 (alternate-ink rendering) |
| **R106** | Two vertically stacked dots | colon `:` | R218 |
| **R107** | Three vertically stacked dots | vertical ellipsis `⋮`, if wanted; **not** the usual horizontal `…` | R219 |
| **A054** | Drawn question mark with detached dot | sentence-final `?` | none |

These are **not yet excluded or moved**. If the user approves all four for reserve, normalised root/design candidate count drops from 257 to 253; the three Runic alternate-ink source IDs must be linked in the reserve too, without double-counting them as new designs. The reserve still has to be drawn at punctuation-appropriate size/baseline; using root-glyph em proportions unchanged is not automatically suitable.

## Group B — extremely simple or resembling ordinary marks: discuss

| ID | Visual | Reason to flag | Prior decision |
| --- | --- | --- | --- |
| **R076** | Dot above long vertical stroke | resembles dotted `i` or inverted `¡`; not a conventional `!` without reorientation | previously still eligible |
| **R030** | Full-height plain vertical stroke | resembles `|` or `I` and is very weak as a distinct root sign | still eligible |
| **R070** | Shorter plain vertical stroke | easy to confuse with R030, typeface bar, or letter `l` | still eligible |
| **R108** | Plain crossing strokes | visually identical to plus `+`, but user **explicitly kept R108** in Group 107 | keep decision stands; do not automatically remove |

The historical Cuspell parser's old hard-binding pipe is **debug-only**, not modern player-facing grammar. Do not assume a new semantic need for a `|` punctuation key solely to justify moving R030.

## Group C — recognizable conventional signs, not automatically disallowed

| ID | Visual likeness | Question |
| --- | --- | --- |
| **R009** | less-than `<` | Could be ordinary mathematical notation rather than a magic root |
| **A018** | infinity `∞` | A strongly recognizable math symbol |
| **A039** | Greek uppercase omega-like `Ω` over two strokes | The Greek letter likeness might be distracting, though the horizontal lines distinguish it |
| **A062** | numeral `4` with lower short crossbar | May be confusing next to Cuspell's separate numeric writing system |

These are **review flags**, not a recommendation to necessarily reject recognizable motifs. Reuse as notation, retain as root art, or archive after a visual vote.

## Proposed structural change after user approval

Maintain two **separate named pools**, while keeping original R/A/G source IDs and CC0 attribution:

1. **Magic glyph candidates** — must be individually distinguishable; count toward the 218 minimum.
2. **Punctuation / typography reserve** — sentence `.`, `?`, `!` and any additional approved syntax marks or number/math signs; available in the eventual typeface, but **not** subject to the random semantic root-sign mapping, and **not** counted among the 218 required signs.

Potential optional category: **excluded source design** with all historical assets preserved.

**IMPORTANT:** This document only presents a classification proposal. Do not alter the committed candidate/exclusion totals, source SVGs, parser punctuation semantics, font cmap, or root bindings until exact decisions are made.

Example review sheet generated for user: `CUSPELL_punctuation_symbol_audit.png` (inline in conversation; not currently stored as a repository asset). The pictured silhouettes come directly from the approved stylized source SVG geometries, without changing their form.

Experimental branch `glyphs/idylwild-style-sample-01` / Draft PR #124. `main` untouched.
