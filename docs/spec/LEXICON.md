# Working Lexicon

_Status: registered/candidate lexical inventory v0.1_

This is the current consolidated vocabulary map. Detailed semantics live in the domain specifications.

Legend:

- **R** — registered working root/lexical item.
- **D** — derivable/conventional semantic molecule; may receive a compact rune.
- **C** — contextual ordinary-language item; magic needs an explicit standard.
- **W** — world/campaign ontology item.
- **X** — deferred/rejected as a generic magical root.
- Tier **B/I/A** — beginner/intermediate/advanced candidate.
- Tier **F** — full-language/ordinary vocabulary, not a caster tier.

The English labels are glosses, not definitions.\n\nCurrent minimized executable registry: **206 entries**. Rows marked D describe useful derived meanings but are not standalone productive roots unless also marked R.

## Reference, identity, ontology

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Thing | R | Kind, broad entity ontology | B |
| Matter | R | Kind/domain | B |
| Exist | R | existence-state Property over Entity/SemanticValue, including Sign tokens | I |
| Self | R | Reference<Entity> caster/issuer | B |
| You | R | Reference<Entity> formal addressee | I |
| This | R | Reference<T> designated referent | B |
| Here | R | Reference<Location> activation origin | B |
| Now | R | Reference<TimePoint> evaluation instant | I |
| InstanceOf | R/D | Entity-Kind membership Relation; Kind-head shorthand | B |
| Same | D | Entity `Equal` | I |
| Different | D | NotSame | I |
| Part | R | structural mereology Relation | B |
| Joined | R | persistent structural Relation | I |
| Whole | R | persistent integrity/completeness StateProperty; End Whole is structural-loss transition | B |
| Kind (generic rune) | X | ambiguous classification level | — |
| Group | R | group Entity/Kind with Members | I |
| Member | R | Collection/group membership Relation | I |
| Other/OtherThan | D | relative identity exclusion | I |

## Logic and control

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Not | R | logical complement Operator | B |
| Opposite | R | reversible-axis Operator | B |
| Converse | D/X | role reversal written by direct Relation argument order | — |
| And | R | conjunction/composite Operator | B |
| Or | R | disjunction Operator | I |
| If | R | typed conditional Operator | A |
| Requires | R | necessity/prerequisite Relation | I |
| SufficientFor | D/R | sufficiency implication Relation | I |
| True | R | Proposition truth Property | I |
| False | D | Not True | I |
| Because | D | contextual `Explains reason target`; use Cause/EvidenceFor for those typed readings | I |
| All | R | universal quantifier | A |
| Some | R | existential quantifier | A |
| None | D | NotSome | A |
| Both | D | two-member conjunction | I |
| Either | X/C | ambiguous selector/disjunction gloss | F |
| Only | R | scope/restriction Operator | A |
| Generic | D/C | contextual `High Ratio Count Collect... / Count Collect...` prevalence | F |
| Most | R | strict majority quantifier | I |
| Like | C | similarity requiring dimensions/standard | F |
| Maybe | C | epistemic modality | F |

## Collections and selection

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Collect | R | set-comprehension Operator | A |
| Filter | R | Collection predicate restriction | A |
| Each | R | distributed EventSpec Operator | A |
| Count | R | Collection -> integer Quantity | I |
| Unique | R | exactly-one selector | A |
| Nearest | R | minimum-Distance selector returning ties | A |
| Farthest | R | maximum-Distance selector returning ties | A |
| Lowest | R | minimum-scalar selector | A |
| Highest | R | maximum-scalar selector | A |
| First | R | Sequence selector; contextual EventSpec overload gives next/first matching occurrence | I |
| Last | R | Sequence selector | I |
| Random | R | explicit nondeterministic selector | A |
| OneOf | X | selection policy unspecified | — |

