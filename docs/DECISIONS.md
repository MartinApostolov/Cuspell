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

### D-005 — Not, Zero, and Opposite are distinct; Converse is not a primitive

- Not = logical complement.
- Zero = numerical value 0.
- Opposite = declared semantic-axis inverse.

A separate Converse rune is unnecessary. If a Relation is needed from the other participant perspective, write the same underlying Relation with its actual roles/arguments in the intended order. Do not turn role reversal into a meaning-bearing primitive.

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

### D-014 — Superseded: do not aggressively minimize the rune inventory

Earlier work prioritized convenience over primitive-count reduction. D-086 and the active minimization audit supersede that default.

Clarity and semantic precision still outrank a small count, but exact compositional duplicates should now be removed rather than lexicalized merely for convenience.

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

Earlier policy allowed Water, Iron, Wolf, Hand, Sword, etc. to become direct registered Kind roots. D-074 supersedes this as the default for culturally ordinary vocabulary. The first migration is now complete for Human, Cat, Water, Body, Hand, and Sound; they are concepts + provisional Old Names rather than direct roots.

### D-023 — Kind identity is separate from temporary state

Material Kind is separate from Phase; biological/artifact Kind can survive damage or temporary state change. Identity-essential and typical properties are distinct.

### D-024 — Creation, transformation, restoration, and ending Existence are distinct

The semantic distinctions remain important even where convenience verbs are not primitive roots.

- creation allocates a fresh Entity identity;
- transformation changes a profile while preserving identity by default;
- Begin(Exist(X)) may restore/reinstate an already identifiable non-active X where world metaphysics permits;
- End(Exist(X)) ends active Existence.

A standalone Destroy root is unnecessary because its intended meaning is exactly EndExist.

### D-025 — Life is distinct from Existence

EndLife is not Destroy. A corpse may still Exist and retain historical biological classification.

### D-026 — State predicates may be Relations

Persistent Relations such as Have, Know, Remember, In, and Joined may undergo Begin/End transitions. Do not automatically lexicalize ordinary verbs that are exactly those boundaries: acquisition/loss use BeginHave/EndHave, and joining/separating use BeginJoined/EndJoined unless a future verb proves to carry additional meaning.

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
- selectors such as Unique/MinBy/MaxBy/Random explicitly choose/reduce.

A Kind or Some never silently chooses a target, and a Process never silently distributes over a Collection.

### D-031 — Selector ties are explicit

MinBy and MaxBy return all tied extrema by default. A singular role normally requires Unique or another explicit tie policy. Random is allowed only when explicitly written.

### D-032 — Information access is not implied by grammar

Questions, References, Collect, and selectors do not grant omniscience. Hidden information requires an explicit Sense/Find/Reveal-like capability.

### D-033 — Names are Relations, not identities or magic macros

Name(Sign, referent, context) can be many-to-many and context-sensitive. Naming does not change Entity identity or create magical lexical compression.

### D-034 — Copy initially applies to Information, not arbitrary physical Entities

Copy duplicates registered Information/Sign content into a distinct token/record. Physical replication requires explicit Create/profile semantics.

### D-035 — Joining/separating use Joined state boundaries

Use Joined(A,B) as the structural state Relation.

- joining = Begin(Joined(A,B));
- separating = End(Joined(A,B)).

Standalone Join and Separate roots are removed. Do not recreate them through Opposite or aliases.

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

Perception/evidence, belief, and assertion do not automatically become world truth or causation. EvidenceFor, Confidence/Believe, Assert, and Cause remain distinct semantic relations. Evidence against P is written as EvidenceFor(..., Not P) rather than a separate root.

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

`Say` can transfer Proposition/Information/Sign content and may name a recipient, including carrying QuestionContent or CommandContent as Information. A separate `Ask` root is unnecessary when the content is already typed as QuestionContent. Quoted Signs remain distinct from semantic speech-act content.

`Almost(EventSpec)` is an ordinary contextual Proposition describing near occurrence/non-completion of an EventSpec; it is not a magical instruction and does not choose a hidden numeric tolerance.

`Permitted` carries an optional explicit authority/context role so permission is not silently treated as global.
### D-068 — Canonical prose is flat; adjacency may tightly bind local applications

Normal player-facing Cuspell must read as a flat sequence of rune units rather than expose the semantic AST with routine parentheses.

Direct adjacency has two typed roles:

1. registered lexical composition such as `SolidMatter` or `EndLife`;
2. tight local application such as `MatterSelf`, `LifeThis`, or `DensityThis`.

Resolution order is exact registered root, licensed lexical compound, then one uniquely typed tight application of the segmented registered roots. Distinct surviving meanings are ambiguous and invalid.

Whitespace separates larger phrase units while typed prefix frames determine their semantic structure. Pipe and parentheses remain legal zero-cost hard-grouping/debugging tools but are not the canonical visual style.

Contextual relations may register shorter frames when the omitted role is genuinely supplied by discourse context. In particular `Evaluate target` uses the current discourse evaluator, while `Evaluate evaluator target` remains the explicit form.

Canonical benchmark:

`More Evaluate MatterSelf Evaluate ThingSelf.`

The future rune script should preserve this flat structure; the Latin root names are only temporary transliteration labels.

### D-069 — Sentence-final punctuation carries mood

Canonical Cuspell no longer writes a mood prefix and then a separate final period.

The sentence-final mark performs both jobs:

- `.` = Assertion;
- `?` = Question;
- `!` = Command.

Examples: `MatterSelf.`, `LifeThis?`, `MoveThisHere!`.

These marks are zero-mana grammar. The reference parser may temporarily accept the older `?Question.` / `!Command.` transliteration for compatibility, but new Cuspell text should use final mood punctuation.

### D-070 — Ordinary And/Sequence are linear; binders drop brackets

Canonical prose should not build visible Collection literals merely to express conjunction or ordered events.

- conjunction is infix: `A And B`;
- event Sequence is `Sequence E1 E2 ...`;
- the sentence boundary closes a Sequence when it reaches the end of the sentence;
- `SequenceEnd` is zero-mana grammar used only when a Sequence must stop before later material;
- Collection<T> remains a real semantic value for Count/Filter/Partition/selectors and other genuinely collection-valued operations;
- binder declaration is `a:Domain`, where Domain may be a semantic type, primitive Kind, or registered named Kind such as `«Know«MoveLifeThing»»`; `$a` remains the bound-variable reference spelling.

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

**In the finalized language/world history**, an Old Name's magical meaning is fixed at the historical magical cutoff. Later slang, broadening, narrowing, renaming, or loss of the original motivation does not silently rewrite its magical denotation.

During the current language-design phase, however, the proposed historical vocabulary is still editable. Changing roots, rebuilding an Old Name, changing its historical description, or changing its frozen cost is allowed until a deliberate language/history freeze is declared.

Current Name relations may therefore diverge from finalized historical Old Name semantics.

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

### D-079 — Later technical senses are New Names even when spelling is old

Old-Name magical privilege attaches to a historically frozen denotation, not merely to a spelling.

If a later System, profession, science, game, or institution reuses an old-looking word for a new technical category, that technical referent is a New Name unless that exact specialized meaning predates the magical cutoff.

Thus Yona-world `«Skill»`, `«Class»`, `«Trait»`, `«Level»`, and similar System categories are New Names even if ordinary pre-magic Cuspell could have older unrelated concepts with comparable glosses.

World-specific New Names belong in opt-in world packages rather than the generic core world.


### D-080 — Graded ordinary states may pair an Attribute with a threshold Property

When ordinary language needs both a degree and a thresholded state, keep them distinct rather than forcing one root to do both jobs.

For example:

- `Hunger(subject)` returns an ordered degree;
- `Hungry(subject)` is the ordinary thresholded state;
- `Sated(subject)` is a separate thresholded state and is **not** declared the logical Opposite of Hungry.

Likewise, physical injury uses an ordered `Damage` Attribute plus the persistent `Injured` state.

Contextual thresholds remain acceptable in ordinary language, but magical use requires objective closure/world calibration.

Camouflage follows the same principle: `CamouflagedAgainst` is contextual and observer/background-sensitive, while concrete appearance remains available through `ColorOf` and `TextureOf`.


### D-081 — Yona ranks and progression-option labels remain setting-specific New Names

Yona-world metal ranks and progression choices are later technical labels, not Cuspell historical vocabulary.

Register exact source-backed labels such as `«Bronze»`, `«Silver»`, `«Gold»`, `«Platinum»`, named evolution options, and named Skill upgrades in the opt-in Yona package as New Names/world concepts.

Do not grant Old-Name magical compression to the component words or to the full technical label merely because the spelling looks ordinary.

