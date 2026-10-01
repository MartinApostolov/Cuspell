# Candidate Rune Inventory Audit

_Status: historical first-pass audit against Semantic Type System v0.2; retained for rationale._

**Current vocabulary status is maintained in `LEXICON.md`; resolved semantics live in the newer domain specifications. Flags in this file describe the state at the time of the audit and must not be treated as current unresolved work.**

**Current minimization checkpoint:** the executable core is now **284 entries**, down from 306. Exact/convenience forms removed across the first two passes include After, Less, AtLeast, AtMost, EvidenceAgainst, NotDetected, Never, False, Claim, Lose, Destroy, Contain, Get, Join, Separate, Tell, See, Hear, Smell, Taste, ChangeBy, and Converse. Inside/Outside were explicitly retained after a detailed geometry check showed that they preserve stricter meanings than In/Not In.

The purpose of this audit was not to freeze the lexicon. It records what semantic machinery each candidate appeared to require and where English labels were hiding multiple meanings.

Legend:

- **OK** — fits current architecture directly.
- **F** — fits, but its frame/argument roles still need formalization.
- **X** — exposes missing machinery.
- **P** — likely polysemous/overloaded and must be resolved.
- **D** — likely derivable after dependencies are formalized.
- **C** — context-dependent; magical use needs an explicit standard/default.

## Reference / identity / category

| Rune | Tentative analysis | Flag |
|---|---|---|
| Thing | Kind; universal entity class | OK |
| Self | Reference<Entity>; caster | OK |
| You | Reference<Entity>; addressee/target resolution | F |
| This | Reference<T>; typed deictic reference | X |
| Other | identity exclusion operator/relation | X |
| Same | binary identity/equivalence Relation | OK |
| Kind | functional ontology relation/operator, Entity -> Kind | X |
| Part | structural Relation vs fractional/ratio operator conflict | P |
| Whole | structural completeness vs integrity-state usage | P |
| Person | Kind | OK |
| Body | Kind, Life/Matter | OK |
| Group | collection Kind | X |
| Name | informational functional relation and/or Sign Kind | P/X |
| People | collection of Person | D |
| OneOf | member-selection operator over collection/Kind | X |

## Logic

| Rune | Tentative analysis | Flag |
|---|---|---|
| Not | logical complement Operator | OK |
| Opposite | requires reversible mapping | OK |
| And | logical composition; predicates now, Propositions later | X |
| Or | same | X |
| If | Proposition/Command conditional | X |
| All | universal quantifier | X |
| Some | existential quantifier | X |
| Like | similarity Relation; dimensions/standard required | C/X |
| Because | causal/reason Relation over Events/Propositions | X |
| Can | modality/capability | X |
| Maybe | epistemic modality | X |
| True | Property of Proposition | X |
| Only | scope/focus Operator | X |
| False | likely complement of True | D/X |
| None | quantifier construction | D/X |
| Different | likely NotSame | D |
| Either | disjunction/selection semantics | X |
| Both | conjunction over two referents | X |

## Quantity / mathematics

| Rune | Tentative analysis | Flag |
|---|---|---|
| @ | Quantity 1 | OK |
| Zero | Quantity 0 | OK |
| Part | fraction/ratio use conflicts with structural Part | P |
| More | ordered Relation, reversible(Less) | OK |
| Less | OppositeMore | D |
| Equal | value equality; distinct from identity Same | F |
| Many | contextual count Property | C |
| Few | contextual count Property | C |
| Very | contextual scalar intensifier | C |
| Add | typed arithmetic Operator | F |
| Ratio | Quantity Operator | F |
| Sequence | ordered collection Kind | X |
| x / Multiply | arithmetic Operator | OK |
| Divide | arithmetic Operator | OK |
| Power | arithmetic Operator | OK |
| Root | arithmetic Operator | OK |

## Space

| Rune | Tentative analysis | Flag |
|---|---|---|
| Space | spatial Kind/domain | OK |
| At | Entity x Location Relation | F |
| To | directional Relation, reversible(From) | OK |
| In | containment Relation | OK |
| Up | directional Relation; needs reference frame, reversible(Down) | X |
| Near | distance Relation with contextual threshold | C |
| Touch | contact Relation | OK |
| Contain | converse of In | X |
| Side | functional geometry relation / feature Kind | X |
| Around | spatial Relation | F |
| Through | path Relation | F |
| Center | functional Region -> Location relation | X |
| Edge | functional object/region -> boundary relation | X |
| Surface | feature Kind plus surface-of relation | P/X |
| From | OppositeTo | D |
| Down | OppositeUp | D |
| Far | opposite end of distance scale only after scale definition | C/D |
| Across | path/topology Relation | F |
| Inside | likely specialized In | D |
| Outside | must not be automatic OppositeIn | F |
| Here | Reference<Location> | OK |

