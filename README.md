# Cuspell

Cuspell is a formal, compositional rune language for objective freeform magic.

The design goal is to let players construct effects that were never prewritten as spells while making the meaning of every valid magical expression mechanically determinable rather than negotiated with the GM.

## Start here

For any new design thread or coding session, read these files in order:

1. `docs/CURRENT_STATE.md` — canonical summary of the current design.
2. `docs/DECISIONS.md` — decisions that should not silently regress.
3. `docs/ROADMAP.md` — current open problems and recommended work order.
4. `docs/spec/` — the current detailed specifications.
5. `docs/history/` — historical snapshots and handoffs; useful context, but not canonical when they conflict with current specs.

## Working convention

GitHub is the persistent source of truth between chat threads.

When meaningful design work is completed:

- update the relevant file under `docs/spec/`;
- update `docs/CURRENT_STATE.md` if the overall state changed;
- append or revise `docs/DECISIONS.md` when a design decision is made, replaced, or reversed;
- update `docs/ROADMAP.md` when the next work changes;
- make a descriptive commit.

Do not create a new versioned copy for every small edit. Git history is the version history. Historical snapshot files are retained only when they are useful milestones.

## Current project phase

The first written semantic-core milestone is complete: typed lexical semantics, sentence grammar, collections/binders, Kind/lexicalization rules, quantities/measurement, space/time, identity, mind/information, magical execution, vocabulary layers, and a first regression suite now have working specifications.

The first executable parser/type-checker slice now exists. The current priority is to expand the machine-readable lexicon, turn more written stress/corpus cases into executable tests, and use implementation failures to expose remaining ambiguities before final rune glyph design.

See `docs/CURRENT_STATE.md` for the current handoff and `docs/ROADMAP.md` for the staged plan.


## Try the parser

With Python 3.11+:

```bash
python run_cuspell.py check '!Move|This|Here.'
python run_cuspell.py explain '!If|Life|This|EndLife|This.'
python run_cuspell.py
```

See `docs/PARSER.md` for the current supported slice and commands.
