# Cuspell Dictionary and Writing Guide

_Status: human-facing reference for the current executable language_

This is the working dictionary for Cuspell.

The **Rune** column is intentionally blank. The Latin/English-looking names in the **Transliteration** column are temporary readable labels for the semantic roots. When the final rune script is designed, its glyphs go in the first column without changing the meanings underneath.

The dictionary currently lists **212 core registered base entries**. Typed measurement units are Old Names built from the single `Unit` root, so they do not add separate primitive rune entries.

## Dictionary

| Rune | Transliteration | Meaning |
| --- | --- | --- |
|  | About | States that Information is about a semantic topic. |
|  | Add | Adds compatible quantities. |
|  | AfterValue | Value of a semantic value/attribute at the ending boundary of an event. Current written cost: 2 runes. |
|  | All | Universal quantifier over a typed binder. |
|  | Almost | Contextual near-satisfaction/near-occurrence operator: the target does not yet hold/occur but is close under a domain-specific criterion. |
|  | And | Logical conjunction of propositions or executable conjunction of event specifications where licensed. |
|  | AnswerFor | States that Information is an answer to QuestionContent. |
|  | Area | Area quantity of a Region. |
|  | Assert | Speech EventSpec asserting a proposition; assertion does not make content objectively true. |
|  | At | Persistent spatial relation: an entity is at a Location; `End At source` + `Begin At goal` expresses discontinuous relocation without a Move Path. |
|  | Attempt | EventSpec in which an agent undertakes a real effort aimed at a goal EventSpec; the goal need not succeed. |
|  | Authority | Persistent recognized normative standing/competence over a supplied scope; distinct from physical Control, capability, and permission for a particular EventSpec. |
|  | Ball | Constructs a spherical Region from center and radius. |
|  | Before | Temporal order: first event/time point is earlier than the second. |
|  | BeforeValue | Value of a semantic value/attribute at the beginning boundary of an event. Current written cost: 2 runes. |
|  | Begin | Begins a persistent state; also returns the beginning TimePoint of an Event or TimeInterval. |
|  | Believe | Persistent epistemic state: a mind believes a proposition. |
|  | Beneficiary | Marks an entity as beneficiary of an Event/EventSpec; distinct from recipient, transfer, possession, or intended Purpose. |
|  | Can | Persistent capability state for carrying out an EventSpec; `Begin Can ...` expresses skill acquisition. |
|  | Cause | Causal relation between actual Events, or causative EventSpec where an entity causes an EventSpec/state; an optional third Entity records the instrument. |
|  | Center | Returns the center Location of a Region. |
|  | Change | EventSpec that sets an attribute/family value to a target. |
|  | Rate | General per-time rate: Quantity-over-Time for a Quantity, or occurrence frequency for an EventSpec. |
|  | Collect | Typed set comprehension: collects values from a binder's declared domain that satisfy an optional predicate; the collection preserves the binder type. |
|  | Concurrent | Constructs an EventSpec whose component events occur concurrently. |
|  | Confidence | Degree of confidence a mind assigns to a proposition. |
|  | Contrast | Contextual discourse contrast/concession relation; unlike plain And, it also marks tension or expectation mismatch between the represented sides. |
|  | Control | Persistent control/manipulability relation; concurrent `Begin Touch` + `Begin Control` expresses grabbing/taking hold. |
|  | Counterfactual | Contextual proposition: in a relevant contrary-to-actual alternative history where the antecedent holds, the consequent holds. |
|  | Count | Returns the nonnegative integer count of members in a collection. |
|  | Density | Scalar density attribute of an entity; returns a Density quantity. |
|  | Directive | Constructs semantic CommandContent from an EventSpec without executing it. |
|  | Distance | Physical/spatial separation between SpatialValues such as Entities, Locations, and Regions; returns Length. |
|  | DistributionOf | Constructs a spatial Distribution of a resource over a host. |
|  | Divide | Divides quantities and combines their dimensions. |
|  | During | Temporal containment/holding of events, points, EventSpecs, or propositions over an explicit interval/reference. |
|  | Each | Applies an EventSpec to each member of a collection. |
|  | Edge | Returns edge Region(s) of an entity/Region. |
|  | End | Ends a persistent state; returns the ending TimePoint of an Event or TimeInterval; or stops an ongoing Event when EventSpec is expected. |
|  | Equal | States exact equality between two values of compatible type. |
|  | Evaluate | Produces an ordered evaluation of a target. Two-argument form names the evaluator; one-argument form uses the discourse evaluator/context. |
|  | EvidenceFor | States that Information is evidence supporting a proposition. |
|  | Exist | Existence state over entities and semantic values such as Sign tokens; `Cause A Begin Exist S` expresses agentive creation of S. |
|  | Expect | Relation: expect; roles mind, content; produces StateProposition. |
|  | Explains | States that an Explanation explains a proposition; a contextual Proposition+Proposition frame covers ordinary discourse explanation (`target because reason`). |
|  | Extent | General extent family: occupied Region, contextual holistic extent/size EvaluationValue, axis-indexed projected Length, or temporal extent of an Event/TimeInterval. |
|  | Filter | Filters a collection by a typed binder/predicate. |
|  | First | Selects the first member of an ordered Sequence; with an EventSpec it contextually denotes the next/first matching occurrence. |
|  | Form | Geometric/form profile of an entity. |
|  | Gas | Matter-phase value/property: gas. |
|  | Group | Kind: a group entity. |
|  | Gustation | Sense channel: taste/gustation. |
|  | Happen | States that an EventSpec actually occurs, optionally in an interval. |
|  | High | Contextual above-standard predicate over ordered EvaluationValue, Quantity, or Ratio values; with an AttributeDescriptor it forms a first-class threshold Property. |
|  | Low | Contextual below-standard predicate; with an AttributeDescriptor it forms a first-class threshold Property such as LowHunger. It is not equivalent to Not High. |
|  | Have | Persistent possession/holding relation. |
|  | Hearing | Sense channel: hearing. |
|  | Heat | Scalar heat attribute of an entity. |
|  | Here | Current contextual location. |
|  | If | Conditional: if the condition holds, the consequent proposition/event follows in the represented structure. |
|  | In | Persistent spatial relation: an entity is in a Region. |
|  | Infer | EventSpec in which a mind infers a proposition from Information. |
|  | Intend | States an agent's intention to carry out an EventSpec. |
|  | Interval | Constructs a TimeInterval from start and end TimePoints. |
|  | IntervalFor | Constructs a TimeInterval from a start TimePoint and duration. |
|  | Joined | Persistent structural relation: two entities are joined. |
|  | Know | Persistent epistemic state: a mind knows a proposition. |
|  | Last | Selects the last member of an ordered Sequence. |
|  | Length | Length attribute of an entity/path. |
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
|  | Name | Context-sensitive naming Relation between a Sign and a semantic referent; inverse lookup uses typed `Collect` + `Unique`, not a special Name frame. |
|  | Not | Logical negation of a proposition. |
|  | Now | Current contextual time point. |
|  | Obligated | Persistent deontic/social responsibility for an EventSpec; an optional third value identifies its social/institutional/interpersonal context. |
|  | Offset | Constructs a Location by moving a distance from an origin in a Direction. |
|  | Olfaction | Sense channel: smell/olfaction. |
|  | Opposite | Numeric opposite/negation of a quantity; also participates in licensed reversible lexical compounds. |
|  | Or | Logical disjunction of propositions. |
|  | Overlap | General typed overlap relation; Region/Region overlap means nontrivial shared interior extent and composes strict outside. |
|  | Part | States that one entity is a part of another. |
|  | Partition | Contextually partitions a collection into fixed-size subcollections. |
|  | Permitted | Permission relation: agent+EventSpec states performer permission; EventSpec+Entity states that the event itself is permitted/consented to by that source. Particular permission/consent does not itself assert broad Authority. |
|  | Persist | Actively maintains a state through an interval. |
|  | Phase | Matter phase attribute of an entity. |
|  | Plan | States that an agent has an EventSpec as a plan. |
|  | Plasma | Matter-phase value/property: plasma. |
|  | Power | Raises a quantity to a dimensionless exponent; dimensionful bases require a statically known valid exponent. |
|  | Preserve | Constrains a selected value to remain equal across an event boundary. |
|  | Prevent | Prevents matching future events over an explicit interval/scope. |
|  | Purpose | Persistent intended goal/function relation for a semantic subject, including artifact designed function; temporary Use does not establish it. |
|  | Question | Constructs semantic QuestionContent from a proposition or typed open-question binder. |
|  | Random | Selects one member from a collection. |
|  | Ratio | Constructs a ratio from dimensionless numeric components; distinct from numeric division. |
|  | Repeat | Repeats an EventSpec a specified number of times, optionally with a period. |
|  | Requires | States that an outcome/event has a prerequisite proposition. |
|  | Root | Takes a quantity root; dimensionful inputs require a statically known degree that leaves integral dimension exponents. |
|  | Rotate | Rigidly rotates an Entity about an explicit pivot + oriented axis by a signed number of full turns; distinct from translational Move and intrinsic Form change. |
|  | Say | Speech EventSpec carrying a proposition, Information, or quoted Sign. |
|  | Self | Current discourse self/speaker/caster reference. |
|  | Sense | Generic sensory-acquisition EventSpec with an explicit SenseChannel; Sense does not itself entail semantic interpretation. |
|  | Sequence | Constructs an ordered Sequence value, or an EventSpec that executes event specifications in order. |
|  | ShapeLike | States that an entity's form resembles a Kind/template without asserting Kind identity. |
|  | Sides | Returns side Region(s) of an entity, optionally relative to a frame. |
|  | Simultaneous | States that two events/time points are simultaneous. |
|  | Solid | Matter-phase value/property: solid. |
|  | Some | Existential quantifier over a typed binder. |
|  | SufficientFor | States that a condition is sufficient for an outcome/event. |
|  | Surface | Returns the surface Region of an entity. |
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
|  | Touch | Persistent contact-state relation between two entities. |
|  | TouchChannel | Sense channel: tactile touch. |
|  | Toward | Constructs a Direction toward a reference. |
|  | Transfer | EventSpec moving a resource/value from source to destination, optionally with an amount; Distribution transfers may add an optional destination profile after amount. |
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
|  | Whole | Persistent structural integrity/completeness state; `End Whole X` expresses loss of wholeness. |
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

