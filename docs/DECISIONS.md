# Design Decisions

This file records important accepted/rejected choices so later work does not silently regress them. Git history records wording changes; this file records design intent.

## Accepted

### D-001 — Complex commands are allowed

Do not impose a one-action-per-spell rule. If a complex sentence is grammatically valid, semantically objective, and executable, magic may execute it.

### D-002 — Language and magic are separate layers

The complete language may contain concepts irrelevant to spellcasting. Beginner, magical, ordinary, and hidden/advanced vocabularies may differ.

### D-003 — Meaning-bearing writing costs mana

Every meaning-bearing rune occurrence written in a magical Command costs mana. Pure grammar/syntax can cost zero.

### D-004 — Genuine linguistic compression may reduce mana

Do not charge the expanded semantic value. Shorter registered expressions, semantic molecules, and mathematical compression may genuinely cost less mana.

### D-005 — Not, Zero, Opposite, and Converse are distinct

- Not = logical complement.
- Zero = numerical value 0.
- Opposite = declared semantic-axis inverse.
- Converse = declared participant-role reversal for Relations.

None may be substituted for another by intuition.

### D-006 — No free minus sign

Negative values require a meaning-bearing operation such as Opposite on a Quantity.

### D-007 — Typed composition replaces universal modification

There is no universal rule `AB = B satisfying A`. Compounds compose only through registered categories, traits, frames, families, and constraints.

### D-008 — Eight core lexical Categories

Current root Categories are:

- Entity
- Kind
- Property
- Relation
- Process
- Quantity
- Reference<T>
- Operator

Derived structures such as Proposition, EventSpec, Event, Collection, Region, and GeometryProfile do not require new lexical root Categories.

### D-009 — State, scalarity, family membership, and reversibility are traits/frames

Do not create top-level Categories for State or Axis. Use state-predicate, scalar-attribute, family, reversible, functional, and similar typed metadata.

### D-010 — Broad is not ambiguous

A broad expression such as `LiquidMatter` can have one exact denotation while selecting many possible members. Broadness, ambiguity, contradiction, and type error are separate outcomes.

### D-011 — Contradiction is not a type error

A construction may be well-typed but impossible to satisfy, such as incompatible exclusive family values on one homogeneous subject.

### D-012 — RGB-like color basis with separate intensity

Red, Green, and Blue are the working chromatic basis. Balanced RGB does not automatically mean White; visible Light/intensity is separate. Weighted chroma uses Ratio, not repeated roots or Part.

### D-013 — Arbitrary aliases do not grant magical compression

Names, abbreviations, local definitions, and player-created macros do not become magical lexical entries.

### D-014 — Do not aggressively minimize the rune inventory

Clarity/objectivity outrank a small primitive count. Common semantic molecules and canonical noun roots are allowed.

### D-015 — Typed References are mandatory

References have result types and formal resolution rules. A singular slot requires exactly one compatible result. References do not silently search or guess.

### D-016 — Scalar Attributes are functional relations

Heat, Light, Mass, Length, Duration, Distance, etc. are modeled as value-returning Attributes rather than vague Boolean Properties.

A typed shorthand such as `ZeroLight` may generate a Property meaning the scalar Attribute equals zero.

### D-017 — Dimensional arithmetic is part of the language

Quantities carry dimensions/units. Arithmetic is dimension-checked. Mathematical compression remains mana-efficient.

### D-018 — Begin and End are coherent boundary Operators

Begin/End act on persistent state predicates/Relations and on Event boundaries through typed frames. The separate primitive candidate Start is folded into Begin.

### D-019 — Part is structural; Whole is completeness; Ratio is numerical

- Part = mereological/structural relation.
- Whole = integrity/completeness Property.
- Ratio = numerical/proportional construction.

The earlier numerical use of Part is superseded.

### D-020 — Generic magical Of, By, and For are rejected

English linkers collapse too many relations. Formal/magical expressions use the actual typed relation: Part, Have, DesignedFor, Beneficiary, Using, etc. Conversational umbrella words may exist outside magical execution.