When a source presents a finite option set but names only some members, register only the exact names actually exposed by the source. Do not invent the unnamed options.

Ordinary meditation may be historically old while the Yona System Skill `«Meditate»` and its named upgrade branches remain New Names; ordinary and technical senses are separate referents.


### D-082 — Historical monster, deity, mana, and meditation vocabulary is frozen separately from later technical senses

The supplied pre-magic history settles four previously deferred vocabulary areas.

- Monster is an Old concept named `«AttackHumanThing»`: the wording records an ancient human-danger framing, not a live requirement that every Monster currently attack humans.
- Deity is an Old concept named `«WorshipThing»`: people had objective evidence of gods before executable magic, but being worshipped is historical etymology rather than the live deity classifier.
- Goddess is the later Old Name `«Female«WorshipThing»»`, reusing the Deity Old Name.
- Pre-magic mana is the Old Name `«Use«WorshipThing»Magic»`, reflecting an older understanding of mana as god-used/divine magic before ordinary people could use magic directly.
- Ordinary meditation is the Old Name `«AwakeSleep»`, a fossilized "waking sleep" description rather than a live logical conjunction.

The productive roots `Female` and `Worship` are ordinary language roots, not religion-specific macros. Worship does not entail that its object is objectively divine.

The old Cuspell mana concept and setting-specific technical terms such as Yona `«Mana»` are distinct referents even though they share the English gloss.

No generic `Divine` root or Old Name is introduced yet. Its objective semantic boundary should be defined by later world ontology rather than guessed from the historical deity vocabulary.

Telepathy remains historically undecided.


### D-083 — Full published-corpus pressure does not justify speculative core vocabulary or grammar

The Yona corpus through numbered Chapter 168 plus the 94.5 interlude has been audited against the current language.

No new grammar, semantic type, or general semantic molecule is required for translation completeness after the existing G1–G16 closure.

Later source pressure is therefore classified by default as world/name data unless a future passage demonstrates a genuinely unrepresentable reusable truth condition.

Yona technical labels such as `Connection`, `Telepathy`, `Epithet`, `Skill Morph`, Dungeon subtypes, Classes, Professions, Traits, Titles and Soul Weapons remain opt-in New Names/world concepts.

In particular, registering Yona `«Telepathy»` as a Skill does **not** settle the history of generic telepathy in Cuspell. Core receives no Telepathy Old Name until the pre-magic history is decided.

The later novel also supplies strong world-ontology pressure for Soul, undead/reanimation, Curse/Blessing/Sacred/Divine, and healing/regeneration. These are not silently promoted to roots or Old Names because their objective definitions and/or historical status remain separate worldbuilding questions.

The corpus result shows that speculative grammar expansion is no longer justified by Yona alone. It does **not** make world execution the next milestone; language stabilization and cross-genre validation continue first. See D-085.


### D-084 — Cross-genre corpus pressure expands ordinary vocabulary, not grammar

After the full Yona corpus pass, two deliberately different public-domain novels were audited:

- Jane Austen's _Pride and Prejudice_;
- Mary Shelley's 1818 _Frankenstein_.

Neither exposed a new grammar/type-system gap beyond G1–G16.

They did independently expose the same ordinary-language weakness: core executable vocabulary was disproportionately strong in action/magic/formal semantics and weak in social, emotional, kinship, and learning semantics.

Therefore a cross-genre pass adds 33 ordinary productive entries such as Love, Trust, Consent, Refuse, FriendOf, SpouseOf, Reputation, ResponsibleFor, Learn, Teach, RemorseFor, Forgive, Happy/Sad/Angry, and related concepts.

These are general Cuspell semantics. They are not Austen/Shelley New Names and do not create magical macro privileges.

Historically contingent institutions remain world data. For example:

- Regency entail/inheritance law is not a grammar primitive;
- legal guilt/innocence depends on a normative institution/world model;
- marriage validity and social rank depend on culture/world data;
- Frankenstein's method of assembling/animating a creature depends on objective world physics/biology.

The anti-overfitting result reinforces that new grammar should be evidence-driven. It also exposes remaining ordinary-language vocabulary work, so major engineering effort remains on language stabilization rather than world/game execution. See D-085.


### D-085 — Language stabilization precedes game/world execution

Cuspell is still being designed as a language. Passing large fiction corpora is evidence of structural convergence, not proof that the language is finished and not a trigger to begin building the eventual game's physical/magical simulator.

Therefore:

- objective world classifiers, concrete physics, generation profiles, runtime world execution, and RequiredPower are **deferred**;
- those systems should be designed only after Cuspell reaches an explicit language-stability / v1 semantic-freeze point;
- the eventual game, simulation style, and desired level of physical abstraction must help determine what world model is appropriate;
- current work remains language-focused: root/lexicon cleanup, Old/New naming, ordinary-language coverage, compositional semantics, ambiguity stress, parser/spec agreement, diagnostics, and diverse corpus validation;
- future world concepts may remain recorded as placeholders or ontology questions without implementing classifiers now.

D-043 remains valid: language semantics and world/game semantics are separate layers. D-085 clarifies their **project order**.

Earlier wording in D-083/D-084 that suggested world ontology/execution should immediately become the implementation priority is superseded by this decision.


### D-086 — Primitive roots are now reduction-first; exact compositional duplicates should be removed

Corpus-driven expansion was useful for discovering distinctions, but the current executable registry is not presumed to be the final primitive-root inventory.

A standalone root should now be kept only when it carries a distinct truth condition, supplies a justified canonical semantic primitive, or avoids a composition that would be unreasonably ambiguous/awkward.

The first reduction batch removes eleven exact redundancies:

- After -> reverse Before;
- Less -> reverse More;
- AtLeast / AtMost -> comparison plus Or Equal;
- EvidenceAgainst -> EvidenceFor of the negated proposition;
- NotDetected -> Not Detected;
- Never -> Always Not;
- False -> Not True;
- Claim -> Assert;
- Lose -> EndHave;
- Destroy -> EndExist.

Inside and Outside were initially removed during this batch but restored after the detailed spatial specification showed that they preserve stricter geometry than In / Not In.

Do not preserve redundant spellings as hidden aliases merely to keep old tests green; that would keep the effective root inventory large.

Roots used inside proposed Old Names are **not protected from deletion during language design**. If a root proves redundant, the affected Old Names should be redesigned as necessary. Historical Sign spellings and frozen mana costs become preservation constraints only after an explicit language/history freeze.

Generic/core New Names are documented separately from setting packages in `docs/world/NEW_NAMES.md`. Book/campaign-specific New Names must remain in their own optional packages and are not copied into the generic list.


### D-087 — Proposed Old Names are mutable until the language/history freeze

Old Names describe how the finalized fictional language behaves historically; they are not immutable project artifacts while Cuspell itself is still being designed.

Therefore, before the language/history freeze:

- an Old Name may be renamed or rebuilt;
- its component roots may change;
- its historical etymology may change;
- nested Old Name dependencies may change;
- its frozen mana cost may change;
- a root is never kept merely because a current draft Old Name happens to use it.

Root minimization should evaluate the language first. When a redundant root is removed, affected draft Old Names should be rebuilt from the remaining language where appropriate.

After a deliberate freeze, D-075 through D-079 govern the resulting in-world historical behavior: the finalized Old Name then acts as fossilized vocabulary with fixed denotation and historical cost.

Until that point, Cuspell's working Old Name inventory is a design model, not a compatibility boundary.


### D-088 — Second minimization batch removes convenience wrappers over general machinery

The second reduction batch removes eleven additional primitive entries:

- Contain;
- Get;
- Join;
- Separate;
- Tell;
- See;
- Hear;
- Smell;
- Taste;
- ChangeBy;
- Converse.

Their meanings remain available through existing general forms:

- containment -> In(item, region);
- acquisition -> BeginHave;
- joining/separating -> BeginJoined / EndJoined;
- addressed information transfer -> Say with recipient;
- channel-specific sensing -> Sense + SenseChannel;
- relative attribute change -> Change to Add(BeforeValue(attribute(subject)), delta);
- relation converse -> write the same Relation using its actual roles/arguments in the intended order.

Draft Old Names that used these roots are rebuilt rather than preserving the roots.

This pass reduces the executable core from 295 to 284 entries, and from 306 to 284 across the first two corrected minimization passes.


### D-088 — Executable entries and primitive roots are separate inventories

The executable lexicon registry is not a valid primitive-root count.

Each core entry must now be assigned one design-stage inventory role:

- semantic primitive candidate;
- derived candidate;
- unresolved reduction candidate;
- formal constructor;
- reference form;
- closed-domain value;
- direct noun/name migration candidate (currently none after the first migration batch).

After noun migration and extrema consolidation, 276 executable entries remain while 119 are still classified as semantic primitive candidates.

