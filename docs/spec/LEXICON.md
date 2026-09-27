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

The English labels are glosses, not definitions.

## Reference, identity, ontology

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Thing | R | Kind, broad entity ontology | B |
| Matter | R | Kind/domain | B |
| Exist | R | state-predicate Property | I |
| Self | R | Reference<Entity> caster/issuer | B |
| You | R | Reference<Entity> formal addressee | I |
| This | R | Reference<T> designated referent | B |
| Here | R | Reference<Location> activation origin | B |
| Now | R | Reference<TimePoint> evaluation instant | I |
| Same | R | identity Relation | I |
| Different | D | NotSame | I |
| Part | R | structural mereology Relation | B |
| DirectPart | D/R | immediate structural Part Relation | I |
| Joined | R | persistent structural Relation | I |
| Whole | R | integrity/completeness Property | B |
| Kind (generic rune) | X | ambiguous classification level | — |
| Group | R | group Entity/Kind with Members | I |
| Member | R | membership Relation | I |
| Members | R | Group -> Collection functional Relation | I |
| Other/OtherThan | D | relative identity exclusion | I |

## Logic and control

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Not | R | logical complement Operator | B |
| Opposite | R | reversible-axis Operator | B |
| Converse | R | relation-role permutation Operator | A |
| And | R | conjunction/composite Operator | B |
| Or | R | disjunction Operator | I |
| If | R | typed conditional Operator | A |
| True | R | Proposition truth Property | I |
| False | D | complement of True | I |
| Because | R | causal/reason Relation | I |
| All | R | universal quantifier | A |
| Some | R | existential quantifier | A |
| None | D | NotSome | A |
| Both | D | two-member conjunction | I |
| Either | X/C | ambiguous selector/disjunction gloss | F |
| Only | R | scope/restriction Operator | A |
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
| First | R | Sequence selector | I |
| Last | R | Sequence selector | I |
| Random | R | explicit nondeterministic selector | A |
| OneOf | X | selection policy unspecified | — |

## Quantity and mathematics

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| @ | R | Quantity 1 | B |
| Zero | R | Quantity 0 | B |
| More | R | ordered comparison Relation | B |
| Less | D/R | OppositeMore | B |
| Equal | R | typed value equality | B |
| Add | R | arithmetic Operator | A |
| Multiply (x) | R | arithmetic Operator | A |
| Divide | R | arithmetic Operator | A |
| Power | R | arithmetic Operator | A |
| Root | R | arithmetic Operator | A |
| Ratio | R | proportion constructor | A |
| AtLeast | D/R | scalar comparison | I |
| AtMost | D/R | scalar comparison | I |
| Between | R | ordered ternary Relation | I |
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
| Contain | D/R | ConverseIn | I |
| Inside | D/R | strict interior Relation | I |
| Outside | R | exterior Relation, not NotIn | I |
| Touch | R | contact Relation | B |
| Overlap | R | spatial-overlap Relation | I |
| To | R | oriented goal/path relation | B |
| From | D/R | OppositeTo | B |
| Up | R | frame-relative direction Relation | B |
| Down | D/R | OppositeUp | B |
| Distance | R | scalar attribute/function | I |
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
| Extent | R | Entity -> Region function | I |
| Form | R | Entity -> GeometryProfile function | I |
| Point | R | geometric Kind | I |
| Line | R | geometric Kind | I |
| Straight | R | geometry Property | I |
| Curve | R | geometry Property/Path form | I |
| Flat | R | geometry Property | I |
| Round | R | geometry Property | I |
| Hole/Holes | R | topological feature function | I |
| Symmetry | R | parameterized geometry predicate | A |
| Length | R | scalar attribute | I |
| Area | R | scalar attribute | I |
| Volume | R | scalar attribute | I |
| Height | R | frame-relative scalar attribute | I |
| Width | R | frame-relative scalar attribute | I |
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
| After | D/R | OppositeBefore | B |
| During | R | temporal containment Relation | I |
| Simultaneous | R | temporal Relation | I |
| TimeOverlap | R | interval-overlap Relation | I |
| Duration | R | Event -> Quantity<Time> | I |
| Interval | R | temporal constructor | I |
| When | R | EventSpec temporal attachment | I |
| Begin | R | boundary Operator | B |
| End | R | boundary Operator | B |
| Former | R | historical state Operator | I |
| Always | R | temporal universal Operator | A |
| Never | D/R | temporal negated existential | A |
| Happen | R | EventSpec realization Proposition Operator | I |
| Sequence | R | ordered EventSpec/collection Operator | A |
| Repeat | R | finite recurrence Operator | A |
| Period | R | recurrence temporal measure | A |
| Again | C | discourse-relative recurrence | F |

