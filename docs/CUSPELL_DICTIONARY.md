# Cuspell Dictionary and Writing Guide

_Status: human-facing reference for the current executable language_

This is the working dictionary for Cuspell.

The **Rune** column is intentionally blank. The Latin/English-looking names in the **Transliteration** column are temporary readable labels for the semantic roots. When the final rune script is designed, its glyphs go in the first column without changing the meanings underneath.

The dictionary currently lists **226 core registered base entries**. Typed measurement units are Old Names built from the single `Unit` root, so they do not add separate primitive rune entries.

## Dictionary

| Rune | Transliteration | Meaning |
| --- | --- | --- |
|  | About | States that Information is about a semantic topic. |
|  | Add | Adds compatible quantities. |
|  | AfterValue | Value of a semantic value/attribute at the ending boundary of an event. Current written cost: 2 runes. |
|  | All | Universal quantifier over a typed binder. |
|  | Almost | Contextual near-threshold property or near-occurrence/non-completion of an EventSpec. |
|  | And | Logical conjunction of propositions or executable conjunction of event specifications where licensed. |
|  | AnswerFor | States that Information is an answer to QuestionContent. |
|  | Area | Area quantity of a Region. |
|  | Assert | Speech EventSpec asserting a proposition; assertion does not make content objectively true. |
|  | At | Persistent spatial relation: an entity is at a Location. |
|  | Attempt | EventSpec in which an agent undertakes a real effort aimed at a goal EventSpec; the goal need not succeed. |
|  | Ball | Constructs a spherical Region from center and radius. |
|  | Before | Temporal order: first event/time point is earlier than the second. |
|  | BeforeValue | Value of a semantic value/attribute at the beginning boundary of an event. Current written cost: 2 runes. |
|  | Begin | Begins a persistent state; also returns an Event's beginning TimePoint. |
|  | Believe | Persistent epistemic state: a mind believes a proposition. |
|  | Beneficiary | Marks an entity as beneficiary of an event. |
|  | Can | States capability to carry out an EventSpec. |
|  | Cause | Causal relation between actual Events, or causative EventSpec where an entity causes an event. |
|  | Center | Returns the center Location of a Region. |
|  | Change | EventSpec that sets an attribute/family value to a target. |
|  | ChangeRate | Rate of change of a Quantity over time; output dimension is the input quantity dimension divided by Time. |
|  | Collect | Constructs a collection from a typed binder/predicate. |
|  | CommittedTo | Persistent commitment relation to an EventSpec. |
|  | Concurrent | Constructs an EventSpec whose component events occur concurrently. |
|  | Confidence | Degree of confidence a mind assigns to a proposition. |
|  | Contrast | Contextual contrast/concession relation; preserves both represented sides. |
|  | Control | Persistent intentional manipulability/control relation. |
|  | Counterfactual | Contextual proposition: in a relevant contrary-to-actual alternative history where the antecedent holds, the consequent holds. |
|  | Count | Returns the nonnegative integer count of members in a collection. |
|  | Density | Scalar density attribute of an entity; returns a Density quantity. |
|  | DesignedFor | Persistent design-function relation between an artifact and EventSpec. |
|  | Directive | Constructs semantic CommandContent from an EventSpec without executing it. |
|  | Distance | Returns the Length distance between two semantic/spatial values. |
|  | DistributionOf | Constructs a spatial Distribution of a resource over a host. |
|  | Divide | Divides quantities and combines their dimensions. |
|  | Duration | Length of time occupied by an event. |
|  | During | Temporal containment/holding of events, points, EventSpecs, or propositions over an explicit interval/reference. |
|  | Each | Applies an EventSpec to each member of a collection. |
|  | Edge | Returns edge Region(s) of an entity/Region. |
|  | End | Ends a persistent state; also returns an Event's ending TimePoint. |
|  | Equal | States exact equality between two values of compatible type. |
|  | Evaluate | Produces an ordered evaluation of a target. Two-argument form names the evaluator; one-argument form uses the discourse evaluator/context. |
|  | EvidenceFor | States that Information is evidence supporting a proposition. |
|  | Exist | State property: exists. |
|  | Expect | Relation: expect; roles mind, content; produces StateProposition. |
|  | Explains | States that an Explanation explains a proposition; a contextual Proposition+Proposition frame covers ordinary discourse explanation (`target because reason`). |
|  | Extent | Returns the occupied/spatial extent Region of an entity. |
|  | Filter | Filters a collection by a typed binder/predicate. |
|  | First | Selects the first member of an ordered Sequence; with an EventSpec it contextually denotes the next/first matching occurrence. |
|  | Form | Geometric/form profile of an entity. |
|  | Gas | Matter-phase value/property: gas. |
|  | Generic | Contextual generic/typical statement; not strict universal quantification. |
|  | Give | EventSpec transferring an entity from giver to recipient. |
|  | Group | Kind: a group entity. |
|  | Gustation | Sense channel: taste/gustation. |
|  | Happen | States that an EventSpec actually occurs, optionally in an interval. |
|  | High | Contextual above-standard predicate; with an AttributeDescriptor it forms a first-class threshold Property such as HighLength or HighHunger. |
|  | Low | Contextual below-standard predicate; with an AttributeDescriptor it forms a first-class threshold Property such as LowHunger. It is not equivalent to Not High. |
|  | Have | Persistent possession/holding relation. |
|  | Hearing | Sense channel: hearing. |
|  | Heat | Scalar heat attribute of an entity. |
|  | Here | Current contextual location. |
|  | If | Conditional: if the condition holds, the consequent proposition/event follows in the represented structure. |
|  | In | Persistent spatial relation: an entity is in a Region. |
|  | Infer | EventSpec in which a mind infers a proposition from Information. |
|  | Inside | States that an entity lies inside a Region. |
|  | Intend | States an agent's intention to carry out an EventSpec. |
|  | Interval | Constructs a TimeInterval from start and end TimePoints. |
|  | IntervalFor | Constructs a TimeInterval from a start TimePoint and duration. |
|  | Joined | Persistent structural relation: two entities are joined. |
|  | Know | Persistent epistemic state: a mind knows a proposition. |
|  | Last | Selects the last member of an ordered Sequence. |
|  | Length | Length attribute of an entity/path. |
|  | Span | Axis-indexed extent in an explicit CoordinateFrame; axis @ is height/up, @@ is width. |
|  | Size | Contextual ordered holistic size/extent evaluation used by HighSize and LowSize; objective magic should use explicit physical measures or a registered size model. |
|  | Life | State property: alive/living. |
|  | Light | Scalar light attribute of an entity. |
|  | Like | States that an experiencer likes a target. |
|  | Liquid | Matter-phase value/property: liquid. |
|  | Magic | State property: magical. |
|  | Mass | Scalar mass attribute of an entity. |
|  | MaxBy | Tie-preserving maximum selector over a collection using a bound ordered key expression. |
|  | Matter | Kind: matter/material substance. |
|  | Meaning | Relates a Sign to its semantic Information/propositional meaning. |
|  | Member | States that an entity is a member of a collection. |
|  | MinBy | Tie-preserving minimum selector over a collection using a bound ordered key expression. |
|  | More | States that the first ordered value is greater than the second. |
|  | Most | Contextual majority/most quantifier over a typed binder. |
|  | Move | EventSpec for moving an entity; magical execution must constrain goal or path. |
|  | Multiply | Multiplies quantities and combines their dimensions. |
|  | Name | Relates a Sign/name to a referent, or resolves a contextual named entity reference. |
|  | Not | Logical negation of a proposition. |
|  | Now | Current contextual time point. |
|  | Obligated | States that an agent is obligated to perform an EventSpec. |
|  | OccurrenceRate | Frequency/occurrence rate of an event pattern over an interval. |
|  | Offset | Constructs a Location by moving a distance from an origin in a Direction. |
|  | Olfaction | Sense channel: smell/olfaction. |
|  | Opposite | Numeric opposite/negation of a quantity; also participates in licensed reversible lexical compounds. |
|  | Or | Logical disjunction of propositions. |
|  | Outside | States that an entity lies outside a Region. |
|  | Overlap | States that two entities/regions overlap spatially. |
|  | Part | States that one entity is a part of another. |
|  | Partition | Contextually partitions a collection into fixed-size subcollections. |
|  | Permitted | States that an agent is permitted to perform an EventSpec; optional explicit authority/context. |
|  | Persist | Actively maintains a state through an interval. |
|  | Phase | Matter phase attribute of an entity. |
|  | Plan | States that an agent has an EventSpec as a plan. |
|  | Plasma | Matter-phase value/property: plasma. |
|  | Power | Raises a quantity to a dimensionless exponent; dimensionful bases require a statically known valid exponent. |
|  | Preserve | Constrains a selected value to remain equal across an event boundary. |
|  | Prevent | Prevents matching future events over an explicit interval/scope. |
|  | Purpose | Purpose/goal relation for a semantic subject. |
|  | Question | Constructs semantic QuestionContent from a proposition or typed open-question binder. |
|  | Random | Selects one member from a collection. |
|  | Ratio | Constructs a ratio from dimensionless numeric components; distinct from numeric division. |
|  | Repeat | Repeats an EventSpec a specified number of times, optionally with a period. |
|  | Requires | States that an outcome/event has a prerequisite proposition. |
|  | Root | Takes a quantity root; dimensionful inputs require a statically known degree that leaves integral dimension exponents. |
|  | Say | Speech EventSpec carrying a proposition, Information, or quoted Sign. |
|  | Self | Current discourse self/speaker/caster reference. |
|  | Sense | Generic sensing EventSpec with explicit sense channel and stimulus. |
|  | Sequence | Constructs an ordered Sequence value, or an EventSpec that executes event specifications in order. |
|  | ShapeLike | States that an entity's form resembles a Kind/template without asserting Kind identity. |
|  | Should | Contextual recommendation/advice for an agent to perform an event; weaker than obligation. |
|  | Sides | Returns side Region(s) of an entity, optionally relative to a frame. |
|  | Simultaneous | States that two events/time points are simultaneous. |
|  | Solid | Matter-phase value/property: solid. |
|  | Some | Existential quantifier over a typed binder. |
|  | SufficientFor | States that a condition is sufficient for an outcome/event. |
|  | Surface | Returns the surface Region of an entity. |
|  | Teleport | EventSpec for discontinuous relocation to a Location. |
|  | That | Contextual previously/situationally salient entity reference. |
|  | ThatEvent | Contextual other/salient event reference. |
|  | There | Contextual non-here location. |
|  | They | Contextual plural/entity-collection reference. |
|  | Thing | General thing/entity Kind. |
|  | This | Current salient singular entity reference. |
|  | ThisEvent | Current salient event reference. |
|  | ThisExplanation | Current salient Explanation value. |
|  | ThisInformation | Current salient Information value. |
|  | ThisInterval | Current salient time interval. |
|  | ThisMethod | Current salient Method value. |
|  | ThisPath | Current salient path. |
|  | ThisRegion | Current salient region. |
|  | Through | States that a Path passes through a Region, or constrains an event to occur through a Region. |
|  | TotalAmount | Returns total quantity represented by a Distribution, optionally within a Region. |
|  | Touch | States that two entities are in contact. |
|  | TouchChannel | Sense channel: tactile touch. |
|  | Toward | Constructs a Direction toward a reference. |
|  | Transfer | EventSpec moving a resource/value from source to destination, optionally with an amount; Distribution transfers may add a named `:profile`. |
|  | Trigger | Creates an EventSpec that fires an action when a condition becomes true within a lifetime/scope. |
|  | True | Boolean/propositional truth literal. |
|  | Tube | Constructs a tubular Region around a Path with a radius. |
|  | UnavailableValueOf | States that a particular attribute value exists but is unavailable/inaccessible. |
|  | Unique | Reduces a collection only when it has exactly one member. |
|  | Unit | General measurement-unit Kind/root. Specific typed units are historical Old Names such as `«LengthUnit»` and `«DurationUnit»`. |
|  | UnknownValueOf | States that a particular attribute value is unknown. |
|  | Use | EventSpec in which an agent uses an instrument to pursue a goal EventSpec. |
|  | Vision | Sense channel: vision. |
|  | Volume | Scalar volume attribute of an entity. |
|  | Want | States that a mind desires an event or proposition. |
|  | When | Schedules/locates an EventSpec at a time point or interval. |
|  | Whole | Property: structurally whole/intact. |
|  | Worship | Ordinary intentional/religious worship Process. Worship does not itself entail that the object is objectively divine. |
|  | You | Current addressee reference. |
|  | Zero | Exact dimensionless numeric zero. |