### Ordinary roots added by the audited Yona vocabulary pass

These are productive ordinary-language roots exposed repeatedly by Chapters 1–14 + 47. `Body` has since been migrated to the Old Name `«LifeMatter»`; Yona-specific proper/System terms remain New Names in the optional `world/yona` package.

| Rune | Transliteration | Meaning |
| --- | --- | --- |
|  | Awake | Persistent wakefulness state Property. |
|  | Open | Contextual persistent open-state Property relative to an object's closure/design. |
|  | Locked | Persistent locked/sealed-by-lock state Property. |
|  | Eat | Process: an agent consumes an entity as food. |
|  | Attack | Process: an agent attacks a target. |
|  | Bite | Process: an agent bites a target; oral biting manner is not identical to generic Attack, Eat, Touch, or Damage. |
|  | Climb | Process: an agent climbs a target/entity; climbing manner is not merely upward Move and can include down/across/over traversal. |
|  | Fall | Process: an entity undergoes non-agentive, context/gravity-governed falling motion. |
|  | Female | Positive biological-sex classification Property; not defined as Not Male. Exact membership belongs to world ontology. |
|  | Male | Positive biological-sex classification Property; not defined as Not Female. Exact membership belongs to world ontology. |
|  | Jump | Contextual launch/airborne locomotion Process; a goal Location may be supplied. Generic Move does not encode the jumping manner. |
|  | Stab | Directed puncturing/thrust Process against a target, optionally with an instrument; not equivalent to generic Attack, Damage, Touch, or Use. |
|  | Limp | Locomotion Process with an asymmetric/impaired gait; does not by itself assert a particular Damage level or cause. |