### D-021 — Generic KindOf(This) is not a magical shortcut

An Entity belongs to many Kinds. Classification by example must state the classification dimension/level (species, substance, design, etc.).

### D-022 — Superseded: ordinary noun Kinds as direct lexical roots

Earlier policy allowed Water, Iron, Wolf, Hand, Sword, etc. to become direct registered Kind roots. D-074 supersedes this as the default for culturally ordinary vocabulary. Existing executable roots remain temporarily until migrated safely.

### D-023 — Kind identity is separate from temporary state

Material Kind is separate from Phase; biological/artifact Kind can survive damage or temporary state change. Identity-essential and typical properties are distinct.

### D-024 — Create, Transform, Restore, and Destroy are distinct

- Create allocates a fresh Entity identity.
- Transform changes a profile while preserving identity by default.
- Begin(Exist(X)) may restore/reinstate an already identifiable non-active X where world metaphysics permits.
- Destroy ends active Existence.

### D-025 — Life is distinct from Existence

EndLife is not Destroy. A corpse may still Exist and retain historical biological classification.

### D-026 — State predicates may be Relations

Persistent Relations such as Have, Know, Remember, In, and Joined may undergo Begin/End transitions. Common verbs such as Learn, Forget, Get, Lose, Enter, and Exit may lexicalize such transitions.

### D-027 — EventSpec, Event, Proposition, and Command are distinct

A Process application describes an EventSpec. An Event is an actual occurrence. A Proposition is truth-bearing. Command mood submits an EventSpec/control structure for magical execution.

### D-028 — The caster is not an implicit Agent

The caster/issuer commands reality; they are not automatically a participant in the Event. Agent is represented only when the Process semantics require it.

### D-029 — Grammar may be zero-mana

Grouping, mood, case/role marks, binders, variable references, collection punctuation, quotation marks, and separators are syntax and cost zero. The semantic roots/operators they organize still cost mana.

### D-030 — Quantification, collection, distribution, and selection are separate

- All/Some produce Propositions.
- Collect/Filter produce Collections.
- Each distributes an EventSpec.
- selectors such as Unique/Nearest/Highest/Random explicitly choose/reduce.

A Kind or Some never silently chooses a target, and a Process never silently distributes over a Collection.

### D-031 — Selector ties are explicit

Extrema selectors return all tied results by default. A singular role normally requires Unique or another explicit tie policy. Random is allowed only when explicitly written.

### D-032 — Information access is not implied by grammar

Questions, References, Collect, and selectors do not grant omniscience. Hidden information requires an explicit Sense/Find/Reveal-like capability.

### D-033 — Names are Relations, not identities or magic macros

Name(Sign, referent, context) can be many-to-many and context-sensitive. Naming does not change Entity identity or create magical lexical compression.

### D-034 — Copy initially applies to Information, not arbitrary physical Entities

Copy duplicates registered Information/Sign content into a distinct token/record. Physical replication requires explicit Create/profile semantics.

### D-035 — Join/Separate are state transitions, not a universal Opposite pair

Use Joined(A,B) as a structural state Relation. Join can Begin Joined; Separate can End Joined. Do not assume `OppositeJoin = Separate` for every structural domain.

### D-036 — Purpose/design is distinct from temporary Use

Artifact Kinds use objective Purpose/DesignedFor relations. Using a rock as a hammer once does not automatically change its Kind.

### D-037 — Contextual ordinary words do not become vague magic

Near, Far, Hot, Cold, Good, Bad, Many, Few, etc. may exist in ordinary language, but magical use requires a fixed lexical standard or explicit comparison parameter.

### D-038 — Power is separate from linguistic mana

Working execution model: the written runes determine linguistic mana cost; a Command can also supply a typed Power quantity used against objectively computed RequiredPower.

Numeric compression of Power remains genuine mana compression. Exact requests do not automatically scale down when underpowered or scale up when overpowered.