## Processes and change

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Change | R | explicit Attribute-setting Process | B |
| ChangeBy | D/R | delta Attribute Process | I |
| Move | R | spatial-change Process | B |
| Teleport | D/R | discontinuous Move | A |
| Join | R | Begin Joined structural Process | B |
| Separate | D/R | End Joined structural Process | I |
| Split | D/R | one structure -> multiple result identities Process | A |
| Merge | D/R | identity-forming fusion Process | A |
| Repair | R | integrity restoration Process | I |
| Create | R | fresh-identity Process | A |
| Destroy | D/R | EndExist Process | A |
| Transform | R | identity-preserving profile change | A |
| Cause | R | causal Event relation/control | A |
| Use | R | intentional instrument Process | I |
| Give | R | transfer Process | I |
| Get | D | BeginHave compression | I |
| Lose | D | EndHave compression | I |
| Open | R | artifact/state Process | I |
| Do | X | command mood makes generic Do unnecessary | — |
| Keep | D/C | maintain-state ordinary gloss; magic uses Persist | F |

## General relations / roles

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Have | R | possession/control state Relation | I |
| With | R/C | association Relation with typed frames | F |
| For | C/X | conversational umbrella; not generic magical relation | F |
| Purpose | R | intended goal/function Relation | I |
| DesignedFor | R | objective artifact-design Relation | I |
| Beneficiary | R | Event-beneficiary Relation | I |
| Using | R | instrument Relation | I |
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
| Density | R | scalar Attribute | A |
| Force | R | vector quantity/physical relation | I |
| Energy | R | scalar physical quantity | A |
| Pressure | R | scalar Attribute | A |
| Charge | R | signed scalar Attribute | A |
| Magnetic | R | field/interaction Property/Attribute | A |
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
| Grow | R | biological-development Process | I |
| Reproduce | R | biological fresh-result Process | A |
| Eat | R | biological consumption Process | F |
| Breathe | R | biological exchange Process | F |
| Disease | R | pathological state-predicate | I |
| Birth | D/R | BeginLife semantic molecule | I |
| Death | D/R | EndLife semantic molecule | I |
| Dead | D/R | FormerLife + NotLife profile | I |
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
| Think | R | mental Event Process | F |
| Know | R | factive state Relation | I |
| Believe | R | non-factive state Relation | F |
| Want | R | desire state Relation | F |
| Sense | R | information-acquisition Process | B |
| See | D/R | Vision Sense | I |
| Hear | D/R | Hearing Sense | I |
| TouchSense | D/R | contact Sense | I |
| Smell | D/R | chemical-air Sense | F |
| Taste | D/R | chemical-contact Sense | F |
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

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Information | R | informational Kind/domain | I |
| Sign | R | Information-bearing Kind | B |
| Meaning | R | Sign-content Relation | I |
| Word | R | lexical Sign Kind | F |
| Language | R | sign/grammar system Kind | F |
| Say | R | information-expression Process | I |
| Speak | D/R | Say via audible linguistic medium | F |
| Write | D/R | produce persistent Sign Process | I |
| Read | D/R | perceive+interpret Sign Process | I |
| Record | R | persistent Sign/Information Entity | I |
| Number | D/R | numeral Sign/Information Kind | F |
| NumericValue | R | numeral -> Quantity relation/function | I |
| Question | R | interrogative Information/speech act | F |
| Answer | R | response Information | F |
| Rule | R | conditional/normative Information Kind | A/F |
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
| Friend | R/C | social state Relation |
| Enemy | R/C | social state Relation |
| Owe | R | obligation Relation |
| Promise | R | commitment speech Process |
| Agree | R | proposition-linked social state/process |
| Ask | R | request/question Process |
| Tell | R | information-transfer Process |
| Teach | R | cause Know/Can Process |
| Learn | D/R | BeginKnow/Can |
| Work | C/R | goal-directed activity |
| Play | C | contextual activity |
| Love | R/C | mental/social state Relation |
| Hate | R/C | mental/social state Relation |
| Harm | D/R | cause Damage/adverse state |
| Disagree | D/R | proposition-linked disagreement |

## Magic-specific/control

| Gloss | Status | Category / role | Tier |
|---|---|---|---|
| Magic | R | active magical-state Property | I |
| Mana | R | scalar resource dimension/Attribute | B/I |
| Persist | R | active state-maintenance Operator | A |
| Trigger | R | conditional persistent control Operator | A |
| Repeat | R | finite recurrence Operator | A |
| Enchant | D/R | persistent Magic semantic molecule | A |
| Dispel | D/R | EndMagic semantic molecule | I/A |
| Atomic | D | future transaction/rollback Operator if supported | A |

## Canonical/world-specific noun families

The language is expected to contain many registered Kind roots beyond this core table.

Strong examples:

- Water
- Iron
- Stone
- Oak
- Wolf
- Hand

These are not required to reduce to a tiny semantic primitive inventory. Their recognition classifiers live in the world ontology.

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
