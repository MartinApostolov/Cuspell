# Current State

_Last normalized: checkpoint 141_

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

- **217 total registered entries**;
- **136 semantic primitive candidates**;
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

The complete executable suite currently contains **768 tests** and passes on Python **3.11** and **3.12**.

Checkpoint 96 added systematic whole-registry Old Name validation. Checkpoint 97 measured grammar complexity. Checkpoint 98 separated current truth, player reference, executable tests, and historical evidence into distinct repository layers. Checkpoint 99 audited every multi-frame lexical entry and standardized one redundant optional-role overload. Checkpoint 100 removed the hidden interpreted-Sign `Sense` overload. Checkpoint 101 then generalized typed relation selection, removed the temporary `Interpret` root, and eliminated the `Name` inverse-resolution overload. Checkpoint 102 identified free English `:role` labels as a zero-mana semantic leak. Checkpoint 103 replaces them with the meaning-free positional `_` omission marker and moves canonical transliteration to surface v0.8. Checkpoint 104 finalizes the grouping policy: parentheses remain the player fallback, while pipe is debug/legacy parser compatibility only. Checkpoint 105 resolves the final lexical irregularity by restoring contextual `Almost` and making `Distance` strictly spatial. Checkpoint 106 audits civilization-scale vocabulary without changing the inventory; it finds lexical-balance gaps plus targeted semantic pressure around health/pain, biological-sex classification, and TimeInterval boundary/extent access, and raises a separate vocabulary-design question about historical lexicalization of parameterized verbs/relations. Checkpoint 107 resolves the health finding by adding `Health`, `Pain`, and `Ill` as three independent one-frame semantic primitive candidates while keeping Heal compositional. Checkpoint 108 resolves the sex-classification finding by adding `Male` as a positive one-frame Property and narrowing `Female` to positive biological classification. Checkpoint 109 adds three frames—Begin(TimeInterval), End(TimeInterval), and Extent(TimeInterval)—without adding any registered entry or primitive meaning. Checkpoint 110 generalizes frozen expression Old Names to required typed parameters, closes caller-binder capture, and adds the first parameterized historical word: `«TransferHave»` = give. Checkpoints 111–113 add balanced world-concept/Old-Name vocabulary without changing the base semantic inventory. Checkpoint 114 adds twenty-two craft/transport world concepts + Old Names and one genuine semantic primitive candidate, `Rotate`, because rigid pose/orientation change is not reducible to translation or intrinsic Form change. Checkpoint 115 adds thirteen war/public-institution world concepts + Old Names and one semantic primitive candidate, `Authority`. Checkpoint 116 resolves the world-category pressure from that pass without adding a root: registered world Kind concepts may explicitly declare which semantic types they classify. Sixteen art/ritual/shared-culture concepts are added across Entity, Event/EventSpec, and Information classifier domains. Checkpoint 117 uses the same mechanism for calendar vocabulary: five period Kinds classify TimeInterval and Date classifies Information; no base semantic entry/frame is added. Checkpoint 118 performs the promised exact reduction audit and retains `Authority`: permission, obligation, capability, control, rules, and causation can all match between two world states while recognized standing to make a later decision binding differs. Checkpoint 119 re-tests `Health`, `Pain`, and `Ill` against the stabilized Attribute, evaluator, sensing, and world-Kind machinery and retains all three as independent semantic meanings. Checkpoint 120 re-tests `Male`/`Female` and retains both positive persistent Properties: negation is not converse, a universal Sex attribute adds/overconstrains machinery, and current world-Kind predication would lose their StateProposition/Begin/End behavior. Checkpoint 121 re-tests `Rotate` and retains it: translation/Offset/reference frames do not encode Entity pose, Form is intrinsic shape, and per-Part motion would hide the same rigid transform in constraints. Checkpoint 122 audits typed world-Kind `classifies_types` and retains the mechanism with targeted repairs: the default Entity target is centralized, redundant explicit Entity metadata is removed, named-Kind binders now inherit single classifier domains, multi-domain Kind binders fail explicitly until union binder types exist, and core/package data validation now applies the same classifier-type constraints. Checkpoint 123 audits parameterized expression Old Names and retains the feature narrowly: `«TransferHave»` remains the only current pilot, required typed positional parameters remain mandatory, caller arguments may use caller scope but frozen templates cannot capture it, hidden defaults/unused parameters are invalid, and registry validation now compiles frozen expression templates instead of waiting until first use. Checkpoint 124 finishes the current surface-v0.8 reference reconciliation: stale leading-mood and named-role examples are corrected, Collection metadata no longer implies collection-backed control syntax, and repository tests now reject unlabeled legacy examples in current docs/player material. Checkpoint 125 runs the requested seven-source corpus matrix: existing Yona plus Alice's Adventures in Wonderland, Treasure Island, The Time Machine, Twenty Thousand Leagues under the Sea, On the Origin of Species, and The Wealth of Nations. No new grammar/root gap appears; the one genuinely new physical pressure is quantitative water Pressure. Checkpoint 126 resolves that case by adding `Pressure` as one independently meaningful scalar physical AttributeDescriptor while keeping its Quantity dimension derived from Mass/Length/Time. The audit rejects a generic world-package mechanism that would silently mint new callable semantic descriptors: world packages supply Pressure values and physical laws, while new directly usable semantic attributes still require a language-level meaning or exact composition. Checkpoint 127 then defines the first spell-focused beginner projection: **47 current signs**, two starter Unit Old Names, and **47 parser-validated level-0-to-2 SRD spell-effect analogues**. It adds no semantics or inventory entries. The subset intentionally prefers execution-objective `This`/`You`/`Self` references over context-only `That`, and treats fresh creation, omniscient search/divination, D&D roll modifiers, and full persistent illusion systems as outside this first teaching slice. Checkpoint 128 audits higher-level SRD spell pressure through level 9 and confirms that normal spell surface remains flat: the canonical teleport example is `Concurrent EndAtSelfHere BeginAtSelfThere!`, and all curated beginner spell examples are now parenthesis-free. Advanced effects mostly reuse current state/change/control/Trigger/teleport machinery; the strongest unresolved reusable families are fresh generation, bounded unknown-information acquisition, persistent shared illusion/representation, generic magical-execution interception/suppression, and time-flow manipulation. No new semantic root is added. Checkpoint 129 resolves the first advanced spellcraft gap by adding `Create`: exactly one fresh Entity identity is allocated per invocation and bound through an objective post-creation Proposition profile. This preserves the distinction between creation and `Begin Exist` reactivation, keeps Kind/world generation profiles as realization data rather than hidden spell semantics, and rejects creation profiles that do not constrain the fresh result. Checkpoint 130 then feeds `Create` back through the level-0-to-2 starter corpus: the starter grows to **50 signs** by removing contextual `They` from executable teaching, adding objective `Collect` + `Member` selection, and adding existing `Matter` + `Create`; Faerie Fire becomes objective group illumination instead of duplicating Light, Magic Missile becomes fresh projectile creation plus immediate movement, and a Find Familiar-like fresh creature example is added. The audit also exposes and fixes a compositional scope gap in `Create`: an optional continuation EventSpec may use the fresh binder immediately after creation/profile realization, while the binder still cannot escape the Create expression. Exact duplicate beginner recipes are now regression-guarded as intentional only. Checkpoint 131 resolves bounded unknown-information acquisition by adding `Find` with yes/no and open-query frames under an explicit query-linked information-access scope. `Find` is factive and distinguishes successful empty/false answers from blocked/incomplete access; it does not turn Question, Sense, Collect, If, Trigger, or references into omniscient search. This adds one registered entry, one primitive candidate, and two semantic frames. Checkpoint 132 resolves persistent shared illusion/representation by adding `Represent(carrier,content,channel)` as an objective persistent StateProposition. Fresh non-Matter Sign/Entities can now carry one or more shared sensory representations; observers Sense the same carrier under ordinary access physics, while Meaning, truth, physical solidity, and forced belief remain separate. This adds one registered entry, one primitive candidate, and one semantic frame. Checkpoint 133 resolves generic magical-execution interception without adding a root: `Magic` now classifies EventSpec/Event provenance and bound `Prevent` can match candidate EventSpecs before commit with an optional Region footprint scope. This adds three frames and makes Magic/Prevent multi-frame. Checkpoint 134 resolves time-flow manipulation by adding `TimeFlow(subject,reference,rate)` for Entity/Region subjects with an explicit SpatialValue reference and nonnegative dimensionless rate. Event frequency, Repeat, Prevent, and ordinary scheduling remain separate. This adds one registered entry, one primitive candidate, and two frames. Checkpoint 135 separates learnability from coverage: the old 50-sign SRD-derived set is retained as a coverage projection, while the actual beginner core is rebuilt as **16 signs** in four cumulative steps (6/9/11/16). The core teaches Move, Begin/End state transitions, simple yes/no Find, and one Create continuation pattern. Light is corrected to fresh creation: `Create x:Entity At $x Here Change $x Light «LightUnit» @!`. Checkpoint 136 stress-tests that progression and finds the final 11→16 step too cognitively dense: five new semantic signs arrived together with `@`, an Old Name unit, typed binder syntax, bound-variable reuse, and Create profile/continuation scope. The true semantic core is therefore reduced to **11 signs** at 6/9/11-sign stages. `Ill` leaves the required core, `Magic` takes its place because the same Begin/End/Find pattern yields more spellcraft-relevant effects, and `Here` becomes optional because creation can reuse `There`. Light/attribute change is a +2-sign module (`Change`, `Light`) and fresh creation is a second +2-sign module (`At`, `Create`), for **15 semantic signs** across the full first course. Checkpoint 137 adds two more teaching stages without changing the 11-sign core or language inventory: `ThisInterval` + `Persist` teach finite active maintenance at **17 cumulative semantic signs**, then `Prevent` teaches simple exact-EventSpec protection at **18**. The module explicitly treats `ThisInterval` as an objectively designated TimeInterval, not an implicit duration/forever default; bound EventSpec interception remains advanced. Checkpoint 138 adds shared visual representation as a two-sign module, `Vision` + `Represent`, reaching **20 cumulative semantic signs**. It deliberately reuses Begin/End, Persist, and Create rather than adding conjunction, Sign classification, Sense, or extra channels. Represent remains a carrier/content/channel state: shared does not imply forced perception, belief, truth, solidity, or physical presence. Checkpoint 139 resolves the programming/multi-target teaching bundle by splitting it into five stages: `And` (21 signs), `Sequence` + `Concurrent` (23), `Repeat` (24), `Collect` + `Member` + `Each` (27), and simple `Trigger` (28). The audit adds `Sequence` to the teaching path because the prior candidate list mentioned Concurrent but omitted general ordered composition. Multi-target examples use explicitly resolvable group membership rather than hidden world search; bound-witness Trigger and advanced selectors remain deferred. Checkpoint 140 adds the final planned teaching module: `TimeFlow` alone, reaching **29 cumulative semantic signs**. The required examples use positive Entity-relative factors such as `@@`, so no new arithmetic/zero vocabulary is needed. `Zero` enables stop-time, `Divide` enables fractional slow-time, and Region TimeFlow remains optional/advanced. Negative factors/time reversal remain excluded. Checkpoint 141 stress-tests the whole 29-sign path rather than treating it as one beginner course. Every required example uses only signs introduced by its stage, so no hidden registered-sign prerequisite remains. The stable teaching boundaries are now **11-sign first-lesson core / 18-sign beginner / 24-sign intermediate / 29-sign advanced extension**. The audit also reorders simple `Trigger` before `Collect`+`Member`+`Each`, because the watcher reuses known condition/action/lifetime structure while nested multi-target distribution adds two binder roles and collection resolution.

