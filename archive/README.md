# Cuspell Archive

Everything under this directory is **historical or superseded material**. It is preserved for rationale and project history, but it is not current truth.

When archive material conflicts with `language/`, `world/`, `docs/spec/`, `docs/DECISIONS.md`, or current executable tests, the current files win.

## Chronological guide

The archive is organized by development order rather than by “importance.”

### Earliest design snapshots

1. `design/Cuspell_Rune_Language_Design_v0_3.md`
2. `design/Cuspell_Rune_Language_Handoff_v0_3.md`
3. `audits/early_RUNE_INVENTORY_AUDIT.md`

### Surface-syntax history

4. `syntax/surface_v0_2.json`
5. `syntax/surface_v0_3.json`
6. `syntax/surface_v0_4.json`
7. `syntax/surface_v0_5.json`
8. `syntax/surface_v0_6.json`

Current machine-readable surface syntax remains `language/syntax/surface_v0_7.json`.

The old v0.3 case fixture is preserved at `tests/surface_syntax_cases_v0_3.json`. Current executable compatibility coverage remains in `tests/test_legacy_surface_compatibility.py`.

### Corpus development history

The `corpus/` tree preserves the successive Yona passes, rereads, gap snapshots, the cross-genre Pride and Prejudice / Frankenstein pass, and the earlier post-minimization regression checkpoint.

Use `docs/corpus/PROTOCOL.md` for current methodology and executable `tests/test_corpus_*.py` / vocabulary tests for current regression truth.

### Root-minimization and stabilization audits

Pre-family reduction material:

1. `audits/pre084_ROOT_MINIMIZATION_AUDIT.md`
2. `audits/pre084_PRIMITIVE_DERIVED_INVENTORY.md`
3. `audits/pre084_SECOND_PASS_PRIMITIVE_FAMILY_MAP.md`

Checkpointed family/closure work:

4. cp085 — motion/action manner
5. cp086 — measurement/descriptor
6. cp087 — social/affective
7. cp088 — agency/deontic/event role
8. cp089 — space/topology
9. cp090 — epistemic/discourse
10. cp091 — time/event
11. cp092 — operational/body state
12. cp093 — foundational ontology
13. cp094 — change/transfer/control
14. cp095 — global cross-family closure
15. cp096 — stabilization regression
16. cp097 — grammar complexity

File names carry the checkpoint number so directory sorting preserves this order.

### Decision history

`decisions/DECISIONS_D001_D179.md` preserves the full historical decision log through checkpoint 97, including superseded choices.

Current active invariants were separated into `docs/DECISIONS.md` at checkpoint 98.

### World/vocabulary history

`world/` contains superseded incremental Yona vocabulary snapshots. The current published Yona vocabulary reference remains under `docs/world/`.

## Archive rule

New work should not edit archived files merely to make old examples look current. If an archived conclusion needs correction, record the correction in current documentation and leave the historical record intact.


## Checkpoint-98 normalization snapshots

The normalization pass additionally preserved several pre-cleanup current files so that shortening current documentation did not erase project history:

- `state/CURRENT_STATE_THROUGH_CHECKPOINT_97.md`
- `state/ROADMAP_THROUGH_CHECKPOINT_97.md`
- `tests/WRITTEN_STRESS_TESTS.md`
- `spec/WORKING_LEXICON_PRE_CP98.md`
- `world/FIRST_CIVILIZATION_VOCABULARY_PRE_CP98.md`

These are historical snapshots only.
