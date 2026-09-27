# Roadmap

_Last updated: 2026-09-27_

This is the current recommended work order. Earlier semantic-design phases are retained here as completed milestones so a new thread can see what changed.

## Completed milestone A — lexical semantic architecture

Completed:

- eight-category lexical type architecture;
- traits/frames/constraints;
- Opposite / Not / Converse separation;
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

- Entity identity / Same / Exist;
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

Completed first passes:

- Yona Chapter 1 opening/general discourse;
- Chapter 1 market and investigation prose;
- Chapter 1 System/dialogue remainder;
- Chapter 14 targeted mana-manipulation/body-construction material.

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
- `language/core/lexicon_minimal.json`
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
- Converse through declared relation-converse mappings;
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

A GitHub Actions workflow now runs the complete Python unittest suite on Python 3.11 and 3.12 after every push.

The v0.3 migration adds 11 parser/surface regression checks; the executable suite now contains 40 passing tests.

## Ongoing milestone 1 — corpus expansion + machine-readable language package

Continue corpus pressure while converting the written specification into structured data suitable for a reference implementation.

Near-term corpus targets:

- another body/evolution-heavy chapter;
- the dedicated mana-explanation chapter;
- a dialogue/social-heavy chapter;
- enough sequential Chapter 1/2 material to test discourse continuity across chapter boundaries.

Surface syntax metadata is now machine-readable.

Next create schemas/data for:

- lexicon entries;
- Categories/Traits;
- callable frames/roles/optional positional prefixes;
- compound rules;
- Attributes/families;
- dimensions/Units;
- semantic molecules;
- normalizations;
- selector/control signatures;
- world-model hooks.

The first executable lexicon slice is complete. Next expand it domain-by-domain, prioritizing roots used by current stress tests and corpus translations.

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

- more complete type/dimension/unit relations;
- normalization of additional semantic molecules;
- semantic-incompleteness/executability diagnostics for additional Processes;
- selector/collection and state-relation coverage;
- richer question/discourse nodes;
- better source-span diagnostics;
- executable import of the existing stress/corpus suites.

Exit criterion:

Every current static stress test can be represented and checked automatically.

## Next milestone 3 — executable regression/fuzz testing

Turn `STRESS_TESTS.md` into executable tests.

Then generate/fuzz:

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

## Next milestone 4 — minimal default world package

The formal language now needs concrete data to test full spell execution.

Create a small reference world containing enough examples to exercise the system:

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

This world package is for testing the language, not necessarily the final campaign setting.

## Next milestone 5 — magical balance / RequiredPower

Once semantic execution works mechanically, define objective gameplay formulas/tables.

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

## Next milestone 6 — extended ordinary-language coverage

The core language is now adequate for magic-focused formal expression, but a claim of a "fully usable ordinary language" needs more work.

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