This is not a freeze or a target count. Primitive candidates may still be reduced later; derived/unresolved candidates may remain executable temporarily while their general replacement machinery is designed.

Formal constructors, references, and domain values may still require visible signs/runes, but they must be reported separately from lexical semantic roots.

Inside and Outside remain current primitive candidates because the geometry specification gives them strict boundary semantics that are not equivalent to In and Not In.

A regression must keep inventory-role coverage complete whenever the core registry changes.


### D-089 — Ordinary noun Kinds migrate to Names; extrema use MinBy / MaxBy

The direct Kind roots Human, Cat, Water, Body, Hand, and Sound are removed.

Their semantic concepts remain in the core world package and receive provisional Old Names:

- Human = `«Know«MoveLifeThing»»`
- Cat = `«Small«MoveLifeThing»»`
- Water = `«LiquidMatter»`
- Body = `«LifeMatter»`
- Hand = `«Grab«LifeMatter»Part»`
- Sound = `«HearingThing»`

Registered named Kinds are valid binder domains; quantification therefore does not require ordinary nouns to remain primitive roots.

The specialized selectors Nearest, Farthest, Highest, and Lowest are also removed. Two generic constructors replace them:

- `MinBy(collection, binder, ordered-key)`
- `MaxBy(collection, binder, ordered-key)`

Both preserve all tied extrema. `Unique` is still required when exactly one member is needed.

This reduces the executable registry from 284 to 276 without reducing semantic coverage.


### D-089 — Typed measurement units are Old Names built from one Unit root

Canonical measurement units do not each deserve an independent primitive rune.

The productive language has one general `Unit` root. Specific canonical typed units are historical Old Names built from the measured quantity/attribute root plus `Unit`:

- `«ConfidenceUnit»`
- `«HeatUnit»`
- `«LengthUnit»`
- `«LightUnit»`
- `«MassUnit»`
- `«DurationUnit»` for the Time dimension

Typed scale/dimension metadata remains registered separately so an Old Name such as `«LengthUnit»` can construct a `Quantity:Length`.

These Old Names do not count as separate primitive roots. This replaces six independent Unit constructor rune entries with one productive `Unit` root, reducing the raw base-sign inventory by five.

`DurationUnit` is preferred over introducing a separate `Time` root solely to preserve the earlier temporary ASCII label `TimeUnit`.


### D-090 — Between, Ask, and TimeOverlap are compositional rather than primitive roots

The third direct minimization batch removes three more registered surfaces whose executable meanings are already available exactly:

- ordered `Between(value, lower, upper)` is `More(value, lower) And More(upper, value)`;
- `Ask(speaker, question, addressee?)` is `Say(speaker, QuestionContent, addressee?)`;
- `TimeOverlap` is the general `Overlap` relation with Event/Event and TimeInterval/TimeInterval frames.

The removed ordered `Between` entry did not supply geometric segment/geodesic betweenness. If that spatial meaning becomes necessary, it must receive an exact geometry analysis rather than inheriting numeric ordering by accident.

The draft bridge Old Name is rebuilt without `Between`. This checkpoint changes the registered base inventory **277 -> 274** while semantic primitive candidates remain **120**; derived candidates become **30** and unresolved candidates **46**.

### D-091 — AwayFrom is Opposite Toward

`Toward(reference)` constructs a typed `Direction`. `Opposite` is generalized to accept `Direction`, so `AwayFrom(reference)` does not need a separate root and is written `Opposite Toward reference`.

This is a true semantic inverse on the direction axis, unlike relation converse. No draft Old Name depends on `AwayFrom`. This checkpoint changes the registered base inventory **274 -> 273** while semantic primitive candidates remain **120**.

### D-092 — DirectPart is composition over Part

`DirectPart(A,B)` does not need a separate root. Its exact structural meaning is `Part(A,B)` and there is no distinct entity X such that `Part(A,X)` and `Part(X,B)`.

Identity guards exclude X=A and X=B when the structural model permits reflexive Part. The executable surface can use `Some`, `Not`, `Same`, and explicit zero-mana grouping.

No draft Old Name depends on `DirectPart`. This checkpoint changes the registered base inventory **273 -> 272** while semantic primitive candidates remain **120** and derived candidates become **28**.

### D-093 — Former is Past plus not Present

`Former(P)` is not an independent root. Its exact state meaning is `Past(P) And Not Present(P)`.

