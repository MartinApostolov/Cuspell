# Roadmap

_Last updated: 2026-09-28_

This is the current recommended work order. Earlier semantic-design phases are retained here as completed milestones so a new thread can see what changed.

## Completed milestone A — lexical semantic architecture

Completed:

- eight-category lexical type architecture;
- traits/frames/constraints;
- Opposite / Not separation; explicit relation-role order replaces a separate Converse primitive;
- high-risk lexical polysemy cleanup;
- scalar Attribute model;
- Begin/End state transitions;
- structural Part/Whole/Joined distinctions.

Primary specs:

- `SEMANTIC_TYPE_SYSTEM.md`
- `LEXICAL_RESOLUTIONS.md`
- `ATTRIBUTES_AND_CHANGE.md`
- `STRUCTURE_AND_MEREOLOGY.md`

## Completed milestone B — sentence grammar and binding

Completed working semantics for:

- Proposition / EventSpec / Event / Command;
- Command and Question mood;
- semantic roles;
- grouping/case syntax;
- binders;
- quantification;
- collections;
- distribution;
- selectors;
- multi-action And/Sequence;
- conditional control;
- result/event binders.

Primary specs:

- `SENTENCE_GRAMMAR.md`
- `SURFACE_SYNTAX.md`
- `COLLECTIONS_AND_BINDING.md`
- `SELECTION_AND_REFERENCE.md`

## Completed milestone C — Kind/noun system

Resolved the specific-noun problem through:

- canonical natural Kinds;
- semantic molecules;
- relationally defined artifact Kinds;
- ad-hoc restricted Kinds;
- world classifiers;
- deterministic generation/transform profiles when required.

Primary specs:

- `KIND_AND_LEXICON_SYSTEM.md`
- `PURPOSE_AND_ARTIFACTS.md`
- `WORLD_MODEL_INTERFACE.md`

## Completed milestone D — quantities and physical description

Working systems now exist for:

- unary numbers;
- Zero and signed values;
- arithmetic compression;
- dimensions;
- Units interface;
- scalar Attributes;
- Ratio;
- vectors;
- space/geometry;
- time/events;
- RGB/Light ColorProfile.

Primary specs:

- `NUMBER_AND_MEASUREMENT.md`
- `SPACE_AND_GEOMETRY.md`
- `TIME_AND_EVENTS.md`
- `COLOR_SYSTEM.md`

## Completed milestone E — identity, life, mind, and information

Working semantics now distinguish:

- Entity identity through typed Equal / Exist;
- Create / Transform / Destroy / restoration;
- Life versus existence;
- integrity / Repair / healing;
- material/biological classifiers;
- Sign / Information / Meaning;
- Know / Believe / Remember / Memory;
- Sense / Find;
- Questions versus information acquisition;
- Names versus identity.

Primary specs:

- `IDENTITY_AND_EXISTENCE.md`
- `MATTER_LIFE_INTEGRITY.md`
- `MIND_AND_INFORMATION.md`

## Completed milestone F — magical execution model

Working semantics now exist for:

- command validation stages;
- mana counting;
- command Power / RequiredPower interface;
- underpowered failure;
- semantic closure;
- reference failures;
- And versus Sequence commit behavior;
- Persist;
- Trigger;
- Repeat;
- Dispel;
- competing Magic;
- zero-time recursive-cycle rejection.

Primary spec:

- `MAGIC_EXECUTION.md`

Balance formulas remain intentionally separate.

## Completed milestone G — vocabulary layers and first stress suite

Completed:

- full / magical / beginner / advanced/hidden vocabulary layers;
- consolidated working lexicon;
- first semantic regression suite;
- first eight gaps found by stress testing and resolved;
- implementation-facing normalized AST and diagnostics.

Primary specs:

- `VOCABULARY_LAYERS.md`
- `LEXICON.md`
- `STRESS_TESTS.md`
- `AST_AND_VALIDATION.md`