## Quantity and mathematics

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| @ | R | Quantity 1 | B |
| Zero | R | Quantity 0 | B |
| High | R/C | contextual above-standard predicate / threshold-Property constructor | F/I |
| More | R | ordered comparison Relation | B |
| Less | D | More with reversed arguments | B |
| Equal | R | typed value equality | B |
| Add | R | arithmetic Operator | A |
| Multiply (x) | R | arithmetic Operator | A |
| Divide | R | arithmetic Operator | A |
| Power | R | arithmetic Operator | A |
| Root | R | arithmetic Operator | A |
| Ratio | R | proportion constructor | A |
| AtLeast | D | More Or Equal | I |
| AtMost | D | reversed More Or Equal | I |
| Many | C | Count threshold | F |
| Few | C | Count threshold | F |
| Very | C | contextual scalar intensifier | F |

## Space and geometry

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Space | R | spatial domain/Kind | B |
| Region | R | spatial extent Kind | I |
| Path | R | ordered trajectory Kind/value | I |
| At | R | anchor-location Relation | B |
| In | R | containment state Relation | B |
| Contain | D | same In(item,region) Relation; no separate root | I |
| Inside | D | `In` plus no Region-boundary `Touch`: `And {In A R,Not Touch Extent A R}` | I |
| Outside | D | no interior Region overlap: `Not Overlap Extent A R`; stronger than Not In | I |
| Touch | R | Entity contact-state Relation plus Region/Region boundary-contact topology; `Begin Touch` participates in compositional Grab | B |
| Overlap | R | typed overlap Relation; Region/Region means nontrivial shared interior extent | I |
| To | R | oriented goal/path relation | B |
| From | D/R | OppositeTo | B |
| Up | R | frame-relative direction Relation | B |
| Down | D/R | OppositeUp | B |
| Distance | R/C | physical Length distance plus contextual Property/EventSpec boundary-distance overloads | I/F |
| Near | C/R | threshold Distance Relation | B |
| Far | C/D | opposite pole of Near scale | I |
| Offset | R | relative Location constructor | I |
| Toward | D/R | direction constructor | I |
| AwayFrom | D/R | inverse direction constructor | I |
| Through | R | Path/Region Relation | I |
| Around | R | radius/reference spatial constructor | I |
| Center | R | functional geometry Relation | I |
| Surface | R | boundary SurfaceRegion function | I |
| Edge | R | boundary feature function | I |
| Sides | R | collection of side surfaces | I |
| Extent | R/C | occupied Region, contextual holistic EvaluationValue, or frame-axis projected Length | I/F |
| Form | R | Entity -> GeometryProfile function | I |
| ShapeLike | D/R | Form similarity to template/Kind without Kind identity | I |
| Point | R | geometric Kind | I |
| Line | R | geometric Kind | I |
| Straight | R | geometry Property | I |
| Curve | R | geometry Property/Path form | I |
| Flat | R | geometry Property | I |
| Round | R | geometry Property | I |
| Hole/Holes | R | topological feature function | I |
| Symmetry | R | parameterized geometry predicate | A |
| Length | R | scalar attribute | I |
| Span | D | `Extent X F axis` | I |
| Size | D/C | contextual EvaluationValue frame of `Extent` | F/I |
| Area | R | scalar attribute | I |
| Volume | R | scalar attribute | I |
| Height | D | `Extent X F @` | I |
| Width | D | `Extent X F @@` | I |
| Angle | R | angular scalar attribute | I |
| Ball | D/R | Region constructor | I |
| Disk | D/R | Region constructor | I |
| Box | D/R | Region constructor | I |
| Cylinder | D/R | Region constructor | A |
| Cone | D/R | Region constructor | A |
| Tube | D/R | Path-radius Region constructor | A |

## Time and events

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Time | R | temporal domain/dimension | I |
| Moment | R | TimePoint Kind | I |
| Before | R | temporal order Relation | B |
| After | D | Before with reversed arguments | B |
| During | R | temporal containment Relation | I |
| Simultaneous | R | temporal Relation | I |
| Duration | D | `Extent(Event)` -> Quantity<Time> | I |
| Interval | R | temporal constructor | I |
| When | R | EventSpec temporal attachment | I |
| Begin | R | boundary Operator | B |
| End | R | boundary Operator | B |
| Always | D | `During P I` | A |
| Never | D | `During Not P I` | A |
| Happen | R | EventSpec realization Proposition Operator | I |
| Sequence | R | ordered EventSpec/collection Operator | A |
| Repeat | R | finite recurrence Operator | A |
| Period | D | reciprocal of Rate | A |
| Again | C | discourse-relative recurrence | F |
| Past | D | `Before X Now` | F/I |
| Present | D | bare state at reference time; EventSpec -> `During E Now` | F/I |
| Future | D | `Before Now X` | F/I |
| Ongoing | D | `During E T` | F/I |
| Completed | D | `Before E Now` / `Before E T` | F/I |
| Continue | D | `Prevent End E Interval Now Now` for a resolved ongoing Event | I |
| Habitual | D/C | `High Rate E I` under the contextual habituality threshold | F |
| Whenever | D | `During SufficientFor condition consequence interval/context` | F/I |

