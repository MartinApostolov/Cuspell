# Active Cuspell Decisions

_Status: current cross-spec design invariants. Historical decision log through D-179 is archived at `archive/decisions/DECISIONS_D001_D179.md`._

This file contains only decisions that a maintainer should treat as **currently active**. Detailed semantics live in `docs/spec/`; this file is a compact set of cross-cutting rules that should not silently regress.

## Language purpose

Cuspell is a formal, compositional language for objective freeform magic. A valid magical command must have a mechanically determinable meaning rather than rely on what the caster or GM probably intended.

## Language and magic are separate layers

A sentence may be grammatically and semantically valid without being magically executable. Parsing, typing, semantic closure, reference resolution, world capability, RequiredPower, and resource payment remain separate checks.

## Mana follows written meaning-bearing signs

Every meaning-bearing rune/sign occurrence written in a magical command costs mana. **Every core entry in `language/core/lexicon.json` is one registered rune, written with exactly one glyph, with `rune_cost: 1`.** This includes the formal operators `BeforeValue` and `AfterValue`: they are not Old Names or two-rune composites. Pure grammatical structure may cost zero. Semantic normalization does not refund written cost.

Historical Old Names and explicit multi-rune compositions use the cost of their constituent registered runes and do **not** appear as separate core-rune entries. Legitimate registered linguistic compression may reduce mana. Arbitrary player-created aliases/New Names do not become free magical macros.

## Approved visual mapping is separate from font input

The 217 registered core runes and separate numeric-one `@` have **218 distinct user-approved glyph designs** drawn from the 234 survivors. The 16 leftover designs remain approved spare shapes, not lexicon entries. `language/core/glyph_assignments.json` is the single canonical mapping keyed by stable lexicon IDs; the original G/A/R source IDs and their temporary PUA positions stay intact.

The existing PC test font is deliberately preserved. A future typing page can convert rune-name transliteration to approved glyphs without modifying the font binary, font shape or normal PUA codepoints. Glyph display does not execute Cuspell grammar, spell logic, or mana cost checks.

## Canonical surface is flat Cuspell v0.8

Normal Cuspell should look like a foreign language, not a printed AST.

- sentence-final `.`, `?`, and `!` mark assertion, question, and command;
- heads normally precede their arguments;
- typed frames resolve flat left-to-right application;
- adjacency may form a registered lexical compound or one uniquely typed tight local application;
- ambiguity is rejected rather than guessed;
- parentheses are the explicit player-facing fallback for grouping when flat typing/tight adjacency are insufficient;
- pipe hard-binding is parser/debug and historical compatibility only, not player-facing Cuspell.

Older surface forms remain parser-compatible only where current tests intentionally preserve them.

Checkpoint 104 closes the grouping-policy question: pipe adds no semantic capability beyond tight adjacency plus parentheses, so keeping it player-facing would create a second binding system to learn without increasing expressive power.

## Sequence and Concurrent stay language-like

`Sequence E1 E2 ...` and `Concurrent E1 E2 ...` are flat variadic constructions.

Sentence end closes the group. If later sentence material must follow, `SequenceEnd` or `ConcurrentEnd` closes it first. These are canonical zero-mana grammatical boundary markers and are retained specifically to avoid requiring pseudocode-style tree notation in normal prose.

## Argument omission is not inference

Every Relation and Process has registered frames. Required roles must be present. Optional roles may be omitted, but omission means unspecified/unconstrained, not “infer what the caster wanted.”

Checkpoint 103 removes English `:role` selectors from current Cuspell. Optional arguments are positional. A trailing optional slot may simply be absent; `_` advances over exactly one optional slot when a later slot or outer argument must follow. `_` costs zero mana because it carries no role identity or world meaning. It is invalid for required slots. Internal frame labels such as source, authority, context, and instrument are implementation/specification metadata only.

## Types carry most grammatical regularity

Multiple typed frames are allowed only when they instantiate a coherent semantic core. Different English meanings that merely share a label should not be hidden as one rune.

The parser never chooses a reading because it sounds more plausible.

## Negation, zero, opposites, and converse remain distinct

`Not`, numeric `Zero`, and typed `Opposite` are separate operations. Relation converse is expressed by writing the same underlying relation with its actual roles/arguments in the intended order rather than by a generic Converse rune.

## Names are layered

- semantic roots and formal constructors belong to the language;
- world concepts provide stable identities/classifiers for ordinary concepts;
- Old Names are historically established vocabulary with frozen name-unit cost;
- New Names are ordinary naming/reference relations and do not gain magical macro power.

Draft Old Names remain redesignable while the language is not frozen.

Checkpoint 110 extends the existing Old Name expression mechanism to **typed parameterized expressions**. Checkpoint 123 re-audits that mechanism and retains it narrowly.