### Foundational roots added in the first civilization vocabulary pass

These are productive semantic/descriptive roots, not English object nouns. Common objects such as Ship, House, Sword, Book, and Market are registered as descriptive Old Names instead; see `docs/world/FIRST_CIVILIZATION_VOCABULARY.md`.

| Rune | Transliteration | Meaning |
| --- | --- | --- |
|  | Hard | Contextual material/structural hardness Property. |
|  | Sharp | Contextual edge/point sharpness Property. |
|  | Sleep | Persistent contextual sleep-state Property. |
|  | Sign | General Sign Kind used by the information/language system. |
|  | Rule | General rule/instruction Kind. |
|  | Region | General spatial Region Kind. |
|  | Path | General ordered route/path Kind. |
|  | Write | Process in which an agent produces/writes a Sign. |
|  | Read | Process in which an agent reads/interprets a Sign. |

### Ordinary roots added by the audited Yona vocabulary pass

These are productive ordinary-language roots exposed repeatedly by Chapters 1–14 + 47. `Body` has since been migrated to the Old Name `«LifeMatter»`; Yona-specific proper/System terms remain New Names in the optional `world/yona` package.

| Rune | Transliteration | Meaning |
| --- | --- | --- |
|  | Awake | Persistent wakefulness state Property. |
|  | Open | Contextual persistent open-state Property relative to an object's closure/design. |
|  | Locked | Persistent locked/sealed-by-lock state Property. |
|  | Eat | Process: an agent consumes an entity as food. |
|  | Attack | Process: an agent attacks a target. |
|  | Grab | Process: an agent grabs a target. |
|  | Bite | Process: an agent bites a target. |
|  | Climb | Process: an agent climbs a target/entity. |
|  | Fall | Process: an entity falls. |
|  | Female | Ordinary sex/gender classification Property. Exact objective membership belongs to world ontology. |
|  | Jump | Contextual jumping Process; a goal Location may be supplied. |
|  | Stab | Process: an agent stabs a target, optionally with an instrument. |
|  | Limp | Process: an agent moves with a limp. |
|  | Sever | Process: an agent severs a target, optionally with an instrument. |

