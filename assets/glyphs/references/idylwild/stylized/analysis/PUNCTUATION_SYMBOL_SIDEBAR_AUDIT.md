# Cuspell — punctuation and typography sidebar audit

> **CURRENT DECISION — 2026-10-29:** User excluded `G054` and `R099` after punctuation-glyph comparison; `R211` is the equivalent second-ink Runic source and inherits exclusion. User put `A012` and `A013` on the short leash (still eligible). `G055` was excluded previously. No other glyph from the displayed four groups was newly excluded or automatically approved; particularly the `!` collision group remains unresolved and R076 stays a magic candidate. The JSON ledger now records 84 excluded normalized designs, 250 eligible magic designs, 3 source designs reserved for punctuation, 218 required and 32 provisional spare. The 252 count in the pre-decision scan is historical. Render future comparison sheets directly from source SVGs at high resolution, **not by enlarging 60x100 raster masks**.

## Complete candidate-to-punctuation collision scan (2026-10-29)

The user explicitly requested comparison against **every retained or not-yet-resolved magic candidate**, not only obvious punctuation lookalikes. The scan covered **252 eligible normalized designs × 13 player-facing punctuation designs**. See [PUNCTUATION_COLLISION_FULL_SCAN_2026_10_29.md](PUNCTUATION_COLLISION_FULL_SCAN_2026_10_29.md) for coverage, method, prioritized collisions, and next four human-decision groups.

**Confirmed visually suspicious:** G054 resembles ` (G055 shares the dollar-looking family but was already excluded); A012/A013 resemble `(` and `)`; R099 resembles `?` without its lower dot; R030 and R076 need comparison against the new `!` at small size. No candidates were removed or transferred based on the scan alone.

## Open audit — bracket necessity and punctuation/glyph collisions (2026-10-29)

User questioned whether all 13 draft punctuation marks are truly needed because Cuspell was deliberately designed to avoid bracket-heavy writing. **No punctuation has yet been removed.** Audit results from current canonical dictionary (sections 7–13):

- Square binder brackets `[ ]`: **historical compatibility only**, not player facing; absent from drafts.
- `( )`: legal *fallback* for grouping, not used for ordinary flat expressions; mixed `And`/`Or` is a concrete case requiring explicit grouping in current grammar. **Advanced / optional; proposed for review before inclusion in beginner UI.** Must not drop from general syntax without a replacement/disambiguation rule.
- `{ }` and `,`: collection **literals**, not needed for simple linear `And`, `Or`, `Sequence`, `Concurrent`. Still used when a real Collection value needs enumerated members. **Advanced / conditional.**
- `« »`: Old/New Name quotation and nested Signs; not an optional substitute for grouping brackets.
- `.`, `?`, `!`, `:`, `, `_`: meaningful syntax under present grammar, though some appear mainly in advanced expressions.
- Numeric `@` is **not** free punctuation.

The user also identified a potential visual collision between a magic glyph and the new **` binder-reference symbol**. Preliminary inspection of exact source SVG geometry raised `R026`, `R095`, `G148`, and `G100` as **comparison candidates only**, not proven duplicates or exclusions. Source drawing `R095` is more B-like; the others may have partially similar curving shapes, but the exact glyph the user noticed is **not yet identified**. Check *all* remaining normalized magic designs against all player-facing punctuation at large and small size (including mirroring/rotation for potentially confusing lookalikes); record false positives separately and do not exclude established keeps without approval. In particular, consider **redesigning fixed-function ` typography** rather than sacrificing a distinct random magic glyph if a collision is confirmed.

Keep all 13 current SVGs as *review drafts*, not a declaration that all 13 are mandatory in an initial beginner keyboard. No root binding, font, parser, or eligibility counts changed by this issue.

## Update: 2026-10-29 (supersedes R076 provisional exclamation)

