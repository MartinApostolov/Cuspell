# Cuspell

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

Cuspell is in **language stabilization**. The semantic core remains at 217 registered base entries / 136 semantic primitive candidates. Checkpoint 141 stress-tests the complete learning path and fixes the teaching boundary: **11 signs** for the first-lesson core, **18** for beginner spellcraft, **24** for intermediate composition, and **29** for the advanced extension. No hidden registered-sign prerequisite was found; the one ordering repair moves simple `Trigger` before nested collection distribution.

## Glyph font and click-to-type keyboard

The **234 surviving, unassigned glyphs** and thirteen approved punctuation symbols are available as an installable PC test kit in [`assets/glyphs/references/idylwild/keyboard_kit/`](assets/glyphs/references/idylwild/keyboard_kit/). Download `Cuspell_Codex_Keyboard_Kit.zip`, install the font, open `keyboard.html` to type glyphs, and use `chart.html` as a complete index. **Meanings will be assigned after PC testing, not before.** Recommended viewing is 32–34 px, with 20 px minimum. Historical glyph handoffs are archived under `archive/glyphs/handoffs/`.

## Try the parser

With Python 3.11+:

```bash
python run_cuspell.py check 'MatterSelf.'
python run_cuspell.py check 'More Evaluate MatterSelf Evaluate ThingSelf.'
python run_cuspell.py explain 'If LifeThis EndLifeThis!'
python run_cuspell.py
```

See `docs/PARSER.md` for the current supported slice and commands.
