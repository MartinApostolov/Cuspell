# Yona Corpus Pilot — Chapter 1, Pass A

_Source: Yona [Cat Girl Evolution], Bedivere the Mad, Chapter 1 "Quite the Mystery"_
_Source URL: https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2525425/1-quite-the-mystery_

This file records semantic paraphrases rather than reproducing the chapter text.

Pass A covers the opening through the narrator leaving her owners' house and beginning the trip toward the shore (roughly Royal Road reader lines 58–92 at the time of analysis).

## A01 — current Kind membership

Source meaning: the narrator says that she is currently a cat.

Finding: Cuspell had no explicit normative rule saying a Kind may be used predicatively of an Entity, even though many examples assumed it.

Status: CUSPELL-DEFECT / GRAMMAR.

Required resolution: add Kind predication / InstanceOf semantics.

## A02 — previous non-cat state versus current cat state

Source meaning: the narrator was not a cat in an earlier relevant period but is a cat now.

Possible semantic form: past Not(Cat(Self)) AND current Cat(Self).

Finding: explicit temporal relations can express this, but narrative tense/aspect is extremely verbose. Former(NotCat(Self)) nearly captures the transition, but does not provide a general prose tense system.

Status: PASS-LONG / DISCOURSE.

## A03 — death followed by resumed consciousness

Source meaning: the narrator died earlier and later became conscious again.

Possible core: Sequence(EndLife(Self), BeginAwake(Self)) at past times.

Finding: the event structure is expressible, but ordinary narrative needs a default past reference interval and lexical Awake/Wake. Identity across death/body change is world-metaphysics data.

Status: PASS-LONG / LEXICON / WORLD / DISCOURSE.

## A04 — waking in a different/current body

Source meaning: on waking, the narrator finds herself embodied in the currently indicated body.

Finding: Cuspell intentionally left Mind/Body metaphysics to the world model. The corpus immediately needs a typed relation such as BodyOf, EmbodiedIn, or equivalent setting ontology.

Status: WORLD / LEXICON.

## A05 — System communicates a Quest command

Source meaning: a System-like entity communicates that the narrator should complete a particular Quest.

Possible core: Say/Tell(System, Command-content(Complete(Self, QuestRef)), Self).

Finding: Information versus active Command already prevents quoted quest text from executing accidentally. Missing pieces are world Kinds System, Quest, and a completion state/process.

Status: PASS-LONG / LEXICON / WORLD.

## A06 — stop-talking imperative

Source meaning: the narrator commands the System to cease communicating.

Finding: Cuspell can command Events to happen, but has no clean general command whose semantic target is prevention/cessation of an ongoing Process type such as Say. End applies naturally to state predicates and concrete event boundaries, not arbitrary future occurrences.

Status: GRAMMAR / CUSPELL-DEFECT.

Required resolution: explicit Stop/Prevent or event-negation control semantics.

## A07 — subjective evaluation of being a cat

Source meaning: the narrator evaluates the state of being a cat positively.

Finding: Good exists only as a contextual ordinary-language candidate. The evaluator must be explicit enough for back-translation: good/nice according to Self is different from an objective magical Property.

Status: GRAMMAR / LEXICON.

## A08 — owners and possession/social role

Source meaning: the narrator has human owners.

Finding: Have describes possession/control from possessor to possessed, but ordinary language also needs the inverse social relation OwnerOf/OwnedBy and must decide whether living-creature ownership is modeled as legal/social possession.

Status: LEXICON / WORLD.

## A09 — husband/spouse and profession

Source meaning: one owner is married to the other and works as a fisherman.

Finding: social relations and Profession/Role are not yet specified in enough detail.

Status: LEXICON / WORLD.

## A10 — abundant recurring food access

Source meaning: because of that profession, the narrator has a practically continuous supply of fresh food.

Finding: exact event semantics are possible using repeated Give/Have/availability, but ordinary prose needs compact concepts for access/availability and habitual recurrence.

Status: PASS-LONG / LEXICON / DISCOURSE.