### Residual ordinary roots from the Chapters 1–14 + 47 cleanup

These close the remaining ordinary combat, injury, graded-body-state, texture/camouflage, reflexive-action, and sound/intensity buckets identified by the audited corpus. `Sound` has since been migrated to the Old Name `«HearingThing»`.

| Rune | Transliteration | Meaning |
| --- | --- | --- |
|  | Damage | Ordered physical-damage/injury degree Attribute. |
|  | Hunger | Ordered hunger-degree Attribute. |
|  | TextureOf | TextureProfile Attribute of an Entity. |
|  | Loudness | Ordered sound-loudness Attribute; objective measurement belongs to the world package. |
|  | Dodge | Contextual evasive Process by an agent, optionally relative to a threat EventSpec. |
|  | Reflexive | States that an EventSpec occurs as an involuntary/reflex response. |
|  | CamouflagedAgainst | Contextual state Relation between a subject and background, optionally relative to an observer. |

Concrete anatomy nouns exposed by the same pass remain Old Names/world concepts rather than primitive roots: body, hand, organ, stomach, wrist, tendon, and wound.


### Historical roots and Old Names from the final deferred-vocabulary pass

Two broadly reusable ordinary roots close the religious/social construction needs:

| Rune | Transliteration | Meaning |
| --- | --- | --- |
|  | Female | Ordinary sex/gender classification Property; exact objective classification belongs to world ontology. |
|  | Worship | Intentional/religious worship Process between an agent and an object; worship does not entail actual divinity. |

