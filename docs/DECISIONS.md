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
- Whole = persistent integrity/completeness Property/state.
- Ratio = numerical/proportional construction.

The earlier numerical use of Part is superseded.

### D-020 — Generic magical Of, By, and For are rejected

English linkers collapse too many relations. Formal/magical expressions use the actual typed relation: Part, Have, Purpose, Beneficiary, Use(event,instrument), etc. Conversational umbrella words may exist outside magical execution.

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

Artifact Kinds use persistent Purpose grounded by objective design/function/structure evidence. Using a rock as a hammer once does not automatically establish that Purpose or change its Kind.

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

Natural-language generic claims are not strict universal quantification. The later minimization expresses them as contextual high prevalence over the relevant collected domain; objective magical logic uses All, Most, explicit proportions, or registered world thresholds/defaults.

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

Near occurrence/non-completion of an EventSpec is represented by false-side contextual boundary distance: `And {Not Happen E,Low Distance E}`. It is not a magical instruction and does not choose a hidden numeric tolerance.

`Permitted` carries explicit authority/context when needed. In addition to `Permitted agent EventSpec`, the EventSpec+`:authority` frame states that the event itself is permitted by that authority, which supplies the shared basis for compositional consent/refusal.
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

Counterfactual does not assert A or B in the actual world and is not equivalent to Past, epistemic possibility (`More Confidence ... Zero`), or material implication. Because its alternative-history selection is contextual, it is not implicitly executable inside magic. Objective hypothetical-world execution requires a future explicit construction.

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

Therefore a Ship historically named from High + Size + Boat remains a Ship even if a particular instance is not currently HighSize by the ordinary contextual standard. Objective world classifiers, not etymology, determine concept membership.

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
- `HighHunger(subject)` is the ordinary contextual high-hunger state;
- `LowHunger(subject)` is the contextual satiated/full-enough state and is **not** the logical Opposite of `HighHunger`.

Likewise, physical injury uses the ordered `Damage` Attribute plus the productive persistent threshold state `HighDamage`.

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

Therefore a cross-genre pass originally added 33 ordinary productive entries such as Love, Trust, Consent, Refuse, FriendOf, SpouseOf, Reputation, ResponsibleFor, Learn, Teach, RemorseFor, Forgive, Happy/Sad/Angry, and related concepts. Later minimization removes Teach/Learn through explicit acquisition-state causation/transitions and removes Consent/Refuse through addressed permission assertion/denial.

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
- NotDetected -> Not Happen Sense; with no channel, quantify over SenseChannel;
- Never -> Always Not;
- False -> Not True;
- Claim -> Assert;
- Lose -> EndHave;
- Destroy -> EndExist.

Inside and Outside were initially removed during this batch but restored after the detailed spatial specification showed that they preserve stricter geometry than In / Not In. This first-pass restoration is later superseded by D-171 only after Touch/Overlap gain the Region topology needed to preserve those stricter meanings compositionally.

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

At this checkpoint Inside and Outside remain primitive candidates because the geometry specification gives them strict boundary semantics that are not equivalent to In and Not In. D-171 later removes them using explicit boundary-contact and interior-overlap compositions rather than the rejected plain In/Not In simplification.

A regression must keep inventory-role coverage complete whenever the core registry changes.


### D-089 — Ordinary noun Kinds migrate to Names; extrema use MinBy / MaxBy

The direct Kind roots Human, Cat, Water, Body, Hand, and Sound are removed.

Their semantic concepts remain in the core world package and receive provisional Old Names:

- Human = `«Know«MoveLifeThing»»`
- Cat = `«LowExtent«MoveLifeThing»»`
- Water = `«LiquidMatter»`
- Body = `«LifeMatter»`
- Hand = `«Control«LifeMatter»Part»`
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

Identity guards exclude X=A and X=B when the structural model permits reflexive Part. The executable surface can use `Some`, `Not`, Entity `Equal`, and explicit zero-mana grouping.

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

### D-100 — Teach is agentive Cause of learner-state acquisition

The information specification distinguishes merely saying content from successfully teaching it. The stronger teaching truth condition is that the teacher causes the learner-acquisition event.

Therefore:

`Teach teacher learner content`

is written:

Use the typed acquisition event: `Cause teacher Begin Know learner content`, `Cause teacher Begin Can learner event`, or `Cause teacher Begin Understand learner content`.

The existing agentive `Cause(Entity, EventSpec) -> EventSpec` frame supplies the causation. The later Learn reduction makes the acquired state explicit instead of preserving a generic acquisition root. No draft Old Name depends on `Teach`.

This checkpoint changes the registered base inventory **263 -> 262** and unresolved candidates **45 -> 44**. Semantic primitive candidates remain **119** and derived candidates remain **21**.

### D-101 — Prefer is ordered Evaluate comparison

`Evaluate(evaluator,target)` already yields an ordered `EvaluationValue`. Preference therefore needs no independent root:

`Prefer evaluator A B`

is:

`More Evaluate evaluator A Evaluate evaluator B`

To preserve the old preference state semantics, `More(EvaluationValue, EvaluationValue)` has a specific frame returning `StateProposition`. Generic ordered/numeric More comparisons continue to return ordinary `Proposition`.

No draft Old Name depends on `Prefer`. This checkpoint changes the registered base inventory **262 -> 261** and semantic primitive candidates **119 -> 118**. Derived candidates remain **21** and unresolved candidates remain **44**.