## A11 — preference for fish

Source meaning: the narrator has a standing preference for fish.

Finding: Want is not the same as liking/preference. A stable Prefer/Like mental relation is useful.

Status: LEXICON.

## A12 — food tastes especially good to current narrator

Source meaning: fish produces a strongly positive taste experience for the narrator in her current body/state.

Finding: SenseChannel semantics can represent Taste, but evaluative reaction to sensed Information is missing.

Status: GRAMMAR / LEXICON.

## A13 — ability versus habitual actuality

Source meaning: the narrator is able to eat throughout the day and in fact habitually does so.

Finding: Can can represent capability, but Cuspell lacks a settled Habitual/Usually aspect/operator for ordinary discourse.

Status: DISCOURSE / GRAMMAR.

## A14 — ongoing bodily change

Source meaning: the narrator is currently becoming fatter.

Possible core: ChangeBy(Self, body-fat/mass-related Attribute, positive delta) during an interval containing narrative Now.

Finding: the Change model works, but progressive/ongoing aspect needs compact narrative grammar and body composition is world/lexicon data.

Status: PASS-LONG / DISCOURSE / LEXICON.

## A15 — reason/causal explanation

Source meaning: the narrator considers the weight gain unimportant because she is a cat.

Finding: Because can relate propositions/reasons, but subjective ImportantTo evaluation is missing.

Status: LEXICON.

## A16 — generic claim about cats

Source meaning: cats as a class are generally considered cute across body sizes.

Finding: All(Cat,Cute) would state a strict universal and is too strong. Natural-language generic statements tolerate exceptions.

Status: GRAMMAR / DISCOURSE.

Required resolution: generic/typical quantification distinct from All.

## A17 — community agreement

Source meaning: the village population broadly agrees with the positive evaluation of cats.

Finding: Agree exists as a candidate but needs content and group/distribution semantics. "The whole village" is metonymic for community members rather than the spatial Region.

Status: PASS-LONG / LEXICON / DISCOURSE.

## A18 — habitual conditional

Source meaning: whenever the owners stop feeding the narrator for the day, she can leave and seek food from someone else.

Finding: If exists for one evaluated condition, but prose needs recurring whenever semantics: for each matching event/time, a consequence/capability pattern holds.

Status: GRAMMAR / DISCOURSE.

## A19 — comparative evaluation

Source meaning: the narrator evaluates being a cat as better than being a person.

Finding: numeric More cannot directly compare subjective situations without an evaluation scale/value function.

Status: GRAMMAR / LEXICON.

## A20 — absence of responsibilities

Source meaning: the narrator has no social obligations/responsibilities.

Finding: Owe exists, but obligation/responsibility as a state/modal relation is not formalized.

Status: LEXICON.

## A21 — capability with unrestricted choices

Source meaning: the narrator says she can sleep in arbitrary places and approach arbitrary people for petting when she wants.

Finding: All, collections, and selectors handle formal domains, but ordinary any/anywhere/anyone combines free choice, quantification, and modality. It should not be translated as strict universal truth without a modal frame.

Status: GRAMMAR / DISCOURSE.

## A22 — habitual exception

Source meaning: almost everyone responds positively, except one named man who tends to kick the narrator.

Finding: explicit collections and exclusion can represent this, but ordinary "almost everyone" needs a quantitative/generic construction and named-person reference needs discourse/name lookup.

Status: PASS-LONG / DISCOURSE / LEXICON.

## A23 — self-directed should and intention

Source meaning: the narrator considers damaging the man's shoes again and forms a mild intention because she is bored.

Finding: Want is not enough for the meanings of Should/Intend/Plan. Deontic recommendation, intention, and pragmatic "might as well" are currently absent.

Status: GRAMMAR / LEXICON / STYLE-LOSS.

## A24 — simultaneous body actions

Source meaning: the narrator stands, stretches, and yawns with partial temporal overlap.

Finding: Event And means unordered joint realization and Sequence means order, but neither alone captures while/concurrent overlap precisely.

Status: GRAMMAR.

