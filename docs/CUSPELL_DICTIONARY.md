# Cuspell Dictionary and Writing Guide

_Status: human-facing reference for the current executable language_

This is the working dictionary for Cuspell.

The **Rune** column is intentionally blank. The Latin/English-looking names in the **Transliteration** column are temporary readable labels for the semantic roots. When the final rune script is designed, its glyphs go in the first column without changing the meanings underneath.

The dictionary currently lists **229 core registered entries plus 6 registered Unit constructors**.

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

Assertion has no prefix:

`CatSelf.`

Question uses `?`:

`?LifeThis.`

Command uses `!`:

`!Move This Here.`

Every complete sentence ends with `.`

Mood marks and the terminator are grammar, not semantic runes.

### 9. Named roles

A named role is written `:role Value` when an optional role must be supplied explicitly or positional reading would be ambiguous.

Example:

`Move This Here :source There.`

Permission authority is intentionally explicit when present:

`Permitted You (Move You Here) :authority Self.`

The role marker itself costs no mana.

### 10. Collections

Finite collections use braces:

`{This,Self,You}`

Items are comma-separated complete expressions.

Example:

`Sequence {Move This Here,EndLifeSelf}.`

### 11. Binders and variables

Typed binder declaration:

`[a:Human]`

Reference to that binder:

`$a`

Example:

`All [a:Human] Life$a.`

Binder punctuation and the variable label are grammar; semantic roots such as Human still count normally.

### 12. Numbers

The current exact small-number notation uses `@` repetition:

- `@` = 1
- `@@` = 2
- `@@@` = 3

`Zero` is the registered zero root.

Units turn dimensionless numbers into measured quantities, for example `LengthUnit @@`.

### 13. Quotation and names

Quoted signs use:

`«Sally»`

A name/reference can be written with `Name`, for example:

`Name «Sally»`

Quotation preserves a Sign rather than executing its semantic content.

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