A parameterized Old Name is allowed only when its frozen meaning is already exactly expressible in ordinary Cuspell. Its parameters are all required, typed, positional, and lexically scoped. Actual written arguments are parsed in the caller's scope, but the frozen template itself cannot capture caller binders. Optional parameters, hidden/default arguments, ignored/dead declared parameters, and a second named-role grammar are not allowed.

Frozen expression Old Names are executable language data, so whole-registry validation compiles their frozen source under lexical template scope. Invalid syntax, undeclared/free variables, type-invalid expansion, recursion, unsupported parameter metadata, and unused declared parameters are registry errors rather than failures deferred until first use.

The Old Name Sign pays its frozen historical `name_units` cost once; written arguments pay their normal mana cost. A parameter may appear multiple times in the frozen expansion while being written once by the speaker. That co-reference compression is intentional lexical structure, analogous to an ordinary word/frame reusing one participant internally; it is safe because only frozen pre-magic registry entries receive it. New Names never gain callable/macro behavior.

`«TransferHave»` remains the only current parameterized expression Old Name. It does not restore Give as a semantic root: checkpoint 94 already proved the former Give meaning exactly equal to `Concurrent EndHave giver theme BeginHave recipient theme`. The historical word costs 2 for its frozen Transfer + Have name units, while `«TransferHave» Self This You!` costs 5 including arguments instead of 9 for the fully written composition.

Parameterized Old Names remain historical lexical compression, not a substitute for missing semantics. If a word such as Dance, Cook, Read, Teach, or generic Heal carries a distinction not exactly present in the current semantic basis, hiding an approximate composition inside an Old Name is not allowed.

## Current semantic inventory is reduction-closed for now

Checkpoint 95 closed the global reduction sweep at **205 registered base entries** and **125 semantic primitive candidates**, with **0 unresolved** and **0 derived** candidates. Checkpoint 100 temporarily added `Interpret`; checkpoint 101 superseded it and returned the totals to **205 / 125**. Checkpoint 105 deliberately restores `Almost` as a formal constructor after proving the attempted boundary-Distance reduction semantically invalid. Checkpoint 107 restores three independently necessary civilization/body-state distinctions—`Health`, `Pain`, and `Ill`—after checkpoint 106 showed they are not exactly reducible to `Damage`, `Life`, or each other. Checkpoint 108 adds positive `Male` alongside `Female` rather than treating logical negation as a biological converse. Those checkpoint-108 totals were **212 registered entries / 131 semantic primitive candidates / 55 formal constructors**. Subsequent accepted meanings (Rotate, Authority, Pressure, Create, Find, Represent, TimeFlow) bring the **current** totals to **217 registered entries / 136 semantic primitive candidates / 55 formal constructors**. The current registry also has 276 semantic frames and 53 multi-frame entries; see `language/core/lexicon.json` and `language/core/inventory_roles.json`.

Further semantic deletion or addition is evidence-triggered, not sweep-driven. Exact semantics outrank minimizing the raw root count, but a new root should not survive when an existing general construction can preserve the same distinctions.

## Health-state distinctions survive exact reduction

Checkpoint 107 introduced `Health`, `Pain`, and `Ill` as independent meanings. Checkpoint 119 re-tests all three after the later Attribute, typed world-Kind, and parameterized Old-Name machinery exists.

The exact-reduction result remains:

- `Damage` is ordered physical injury/damage.
- `Health` is ordered overall biological functional condition; generic `Evaluate` does not select this Attribute dimension.
- `Pain` is ordered experienced pain/nociceptive suffering; `Sense` is an acquisition EventSpec, not pain intensity, and generic `Evaluate` likewise does not name the dimension.
- `Ill` is a persistent pathological-state Property; it is not Low Health, High Damage, Pain, Not Life, or an ordinary static world-Kind classification.
- `Life` is the biological alive/living state.

The decisive test is independence: allowed worlds can hold Damage, Health, Pain, Ill, and Life facts in combinations that the proposed reductions would collapse. The generic Attribute machinery operates on a supplied AttributeDescriptor; it does not create the missing semantic descriptor from an English gloss. Moving the distinction into opaque world data would therefore hide rather than reduce it.

There is no standalone `Heal` root. Healing/recovery must state the actual result, such as reducing Damage, ending Ill, improving Health, restoring structure, or an explicit combination.

## Biological sex keeps independent positive persistent classifiers

Checkpoint 108 added `Male` alongside `Female` rather than defining either through negation. Checkpoint 120 re-tests that choice against the later Attribute and typed world-Kind machinery.

The result remains two positive Properties:

- `Male(Entity) -> StateProposition`;
- `Female(Entity) -> StateProposition`.

