# Yona Corpus — Chapter 2 Current Pass

_Status: first pass against current Cuspell, 2026-09-27_

_Source: Yona [Cat Girl Evolution], Bedivere the Mad, Chapter 2 "A Little Adventure"_
_Source URL: https://www.royalroad.com/fiction/129180/cat-girl-evolution-book-1-complete/chapter/2525481/2-a-little-adventure_

This pass is intentionally sequential after Chapter 1. Its main purpose is to test whether discourse referents introduced in Chapter 1 can survive into a new chapter and whether the existing event/epistemic machinery handles ordinary adventure prose.

## C2-01 — boarding while others prepare to depart

Source meaning: while the fishermen prepare to leave, the narrator runs onto their ship.

Current status: **PASS-LONG / LEXICON**.

Concurrent/During plus Move/At can express the event structure. Ship/fisherman/depart are ordinary vocabulary gaps.

## C2-02 — attempted capture and evasive movement

Source meaning: a fisherman attempts to grab the narrator; she avoids him and climbs the mast.

Current status: **PASS-LONG / LEXICON**.

Sequence/Concurrent and movement work. Grab, Dodge, Climb, Mast are lexicon.

## C2-03 — previously introduced person calling the narrator

Source meaning: a woman already known from Chapter 1 calls to Yona.

Current status: **DISCOURSE**.

The speech event is representable, but resolving "the wife"/Sally from prior-chapter discourse is not yet formalized.

## C2-04 — animal utterance carries intended content

Source meaning: the narrator produces a cat vocalization intended to mean refusal.

Current status: **LEXICON / SEMANTIC MOLECULE**.

Assert/Claim can preserve communicated proposition content, but a reusable Sign/Meaning or utterance-channel relation is not executable.

## C2-05 — new person introduction with name, profession, appearance, and inferred history

Source meaning: an older fisherman is introduced by name, described physically/socially, and the narrator tentatively infers a former profession.

Current status: **DISCOURSE / LEXICON**, with epistemic core **PASS**.

Believe/PossibleTo handles the tentative inference. Proper-name introduction and durable definite reference remain missing.

## C2-06 — order/command speech act

Source meaning: the senior fisherman tells another fisherman to stop trying to retrieve the cat and continue departure.

Current status: **PASS-LONG / LEXICON**.

The content can be represented as an asserted obligation/event requirement. A compact speech-act root for Command/Order would shorten it but is not required by the type system.

## C2-07 — multiple simultaneous preparations

Source meaning: crew members perform several preparation actions concurrently while the ship departs.

Current status: **PASS-LONG / LEXICON**.

Concurrent/Sequence/Each can represent the structure. Most missing pieces are maritime vocabulary.

## C2-08 — observing weapons leads to concern about future combat

Source meaning: the narrator notices that most crew members are armed and treats that Information as evidence that monster combat may occur.

Current status: **PASS-LONG / LEXICON**.

Most, EvidenceFor, Believe/PossibleTo, and future EventSpecs provide the needed architecture. Perception roots and weapon/monster vocabulary are missing.

## C2-09 — distance makes a choice no longer attractive

Source meaning: the ship is already some distance from shore, so the narrator judges returning by swimming unacceptable.

Current status: **PASS-LONG / LEXICON**.

Distance is a typed Length quantity and Units now exist. Evaluate/Prefer/Can handle the decision structure.

## C2-10 — visibility under multiple contributing conditions

Source meaning: despite darkness, stars/lanterns/night vision make visibility adequate.

Current status: **PASS-LONG / LEXICON**.

And/Or, scalar Attributes, and causal/evidence relations are enough structurally. Visibility/light-source vocabulary is missing.

## C2-11 — recognizing an island and then a familiar boat

Source meaning: the narrator sees an island and identifies a boat there as the same boat habitually used by a previously introduced person.

Current status: **DISCOURSE / LEXICON**.

Same and Habitual exist. The failure is durable identity/reference across chapters plus Sense/See vocabulary.

## C2-12 — nervous behavior weakens a simple hypothesis

Source meaning: the narrator initially thinks the problem is solved, then crew behavior provides evidence against that belief.

Current status: **PASS-LONG / LEXICON**.

Believe, EvidenceAgainst, Confidence, and assertion-safe epistemic structure fit cleanly.

## C2-13 — impacts, loss of balance, and recovery

Source meaning: the vessel is struck repeatedly, causing the narrator to fall and catch herself while crew members brace.

Current status: **PASS-LONG / LEXICON**.

Sequence/Concurrent and event causation can carry the structure; physical action vocabulary is missing.

## C2-14 — damaged vessel taking on water

Source meaning: holes in the hull cause rapid water ingress and threaten continued travel.

Current status: **LEXICON / WORLD**.

No new grammar is exposed. Damage/part/flow vocabulary and physical-world behavior are needed.

## C2-15 — detecting an incoming attacker before contact