### D-102 — SiblingOf is shared ParentOf composition

Siblinghood is defined by a shared parent plus distinct identity:

`Some p:Entity And {ParentOf $p A,ParentOf $p B,Not Equal A B}`

To preserve the former root's state semantics, `Equal(Entity,Entity)` is a `StateProposition`, `And` has a state-preserving conjunction frame, and `Some` has a state-preserving existential frame. Thus the derived sibling relation remains usable as a persistent state rather than degrading to a generic Proposition.

No draft Old Name depends on `SiblingOf`. This checkpoint changes the registered base inventory **261 -> 260** and semantic primitive candidates **118 -> 117**. Derived candidates remain **21** and unresolved candidates remain **44**.

### D-103 — High is the productive contextual threshold constructor

A single `High` operator now expresses “above the relevant contextual standard” for ordered values. It has typed direct frames for Quantity and EvaluationValue.

When compounded with an AttributeDescriptor, `High` productively forms a first-class PropertyDescriptor. Examples:

- `HighLength X` = length of X is above the relevant standard;
- `HighHunger X` = hunger degree of X is above the relevant standard;
- `High OccurrenceRate E I` = occurrence rate of E over I is above the relevant standard.

The generated property descriptor remains usable by boundary-distance composition, so `And {Not HighHunger Self,Low Distance HighHunger Self}` preserves the near-threshold capability previously supplied by the standalone Hungry Property root.

`Long`, `Hungry`, and `Often` are removed. The draft tail Old Name is rebuilt from `High + Length`.

This checkpoint changes the registered base inventory **260 -> 258**. Derived candidates fall **21 -> 19**, unresolved candidates **44 -> 43**, and formal constructors rise **52 -> 53**. Semantic primitive candidates remain **117**.

### D-104 — Confidence, injury, and stability convenience roots reduce compositionally

Three further passes remove four standalone roots without adding a new constructor:

- `PossibleTo M P` is `More Confidence M P Zero`;
- `ProbableTo M P` is `High Confidence M P`;
- `Injured X` is the generated threshold Property `HighDamage X`;
- exact `Stable V I` is `Equal ChangeRate V I Zero`, with tolerance stability expressed by two-sided rate bounds.

`CertainTo` was temporarily retained because exact certainty is not equivalent to contextual high confidence. It is now reducible after fixing the normalized Confidence endpoint. The wound draft Old Name is rebuilt as `«HighDamage«LifeMatter»Part»`.

These passes change the registered base inventory **258 -> 254** and derived candidates **19 -> 15**. Semantic primitive candidates remain **117**.

### D-105 — Low is a productive below-standard constructor

`Low(value)` means that an ordered value is below the relevant contextual standard. It is not equivalent to `Not High(value)`; the language may recognize an intermediate range that is neither High nor Low.

Like High, Low combines with AttributeDescriptors to form first-class Properties. This supports `LowHunger` as a StateProposition and direct value predicates such as `Low OccurrenceRate E I`.

Therefore `Rarely` and `Sated` are removed as standalone roots:

- `Rarely E I` -> `Low OccurrenceRate E I`;
- `Sated X` -> `LowHunger X`.

### D-106 — Importance is high evaluator-relative evaluation

`ImportantTo(target,evaluator)` is not a separate semantic primitive. It is the contextual high-threshold form of the existing evaluation scale:

`High Evaluate evaluator target`.

The three passes represented by D-105/D-106 change the registered inventory **254 -> 252**. Derived candidates become **14**, unresolved candidates **41**, and formal constructors **54**. Semantic primitive candidates remain **117**.

### D-107 — Confidence has fixed normalized endpoints

The canonical Confidence scale is normalized for language-level comparison:

- `Zero` denotes complete rejection;
- `«ConfidenceUnit» @` denotes complete confidence/certainty.

World and mind models may use arbitrary internal probability, score, or evidence systems, but their exposed Confidence value maps into this canonical scale.

This makes the remaining threshold convenience exact:

`CertainTo M P` = `Equal Confidence M P «ConfidenceUnit» @`.

`CertainTo` is removed as a standalone root. The registered inventory changes **252 -> 251** and derived candidates **14 -> 13**.

### D-108 — Continue is present-boundary End prevention

A concrete Event already has an EventSpec-typed `End(Event)` meaning “terminate this ongoing Event.” Therefore a second continuation Process is unnecessary.

For a resolved ongoing Event E:

`Continue E` = `Prevent End E Interval Now Now`.

The zero-width interval is intentional: ordinary “continue” here means do not end at the present boundary, not “make this event impossible to end for an arbitrary future duration.”

Ordinary discourse may contextually resolve which ongoing Event an EventSpec refers to. Magical/formal use must provide that concrete EventRef before applying the composition.

`Continue` is removed as a standalone root. Registered inventory **251 -> 250**; derived candidates **13 -> 12**.

### D-109 — Period is reciprocal OccurrenceRate

Recurrence Period is not a separate temporal primitive. For a recurrence pattern E:

`Period E` = `Divide @ OccurrenceRate E`.

If a precise measurement scope matters, supply the interval to OccurrenceRate explicitly. Since Frequency is Time^-1, the reciprocal has Time dimension.

This definition applies only where a meaningful recurrence rate exists; zero or undefined recurrence rate does not magically produce a guessed finite Period.

`Period` is removed as a standalone root. Registered inventory **250 -> 249**; unresolved candidates **41 -> 40**.

### D-110 — Present is the default state reference time

