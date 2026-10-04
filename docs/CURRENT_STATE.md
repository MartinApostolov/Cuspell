# Current State

_Last normalized: checkpoint 119_

This is the concise maintainer handoff for **current Cuspell**. Historical development detail is intentionally kept out of this file and preserved under `archive/`.

## Goal

Cuspell is a formal, compositional rune language for objective freeform magic.

Players should be able to construct effects that were never prewritten as spells, while every valid magical expression has a meaning determined by the language rather than negotiated from intent.

## Current source-of-truth layers

- `language/` — machine-readable language data.
- `world/` — machine-readable world concepts and names.
- `docs/spec/` — detailed current semantic/grammar specifications.
- `docs/CUSPELL_DICTIONARY.md` — internal human-facing dictionary and writing reference.
- `docs/DECISIONS.md` — current cross-spec invariants only.
- `tests/` — current executable regression truth.
- `player/` — player/PC-facing projection of current truth.
- `archive/` — superseded snapshots, completed audits, historical corpus passes, old syntax, and the old decision log.

If archived material conflicts with a current layer, the current layer wins.

## Current inventory

The registered base inventory is:

- **212 total registered entries**;
- **131 semantic primitive candidates**;
- **55 formal constructors**;
- **16 reference forms**;
- **10 domain values**;
- **0 unresolved candidates**;
- **0 derived candidates**.

The current semantic basis is **reduction-closed for now**, not permanently frozen. Checkpoint 101 supersedes the temporary checkpoint-100 `Interpret` addition: exact interpretation is compositional once typed inverse-relation selection is available through `Collect` + `Unique`.

## Current Old Name layer

The core registry contains **204 Old Names**:

- **197 concept/Kind Old Names**;
- **6 canonical Unit Old Names**;
- **1 parameterized expression Old Name** (`give`).

Old Names are provisional historical vocabulary while the language is still being designed. They may be rewritten if semantic cleanup requires it.

New Names remain ordinary naming/reference data and never gain free magical macro behavior.

Checkpoint 106 audits this vocabulary for civilization-scale coverage. The current Old Name layer is a strong but **uneven, corpus-shaped foundation**, not a claim of civilization-complete historical vocabulary. Checkpoints 111–116 complete anatomy, geography/weather, agriculture/material, craft/transport, war/public-institution, and art/ritual/shared-culture batches. Checkpoint 117 completes the planned balanced sweep with day/calendar day, night, season, year, month/calendar month, and date/calendar date. Calendar periods are typed world Kinds over TimeInterval; Date is an Information Kind. Age remains compositional from an explicit start point plus temporal Extent rather than becoming a new root.

Checkpoint 107 resolves the first semantic issue exposed by that audit: `Health`, `Pain`, and `Ill` are restored as independent core meanings. `Damage`, `Health`, `Pain`, `Ill`, and `Life` are deliberately non-equivalent; `Heal` remains compositional. Checkpoint 108 resolves the biological-sex asymmetry by adding positive `Male` alongside `Female`; neither is defined as negation of the other or as part of a universally exhaustive binary. Checkpoint 109 resolves the referenced-TimeInterval gap by adding typed Begin/End/Extent frames to existing roots, with unavailable boundaries/duration left unavailable for unbounded intervals. Checkpoint 110 resolves the final structural vocabulary question: exact pre-magic compositional verbs/relations may be parameterized expression Old Names with required typed positional parameters, lexical scope, frozen historical Sign cost, and ordinary mana cost for written arguments. `«TransferHave»` = give is the first pilot.

## Current surface syntax

Canonical transliteration is **surface v0.8**.

Core writing principles:

- sentence-final `.`, `?`, and `!` mark assertion, question, and command;
- normal Cuspell is flat prose;
- heads normally precede arguments;
- typed frames determine left-to-right attachment;
- adjacency may form an exact root, registered lexical compound, or one uniquely typed tight local application;
- the whole sentence must consume completely and resolve to one semantic normal form;
- ambiguity is rejected rather than guessed;
- required roles cannot be silently omitted;
- optional arguments are positional; `_` skips exactly one optional slot when a later slot or outer argument must follow; English/internal role labels are not surface Cuspell;
- `And` / `Or` use canonical spoken-order infix form;
- `Sequence` / `Concurrent` use flat event lists;
- sentence end closes a final Sequence/Concurrent;
- `SequenceEnd` / `ConcurrentEnd` are canonical zero-mana boundary markers when later sentence material follows;
- bare binders use `name:Domain`, with `$name` references;
- true Collection values still use collection syntax when the meaning genuinely is a collection;
- quotation `«... »` preserves an exact Sign;
- parentheses and pipe remain legal fallback/debug grouping, not the normal prose style.

Legacy leading mood, bracketed binder, and older collection-backed forms remain parser-compatible only where current tests intentionally preserve them.

## Semantic architecture

The executable core continues to use the same broad semantic architecture:

- Entity
- Kind
- Property
- Relation
- Process
- Quantity
- Reference<T>
- Operator

Higher structures include Proposition, EventSpec, Event, Command, Collection<T>, Sequence<T>, Location, Region, Path, GeometryProfile, TimePoint, TimeInterval, and Information values.

Key distinctions that remain important:

- Property vs value-bearing Attribute;
- persistent state predicates vs value change;
- EventSpec vs actual Event;
- language validity vs magical executability;
- negation vs zero vs semantic opposite;
- names vs semantic identity/classification;
- lexical mana cost vs RequiredPower/world execution.

## Names and world concepts

Ordinary nouns do not all need primitive roots.

Current layers are:

1. productive semantic roots;
2. stable world concepts/classifiers;
3. Old Names for established pre-magic vocabulary;
4. New Names for people, particular objects, foreign/proper names, and newly coined terms.

The direct noun roots Human, Cat, Water, Body, Hand, and Sound have already migrated into world concepts + Old Names.

## Corpus status

The previously audited Yona material through numbered Chapter 168 plus 94.5, Pride and Prejudice, and Frankenstein remain covered by executable regression pressure.

No post-minimization corpus regression requires restoring a removed root or adding a new grammar/type family.

Completed prose-pass reports are archived under `archive/corpus/`; current methodology lives in `docs/corpus/`; current regression truth lives in `tests/`.

## Validation status

The complete executable suite currently contains **654 tests** and passes on Python **3.11** and **3.12**.

