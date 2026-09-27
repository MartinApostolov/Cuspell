# Roadmap

_Last updated: 2026-09-27_

This is the current recommended work order. Reorder it when stress tests show a better dependency path.

## Phase 1 — Stabilize lexical semantics

Resolve the current high-risk roots whose English labels hide multiple possible meanings:

- Part
- Whole
- Kind
- Of
- By
- End
- Start / Begin
- Form
- Surface
- Volume
- Magic
- Copy
- Disease
- Memory
- Name

For each root, record:

- Category
- Domain
- Traits
- Compound/argument frames
- Constraints
- Reversible mapping if any
- Whether the English label hides multiple runes

Exit criterion: the type system can explain these roots without informal "you know what it means" interpretation.

## Phase 2 — Sentence grammar and semantic roles

Formalize how Processes, Relations, References, Kinds, Properties, quantities, and logical operators form propositions and commands.

Important roles likely include:

- agent
- patient/theme
- experiencer
- stimulus/content
- source
- destination
- location
- instrument
- beneficiary
- result
- cause
- condition
- time
- duration

Also define:

- Proposition
- Event
- Command
- scope and grouping
- quantifiers
- conditionals
- conjunction/disjunction
- relation converse
- how multiple actions compose

Exit criterion: nontrivial multi-action sentences have one machine-derivable semantic structure.

## Phase 3 — Specific Kinds / noun problem

Solve objective reference to concepts such as:

- Water
- Iron
- Stone
- Oak
- Tree
- Wolf
- Human
- Hand
- Fire
- House
- Door
- Sword

Evaluate a mixture of:

- primitive Kinds;
- formally defined semantic molecules;
- relationally restricted Kinds;
- reference-by-example / same-Kind mechanisms;
- conventional language-level compounds.

Constraint: user-defined aliases must not automatically reduce mana.

## Phase 4 — Numbers, measurement, geometry, and scales

Finalize:

- unary quantities;
- Zero and negatives;
- multiplication/compression;
- ratios / Part semantics;
- dimensional quantities;
- units;
- vectors/directions;
- distance, range, area, volume;
- duration;
- scalar comparisons;
- fixed vs contextual thresholds.

## Phase 5 — Magical execution semantics

Define what reality does with a valid Command.

Specify:

- mana accounting;
- target/reference resolution;
- insufficient mana;
- impossible but well-typed commands;
- contradictory constraints;
- underspecified commands;
- commands whose required referent does not exist;
- underpowered transformations;
- partial execution vs atomic failure;
- persistence;
- triggers;
- repetition;
- dispelling;
- interaction between simultaneous commands.

## Phase 6 — Vocabulary layers

Separate:

1. full language inventory;
2. magically meaningful vocabulary;
3. beginner caster vocabulary;
4. hidden/advanced vocabulary.

Do not force every ordinary-language rune to be magically executable.

## Phase 7 — Large-scale stress testing

Construct many examples across domains:

- matter/physics
- space/motion
- life/healing
- mind/perception
- information
- time
- social language
- multi-action spells

Search for:

- multiple legal parses with different meanings;
- hidden English assumptions;
- unnecessary primitives;
- missing primitives;
- contradictions treated as type errors;
- unsafe alias-like compression loopholes.

## Phase 8 — Reference implementation

Once the written specification is stable enough, implement a parser/type-checker.

Use it to:

- parse compounds;
- normalize semantics;
- reject ill-typed expressions;
- detect contradictions;
- compute mana cost;
- fuzz-test random combinations;
- prove whether two expressions normalize to the same meaning.

This is where Codex becomes especially useful.

## Phase 9 — Rune glyph design

Design the actual written glyph system only after the semantic language is stable enough that glyph structure can reflect useful relationships instead of freezing premature assumptions.
