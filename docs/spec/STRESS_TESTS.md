# Semantic Stress Tests

_Status: ongoing regression suite_

These tests exercise the current specification against ordinary concepts and useful magical constructions. They are not a spell list. Their purpose is to expose missing semantics and prevent later changes from reintroducing ambiguity.

Notation is abstract when final surface syntax is not fixed.

## A. Basic lexical composition

### A1 — Red matter

`RedMatter`

Expected: valid restricted Kind/property construction.

Status: PASS.

### A2 — Liquid matter

`LiquidMatter`

Expected: all Matter satisfying Liquid, not Water.

Status: PASS.

### A3 — Ice-like Water

`SolidWater`

Expected: Water material Kind constrained by Solid Phase.

Status: PASS once Water is registered.

### A4 — Steam-like Water

`GasWater`

Expected: Water material Kind constrained by Gas Phase.

Status: PASS once Water is registered.

### A5 — contradictory homogeneous phase

`SolidLiquidMatter`

Expected: typeable constraints but contradictory for one homogeneous subject under single-valued Phase.

Status: PASS.

### A6 — negative two

`Opposite@@`

Expected: Quantity(-2), cost 3 semantic runes.

Status: PASS.

### A7 — compressed sixteen

`@@@@x@@@@`

Expected: Quantity(16), cost based on nine written semantic runes rather than expanded 16.

Status: PASS.

### A8 — after versus not-before

`OppositeBefore` vs `NotBefore`

Expected: After versus complement of Before.

Status: PASS.

## B. Color and light

### B1 — equal red/green chroma

`RedGreen`

Expected: equal included Red/Green chromatic components.

Status: PASS at semantic-family level.

### B2 — balanced RGB

`RedGreenBlue`

Expected: balanced chromatic profile, not automatically White.

Status: PASS.

### B3 — weighted red/green

Concept:

`ColorProfile(Ratio(Red=3,Green=5), intensity)`

Expected: normalized 3:5 channel relationship.

Status: PASS after COLOR_SYSTEM defined Ratio key/value syntax and ColorProfile construction.

### B4 — zero visible intensity

`ZeroLight`

Expected: measured Property generated from Light scalar attribute at zero.

Status: PASS.

### B5 — white/gray distinction

Expected: both can have balanced RGB ratio; intensity/range distinguishes them.

Status: PARTIAL. Exact registered intensity thresholds/profiles remain world/lexicon data.

## C. Spatial movement

### C1 — move selected object to activation origin

`!Move(This,Here).`

Expected: move referenced Entity to Here with ordinary continuous-path semantics.

Status: PASS if references resolve and destination is valid.

### C2 — teleport selected object to origin

`!Teleport(This,Here).`

Expected: endpoint relocation without continuous intermediate Path.

Status: PASS once Teleport semantic molecule is registered.

### C3 — push three length-units away from Self

Needed structure:

target position = current/reference position offset away from Self by distance q.

Status: PASS after SPACE_AND_GEOMETRY added `Offset(origin,direction,distance)` and typed Toward/AwayFrom direction constructors.

### C4 — pull toward Self by three units

Same gap as C3.

### C5 — nearest Wolf

Expected deterministic selection from a Collection by Distance.

Status: PASS after SELECTION_AND_REFERENCE defined Nearest as a tied Collection selector plus Unique for singular resolution.

### C6 — area within three units of Here

Can be represented by Ball(Here,3 units).

Status: PASS once Unit and Ball lexical items are registered.

## D. Attribute change

### D1 — heat Water by delta

`ChangeBy(water, Heat, q)`

Expected: increase/decrease Heat by typed quantity.

Status: PASS.

### D2 — set exact thermal value

`Change(water, Heat, q)`

Expected: target exact thermal attribute value.

Status: PASS.

### D3 — freeze Water

`Change(water, Phase, Solid)`

Expected: set Phase family value Solid.

Status: PASS after Phase was registered as an Attribute in ATTRIBUTES_AND_CHANGE.

