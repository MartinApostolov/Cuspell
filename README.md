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

The project is currently formalizing the semantic type system and auditing the candidate rune inventory before moving into full sentence grammar and semantic roles.