## Processes and change

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Change | R | explicit Attribute-setting Process | B |
| ChangeBy | D | Change + Add + BeforeValue | I |
| BeforeValue | R | pre-event value snapshot function | A |
| AfterValue | R | post-event value snapshot function | A |
| Preserve | R | event-boundary invariant constraint | A |
| Almost | D/C | `And {Not P x,Low Distance P x}`; EventSpec form uses `Not Happen E` | F/I |
| Move | R | spatial-change Process | B |
| Teleport | D | discontinuous `End At source + Begin At goal` state transition | A |
| Join | D | Begin Joined | B |
| Separate | D | End Joined | I |
| Split | D/R | one structure -> multiple result identities Process | A |
| Merge | D/R | identity-forming fusion Process | A |
| Repair | R | integrity restoration Process | I |
| Create | R | fresh-identity Process | A |
| Destroy | D | End Exist | A |
| Transform | R | identity-preserving profile change | A |
| Cause | R | causal Event relation/control; Entity may cause EventSpec or StateProposition, optional `:instrument` | A |
| Sever | D | `Cause agent (End Whole target)`, optional `:instrument` | I |
| Attempt | R | goal-directed effort Process; does not entail goal success | I/F |
| Use | R | intentional instrument Process | I |
| Control | R | persistent controller-target state; `Begin Control` participates in compositional Grab | I/A |
| Redistribute | D | Distribution-valued `Transfer`, optional named `:profile` | A |
| Give | R | transfer Process | I |
| Get | D | Begin Have | I |
| Lose | D | End Have | I |
| Open | R | artifact/state Process | I |
| Prevent | R | prohibit matching Events over scope/interval | A |
| Concurrent | R | overlapping composite EventSpec Operator | I |
| Do | X | command mood makes generic Do unnecessary | — |
| Keep | D/C | maintain-state ordinary gloss; magic uses Persist | F |

## General relations / roles

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Have | R | possession/control state Relation | I |
| With | R/C | association Relation with typed frames | F |
| For | C/X | conversational umbrella; not generic magical relation | F |
| Purpose | R | persistent intended goal/function Relation, including artifact designed function | I |
| DesignedFor | D | `Purpose artifact function` grounded by design evidence | I |
| Beneficiary | R | Event-beneficiary Relation | I |
| Using | D | `Use event instrument` relation overload | I |
| About | R | Information-topic Relation | F |
| Against | C/R | domain-specific opposition Relation | F |
| Of | X | rejected generic relation | — |
| By | X | rejected overloaded relation | — |
| Without | D | NotWith | F |
| Mine | D | Have(Self, x) construction | F |
| Exchange | D/R | reciprocal transfer Process | I |

## Matter and physical attributes

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Phase | R | material Attribute | I |
| Solid | R | Phase family Property | B |
| Liquid | R | Phase family Property | B |
| Gas | R | Phase family Property | B |
| Plasma | R | Phase family Property | I |
| Heat | R | scalar thermal Attribute | B |
| Mass | R | scalar Attribute | I |
| Density | R | scalar Attribute; also Distribution+Region local density | A |
| Distribution | R | spatial resource/field structured value | A |
| DistributionOf | R | resource/host -> Distribution function | A |
| LocalDensity | D | `Density distribution region` | A |
| TotalAmount | R | Distribution-region amount function | A |
| Force | R | vector quantity/physical relation | I |
| Energy | R | scalar physical quantity | A |
| Pressure | R | scalar Attribute | A |
| Charge | R | signed scalar Attribute | A |
| Magnetic | R | field/interaction Property/Attribute | A |
| Big | D/C | `HighSize` | F/I |
| Small | D/C | `LowSize` | F/I |
| Hard | R/C | material scalar/threshold Property | I |
| Flexible | R/C | material Property | I |
| Brittle | R/C | material Property | I |
| Sharp | R/C | geometry/material Property | I |
| Smooth | R/C | surface Property | I |
| Soft | D/C | low Hard region | I |
| Rough | D/C | low/opposite Smooth region | I |
| Element | W/R | material taxonomy Kind | F |
| Atom | W/R | material Kind | F |
| Molecule | W/R | material Kind | F |
| Metal | W/R | material class | F |
| Organic | W/C | material/biological classifier | F |