## Time

| Rune | Tentative analysis | Flag |
|---|---|---|
| Time | temporal domain/measurement Kind | F |
| Before | temporal Relation, reversible(After) | OK |
| During | Event x interval Relation | X |
| Start | event boundary vs begin Process ambiguity | P |
| Moment | temporal-point Kind | OK |
| Again | recurrence Operator over Event/Process | X |
| End | event boundary vs termination Process ambiguity | P |
| After | OppositeBefore | D |
| Now | Reference<Time> | OK |
| Duration | functional Event -> Quantity[Time] | X |
| Always | temporal quantification | X |
| Never | temporal quantification | X |

## Actions / change

| Rune | Tentative analysis | Flag |
|---|---|---|
| Do | generic Process/execution semantics unclear | X |
| Happen | occurrence Process/Event construction | X |
| Make | Process: agent/patient/result or causation | F |
| End | termination Process | F/P |
| Change | target + old/new value/property Process | F |
| Move | mover/source/destination/path Process | F |
| Join | structural Process | F |
| Keep | maintain State/Relation Process | F |
| Begin | begin State/Process/Event | F |
| Cause | Event/Process causal construction | X |
| Use | agent/instrument/goal Process | F |
| Give | transfer Process | F |
| Get | acquisition Process | F |
| Open | state-changing Process on openable target | F |
| Separate | potential OppositeJoin | D/F |
| Stop | specialized End of Process/Event | D |
| Take | role-rearranged transfer construction | D/X |
| Lose | termination of Have Relation | D/X |
| Break | integrity-damage Process | D |
| Repair | restore integrity/reduce Damage | D |
| Create | Begin existence | X |
| Destroy | End existence | X |

## Relations / semantic roles

| Rune | Tentative analysis | Flag |
|---|---|---|
| With | association Relation | F |
| Have | possession/control Relation | F |
| For | purpose/beneficiary Relation | F |
| Of | dangerously broad English relation; must split or tightly type | P/X |
| By | agency/instrument/means overloaded | P |
| Using | instrument Relation | F |
| About | information-topic Relation | F |
| Against | opposition Relation; domain-sensitive | F |
| Among | collection Relation | X |
| Exchange | semantically a transfer Process, not generic Relation | P |
| Without | likely NotWith | D |
| Mine | Self-linked Have construction | D/X |

## Matter / physics

| Rune | Tentative analysis | Flag |
|---|---|---|
| Matter | Kind | OK |
| Solid | Phase Property | OK |
| Liquid | Phase Property | OK |
| Gas | Phase Property | OK |
| Force | vector physical Property/quantity | X |
| Energy | scalar physical dimension | X |
| Plasma | Phase Property | OK |
| Mass | scalar dimension | X |
| Density | scalar dimension | X |
| Hard | material scalar Property | F |
| Flexible | material scalar Property | F |
| Brittle | material scalar Property | F |
| Sharp | geometry scalar Property | F |
| Smooth | surface scalar Property | F |
| Pressure | scalar dimension | X |
| Charge | signed scalar dimension | X |
| Magnetic | field/vector Property | X |
| Chemical | label too broad; Kind/Property distinction unresolved | P |
| Element | Matter Kind | OK |
| Atom | Matter Kind | OK |
| Molecule | Matter Kind | OK |
| Metal | Matter Kind/class | OK |
| Organic | material/biological classification unresolved | P |
| Soft | low/inverse Hard region if axis defined | D |
| Rough | inverse/low Smooth region if axis defined | D |

## Temperature

| Rune | Tentative analysis | Flag |
|---|---|---|
| Heat | scalar thermal Property | OK/X |
| Temperature | possibly overlaps Heat | P |
| Cold | low Heat region | D/C |
| Hot | high Heat region | D/C |
| HeatChange | Change specialized to Heat | D |

## Light / color