The corresponding historical vocabulary is recorded as Old Names rather than direct noun roots:

- monster = `«Attack«Know«MoveLifeThing»»Thing»`;
- god/deity = `«WorshipThing»`;
- goddess = `«Female«WorshipThing»»`;
- old/pre-magic mana = `«Use«WorshipThing»Magic»`;
- meditation = `«AwakeSleep»`.

These are fossilized historical descriptions. Their present-world membership is supplied by world ontology, not by re-running the literal descriptions.


### Cross-genre ordinary social, emotional, and cognitive roots

A full anti-overfitting pass over _Pride and Prejudice_ and the 1818 _Frankenstein_ found no new grammar gap, but it exposed a clear executable-dictionary imbalance. The following are ordinary productive semantics shared across both corpora:

| Rune | Transliteration | Meaning |
| --- | --- | --- |
|  | Love | Persistent affectionate/loving Relation toward a target. |
|  | Hate | Persistent strong aversive/hostile Relation toward a target. |
|  | Trust | Interpersonal confidence/reliance Relation. |
|  | Respect | Positive-regard Relation acknowledging worth/status/character. |
|  | Admire | Evaluative admiration Relation. |
|  | GratefulTo | Gratitude Relation toward a benefactor. |
|  | CompassionFor | Compassion Relation toward another entity. |
|  | JealousOf | Jealous-attitude Relation. |
|  | Fear | Fear Relation toward an Entity/Event/Proposition/other semantic target. |
|  | GrieveFor | Grief Relation concerning a person/event/state. |
|  | RemorseFor | Remorse Relation concerning an action/event/consequence. |
|  | ShameAbout | Shame Relation concerning an action/property/event/social fact. |
|  | FriendOf | Ordinary friendship Relation. |
|  | ParentOf | Parent-child Relation. |
|  | SpouseOf | Persistent marriage/spousal Relation. |
|  | EngagedTo | Persistent betrothal/engagement Relation. |
|  | Own | Ownership/property-right Relation; exact legal rules belong to world ontology. |
|  | Understand | Comprehension Relation over semantic content. |
|  | Remember | Memory/retention Relation over semantic content. |
|  | ResponsibleFor | Responsibility-attribution Relation; causal/legal/moral grounds remain separately expressible. |
|  | Reputation | Ordered social-standing Attribute, optionally relative to an explicit community/evaluator. |
|  | Consent | Process: explicitly give agreement/consent to a proposed EventSpec. |
|  | Refuse | Process: explicitly decline/reject a proposed/requested EventSpec. |
|  | Forgive | Process: relinquish blame/resentment toward an offender for an offense. |
|  | Deceive | Process: successfully deceive a target concerning proposition content. |
|  | Learn | Process: acquire knowledge/skill/language/rule/other semantic content. |
|  | Happy | Persistent/contextual happiness Property. |
|  | Sad | Persistent/contextual sadness Property. |
|  | Angry | Persistent/contextual anger Property. |