### D-039 — Exact commands fail rather than inventing a weaker result

If a closed exact EventSpec lacks enough Power/capability, default behavior is no realization of that EventSpec. Partial/scalable behavior must be explicitly requested by semantics.

### D-040 — And and Sequence have different execution semantics

- And over EventSpecs is an unordered joint composite and is transaction-like at its result boundary.
- Sequence executes in order; completed earlier steps are not freely rolled back if a later step fails.

### D-041 — Persistence is active maintenance, not ordinary consequence

Natural consequences continue under world law without Persist. Persist actively maintains a specified state/relation/process for an explicit lifetime/end condition and creates an active Magic state.

### D-042 — Trigger and Repeat require explicit finite/well-founded control

Trigger has explicit lifetime and witness-binding when needed. Repeat has explicit finite count unless a persistent conditional recurrence is constructed. Infinite zero-time activation chains are non-executable.

### D-043 — World ontology and balance are separate from language semantics

The core language defines grammar/types/meaning. A versioned world package supplies material/biological classifiers, Units, geometry defaults, physical/metaphysical rules, capability restrictions, generation profiles, and RequiredPower calibration.

### D-044 — Temporary surface syntax is structural, not the final glyph system

The current ASCII syntax is a deterministic reference notation for testing. Future rune glyphs may encode the same AST differently but may not introduce ambiguity.

### D-045 — Kind predication is explicit

A Kind may be used predicatively of an Entity and normalizes to InstanceOf(entity, Kind). This is separate from Property + Kind restriction and from selecting a member of a Kind.

### D-046 — Ordinary discourse may be contextual; magic must resolve it

Connected discourse may use anaphora, definite descriptions, proper-name shorthand, generics, narrative reference time, and contextual evaluation. Before such content participates in magical execution, it must normalize to a closed objective structure or be rejected.

### D-047 — Nested speech changes deictic context

Direct/reported speech uses nested utterance contexts. Self, You, Here, and Now inside embedded speech resolve relative to the embedded speaker/addressee/time/place rather than automatically to the outer narrator/caster.

### D-048 — Generic is not All

Natural-language generic claims are not strict universal quantification. Generic/Typical discourse is contextual and ordinarily non-magical; objective magical logic uses All, Most, explicit proportions, or registered Kind defaults.

### D-049 — Evidence is not Cause

Perception/evidence, belief, and assertion do not automatically become world truth or causation. EvidenceFor/Against, Confidence/Believe, Assert, and Cause remain distinct semantic relations.

### D-050 — Stop and Prevent are distinct

Stop terminates an already ongoing resolved Event/process pattern. Prevent constrains future matching Events over an explicit scope/interval. Prevent is persistence-like for magic.

### D-051 — Relative changes use snapshots; preservation is event-boundary only

BeforeValue/AfterValue provide event-boundary snapshots. Preserve constrains selected values to remain equal across an Event boundary. Preserve is distinct from Persist, which actively maintains a condition through time.

### D-052 — Form similarity does not imply Kind identity

ShapeLike/SimilarForm can compare geometry to a template/Kind profile without asserting InstanceOf. A hand-shaped mana construct can therefore remain not-a-Hand.

### D-053 — Control is distinct from Have, Use, and Command

Control(controller,target/process) is a persistent relation about intentional manipulability. It does not imply ownership, tool use, or magical command issuance.

### D-054 — Spatially varying resources may use Distribution values

World packages may represent resources/fields as spatial Distributions with local density and total amount. The core type system supports such structured values without assuming every scalar Attribute is uniform.

### D-055 — Whitespace separates phrases; pipe binds application

Surface syntax v0.2 changes the role of `|`.

- adjacency with no separator remains lexical compound formation;
- unbridged whitespace ends the current expression/phrase;
- `|` explicitly binds connected fields into one application phrase.

Thus `Move|A|B|C` is one application phrase, while `Move|A|B C` contains `Move(A,B)` followed by a separate source expression C.