A bare StateProposition is evaluated at the active discourse/evaluation reference time. Therefore wrapping that state in a separate Present operator adds no semantic content.

- `Present P` = `P`;
- for an EventSpec E, present occurrence = `During E Now`.

This keeps EventSpec and state semantics distinct while removing the redundant tense wrapper. It also simplifies Former from `Past P And Not Present P` to `Past P And Not P`.

`Present` is removed as a standalone root. Registered inventory **249 -> 248**; derived candidates **12 -> 11**.

### D-111 — Completed is the explicit Past EventSpec reading

The separate Completed aspect operator duplicates Past once Past accepts an explicit EventSpec reference/scope argument.

- `Completed E` = `Past E`;
- `Completed E T` = `Past E T`.

The EventSpec reading of Past is defined as a matching occurrence complete before the contextual or supplied reference boundary. `Completed` is removed. Inventory **248 -> 247**; derived candidates **11 -> 10**.

### D-112 — Ongoing is EventSpec During

`During` is extended to EventSpec + TimePoint/TimeInterval:

`Ongoing E T` = `During E T`.

For EventSpecs, During means at least one matching occurrence is active across the supplied temporal target. This also makes present-event wording `During E Now`.

`Ongoing` is removed. Inventory **247 -> 246**; derived candidates **10 -> 9**.

### D-113 — Big is HighSize

Introduce one contextual ordered `Size(subject) -> EvaluationValue` descriptor for ordinary holistic size/extent comparison. It is not an objective replacement for explicit physical Length/Width/Height/Volume.

`Big X` = `HighSize X`.

Adding Size while deleting Big leaves the registered total at **246**.

### D-114 — Small is LowSize

The same Size scale provides the lower threshold:

`Small X` = `LowSize X`.

LowSize is not Not HighSize; an intermediate band may exist. `Small` is removed, bringing the registered total **246 -> 245** and unresolved candidates **40 -> 39**.

Draft Old Names that previously contained Big/Small are rebuilt with High + Size / Low + Size. Their concept identities remain unchanged.

### D-115 — Past is contextual Before against the reference time

The general temporal relation `Before` is extended to StateProposition/EventSpec patterns against a TimePoint. These pattern frames remain contextual.

- `Past X` = `Before X Now`;
- explicit EventSpec reference/scope: `Past E T` = `Before E T`.

For EventSpecs, the first form means a matching occurrence is complete before the reference point. For states, it means the state held at a relevant earlier time.

`Past` is removed as a standalone root. The draft corpse Old Name is rebuilt as `«BeforeLifeNowNotLife«LifeMatter»»`. Registered inventory **245 -> 244**; derived candidates **9 -> 8**.

### D-116 — Future is the converse Before ordering

The generalized Before relation also covers the later-time reading by reversing its arguments:

`Future X` = `Before Now X`.

For EventSpecs this means a matching occurrence begins after Now; for states it means the state holds at a relevant later time. The pattern/state overloads are contextual, preserving Future's discourse-only character unless a world model supplies objective resolution.

`Future` is removed. Registered inventory **244 -> 243**; derived candidates **8 -> 7**.

### D-117 — Always is Proposition During an interval

`During` now accepts `Proposition + TimeInterval`, meaning the proposition holds throughout that interval.

`Always P I` = `During P I`.

This is temporal universal holding, not a frequency threshold. Consequently `Never P I` is `During Not P I`.

`Always` is removed. Registered inventory **243 -> 242**; derived candidates **7 -> 6**.

### D-118 — LocalDensity is a Density overload

The general Density relation/attribute family now has:

`Density(distribution, region) -> Quantity:Density`.

This is exactly the old `LocalDensity(distribution,region)` meaning, so the specialized root is removed.

Registered inventory **242 -> 241**; unresolved candidates **39 -> 38**.

### D-119 — Height and Width are indexed Span measurements

Frame-relative scalar extent is generalized as:

`Span(subject, frame, axis-index) -> Quantity:Length`.

CoordinateFrame basis index `@` is the primary/up axis and `@@` is the designated width axis. Therefore:

- `Height X F` = `Span X F @`;
- `Width X F` = `Span X F @@`.

Span is retained as an unresolved general geometry relation because it may later derive from lower-level Region projection. Height removal is inventory-neutral because Span is added; Width then reduces the registered inventory **241 -> 240** and unresolved candidates **38 -> 37**.

### D-120 — Grow is directional Change(Size)

`Change` gains a constraint frame whose Proposition may use event-local `BeforeValue` and `AfterValue`.

`Grow X` = `Change X Size More AfterValue Size X BeforeValue Size X`.

This encodes positive holistic size change without choosing an arbitrary target. `Grow` is removed. Registered inventory **240 -> 239**; derived candidates **6 -> 5**.

### D-121 — Promise is speech plus the beginning of commitment

A Promise does not require its own primitive event ontology. A successful Promise combines an addressed utterance of the commitment with the transition into that commitment state:

`Promise S A E` was first reduced through CommittedTo; after commitment consolidation the current form is `And {Say S (Obligated S E :context A) A,Begin (Obligated S E :context A)}`.

The promised EventSpec is not asserted to happen. The contract draft Old Name is now rebuilt from contextual Obligation + Record.

`Promise` is removed. Registered inventory **239 -> 238**; unresolved candidates **37 -> 36**.

### D-122 — Same is Entity Equal