Historically specific institutions such as entailment law, courts, marriage-law validity, social titles, and Frankenstein's physical method for constructing life remain world/history data rather than core semantic atoms.

## How to write Cuspell

### 1. Normal Cuspell is flat prose

Write a sentence as a linear sequence of runes/words. Do **not** expose the semantic tree with parentheses unless the sentence is genuinely ambiguous.

Canonical style:

`More Evaluate MatterSelf Evaluate ThingSelf.`

Not normal prose:

`More Evaluate Self (Cat Self) Evaluate Self (Human Self).`

The second form may still be useful for debugging, teaching the parser, or forcing a difficult boundary, but it is not the player-facing standard.

### 2. Heads come before their arguments

Cuspell uses typed prefix order.

`Move This Here.`

means Move with theme `This` and goal `Here`.

`More A B.`

means A is greater than B on their shared ordered scale.

The type system, not English intuition, decides which frame/roles are legal.

### 3. Tight adjacency makes a local unit

Adjacent rune names with no space may form one tightly bound local expression when their registered roots have exactly one complete typed reading.

Examples:

- `MatterSelf` = `Matter Self`
- `ThingSelf` = `Thing Self`
- `LifeThis` = `Life This`
- `DensityThis` = `Density This`
- `NotLifeThis` = `Not Life This`

This is the normal way to make short language-like local units without writing parentheses.

### 4. Registered lexical compounds still exist

Some adjacency is a lexical compound, not merely tight application.

Examples:

- `SolidWater` = Water restricted to Solid
- `NotLife` = the negated Life property
- `EndLife` = ending the Life state

Resolution order is:

1. an exact registered root label;
2. a licensed registered lexical compound;
3. otherwise, one uniquely typed tight application of the adjacent roots.

If more than one distinct meaning survives, the form is invalid until rewritten.

### 5. Spaces separate larger phrase units

Whitespace is the normal separator between larger words/units:

`More Evaluate MatterSelf Evaluate ThingSelf.`

The spaces themselves do not mean And, Sequence, application, or any other semantic relation. Registered frames and types determine the structure.

### 6. Context may omit an obvious evaluator

`Evaluate Self MatterSelf` explicitly says that Self evaluates the proposition/state `MatterSelf`.

In ordinary contextual prose, `Evaluate MatterSelf` may omit the evaluator and use the current discourse evaluator/context.

That is why:

`More Evaluate MatterSelf Evaluate ThingSelf.`

is the normal first-person/contextual comparison form.

Objective magical logic should make context-dependent information explicit before execution.

### 7. Pipe and parentheses are fallback tools

Pipe hard-binds a complete subexpression:

`Move|This|Here.`

Parentheses hard-group an expression containing spaces:

`If (Life This) (EndLife This).`

Both are legal and zero-mana grammar, but neither is the normal visual style. Prefer:

`Move This Here.`

`If LifeThis EndLifeThis.`

when the flat form has one objective parse.

### 8. Sentence mood

The **final punctuation is also the mood marker**. There is no separate mood symbol at the start.

Assertion:

`MatterSelf.`

Question:

`LifeThis?`

Command:

`Move This Here!`

So `.`, `?`, and `!` all mean both "the sentence ends here" and what kind of sentence it is.

The punctuation costs no mana.

The reference parser temporarily accepts the older transliteration forms `?LifeThis.` and `!Move This Here.` so old tests/documents do not break, but they are no longer canonical Cuspell.