## Completed milestone H — real-prose corpus testing

A corpus-driven stress-test workflow is now active.

Completed corpus work:

- Yona Chapter 1 opening/general discourse, market/investigation, and System/dialogue passes;
- Chapter 1 current-language re-audit;
- Chapter 2 sequential adventure/discourse pass;
- Chapter 14 targeted mana-manipulation/body-construction material plus current-language re-audit;
- Chapter 47 dedicated mana-system pass;
- consolidated current gap ledger.

The corpus produced and resolved/partially resolved new needs for:

- Kind predication;
- discourse/anaphora;
- nested speech context;
- narrative time/aspect;
- Generic/Habitual/Most;
- subjective evaluation/preferences;
- modality/intention/obligation;
- wh-questions;
- Stop/Prevent;
- Concurrent events;
- epistemic Confidence/Evidence/Assert;
- rate/trend language;
- prerequisite/Method structures;
- relative pre-state values;
- Preserve constraints;
- approximation/almost;
- Control;
- distributed resource/field descriptions.

Primary files:

- docs/corpus/PROTOCOL.md
- docs/corpus/yona/CH01_PASS_A.md
- docs/corpus/yona/CH01_PASS_B.md
- docs/corpus/yona/CH01_PASS_C.md
- docs/corpus/yona/CH14_MAGIC_PASS.md
- docs/corpus/yona/CH01_REAUDIT_2026.md
- docs/corpus/yona/CH02_PASS_A.md
- docs/corpus/yona/CH14_REAUDIT_2026.md
- docs/corpus/yona/CH47_MANA_PASS.md
- docs/corpus/yona/CURRENT_GAPS_2026.md
- docs/spec/DISCOURSE_AND_NARRATIVE.md
- docs/spec/EPISTEMIC_REASONING.md
- docs/spec/RELATIVE_CHANGE_AND_FIELDS.md

## Completed milestone I — flat surface syntax v0.2

The parenthesis-heavy temporary notation has been replaced by a flatter grammar:

- adjacency = lexical compound;
- unbridged whitespace = phrase boundary;
- `|` = application binding;
- typed prefix parsing recovers nested structure;
- pipe phrases require full field consumption;
- ambiguity is rejected rather than guessed;
- parentheses remain fallback grouping;
- semantic And/Sequence are never supplied for free by whitespace.

A parser-facing algorithm, machine-readable syntax file, and initial syntax test corpus now exist.

Primary files:

- `docs/spec/SURFACE_SYNTAX.md`
- `docs/spec/LINEAR_PARSING.md`
- `language/syntax/surface_v0_2.json`
- `tests/surface_syntax_cases.json`

## Completed milestone J — first executable parser

The first runnable reference parser/type-checker now exists.

Implemented:

- data-driven minimal type hierarchy and lexicon/frame slice;
- v0.2 whitespace/pipe segmentation;
- typed recursive prefix parsing;
- full-consumption phrase validation;
- optional positional arguments and named roles;
- binder scope;
- collection parsing;
- Kind predication;
- selected dynamic Attribute/result typing;
- event-local BeforeValue/AfterValue shorthand;
- AST/canonical serialization;
- written mana counting;
- human-readable diagnostics;
- command-line and interactive use;
- executable regression tests.

The first local test run passes 12 tests.

Primary files:

- `run_cuspell.py`
- `src/cuspell/`
- `language/core/types.json`
- `language/core/lexicon.json`
- `tests/test_parser.py`
- `docs/PARSER.md`

## Completed milestone K — compound semantics and contradiction validation

The executable parser now derives adjacent-root compounds from registered composition rules rather than requiring every compound to be hard-coded.

Implemented:

- machine-readable compound-rule package;
- exhaustive registered-root segmentation for unknown compound fields;
- Property + Kind restriction;
- compatible Property conjunction;
- Not over Properties;
- Opposite through declared reversible mappings;
- direct relation-role order rather than a dedicated Converse operator;
- Begin/End state-boundary compounds;
- compound Kind binder domains;
- distinct UnknownRoot versus IllegalCompound diagnostics;
- exact source rune cost for current compound cases;
- contradiction detection for exclusive families and P + NotP;
- EndLife normalized through End + Life;
- 12 new executable compound/operator tests.

The full executable suite now passes 24 tests.

Primary files:

- `language/core/compounds.json`
- `src/cuspell/language.py`
- `src/cuspell/validator.py`
- `tests/test_compounds.py`

## Completed milestone L — command semantic closure

The checker now distinguishes a type-correct EventSpec from a Command whose execution-relevant roles are still underconstrained.

Implemented:

- frame metadata for execution-only closure requirements;
- Move requires at least a goal or path when used as a Command;
- recursive closure checking through If/Sequence/nested EventSpecs;
- explicit SemanticallyIncomplete diagnostics;
- CLI output distinguishes INCOMPLETE from INVALID and CONTRADICTORY;
- explicit path-only Move example;
- 5 executable closure regression tests.

Parser version is now v0.2 and the complete executable suite passes 29 tests.

## Completed milestone M — surface syntax v0.3 and automated CI

The mistaken v0.2 whitespace interpretation has been corrected.

Current syntax:

- adjacency = lexical compound;
- whitespace = ordinary token separation;
- typed prefix parsing infers application across spaces;
- pipe = explicit hard subexpression binding;
- parentheses = fallback hard grouping.

The parser accepts both `Move This Here` and explicit `Move|This|Here`, while `Move|This Here` preserves the intended hard boundary.

A GitHub Actions workflow runs the complete Python unittest suite on Python 3.11 and 3.12 for pull requests and pushes to `main`.

The v0.3 migration added 11 parser/surface regression checks and brought the executable suite to 40 tests.

## Completed milestone P — naturalized And Sequence and binders

Surface syntax v0.6 removes more visible parser scaffolding from normal prose:

- `A And B` is canonical conjunction;
- `Sequence E1 E2 ...` is canonical ordered event syntax;
- sentence end closes the Sequence automatically;
- `SequenceEnd` is used only when the Sequence must end before later material;
- binder declarations use bare `a:TypeOrNamedKind` syntax; named Kind domains such as `a:«Know«MoveLifeThing»»` are supported.
- true Collection values remain available where collection semantics are actually needed.

## Completed milestone O — sentence-final mood punctuation

Surface syntax v0.5 moves mood to the sentence-ending punctuation:

- `.` assertion;
- `?` question;
- `!` command.

This removes redundant leading mood marks from normal Cuspell prose while keeping old prefix forms temporarily parser-compatible for historical tests/documents. The writing guide also now includes fuller examples for named roles, collections, binders, and large compounds/tight expressions.

## Completed milestone N — flat prose surface v0.4 and human dictionary

Canonical player-facing Cuspell is now flat prose rather than visible AST notation.

- tight local adjacency supports forms such as `MatterSelf`, `LifeThis`, and `DensityThis`;
- registered lexical compounds such as `SolidMatter` retain priority and their existing derived meanings;
- whitespace separates larger phrase units and typed prefix frames determine structure;
- pipe and parentheses remain fallback/debugging grouping rather than normal writing;
- contextual `Evaluate target` supports compact discourse comparison such as `More Evaluate MatterSelf Evaluate ThingSelf.`;
- `docs/CUSPELL_DICTIONARY.md` contains the full current registered vocabulary with a blank future-rune column and a consolidated writing guide;
- `language/syntax/surface_v0_4.json` records the same standard mechanically.

## Completed milestone M — broad executable semantic expansion and hardening

After the v0.3 surface migration, the reference implementation expanded from the initial 40-test slice to **317 passing tests**. Executable coverage now includes collection/selector semantics, state and control structures, measured properties, dimension-vector Add/Multiply/Divide arithmetic, distinct dimension diagnostics, open questions, epistemic/information semantics, discourse/modality cases, corpus-bridge translations, written stress distinctions, language-data validation, execution closure, logical constraints, semantic equivalence, deterministic fuzz smoke testing, and source spans propagated through parser, AST, semantic validation, and execution closure.