### Residual ordinary roots from the Chapters 1–14 + 47 cleanup

These close the remaining ordinary combat, injury, graded-body-state, texture/camouflage, reflexive-action, and sound/intensity buckets identified by the audited corpus. `Sound` has since been migrated to the Old Name `«HearingThing»`.

| Rune | Transliteration | Meaning |
| --- | --- | --- |
|  | Damage | Ordered physical-damage/injury degree Attribute. |
|  | Health | Ordered overall biological functional-condition Attribute; distinct from Damage and Ill. |
|  | Hunger | Ordered hunger-degree Attribute. |
|  | Pain | Ordered experienced pain/nociceptive-suffering Attribute; distinct from physical Damage. |
|  | Ill | Persistent pathological/illness-state Property; distinct from Damage, Pain, Low Health, and Not Life. |
|  | TextureOf | TextureProfile Attribute of an Entity. |
|  | Loudness | Ordered sound-loudness Attribute; objective measurement belongs to the world package. |
|  | Dodge | Contextual evasive Process intended to avoid a threat; it need not prevent the threatening event itself. |
|  | Reflexive | States that an EventSpec occurs as an involuntary/reflex response; absence of conscious intention alone is not equivalent. |
|  | CamouflagedAgainst | Contextual observer/background-sensitive camouflage state; concrete ColorOf/TextureOf values alone do not define the full relation. |