Source meaning: the senior fighter somehow senses where an aquatic attacker will approach, then attacks that location.

Current status: **LEXICON / WORLD**.

The information/epistemic architecture is adequate; Sense/channel/capability vocabulary is missing.

## C2-16 — attack kills the creature

Source meaning: a magical ranged attack strikes the creature and ends its life.

Current status: **PASS-LONG / LEXICON / WORLD**.

EndLife composition already exists. Attack/projectile/capability terms are world vocabulary.

## C2-17 — quantified group state after reaching shore

Source meaning: the whole group reaches shore; nobody is missing; the group is temporarily stranded.

Current status: **PASS-LONG / LEXICON**.

All/Some/Not plus state relations can represent the quantified core.

## C2-18 — split a collection into pairs

Source meaning: the leader partitions the crew into groups of exactly two and assigns each group a search direction.

Current status: **GRAMMAR / COLLECTION GAP**.

Cuspell has finite collections, Collect, Filter, Each, Count, selectors, and binders, but no generic operation for **partitioning a collection into fixed-size subcollections**.

This is a genuine new corpus finding.

## C2-19 — conditional standing orders for each search pair

Source meaning: if a pair encounters a monster, they must retreat and report; if they find missing fishermen, they must inspect conditions and report according to available group size.

Current status: **PASS-LONG / LEXICON**, aside from the pair-partition issue.

If, Sequence, Obligated, Count, Each, and conditional EventSpecs are sufficient once the groups exist.

## C2-20 — priority among goals

Source meaning: rescue/safety is declared a higher priority than engaging enemies.

Current status: **GRAMMAR / EVALUATION**.

Current Evaluate values are not generically ordered by More/Less. This reinforces the ordered-evaluation gap from Chapter 1.

## C2-21 — prediction that searchers will be too late

Source meaning: the System claims that none of the searchers will arrive before a relevant deadline.

Current status: **PASS-LONG / DISCOURSE**.

Quantification and temporal order exist. A convenient Deadline/InTime relation would shorten the expression; identifying the relevant future event/deadline is discourse-dependent.

## C2-22 — scent trail identifies a known person

Source meaning: the narrator follows a smell trail and infers that it belongs to Henry, a person introduced earlier.

Current status: **DISCOURSE / LEXICON**.

Evidence/Believe architecture works. Sense/Smell and cross-chapter proper-name reference remain gaps.

## C2-23 — wounded living person among dead people

Source meaning: one known person is still alive but severely injured while several companions are dead.

Current status: **PASS-LONG / LEXICON / WORLD**.

Life/EndLife and quantification work. Injury/anatomy vocabulary is missing.

## C2-24 — request for help with incomplete information

Source meaning: the injured person tells the narrator to obtain help and begins communicating a warning before losing the ability to finish.

Current status: **PASS-LONG / DISCOURSE / LEXICON**.

Assert plus Obligated/Intend can represent the communicated goal. Interrupted/incomplete utterance is an aspect/discourse refinement.

## C2-25 — completing one event unlocks a capability/system state

Source meaning: completing the starter task changes the System-access state.

Current status: **LEXICON / WORLD**, with prerequisite architecture still relevant.

Trigger/Begin/Change can represent the transition. A canonical prerequisite/enabling relation would make the general pattern cleaner.

## C2-26 — narrator forms a rescue plan

Source meaning: the narrator refuses to accept the injured person's likely death and intends to fetch the strongest nearby helper.

Current status: **PASS-LONG / LEXICON / DISCOURSE**.

Intend, Highest/Nearest, belief, and Life semantics are adequate if the referenced people/attributes are available.

## C2-27 — almost-human morphology

Source meaning: a creature has an approximately human body plan but differs in multiple anatomical details.

Current status: **PASS-LONG / LEXICON**, with **Almost** still a minor grammar gap.

ShapeLike cleanly avoids asserting Human Kind identity. Anatomy vocabulary is missing. Generic near-threshold resemblance still lacks an Almost operator.

## C2-28 — unknown displayed level/value

Source meaning: an information display identifies a creature type but leaves its level unknown.

Current status: **INFORMATION GAP / LEXICON**.

Open questions represent unknown answer variables when asking, but Cuspell does not yet have a compact first-class "known field with unknown/unavailable value" structure for assertions/information records.

## Chapter 2 findings

Chapter 2 does **not** expose a broad collapse of the language. Most prose reduces to existing event, quantifier, epistemic, and measurement machinery plus missing nouns/verbs.

New or reinforced structural needs are:

1. durable cross-chapter discourse reference and proper names;
2. partitioning collections into fixed-size groups;
3. ordered evaluation/priority;
4. generic near-threshold Almost;
5. a first-class unavailable/unknown field value in Information;
6. a reusable Sense/utterance semantic family;
7. prerequisite/enabling relation (reinforced rather than newly discovered).

The collection-partition requirement is the clearest genuinely new grammar finding from this chapter.