## Light, color, sound

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Light | R | scalar visible-intensity Attribute | B |
| ColorOf | R | subject -> ColorProfile Attribute | I |
| ColorValue | D/R | ColorProfile constructor | I |
| Red | R | Color blend-family component | B |
| Green | R | Color blend-family component | B |
| Blue | R | Color blend-family component | B |
| Yellow | D/R | RedGreen profile | I |
| Cyan | D/R | GreenBlue profile | I |
| Magenta | D/R | RedBlue profile | I |
| White | D/R | balanced high-intensity profile | I |
| Gray | D/R | balanced lower-intensity profile | I |
| Black | D/R | zero/near-zero intensity profile | I |
| Bright | C | high Light threshold | F |
| Dark | C | low Light threshold | F |
| Transparent | R | optical Attribute/Property | I |
| Opaque | D/R | low-transparency profile | I |
| Reflectance | R | optical Attribute | A |
| Glow/EmitLight | D/R | light-emission Process | I |
| Sound | R | scalar acoustic Attribute/phenomenon | B |
| Vibration | R | physical oscillation Process/Attribute | I |
| Frequency | R | scalar inverse-Time Attribute | I |
| Rate | R | Typed per-Time rate: EventSpec occurrence frequency or Quantity change-rate | I |
| Stable | D | Equal Rate with Zero, or a two-sided tolerance bound | I |
| Wave | R | phenomenon Kind/profile | I |
| Loud | C | high Sound threshold | F |
| Quiet | C | low Sound threshold | F |

## Integrity

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Damage | R | structured integrity Attribute/Property | B |
| Broken | D/R | Kind-relative damage state | I |
| Cut | D/R | separation/damage Process | I |
| Crush | D/R | compression/damage Process | I |
| Burn | D/R | thermal/material damage Process | I |
| Wound | D/R | living Damage specialization | I |
| Heal | D/R | biological Repair | I |

## Life and biology

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Life | R | biological state-predicate Property | B |
| Grow | D | constrained positive Change(Extent) | I |
| Reproduce | R | biological fresh-result Process | A |
| Eat | R | biological consumption Process | F |
| Breathe | R | biological exchange Process | F |
| Disease | R | pathological state-predicate | I |
| Birth | D/R | BeginLife semantic molecule | I |
| Death | D/R | EndLife semantic molecule | I |
| Dead | D/R | PastLife + NotLife profile | I |
| ToxicTo | R | dose/target toxicity Relation | I |
| Poison | W/C | conventional toxicity-defined Kind | F |
| Food | W/R | consumer-relative function Kind | F |
| Medicine | W/R | therapeutic function Kind | F |
| Blood | W/R | biological Material Kind | I |
| Plant | W/R | biological Kind | F |
| Animal | W/R | biological Kind | F |
| Human | W/R | biological/person Kind | B/I |
| Undead | W | setting-defined only | — |