Whitespace itself has no semantic meaning and never supplies free And/Sequence semantics.

### D-056 — Pipe phrases use typed prefix parsing

One pipe-connected phrase must parse to exactly one full-consumption semantic expression.

Registered frame arity, slot types, functional outputs, role markers, and context determine nested boundaries.

If multiple distinct semantic parses survive, the phrase is invalid until explicitly grouped or rewritten.

### D-057 — Parentheses are fallback grouping, not normal syntax

Under v0.2, uniquely typed nested expressions should normally be written flat.

Parentheses remain zero-mana hard grouping for ambiguous cases, deliberate readability, and complex variadic structures.

### D-058 — Event-local BeforeValue/AfterValue may omit the event

Inside exactly one enclosing EventSpec result/value context, BeforeValue/AfterValue may omit their Event argument and resolve to the nearest enclosing event boundary.

Outside such a unique context the Event must be explicit.

### D-059 — Known-root concatenation is not automatically a legal compound

The executable parser may segment an adjacent transliteration into registered roots, but the result is valid only when a registered compound rule licenses the composition. If segmentation succeeds but composition does not, report IllegalCompound rather than UnknownRoot.

### D-060 — Contradiction checking follows typing

A well-typed expression can still carry unsatisfiable constraints. The reference validator now treats incompatible exclusive-family values and direct P + NotP requirements as ContradictoryConstraint rather than TypeMismatch.

### D-061 — EndLife is composition, not a special parser primitive

The executable lexicon derives EndLife from the general End state-boundary Operator applied to Life. Its written cost remains End + Life. This keeps the parser aligned with the semantic rule that Begin/End operate on persistent state predicates.

### D-062 — Command closure is checked after semantic validity

A Process phrase can be meaningful and type-correct while still leaving execution-relevant choices unconstrained. Command mood therefore runs an additional closure stage after parsing/type/constraint validation.

For Move, a magical Command must currently bind at least one of goal or path. Missing closure is SemanticallyIncomplete, not TypeMismatch.

### D-063 — Incomplete, contradictory, and invalid are distinct checker outcomes

The CLI should surface SemanticallyIncomplete as INCOMPLETE and ContradictoryConstraint as CONTRADICTORY rather than collapsing both into a generic INVALID heading. Structured diagnostic codes remain authoritative for tooling.

### D-064 — Whitespace is ordinary token separation; pipe is hard binding

Surface syntax v0.3 supersedes D-055's v0.2 interpretation.

Whitespace separates normal written tokens, and registered typed frames infer application/nesting across that stream. Pipe explicitly hard-binds the connected tokens into one complete subexpression before the surrounding stream is parsed.

Thus `Move This Here` is the normal form; `Move|This|Here` is an explicit equivalent; and `Move|This Here` closes the hard group after This.

Whitespace still has no semantic And/Sequence meaning.

### D-065 — Parser changes must be continuously regression-tested

The repository now uses GitHub Actions to run the parser suite on supported Python versions after pushes. Language/parser milestones should add executable regression cases before being treated as stable implementation behavior.

### D-066 — Dimension-changing Power/Root require statically known degree

Power and Root always take a dimensionless numeric exponent/degree.

If the base/radicand is dimensionful (or not statically proven dimensionless), that exponent/degree must have an exact statically known value so the resulting dimension can be validated and typed. A runtime-variable exponent/degree is legal only when the base/radicand is statically `Quantity:Number`, because its result remains dimensionless regardless of the runtime value.

For known dimensional inputs, Power scales dimension exponents by the exponent. Root divides dimension exponents by the degree and is valid only when every resulting dimension exponent remains integral in the current integer-exponent dimension model. Root degree zero is invalid.

### D-067 — Embedded questions and directives are Information values

Question and directive force must survive when speech is narrated inside another sentence.

`Question(Proposition)` and `Question(Binder, Proposition)` construct `QuestionContent`, while `Directive(EventSpec)` constructs `CommandContent`. Both are Information values and can therefore be embedded in speech acts without becoming active top-level Question or Command mood.