`Equal` already expresses typed equality. For Entity values, equality is identity equality, so `Same` duplicates an exact typed case.

`Same A B` = `Equal A B`.

Equal is represented as a StateProposition, preserving the state typing needed by identity-constrained relations such as the compositional SiblingOf definition.

`Same` is removed. Registered inventory **238 -> 237**; semantic primitive candidates **117 -> 116**.

### D-123 — Detected is occurrence of Sense

A successful `Sense` EventSpec is precisely the perception event whose occurrence establishes detection:

`Detected A X C` = `Happen Sense A C X`.

If no channel is specified, use `Some c:SenseChannel Happen Sense A $c X`. This says some sensory channel detected X without confusing perception with Meaning/understanding.

`Detected` is removed. Registered inventory **237 -> 236**; semantic primitive candidates **116 -> 115**.

### D-124 — MethodFor is Purpose over a Method

Methods are SemanticValues and their goal relation is already represented by Purpose:

`MethodFor M E` = `Purpose M E`.

No separate Method-goal root is needed. Registered inventory **236 -> 235**; semantic primitive candidates **115 -> 114**.

### D-125 — Using is a Use relation frame

One semantic family now covers both intentional instrument use and the event participant role:

- `Use agent instrument goal` -> EventSpec;
- `Use event-or-EventSpec instrument` -> Proposition.

Therefore `Using E I` = `Use E I`.

`Using` is removed. Registered inventory **235 -> 234**; unresolved candidates **36 -> 35**.

### D-126 — Habitual uses the general occurrence-rate threshold

The standalone contextual `Habitual` operator is removed. Its working semantics were recurrence at a contextually sufficient/normal rate over the relevant interval, already represented by the frequency machinery:

`Habitual E I` = `High OccurrenceRate E I`.

This remains contextual ordinary-language semantics. It is not a hidden objective magical threshold. Registered inventory **234 -> 233**; derived candidates **5 -> 4**.

### D-127 — Depth is the third axis of Span

The geometry family now treats height, width, and depth as axis selections of one `Span` relation:

- primary/up axis `@`;
- width axis `@@`;
- depth/third axis `@@@`.

`Span subject axis` is allowed only as contextual shorthand where discourse/world context supplies the CoordinateFrame; objective magical geometry should provide the frame explicitly. `Depth` is removed. Registered inventory **233 -> 232**; unresolved candidates **35 -> 34**.

### D-128 — Thank is addressed Say of gratitude

Thanking is represented by uttering gratitude content to the beneficiary/addressee:

`Thank S A` = `Say S (GratefulTo S A) A`.

`GratefulTo` accepts an optional explicit `:basis` semantic value for the reason. Since `Say` does not entail its content, the construction does not require sincere gratitude. `Thank` is removed. Registered inventory **232 -> 231**; unresolved candidates **34 -> 33**.

### D-129 — Apologize is addressed Say of remorse

Apology likewise does not require an independent Process root:

- contextual offense: `Apologize S A` = `Say S (RemorseFor S) A`;
- explicit offense/basis X: `Say S (RemorseFor S X) A`.

`RemorseFor(experiencer)` is contextual ordinary-language shorthand; explicit formal/objective use should state the basis. `Say` does not entail sincere remorse. `Apologize` is removed. Registered inventory **231 -> 230**; unresolved candidates **33 -> 32**.

### D-130 — Whenever is During over SufficientFor

The recurring conditional wrapper is compositional:

- explicit interval: `Whenever C K I` = `During SufficientFor C K I`;
- contextual interval: `Whenever C K` = `During SufficientFor C K ThisInterval`.

`ThisInterval` supplies the active discourse interval. Ordinary discourse may resolve it contextually; objective magic requires that reference to be formally resolved. `Whenever` is removed. Registered inventory **230 -> 229**; derived candidates **4 -> 3**.

### D-131 — NextOccurrence is First over an EventSpec

`First` now has a contextual EventSpec frame. In that frame:

`NextOccurrence E` = `First E`.

It denotes the next/first matching occurrence after the active temporal reference. Because the occurrence domain/reference is contextual, this remains ordinary-language reference rather than an implicit magical selector. `NextOccurrence` is removed. Registered inventory **229 -> 228**; derived candidates **3 -> 2**.

### D-132 — Redistribute is Transfer over a Distribution

Distribution movement is a specialized case of the existing general `Transfer` Process:

- `Redistribute D S T` = `Transfer D S T`;
- target profile P is written `Transfer D S T :profile P`.

The optional `:profile` role is meaningful for Distribution-valued transfer and constrains the destination profile. `Redistribute` is removed. Registered inventory **228 -> 227**; derived candidates **2 -> 1**.

### D-133 — Generic Because is typed contextual Explains

The English word “because” conflates physical causation, epistemic evidence, and discourse explanation. Cuspell keeps the exact relations separate:

- world causation -> `Cause`;
- evidential support -> `EvidenceFor`;
- ordinary clause explanation -> `Explains reason target`.

The Proposition+Proposition frame of `Explains` is contextual, preserving the ordinary discourse reading without implying physical Cause or EvidenceFor. `Because` is removed. Registered inventory **227 -> 226**; unresolved candidates **32 -> 31**.

### D-134 — Almost is false-side low boundary distance

`Distance` is generalized with contextual boundary-distance frames over gradable PropertyDescriptors and EventSpecs.

- property: `Almost P X` = `And {Not P X,Low Distance P X}`;
- event: `Almost E` = `And {Not Happen E,Low Distance E}`.

