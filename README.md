# Cuspell

**Language v1.0 — release source (tag `v1.0.0`).** Canonical surface grammar is **v0.10**. The [release notes](docs/release/LANGUAGE_V1_0_RELEASE_NOTES.md), [frozen release manifest](docs/release/LANGUAGE_V1_0_MANIFEST.json) and [Windows font kit](assets/glyphs/references/idylwild/windows_test_font/) describe the stable language-only release. A complete ready-to-use archive and a corrected offline keyboard are published as GitHub release assets.

Cuspell is a formal, compositional rune language for objective freeform magic.

The design goal is to let players construct effects that were never prewritten as spells while making the meaning of every valid magical expression mechanically determinable rather than negotiated with the GM.

## Players / PCs

Start with `player/README.md`.

The player layer contains only the information needed to use Cuspell:

- quick start;
- canonical writing rules;
- rune/sign dictionary;
- advanced grammar;
- Old Names and New Names.

## Maintainers / designers

For a new design or coding session, read:

1. `docs/CURRENT_STATE.md`
2. `docs/CUSPELL_DICTIONARY.md`
3. `docs/DECISIONS.md`
4. `docs/ROADMAP.md`
5. relevant files under `docs/spec/`

Repository roles are deliberately separated:

- `language/` — current machine-readable language truth;
- `world/` — current machine-readable world/name truth;
- `src/` — implementation;
- `tests/` — current executable regression truth;
- `docs/` — current maintainer/designer documentation;
- `player/` — player/PC-facing reference;
- `archive/` — superseded/historical material in development order.

Use `archive/` for rationale only. It is never current truth when it conflicts with the current layers.

## Working convention

GitHub is the persistent source of truth between chat threads.

When meaningful design work is completed, update current specs/state/decisions/roadmap as needed and keep completed snapshots/audits out of the current-doc root. Git history is normal version history; preserved superseded milestones belong in `archive/`.

## Current project phase

Cuspell Language v1.0 is **frozen** with a new canonical rune-native binder syntax (surface v0.10). The semantic core remains at 217 registered base entries / 136 semantic primitive candidates. Checkpoint 141 stress-tests the complete learning path and fixes the teaching boundary: **11 signs** for the first-lesson core, **18** for beginner spellcraft, **24** for intermediate composition, and **29** for the advanced extension. No hidden registered-sign prerequisite was found; the one ordering repair moves simple `Trigger` before nested collection distribution.

## Glyph font and click-to-type keyboard

**Accepted Windows font:** [Cuspell Compact WinTest](assets/glyphs/references/idylwild/windows_test_font/) is the existing proportionally spaced design that passed Windows Notepad and UTF-8 save/reopen/decode. Install **CuspellCompactWinTest-Regular.ttf** and use the corrected **Language v1.0 Windows Font Kit** from the GitHub release for offline typing. VS Code is optional, not a release requirement. Earlier Cuspell Compact/234 Review kits remain as original historical sources.


The **234 approved source glyph designs** and thirteen punctuation symbols remain available in the original installable PC test kit in [`assets/glyphs/references/idylwild/keyboard_kit/`](assets/glyphs/references/idylwild/keyboard_kit/). Download `Cuspell_Codex_Keyboard_Kit.zip`, install the font, open `keyboard.html` to type glyphs, and use `chart.html` as a complete index. **All 217 registered rune meanings plus numeric `@` have approved individual glyphs, with 16 approved spares** (canonical mapping: [`language/core/glyph_assignments.json`](language/core/glyph_assignments.json)). The original font and ID-based keyboard remain unchanged. The [meaning-aware typing page](assets/glyphs/references/idylwild/keyboard_kit/meaning_keyboard.html) now converts approved rune names to glyphs and back. See [glyph typing instructions](player/GLYPH_TYPING.md), the [PC font acceptance check](player/PC_FONT_CHECK.md), and the [Language v1.0 validation checklist](docs/LANGUAGE_V1_VALIDATION.md); 82 maintained spellcraft examples and representative tests from nine previously sampled books, Yona/cross-genre regressions, and current reference documents now exercise glyph/parser round trips. Glyph-origin root collisions are disambiguated; Windows real-PC validation passed and the Language v1.0 source is frozen. Recommended viewing is 32–34 px, with 20 px minimum. Historical glyph handoffs are archived under `archive/glyphs/handoffs/`.

## Try the parser

With Python 3.11+:

```bash
python run_cuspell.py check 'MatterSelf.'
python run_cuspell.py check 'More Evaluate MatterSelf Evaluate ThingSelf.'
python run_cuspell.py explain 'If LifeThis EndLifeThis!'
python run_cuspell.py
```

See `docs/PARSER.md` for the current supported slice and commands.


**Surface v0.10:** rune-native binders infer a unique type from typed uses (`All :«This» Life $«This».`), accept existing tight Cuspell expressions as witnesses (`:«This»:MassSelf`), and reject duplicate active labels. Prior v0.9 syntax remains archived.
