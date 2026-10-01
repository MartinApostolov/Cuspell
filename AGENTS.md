# AGENTS.md — Cuspell project working rules

This repository is the persistent source of truth for the Cuspell rune-language project.

## On every new thread/session

Read, in order:

1. `README.md`
2. `docs/CURRENT_STATE.md`
3. `docs/DECISIONS.md`
4. `docs/ROADMAP.md`
5. Relevant files under `docs/spec/`

Use `archive/` only for historical context. If archived material conflicts with current machine data, specs, decisions, current-state files, or executable tests, the current files win.

`player/` is a player-facing projection of current truth, not the maintainer source of truth.

## Design mandate

Cuspell is not a fixed spell list with decorative syntax. It is intended to be a genuine formal/compositional language whose valid magical commands have objective meanings.

Preserve these principles unless explicitly reconsidered and recorded:

- Valid expressions must resolve objectively; do not rely on "what the caster probably meant."
- Complex commands and multiple actions are allowed if the language can express them unambiguously.
- Every meaning-bearing rune in a magical command costs mana; syntax/punctuation may cost zero.
- Legitimate linguistic compression may genuinely reduce mana cost.
- Do not aggressively minimize the rune inventory early. Clarity and objective semantics come first.
- The complete language, magical vocabulary, beginner vocabulary, and hidden/advanced vocabulary may differ.
- Do not allow arbitrary user-defined aliases to become free magical compression.
- Distinguish logical negation, zero magnitude, semantic opposites, and relation converse.
- Prefer formal typing, traits, frames, and constraints over GM interpretation.

## Working style

The user is comfortable delegating the next design step. Once they explicitly ask for the full autonomous build, continue step-by-step without requiring approval after every subsection. Revise earlier work when stress tests expose problems, but record the change and rationale.

Do not silently overwrite major prior decisions. If one must change:
1. update the relevant spec;
2. record the superseded decision in `docs/DECISIONS.md`;
3. update `docs/CURRENT_STATE.md`;
4. explain the reason in the commit message or accompanying design note.

## File discipline

- Current normative specifications live under `docs/spec/`.
- `docs/CURRENT_STATE.md` is a concise handoff, not the full specification.
- `docs/DECISIONS.md` records only current cross-spec invariants; full historical decisions are archived.
- `docs/ROADMAP.md` records unresolved work in priority order.
- `archive/` contains milestone snapshots, completed audits, old handoffs, old syntax versions, and other superseded material.
- Use Git commits for normal version history instead of proliferating `v0.x` copies.

When a session materially advances the project, leave the repository in a state where a new thread can continue using the files alone.
