# Cuspell Dictionary and Writing Guide

_Status: human-facing reference for the current executable language_

This is the working dictionary for Cuspell.

The **Rune** column is intentionally blank. The Latin/English-looking names in the **Transliteration** column are temporary readable labels for the semantic roots. When the final rune script is designed, its glyphs go in the first column without changing the meanings underneath.

The dictionary currently lists **271 core registered entries plus 6 registered Unit constructors**.

## Dictionary

| Rune | Transliteration | Meaning |
| --- | --- | --- |
|  | About | States that Information is about a semantic topic. |
|  | Add | Adds compatible quantities. |
|  | After | Temporal order: first event/time point is later than the second. |
|  | AfterValue | Value of a semantic value/attribute at the ending boundary of an event. Current written cost: 2 runes. |
|  | All | Universal quantifier over a typed binder. |
|  | Almost | Contextual near-threshold property or near-occurrence/non-completion of an EventSpec. |
|  | Always | States that a proposition holds throughout an explicit interval. |
|  | And | Logical conjunction of propositions or executable conjunction of event specifications where licensed. |
|  | AnswerFor | States that Information is an answer to QuestionContent. |
|  | ApproxEqual | States measured approximate equality with an explicit tolerance. |
|  | Area | Area quantity of a Region. |
|  | Ask | Speech EventSpec embedding QuestionContent. |
|  | Assert | Speech EventSpec asserting a proposition; assertion does not make content objectively true. |
|  | At | Persistent spatial relation: an entity is at a Location. |
|  | AtLeast | States that the first ordered value is greater than or equal to the second. |
|  | AtMost | States that the first ordered value is less than or equal to the second. |
|  | Attempt | EventSpec in which an agent undertakes a real effort aimed at a goal EventSpec; the goal need not succeed. |
|  | AwayFrom | Constructs a Direction away from a reference. |
|  | Ball | Constructs a spherical Region from center and radius. |
|  | Because | Contextual explanatory/reason relation between propositions. |
|  | Before | Temporal order: first event/time point is earlier than the second. |
|  | BeforeValue | Value of a semantic value/attribute at the beginning boundary of an event. Current written cost: 2 runes. |
|  | Begin | Begins a persistent state; also returns an Event's beginning TimePoint. |
|  | Believe | Persistent epistemic state: a mind believes a proposition. |
|  | Beneficiary | Marks an entity as beneficiary of an event. |
|  | Between | Relation: between; roles value, lower, upper; produces Proposition. |
|  | Can | States capability to carry out an EventSpec. |
|  | Cat | Kind: cat. |
|  | Cause | Causal relation between actual Events, or causative EventSpec where an entity causes an event. |
|  | Center | Returns the center Location of a Region. |
|  | CertainTo | Epistemic/modal judgment that a proposition is certain for a mind. |
|  | Change | EventSpec that sets an attribute/family value to a target. |
|  | ChangeBy | EventSpec that changes an attribute by a signed delta. |
|  | ChangeRate | Rate of change of an attribute over time; output dimension is attribute-dimension per Time. |
|  | Claim | Speech EventSpec claiming a proposition; distinct from objective truth. |
|  | Collect | Constructs a collection from a typed binder/predicate. |
|  | CommittedTo | Persistent commitment relation to an EventSpec. |
|  | Completed | States that an event has completed by/within a time/interval. |
|  | Concurrent | Constructs an EventSpec whose component events occur concurrently. |
|  | Confidence | Degree of confidence a mind assigns to a proposition. |
|  | Contain | Persistent relation: a Region contains an entity. |
|  | Continue | EventSpec for continuing an event/process. |
|  | Contrast | Contextual contrast/concession relation; preserves both represented sides. |
|  | Control | Persistent intentional manipulability/control relation. |
|  | Counterfactual | Contextual proposition: in a relevant contrary-to-actual alternative history where the antecedent holds, the consequent holds. |
|  | Converse | Forms a registered converse relation from a reversible relation. |
|  | Count | Returns the nonnegative integer count of members in a collection. |
|  | Decreasing | States that a quantity/value trend decreases over an interval. |
|  | Density | Scalar density attribute of an entity; returns a Density quantity. |
|  | DesignedFor | Persistent design-function relation between an artifact and EventSpec. |
|  | Destroy | EventSpec that ends an entity's existence/integrity rather than specifically ending Life. |
|  | Detected | States that a stimulus was detected by an experiencer, optionally through a channel. |
|  | Directive | Constructs semantic CommandContent from an EventSpec without executing it. |
|  | DirectPart | States that one entity is an immediate/direct part of another. |
|  | Distance | Returns the Length distance between two semantic/spatial values. |
|  | DistributionOf | Constructs a spatial Distribution of a resource over a host. |
|  | Divide | Divides quantities and combines their dimensions. |
|  | Duration | Length of time occupied by an event. |
|  | During | Temporal containment/overlap of an event/time point within an event or interval. |
|  | Each | Applies an EventSpec to each member of a collection. |
|  | Edge | Returns edge Region(s) of an entity/Region. |
|  | End | Ends a persistent state; also returns an Event's ending TimePoint. |
|  | Equal | States exact equality between two values of compatible type. |
|  | Evaluate | Produces an ordered evaluation of a target. Two-argument form names the evaluator; one-argument form uses the discourse evaluator/context. |
|  | EvidenceAgainst | States that Information is evidence against a proposition. |
|  | EvidenceFor | States that Information is evidence supporting a proposition. |
|  | Exist | State property: exists. |
|  | Expect | Relation: expect; roles mind, content; produces StateProposition. |
|  | Explains | States that an Explanation explains a proposition. |
|  | Extent | Returns the occupied/spatial extent Region of an entity. |
|  | False | Boolean/propositional falsehood literal. |
|  | Farthest | Selects member(s) farthest from a reference; ties may remain a collection. |
|  | Filter | Filters a collection by a typed binder/predicate. |
|  | First | Selects the first member of an ordered Sequence. |
|  | Form | Geometric/form profile of an entity. |
|  | Former | States that a state held formerly rather than currently. |
|  | Future | Places an event/state in contextual future discourse time. |
|  | Gas | Matter-phase value/property: gas. |
|  | Generic | Contextual generic/typical statement; not strict universal quantification. |
|  | Get | EventSpec by which a holder comes to Have an entity. |
|  | Give | EventSpec transferring an entity from giver to recipient. |
|  | Group | Kind: a group entity. |
|  | Gustation | Sense channel: taste/gustation. |
|  | Habitual | States that an event is habitual over an optional interval. |
|  | Hand | Kind: hand. |
|  | Happen | States that an EventSpec actually occurs, optionally in an interval. |
|  | Have | Persistent possession/holding relation. |
|  | Hear | Hearing-channel sensing EventSpec. |
|  | Hearing | Sense channel: hearing. |
|  | Heat | Scalar heat attribute of an entity. |
|  | Height | Height relative to an explicit CoordinateFrame. |
|  | Here | Current contextual location. |
|  | Highest | Selects member(s) with the highest scalar attribute value; ties are preserved as a collection. |
|  | Human | Kind: human/person. |
|  | If | Conditional: if the condition holds, the consequent proposition/event follows in the represented structure. |
|  | ImportantTo | States that a target is important to an evaluator. |
|  | In | Persistent spatial relation: an entity is in a Region. |
|  | Increasing | States that a quantity/value trend increases over an interval. |
|  | Infer | EventSpec in which a mind infers a proposition from Information. |
|  | Inside | States that an entity lies inside a Region. |
|  | Intend | States an agent's intention to carry out an EventSpec. |
|  | Interval | Constructs a TimeInterval from start and end TimePoints. |
|  | IntervalFor | Constructs a TimeInterval from a start TimePoint and duration. |
|  | Join | EventSpec that makes two entities Joined. |
|  | Joined | Persistent structural relation: two entities are joined. |
|  | Know | Persistent epistemic state: a mind knows a proposition. |
|  | KnowAnswer | States that a mind knows an answer to QuestionContent. |
|  | Last | Selects the last member of an ordered Sequence. |
|  | Length | Length attribute of an entity/path. |
|  | Less | States that the first ordered value is less than the second. |
|  | Life | State property: alive/living. |
|  | Light | Scalar light attribute of an entity. |
|  | Like | States that an experiencer likes a target. |
|  | Liquid | Matter-phase value/property: liquid. |
|  | LocalDensity | Returns local Density of a Distribution in a Region. |
|  | Lose | EventSpec by which a holder ceases to Have an entity. |
|  | Lowest | Selects member(s) with the lowest scalar attribute value; ties are preserved as a collection. |
|  | Magic | State property: magical. |
|  | Mass | Scalar mass attribute of an entity. |
|  | Matter | Kind: matter/material substance. |
|  | Meaning | Relates a Sign to its semantic Information/propositional meaning. |
|  | Member | States that an entity is a member of a collection. |
|  | Members | Returns the entity members of a Group. |
|  | MethodFor | States that a Method is a method for achieving an EventSpec. |
|  | More | States that the first ordered value is greater than the second. |
|  | Most | Contextual majority/most quantifier over a typed binder. |
|  | Move | EventSpec for moving an entity; magical execution must constrain goal or path. |
|  | Multiply | Multiplies quantities and combines their dimensions. |
|  | Name | Relates a Sign/name to a referent, or resolves a contextual named entity reference. |
|  | Nearest | Selects member(s) nearest to a reference; ties may remain a collection. |
|  | Never | States that a proposition never holds throughout an explicit interval. |
|  | NextOccurrence | Contextual reference to the next occurrence of an event pattern. |
|  | Not | Logical negation of a proposition. |
|  | NotDetected | States that a stimulus was not detected; does not assert objective absence. |
|  | Now | Current contextual time point. |
|  | Obligated | States that an agent is obligated to perform an EventSpec. |
|  | OccurrenceRate | Frequency/occurrence rate of an event pattern over an interval. |
|  | Offset | Constructs a Location by moving a distance from an origin in a Direction. |
|  | Often | States that an event often occurs. |
|  | Olfaction | Sense channel: smell/olfaction. |
|  | Ongoing | States that an event is ongoing at a time/interval. |
|  | Opposite | Numeric opposite/negation of a quantity; also participates in licensed reversible lexical compounds. |
|  | Or | Logical disjunction of propositions. |
|  | Outside | States that an entity lies outside a Region. |
|  | Overlap | States that two entities/regions overlap spatially. |
|  | Part | States that one entity is a part of another. |
|  | Partition | Contextually partitions a collection into fixed-size subcollections. |
|  | Past | Places an event/state in contextual past discourse time. |
|  | Period | Returns the period/duration between recurrences of an event pattern. |
|  | Permitted | States that an agent is permitted to perform an EventSpec; optional explicit authority/context. |
|  | Persist | Actively maintains a state through an interval. |
|  | Phase | Matter phase attribute of an entity. |
|  | Plan | States that an agent has an EventSpec as a plan. |
|  | Plasma | Matter-phase value/property: plasma. |
|  | PossibleTo | Epistemic/modal judgment that a proposition is possible for a mind. |
|  | Power | Raises a quantity to a dimensionless exponent; dimensionful bases require a statically known valid exponent. |
|  | Prefer | States that an experiencer prefers one value/option over another. |
|  | Present | Places an event/state in contextual present discourse time. |
|  | Preserve | Constrains a selected value to remain equal across an event boundary. |
|  | Prevent | Prevents matching future events over an explicit interval/scope. |
|  | ProbableTo | Epistemic/modal judgment that a proposition is probable for a mind. |
|  | Promise | Speech EventSpec committing speaker to a future EventSpec toward an addressee. |
|  | Purpose | Purpose/goal relation for a semantic subject. |
|  | Question | Constructs semantic QuestionContent from a proposition or typed open-question binder. |
|  | Random | Selects one member from a collection. |
|  | Rarely | States that an event rarely occurs. |
|  | Ratio | Constructs a ratio from dimensionless numeric components; distinct from numeric division. |
|  | Redistribute | EventSpec changing a Distribution between source and target Regions. |
|  | Repeat | Repeats an EventSpec a specified number of times, optionally with a period. |
|  | Requires | States that an outcome/event has a prerequisite proposition. |
|  | Root | Takes a quantity root; dimensionful inputs require a statically known degree that leaves integral dimension exponents. |
|  | Same | States that two entity references identify the same entity. |
|  | Say | Speech EventSpec carrying a proposition, Information, or quoted Sign. |
|  | See | Vision-channel sensing EventSpec. |
|  | Self | Current discourse self/speaker/caster reference. |
|  | Sense | Generic sensing EventSpec with explicit sense channel and stimulus. |
|  | Separate | EventSpec that ends a Joined relation. |
|  | Sequence | Constructs an ordered Sequence value, or an EventSpec that executes event specifications in order. |
|  | ShapeLike | States that an entity's form resembles a Kind/template without asserting Kind identity. |
|  | Should | Contextual recommendation/advice for an agent to perform an event; weaker than obligation. |
|  | Sides | Returns side Region(s) of an entity, optionally relative to a frame. |
|  | Simultaneous | States that two events/time points are simultaneous. |
|  | Smell | Olfaction-channel sensing EventSpec. |
|  | Solid | Matter-phase value/property: solid. |
|  | Some | Existential quantifier over a typed binder. |
|  | Sometimes | States that an event sometimes occurs. |
|  | Stable | States that a quantity/value remains stable over an interval, optionally within tolerance. |
|  | Stop | EventSpec that stops an already ongoing Event. |
|  | SufficientFor | States that a condition is sufficient for an outcome/event. |
|  | Surface | Returns the surface Region of an entity. |
|  | Taste | Gustation-channel sensing EventSpec. |
|  | Teleport | EventSpec for discontinuous relocation to a Location. |
|  | Tell | Speech EventSpec transferring Information to an addressee. |
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
|  | TimeOverlap | States that two events/intervals overlap in time. |
|  | TotalAmount | Returns total quantity represented by a Distribution, optionally within a Region. |
|  | Touch | States that two entities are in contact. |
|  | TouchChannel | Sense channel: tactile touch. |
|  | Toward | Constructs a Direction toward a reference. |
|  | Transfer | EventSpec moving a resource/value from source to destination, optionally with an amount. |
|  | Trigger | Creates an EventSpec that fires an action when a condition becomes true within a lifetime/scope. |
|  | True | Boolean/propositional truth literal. |
|  | Tube | Constructs a tubular Region around a Path with a radius. |
|  | UnavailableValueOf | States that a particular attribute value exists but is unavailable/inaccessible. |
|  | Unique | Reduces a collection only when it has exactly one member. |
|  | UnknownValueOf | States that a particular attribute value is unknown. |
|  | Use | EventSpec in which an agent uses an instrument to pursue a goal EventSpec. |
|  | Using | Marks the instrument used by an event. |
|  | Vision | Sense channel: vision. |
|  | Volume | Scalar volume attribute of an entity. |
|  | Want | States that a mind desires an event or proposition. |
|  | Water | Kind: water. |
|  | When | Schedules/locates an EventSpec at a time point or interval. |
|  | Whenever | Contextual recurring conditional relation. |
|  | Whole | Property: structurally whole/intact. |
|  | Width | Width relative to an explicit CoordinateFrame. |
|  | You | Current addressee reference. |
|  | Zero | Exact dimensionless numeric zero. |
|  | ConfidenceUnit | Canonical Confidence Unit constructor: converts a dimensionless number into a Quantity:Confidence at scale 1/1. |
|  | HeatUnit | Canonical Heat Unit constructor: converts a dimensionless number into a Quantity:Heat at scale 1/1. |
|  | LengthUnit | Canonical Length Unit constructor: converts a dimensionless number into a Quantity:Length at scale 1/1. |
|  | LightUnit | Canonical Light Unit constructor: converts a dimensionless number into a Quantity:Light at scale 1/1. |
|  | MassUnit | Canonical Mass Unit constructor: converts a dimensionless number into a Quantity:Mass at scale 1/1. |
|  | TimeUnit | Canonical Time Unit constructor: converts a dimensionless number into a Quantity:Time at scale 1/1. |