### D4 — change color

`Change(target, Color, profile)`

Expected: change Color structured attribute.

Status: PASS after COLOR_SYSTEM defined ColorProfile/ColorOf and weighted profile syntax.

### D5 — change vague "size"

Expected: reject unless Size operation defines uniform scaling or explicit dimension.

Status: PASS as rejection.

## E. Creation, destruction, and transformation

### E1 — create a quantity of Water in a Ball region

Expected: Create a fresh Entity/profile with Water material Kind and explicit extent/location/amount.

Status: PASS in principle; profile construction syntax still needs final form.

### E2 — destroy existing object

`Destroy(This)`

Expected: End Exist(This), not merely Damage.

Status: PASS.

### E3 — create a generic Human from only Kind Human

Expected: usually underdetermined because Human does not uniquely specify Form and other creation-essential attributes.

Status: PASS as semantic-closure failure unless Human declares a canonical generation profile.

### E4 — transform Human to Wolf using only Kind Wolf

Expected: potentially underdetermined.

Status: PASS after the generation-profile/source-to-target mapping rule was added to KIND_AND_LEXICON_SYSTEM and MAGIC_EXECUTION.

### E5 — replacement versus transformation

Destroy A + Create EqualProfile B must not yield Same(A,B).

Status: PASS.

## F. Integrity and life

### F1 — repair damaged Sword

`Repair(sword, canonical-intact-Sword-profile)`

Expected: reduce Damage/restore Whole without changing identity.

Status: PASS.

### F2 — heal wound

Biological Repair against selected healthy/reference profile.

Status: PASS.

### F3 — kill living target

`End(Life(target))`

Expected: terminate Life, not Exist.

Status: PASS.

### F4 — resurrect intact corpse

`Begin(Life(corpse))`

Expected: possible only if biological requirements for Life are satisfiable.

Status: PASS semantically; capability/RequiredPower decides execution.

### F5 — resurrect badly damaged corpse

Likely needs Repair then BeginLife.

Status: PASS as Sequence requirement.

### F6 — Undead

Expected: must use setting-defined Kind/state, not OppositeLife.

Status: PASS as deliberate world-specific unresolved concept.

## G. Mind and information

### G1 — make target sleep

`Begin(Sleep(target))`

Status: PASS if Sleep is a state-predicate Property.

### G2 — wake target

`End(Sleep(target))`

Status: PASS.

### G3 — cause Fear of Self

`Begin(Fear(target,Self))`

Status: PASS once Fear is marked state-predicate Relation.

### G4 — forget a selected Memory

`End(Remember(target,memory))`

Status: PASS.

### G5 — insert false memory

Create Memory Information, then Begin Remember relation.

Status: PASS semantically; Mind-manipulation capability determines executability.

### G6 — direct knowledge

`Begin(Know(target,P))`

Expected valid only when P is true if Know is factive.

Status: PASS.

False content can produce Believe, not Know.

### G7 — read unknown rune

Sense can detect the Sign but Read requires Language/Meaning knowledge.

Status: PASS.

### G8 — ask reality a question

Question mood alone must not reveal hidden truth.

Status: PASS as rejection; requires Find/Reveal/Sense-like information acquisition.

## H. Collections and targeting

### H1 — all Humans in a Region

`Collect([h:Human], In($h,region))`

Expected Collection<Human>.

Status: PASS.

### H2 — apply Event to each

`Each(collection,[h],EventSpec($h))`

Expected explicit distributed composite.

Status: PASS.

### H3 — use Some(Human) as target

Expected invalid because existential quantifier does not select a witness.

Status: PASS as rejection.

### H4 — first/nearest/random member

Status: PASS after selector family specification (Unique, Nearest/Farthest, Highest/Lowest, First/Last, Random).

## I. Triggers and bindings

### I1 — trigger when any Human touches a specific object, affect that same Human

Naive:

