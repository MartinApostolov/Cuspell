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

Cuspell is in **language stabilization**. Semantic root reduction has reached practical closure at 206 registered base entries / 125 semantic primitive candidates, and the current focus is repository/spec cleanup, player-facing grammar clarity, beginner-subset definition, and regression stability before final rune glyph design or game/world execution becomes primary work.

## Try the parser

With Python 3.11+:

```bash
python run_cuspell.py check 'MatterSelf.'
python run_cuspell.py check 'More Evaluate MatterSelf Evaluate ThingSelf.'
python run_cuspell.py explain 'If LifeThis EndLifeThis!'
python run_cuspell.py
```

See `docs/PARSER.md` for the current supported slice and commands.