The explicit negation keeps the value on the non-satisfying/non-occurring side; `Low Distance` states that it is near the relevant boundary. Objective magic must use a registered metric and threshold rather than inherit contextual `Low`. `Almost` is removed. Registered inventory **226 -> 225**; derived candidates **1 -> 0**.

### D-135 — Should is contextual High Evaluate

The weak recommendation/advice reading is the high end of evaluator-relative desirability:

`Should A E` = `High Evaluate A E`.

This remains contextual and does not replace the stronger deontic state `Obligated A E`. `Should` is removed. Registered inventory **225 -> 224**; unresolved candidates **31 -> 30**.

### D-136 — DesignedFor is Purpose

`Purpose(subject,goal)` already means a persistent intended function/goal and is distinct from temporary `Use`. For artifacts, world classification grounds that Purpose in recognized design/construction evidence.

`DesignedFor X E` = `Purpose X E`.

`DesignedFor` is removed. Registered inventory **224 -> 223**; unresolved candidates **30 -> 29**.

### D-137 — Learn is typed Begin-state acquisition

A generic `Learn` Process hid which persistent state was acquired. Write that state transition explicitly:

- fact/proposition or Information: `Begin Know learner content`;
- skill/EventSpec: `Begin Can learner event`;
- other semantic comprehension: `Begin Understand learner content`.

`Can` is explicitly state-typed so `Begin Can` yields a proper acquisition EventSpec. Teaching is agentive `Cause` of whichever transition applies. `Learn` is removed. Registered inventory **223 -> 222**; unresolved candidates **29 -> 28**.

### D-138 — Generic is contextual high prevalence

The standalone `Generic` quantifier is removed. Its characteristic/normal reading is represented by contextual prevalence over the relevant domain:

`Generic [x:D] P(x)` = `High Ratio Count Collect [x:D] P(x) Count Collect [y:D]`.

`High` gains a Ratio frame. The threshold remains contextual/world-standard, so this is still not strict `All` or fixed-majority `Most`. Registered inventory **222 -> 221**; unresolved candidates **28 -> 27**.

### D-139 — Size is an Extent evaluation frame

The contextual holistic size scale is folded into `Extent`. `Extent(entity)` now has type-directed readings:

- Region output: occupied/spatial extent;
- EvaluationValue output: contextual holistic physical extent/size.

Thus `HighSize`/`LowSize` become `HighExtent`/`LowExtent`, and Grow's directional comparison uses event-local `Extent`. `Size` is removed. Registered inventory **221 -> 220**; unresolved candidates **27 -> 26**.

### D-140 — Span is axis-indexed Extent

Projected axis length is also part of the Extent family. The former Span frames move unchanged to `Extent(subject,frame,axis)`, with contextual no-frame shorthand where already permitted.

Height, Width, and Depth therefore remain `Extent ... @`, `Extent ... @@`, and `Extent ... @@@`. `Span` is removed. Registered inventory **220 -> 219**; unresolved candidates **26 -> 25**.

### D-141 — CommittedTo is contextual Obligation

A promise-established commitment is a persistent deontic/social responsibility whose interpersonal source/context matters. `Obligated` gains optional named `:context`:

`CommittedTo S E A` = `Obligated S E :context A`.

Promise remains the addressed utterance plus `Begin` of that state. `CommittedTo` is removed, and the draft contract Old Name is rebuilt from `Obligated` + Record. Registered inventory **219 -> 218**; unresolved candidates **25 -> 24**.

### D-142 — Teleport is discontinuous At-state transition

Teleportation is represented without a dedicated motion root:

- explicit source: `Teleport X G S` = `And {End At X S,Begin At X G}`;
- source omitted: `Teleport X G` = `Begin At X G`.

The absence of `Move`/`Path` is semantically important: this is a location-state boundary transition, not continuous traversal. `Teleport` is removed. Registered inventory **218 -> 217**; unresolved candidates **24 -> 23**.

### D-143 — Write is Cause of Begin Exist for a Sign

The executable Write frame required an agent and a Sign token. Writing is represented as:

`Write A S` = `Cause A Begin Exist S`, with S typed Sign.

`Exist` is generalized to semantic values so Sign tokens can participate directly in existence-state transitions. `Write` is removed. Registered inventory **217 -> 216**; unresolved candidates **23 -> 22**.

### D-144 — Read is the interpreted-Sign Sense frame

`Sense` gains a contextual two-argument Sign frame meaning successful Sign perception plus semantic interpretation:

`Read A S` = `If Sign S (Sense A S)`.

The `Sign S` condition preserves the former Sign role. The explicit channel Sense frame remains the raw-perception form; channel/language mapping for the interpreted-Sign shorthand is context-resolved unless explicitly represented elsewhere. `Read` is removed. Registered inventory **216 -> 215**; unresolved candidates **22 -> 21**.

### D-145 — Grab is concurrent Begin Touch + Begin Control

`Touch` is state-typed. Taking hold is represented as the simultaneous onset of contact and control:

`Grab A T` = `And {Begin Touch A T,Begin Control A T}`.

This keeps both physical contact and acquisition of control. The draft Hand Old Name is rebuilt as `«Control«LifeMatter»Part»`, and Wrist follows the rebuilt Hand name. `Grab` is removed. Registered inventory **215 -> 214**; unresolved candidates **21 -> 20**.

### D-146 — Consent is addressed assertion of authority-scoped permission