### Foundational roots added in the first civilization vocabulary pass

These are productive semantic/descriptive roots, not English object nouns. Common objects such as Ship, House, Sword, Book, and Market are registered as descriptive Old Names instead; see `docs/world/FIRST_CIVILIZATION_VOCABULARY.md`.

| Rune | Transliteration | Meaning |
| --- | --- | --- |
|  | Big | Contextual Property: size/extent above the relevant comparison standard. Direct magical use must make the standard objective. |
|  | Small | Contextual Property: size/extent below the relevant comparison standard. Direct magical use must make the standard objective. |
|  | Hard | Contextual material/structural hardness Property. |
|  | Sharp | Contextual edge/point sharpness Property. |
|  | Grow | Contextual growth/development Process. |
|  | Sleep | Persistent contextual sleep-state Property. |
|  | Sign | General Sign Kind used by the information/language system. |
|  | Information | General informational Kind/domain. |
|  | Rule | General rule/instruction Kind. |
|  | Region | General spatial Region Kind. |
|  | Path | General ordered route/path Kind. |
|  | Write | Process in which an agent produces/writes a Sign. |
|  | Read | Process in which an agent reads/interprets a Sign. |

### Ordinary roots added by the audited Yona vocabulary pass

These are productive ordinary-language roots exposed repeatedly by Chapters 1–14 + 47. Yona-specific proper/System terms remain New Names in the optional `world/yona` package.