| Rune | Tentative analysis | Flag |
|---|---|---|
| Light | scalar perceptual/physical Property | OK |
| Red | Color channel Property | OK |
| Green | Color channel Property | OK |
| Blue | Color channel Property | OK |
| Transparent | optical scalar Property | F |
| Reflect | Process vs reflective Property conflict | P |
| Opaque | low/zero transparency | D |
| Yellow | RedGreen color blend | D |
| Cyan | GreenBlue blend | D |
| Magenta | RedBlue blend | D |
| White | balanced RGB + high intensity; exact definition needed | D/F |
| Gray | balanced RGB + lower intensity | D/F |
| Black | leading model ZeroLight | D |
| Bright | high Light range; contextual unless fixed | C/D |
| Dark | low Light range; contextual unless fixed | C/D |
| Glow | emit-Light Process/Property distinction | P/F |

## Waves / sound

| Rune | Tentative analysis | Flag |
|---|---|---|
| Sound | perceptual phenomenon/stimulus Property | F |
| Vibration | Process vs state/property distinction | P |
| Frequency | scalar inverse-Time dimension | X |
| Wave | phenomenon Kind vs propagation Process | P |
| Loud | high Sound magnitude | C/D |
| Quiet | low Sound magnitude | C/D |

## Form / geometry

| Rune | Tentative analysis | Flag |
|---|---|---|
| Form | geometric value/property vs Kind issue | P |
| Size | aggregate scalar concept; dimensions unclear | X |
| Length | scalar dimension | X |
| Point | geometric Kind | OK |
| Line | geometric Kind | OK |
| Surface | Kind plus functional relation | P |
| Width | Length relative to orientation | X |
| Volume | scalar amount of space vs 3D region Kind | P |
| Angle | scalar angular dimension | X |
| Round | geometric Property | F |
| Flat | geometric Property | F |
| Straight | geometric Property | F |
| Curve | Property vs curve-object Kind | P |
| Center | functional Relation | X |
| Edge | functional Relation | X |
| Hole | topological feature relative to host | X |
| Symmetry | geometric Property, possibly parameterized | F |
| Height | Length measured along Up frame | D/X |

## Integrity

| Rune | Tentative analysis | Flag |
|---|---|---|
| Whole | completeness/integrity Property and structural whole relation | P |
| Damage | scalar/state integrity loss | F |
| Broken | severe structural Damage / NotWhole | D |
| Repair | restore Whole/reduce Damage | D/F |
| Cut | separation/damage Process | D/F |
| Crush | compression/deformation Damage Process | D/F |
| Burn | thermal/chemical Damage Process | D/F |
| Wound | Damage specialized to living target | D/P |
| Heal | Repair specialized to Life | D |

## Life

| Rune | Tentative analysis | Flag |
|---|---|---|
| Life | biological state Property | OK |
| Grow | biological development/size Process | F |
| Reproduce | Life Process producing new organism | F |
| Eat | Life Process | F |
| Breathe | Life/material-exchange Process | F |
| Plant | Life Kind | OK |
| Animal | Life Kind | OK |
| Human | Life/Mind Kind | OK |
| Disease | diseased state vs disease Kind/type | P |
| Blood | Life/Matter Kind | OK |
| Poison | functionally/causally defined Matter Kind | X |
| Birth | BeginLife | D |
| Death | EndLife | D |
| Dead | FormerLife + NotLife | D/X |
| Undead | no objective semantic definition yet | X |

## Mind

| Rune | Tentative analysis | Flag |
|---|---|---|
| Mind | mental-system Kind | OK |
| Think | Process with thinker/content | F |
| Know | state/relation to Information or Proposition | X |
| Want | state/relation to desired entity/event/state | X |
| Feel | overly broad state/process | P |
| Sense | perception Process with channel frame | F |
| Remember | mind-information state/relation | X |
| Sleep | Life/Mind state Property | F |
| Dream | mental Event/content | X |
| Pain | perceptual/mental state Property | F |
| Fear | experiencer-target state/relation | F |
| Attention | mind-target relation, perhaps scalar | F |
| Believe | mind-Proposition state/relation | X |
| Smell | specialized Sense channel | D/F |
| Taste | specialized Sense channel | D/F |
| Forget | change/end Remember | D/X |
| See | LightSense | D |
| Hear | SoundSense | D |
| TouchSense | contact Sense channel | D/X |

## Information / language

