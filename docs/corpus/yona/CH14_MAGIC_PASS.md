# Yona Corpus Pilot — Chapter 14 Magic Pass

_Source: Yona [Cat Girl Evolution], Bedivere the Mad, Chapter 14 "External Mana Manipulation"_
_Source URL: https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2540191/14-external-mana-manipulation_

This pass deliberately targets mana manipulation, shaped constructs, body-like structures, measurement, perception, and skill progression rather than translating the whole chapter.

Primary source region is roughly Royal Road reader lines 135–143 and 221–234 at the time of analysis.

## M01 — sensing mana as a dedicated channel

Source meaning: the protagonist can perceive ambient/internal mana after entering an appropriate mental state.

Finding: SenseChannel architecture handles this cleanly. The world package can register ManaSense with stimulus domain ManaField/ManaDistribution.

Status: PASS architecture / WORLD.

## M02 — moving mana out of the body

Source meaning: some mana resource/distribution is transferred from inside the body to an external region.

Finding: current Cuspell treats Mana mainly as a scalar resource dimension. This story uses mana as a spatially distributed substance/field as well.

Status: WORLD-MODEL GAP, not core grammar failure.

Required world extension: distinguish ManaAmount from ManaDistribution/ManaField/portion entities so Move and Density can apply spatially.

## M03 — shaping external mana into a spoon

Source meaning: external mana is given the geometry/form of a spoon-like object.

Finding: Form/GeometryProfile and Change can express the geometry. However "spoon-shaped" must not imply the result is a canonical Spoon artifact Kind unless its material/design/function classifier is satisfied.

Status: PASS architecture.

This strongly validates the earlier distinction between Form and Kind.

## M04 — keeping a construct manifested

Source meaning: the mana form continues existing while attention shifts elsewhere.

Finding: the story-specific ability may supply automatic persistence. Cuspell can describe the state with Exist plus world-specific ManaConstruct rules or explicit Persist if the effect would otherwise dissipate.

Status: PASS architecture / WORLD.

## M05 — spoon to partial hand transformation

Source meaning: the same mana construct changes Form from spoon-like to an incomplete hand-like geometry.

Finding: Transform/Change Form preserves Entity identity while geometry changes. The construct can be hand-shaped without InstanceOf(Hand).

Status: PASS.

## M06 — incomplete anatomical structure

Source meaning: the construct has fewer digits than a normal hand and a rough/lumpy shape.

Finding: canonical Hand profile plus Part/Count/Form allows objective comparison to a real Hand without forcing Kind membership.

Status: PASS-LONG.

## M07 — bending fingers under control

Source meaning: the protagonist can intentionally change joint/segment geometry of the construct.

Finding: Cuspell lacks an explicit Control relation tying an agent to manipulation of another Entity/Process.

Status: LEXICON.

A Control(agent,target/process) state Relation is broadly useful for both language and magic.

## M08 — low tactile interaction despite visible form

Source meaning: the construct affects fur only weakly, producing an effect like light airflow rather than firm contact.

Finding: visual Form does not imply mechanical Force/contact. Force, Touch, and Sense already separate these channels.

Status: PASS.

This is another strong validation of not defining artifact/anatomical Kind from appearance alone.

## M09 — increasing density while preserving size

Source meaning: mana is added so density increases while the construct retains its prior size.

Finding: Cuspell can set Density, but "keep the old Size/Volume value unchanged" needs a compact way to refer to a pre-event value or declare an invariant.

Status: CUSPELL-DEFECT / GRAMMAR.

Required resolution: snapshot/pre-state value references and Preserve constraints.

## M10 — twice the previous density

Source meaning: density becomes two times the value it had before the change.

Finding: arithmetic can express multiplication, but it needs OldValue/BeforeValue(attribute, subject, event) to reference the previous state.

Status: GRAMMAR.

## M11 — approximately ten times starting density

Source meaning: later density is near ten times the initial value.

Finding: Multiply works, but the chapter stresses both reference-state selection and approximate/tolerance language.

Status: GRAMMAR / LEXICON.

Near-threshold/tolerance work from Chapter 1 should generalize to ApproxEqual/WithinTolerance.

## M12 — redistributing mana from center to edges

Source meaning: material/resource is moved internally so the center becomes mostly empty while boundary regions become denser.

Finding: Cuspell has Center/Surface/Edge, Region, Density, and Move, but lacks a general spatial field/distribution value connecting amount per subregion.

Status: WORLD/SEMANTIC GAP.