- **R076 is retained as a magic glyph candidate** (R188 is its existing Runic source variant). It will NOT be used as punctuation. A **new independent `!`** was drawn in the Cuspell stroke style; it is in `../typography/player_facing/exclamation.svg`.
- Suitability groups 2–4: user found no issue with **R030, R108, R009, A018, A039, A062, R098, R019, R083, A070, A073, A075**. Retain all as magic-eligible. The old short-leash similarity flag on R098 still applies.
- Drafted **13 fixed-function player-facing punctuation SVGs** under `../typography/player_facing/`: `.`, `:`, `?`, `!`, `«`, `»`, `# Cuspell — punctuation and typography sidebar audit

## Open audit — bracket necessity and punctuation/glyph collisions (2026-10-29)

User questioned whether all 13 draft punctuation marks are truly needed because Cuspell was deliberately designed to avoid bracket-heavy writing. **No punctuation has yet been removed.** Audit results from current canonical dictionary (sections 7–13):

- Square binder brackets `[ ]`: **historical compatibility only**, not player facing; absent from drafts.
- `( )`: legal *fallback* for grouping, not used for ordinary flat expressions; mixed `And`/`Or` is a concrete case requiring explicit grouping in current grammar. **Advanced / optional; proposed for review before inclusion in beginner UI.** Must not drop from general syntax without a replacement/disambiguation rule.
- `{ }` and `,`: collection **literals**, not needed for simple linear `And`, `Or`, `Sequence`, `Concurrent`. Still used when a real Collection value needs enumerated members. **Advanced / conditional.**
- `« »`: Old/New Name quotation and nested Signs; not an optional substitute for grouping brackets.
- `.`, `?`, `!`, `:`, `, `_`: meaningful syntax under present grammar, though some appear mainly in advanced expressions.
- Numeric `@` is **not** free punctuation.

The user also identified a potential visual collision between a magic glyph and the new **` binder-reference symbol**. Preliminary inspection of exact source SVG geometry raised `R026`, `R095`, `G148`, and `G100` as **comparison candidates only**, not proven duplicates or exclusions. Source drawing `R095` is more B-like; the others may have partially similar curving shapes, but the exact glyph the user noticed is **not yet identified**. Check *all* remaining normalized magic designs against all player-facing punctuation at large and small size (including mirroring/rotation for potentially confusing lookalikes); record false positives separately and do not exclude established keeps without approval. In particular, consider **redesigning fixed-function ` typography** rather than sacrificing a distinct random magic glyph if a collision is confirmed.

Keep all 13 current SVGs as *review drafts*, not a declaration that all 13 are mandatory in an initial beginner keyboard. No root binding, font, parser, or eligibility counts changed by this issue.

## Update: 2026-10-29 (supersedes R076 provisional exclamation)

- **R076 is retained as a magic glyph candidate** (R188 is its existing Runic source variant). It will NOT be used as punctuation. A **new independent `!`** was drawn in the Cuspell stroke style; it is in `../typography/player_facing/exclamation.svg`.
- Suitability groups 2–4: user found no issue with **R030, R108, R009, A018, A039, A062, R098, R019, R083, A070, A073, A075**. Retain all as magic-eligible. The old short-leash similarity flag on R098 still applies.
- Drafted **13 fixed-function player-facing punctuation SVGs** under `../typography/player_facing/`: `.`, `:`, `?`, `!`, , `(`, `)`, `_`, `{`, `}`, `,`. R105/R106/A054 remain the previously approved visual sources for period/colon/question, now with typography-only derivatives where needed.
- The drafts require visual sign-off and font metric/cmap work later. No debug-only pipe, old brackets or non-core punctuation added. Numeric `@` is NOT punctuation and still counts toward the 218.
- **No count change:** 82 directly excluded normalized designs, 3 imported designs reserved for punctuation, 252 magic-eligible designs (including R076), at least 218 required. No canonical font, parser, root mapping, or source changes.

### Previous checkpoint — 2026-10-25 (historical)

**Historical status:** user-selected punctuation symbols and two glyph exclusions have been recorded in the Stage 2 ledger. No actual source SVGs, canonical fonts, root bindings, or parser semantics have been changed. This file supersedes the initial proposal-only audit.

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