`Trigger(Some([h:Human],Touch($h,object)), action($h))`

fails because existential Some does not export its witness.

Status: PASS after pattern-binding Trigger was added to MAGIC_EXECUTION.

### I2 — one-shot trigger

Expected default one-shot lifetime-bound Trigger.

Status: PASS.

### I3 — rearming trigger

Requires explicit rearm/repeat semantics.

Status: PASS as advanced construction.

### I4 — immediate self-triggering loop

A Trigger whose action recreates/fires itself at the same instant could create an infinite zero-time event chain.

Status: PASS after temporal well-foundedness / zero-time recursive-cycle rejection was added to MAGIC_EXECUTION.

## J. Persistence

### J1 — maintain silence in Region

Concept:

`Persist(Equal(Sound(region),Zero), duration)`

Status: PASS once Sound is scalar attribute over Region.

### J2 — maintain exclusion from Region

Concept:

`Persist(All([x:Kind],Not(In($x,region))),duration)`

Status: PASS semantically if quantifier scope is resolvable.

Execution may require continuous counteraction and Power.

### J3 — permanent persistence with omitted duration

Expected invalid; omission does not mean forever.

Status: PASS.

## K. Multi-action control

### K1 — two unordered changes

`And(E1,E2)`

Expected jointly realized composite with no order.

Status: PASS.

### K2 — ordered repair then revive

`Sequence(Repair(body,...),BeginLife(body))`

Status: PASS.

### K3 — failure in second sequence step

Expected first completed step remains; no free rollback.

Status: PASS.

### K4 — Or(E1,E2) command

Expected non-executable without branch-selection rule.

Status: PASS.

## L. Spell text and copying

### L1 — write a Command in a book

Quoted/recorded Command-content must not execute.

Status: PASS.

### L2 — copy written spell text

Information Copy duplicates content into a new Record.

Status: PASS.

### L3 — copy physical enchanted sword with Information Copy

Expected invalid.

Status: PASS as rejection.

Physical replication requires explicit Create/profile semantics.

## M. Artifact and Kind identity

### M1 — Water versus LiquidMatter

Status: PASS.

### M2 — Iron versus SolidMetalMatter

Status: PASS.

### M3 — Hand versus PartLifeMatter

Status: PASS.

### M4 — Sword versus "sharp metal"

Status: PASS.

Sword can use registered artifact classifier/design semantics.

### M5 — broken Sword remains Sword

Expected Kind membership can persist through Damage.

Status: PASS when Sword identity-essential constraints allow it.

## N. Time

### N1 — Yesterday

Calendar-relative interval semantic molecule.

Status: PASS conceptually.

### N2 — FormerLife versus NotLife

FormerLife requires historical Life; NotLife does not.

Status: PASS.

### N3 — Again

Generic Again depends on contextual previous-event matching.

Expected ordinary-language only unless matching rule supplied.

Status: PASS as magical restriction.

### N4 — periodic Repeat

Repeat needs count plus interval/Period when timing matters.

Status: PASS.

## O. Visibility and sensory interaction

### O1 — invisibility

Current system can describe Light and Sense but lacks a direct typed relation for whether observer receives visual information from target.

Status: PASS after `VisibleTo` was added to MIND_AND_INFORMATION with optional lower-level optical modeling.

### O2 — silence

Better covered through Sound attribute over Region.

Status: PASS.

## P. Regression findings

The first regression pass exposed eight concrete gaps:

1. Phase Attribute.
2. relative Location construction.
3. deterministic/tie-aware selectors.
4. Trigger witness binding.
5. zero-time recursion handling.
6. Create/Transform generation-profile closure.
7. observer-relative visibility.
8. weighted ColorProfile syntax.

All eight now have working specification-level resolutions.

The remaining open work found by these tests is primarily implementation/world-model detail (Units, exact thresholds, generation profiles, RequiredPower calibration), not missing core semantic architecture.

No stress test so far requires abandoning the typed architecture.