Required extension: Distribution<Field/Material> over Region with integrals/amount conservation rules supplied by world physics.

## M13 — hollow structure

Source meaning: the mana object becomes mostly hollow while maintaining an outer hand-like shape.

Finding: Form/Region/mereology can describe a shell, but a canonical Hollow geometry predicate/profile would be useful.

Status: PASS-LONG / LEXICON.

## M14 — real-hand-like feel without real Hand Kind

Source meaning: optimized force/density distribution makes the construct feel similar to a real hand.

Finding: similarity must specify dimensions: tactile interaction/Force profile may be Like a Hand while material Kind and anatomical Kind remain different.

Status: PASS-LONG.

This validates typed similarity dimensions.

## M15 — shape-like versus identity

Source meaning: a later construct looks like a hand but can bend in anatomically impossible ways because it is effectively a flexible mana shape, not a biological hand.

Finding: Cuspell's Kind/Form split is exactly what this needs.

Status: PASS.

A useful relation is SimilarFormTo/ShapeLike rather than generic Like.

## M16 — adding joints

Source meaning: the protagonist explicitly builds internal joint structures so the construct moves more like a biological hand.

Finding: Part, DirectPart, Joined, Form, and anatomical Kind profiles cover this.

Status: PASS-LONG.

## M17 — separate pieces versus connected pieces

Source meaning: two construct components can touch without being structurally connected.

Finding: the existing distinction Touch(A,B) versus Joined(A,B) passes perfectly.

Status: PASS.

This is a particularly strong corpus confirmation of STRUCTURE_AND_MEREOLOGY.

## M18 — component separation causing loss of control/disintegration

Source meaning: once a mana component separates from the controlled construct, control is lost and the component disperses into ambient mana.

Finding: requires world rules connecting Control/Joined/Exist and ManaDistribution, but no new sentence grammar.

Status: WORLD / LEXICON.

## M19 — maintaining multiple manifested parts

Source meaning: the protagonist learns to sustain several mana objects/components simultaneously while concentrating mainly on one.

Finding: collections plus Each/And can represent multiple objects, but cognitive allocation suggests a scalar Attention/ControlLoad world Attribute.

Status: PASS architecture / WORLD.

## M20 — resource cost of sustained constructs

Source meaning: maintaining/building the structure consumes a large amount of mana.

Finding: Mana resource Quantity plus Process cost can express this. This is directly relevant to Cuspell's own execution layer, though the novel's cost formula is story-specific.

Status: PASS architecture / WORLD.

## M21 — sensing different mana density in air and meat

Source meaning: mana is perceived in multiple media, with a higher local density in one than another.

Finding: ManaSense plus Density and More works once the world package represents mana spatially.

Status: PASS after world extension.

## M22 — absorbing mana by eating

Source meaning: consuming matter transfers/absorbs mana into the protagonist's internal reserve.

Finding: Eat plus resource transfer can express this. A resource Flow/Transfer Process may be useful as a generic semantic molecule.

Status: PASS-LONG / LEXICON.

## M23 — increasingly efficient mana digestion

Source meaning: the conversion/absorption rate has improved over time.

Finding: ChangeRate/Increasing from the prose pass handles this naturally.

Status: PASS.

## M24 — passive perception after repeated use

Source meaning: a Sense capability that previously required an active mental Process becomes available passively after training.

Finding: Can/Begin(Can(...)), SenseChannel, and capability profiles can represent this. Skill progression itself is world/game data.

Status: PASS architecture / WORLD.

## M25 — skill proficiency thresholds

Source meaning: repeated successful use changes a skill's proficiency category, which unlocks improved control.

Finding: this is a world Attribute/family similar to Phase: Proficiency(skill) -> proficiency value. It does not require new core grammar.

Status: WORLD.

## Magic-pass architecture findings

The magic-heavy chapter is encouraging: most constructions fit the semantic architecture better than the ordinary prose did.

It exposes four particularly useful additions:

1. **Pre-state/snapshot references** such as OldValue/BeforeValue are needed for relative changes like "twice as dense while staying the same size."
2. **Preserve/invariant constraints** are needed during Change/Transform.
3. **Spatial resource distributions/fields** are needed for quantities such as mana density varying across a Region.
4. **Control** should be a first-class state Relation distinct from Have, Use, and magic Command issuance.

It also strongly confirms several prior design choices:

- Form is not Kind.
- Touch is not Joined.
- Part structure matters.
- Density and Force are separate from visible geometry.
- Sense channels generalize well to fantasy senses.
- Rate/trend semantics are useful in magical training descriptions.