| Rune | Tentative analysis | Flag |
|---|---|---|
| Sign | Information-bearing Kind | OK |
| Say | information-expression Process | F |
| Meaning | functional/semantic Sign -> Information relation | X |
| Word | linguistic Sign Kind | OK |
| Language | structured Sign-system Kind | OK |
| Question | interrogative Proposition/Information structure | X |
| Answer | response tied to Question | X |
| True | Proposition Property | X |
| Name | Sign Kind / functional naming Relation conflict | P |
| Rule | normative/conditional Information structure | X |
| Command | grammar-level executable Information object | X |
| Record | persistent Sign/Information Kind | F |
| Memory | information object vs remembered mental state | P |
| Number | Sign/Information representing Quantity | D/F |
| Write | produce persistent Sign | D/F |
| Read | Sense + interpret Sign Meaning | D/F |
| Speak | Say via Sound Sign | D |
| HearSpeech | Hear + interpret linguistic Sign | D |
| False | complement of True | D/X |

## Purpose / tools

| Rune | Tentative analysis | Flag |
|---|---|---|
| For | purpose Relation | F |
| Use | instrument/goal Process | F |
| Tool | purpose-defined Kind | X |
| Weapon | damage-purpose Tool Kind | D/X |
| Container | containment-purpose Kind | D/X |
| House | complex structure/purpose semantic molecule | D/X |
| Door | boundary/passage-function semantic molecule | D/X |
| Sword | geometry/material/purpose semantic molecule | D/X |
| Clothing | worn-covering purpose Kind | D/X |
| Food | Life-support/eating purpose Kind | D/X |
| Medicine | therapeutic purpose Kind | D/X |

## Social / ordinary language

| Rune | Tentative analysis | Flag |
|---|---|---|
| Good | evaluator/standard-dependent Property | C |
| Bad | evaluator/standard-dependent Property | C |
| Help | Process advancing another goal/state | F |
| Friend | social Relation/state | F |
| Enemy | social Relation/state | F |
| Give | transfer Process | F |
| Have | possession Relation | F |
| Owe | obligation Relation | F |
| Promise | creates commitment from Information/social act | X |
| Agree | relation/process to Proposition/content | X |
| Tell | information-transfer/expression Process | F |
| Teach | cause another to Know/Can | X |
| Learn | Begin/Change Know/Can | X |
| Work | broad goal-directed Process | C/F |
| Play | strongly contextual social Process | C |
| Love | mental/social Relation/state | F |
| Hate | mental/social Relation/state | F |
| Harm | cause Damage/negative state | D |
| Disagree | Proposition-linked relation/process | D/X |

These may be legitimate ordinary-language roots even when they are unsuitable for objective magical execution without explicit parameters.

## Magic-specific / advanced

| Rune | Tentative analysis | Flag |
|---|---|---|
| Magic | magical state/effect Kind/Property distinction unresolved | P |
| Mana | scalar resource dimension | X |
| x / Multiply | Quantity Operator | OK |
| Persist | extend State/Event/Effect through Time | X |
| Trigger | condition -> Command activation | X |
| Repeat | Event/Command repetition, likely Quantity-bound | X |
| Copy | duplicate Entity/value/effect; semantics vary by target type | P/X |

Derived candidates remain promising:

- Dispel = EndMagic, once Magic is an endable state/effect.
- Range = distance quantity.
- Duration = time quantity.
- Area = spatial extent.
- Transform = Change.
- Summon = Move target to a location.
- Teleport = specialized Move with path semantics.
- Enchant = persistent Magic associated with a Thing.


Current minimization note: the earlier audit candidates `Between`, `Ask`, `TimeOverlap`, `AwayFrom`, and `DirectPart` have since been removed from the registered base inventory. `Duration` has also since been removed as a standalone root: concrete Event duration is the Time-valued `Extent(Event)` frame. Their executable meanings are expressed by ordered comparison composition, `Say` carrying `QuestionContent`, the general typed `Overlap` relation, `Opposite Toward`, and `Part` plus an explicit no-intermediate-part condition respectively.

## Main audit conclusions

The eight lexical categories broadly survive the full inventory.

The inventory primarily demands reusable mechanisms rather than many new top-level types:

- typed references;
- dimensional quantities;
- functional relations;
- collections and quantification;
- Proposition semantics;
- Event semantics;
- contextual comparison standards;
- generalized Sense channels;
- relationally defined Kinds;
- existence semantics;
- converse relations.

Highest-priority roots for semantic cleanup:

1. Part
2. Whole
3. Kind
4. Of
5. By
6. End
7. Start / Begin
8. Form
9. Surface
10. Volume
11. Magic
12. Copy
13. Disease
14. Memory
15. Name

The audit result is extension, not replacement, of the current semantic architecture.


Current minimization note: the former `Information` Kind candidate has since been removed because Information is already an abstract semantic type. `Former` is also removed in favor of `Past P And Not Present P`, and `KnowAnswer` is expressed through existential `Know + AnswerFor`.