Collection-dependent binders are now data-driven: `Filter` and `Each` declare which collection role supplies their members, and the parser checks the binder's semantic type against that member type. Selector regressions also confirm that tie-preserving extrema remain Collections until explicitly reduced.

Backtracking diagnostic ranking now tracks completed parse progress separately from user-facing error location, so speculative branches no longer outrank a more complete typed parse simply because they wandered farther. Parser diagnostics also retain original-source half-open character spans through pipe-spacing normalization. The remaining location-quality work is to propagate spans into normalized AST nodes and semantic/closure validator diagnostics.

## Completed milestone Q — counterfactuals and surface v0.7

The Chapters 1–14 + 47 corpus sweep exposed one repeated new structural gap and two surface asymmetries. Surface/language v0.7 closes them:

- `Counterfactual(A,B)` is a contextual proposition over a contrary-to-actual alternative history and remains distinct from actual-world `If`;
- contextual counterfactual selection is rejected inside magical Commands until an explicit objective hypothetical-history construction exists;
- proposition `Or` is canonical infix syntax;
- mixed bare And/Or requires explicit grouping rather than hidden precedence;
- `Concurrent E1 E2 ...` is canonical flat concurrent-event syntax;
- sentence end closes Concurrent, and `ConcurrentEnd` closes it before later material;
- regression coverage runs successfully on Python 3.11 and 3.12.

## Completed milestone R — full v0.7 source rerun and Attempt closure

A fresh reread of the live Yona source for Chapters 1–14 and 47 rechecked the entire previously audited corpus rather than relying on stored findings.

The rerun found one missed reusable semantic molecule:

- `Attempt(agent, goal)` is an actual goal-directed effort EventSpec;
- it is distinct from Intend/Plan;
- it does not entail goal success;
- success/failure can be built from Attempt plus goal occurrence/non-occurrence in the relevant attempt context;
- magical Attempt commands the effort episode, not guaranteed success.

The rerun also rechecked Only, still/already/yet, unless, until, instead, even, past-directed Should, expected "should have", succeed/fail/manage, and the v0.7 Or/Concurrent surface. None required another grammar/type-system change for the audited passages.

The executable suite reaches 334 passing tests on Python 3.11 and 3.12.

## Completed milestone S — Old Names, New Names, and world concepts

Vocabulary/worldbuilding now has an explicit historical naming architecture:

- `«... »` is an exact Sign and supports nesting;
- world concepts have stable identities independent of names/descriptions;
- New Names remain ordinary Name/reference relations and do not create magical macros;
- Old Names are pre-magic historically established vocabulary with frozen semantic meanings;
- Old Name mana comes from historical name units rather than expansion size;
- later Old Names may use earlier Old Names as historical name units, with recursive frozen cost and acyclic dependency ordering;
- common ordinary Old Names should originate as plausible descriptions built from roots or earlier vocabulary available at the time, not newly invented one-word English labels;
- exact punctuation can distinguish names without carrying active sentence grammar inside the quote;
- machine-readable registries exist for Old Names, world concepts, and New Names;
- ordinary direct noun roots should be migrated into concepts + Names when the naming/history layer is ready.

The implementation validates these registries and regression-tests nested names, same-description/different-name concepts, direct Kind use, historical spell compression, and the rule that unregistered/New quoted Signs are not magical macros.

## Completed milestone T — first civilization vocabulary seed

The Old Name system now has its first substantial non-corpus-specific vocabulary layer.

