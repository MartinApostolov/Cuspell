# Yona Corpus — Chapter 47 Mana-System Pass

_Status: first pass against current Cuspell, 2026-09-27_

_Source: Yona [Cat Girl Evolution], Bedivere the Mad, Chapter 47 "How Mana Works"_
_Source URL: https://www.royalroad.com/fiction/129180/cat-girl-evolution-book-1-complete/chapter/2745177/47-how-mana-works_

This chapter was chosen because it explains another fictional magic system in detail. The goal is to test whether Cuspell can describe a foreign magic ontology rather than only its own spell semantics.

## HMW-01 — choice between two learnable skills

Source meaning: the protagonist is offered a choice of which of two Skills to learn first and changes her preference before deciding.

Current status: **PASS-LONG / LEXICON / WORLD**.

Or/collection choice, Prefer, Intend, Sequence, and Change-like state transitions are enough structurally. Skill/Learn and the named abilities are world vocabulary.

## HMW-02 — mana properties depend on mana attribute/type

Source meaning: different mana types have characteristic values for stability, volatility, flow, resilience, potency, and related properties.

Current status: **PASS-LONG / LEXICON / WORLD**.

The scalar Attribute system is already generic enough for these to be registered as AttributeDescriptors returning typed ordered values. Generic/All can describe type-level regularities. No new expression grammar is required.

## HMW-03 — comparative property strengths

Source meaning: one mana type has more volatility, another has more resilience, and so on.

Current status: **PASS once scalar property descriptors exist**.

More/Less work for compatible Quantities. The missing pieces are the property descriptors and their value domains/Units, not comparison grammar.

## HMW-04 — a specialist focuses on several properties

Source meaning: a barrier specialist trains/uses stability and resilience, while construct use also emphasizes flexibility.

Current status: **PASS-LONG / LEXICON / WORLD**.

Have/Can/ImportantTo plus Skill/world relations can represent the association. Training/focus vocabulary would improve compactness.

## HMW-05 — form a geometric mana construct

Source meaning: mana is shaped into a circular barrier-like construct in space.

Current status: **PASS architecture / WORLD**, with the Chapter 14 field gap.

Form/ShapeLike, Region/geometry, Change, and resource quantities cover much of the meaning. Exact spatial resource distribution is still not first-class.

## HMW-06 — thinner object with much more mana

Source meaning: one barrier is much thinner than another while containing roughly three times as much mana.

Current status: **PASS-LONG / LEXICON / WORLD**.

Typed arithmetic, Multiply, measurement Units, More/Less, and ApproxEqual are sufficient if Thickness/Amount-of-Mana attributes are registered.

## HMW-07 — increase potency without adding more mana

Source meaning: strength/potency of the mana already present increases while total mana amount is held fixed.

Current status: **PASS architecture / LEXICON**.

This maps naturally to Change(Potency) plus Preserve(ManaAmount). This is strong confirmation that Preserve generalizes beyond Chapter 14 density/volume examples.

## HMW-08 — analogy used to explain a difficult concept

Source meaning: a teacher uses a fire/air analogy to explain a mana-property change.

Current status: **STYLE/PRAGMATICS**, not a core semantic blocker.

Cuspell can state both source and target propositions, but a first-class analogy/metaphor relation is optional if style preservation becomes a goal.

## HMW-09 — repeated effort causes sudden acquisition of a Skill

Source meaning: after trying to change a mana property, the protagonist reaches a threshold and acquires a new Skill.

Current status: **PASS architecture / WORLD**.

Trigger, Begin/Change, Happen, and capability relations support the event structure. Skill/proficiency thresholds belong in world data.

## HMW-10 — one Skill supports many strategic uses

Source meaning: the same barrier capability can protect, lift, obstruct, redirect enemies, and otherwise be used in different plans.

Current status: **PASS-LONG / LEXICON / WORLD**.

Can plus EventSpecs and MethodFor can describe alternative uses. No new core grammar is exposed.

## HMW-11 — stable versus volatile attacks defined by temporal behavior

Source meaning: stability is diagnosed by persistence of shape/signature during travel, while volatility involves change/fluctuation and emission.

Current status: **RATE/TREND GAP + LEXICON**.

A Stability scalar can be lexicalized, but the explanatory definition itself repeatedly needs Stable/Increasing/Decreasing/Fluctuating over an interval. This reinforces the generic trend/value-function gap already seen in Chapters 1 and 14.

## HMW-12 — damage composition/proportion

Source meaning: an attack's damage is described as entirely one damage mode rather than another.

Current status: **LEXICON / RATIO GAP**.

The written spec has a Ratio concept, but Ratio is not currently executable in the reference lexicon. This chapter provides a concrete ordinary-language reason to finish it.

## HMW-13 — forbidden action versus recommendation not to do it

Source meaning: a class of dangerous spells is formally forbidden; separately, speakers recommend that the protagonist not experiment with them.

Current status:
- formal prohibition: **PASS** via Not(Permitted(...)) / obligation-like semantics;
- recommendation/advice: **GRAMMAR/MODALITY GAP**.