| Rune | Transliteration | Meaning |
| --- | --- | --- |
|  | Body | General body Kind/domain. |
|  | Long | Contextual Property: length above the relevant comparison standard. |
|  | Awake | Persistent wakefulness state Property. |
|  | Open | Contextual persistent open-state Property relative to an object's closure/design. |
|  | Locked | Persistent locked/sealed-by-lock state Property. |
|  | Eat | Process: an agent consumes an entity as food. |
|  | Attack | Process: an agent attacks a target. |
|  | Grab | Process: an agent grabs a target. |
|  | Bite | Process: an agent bites a target. |
|  | Climb | Process: an agent climbs a target/entity. |
|  | Fall | Process: an entity falls. |
|  | Jump | Contextual jumping Process; a goal Location may be supplied. |
|  | Stab | Process: an agent stabs a target, optionally with an instrument. |
|  | Limp | Process: an agent moves with a limp. |
|  | Sever | Process: an agent severs a target, optionally with an instrument. |

### Residual ordinary roots from the Chapters 1–14 + 47 cleanup

These close the remaining ordinary combat, injury, graded-body-state, texture/camouflage, reflexive-action, and sound/intensity buckets identified by the audited corpus.

| Rune | Transliteration | Meaning |
| --- | --- | --- |
|  | Damage | Ordered physical-damage/injury degree Attribute. |
|  | Depth | Contextual Length-valued depth/penetration Attribute; an explicit frame/reference surface removes ambiguity. |
|  | Hunger | Ordered hunger-degree Attribute. |
|  | TextureOf | TextureProfile Attribute of an Entity. |
|  | Loudness | Ordered sound-loudness Attribute; objective measurement belongs to the world package. |
|  | Sound | General acoustic-phenomenon Kind/domain. |
|  | Injured | Persistent physical-injury state Property. |
|  | Hungry | Contextual hunger-threshold state Property. |
|  | Sated | Contextual satiated/full-enough state Property; not defined as the logical Opposite of Hungry. |
|  | Dodge | Contextual evasive Process by an agent, optionally relative to a threat EventSpec. |
|  | Reflexive | States that an EventSpec occurs as an involuntary/reflex response. |
|  | CamouflagedAgainst | Contextual state Relation between a subject and background, optionally relative to an observer. |