Concrete anatomy nouns remain Old Names/world concepts rather than primitive roots. The current common layer includes body, hand, eye, ear, mouth, skin, bone, flesh, blood, organ, stomach, wrist, tendon, wound, head, face, arm, leg, foot, finger, nose, tooth, tongue, heart, brain, and hair.

Natural geography/weather vocabulary follows the same rule. Land, soil, sand, river, lake, sea/ocean, mountain, hill, island, shore/coast, forest, sky, cloud, rain, ice, snow, wind, and storm are world concepts + Old Names, not productive semantic roots. Exact geography/meteorology belongs to world classifiers and execution physics.

Food/agriculture/material vocabulary also stays primarily in the world/Old-Name layer. Field, seed, leaf, fruit, crop/cultivated plant, grain, milk, egg, salt, clay, cloth/textile, leather/hide, glass, and fuel are world concepts + Old Names. `Staple food` remains culture-relative world/history vocabulary rather than one universal core Kind; specific crop species, recipes, oils, spices, beverages, and similar material/food distinctions are likewise world-package concerns unless later pressure proves otherwise.

Craft/manufacturing/transport vocabulary likewise uses world concepts + Old Names for knife, axe, saw, pot, needle, wheel, cart/wagon, plow, loom, furnace/kiln, anvil, sail, oar, anchor, port, building, roof, room, floor, workshop, mill, and fortification. This batch adds one productive spatial Process, `Rotate`, because actual rigid turning cannot be expressed exactly by the existing translation/Form machinery.

War/public-institution vocabulary uses world concepts + Old Names for soldier, army, armor, shield, spear, bow, arrow, prison, prisoner, judge, polity/state, government, and citizen/member of polity. This batch adds the productive social Relation `Authority`. Checkpoint 118 re-audits that addition and retains it because recognized standing over a scope is not determined by particular permissions, obligations, capability, control, rules, or causation.

Art/ritual/shared-culture vocabulary uses world concepts + Old Names for temple, shrine, priest, ritual/ceremony, prayer, sacrifice/offering, dance, performance, game/sport, festival/feast, story/tale, music/composition, song, musical instrument, image/painting, and sculpture. Registered world Kind concepts now support explicit `classifies_types`: existing concepts default to Entity, event categories classify EventSpec/Event, and story/music/song classify Information. No new rune is required for that generalization.

Calendar/daily-life vocabulary uses world concepts + Old Names for day/calendar day, night, season, year, month/calendar month, and date/calendar date. The first five classify TimeInterval; Date classifies Information. They are calendar/reference categories rather than hidden fixed time units. `Age` remains compositional as `Extent Interval start reference`, with the relevant birth/creation/start point supplied explicitly by world/reference data.


### Historical roots and Old Names from the final deferred-vocabulary pass

Two broadly reusable ordinary roots close the religious/social construction needs:

| Rune | Transliteration | Meaning |
| --- | --- | --- |
|  | Female | Positive persistent biological-sex classification Property; not a universal social-gender category. Exact objective membership belongs to world ontology. |
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
|  | Forgive | Process: relinquish blame/resentment toward an offender for an offense without necessarily denying responsibility or erasing memory/other emotions. |
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

### 7. Parentheses are the explicit grouping fallback

Normal Cuspell should stay flat. Tight adjacency is the preferred way to bind a short local expression:

`MoveYouHere`

Parentheses remain available when a larger spaced expression must be forced into one argument:

`If (Life This) (EndLife This).`

Parentheses are legal zero-mana grammar, but should be uncommon when flat typing or tight adjacency already gives one objective parse.

Pipe hard-binding is retained by the reference parser only for debugging and historical compatibility. It is not player-facing Cuspell and should not appear in new canonical examples.

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

### 9. Optional arguments and omission

Frame arguments are positional.