Checkpoint 96 added systematic whole-registry Old Name validation. Checkpoint 97 measured grammar complexity. Checkpoint 98 separated current truth, player reference, executable tests, and historical evidence into distinct repository layers. Checkpoint 99 audited every multi-frame lexical entry and standardized one redundant optional-role overload. Checkpoint 100 removed the hidden interpreted-Sign `Sense` overload. Checkpoint 101 then generalized typed relation selection, removed the temporary `Interpret` root, and eliminated the `Name` inverse-resolution overload. Checkpoint 102 identified free English `:role` labels as a zero-mana semantic leak. Checkpoint 103 replaces them with the meaning-free positional `_` omission marker and moves canonical transliteration to surface v0.8. Checkpoint 104 finalizes the grouping policy: parentheses remain the player fallback, while pipe is debug/legacy parser compatibility only. Checkpoint 105 resolves the final lexical irregularity by restoring contextual `Almost` and making `Distance` strictly spatial. Checkpoint 106 audits civilization-scale vocabulary without changing the inventory; it finds lexical-balance gaps plus targeted semantic pressure around health/pain, biological-sex classification, and TimeInterval boundary/extent access, and raises a separate vocabulary-design question about historical lexicalization of parameterized verbs/relations. Checkpoint 107 resolves the health finding by adding `Health`, `Pain`, and `Ill` as three independent one-frame semantic primitive candidates while keeping Heal compositional. Checkpoint 108 resolves the sex-classification finding by adding `Male` as a positive one-frame Property and narrowing `Female` to positive biological classification. Checkpoint 109 adds three frames—Begin(TimeInterval), End(TimeInterval), and Extent(TimeInterval)—without adding any registered entry or primitive meaning. Checkpoint 110 generalizes frozen expression Old Names to required typed parameters, closes caller-binder capture, and adds the first parameterized historical word: `«TransferHave»` = give. Checkpoints 111–113 add balanced world-concept/Old-Name vocabulary without changing the base semantic inventory. Checkpoint 114 adds twenty-two craft/transport world concepts + Old Names and one genuine semantic primitive candidate, `Rotate`, because rigid pose/orientation change is not reducible to translation or intrinsic Form change. Checkpoint 115 adds thirteen war/public-institution world concepts + Old Names and one semantic primitive candidate, `Authority`. Checkpoint 116 resolves the world-category pressure from that pass without adding a root: registered world Kind concepts may explicitly declare which semantic types they classify. Sixteen art/ritual/shared-culture concepts are added across Entity, Event/EventSpec, and Information classifier domains. Checkpoint 117 uses the same mechanism for calendar vocabulary: five period Kinds classify TimeInterval and Date classifies Information; no base semantic entry/frame is added. Checkpoint 118 performs the promised exact reduction audit and retains `Authority`: permission, obligation, capability, control, rules, and causation can all match between two world states while recognized standing to make a later decision binding differs. Checkpoint 119 re-tests `Health`, `Pain`, and `Ill` against the stabilized Attribute, evaluator, sensing, and world-Kind machinery and retains all three as independent semantic meanings.

## Current grammar-complexity result

Checkpoint 99 completed the audit of all **51** entries that were multi-frame at checkpoint 98.

One redundant overload was mechanical rather than semantic: `GratefulTo` now uses one ordinary frame with an optional positional basis value. The live registry exposes **265 semantic frames** and **48 multi-frame entries**:

- 22 entries have no callable frame;
- 142 have exactly one frame;
- 35 have exactly two frames;
- 13 have three or more.

The original 51 audit targets classify as:

- **33** same-operation typed generalizations;
- **15** contextual/shorthand forms of the same operation;
- checkpoint 99 originally found **3** genuinely irregular lexical cases: `Distance`, `Sense`, and `Name`.

Checkpoint 100 resolved the hidden `Sense` overload, and checkpoint 101 goes further: successful interpretation is compositional through `Meaning`, `Understand`, `Sense`, and explicit state transitions, so the temporary `Interpret` root is removed. The same checkpoint replaces one-argument resolving `Name` with general typed `Unique Collect ...` selection. Checkpoint 105 resolves `Distance`: spatial Distance is one coherent operation, while contextual near-satisfaction/near-occurrence returns to the distinct `Almost` operator. The current learning-complexity summary is therefore **7 universal writing rules, 7 reusable player-facing structural constructions, and 0 genuinely irregular multi-frame lexical cases**.

## Current project phase

The project is in **language stabilization**.

Immediate priorities are:

1. finish reconciling current grammar specs/examples with canonical v0.8;
2. continue the **reduction/redundancy audit** over the remaining productive meanings restored/added during checkpoints 107–117; checkpoints 118–119 retain `Authority`, `Health`, `Pain`, and `Ill`, so the next semantic targets are `Male` and `Rotate`;
3. keep the player-facing layer small and mechanically checked against current truth;
4. define/test a beginner vocabulary + grammar subset;
5. return to glyph/rune visual design only after the writing system is stable enough.

Game/world execution, concrete physics, RequiredPower calibration, and final glyph design remain later work.

## Historical record

For pre-checkpoint-98 state history, completed audits, old syntax versions, corpus passes, and the D001-D179 decision log, start at `archive/README.md`.