### 9. Named roles

Most arguments are understood from their position and type:

`Move This Here!`

means roughly:

- Move
- theme = This
- goal = Here

But some frames have **optional roles**. If you want to supply one of those roles explicitly, especially while skipping another optional role, write:

`:role Value`

Example:

`Move This Here :source There!`

Here the ordinary arguments say "move This to Here", while `:source There` adds "starting from There".

Another example:

`Move This :path ThisPath!`

This means "move This along ThisPath" without having to invent a positional goal just to reach the path slot.

Named roles also help when nested expressions would otherwise compete for the same trailing argument:

`Permitted You MoveYouHere :authority Self.`

means "You are permitted to move yourself Here, with Self as the authority granting/defining that permission."

The `:source`, `:path`, and `:authority` marks are grammar, not runes, and cost no mana.

### 10. And/Or, Sequence/Concurrent, and real collections

Ordinary conjunction and proposition disjunction are written in spoken order:

`LifeThis And MagicThis.`

`LifeThis Or MagicThis.`

Repeated same-operator chains stay linear:

`LifeThis And MagicThis And WholeThis.`

`LifeThis Or MagicThis Or WholeThis.`

Internally these normalize to the same semantic collection-backed And/Or structures. The older prefix forms may remain parser-compatible, but they are not normal prose style.

Mixed bare And/Or has no hidden precedence. Group it explicitly:

`(LifeThis And MagicThis) Or WholeThis.`

Ordered and concurrent events are written directly after their heads:

`Sequence MoveSelfHere MoveSelfThere!`

`Concurrent MoveSelfHere MoveYouThere!`

If the group runs to the end of the sentence, the final `.`, `?`, or `!` closes it.

If something must follow inside the same sentence, use the zero-mana grammar marker `SequenceEnd` or `ConcurrentEnd`:

`Permitted You Sequence MoveYouHere MoveYouThere SequenceEnd :authority Self.`

`Permitted You Concurrent MoveYouHere MoveYouThere ConcurrentEnd :authority Self.`

A **real Collection value still exists** when the meaning genuinely is "this group of values as one value", for example:

`{This,Self,You}`

Selectors, Count, Filter, Partition, and similar operators may genuinely need such a Collection. The point is only that normal `And` and event `Sequence` no longer force visible braces.

### 11. Binders and variables

A binder means: **"introduce a temporary placeholder ranging over things of this type/Kind."**

Canonical declaration:

`a:«Know«MoveLifeThing»»`

Read that as:

> let `a` stand for an arbitrary Human in this scope.

Reference that placeholder with:

`$a`

Example:

`All a:«Know«MoveLifeThing»» Life $a.`

means:

> for every Human `a`, `a` is alive.

Another example:

`Some c:«LowSize«MoveLifeThing»» At $c Here.`

means:

> there exists at least one Cat `c` that is Here.

Binders are also how Cuspell asks open questions:

`g:Location Intend You Move You $g?`

means approximately:

> which Location `g` is such that You intend to move to `g`?

The brackets from the older form `[a:«Know«MoveLifeThing»»]` are no longer canonical; the parser may keep accepting them for backwards compatibility.

The variable name `a`, `c`, or `g` is temporary grammar. It is not a rune and costs no mana. The semantic domain still carries its normal meaning/cost whether it is a semantic type such as `Location` or a named Kind such as `«Know«MoveLifeThing»»`.

### 12. Numbers

The current exact small-number notation uses `@` repetition:

- `@` = 1
- `@@` = 2
- `@@@` = 3

`Zero` is the registered zero root.

Units turn dimensionless numbers into measured quantities, for example `LengthUnit @@`.

### Migrated ordinary noun Kinds

The following ordinary nouns are no longer primitive roots. They are concepts with provisional Old Names:

- Human = `«Know«MoveLifeThing»»`
- Cat = `«LowSize«MoveLifeThing»»`
- Water = `«LiquidMatter»`
- Body = `«LifeMatter»`
- Hand = `«Grab«LifeMatter»Part»`
- Sound = `«HearingThing»`

They remain fully usable as Kinds through their Names, including as binder domains such as `a:«Know«MoveLifeThing»»`.

### Generic extrema selection

The former special selectors `Nearest`, `Farthest`, `Highest`, and `Lowest` are replaced by two general tie-preserving constructors:

- `MinBy collection binder key`
- `MaxBy collection binder key`

For example:

- nearest to Here: `MinBy C x:Entity Distance $x Here`
- farthest from Here: `MaxBy C x:Entity Distance $x Here`
- lowest Mass: `MinBy C x:Entity Mass $x`
- highest Mass: `MaxBy C x:Entity Mass $x`