## Mind and perception

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Mind | R/W | mental-system Kind/domain | I |
| BodyOf | W/R | world-metaphysics body-person/mind Relation | F/I |
| Awake | W/R | wakefulness state Property | F/I |
| Think | R | mental Event Process | F |
| Know | R | factive state Relation | I |
| Believe | R | non-factive state Relation | F |
| Confidence | R | Mind-Proposition epistemic scalar Attribute | I/F |
| ProbableTo | D | High Confidence composition | F |
| PossibleTo | D | More Confidence ... Zero composition | F |
| CertainTo | D | `Equal Confidence mind P «ConfidenceUnit» @` | F |
| EvidenceFor | R | Information supports Proposition Relation | I/F |
| EvidenceAgainst | D | EvidenceFor of Not proposition | I/F |
| EvidenceStrength | R | evidence-support scalar function | A/F |
| Expect | R | prospective epistemic state Relation | F |
| Infer | R | evidence-driven belief-update Process | F/I |
| Detected | D | `Happen Sense ...` | I |
| NotDetected | D | `Not Happen Sense ...` | I |
| Want | R | desire state Relation | F |
| Evaluate | R/C | evaluator-target evaluation function/relation | F |
| GoodFor | D/R | positive evaluator-relative judgment | F |
| BadFor | D/R | negative evaluator-relative judgment | F |
| ImportantTo | D/C | `High Evaluate evaluator target` | F |
| Like | R/C | stable positive-attitude Relation | F |
| Intend | R | agent-goal/EventSpec intention state Relation | F/I |
| Plan | R | agent-plan Information/state Relation | F/I |
| Obligated | R/C | deontic responsibility Relation | F |
| Permitted | R/C | agent permission or EventSpec permission/consent with explicit `:authority` | F |
| Consent | D | addressed `Say` of `Permitted E :authority consenter` | F/I |
| Refuse | D | addressed `Say` of `Not (Permitted E :authority refuser)` | F/I |
| Deceive | D | `If (Not P) (Cause deceiver (Believe target P))` | F/I |
| Sense | R | sensing Process; explicit-channel raw perception plus contextual interpreted-Sign overload | B |
| See | D | Sense + Vision | I |
| Hear | D | Sense + Hearing | I |
| TouchSense | D/R | contact Sense | I |
| Smell | D | Sense + Olfaction | F |
| Taste | D | Sense + Gustation | F |
| Sleep | R | mind/life state Property | I |
| Dream | R | mental Event Process | F |
| Remember | R | Mind-Information state Relation | I |
| Forget | D/R | EndRemember | I |
| Memory | R | Information Kind | I |
| Fear | R | mental state Relation | I |
| Pain | R | sensation state/Information | I |
| Attention | R | mind-target state Relation | F |
| Feel | C/X | overloaded ordinary umbrella | F |
| VisibleTo | R | observer-relative visual-access Relation | I |

## Information and language

Information itself is a semantic type rather than a registered Kind root. The table below lists lexical items that operate on or represent Information.

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Sign | R | Information-bearing Kind | B |
| Meaning | R | Sign-content Relation | I |
| Word | R | lexical Sign Kind | F |
| Language | R | sign/grammar system Kind | F |
| Say | R | information-expression Process | I |
| Assert | R | speech act presenting Proposition as true | F/I |
| Claim | D | Assert | F |
| Promise | D | Say contextual Obligation + Begin contextual Obligation | F/I |
| CommittedTo | D | `Obligated agent event :context other` | F/I |
| Explanation | R | explanatory Information structure | F/I |
| Explains | R | Explanation-target Relation; contextual Proposition+Proposition frame covers discourse explanation | F/I |
| Contrast | R/C | discourse concession/contrast Relation | F |
| Speak | D/R | Say via audible linguistic medium | F |
| Write | D | `Cause writer Begin Exist sign` for a typed Sign | I |
| Read | D | `If Sign S (Sense reader S)` using contextual interpreted-Sign Sense | I |
| Record | R | persistent Sign/Information Entity | I |
| Number | D/R | numeral Sign/Information Kind | F |
| NumericValue | R | numeral -> Quantity relation/function | I |
| Question | R | interrogative Information/speech act | F |
| Answer | R | response Information | F |
| Rule | R | conditional/normative Information Kind | A/F |
| Method | R | procedural Information/Plan Kind | F/I |
| MethodFor | D | `Purpose method goal` | F/I |
| Command-content | R | directive Information Kind | A |
| Copy | R | Information-copy Process | A |
| Find/Reveal | R | information-acquisition/search Process | A |
| Name | R | Sign-referent Relation | F |

## Purpose, tools, and artifact Kinds