`Permitted` gains an EventSpec+`:authority` frame meaning that the event itself is permitted/consented to by the named authority.

- `Consent C E` = `Say C (Permitted E :authority C)`;
- with requester R = `Say C (Permitted E :authority C) R`.

This does not imply Want or Intend. `Consent` is removed. Registered inventory **214 -> 213**; unresolved candidates **20 -> 19**.

### D-147 — Refuse is addressed denial of authority-scoped permission

The explicit rejection speech act is the negation of the same permission content:

- `Refuse R E` = `Say R (Not (Permitted E :authority R))`;
- with requester Q = `Say R (Not (Permitted E :authority R)) Q`.

This preserves explicit communicative refusal rather than reducing it to absence of intention. `Refuse` is removed. Registered inventory **213 -> 212**; unresolved candidates **19 -> 18**.

### D-148 — Deceive is successful causation of false belief

Agentive `Cause` gains a StateProposition effect frame. Successful deception concerning proposition P is:

`Deceive D T P` = `If (Not P) (Cause D (Believe T P))`.

The false proposition and caused target-belief state are both explicit; method remains unconstrained. `Deceive` is removed. Registered inventory **212 -> 211**; unresolved candidates **18 -> 17**.

### D-149 — Sever is causative loss of Whole

`Whole` is explicitly state-typed, and agentive `Cause` accepts optional named `:instrument`.

- `Sever A T` = `Cause A (End Whole T)`;
- instrument I = `Cause A (End Whole T) :instrument I`.

This captures successful structural loss of wholeness; narrower material/cutting mechanics belong to the world model. `Sever` is removed. Registered inventory **211 -> 210**; unresolved candidates **17 -> 16**.

### D-150 — Meaning remains a primitive semantic relation

`Meaning(Sign, content)` connects a representation token to conveyed semantic content under language/context. It is not equivalent to `About`, equality, evidence, Purpose, or structural Part. Ambiguity/polysemy are valid ordinary cases.

No exact smaller analysis currently preserves those truth conditions. Registered inventory remains **210**; semantic primitive candidates **114 -> 115**; unresolved candidates **16 -> 15**.

### D-151 — About remains distinct Information topicality

`About(Information, topic)` expresses subject-matter/topicality. A piece of Information may be about a topic regardless of which Sign conveys it, so replacing About with Meaning would collapse Sign interpretation and Information subject matter.

Registered inventory remains **210**; semantic primitive candidates **115 -> 116**; unresolved candidates **15 -> 14**.

### D-152 — DistributionOf remains the Distribution constructor/accessor

`DistributionOf(resource, host)` yields the Distribution field/object associated with that resource over that host/domain. `Density` consumes a Distribution, while Transfer manipulates one; neither supplies the same constructor/accessor semantics.

Registered inventory remains **210**; semantic primitive candidates **116 -> 117**; unresolved candidates **14 -> 13**.

### D-153 — TotalAmount remains the aggregate Distribution operator

`TotalAmount(distribution, region?)` represents the aggregate/integrated amount of a Distribution over a domain. General reduction to Density would require an integration operator and world-model measure semantics that the current core does not otherwise contain.

Registered inventory remains **210**; semantic primitive candidates **117 -> 118**; unresolved candidates **13 -> 12**.


### D-154 — Beneficiary remains a distinct event-role relation

`Beneficiary(event, entity)` marks who benefits from an Event or EventSpec. It is not identical to recipient, possession, transfer, or `Purpose`: a beneficiary may receive nothing directly, and an event may benefit someone without that benefit being its intended goal.

No exact smaller current analysis preserves the role. Registered inventory remains **210**; semantic primitive candidates **118 -> 119**; unresolved candidates **12 -> 11**.

### D-155 — Bite remains a distinct action-manner Process

`Bite(agent, target)` encodes an oral biting action. `Attack`, `Eat`, `Touch`, and `Damage` overlap with some bites but none entails the oral action manner, and bites need not be attacks, feeding, or damaging.

Until Cuspell has a general exact action-manner/body-part mechanism, Bite remains primitive. Registered inventory remains **210**; semantic primitive candidates **119 -> 120**; unresolved candidates **11 -> 10**.

### D-156 — CamouflagedAgainst remains observer/background-sensitive camouflage

`CamouflagedAgainst(subject, background, observer?)` is a contextual perceptual state. `ColorOf` and `TextureOf` expose concrete appearance components, but the core has no general perceptual-similarity metric that combines color, texture, pattern, form, lighting, and observer sensitivity. The existing `Contrast` relation is discourse contrast, not visual contrast.

Registered inventory remains **210**; semantic primitive candidates **120 -> 121**; unresolved candidates **10 -> 9**.

### D-157 — Climb remains a distinct locomotion-manner Process

`Climb(agent, target)` is not exactly `Move` plus `Up`, `Touch`, or `Surface`. Climbing may proceed upward, downward, across, or over a target, while generic Move does not encode the characteristic supported/contact locomotion manner.

No exact current composition preserves that manner without adding equivalent machinery elsewhere. Registered inventory remains **210**; semantic primitive candidates **121 -> 122**; unresolved candidates **9 -> 8**.


### D-158 — Contrast remains a distinct discourse relation

`Contrast(a, b)` marks contextual concession/tension between two represented propositions or EventSpecs. Replacing it with `And` preserves that both sides hold but loses the contrast relation itself. The current core has no general discourse-coherence or expectation-violation mechanism that reconstructs that meaning exactly.