Neither is the logical complement of the other. The core language therefore continues to permit both, neither, or additional world-defined classifications rather than asserting universal binary exhaustiveness.

A universal `Sex` Attribute is not a reduction: it adds a productive descriptor/value family and, if single-valued, imposes a functional/exclusive axis that not every allowed world shares.

Ordinary registered world Kinds are also not exact replacements under the current type system. Their classifier application yields `Proposition`; Male/Female are persistent state predicates yielding `StateProposition`, including `Begin`/`End` classification transitions. A new stateful-Kind mechanism would be a broader structural addition, not evidence that these two roots are already redundant.

Exact membership rules remain world ontology. These roots are biological classifiers, not a universal social-gender system; cultural identity, role, title, or presentation belongs in world concepts/Names or independently justified social semantics.

## Multi-frame overloads must preserve one semantic core

Checkpoint 99 audited all 51 entries that were multi-frame at checkpoint 98.

- 33 are straightforward same-operation typed generalizations;
- 15 contain contextual or shorthand forms of the same operation;
- checkpoint 99 found 3 lexical semantic boundary crossings: `Distance`, `Sense`, and `Name`.

Checkpoint 100 resolves the hidden `Sense` overload: `Sense` now has only the explicit-channel sensory-acquisition frame. Checkpoint 101 supersedes the temporary `Interpret` root by keeping the underlying pieces explicit: `Meaning` supplies the real Sign-to-content relation, `Understand` supplies comprehension of that mapping, `Sense` supplies perception, and `Begin Understand` remains distinct when a new mapping is actually learned.

Checkpoint 101 also resolves `Name`. `Name` now has only its nonfunctional naming-relation frame. Inverse relation lookup uses the existing `Collect` + `Unique` construction, with `Collect` generalized to preserve the binder's semantic type. This mechanism is general: it can select an Entity named by a Sign, a Region named by a Sign, or Information uniquely related by `Meaning` without pretending those relations are globally functions.

Checkpoint 105 resolves the remaining `Distance` irregularity. Physical `Distance` is spatial-only and returns Length. Contextual near-satisfaction/near-occurrence is represented by the distinct `Almost` operator. `Almost` has Proposition and EventSpec frames with one semantic core, so **no genuine multi-frame lexical irregularity remains** from the checkpoint-99 audit.

New overloads should be accepted only when their frames share one semantic core.

An optional role does not by itself justify a second frame. `GratefulTo` uses one frame with an optional positional basis value; omission is handled by the general frame/omission grammar.

## Registered world Kinds keep explicit classified-value domains

Checkpoint 122 re-audits checkpoint 116's `classifies_types` mechanism and retains it.

A world concept with semantic type `Kind` may declare `classifies_types`.

- absence means exactly `["Entity"]`; explicit `["Entity"]` is redundant metadata;
- event categories may declare the distinct `EventSpec` and `Event` domains;
- content categories may declare `Information`;
- calendar-period categories may declare `TimeInterval`;
- targets must be known concrete semantic types rather than `Any`, `SemanticValue`, `Binder`, or `Kind`;
- duplicate target types are invalid;
- the same validation applies to core and setting/world-package concepts.

The parser obtains predicate subject types and named-Kind binder types from the same registered concept metadata. A named Kind with one classifier domain therefore types its binder correctly—for example Story -> Information and Day -> TimeInterval.

A Kind with multiple incomparable classifier domains, currently the EventSpec/Event categories, cannot supply one sound binder type because Cuspell has no union binder type. Such a named-Kind binder is rejected with guidance to bind `EventSpec` or `Event` explicitly and apply the Kind predicate in the query.

The full current world-concept scan found sixteen non-default classifier declarations and no evidence-supported legacy concept migration. In particular, a registry `domain` label such as `information` is organizational metadata, not proof that the concept classifies the semantic type `Information`; older Record/Book/Rule/Law-style Kinds therefore remain Entity-classifying unless their ontology is separately changed.

This metadata belongs to the world classifier, not to the historical Old Name spelling. Direct lexical Kind roots keep their own registered frames; Kind is not made universally polymorphic.

## Calendar periods are world categories, not universal time units

Day, Night, Season, Year, and Month are registered world Kinds whose members are `TimeInterval` values.

They do not silently define fixed `Quantity:Time` conversions. Conventional day/year/etc. Units, when a setting uses them, must be registered separately with explicit conversion rules.

Date is calendar `Information`, not fundamental time itself; the world calendar maps that Information/its Signs to TimePoints or TimeIntervals.

Age remains an explicit elapsed-time construction from a chosen origin:

`Extent Interval start reference`

The language does not choose birth, creation, activation, completion, or another start point implicitly.

## Recognized authority survives exact deontic reduction

