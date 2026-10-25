# Cuspell — punctuation and typography sidebar audit

**Status:** user-selected punctuation symbols and two glyph exclusions have been recorded in the Stage 2 ledger. No actual source SVGs, canonical fonts, root bindings, or parser semantics have been changed. This file supersedes the initial proposal-only audit.

## User decisions — 2026-10-25

User instructed:
- R105 shall represent the assertion/final stop `.`.
- R106 shall represent the binder separator `:`.
- A054 shall represent the final question mark `?`.
- If nothing better is found, R076 may be used as an exclamation point `!`.
- Remove R070 and, in follow-up, also remove R107.

### Approved punctuation (excluded from magic-root candidate pool, preserved as font resources)

| Source vector | Punctuation character | Purpose | Alternate archived source | Status |
| --- | --- | --- | --- | --- |
| R105 | `.` | Sentence end / assertion mood | R217 | User-approved punctuation design |
| R106 | `:` | Typed binder separation, e.g. `a:Location` | R218 | User-approved punctuation design |
| A054 | `?` | Sentence end / question mood | — | User-approved punctuation design |

R105 and R106 have linked alternate-ink Runic source records. Their source variants are **also reserved** (not extra distinct punctuation designs), and all original source artwork is preserved.

### Deferred option for exclamation

**R076** is a provisional choice for `!`, **not yet transferred from the magic candidate count**. Its approved current adaptation has the dot **above** the long stroke; conventional `!` needs dot below. If chosen, produce a flipped/reflowed punctuation-specific variant for correct typography. Its linked alternate-ink source is R188. A better existing exclamation candidate can still supersede R076.

### Excluded, not repurposed

- **R070** is excluded from the magic glyph pool. Its normalized second-ink source variant **R182** inherits the exclusion.
- **R107** (three vertically stacked dots) is excluded outright, rather than added to the punctuation reserve. Its linked second-ink source **R219** inherits the exclusion.

The originals remain archived; exclude here means ineligible for final selection, not destructive deletion.

## What punctuation and notation Cuspell grammar actually uses

Evidence: `docs/CUSPELL_DICTIONARY.md`, sections 7–13.

| Character(s) | Function in present player-facing grammar | Necessary? | Special handling |
| --- | --- | --- | --- |
| `.` | Assertion end/mood | **Yes** | R105 approved |
| `?` | Question end/mood | **Yes** | A054 approved |
| `!` | Command end/mood | **Yes** | R076 provisional |
| `:` | Binder delimiter, e.g. `a:Location` | **Yes** | R106 approved |
| `«` and `»` | Quoted Signs, New Names, Old Names (nestable) | **Yes** | Need custom/standard font glyphs, *not* magic-root assignments |
| `$` | Reference to scoped binder, e.g. `$a` | **Yes** | Grammar token, not magic-root symbol |
| `(` and `)` | Explicit grouping fallback | **Yes, optional in typical text** | Must render and parse when needed |
| `_` | Skip an optional argument | **Yes, when needed** | Zero-mana syntax |
| `{` and `}` and `,` | Actual collection literals, e.g. `{This,Self,You}` | **Yes, for collection literal use** | Not needed for ordinary linear And/Or or event sequence |
| `@` | Current small-number one sign (repeated as `@@` and so on) | **Yes** | **Not ordinary punctuation:** number-1 glyph remains in the 218-sign goal (217 semantic roots + 1 numeric sign). Don't silently adopt a spare punctuation artwork for this yet. |
| space | Word/phrase separation | **Yes** | Spacing metric, no dedicated drawable glyph |

Older pipe hard-binding is **debug-only**; older bracketed binder forms are compatibility-only; no need to promote `|`, `[`, or `]` as canonical syntax. Conventional semicolon, em dash, slash, hyphen, ellipsis and straight quotation marks are **not currently obligatory grammar markers**, although the eventual font may support them as normal text typography without claiming they are roots.

## Two distinct inventories

1. **Magic glyph candidates:** uniquely identifiable designs eligible for 217 base roots + special numeric `@` sign, randomly assigned as appropriate between game runs.
2. **Punctuation / syntax typography:** fixed lexical functions, free of root assignment, kept outside the 218 magic glyph goal.

**Counts after the above changes:**
- Initially 337 normalized designs.
- Direct normalized exclusions: **82** (48 G originals + 34 imported R/A).
- Remaining normalized designs **not directly excluded: 255**, including **3** reserved punctuation designs.
- Thus **252 eligible magic candidates = 102 G + 84 R + 66 A**; the R076 exclamation option is still counted among these 252 until separately approved/reclassified.
- **26** Runic second-ink linked source records inherit exclusions; 82 direct + 26 linked = **108/449** archived source records excluded. **341** records not excluded, including **5** source records earmarked for punctuation typography; **336** source records remain eligible for magic candidacy.
- 12 individual short-leash glyphs and 4 unresolved pair choices remain unchanged.

**No canonical edits** yet: original CC0 ZIPs, stylized SVGs, parser, source glyph registry, root assignments, and existing font are untouched. Experimental branch `glyphs/idylwild-style-sample-01` / draft PR #124 only.
