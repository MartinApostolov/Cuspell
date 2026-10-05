# Player Rune Dictionary

_Status: player-facing index generated from the current internal dictionary at checkpoint 132_

This file lists the **216 registered Cuspell signs** using their temporary Latin transliterations. The final rune glyphs are not designed yet.

For designer/maintainer detail, frames, historical rationale, and reduction notes, use `docs/CUSPELL_DICTIONARY.md`. Players normally only need the meanings below.

| Rune | Meaning |
| --- | --- |
| `About` | States that Information is about a semantic topic. |
| `Add` | Adds compatible quantities. |
| `Admire` | Evaluative admiration Relation. |
| `AfterValue` | Value of a semantic value/attribute at the ending boundary of an event. Current written cost: 2 runes. |
| `All` | Universal quantifier over a typed binder. |
| `Almost` | Contextual near-satisfaction/near-occurrence operator. The target does not yet hold/occur but is close under a domain-specific criterion; contextual Almost is not magically executable until that criterion is objective. |
| `And` | Logical conjunction of propositions or executable conjunction of event specifications where licensed. |
| `Angry` | Persistent/contextual anger Property. |
| `AnswerFor` | States that Information is an answer to QuestionContent. |
| `Area` | Area quantity of a Region. |
| `Assert` | Speech EventSpec asserting a proposition; assertion does not make content objectively true. |
| `At` | Persistent spatial relation: an entity is at a Location; `End At source` + `Begin At goal` expresses discontinuous relocation without a Move Path. |
| `Attack` | Process: an agent attacks a target. |
| `Attempt` | EventSpec in which an agent undertakes a real effort aimed at a goal EventSpec; the goal need not succeed. |
| `Authority` | Persistent recognized normative standing/competence over a supplied scope; distinct from physical Control, capability, or permission for a particular EventSpec. |
| `Awake` | Persistent wakefulness state Property. |
| `Ball` | Constructs a spherical Region from center and radius. |
| `Before` | Temporal order: first event/time point is earlier than the second. |
| `BeforeValue` | Value of a semantic value/attribute at the beginning boundary of an event. Current written cost: 2 runes. |
| `Begin` | Begins a persistent state; also returns the beginning TimePoint of an Event or TimeInterval. |
| `Believe` | Persistent epistemic state: a mind believes a proposition. |
| `Beneficiary` | Marks an entity as beneficiary of an Event/EventSpec; distinct from recipient, transfer, possession, or intended Purpose. |
| `Bite` | Process: an agent bites a target; oral biting manner is not identical to generic Attack, Eat, Touch, or Damage. |
| `CamouflagedAgainst` | Contextual observer/background-sensitive camouflage state; concrete ColorOf/TextureOf values alone do not define the full relation. |
| `Can` | Persistent capability state for carrying out an EventSpec; `Begin Can ...` expresses skill acquisition. |
| `Cause` | Causal relation between actual Events, or causative EventSpec where an entity causes an EventSpec/state; an optional third Entity records the instrument. |
| `Center` | Returns the center Location of a Region. |
| `Change` | EventSpec that sets an attribute/family value to a target. |
| `Climb` | Process: an agent climbs a target/entity; climbing manner is not merely upward Move and can include down/across/over traversal. |
| `Collect` | Collects values from a typed binder domain that satisfy an optional predicate; the result keeps that value type. |
| `CompassionFor` | Compassion Relation toward another entity. |
| `Concurrent` | Constructs an EventSpec whose component events occur concurrently. |
| `Confidence` | Degree of confidence a mind assigns to a proposition. |
| `Contrast` | Contextual discourse contrast/concession relation; unlike plain And, it also marks tension or expectation mismatch between the represented sides. |
| `Control` | Persistent control/manipulability relation; concurrent `Begin Touch` + `Begin Control` expresses grabbing/taking hold. |
| `Create` | Allocates exactly one fresh Entity identity and binds it into an objective post-creation profile; an optional continuation may immediately use that fresh result in the same command. Distinct from reactivating an existing identity with `Begin Exist`. |
| `Count` | Returns the nonnegative integer count of members in a collection. |
| `Counterfactual` | Contextual proposition: in a relevant contrary-to-actual alternative history where the antecedent holds, the consequent holds. |
| `Damage` | Ordered physical-damage/injury degree Attribute. |
| `Density` | Scalar density attribute of an entity; returns a Density quantity. |
| `Directive` | Constructs semantic CommandContent from an EventSpec without executing it. |
| `Distance` | Physical/spatial separation between SpatialValues such as Entities, Locations, and Regions; returns Length. |
| `DistributionOf` | Constructs a spatial Distribution of a resource over a host. |
| `Divide` | Divides quantities and combines their dimensions. |
| `Dodge` | Contextual evasive Process intended to avoid a threat; it need not prevent the threatening event itself. |
| `During` | Temporal containment/holding of events, points, EventSpecs, or propositions over an explicit interval/reference. |
| `Each` | Applies an EventSpec to each member of a collection. |
| `Eat` | Process: an agent consumes an entity as food. |
| `Edge` | Returns edge Region(s) of an entity/Region. |
| `End` | Ends a persistent state; also returns an Event's ending TimePoint. |
| `EngagedTo` | Persistent betrothal/engagement Relation. |
| `Equal` | States exact equality between two values of compatible type. |
| `Evaluate` | Produces an ordered evaluation of a target. Two-argument form names the evaluator; one-argument form uses the discourse evaluator/context. |
| `EvidenceFor` | States that Information is evidence supporting a proposition. |
| `Exist` | Existence state over entities and semantic values such as Sign tokens; `Cause A Begin Exist S` expresses agentive creation of S. |
| `Expect` | Relation: expect; roles mind, content; produces StateProposition. |
| `Explains` | States that an Explanation explains a proposition; a contextual Proposition+Proposition frame covers ordinary discourse explanation (`target because reason`). |
| `Extent` | General extent family: occupied Region, contextual holistic extent/size, axis-indexed projected Length, or temporal extent of an Event/TimeInterval. |
| `Fall` | Process: an entity undergoes non-agentive, context/gravity-governed falling motion. |
| `Fear` | Fear Relation toward an Entity/Event/Proposition/other semantic target. |
| `Female` | Positive biological-sex classification Property; not defined as Not Male. Exact membership belongs to world ontology. |
| `Filter` | Filters a collection by a typed binder/predicate. |
| `Find` | Bounded factive information-acquisition Process: gives a mind the truthful yes/no or open-query answer within an explicit information-access scope. The scope must be part of the query; blocked/incomplete access is failure, not an empty answer. |
| `First` | Selects the first member of an ordered Sequence; with an EventSpec it contextually denotes the next/first matching occurrence. |
| `Forgive` | Process: relinquish blame/resentment toward an offender for an offense without necessarily denying responsibility or erasing memory/other emotions. |
| `Form` | Geometric/form profile of an entity. |
| `FriendOf` | Ordinary friendship Relation. |
| `Gas` | Matter-phase value/property: gas. |
| `GratefulTo` | Gratitude Relation toward a benefactor. |
| `GrieveFor` | Grief Relation concerning a person/event/state. |
| `Group` | Kind: a group entity. |
| `Gustation` | Sense channel: taste/gustation. |
| `Happen` | States that an EventSpec actually occurs, optionally in an interval. |
| `Happy` | Persistent/contextual happiness Property. |
| `Hard` | Contextual material/structural hardness Property. |
| `Hate` | Persistent strong aversive/hostile Relation toward a target. |
| `Health` | Ordered overall biological functional-condition Attribute; distinct from Damage and Ill. |
| `Have` | Persistent possession/holding relation. |
| `Hearing` | Sense channel: hearing. |
| `Heat` | Scalar heat attribute of an entity. |
| `Here` | Current contextual location. |
| `High` | Contextual above-standard predicate over ordered EvaluationValue, Quantity, or Ratio values; with an AttributeDescriptor it forms a first-class threshold Property. |
| `Hunger` | Ordered hunger-degree Attribute. |
| `If` | Conditional: if the condition holds, the consequent proposition/event follows in the represented structure. |
| `Ill` | Persistent pathological/illness-state Property; distinct from Damage, Pain, Low Health, and Not Life. |
| `In` | Persistent spatial relation: an entity is in a Region. |
| `Infer` | EventSpec in which a mind infers a proposition from Information. |
| `Intend` | States an agent's intention to carry out an EventSpec. |
| `Interval` | Constructs a TimeInterval from start and end TimePoints. |
| `IntervalFor` | Constructs a TimeInterval from a start TimePoint and duration. |
| `JealousOf` | Jealous-attitude Relation. |
| `Joined` | Persistent structural relation: two entities are joined. |
| `Jump` | Contextual launch/airborne locomotion Process; a goal Location may be supplied. Generic Move does not encode the jumping manner. |
| `Know` | Persistent epistemic state: a mind knows a proposition. |
| `Last` | Selects the last member of an ordered Sequence. |
| `Length` | Length attribute of an entity/path. |
| `Life` | State property: alive/living. |
| `Light` | Scalar light attribute of an entity. |
| `Like` | States that an experiencer likes a target. |
| `Limp` | Locomotion Process with an asymmetric/impaired gait; does not by itself assert a particular Damage level or cause. |
| `Liquid` | Matter-phase value/property: liquid. |
| `Locked` | Persistent locked/sealed-by-lock state Property. |
| `Loudness` | Ordered sound-loudness Attribute; objective measurement belongs to the world package. |
| `Love` | Persistent affectionate/loving Relation toward a target. |
| `Low` | Contextual below-standard predicate; with an AttributeDescriptor it forms a first-class threshold Property such as LowHunger. It is not equivalent to Not High. |
| `Magic` | State property: magical. |
| `Male` | Positive biological-sex classification Property; not defined as Not Female. Exact membership belongs to world ontology. |
| `Mass` | Scalar mass attribute of an entity. |
| `Matter` | Kind: matter/material substance. |
| `MaxBy` | Tie-preserving maximum selector over a collection using a bound ordered key expression. |
| `Meaning` | Relates a Sign to its semantic Information/propositional meaning. |
| `Member` | States that an entity is a member of a collection. |
| `MinBy` | Tie-preserving minimum selector over a collection using a bound ordered key expression. |
| `More` | States that the first ordered value is greater than the second. |
| `Most` | Contextual majority/most quantifier over a typed binder. |
| `Move` | EventSpec for moving an entity; magical execution must constrain goal or path. |
| `Multiply` | Multiplies quantities and combines their dimensions. |
| `Name` | Relates a Sign/name to a referent in a naming context. To select a unique referent, use typed `Collect` + `Unique`. |
| `Not` | Logical negation of a proposition. |
| `Now` | Current contextual time point. |
| `Obligated` | Persistent deontic/social responsibility for an EventSpec; an optional third value identifies its social/institutional/interpersonal context. |
| `Offset` | Constructs a Location by moving a distance from an origin in a Direction. |
| `Olfaction` | Sense channel: smell/olfaction. |
| `Open` | Contextual persistent open-state Property relative to an object's closure/design. |
| `Opposite` | Numeric opposite/negation of a quantity; also participates in licensed reversible lexical compounds. |
| `Or` | Logical disjunction of propositions. |
| `Overlap` | General typed overlap relation; Region/Region overlap means nontrivial shared interior extent and composes strict outside. |
| `Own` | Ownership/property-right Relation; exact legal rules belong to world ontology. |
| `Pain` | Ordered experienced pain/nociceptive-suffering Attribute; distinct from physical Damage. |
| `ParentOf` | Parent-child Relation. |
| `Part` | States that one entity is a part of another. |
| `Partition` | Contextually partitions a collection into fixed-size subcollections. |
| `Path` | General ordered route/path Kind. |
| `Permitted` | Permission relation: agent+EventSpec states performer permission; EventSpec+Entity states permission/consent from that source. A particular permission does not itself assert broad Authority. |
| `Persist` | Actively maintains a state through an interval. |
| `Phase` | Matter phase attribute of an entity. |
| `Plan` | States that an agent has an EventSpec as a plan. |
| `Plasma` | Matter-phase value/property: plasma. |
| `Power` | Raises a quantity to a dimensionless exponent; dimensionful bases require a statically known valid exponent. |
| `Pressure` | Absolute scalar mechanical-pressure Attribute for an Entity/material/system or a Location; its Quantity dimension is derived from Mass/Length/Time. |
| `Preserve` | Constrains a selected value to remain equal across an event boundary. |
| `Prevent` | Prevents matching future events over an explicit interval/scope. |
| `Purpose` | Persistent intended goal/function relation for a semantic subject, including artifact designed function; temporary Use does not establish it. |
| `Question` | Constructs semantic QuestionContent from a proposition or typed open-question binder. |
| `Random` | Selects one member from a collection. |
| `Rate` | General per-time rate: Quantity-over-Time for a Quantity, or occurrence frequency for an EventSpec. |
| `Ratio` | Constructs a ratio from dimensionless numeric components; distinct from numeric division. |
| `Reflexive` | States that an EventSpec occurs as an involuntary/reflex response; absence of conscious intention alone is not equivalent. |
| `Region` | General spatial Region Kind. |
| `Remember` | Memory/retention Relation over semantic content. |
| `RemorseFor` | Remorse Relation concerning an action/event/consequence. |
| `Repeat` | Repeats an EventSpec a specified number of times, optionally with a period. |
| `Represent` | Persistent channel-specific representation: an Entity presents/depicts semantic content through a named SenseChannel. It does not make the represented content real and is distinct from Meaning and Sense. |
| `Reputation` | Ordered social-standing Attribute, optionally relative to an explicit community/evaluator. |
| `Requires` | States that an outcome/event has a prerequisite proposition. |
| `Respect` | Positive-regard Relation acknowledging worth/status/character. |
| `ResponsibleFor` | Responsibility-attribution Relation; causal/legal/moral grounds remain separately expressible. |
| `Root` | Takes a quantity root; dimensionful inputs require a statically known degree that leaves integral dimension exponents. |
| `Rotate` | Rigidly rotates an Entity around an explicit pivot + oriented axis by a signed number of full turns; distinct from Move and Form change. |
| `Rule` | General rule/instruction Kind. |
| `Sad` | Persistent/contextual sadness Property. |
| `Say` | Speech EventSpec carrying a proposition, Information, or quoted Sign. |
| `Self` | Current discourse self/speaker/caster reference. |
| `Sense` | Generic sensory-acquisition EventSpec with an explicit SenseChannel; it does not by itself mean the Sign/stimulus was understood. |
| `Sequence` | Constructs an ordered Sequence value, or an EventSpec that executes event specifications in order. |
| `ShameAbout` | Shame Relation concerning an action/property/event/social fact. |
| `ShapeLike` | States that an entity's form resembles a Kind/template without asserting Kind identity. |
| `Sharp` | Contextual edge/point sharpness Property. |
| `Sides` | Returns side Region(s) of an entity, optionally relative to a frame. |
| `Sign` | General Sign Kind used by the information/language system. |
| `Simultaneous` | States that two events/time points are simultaneous. |
| `Sleep` | Persistent contextual sleep-state Property. |
| `Solid` | Matter-phase value/property: solid. |
| `Some` | Existential quantifier over a typed binder. |
| `SpouseOf` | Persistent marriage/spousal Relation. |
| `Stab` | Directed puncturing/thrust Process against a target, optionally with an instrument; not equivalent to generic Attack, Damage, Touch, or Use. |
| `SufficientFor` | States that a condition is sufficient for an outcome/event. |
| `Surface` | Returns the surface Region of an entity. |
| `TextureOf` | TextureProfile Attribute of an Entity. |
| `That` | Contextual previously/situationally salient entity reference. |
| `ThatEvent` | Contextual other/salient event reference. |
| `There` | Contextual non-here location. |
| `They` | Contextual plural/entity-collection reference. |
| `Thing` | General thing/entity Kind. |
| `This` | Current salient singular entity reference. |
| `ThisEvent` | Current salient event reference. |
| `ThisExplanation` | Current salient Explanation value. |
| `ThisInformation` | Current salient Information value. |
| `ThisInterval` | Current salient time interval. |
| `ThisMethod` | Current salient Method value. |
| `ThisPath` | Current salient path. |
| `ThisRegion` | Current salient region. |
| `Through` | States that a Path passes through a Region, or constrains an event to occur through a Region. |
| `TotalAmount` | Returns total quantity represented by a Distribution, optionally within a Region. |
| `Touch` | Persistent contact-state relation between two entities. |
| `TouchChannel` | Sense channel: tactile touch. |
| `Toward` | Constructs a Direction toward a reference. |
| `Transfer` | EventSpec moving a resource/value from source to destination, optionally with an amount and destination Distribution profile. |
| `Trigger` | Creates an EventSpec that fires an action when a condition becomes true within a lifetime/scope. |
| `True` | Boolean/propositional truth literal. |
| `Trust` | Interpersonal confidence/reliance Relation. |
| `Tube` | Constructs a tubular Region around a Path with a radius. |
| `UnavailableValueOf` | States that a particular attribute value exists but is unavailable/inaccessible. |
| `Understand` | Comprehension Relation over semantic content. |
| `Unique` | Reduces a collection only when it has exactly one member. |
| `Unit` | General measurement-unit Kind/root. Specific typed units are historical Old Names such as `«LengthUnit»` and `«DurationUnit»`. |
| `UnknownValueOf` | States that a particular attribute value is unknown. |
| `Use` | EventSpec in which an agent uses an instrument to pursue a goal EventSpec. |
| `Vision` | Sense channel: vision. |
| `Volume` | Scalar volume attribute of an entity. |
| `Want` | States that a mind desires an event or proposition. |
| `When` | Schedules/locates an EventSpec at a time point or interval. |
| `Whole` | Persistent structural integrity/completeness state; `End Whole X` expresses loss of wholeness. |
| `Worship` | Ordinary intentional/religious worship Process. Worship does not itself entail that the object is objectively divine. |
| `You` | Current addressee reference. |
| `Zero` | Exact dimensionless numeric zero. |