The draft corpse Old Name is rebuilt from `«FormerLife«LifeMatter»»` to `«PastLifeNotLife«LifeMatter»»`. This changes the registered base inventory **272 -> 271** and derived candidates **28 -> 27**.

### D-094 — Information is a semantic type; KnowAnswer is compositional

The direct `Information` Kind root duplicated the already-existing semantic type `Information`, and its Entity-classifier frame conflicted with the information spec's definition of Information as abstract content.

The Kind root is removed. `i:Information` therefore binds the semantic value type directly. `Know` accepts both Proposition and Information content, as the written specification already required.

With that ambiguity gone, `KnowAnswer(mind, question)` is exactly:

`Some i:Information And {Know mind i, AnswerFor i question}`

So `KnowAnswer` is removed as a separate root. This checkpoint changes the registered base inventory **271 -> 269**, semantic primitive candidates **120 -> 119**, and derived candidates **27 -> 26**.

### D-095 — Trend direction is ChangeRate compared with typed Zero

`ChangeRate` is generalized from an AttributeDescriptor-specific function to `ChangeRate(value: Quantity, interval) -> Quantity<value-dimension/Time>`. `Zero` can take the expected Quantity dimension.

Therefore increasing trend is `More ChangeRate value interval Zero`; decreasing trend is the same comparison on the opposite rate (equivalently zero greater than the rate). Separate `Increasing` and `Decreasing` roots are removed.

This checkpoint changes the registered base inventory **269 -> 267** and derived candidates **26 -> 24**. Semantic primitive candidates remain **119**.

### D-096 — ApproxEqual is explicit tolerance-bounded difference

For same-dimension quantities A, B, and tolerance T, `ApproxEqual(A,B,T)` is represented by both signed differences being no greater than T:

`And {Not More Add A Opposite B T, Not More Add B Opposite A T}`

This preserves an explicit tolerance and requires no approximate-equality primitive. `ApproxEqual` is removed.

This checkpoint changes the registered base inventory **267 -> 266** and derived candidates **24 -> 23**. Semantic primitive candidates remain **119**.

### D-097 — Sometimes is existential Happen

For EventSpec meanings, `Sometimes(event, interval?)` and the existing `Happen(event, interval?)` had the same typed shape. `Happen` already means that at least one concrete matching Event occurs in the relevant interval/domain.

The separate `Sometimes` convenience root is therefore removed. This checkpoint changes the registered base inventory **266 -> 265** and derived candidates **23 -> 22**. Semantic primitive candidates remain **119**.

### D-098 — Members is Collect over Member

The functional `Members(group) -> Collection<Entity>` root is redundant once `Member` accepts group membership directly.

The exact collection form is:

`Collect x:Entity Member $x group`

`Member` keeps its existing collection-membership frame and gains a group-Entity frame. The old `Members` frame already accepted any Entity as its group argument, so this does not weaken typing relative to the removed root.

No draft Old Name depends on `Members`. This checkpoint changes the registered base inventory **265 -> 264** and unresolved candidates **46 -> 45**. Semantic primitive candidates remain **119** and derived candidates remain **22**.

### D-099 — Stop is the terminating EventSpec frame of End

`End` already names the general ending/boundary concept. Typed output disambiguation lets the same root support both:

- `End(Event) -> TimePoint`: the event's ending time;
- `End(Event) -> EventSpec`: terminate that ongoing concrete event.

Therefore `Stop(Event)` adds no independent semantic root and is removed. No draft Old Name depends on `Stop`.

This checkpoint changes the registered base inventory **264 -> 263** and derived candidates **22 -> 21**. Semantic primitive candidates remain **119**.

### D-100 — Teach is agentive Cause of Learn

The information specification distinguishes merely saying content from successfully teaching it. The stronger teaching truth condition is that the teacher causes the learner-acquisition event.

Therefore:

`Teach teacher learner content`

is written:

`Cause teacher Learn learner content`

The existing agentive `Cause(Entity, EventSpec) -> EventSpec` frame supplies the causation, while `Learn` preserves the acquisition event itself. No draft Old Name depends on `Teach`.

This checkpoint changes the registered base inventory **263 -> 262** and unresolved candidates **45 -> 44**. Semantic primitive candidates remain **119** and derived candidates remain **21**.

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
- Generic `Opposite(BeginJoined) = EndJoined` shortcuts.
- Treating Heat/Light/Length/Mass as merely Boolean Properties.