## Current grammar-complexity result

Checkpoint 99 completed the audit of all **51** entries that were multi-frame at checkpoint 98.

One redundant overload was mechanical rather than semantic: `GratefulTo` now uses one ordinary frame with an optional positional basis value. After checkpoint 134, the live registry exposes **276 semantic frames** and **53 multi-frame entries**:

- 22 entries have no callable frame;
- 142 have exactly one frame;
- 39 have exactly two frames;
- 14 have three or more.

The original 51 audit targets classify as:

- **33** same-operation typed generalizations;
- **15** contextual/shorthand forms of the same operation;
- checkpoint 99 originally found **3** genuinely irregular lexical cases: `Distance`, `Sense`, and `Name`.

Checkpoint 100 resolved the hidden `Sense` overload, and checkpoint 101 goes further: successful interpretation is compositional through `Meaning`, `Understand`, `Sense`, and explicit state transitions, so the temporary `Interpret` root is removed. The same checkpoint replaces one-argument resolving `Name` with general typed `Unique Collect ...` selection. Checkpoint 105 resolves `Distance`: spatial Distance is one coherent operation, while contextual near-satisfaction/near-occurrence returns to the distinct `Almost` operator. The current learning-complexity summary is therefore **7 universal writing rules, 7 reusable player-facing structural constructions, and 0 genuinely irregular multi-frame lexical cases**.

## Current project phase

The project is in **language stabilization**.

Immediate priorities are:

1. return to **rune/glyph visual design** now that the spellcraft teaching boundary is stress-tested and explicitly tiered;
2. keep strengthening repository/player drift checks while visual work proceeds;
3. keep advanced bound watchers/selectors/interception, richer multi-channel representation, and advanced TimeFlow applications outside the required learning path;
4. keep the 50-sign SRD set as a coverage benchmark rather than a teaching target.

Concrete world physics, RequiredPower calibration, and detailed execution laws remain later work. The SRD spell list is a coverage benchmark, not Cuspell's balance system.

## Historical record

For pre-checkpoint-98 state history, completed audits, old syntax versions, corpus passes, and the D001-D179 decision log, start at `archive/README.md`.