Use `Unique` when a singular result is required.

### Measurement units use one root

`Unit` is the single productive measurement-unit root.

The canonical typed units are Old Names rather than separate primitive runes:

- `«ConfidenceUnit»`
- `«HeatUnit»`
- `«LengthUnit»`
- `«LightUnit»`
- `«MassUnit»`
- `«DurationUnit»` for the Time dimension

For example, `«LengthUnit» @@` constructs a Length quantity. The unit's spelling/mana cost comes from the Old Name; its dimensional scale comes from `language/core/units.json`.

### Root minimization status

The dictionary is now under an explicit reduction pass. Eleven exact-redundancy roots were removed in the first batch rather than retained as aliases:

- `After` -> reverse `Before`;
- `Less` -> reverse `More`;
- `AtLeast` / `AtMost` -> comparison + `Or Equal`;
- `EvidenceAgainst` -> `EvidenceFor ... Not ...`;
- `NotDetected A X C` -> `Not Happen Sense A C X`; without an explicit channel, quantify over `SenseChannel`;
- `Never P I` -> `During Not P I`;
- `False` -> `Not True`;
- `Claim` -> `Assert`;
- `Lose` -> `EndHave`;
- `Destroy` -> `EndExist`;

The second batch removes another eleven entries by using the general mechanisms already present:

- `Contain` -> write `In(item, region)` with the actual participant order;
- `Get` -> `BeginHave`;
- `Join` / `Separate` -> `BeginJoined` / `EndJoined`;
- `Tell` -> `Say` with an explicit recipient;
- `See` / `Hear` / `Smell` / `Taste` -> `Sense` + `Vision` / `Hearing` / `Olfaction` / `Gustation`;
- `ChangeBy` -> `Change` to `Add(BeforeValue(...), delta)`;
- `Converse` -> write the underlying Relation directly with its roles in the intended order.


A third exact-wrapper batch removes three more standalone entries:

- `Between V L U` -> `More V L And More U V`;
- `Ask S Q A` -> `Say S Q A` when `Q` is `QuestionContent`;
- `TimeOverlap A B` -> `Overlap A B`, with temporal frames on the general relation.

These removed meanings remain writable compositionally and do not become Old Names.

The direction-family cleanup also removes:

- `AwayFrom X` -> `Opposite Toward X`, after generalizing `Opposite` to typed `Direction` values;
- `DirectPart A B` -> `Part A B` plus `Not Some X` that is a distinct intermediate Part;
- `Former P` -> `And {Before P Now,Not P}`;
- `KnowAnswer M Q` -> `Some i:Information And {Know M $i,AnswerFor $i Q}`;
- `Increasing V I` -> `More ChangeRate V I Zero`;
- `Decreasing V I` -> `More Opposite ChangeRate V I Zero`;
- `ApproxEqual A B T` -> `And {Not More Add A Opposite B T,Not More Add B Opposite A T}`;
- `Sometimes E I` -> `Happen E I`;
- `Members G` -> `Collect x:Entity Member $x G`;
- `Stop E` -> `End E` in EventSpec context;
- `Teach T L C` -> `Cause T Learn L C`;
- `Prefer E A B` -> `More Evaluate E A Evaluate E B`;
- `SiblingOf A B` -> `Some p:Entity And {ParentOf $p A,ParentOf $p B,Not Equal A B}`;
- `Long X` -> `HighLength X`;
- `Hungry X` -> `HighHunger X`;
- `Often E I` -> `High OccurrenceRate E I`;
- `PossibleTo M P` -> `More Confidence M P Zero`;
- `ProbableTo M P` -> `High Confidence M P`;
- `Injured X` -> `HighDamage X`;
- exact `Stable V I` -> `Equal ChangeRate V I Zero`;
- tolerance-bounded `Stable V I T` -> `And {Not More ChangeRate V I T,Not More Opposite ChangeRate V I T}`.
- `Rarely E I` -> `Low OccurrenceRate E I`;
- `Sated X` -> `LowHunger X`;
- `ImportantTo X E` -> `High Evaluate E X`.
- `CertainTo M P` -> `Equal Confidence M P «ConfidenceUnit» @`.
- `Continue E` at the present boundary -> `Prevent End E Interval Now Now` for a resolved concrete Event.
- `Period E` -> `Divide @ OccurrenceRate E` (or use an explicit OccurrenceRate interval).
- `Completed E` -> `Before E Now`; with an explicit reference/scope T, use `Before E T`;
- `Ongoing E T` -> `During E T` for EventSpecs;
- `Big X` -> `HighSize X`;
- `Small X` -> `LowSize X`.
- `Past X` -> `Before X Now` (or `Before X T` for an explicit reference/scope);
- `Future X` -> `Before Now X`;
- `Always P I` -> `During P I`;
- `LocalDensity D R` -> `Density D R`.
- `Height X F` -> `Span X F @`;
- `Width X F` -> `Span X F @@`;
- `Grow X` -> `Change X Size More AfterValue Size X BeforeValue Size X`;
- `Promise S A E` -> `And {Say S CommittedTo S E A A,Begin CommittedTo S E A}`.
- `Same A B` -> `Equal A B` for Entities;
- `Detected A X C` -> `Happen Sense A C X`; channel-omitted detection existentially quantifies a `SenseChannel`;
- `MethodFor M E` -> `Purpose M E`;
- `Using E I` -> `Use E I` (Event/EventSpec instrument-role overload).
- `Present P` for a state -> bare `P`; `Present E` for an EventSpec -> `During E Now`.