Obligated is too strong for ordinary "should/recommend". Chapter 1 already hinted at this. A Recommendation/Advisable/Should-strength modality is still useful.

## HMW-14 — reported rumor with uncertain truth

Source meaning: a speaker reports second-hand information about a past catastrophic spell without asserting direct knowledge.

Current status: **PASS-LONG**.

Assert/Claim, Believe, EvidenceFor, PossibleTo/ProbableTo, and source attribution are now adequate. Durable named references remain a discourse issue.

## HMW-15 — cause of destruction described as transformation rather than explosion

Source meaning: a spatial effect warps/splices structures, producing destruction by a particular mechanism.

Current status: **LEXICON / WORLD**.

Event structure, Change/Form, Part/Separate, Destroy, and causal relations are sufficient in principle. Spatial-magic physics is setting ontology.

## HMW-16 — innate affinity restricts future capability

Source meaning: characters possess an innate Trait that grants unusually high performance in one area while excluding other affinities.

Current status: **WORLD / LEXICON**, with prerequisite/enabling semantics useful.

Kinds/Properties, Have, Can, Not, and comparisons are adequate. The exact unlock/exclusion rules belong to the world package.

## HMW-17 — strongest-at-level / exceptional comparative claim

Source meaning: characters claim they are probably among the strongest specialists at their current level.

Current status: **PASS-LONG / LEXICON**, with ordered evaluation/scalar-model requirements.

Highest can reduce a collection by a scalar Attribute. The remaining work is defining the relevant capability/performance scalar and discourse comparison set.

## HMW-18 — slower progression improves future option quality

Source meaning: spending longer mastering a Class is claimed to improve the probability/quality of later upgrade options.

Current status: **PASS-LONG / WORLD**, with ordered evaluation still relevant.

Probability/confidence and temporal relations exist. "Better option quality" still requires a defined ordered Evaluation/quality scale.

## HMW-19 — volatile construct has limited lifetime/range

Source meaning: a volatile projectile becomes unstable and explodes after enough travel/time unless improved.

Current status: **PASS-LONG / LEXICON / WORLD**.

If/When, Duration, Distance, Change, Trigger, and event boundaries are adequate. Instability/explosion/range vocabulary is missing.

## HMW-20 — conditional loss of control

Source meaning: the protagonist adds potency until she judges the object near the limit of what she can control, then throws it before failure.

Current status: **PASS-LONG**, with generic Almost/threshold semantics still useful.

Can/Control, Intend, Change, and Event ordering handle the core. "Near my control limit" is another near-threshold case.

## HMW-21 — visible inexperience inferred by knowledgeable observers

Source meaning: experienced people infer that the protagonist is new to a Class from observable behavior.

Current status: **PASS-LONG / LEXICON**.

EvidenceFor plus Believe/Know and proficiency vocabulary is sufficient.

## HMW-22 — advice to use a capability for everything

Source meaning: teachers recommend frequent broad use of constructs to improve mastery.

Current status: **MODALITY GAP / WORLD**.

Habitual and Repeat can describe the behavior, but advice/recommendation is weaker than obligation and stronger than mere preference. This reinforces HMW-13.

## HMW-23 — body-like constructs used as substitute limbs

Source meaning: the protagonist creates temporary mana limbs, changes their geometry, anchors them to a platform, and uses them for locomotion.

Current status: **PASS architecture / LEXICON / WORLD**, with spatial fields still relevant.

ShapeLike, Joined, Control, Move, Form/Change, and anatomy/world vocabulary fit the structure. Chapter 14's field/distribution issue remains for the mana material itself.

## HMW-24 — covert communication channel

Source meaning: two people exchange information without ordinary audible speech, and the protagonist infers this from behavior/mana use.

Current status: **PASS architecture / LEXICON**.

Information transfer and EvidenceFor are sufficient; Telepathy/CommunicationChannel is vocabulary.

## HMW-25 — persistent construct versus dispelling/reabsorbing

Source meaning: the protagonist considers leaving a mana construction active, then later dispersing it and returning the mana to an internal reserve.

Current status: **PASS-LONG / WORLD**, with Transfer/Flow useful.

Persist handles active maintained states/events; Transfer would make resource movement cleaner.

## Chapter 47 findings

This chapter is a strong result for the current architecture: a foreign magic system with detailed property interactions does **not** force a new basic grammar.

Most of the chapter needs:

- new scalar AttributeDescriptors (Stability, Volatility, Potency, Flow, Resilience, Flexibility, etc.);
- world ontology for Skills, Affinities, Classes, proficiency, spells, and mana physics;
- ordinary action vocabulary.

The structural findings are concentrated in a small set already seen elsewhere:

1. generic Rate/Trend/Fluctuation semantics;
2. ordered subjective/quality evaluation;
3. recommendation/advice modality weaker than obligation;
4. generic near-threshold Almost;
5. prerequisite/enabling relations;
6. spatial resource Fields/Distributions;
7. reusable Transfer/Flow;
8. executable Ratio.

This convergence is important: Chapter 47 mostly **repeats** gaps found by Chapters 1/14 instead of uncovering an entirely new semantic architecture.