Concrete anatomy nouns exposed by the same pass remain Old Names/world concepts rather than primitive roots: organ, stomach, wrist, tendon, and wound.

## How to write Cuspell

### 1. Normal Cuspell is flat prose

Write a sentence as a linear sequence of runes/words. Do **not** expose the semantic tree with parentheses unless the sentence is genuinely ambiguous.

Canonical style:

`More Evaluate CatSelf Evaluate HumanSelf.`

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

- `CatSelf` = `Cat Self`
- `HumanSelf` = `Human Self`
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

`More Evaluate CatSelf Evaluate HumanSelf.`

The spaces themselves do not mean And, Sequence, application, or any other semantic relation. Registered frames and types determine the structure.

### 6. Context may omit an obvious evaluator

`Evaluate Self CatSelf` explicitly says that Self evaluates the proposition/state `CatSelf`.

In ordinary contextual prose, `Evaluate CatSelf` may omit the evaluator and use the current discourse evaluator/context.

That is why:

`More Evaluate CatSelf Evaluate HumanSelf.`

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

`CatSelf.`

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

`a:Human`

Read that as:

> let `a` stand for an arbitrary Human in this scope.

Reference that placeholder with:

`$a`

Example:

`All a:Human Life $a.`

means:

> for every Human `a`, `a` is alive.

Another example:

`Some c:Cat At $c Here.`

means:

> there exists at least one Cat `c` that is Here.

Binders are also how Cuspell asks open questions:

`g:Location Intend You Move You $g?`

means approximately:

> which Location `g` is such that You intend to move to `g`?

The brackets from the older form `[a:Human]` are no longer canonical; the parser may keep accepting them for backwards compatibility.

The variable name `a`, `c`, or `g` is temporary grammar. It is not a rune and costs no mana. The semantic domain such as `Human`, `Cat`, or `Location` still carries its normal meaning/cost.

### 12. Numbers

The current exact small-number notation uses `@` repetition:

- `@` = 1
- `@@` = 2
- `@@@` = 3

`Zero` is the registered zero root.

Units turn dimensionless numbers into measured quantities, for example `LengthUnit @@`.

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

`More Evaluate CatSelf Evaluate HumanSelf.`

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