These are mostly registered semantic molecules or world lexicon entries rather than semantic primitives.

| Gloss | Status | Role | Tier |
|---|---|---|---|
| Tool | W/D | design/function Kind | F |
| Weapon | W/D | Tool function Kind | F |
| Container | W/D | containment-function Kind | I/F |
| House | W/D | inhabitable structure Kind | F |
| Door | W/D | passage-control structure Kind | I/F |
| Sword | W/D | artifact design Kind | I/F |
| Clothing | W/D | worn-covering function Kind | F |

## Social / ordinary language

These are legitimate full-language candidates but generally need social/context models before magical use.

| Gloss | Status | Role |
|---|---|---|
| Good | C | evaluator/standard Property |
| Bad | C | evaluator/standard Property |
| Help | R/C | goal-support Process |
| OwnerOf | W/R | social/legal possession Relation | F |
| Spouse | W/R | marriage/social Relation | F |
| Profession | W/R | person-role/profession Relation | F |
| Friend | R/C | social state Relation |
| Enemy | R/C | social state Relation |
| Owe | R | obligation Relation |
| Promise | D | Say + Begin contextual Obligation |
| Agree | R | proposition-linked social state/process |
| Tell | R | information-transfer Process |
| Learn | D | typed `Begin Know` / `Begin Can` / `Begin Understand` acquisition |
| Thank | D | addressed `Say` of a `GratefulTo` proposition |
| Apologize | D | addressed `Say` of a `RemorseFor` proposition |
| Work | C/R | goal-directed activity |
| Play | C | contextual activity |
| Love | R/C | mental/social state Relation |
| Hate | R/C | mental/social state Relation |
| Harm | D/R | cause Damage/adverse state |
| Disagree | D/R | proposition-linked disagreement |

## Magic-specific/control

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| AvailableTo | W/R | access/availability state Relation | F/I |
| Unlock | D/R | Begin AvailableTo semantic molecule | F/I |
| Magic | R | active magical-state Property | I |
| Mana | R | scalar resource dimension/Attribute | B/I |
| Persist | R | active state-maintenance Operator | A |
| Trigger | R | conditional persistent control Operator | A |
| Repeat | R | finite recurrence Operator | A |
| Enchant | D/R | persistent Magic semantic molecule | A |
| Dispel | D/R | EndMagic semantic molecule | I/A |
| Atomic | D | future transaction/rollback Operator if supported | A |

## World concepts and historically conventional noun names

Earlier work expected many ordinary nouns to become registered Kind roots. The default policy is now different.

Common culturally developed nouns should normally be modeled as:

1. a stable world concept/classifier;
2. a historically plausible descriptive **Old Name** built from semantic roots already available when the name arose;
3. an exact quoted Sign `«... »` whose frozen historical meaning points to that concept.

Do not invent a new one-word primitive merely because modern English has one.

Existing executable noun roots such as Water, Human, Cat, or Hand remain temporarily for compatibility until the corpus/worldbuilding pass constructs and tests their replacements. Migration is deliberate rather than piecemeal.

Proper/current names such as a person's foreign name are **New Names** and remain ordinary Name/reference relations without magical lexical expansion.

The first seeded civilization/worldbuilding batch is listed in `docs/world/FIRST_CIVILIZATION_VOCABULARY.md`. It deliberately adds productive descriptive roots such as Extent/Hard/Sharp/Sign/Rule rather than direct English noun roots for objects such as Ship, House, Sword, Book, or Market.

See `NAMES_AND_WORLDBUILDING.md`.

## Rejected generic roots

The following should not return without a new formal justification:

- generic magical Of
- generic magical By
- generic magical For as purpose/beneficiary umbrella
- generic KindOf(This)
- OneOf as unspecified selector
- Start separate from Begin
- Part as numerical Ratio
- universal physical Copy
- Do as mandatory command verb
- automatic Undead = OppositeLife
- generic Feel as one precise magical predicate

## Maintenance rule

Whenever a root is added, record:

- Category;
- Domain;
- Traits;
- Frame;
- constraints;
- derivation/normalization;
- magical availability;
- discovery tier.

This file is a vocabulary map, while exact definitions remain in the corresponding domain specifications.