- 13 productive descriptive/information/spatial roots were made executable where needed by general worldbuilding;
- 62 stable world concepts were added across biology, materials, artifacts, buildings, transport, resources, economy, institutions, social roles, information, and measurement;
- each concept receives an actual descriptive Old Name rather than an English object root;
- later names reuse earlier names recursively, including Ship from the already-established Boat name;
- contextual etymological material such as HighSize/Hard remains historical spelling material after fossilization rather than live membership conditions;
- all current concept classifiers are explicitly marked as requiring later objective world-ontology rules;
- dedicated regressions prevent the English glosses from silently becoming direct core roots.

The human-facing inventory is `docs/world/FIRST_CIVILIZATION_VOCABULARY.md`.

## Completed milestone U — audited Yona vocabulary split through current publication

The Yona corpus through the current publication boundary (numbered Chapters 1–168 plus 94.5) now has an explicit Old/New vocabulary classification layer and a full structural stress pass.

- 15 broad ordinary semantic/action roots were added where the corpus needed reusable language rather than named objects;
- 18 additional ordinary concepts received descriptive Old Names;
- setting-specific vocabulary was moved into an opt-in `world/yona` package rather than contaminating `world/core`;
- the Yona package currently contains 318 world concepts and 329 New Name entries, including later Dungeon/System ontology, Adamantium/Hero ranks, Epithets, Classes, Professions, Skills, Traits, Soul Weapons, Event rewards, people/places/species, and exact source-visible progression labels through Chapter 168;
- System technical categories such as Skill/Class/Trait/Level/Tier are New Names even if ordinary pre-magic language could contain older similar-sounding concepts;
- named species, Skills, people, and places are New Names;
- world-package validation checks concept types, referents, duplicate IDs, and core collisions;
- regression tests verify that loading the Yona package is opt-in and that ordinary Old Names remain available alongside it.
- a second cleanup pass closes the seven explicitly listed ordinary residual buckets with 12 reusable roots/relations and 5 additional anatomy/injury Old Names;
- the historical monster/divine/mana/meditation questions are now resolved into core Old Names; telepathy remains the only undecided history-dependent vocabulary item from that audit.

See `docs/world/YONA_PUBLISHED_THROUGH_168_VOCABULARY.md` and `docs/corpus/yona/CH01_168_V09_FULL_PUBLISHED_PASS.md`.

## Ongoing milestone 1 — corpus expansion + machine-readable language package

Continue corpus pressure while converting the written specification into structured data suitable for a reference implementation.

Near-term corpus targets:

- every currently published numbered chapter through 168 plus 94.5 has now received corpus pressure; the v0.9 full pass found no new structural gap beyond the already-closed G1–G16 set;
- the seven previously listed ordinary residual vocabulary buckets are closed, and monster/deity/goddess/old-mana/meditation are now historical Old Names; only telepathy remains historically undecided, alongside future world classifiers;
- preserve the Old/New historical distinction when adding any remaining source vocabulary;
- treat future newly published chapters as incremental regressions; keep major engineering effort on language stabilization, vocabulary balance, parser/spec agreement, and ambiguity testing. World execution and RequiredPower are deferred until the language is deliberately frozen enough and an actual game/use-case supplies requirements.

Surface syntax, the type hierarchy, executable lexicon/frame data, and compound rules are now machine-readable. Frame metadata already drives typed roles, optional arguments, event context, output typing, execution-closure alternatives, and collection/member binder relationships.

Next expand the structured package for:

- richer Categories/Traits and reusable frame constraints;
- dimensions and concrete Units;
- additional semantic molecules/normalizations;
- reference-resolution metadata;
- selector/control signatures that still require ordered or world-dependent values;
- world-model hooks, classifiers, generation profiles, and capability requirements.

Continue moving semantics into data whenever a rule can be expressed generically rather than adding one-off parser code.

Exit criterion:

A tool can load the language without hard-coding semantic rules throughout application code.

## Ongoing milestone 2 — expand reference parser and type checker

Implement the temporary surface syntax and semantic pipeline.

Required capabilities:

- segment whitespace-separated phrases while respecting pipe bridges;
- tokenize pipe-connected fields;
- parse compounds and typed prefix application;
- enforce full-consumption phrase parsing;
- bind roles/variables;
- type-check expressions;
- build AST;
- normalize semantic molecules/arithmetic;
- compute written mana cost;
- distinguish broad/contradictory/incomplete/ill-typed;
- return structured diagnostics.

Near-term parser work:

- refine exact inner spans for collection/group subexpressions beyond enclosing-phrase fallback;
- extend world-specific/non-canonical Unit packages only when corpus/world data requires them; core value-domain checks, Power/Root, and canonical Unit normalization are executable;
- normalization of additional semantic molecules;
- semantic-incompleteness/executability diagnostics for additional Processes;
- broader executable import of the existing stress/corpus suites;
- more reusable data-driven constraints between frame roles;
- ordered-value support needed before `First`/`Last` can become executable without inventing implicit ordering.

Exit criterion:

Every current static stress test can be represented and checked automatically.

## Ongoing milestone 3 — executable regression/fuzz testing

Deterministic fuzz-smoke testing is now active, and many written stress/corpus cases have executable counterparts. Continue converting `STRESS_TESTS.md` cases and expand generated/fuzz coverage for:

- root compounds;
- Process frames;
- nested conditions;
- collection/binder structures;
- numeric/dimensional expressions;
- ambiguous grouping cases;
- invalid references;
- contradictory Attribute families.

The goal is specifically to make the implementation expose holes in the written language.

Every newly found ambiguity should become a permanent regression test.

## Deferred post-language milestone — minimal objective world package

This is **not current work**. Do not begin concrete world classifiers/physics simply because the expression language can describe them.

Revisit this only after:

- the language has reached an explicit stability/freeze point;
- remaining root/Old Name/New Name cleanup is substantially complete;
- parser/spec behavior is aligned enough for a v1 language target;
- the intended game/simulation/use-case is known well enough to determine what fidelity and abstractions the world model actually needs.

At that future point, a small reference world may contain examples such as:

### Units/dimensions

- one canonical Length unit;
- one Time unit;
- Mass;
- thermal;
- Light;
- Mana/MagicPower.

### Material Kinds

At minimum:

- Water
- Iron
- Stone

### Biological Kinds

At minimum:

- Human
- Wolf
- Oak/Tree
- Hand/anatomy examples.

### Artifact Kinds

At minimum:

- Container
- Door
- Sword

### Physics/setting rules

Enough deterministic behavior for:

- movement;
- phase;
- heat;
- damage/repair;
- visibility;
- life state;
- basic resistance.

This future world package would test a chosen magic-system/game execution model. It is not part of proving that the language itself is linguistically ready, and it need not resemble the final campaign setting.

## Deferred post-language milestone — magical balance / RequiredPower

RequiredPower is explicitly game/magic-system work. Define objective gameplay formulas/tables only after a concrete execution model and game design exist.

Need to calibrate:

- mass/extent scaling;
- distance;
- Attribute delta;
- transformation complexity;
- creation;
- biological resistance;
- target count;
- duration;
- persistence;
- active Magic resistance;
- information search;
- competing commands.

The balance layer should not alter sentence meaning.

## Completed milestone V — cross-genre anti-overfitting corpus pass

_Pride and Prejudice_ and the 1818 _Frankenstein_ were audited as deliberately non-Yona corpora.

- neither novel exposes a new grammar/type-system gap;
- social, emotional, kinship and learning semantics were the main weak area;
- 33 general core entries were added rather than book-specific packages;
- historically specific institutions remain world/history data;
- the result strengthens confidence that broad grammar is converging, but does not end language work; the active priority remains language cleanup, ordinary-language breadth, parser/spec agreement, and targeted anti-overfitting tests.

See `docs/corpus/cross_genre/PRIDE_PREJUDICE_FRANKENSTEIN_V10_PASS.md`.

## Completed cleanup checkpoint — classify the whole executable inventory