## A25 — direct speech and speaker-context switching

Source meaning: a human owner utters a comment to/about the narrator.

Finding: Say plus quoted Information can represent the event, but inside quotations Self, You, Here, Now, and anaphora must resolve relative to the quoted utterance speaker/context rather than the outer narrator.

Status: DISCOURSE / CUSPELL-DEFECT.

## A26 — apposition and proper naming

Source meaning: a previously introduced owner is identified as the wife and as a person named Sally.

Finding: Name exists as a Relation, but prose needs convenient discourse binding/apposition so multiple predicates can update one salient referent and later pronouns can recover it.

Status: DISCOURSE / GRAMMAR.

## A27 — multiple descriptive predicates

Source meaning: Sally is described with several personal, bodily, and professional properties.

Finding: Property conjunction works, but evaluative properties require an evaluator/standard and profession remains world/social vocabulary.

Status: PASS / LEXICON.

## A28 — perception plus evaluation during another event

Source meaning: the narrator dislikes bread as food but evaluates its smell positively while Sally is baking/working.

Finding: Sense and temporal relations can express the parts. Missing pieces are compact preference/evaluation and while/aspect.

Status: PASS-LONG / LEXICON / DISCOURSE.

## A29 — action chain with pronouns

Source meaning: the narrator jumps down, rubs against Sally, receives petting, then walks toward the door.

Finding: Sequence can represent ordered actions, but pronoun/anaphoric reference and implicit reciprocal/social event interpretation are missing from ordinary discourse.

Status: PASS-LONG / DISCOURSE / LEXICON.

## A30 — open wh-question

Source meaning: Sally asks for the destination of the narrator's current/intended movement.

Finding: current Question syntax primarily handles proposition questions. It mentions open-value query shapes but does not define them.

Status: GRAMMAR / CUSPELL-DEFECT.

## A31 — continuing action and passage through door

Source meaning: the narrator ignores Sally, continues walking, and passes through a partly open door.

Finding: path/Through semantics work. Continue/keep doing needs aspectual continuation; partial Open state needs an Attribute/degree model.

Status: PASS-LONG / LEXICON / DISCOURSE.

## A32 — most-people habitual generalization

Source meaning: most local residents habitually leave doors open; the remainder generally leave them unlocked.

Finding: All/Some/None are insufficient. Most plus Habitual/Typical semantics are needed.

Status: GRAMMAR / DISCOURSE.

## A33 — reciprocal generalized knowledge

Source meaning: community members generally know one another, supporting greater trust and less crime.

Finding: nested binders can express strict reciprocal All/All knowledge, but the source is generic rather than exceptionless. Comparative abstract nouns Trust/Crime also need social lexicon.

Status: PASS-LONG / DISCOURSE / LEXICON.

## A34 — purpose clause and arbitrary-time desire

Source meaning: the narrator can enter residents' houses in order to obtain food whenever desired.

Finding: Purpose can represent the goal, but modal free-choice any, habitual whenever, and desire-conditioned timing need ordinary-language grammar.

Status: GRAMMAR / DISCOURSE.

## First-pass architecture findings

The opening alone exposes language-wide features that spell-oriented tests did not force:

1. Kind predication / InstanceOf must be normative.
2. Discourse reference and anaphora are necessary.
3. Narrative reference time and tense/aspect need compact semantics.
4. Generic/habitual quantification must be distinct from strict All.
5. Subjective evaluation and preference need explicit evaluator/experiencer frames.
6. Modality needs more than Can/Want: at least intention and obligation/recommendation families.
7. Direct/reported speech requires nested utterance contexts.
8. Open wh-questions need typed answer binders.
9. Process cessation/prevention needs explicit semantics.
10. Concurrent/overlapping event composition needs a compact form.
11. Proper-name/definite reference needs an ordinary discourse layer.
12. The world package needs social-role/profession/body vocabulary, but those are lexical/world gaps rather than core grammar failures.

This is a successful corpus test: it found several holes that the magic-focused regression suite had not exposed.