Trailing optional arguments may simply be absent. To skip an optional position and supply a later one, write `_` for each skipped slot.

`Move This Here There!`

supplies goal `Here` and source `There`.

`Move This _ _ ThisPath!`

omits goal and source and then supplies path.

`Transfer DistributionOf This Self ThisRegion ThisRegion _ DistributionOf You Self!`

omits the optional amount and supplies the destination Distribution profile.

For a broad optional tail inside a larger expression, `_` can explicitly close the omission:

`Say Self Obligated Self MoveSelfHere _ You!`

Internal frame names such as source, path, authority, and context are maintainer metadata, not Cuspell vocabulary. The omission marker costs no mana because it carries no role identity.

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

`Permitted You Sequence MoveYouHere MoveYouThere SequenceEnd Self.`

`Permitted You Concurrent MoveYouHere MoveYouThere ConcurrentEnd Self.`

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

`Some c:«LowExtent«MoveLifeThing»» At $c Here.`

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
- Cat = `«LowExtent«MoveLifeThing»»`
- Water = `«LiquidMatter»`
- Body = `«LifeMatter»`
- Hand = `«Control«LifeMatter»Part»`
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

### Current inventory status

The current base registry contains **212 entries**:

- **131 semantic primitive candidates**;
- **55 formal constructors**;
- **16 reference forms**;
- **10 domain values**;
- **0 unresolved candidates**;
- **0 derived candidates**.

The current 131-root semantic primitive basis is **reduction-closed for now**, not permanently frozen. Checkpoint 105 intentionally restores `Almost` as a formal constructor because the attempted `Low Distance ...` reduction required an undefined hidden metric over propositions/events. Checkpoint 107 adds `Health`, `Pain`, and `Ill` after the civilization audit showed that physical Damage and Life state do not preserve those independent biological/experienced distinctions. Checkpoint 119 re-tests those three against the later generic Attribute, `Evaluate`, `Sense`, world-Kind, and Old-Name machinery and retains them: those mechanisms can operate on or classify an identified meaning but do not reconstruct the Health/Pain dimensions or persistent Ill state. Checkpoint 108 adds positive `Male` alongside `Female` because negation cannot supply the converse biological classification. Checkpoint 120 re-tests the pair against a Sex attribute/value family and typed world-Kind migration and retains both Properties: the attribute model adds/overconstrains a universal functional axis, while current world-Kind predication would lose their persistent StateProposition/Begin/End semantics. Checkpoint 114 adds `Rotate` because rigid orientation change is not exactly reducible to translational `Move` or `Change Form`. Checkpoint 115 adds `Authority` because recognized legitimate/institutional standing is not equivalent to physical `Control`, permission, ownership, or causation. Checkpoint 118 re-runs that exact reduction test against the stabilized deontic/capability machinery and retains `Authority`: two worlds can match on current permissions, obligations, rules, control, and capabilities while differing on whose later decision is recognized as binding. Further deletion or addition remains evidence-triggered and must preserve complete meaning, typing, and execution closure.

Removed convenience meanings remain available through the general mechanisms described elsewhere in this guide. Representative examples include:

- temporal “after” by reversing `Before`;
- comparative “less” by reversing `More`;
- acquisition/loss through `Begin Have` / `End Have`;
- joining/separation through `Begin Joined` / `End Joined`;
- sense-specific seeing/hearing/etc. through `Sense` + a `SenseChannel`;
- duration through temporal `Extent(Event)`;
- inside/outside through Region topology composition;
- giving transparently through `Concurrent EndHave giver theme BeginHave recipient theme`, with the historical parameterized Old Name `«TransferHave» giver theme recipient` available as frozen lexical compression;
- learning through `Begin Know`, `Begin Can`, or `Begin Understand`.

The complete reduction history and rationale are preserved under `archive/audits/`; they are not part of the current writing rules a learner must memorize.

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

A frozen expression Old Name may also have **required typed parameters** when the historical word is already an exact composition. Arguments follow the quoted Old Name in registered order and pay their normal written mana cost.

Example:

`«TransferHave» Self This You!`

is the historical **give** word and expands to the same event meaning as:

`Concurrent EndHave Self This BeginHave You This!`

The mechanism cannot invent missing semantics: an approximate definition of words such as Dance, Cook, Read, Teach, or generic Heal may not be hidden inside an Old Name merely to make it look lexicalized.

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