Checkpoint 118 re-tests `Authority(holder,scope) -> StateProposition` against `Permitted`, `Obligated`, Rule/Law vocabulary, `Can`, `Control`, ownership/possession, and `Cause`.

`Authority` records persistent recognized social/institutional standing or normative competence to issue or validate binding rules, permissions, obligations, or decisions for the supplied scope.

It remains independently necessary because:

- `Permitted` states that a particular EventSpec is allowed; being allowed to issue a statement does not make the statement binding;
- `Obligated` states a duty and may name a context/source, but does not state who has competence to create or validate duties;
- `Can` states capability; an incapacitated office-holder may retain Authority, while a coercive actor may be capable of producing an outcome without legitimate standing;
- `Control` is factual control/manipulability and can diverge from recognized legitimacy;
- Rule/Law vocabulary can identify normative rules, but does not itself relate an arbitrary holder to an arbitrary jurisdiction/scope;
- ownership/possession and causation likewise do not establish recognized standing.

A decisive countermodel is possible: two worlds can have the same current permissions, obligations, rules, control, and capabilities while differing only in which office-holder's later decision is recognized as binding. Any exact representation therefore needs a fact equivalent to `Authority`; hiding that fact only in world data would make it unavailable to Cuspell expressions.

The world model determines the source, jurisdiction, legitimacy rules, delegation, revocation conditions, succession, and conflicts of authority. The language exposes the relation without assuming one universal political/legal theory.

## Rigid rotation survives exact geometric reduction

`Rotate(Entity,pivot,axis,turns)` is a productive spatial Process. Checkpoint 121 re-tests it against the stabilized geometry system rather than preserving the checkpoint-114 addition automatically.

It remains independently necessary because:

- `Move` constrains translational position/path and does not encode rigid orientation change;
- `Offset` constructs a Location from an origin/direction/distance but says nothing about an Entity's orientation;
- CoordinateFrame and Direction values provide spatial references but the current language has no Entity pose/orientation Attribute whose value could be changed;
- `Form` is intrinsic geometry/shape, so `Change Form` would incorrectly treat a rigid turn as reshaping;
- moving every Part along separately constructed arc Paths would require preserving all relative distances/orientations under one shared pivot/axis/turn amount, which is a hidden rigid rotation transform rather than a smaller exact composition.

A rigid object can rotate about its own anchor with no anchor translation and no Form change, while ordinary Move can translate it without any rotation. These counterexamples separate the truth conditions.

The rotation amount is a signed dimensionless number of full turns. The world/frame convention fixes positive rotational direction.

## Pressure is a semantic Attribute; its dimension is derived

Checkpoint 126 resolves the physical-measurement question raised by the Verne corpus pressure.

`Pressure` is a registered `AttributeDescriptor` with two query frames:

- `Pressure(Entity) -> Quantity:Pressure` where the active world defines a scalar pressure state for that entity/material/system;
- `Pressure(Location) -> Quantity:Pressure` for local ambient pressure.

Its Quantity dimension is not a new base dimension. It is the registered derived vector:

`Mass · Length^-1 · Time^-2`.

This distinction is deliberate. Dimensional arithmetic can prove that two values have compatible Pressure dimensions, but dimensional equality does not identify what physical relation produced the value. An arbitrary Mass/Length/Time expression is not thereby the Pressure of an Entity or Location.

A generic world-package mechanism for silently minting new callable AttributeDescriptors is rejected for now. Such a mechanism would move irreducible language semantics into setting metadata, complicate static descriptor-output typing, and let world data create meaning-bearing spell vocabulary without the normal rune/Old-Name boundary. World packages instead provide objective values, applicability conditions, material behavior, gradients, and causal laws for registered language descriptors.

No `PressureUnit` Old Name is added. Derived Pressure quantities can be built from the existing Mass, Length, and Duration units with ordinary arithmetic.

This decision does not imply that Force, Energy, charge, voltage, acceleration, or every scientific measurement word should become a root. Each candidate still requires an independent exact-reduction test. The Pressure addition is supported because current language states can agree on all existing registered Attributes while differing in scalar mechanical pressure, and because neither a dimension vector nor current Distribution/Density machinery reconstructs that distinction.

## Referenced TimeIntervals expose their own boundaries and finite extent

`Begin`, `End`, and `Extent` apply to `TimeInterval` as well as their existing Event/state meanings.

- `Begin(TimeInterval) -> TimePoint`;
- `End(TimeInterval) -> TimePoint`;
- finite `Extent(TimeInterval) -> Quantity:Time`.

This lets named/referenced intervals be inspected without reconstructing the syntax that originally created them.

For explicitly unbounded intervals, missing boundaries or non-finite duration are unavailable values; Cuspell does not invent a boundary or finite Quantity.