`Ask` consumes QuestionContent. `Tell` can transfer Information, including CommandContent. Quoted Signs remain distinct from semantic speech-act content.

`Almost(EventSpec)` is an ordinary contextual Proposition describing near occurrence/non-completion of an EventSpec; it is not a magical instruction and does not choose a hidden numeric tolerance.

`Permitted` carries an optional explicit authority/context role so permission is not silently treated as global.
### D-068 — Canonical prose is flat; adjacency may tightly bind local applications

Normal player-facing Cuspell must read as a flat sequence of rune units rather than expose the semantic AST with routine parentheses.

Direct adjacency has two typed roles:

1. registered lexical composition such as `SolidWater` or `EndLife`;
2. tight local application such as `CatSelf`, `LifeThis`, or `DensityThis`.

Resolution order is exact registered root, licensed lexical compound, then one uniquely typed tight application of the segmented registered roots. Distinct surviving meanings are ambiguous and invalid.

Whitespace separates larger phrase units while typed prefix frames determine their semantic structure. Pipe and parentheses remain legal zero-cost hard-grouping/debugging tools but are not the canonical visual style.

Contextual relations may register shorter frames when the omitted role is genuinely supplied by discourse context. In particular `Evaluate target` uses the current discourse evaluator, while `Evaluate evaluator target` remains the explicit form.

Canonical benchmark:

`More Evaluate CatSelf Evaluate HumanSelf.`

The future rune script should preserve this flat structure; the Latin root names are only temporary transliteration labels.

### D-069 — Sentence-final punctuation carries mood

Canonical Cuspell no longer writes a mood prefix and then a separate final period.

The sentence-final mark performs both jobs:

- `.` = Assertion;
- `?` = Question;
- `!` = Command.

Examples: `CatSelf.`, `LifeThis?`, `MoveThisHere!`.

These marks are zero-mana grammar. The reference parser may temporarily accept the older `?Question.` / `!Command.` transliteration for compatibility, but new Cuspell text should use final mood punctuation.

### D-070 — Ordinary And/Sequence are linear; binders drop brackets

Canonical prose should not build visible Collection literals merely to express conjunction or ordered events.

- conjunction is infix: `A And B`;
- event Sequence is `Sequence E1 E2 ...`;
- the sentence boundary closes a Sequence when it reaches the end of the sentence;
- `SequenceEnd` is zero-mana grammar used only when a Sequence must stop before later material;
- Collection<T> remains a real semantic value for Count/Filter/Partition/selectors and other genuinely collection-valued operations;
- binder declaration is `a:Human`, with `$a` remaining the bound-variable reference spelling.

Legacy prefix-And collections, brace Sequence forms, and bracketed binders may remain temporarily parser-compatible for existing tests/documents, but are not canonical prose.

### D-071 — Counterfactual is distinct from actual-world If

`If` continues to evaluate its condition in the actual evaluation context. `Counterfactual(A,B)` is a contextual ordinary-language Proposition about a relevant contrary-to-actual alternative history where A holds and B follows.

Counterfactual does not assert A or B in the actual world and is not equivalent to Past, PossibleTo, or material implication. Because its alternative-history selection is contextual, it is not implicitly executable inside magic. Objective hypothetical-world execution requires a future explicit construction.

### D-072 — Or and Concurrent receive the v0.7 linear surface treatment

Corpus pressure supports extending the v0.6 naturalization rule:

- proposition disjunction is infix: `A Or B`;
- repeated Or chains remain linear;
- mixed bare And/Or has no implicit precedence and must be explicitly grouped;
- `Concurrent E1 E2 ...` is the canonical concurrent event surface;
- sentence end closes Concurrent when it is final;
- `ConcurrentEnd` is zero-mana grammar used only when Concurrent must stop before later material;
- legacy prefix/collection forms may remain parser-compatible.

This is a surface change only. And/Or/Sequence/Concurrent retain their distinct semantic structures.