Registered inventory remains **210**; semantic primitive candidates **122 -> 123**; unresolved candidates **8 -> 7**.

### D-159 — Dodge remains a distinct evasive-action Process

`Dodge(agent, threat?)` is action intended to avoid a threat. Generic `Move` does not encode the avoidance goal, `Prevent` prevents the threatening EventSpec rather than merely avoiding its effect/contact on the dodger, and `Attempt` alone does not encode evasive action.

Registered inventory remains **210**; semantic primitive candidates **123 -> 124**; unresolved candidates **7 -> 6**.

### D-160 — Fall remains a distinct non-agentive motion Process

`Fall(theme)` is a gravity/context-governed motion manner. Generic `Move` does not encode falling, the local gravity/down frame, or uncontrolled/non-agentive motion, and its executable frame requires a goal or Path. Existing `At`, `Offset`, and direction machinery therefore does not supply an exact replacement.

Registered inventory remains **210**; semantic primitive candidates **124 -> 125**; unresolved candidates **6 -> 5**.

### D-161 — Forgive remains a distinct social transition Process

`Forgive(forgiver, offender, :offense?)` is relinquishing blame/resentment toward an offender. It is not equivalent to `End Hate`, `End Angry`, or `Not ResponsibleFor`: forgiveness can occur without prior hatred, can coexist with residual anger, and can leave memory and responsibility judgments intact.

Registered inventory remains **210**; semantic primitive candidates **125 -> 126**; unresolved candidates **5 -> 4**.


### D-162 — Reflexive remains a distinct involuntary-event relation

`Reflexive(event)` states that an EventSpec occurs as an involuntary/reflex response. `Not Intend` is too broad: accidents, coercion, habits, and unknown intentions can all lack conscious intention without being reflexes. `Cause` also addresses causation rather than execution mode.

Registered inventory remains **210**; semantic primitive candidates **126 -> 127**; unresolved candidates **4 -> 3**.

### D-163 — Jump remains a distinct locomotion-manner Process

`Jump(agent, goal?)` encodes launch/airborne locomotion manner. Generic `Move` can encode displacement and destination but not the jumping manner itself, and the current path/direction machinery has no general motion-manner constructor that makes the reduction exact.

Registered inventory remains **210**; semantic primitive candidates **127 -> 128**; unresolved candidates **3 -> 2**.

### D-164 — Limp remains a distinct gait-manner Process

`Limp(agent)` encodes asymmetric/impaired gait. It is not equivalent to `Move` plus `Damage`: Damage is a graded condition, damaged entities need not limp, and limping can have multiple causes unrelated to current Damage.

Registered inventory remains **210**; semantic primitive candidates **128 -> 129**; unresolved candidates **2 -> 1**.

### D-165 — Stab remains a distinct puncturing/thrust Process

`Stab(agent, target, instrument?)` encodes a directed puncturing/thrust action manner. `Attack`, `Damage`, `Touch`, and `Use` may describe surrounding intent, consequence, contact, or instrumentation but do not identify the same event type.

Registered inventory remains **210**; semantic primitive candidates **129 -> 130**; unresolved candidates **1 -> 0**. The explicit unresolved-candidate bucket is now empty, but retained primitive candidates remain revisitable.

### D-166 — ChangeRate and OccurrenceRate consolidate into one typed Rate root

The two previous roots encode the same reusable semantic operation: measurement per Time.

Current canonical frames are:

- `Rate(value: Quantity, interval: TimeInterval) -> Quantity<value-dimension/Time>`;
- `Rate(event: EventSpec, interval: TimeInterval) -> Quantity:Frequency`;
- `Rate(event: EventSpec) -> Quantity:Frequency` with contextual measurement scope.

The Quantity and EventSpec input types distinguish the frames exactly. This is a real primitive reduction, not an enum-shaped rename: there is no separate `ChangeRateKind` or `OccurrenceRateKind` semantic atom.

Earlier decisions and audit history that mention ChangeRate or OccurrenceRate remain historical descriptions of the pre-D-166 vocabulary; their semantics now map to `Rate`.

Registered inventory **210 -> 209**; semantic primitive candidates **130 -> 129**; unresolved candidates remain **0**.

### D-167 — Do not add a generic Manner layer yet; motion/action roots remain distinct

The second-pass family audit tested Bite, Climb, Dodge, Fall, Jump, Limp, and Stab against the existing Move/Touch/Through/Use/Attack/Damage/Attempt/Prevent/Reflexive/Cause machinery and against candidate shared-feature designs.

No exact net reduction was found. The missing distinctions are respectively oral biting, supported traversal, evasive realization, gravity-driven uncontrolled motion, self-launched airborne motion, asymmetric gait, and puncturing/thrust interaction.

A generic `Manner(event, value)` design is rejected for now because one atomic manner value per old root would preserve the same irreducible semantic atoms while adding another meaning-bearing constructor. Moving those atoms into world tags or Old Names would likewise only hide them.

The boundary roots Attack, Eat, Move, Use, and Worship also remain: Move and Use are reusable base abstractions, while Attack, Eat, and Worship retain activity meanings not recoverable from the other family members.

Registered inventory remains **209**; semantic primitive candidates remain **129**.

### D-168 — Duration is the Event frame of Extent

A concrete Event's duration is exactly its temporal extent. The standalone `Duration` root therefore does not carry an independent semantic distinction.

The general `Extent` family gains:

`Extent(event: Event) -> Quantity:Time`.

This sits beside its existing spatial Region, holistic size, and frame-axis Length readings and is type-distinct by both input and output.

The `Duration` root is removed. `«DurationUnit»` remains a typed Old Name for the canonical Time unit and is rebuilt from `Extent + Unit`; draft Old Name etymology does not protect a redundant root.

The broader measurement audit rejects fake descriptor compression: Mass/Heat/Light/etc. do not become one generic Measure plus one atomic kind value each.

Registered inventory **209 -> 208**; semantic primitive candidates **129 -> 128**; unresolved candidates remain **0**.

### D-169 — Do not collapse social/affective roots into one attitude or valence layer

The second-pass social/affective audit tests the 26 current roots as three interacting groups: affective attitudes/states, social/institutional relations, and social evaluation/repair.

No exact net reduction is accepted.

A generic `Attitude(experiencer,target,kind)` or `SocialRelation(a,b,kind)` would require one irreducible kind value per surviving relation and therefore move rather than remove the primitive distinctions.

`Evaluate` remains a useful ordered abstraction for preference/importance/Should-style meanings, but Like, Love, Hate, Admire, Respect, and Trust are not equivalent to one point or threshold on that scale.

Do not define Happy/Sad as High/Low of one generic valence attribute, and do not register Happy/Sad or Love/Hate as Opposite pairs. The current semantics permit distinctions and mixed states that a one-axis inverse model would erase.

Trust remains interpersonal reliance rather than an unspecified proposition-level Believe/Confidence/Expect state. Gratitude, grief, remorse, shame, jealousy, compassion, and fear retain distinct target/basis/appraisal semantics. FriendOf, ParentOf, SpouseOf, EngagedTo, Have, Own, and ResponsibleFor likewise remain distinct social/institutional relations. Reputation is not defined as a simple aggregate of individual Evaluate values.

Forgive remains the independent transition already established by D-161.

Registered inventory remains **208**; semantic primitive candidates remain **128**.

### D-170 — Keep agency, stance, deontic, and event-role distinctions separate

The second-pass audit tests Attempt, Reflexive, Beneficiary, Can, Expect, Intend, Obligated, Permitted, Plan, Purpose, and Want as one family.

No generic Stance/Modal/Role abstraction reduces the semantic alphabet. Want, Expect, Intend, and Plan are not interchangeable modes of one truth condition; replacing them with mode values would only move the primitive distinctions.

Can remains capability and must not collapse into Permitted authorization or epistemic Confidence. Permitted and Obligated are not defined as deontic logical duals: Cuspell currently has no general EventSpec-negation operator or normative axiom making permission equivalent to absence of contrary obligation, and authority/context roles may differ.

Purpose remains a persistent goal/function relation applicable to non-agent SemanticValues. Beneficiary remains an event participant/benefit role that may be unintended. Attempt remains a real effort EventSpec distinct from mental Intend/Plan. Reflexive remains a specific involuntary execution relation rather than Not Intend.

Registered inventory remains **208**; semantic primitive candidates remain **128**.

### D-171 — Inside and Outside are exact compositions over Region Touch/Overlap

The earlier restoration of Inside and Outside was correct: `Inside != In` and `Outside != Not In`.

The missing abstraction was typed Region topology, not two independent strict-containment roots.

`Touch` gains a Region/Region frame meaning boundary contact.

`Overlap` gains a Region/Region frame meaning nontrivial shared interior extent.

The exact strict predicates are therefore:

- `Inside A R` = `And {In A R,Not Touch Extent A R}`;
- `Outside A R` = `Not Overlap Extent A R`.

This preserves the key counterexamples:

- boundary-contained A satisfies In but fails the Inside composition;
- partial overlap satisfies Not In but fails the Outside composition;
- boundary-only contact satisfies the Outside composition because there is no interior overlap.

Inside and Outside are removed as standalone roots. This supersedes only the *retention* conclusion of the earlier geometry checkpoint, not its warning against plain In / Not In.

The remaining spatial roots stay distinct after family review.

Registered inventory **208 -> 206**; semantic primitive candidates **128 -> 126**; unresolved candidates remain **0**.

### D-172 — Keep communication, epistemic, and discourse layers distinct

The second-pass audit tests Assert, Infer, Say, Sense, About, AnswerFor, Believe, Confidence, Contrast, EvidenceFor, Explains, Know, Meaning, Remember, and Understand as one family.

No generic information/epistemic/speech wrapper reduces the semantic alphabet.

`Believe` is not removed in favor of `High Confidence` at this checkpoint. Believe is a persistent mind-model belief state. `High Confidence` is a contextual threshold over Quantity:Confidence, returns an ordinary Proposition in the current typing, and is already used for probability-standard language. Making the two identical would either collapse context-sensitive probability and belief thresholds or require a new explicit belief-threshold semantic atom.

`Know` remains factive and is not defined as true belief. `Remember` remains memory/retention over broad semantic content, and `Understand` remains comprehension.

`Say` is general utterance; `Assert` adds assertion force. `Sense` is perception; `Meaning` is sign interpretation. `About`, `EvidenceFor`, and `Explains` remain topicality, epistemic support, and explanation respectively. `Infer` remains an actual reasoning event. `AnswerFor` remains typed answerhood for QuestionContent. `Contrast` remains a discourse relation beyond And or one holder's Expect state.

Registered inventory remains **206**; semantic primitive candidates remain **126**.

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
