# Stabilization and Regression Audit

_Status: checkpoint 96 — post-closure corpus and Old Name stabilization pass_

## Purpose

Checkpoint 95 reached practical semantic-reduction closure at:

- **205 registered base entries**;
- **125 semantic primitive candidates**;
- **0 unresolved candidates**;
- **0 derived candidates**.

This checkpoint does not search for more deletions. It asks whether the minimized
language still supports the previously translated book pressure and whether the
provisional historical vocabulary remains internally sound after the reductions.

## Book-corpus regression

The existing three-book regression is rerun against the checkpoint-95 language:

1. **Yona [Cat Girl Evolution]** — all previously audited published material through
   numbered Chapter 168 plus 94.5;
2. **Pride and Prejudice** — the prior full 61-chapter pass;
3. **Frankenstein (1818)** — the prior full-novel pass.

The executable corpus regression continues to cover the established semantic
pressure rather than mirroring copyrighted source text.

Checkpoint 96 additionally exercises the reductions introduced after the earlier
post-minimization corpus checkpoint:

- generalized `Rate` in place of ChangeRate/OccurrenceRate;
- temporal `Extent(Event)` in place of Duration;
- strict inside/outside through `In + Extent + Touch` and `Extent + Overlap`;
- possession-giving through concurrent `EndHave + BeginHave` after removal of
  Give.

The removed roots are explicitly checked as absent.

**Result: no book-corpus meaning requires restoration of a removed root or a new
grammar/type family.**

## Old Name integrity audit

The core historical registry currently contains **102 Old Names**:

- **96 concept/Kind Old Names**;
- **6 canonical Unit Old Names**.

The stabilization suite now checks the whole registry rather than only selected
examples.

For every Old Name:

- recursive mana cost resolves to a positive integer;
- every root-valued `name_unit` still names a registered current root;
- nested Old Name dependencies are already covered by language-data cycle and
  reference validation.

For every concept Old Name:

- the quoted sign resolves to its intended world `Kind`;
- the Kind works predicatively in an ordinary sentence.

For every canonical Unit Old Name:

- applying the unit to `@` still constructs a typed Quantity.

This catches exactly the kind of silent regression that can occur when a primitive
root is deleted but an older historical spelling is not rebuilt.

**Result: all 102 current Old Names survive the minimized registry.**

## World/package validation

Full `validate_language_data` validation remains part of this checkpoint, including
the opt-in Yona package and core world data.

No dangling Old Name root, nested-name dependency, unit reference, concept reference,
or world-package registration is accepted.

## Inventory result

This is a stabilization checkpoint, not a semantic-reduction checkpoint.

Inventory remains:

- **205 registered base entries**;
- **125 semantic primitive candidates**;
- **54 formal constructors**;
- **16 reference forms**;
- **10 domain values**;
- **0 unresolved candidates**;
- **0 derived candidates**.

No root or Old Name is added or removed.

## Conclusion

The language remains stable after the completed minimization passes:

- the previously translated book pressure still parses under current replacements;
- recent second-pass reductions are represented in the permanent corpus safety net;
- all current historical Old Names resolve, retain computable costs, and use only
  surviving roots;
- all language/world data validates.

The next stabilization target is the **canonical rune visual-feasibility pass** over
the current registered signs. That pass should identify whether any surviving
meaning requires a glyph design outside the agreed canonical visual target, without
changing semantics merely to make drawing easier.