### D-073 — Attempt is an event, not merely intention or failed success

`Attempt(agent, goal)` denotes a real goal-directed effort EventSpec.

It does not entail that the embedded goal occurs. It is distinct from `Intend` and `Plan`, which can hold without any attempt Event, and from `Cause`, which represents successful causation rather than trying.

This distinction is required by the full Yona Chapters 1–14 + 47 rerun, which repeatedly contrasts attempts with success, partial success, and failure.

A magical Command of Attempt commands the effort episode itself; it must not silently guarantee the embedded goal.

### D-074 — Old Names and New Names are different semantic privileges

Quoted `«... »` material is an exact Sign and may nest.

**New Names** are ordinary Name relations/references. They can name people, particular objects, newly coined Skills, foreign names, and similar current referents. They do not substitute the referent's meaning into magical execution and therefore cannot create cheap spell aliases.

**Old Names** are historically established pre-magic vocabulary with frozen meanings. They may denote world concepts or frozen semantic expressions and can be used directly in compatible semantic slots.

Old Name mana is the cost of the historical written name units, not the cost of its semantic expansion. This is legitimate historical lexical compression.

Old status cannot be created after the magical cutoff.

### D-075 — Common Old Names should fossilize earlier descriptions

For ordinary pre-magic objects/concepts, do not invent a one-word label merely because modern English has one.

Construct a plausible short description from semantic roots that already existed when the term arose, then let that description fossilize into the conventional Old Name.

The historical description need not be an exhaustive modern definition. Salient, functional, incomplete, or historically misleading descriptions are acceptable if they plausibly became conventional.

Concept identity remains separate from description: two world concepts may have identical descriptions and distinct exact names such as `«SharpStick»` and `«Sharp!Stick»`.

### D-076 — Old Name magical denotation is frozen against later semantic drift

An Old Name's magical meaning is fixed at the historical magical cutoff. Later slang, broadening, narrowing, renaming, or loss of the original motivation does not silently rewrite its magical denotation.

Current Name relations may therefore diverge from historical Old Name semantics.

### D-077 — Later Old Names may reuse earlier Old Names

Historical vocabulary can grow from vocabulary that already exists.

An Old Name `name_units` entry may therefore reference an earlier Old Name by ID. The referenced name contributes its full frozen historical mana cost recursively; nesting does not collapse the earlier name to a new one-mana unit.

The Old Name dependency graph defines historical precedence and must be acyclic. Circular name derivations are invalid.

This permits natural developments such as a later Ship name structurally reusing an already established Boat Old Name instead of rebuilding Boat from primitive roots.

### D-078 — Old Name etymology does not remain a live definition

An Old Name's `name_units` record historical formation and written mana cost.

Once the name is frozen, semantic use resolves to its world concept or frozen expression rather than re-evaluating the historical description as a current conjunction of properties.

Therefore a Ship historically named from Big + Boat remains a Ship even if a particular instance is not currently Big by the ordinary contextual standard. Objective world classifiers, not etymology, determine concept membership.

This permits natural, imperfect, historically contingent names without sacrificing magical objectivity.

## Rejected / superseded

- One action per magical command.
- v0.1 rule that `|` is merely a word/expression separator while whitespace is semantically ignored.
- D-055 / surface v0.2 rule that unbridged whitespace ends the current expression and pipe is ordinary application binding.
- Free zero-cost minus sign.
- Universal `AB = B that satisfies A` composition.
- Arbitrary aliases as free magical compression.
- Numerical use of Part.
- Generic magical Of.
- Generic magical By.
- Generic magical For as an English umbrella relation.
- Generic KindOf(This) classification shortcut.
- Start as a separate primitive from Begin.
- OneOf as an unspecified target selector.
- Generic Do as a required command verb.
- Universal physical Copy.
- `OppositeLife = undead`.
- Generic `OppositeJoin = Separate`.
- Treating Heat/Light/Length/Mass as merely Boolean Properties.
