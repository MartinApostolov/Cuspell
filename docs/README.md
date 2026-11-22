# Maintainer / Designer Documentation

This directory contains the **current working documentation** used to design and maintain Cuspell.

Start here:

For **Language v1.0**, begin with [the release notes](release/LANGUAGE_V1_0_RELEASE_NOTES.md), [canonical manifest](release/LANGUAGE_V1_0_MANIFEST.json), and [Windows font acceptance](release/LANGUAGE_V1_PC_UTF8_ACCEPTANCE.md). The language is frozen at written surface v0.10; earlier exploratory history remains archived.

1. `CURRENT_STATE.md` — concise current handoff.
2. `CUSPELL_DICTIONARY.md` — complete internal dictionary with all 217 illustrated core runes and writing guide.
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