## Inverse relation selection is explicit

Relations such as `Name` and `Meaning` remain nonfunctional. To obtain a value from the inverse direction, bind the desired type, `Collect` values satisfying the relation, then apply `Unique` only when exactly one value is objectively available under the stated constraints. This is selection over a relation, not a hidden function frame.

## Beginner Cuspell is spell-first, but semantic-sign count is not total learning load

Checkpoint 127 made the first teaching projection follow Cuspell's original design goal: **teach magical Commands first**, not general conversation first. The SRD level 0–2 corpus remains a stress test, not a compatibility or balance target.

Checkpoint 135 correctly separated the 50-sign coverage projection from a smaller teaching progression, but checkpoint 136 stress-tests the resulting 16-sign core and finds one hidden-complexity problem: its final 11→16-sign tier simultaneously introduced five semantic signs plus `@`, an Old Name unit, a typed binder, bound-variable references, and Create profile/continuation scope.

Current teaching distinguishes four learning layers plus an independent coverage benchmark:

- **11-sign first-lesson semantic core** — movement, Begin/End state transitions, and simple yes/no Find;
- **18-sign beginner spellcraft course** — measured change, fresh creation, finite maintenance, and exact-event protection;
- **24-sign intermediate composition course** — shared representation, proposition conjunction, ordered/concurrent event composition, and finite repetition;
- **29-sign advanced extension** — simple reactive programming, bounded multi-target distribution, and relative TimeFlow;
- **50-sign coverage projection** — retained only to demonstrate broad SRD-like effect coverage.

The semantic core is cumulative:

1. `This There Move Begin End Whole` — 6;
2. add `You Locked Magic` — 9;
3. add `Self Find` — 11.

The first follow-on module adds `Change Light` and separately teaches `@` plus the Old Name `«LightUnit»`.

The fresh-creation module then adds only `At Create`; it introduces `x:Entity` / `$x` and reuses all earlier spell vocabulary:

`Create x:Entity At $x There Change $x Light «LightUnit» @!`

This remains distinct from:

`Change This Light «LightUnit» @!`

which makes an already-existing Entity luminous.

`Here` is not a prerequisite because `There` already supplies a Location. `Here` becomes optional convenience vocabulary.

`Ill` is likewise not a structural prerequisite. Once Begin/End/Find are understood, adding `Ill` immediately gives illness/cure/diagnosis expressions without any new grammar. `Magic` replaces it in the required core because Begin/End/Find over Magic is more central to spellcraft while exercising exactly the same state pattern.

Selection rule:

- count registered semantic signs separately from grammar/notation concepts;
- teach one reusable semantic pattern at a time;
- every required core sign should appear in the core spellbook;
- teach measured quantities before fresh binder scope;
- reuse already-known references rather than adding convenience vocabulary as hidden prerequisites;
- keep `And`, `Repeat`, `Concurrent`, `Each`, `Collect`, `Member`, `Trigger`, `Persist`, `Prevent`, `Represent`, and `TimeFlow` out of the semantic core;
- do not add a root merely because an SRD spell has a familiar name.

The exact orb/Form of the Light creation spell is still not silently inferred by language semantics. If a setting wants a canonical glowing orb, its world generation rules must deterministically realize that profile or the spell must use a more specific generation profile.

The retained 50-sign projection stays current as a coverage benchmark, not a learner starter.

Checkpoint 137 continues the same modularity rule for duration/protection instead of enlarging the semantic core.

The next stages are:

- add `ThisInterval Persist`, reaching 17 semantic signs;
- then add `Prevent`, reaching 18 semantic signs.

`ThisInterval` is a contextual typed reference that must resolve to one objectively designated TimeInterval through the command/casting environment. It is not an omitted duration literal and never means “forever” by itself.

Beginner `Persist` is taught only as active maintenance of an already-stated StateProposition over that interval:

`Persist Whole This ThisInterval!`

It remains semantically distinct from `Begin`: establishing a missing state and actively maintaining that state are separate operations.

Beginner `Prevent` is taught only in the simple exact-event frame:

`Prevent Move This There ThisInterval!`

`Prevent End Whole This ThisInterval!`

`Prevent Begin Locked This ThisInterval!`

This does not mean “prevent anything that has a similar consequence.” It blocks the supplied EventSpec over the interval.

The bound matcher form used for generic interception/antimagic remains advanced:

`Prevent e:EventSpec Magic $e _ ThisInterval!`

That form adds an EventSpec binder, predicate matching, optional spatial scope, and pre-commit execution interception; those concepts are intentionally not smuggled into the simple protection lesson.

Checkpoint 138 applies the same rule to shared representation.

The required representation module adds only:

`Vision Represent`

reaching 20 cumulative semantic signs.

