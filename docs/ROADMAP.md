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

The first lexicon slice should be just large enough to make the v0.2 surface tests executable before attempting the entire dictionary.

Exit criterion:

A tool can load the language without hard-coding semantic rules throughout application code.

## Ongoing milestone 2 — reference parser and type checker

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