The raw executable count is now separated from the actual primitive-root inventory.

Every registered base entry has one machine-readable role in `language/core/inventory_roles.json`. After the current resolution checkpoints, 118 semantic primitive candidates remain out of 210 registered entries; 12 unresolved candidates remain, alongside formal constructors, references, and domain values. No registered derived candidates remain.

The next reduction work should target **families**, not English-word-by-English-word deletion:

- direct noun Kind migration — completed for Human, Cat, Water, Body, Hand, and Sound;
- generic extrema selection — completed with MinBy/MaxBy;
- High/Low threshold-property machinery now covers both contextual directions; preserve genuinely multi-threshold and non-scalar distinctions;
- epistemic confidence thresholds — completed for PossibleTo, ProbableTo, and CertainTo;
- unify temporal/frequency wrappers;
- then revisit unresolved ordinary/social/action vocabulary.

See `docs/PRIMITIVE_DERIVED_INVENTORY.md`.

## Completed reduction checkpoint — noun Kinds and extrema family

- Human, Cat, Water, Body, Hand, and Sound are now concepts + provisional Old Names rather than primitive Kind roots.
- binder domains accept named Kinds;
- Nearest/Farthest/Highest/Lowest are replaced by generic tie-preserving `MinBy` / `MaxBy`;
- executable core: **284 → 276** for this checkpoint;
- direct noun/name migration candidates: **6 → 0**;
- derived candidates: **36 → 32**.

## Completed cleanup checkpoint — generalize measurement units

Six special Unit constructor rune entries were replaced by one productive `Unit` root plus typed Old Names, taking the raw rune/base-sign inventory from 282 to 277 while preserving typed dimensional arithmetic. The later reductions bring it to 210.

## Active cleanup — reduce the primitive/root inventory

The core executable registry has begun a reduction-first audit.

Pass 1 removes 11 exact redundancies after restoring semantically distinct Inside/Outside, reducing the core from 306 to 295.

Pass 2 removes 11 more compositional entries and rebuilds affected draft Old Names, reducing the core from 295 to **284**. Removed in pass 2: Contain, Get, Join, Separate, Tell, See, Hear, Smell, Taste, ChangeBy, and Converse. Inside/Outside were restored because the detailed geometry spec proves they preserve distinctions not expressible as plain In/Not In.

Pass 3 removes Between, Ask, and TimeOverlap. Their exact executable meanings are now comparison composition, Say + QuestionContent, and typed general Overlap respectively. Later cleanups remove AwayFrom in favor of Opposite Toward and DirectPart in favor of Part plus an explicit no-intermediate-part condition. Former is now Before(state,Now) + Not bare-present state; the duplicate Information Kind is removed in favor of the semantic Information type; and KnowAnswer is existential Know + AnswerFor. Increasing/Decreasing now use generalized ChangeRate plus typed Zero, ApproxEqual is tolerance-bounded difference composition, Sometimes is Happen over the relevant interval, and Members is Collect + Member over a group, and Stop is the EventSpec overload of End on a concrete Event, and Teach is agentive Cause of a typed `Begin Know` / `Begin Can` / `Begin Understand` acquisition transition, and Prefer is ordered evaluation with More + Evaluate, and SiblingOf is shared ParentOf composition with distinctness, Long/Hungry/Often are High-based contextual threshold constructions, PossibleTo/ProbableTo are Confidence threshold compositions, Injured is HighDamage, Stable is an explicit ChangeRate bound, Rarely is Low OccurrenceRate, Sated is LowHunger, ImportantTo is High Evaluate, CertainTo is equality with the complete-confidence endpoint, Continue is present-boundary prevention of End(Event), Period is reciprocal OccurrenceRate, Present is bare state / During-at-Now for EventSpecs, Completed is Before-the-reference-boundary, Ongoing is EventSpec During, Big/Small are HighExtent/LowExtent, Past/Future are argument-orderings of Before, Always is Proposition During, LocalDensity is a Density overload, Height/Width are axis-indexed Extent, Grow is constrained Change(Extent), Promise is Say + Begin contextual Obligation, Same is Entity Equal, Detected is Happen Sense, MethodFor is Purpose, and Using is a Use relation frame. The next four reductions then make Habitual `High OccurrenceRate`, Depth the third `Extent` axis, Thank addressed `Say` of `GratefulTo`, and Apologize addressed `Say` of `RemorseFor`. The following batch makes Whenever `During SufficientFor`, NextOccurrence the EventSpec overload of `First`, Redistribute Distribution-valued `Transfer`, and generic discourse Because contextual `Explains`. The next four remove Almost through false-side low boundary distance, Should through `High Evaluate`, DesignedFor through `Purpose`, and Learn through typed `Begin Know` / `Begin Can` / `Begin Understand`. The following batch removes Generic through contextual high prevalence, folds Size and Span into the general `Extent` family, and folds CommittedTo into `Obligated ... :context ...`. The next four remove Teleport through discontinuous `At` state boundaries, Write through `Cause + Begin Exist` for Sign, Read through `If Sign S (Sense A S)` interpreted-Sign sensing, and Grab through concurrent `Begin Touch` + `Begin Control`. The following batch removes Consent/Refuse through addressed permission assertion/denial, Deceive through causation of a false belief state, and Sever through agentive `Cause` of `End Whole` with optional instrument. The next four audit passes retain Meaning, About, DistributionOf, and TotalAmount as semantic primitive candidates because no exact surviving composition preserves their interpretation/topicality/field-construction/aggregation semantics. The registered base inventory remains **210**.