The learner reuses existing state/control patterns:

`Begin Represent This You Vision!`

`End Represent This You Vision!`

`Persist Represent This You Vision ThisInterval!`

and can reuse the already-learned Create binder without adding conjunction:

`Create i:Entity At $i There Begin Represent $i This Vision!`

This teaching split is intentional:

- `Represent` is an objective persistent carrier/content/channel relation, not forced `Sense`;
- `Vision` is the first explicit SenseChannel, while Hearing/TouchChannel are optional later vocabulary;
- `Sign` classification is not required to understand representation itself;
- `And` is not pulled forward merely to build a richer illusion profile;
- the represented content does not become true, physically present, solid, believed, or understood;
- exact carrier realization remains subject to deterministic world/media rules.

Multi-channel representation, combined carrier profiles, scheduled ending, and programmed illusion behavior remain part of later conjunction/programming material.

Checkpoint 139 keeps programming/multi-target teaching modular rather than introducing all control signs at once.

The progression adds:

1. `And` -> 21 cumulative semantic signs;
2. `Sequence Concurrent` -> 23;
3. `Repeat` -> 24;
4. `Collect Member Each` -> 27;
5. `Trigger` -> 28.

The teaching boundary deliberately distinguishes these meanings:

- beginner `And` is proposition/state conjunction; event-level transactional And remains advanced;
- `Sequence` is ordered execution and `Concurrent` is simultaneous composition;
- `Repeat` is finite count-based recurrence and never means an unbounded loop;
- `Collect` constructs an explicitly typed, resolvable collection; it does not grant omniscient search;
- `Each` is required for distribution because singular Process frames never silently apply to every collection member;
- simple `Trigger(condition, action, lifetime)` is one-shot by default and does not export a hidden witness.

Checkpoint 139 also repairs one teaching-list omission: general ordered programming requires `Sequence`. The earlier candidate list included `Concurrent` but left `Sequence` out. Create's immediate continuation is special lexical scope for a fresh result and is not a replacement for general ordered execution.

The canonical bounded multi-target teaching shape is:

`Each Collect x:Entity Member $x This y:Entity Begin Magic $y!`

Here `This` must designate an Entity whose group membership is objectively resolvable in the active context. The Entity binder does not authorize a world-wide search.

The simple Trigger teaching shape is:

`Trigger Locked This End Locked This ThisInterval!`

Bound-witness Trigger, general selectors/ranking/randomness, mixed logical branch selection, event-level And transaction semantics, and richer programmed illusion behavior remain advanced.

Checkpoint 140 completes the planned modular teaching path with **one required time-flow sign**:

`TimeFlow`

This reaches 29 cumulative semantic signs while keeping the semantic core at 11.

The required lesson reuses already-known `Self` / `You` references, positive integer `@` notation, `Persist`, and `ThisInterval`:

`Persist TimeFlow You Self @@ ThisInterval!`

The teaching rule is:

- the subject and reference are always explicit;
- `@@` is sufficient to teach faster relative progression without adding another semantic sign;
- `Zero` is optional vocabulary for exact stopped local progression;
- `Divide` is optional arithmetic for fractional slow-time such as `Divide @ @@`;
- Region TimeFlow is advanced because boundary/crossing realization rules matter;
- negative rates remain invalid, so time reversal is not smuggled into TimeFlow.

TimeFlow is taught as whole local physical/process temporal progression, not as `Repeat`, event `Rate`, movement speed, action-count metadata, or time travel.

Checkpoint 141 completes that whole-progression stress test.

The 29-sign path is retained, but **it is not one beginner course**.

The stable teaching boundaries are:

- 11 signs — first-lesson core;
- 18 signs — beginner spellcraft, ending after simple exact-event `Prevent`;
- 24 signs — intermediate composition, ending after finite `Repeat`;
- 29 signs — advanced extension, ending with `TimeFlow`.

The boundary criteria are structural rather than game-power-based:

- beginner material constructs direct effects and exact protection;
- intermediate material introduces a new representation ontology plus general composition/control flow;
- advanced material introduces persistent watchers, nested collection binders/distribution, or explicit relative temporal frames.

Executable progression checks confirm that each required example uses only registered semantic signs introduced no later than its own stage. No hidden semantic-sign prerequisite was found.

The stress test makes one ordering repair. Simple `Trigger` moves before `Collect Member Each`: Trigger adds a watcher model but reuses already-known condition/action/lifetime forms and no new binder syntax, whereas bounded multi-target distribution requires a selection binder, a distribution binder, collection resolution, and repeated event instantiation.

Current advanced order is therefore:

1. `Trigger` -> 25 signs;
2. `Collect Member Each` -> 28;
3. `TimeFlow` -> 29.