The registered base inventory is now **226** entries. After the Habitual/Depth/Thank/Apologize batch, the next four reductions remove `Whenever`, `NextOccurrence`, `Redistribute`, and `Because`: recurring conditionals are `During SufficientFor ...`, next occurrence is the EventSpec overload of `First`, distribution redistribution is `Transfer ... :profile ...`, and ordinary discourse `because` is contextual `Explains reason target`.

See `docs/ROOT_MINIMIZATION_AUDIT.md`.

### 13. Quotation, Old Names, and New Names

Quoted Signs use:

`«Yona»`

Quotation preserves exact sign content rather than running the inside as sentence grammar.

Quoted Signs may nest:

`«Yona's«SharpStick»»`

and punctuation inside them is literal, so `«SharpStick»` and `«Sharp!Stick»` are different Signs.

A **New Name** is an ordinary Name/reference relation. It may identify a person, one particular object, a foreign proper name, or a newly coined term:

`Name «Yona»`

New Names do not become magical macros.

An **Old Name** is historically established pre-magic vocabulary recorded in `language/names/old_names.json`. It has a frozen semantic meaning and may therefore be used directly in a compatible typed position.

For common objects, Old Names should normally be fossilized descriptions built from roots that already existed when the name historically arose, rather than newly invented one-word English labels.

Old Name mana is the cost of its historical name units, not the size of its frozen semantic expansion.

See `docs/spec/NAMES_AND_WORLDBUILDING.md`.

### 14. Ordinary discourse may be contextual

Roots such as `This`, `That`, `They`, `Here`, `Now`, contextual one-argument `Evaluate`, tense/aspect markers, and similar forms may depend on discourse context.

This is allowed for language.

Before a contextual expression becomes an executable magical instruction, its relevant references/values must resolve objectively or the command remains incomplete.

### 15. Meaning is determined by types, not plausibility

If a token sequence has:

- no complete typed reading -> invalid;
- exactly one semantic reading -> valid;
- several surface parses that normalize to the same meaning -> valid;
- several distinct semantic readings -> ambiguous and invalid until rewritten.

The parser never chooses the interpretation that merely “sounds most likely.”

### 16. Canonical visual target

The working visual target is a foreign-language sentence made of runes, not a printed AST.

Transliteration:

`More Evaluate MatterSelf Evaluate ThingSelf.`

Future rune script, schematically:

`カ ロ コヲ ロ マヲ.`

The exact glyphs are undecided. The important standard is the **flat written structure**.


### 17. How large compounds can get

There are two different things that can look like a "big compound".

**A lexical compound** creates a new derived word/Kind/Property from several roots.

Example:

`SolidMagicWater`

can mean Water restricted by both Solid and Magic. It is one written lexical unit built compositionally from three meaning-bearing roots.

**A tight local expression** is not a new dictionary word; it is a whole small expression written without spaces.

Examples:

- `EndLifeSelf` = `End Life Self`
- `MoreDensityThisDensityThat` = `More DensityThis DensityThat`

The second example is semantically "the Density of This is greater than the Density of That", but all five roots can be written as one tight unit because the typed parse is unique.

Cuspell does **not** require maximal compounding. A writer should normally keep spaces between larger thought-units when that is easier to read:

`More DensityThis DensityThat.`

is usually preferable to:

`MoreDensityThisDensityThat.`

Both forms may be valid when they have the same unique typed meaning.

Very long adjacency is rejected if it can produce more than one distinct semantic reading. The language never chooses a convenient interpretation merely because one seems more natural.