Next reduction work should proceed family-by-family:

- draft Old Names do not protect roots from removal; pass 2 demonstrates rebuilding them after deletion;
- channel-specific sensing, state-boundary verbs, selectors, change helpers, modal/frequency conveniences, and recently added social/cognitive verbs are strong candidates for compositional replacement;
- the first six direct noun migration candidates have been removed from the primitive inventory;
- every deletion must preserve truth conditions and pass corpus/parser regressions; Old Name spellings/costs may change during this design phase.

See `docs/ROOT_MINIMIZATION_AUDIT.md`.

## Current milestone — language stabilization and extended ordinary-language coverage

The core language is adequate for magic-focused formal expression and has now survived two non-Yona full-novel stress tests. Ordinary-language coverage still needs gradual vocabulary growth, but the cross-genre pass closes a major social/emotional/cognitive imbalance with 33 new productive entries.

Expand/test:

- pronouns/anaphora;
- social concepts;
- modality;
- discourse relations;
- reported speech;
- questions/answers;
- tense/aspect shortcuts;
- names/titles;
- comparison standards;
- everyday artifact vocabulary.

Ordinary discourse may permit controlled contextual resolution that magical Commands do not.

## Next milestone 7 — player-facing progression design

Convert the lexical metadata into practical discovery/teaching layers:

- beginner starting dictionary;
- intermediate expansions;
- advanced mathematical/control vocabulary;
- lost/restricted roots;
- teaching/research rules;
- player-facing examples.

Check that beginners can create useful effects without knowing the full formal system.

## Next milestone 8 — rune glyph system

Only after parser semantics are stable:

- design root glyph families;
- encode grammatical case/grouping/binders visually;
- develop compound layout;
- ensure legibility;
- ensure every glyph form maps uniquely to AST;
- create a font/asset workflow if useful.

Glyph aesthetics must not alter meaning.

## Next milestone 9 — reference manual / game supplement

Produce final player/GM documentation:

- language introduction;
- rune dictionary;
- grammar;
- spell construction;
- mana/Power rules;
- examples;
- progression;
- world integration;
- troubleshooting/diagnostics.

## Working rule

Do not consider the written semantic phase "finished" merely because the documents are internally plausible.

The next serious test is independent executable interpretation.

Implementation failures should drive further language revision before final glyphs and publication.