The current machine-readable learning truth is `language/subsets/spellcraft_progression_v1.json`. The player layer is intentionally split: `BEGINNER_SPELLCRAFT.md` stops at 18 signs, while `SPELLCRAFT_PROGRESSION.md` carries the intermediate and advanced stages.

The teaching boundary is now stable enough to stop expanding the planned course and return primary design attention to rune/glyph visual design.


## Normal spell surface should remain parenthesis-free

Checkpoint 128 re-tests the grouping policy specifically against spell construction.

The canonical teleport-like command is:

`Concurrent EndAtSelfHere BeginAtSelfThere!`

not a parenthesized AST-style rendering.

`Sequence` and `Concurrent` consume flat EventSpec lists, and tight adjacency forms uniquely typed local application. Parentheses remain legal zero-mana fallback grouping, but curated beginner spell examples are now required to avoid them.

The advanced SRD spell pass also confirms that spell names are pressure examples, not vocabulary candidates. High-level effects mostly stress reusable semantic/execution families rather than requiring roots named Counterspell, Teleport, Wish, and so on.

Checkpoint 128 isolates five advanced spellcraft families for later exact audits:

- fresh deterministic generation;
- bounded unknown-information acquisition;
- persistent shared illusion/representation;
- magical-execution interception/suppression;
- time-flow manipulation.

No semantic addition follows merely from appearing in this list.

## Fresh creation allocates a new identity

Checkpoint 129 closes the creation gap that had remained explicit since the identity model was first stabilized.

Creation is not:

- `Begin Exist X`, which acts on an already identifiable X;
- `Change X ...`, which preserves X's identity;
- Kind predication;
- naming;
- restoration/resurrection of a known identity.

The productive form is:

`Create x:Entity profile`

or a named Entity-Kind binder such as:

`Create x:«LowExtent«MoveLifeThing»» ...`

Each Create invocation allocates exactly one Entity identity that has never previously been allocated. The binder is scoped through the objective post-creation profile and, when present, one immediate continuation EventSpec. The profile must actually constrain or relate the new result.

The binder domain contributes type/Kind constraints; the written Proposition contributes additional immediate post-creation constraints. World generation data may supply deterministic canonical details needed to realize the result, but it does not add hidden language semantics or randomly choose execution-significant details.

Create implies the fresh result Exists. It does not silently imply Life, consciousness, Magic, ownership, Control, a Name, a body/material, or any particular Form unless those follow from the binder domain/profile/world generation rules.

Repeated Create invocations allocate distinct identities.

Checkpoint 130 adds the optional continuation because a fresh-result binder that ended at the profile could not directly support ordinary create-then-use spell composition such as a conjured projectile. The continuation executes after successful creation/profile realization with the fresh binder still in lexical scope; later failure follows the ordinary non-rollback execution rule.

The same checkpoint re-audits the level-0-to-2 starter examples for accidental semantic collapse. Exact duplicate recipes are allowed only when the chosen objective effect slice is genuinely the same. Light/Faerie Fire and generic movement/Magic Missile are no longer duplicate recipes; Faerie Fire now collects an objectively designated Group's members rather than relying on contextual `They`; the regression suite explicitly records the remaining intentional duplicates.

This is a semantic primitive candidate because two worlds can agree about every already identifiable Entity and every current state transition while differing on whether a genuinely new identity is allocated. No composition over Begin/End/Change/Name/Kind can reproduce that freshness condition.

## Find is bounded factive information acquisition

Checkpoint 131 closes the second advanced spellcraft gap with one productive Process:

`Find mind scope proposition`

`Find mind scope binder proposition`

The explicit scope is an information-access boundary, not an implicit spatial/topic/source relation. The query itself must mention/relate to the scope, and an open query must use its answer binder.

Successful Find gives the designated mind the truthful complete answer available under that scope. A yes/no Find yields the true polarity. An open Find yields the complete satisfying binding set within the permitted scope. A successful empty set is distinct from blocked or incomplete access.

At execution time, every otherwise unavailable fact needed for the answer must be licensed by the scope and world capability. Range, wards, occlusion, privacy/mind protection, temporal access, information volume, RequiredPower, and setting metaphysics may therefore make a valid Find fail. Failure never masquerades as “false” or “no matches.”

Find remains distinct from:

- `Question`, which constructs/asks a query but does not acquire its answer from reality;
- `Sense`, which is explicit-channel sensory acquisition;
- `Collect`, which only selects from already resolvable domains;
- `Infer`, which requires evidence and is not automatically factive;
- `Know` / `Begin Know`, which require the content to already be supplied;
- `AnswerFor`, which relates Information to a QuestionContent but does not source it.

