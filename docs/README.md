# Maintainer / Designer Documentation

This directory contains the **current working documentation** used to design and maintain Cuspell.

Start here:

1. `CURRENT_STATE.md` — concise current handoff.
2. `CUSPELL_DICTIONARY.md` — complete internal dictionary and writing guide.
3. `DECISIONS.md` — active cross-spec design invariants only.
4. `ROADMAP.md` — unresolved/current work order.
5. `spec/` — detailed normative specifications.
6. `PARSER.md` — executable parser/tooling guide.
7. `world/` — current human-readable world/name reference.
8. `corpus/` — current corpus methodology; completed pass records are archived.

Repository layers:

- `language/` — current machine-readable language truth;
- `world/` — current machine-readable world/name truth;
- `src/` — current implementation;
- `tests/` — current executable regression truth;
- `player/` — player/PC-facing reference;
- `archive/` — superseded snapshots, completed audits, old syntax versions, and historical test data.

Do not put new completed audit snapshots at the root of `docs/`. Record the result in current state/decisions/roadmap, then archive the evidence under `archive/`.