`If` and `Trigger` do not reduce Find: their conditions can be evaluated only when the needed information is already available to the execution context. Hidden-condition divination therefore requires an explicit acquisition capability.

Future-oriented Find works only if the world exposes an objective future/predictive information source; it does not make an undetermined future determinate.

This is a semantic primitive candidate because two worlds can agree on the written query, current sensory evidence, known Information, and all ordinary selection relations while differing on whether magic grants access to the hidden truthful answer under the stated scope.

## Shared illusion uses objective Represent carriers

Checkpoint 132 closes the persistent multi-observer illusion/representation gap with one reusable Relation:

`Represent carrier content channel`

It is a persistent StateProposition stating that an Entity presents/depicts semantic content through an explicit SenseChannel.

Represent is not reducible to:

- `Meaning`, which is semantic interpretation and context/language-sensitive;
- `Sense`, which is one observer's acquisition event;
- `Form` or `ShapeLike`, which describe actual geometry;
- a world image Kind, which classifies a carrier but does not state arbitrary represented content.

A magical shared illusion is compositionally a created Sign/Entity with Magic, spatial placement, and one or more Represent states. It need not be Matter. Observers independently Sense the same carrier under ordinary access physics.

Representation never makes its content true or physically present. Additional sensory channels, solidity, damage, light emission, sound pressure, movement, lifetime, and programmed behavior remain explicit.

This is a semantic primitive candidate because two worlds can agree on the carrier's actual Form, Meaning, observer Sense events that have or have not occurred, and world Kind classification while differing on what content the carrier perceptually presents through a channel.

## Magical suppression is a bound Prevent pattern, not a spell root

Checkpoint 133 closes the generic magical-execution interception gap without adding a registered entry.

Two existing meanings are generalized in their natural typed domains:

- `Magic(EventSpec/Event)` classifies magical-execution provenance;
- `Prevent e:EventSpec predicate region? interval` installs a pre-commit matcher/interceptor.

Canonical antimagic-style pattern:

`Prevent e:EventSpec Magic $e ThisRegion ThisInterval!`

The candidate binder is supplied by the execution engine before commit. The predicate must actually use the binder. The optional Region restricts interception by objective realization footprint.

This is not reducible to Trigger because a Trigger reacting to `Happen E` is too late to veto the commit. It is not reducible to `EndMagic` because that acts on an already active selected effect/state. It is not a Counterspell root because the same machinery can intercept any objectively classifiable EventSpec family.

No primitive/root count changes. The change adds typed frames/execution semantics only.

## Time-flow manipulation uses explicit relative TimeFlow

Checkpoint 134 closes the final unresolved advanced spellcraft family with:

`TimeFlow subject reference rate`

for Entity or Region subjects.

The reference frame/worldline is explicit. The rate is a nonnegative dimensionless factor:

- `@` = equal progression;
- `Zero` = stopped progression;
- greater than @ = faster;
- between Zero and @ = slower.

TimeFlow is not reducible to:

- `Rate(EventSpec,interval)`, which measures selected event occurrence frequency against already-defined time;
- `Repeat`, which schedules selected repetitions;
- `Prevent`, which blocks specified classes of events;
- changing movement speed or action counts, which affects only selected processes rather than all local physical/process evolution.

Region TimeFlow is interpreted by the executor over objective realization footprints/boundaries. Entity TimeFlow applies to that Entity's temporally evolving processes.

Negative rates are rejected; time reversal is not silently included.

This is a semantic primitive candidate because two worlds can agree on every event frequency, scheduled repetition, prevented event class, position, capability, and ordinary TimePoint/TimeInterval fact while differing on the relative rate at which one local physical frame evolves.

## Current project phase is language stabilization

Before glyph design or game/world execution becomes primary work, Cuspell should have:

- one clean current repository layout;
- one clean player-facing grammar;
- current specs that agree with the parser;
- stable regression/corpus coverage.

## Repository layers are deliberately separated

Checkpoint 98 establishes a repository invariant:

- current machine truth lives in `language/` and `world/`;
- current maintainer/design truth lives in `docs/` and `docs/spec/`;
- current executable regression truth lives in `tests/`;
- player/PC reference lives in `player/` and must remain a checked projection of current truth;
- superseded snapshots, completed audits, historical corpus passes, old syntax/test fixtures, and the long decision history live in `archive/`.

Do not put completed audit snapshots back into the current-doc root merely because they are useful history. Preserve them in the archive and summarize only their current consequences in state/decisions/specs.

## Source-of-truth boundary

Current truth lives in `language/`, `world/`, `docs/spec/`, this file, `docs/CURRENT_STATE.md`, and executable `tests/`.

`player/` is a player-facing projection of current truth and must not invent semantics.

`archive/` is historical evidence only. If archive material conflicts with current files, the current files win.
