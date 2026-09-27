# Epistemic State, Evidence, Assertion, and Inference

_Status: working specification v0.1_

This specification was forced by the prose corpus. It separates facts about the world from what a speaker perceives, believes, expects, or asserts.

## 1. World truth versus mental state

A Proposition may be true or false independently of any Mind.

A Mind may:

- Know a true Proposition;
- Believe a Proposition with some confidence;
- consider a Proposition possible;
- expect a Proposition/Event;
- possess Evidence for or against a Proposition;
- Assert a Proposition without making it true.

These relations must not collapse.

## 2. Confidence

Introduce:

Confidence(mind, proposition, context?) -> Quantity<EpistemicConfidence>.

The default normalized scale is ordered and bounded by the world/mind model, conceptually from complete rejection to complete confidence.

The exact numerical interpretation can be world-model data.

The important language fact is that confidence values are ordered and comparable.

## 3. Believe

Refine:

Believe(mind, proposition) -> state-predicate Proposition.

Believe means the Mind's Confidence in the Proposition meets the relevant belief threshold.

It does not require the Proposition to be true.

A more precise expression can compare Confidence directly.

## 4. Know

Know remains factive:

Know(mind, proposition)

requires both:

- the Proposition is true;
- the Mind satisfies the world's knowledge/justification model.

Knowledge is not merely maximum Confidence.

A confidently held false belief remains Believe, not Know.

## 5. Probably / maybe / certainly

Ordinary-language epistemic terms can be threshold predicates over Confidence.

Working semantic molecules:

- ProbableTo(mind, P): Confidence above a registered/contextual probability threshold.
- PossibleTo(mind, P): Confidence/possibility above the minimum possibility threshold.
- CertainTo(mind, P): Confidence at or above the certainty standard.

Maybe can lexicalize PossibleTo for ordinary speech.

For magical execution or exact technical reasoning, thresholds must be explicit or registered.

## 6. Evidence

Introduce:

EvidenceFor(information, proposition, reasoner/model?) -> Proposition/Relation.

and:

EvidenceAgainst(information, proposition, reasoner/model?) -> Proposition/Relation.

Evidence means that, under the relevant inference model, the Information bears positively/negatively on rational confidence in the Proposition.

Evidence does not mean Cause.

Seeing shoes by a door can be EvidenceFor(OwnerIsHome) without causing the owner to be home.

## 7. Evidence strength

A richer model may use:

EvidenceStrength(information, proposition, model) -> Quantity<EvidenceStrength>.

This supports More/Less comparison between pieces of evidence.

The corpus does not yet require exact numeric Bayesian semantics; ordered evidential support is sufficient.

## 8. Observation

Sense produces Information under a defined channel/scope.

Observation claims should distinguish:

- information positively detected;
- failure to detect;
- measured absence.

Introduce conceptual Relations:

Detected(sense-event/result, phenomenon/value).

NotDetected(sense-event/result, phenomenon/value).

NotDetected(Sound) does not imply Equal(SoundLevel, Zero) unless the Sense/measurement model guarantees that inference.

This distinction is mandatory for objective magic and useful in ordinary prose.

## 9. Expectation

Introduce:

Expect(mind/model, proposition-or-EventSpec, context) -> state-predicate Proposition.

Expectation is a prospective belief about what normally/future-likely occurs.

It can be derived from Habitual/Generic knowledge but is represented separately as a mental/model state.

Unexpected/Anomalous can be defined by conflict between observation and Expect.

## 10. Belief update

An Event in which a Mind receives Evidence can change Confidence/Believe.

The language may describe that change explicitly:

Change(mind, Confidence(...), new-value)

or through a conventional Process:

Infer(mind, evidence, proposition) -> EventSpec.

Infer does not guarantee truth; it changes the reasoner's epistemic state according to an inference rule/model.

## 11. Inference model

Objective semantics does not require all Minds to reason identically.

An inference model may be:

- ordinary rational/world-model inference;
- a particular person's reasoning;
- formal logic;
- probabilistic model;
- magical oracle model.

When omitted in casual discourse, the context supplies it.

Magic that depends on exact inference must name/fix the model.

## 12. Cause versus evidence

Keep three concepts distinct:

### Cause

A world relation between Events/states where one brings about another under the setting's causal model.

### EvidenceFor / ReasonForBelief

An epistemic relation where Information supports confidence in a Proposition.

### Discourse explanation

A speaker can present one clause as explaining another without asserting a direct physical Cause.

The English gloss "because" can express all three.

Therefore a generic Because is ordinary-language/contextual unless its typed frame resolves uniquely.

Magical/technical Cuspell should prefer Cause or EvidenceFor/Explanation explicitly.

## 13. Explanation

An Explanation is an Information structure linking a target question/fact to one or more causal, evidential, purposive, or rule-based reasons.

This gives open why-questions an answer type.

A why-question can ask for:

[x:Explanation] Explains($x, target).

The answer may contain Events, Propositions, or rules.

## 14. Assert

Introduce:

Assert(speaker, proposition, recipient/context?) -> EventSpec.

Assert is a speech act in which the speaker publicly commits to presenting the Proposition as true.

Crucially:

Happen(Assert(A,P))

does not imply P.

It implies that A asserted P.

This solves reported claims in narration.

## 15. Claim

Claim can be a conventional synonym/semantic molecule around Assert when the surrounding narrator does not endorse the content.

The formal semantic core need not encode skepticism; outer discourse relations can do that.

## 16. Promise

Refine Promise as a speech act:

Promise(speaker, addressee/beneficiary, future-EventSpec) -> EventSpec.

A successful Promise Event begins a social commitment state:

CommittedTo(speaker, future-EventSpec, commitment-context).

Whether the speaker later fulfills it is a separate fact.

## 17. Contrast and concession

Add ordinary discourse Relation:

Contrast(A,B, context) / Although(A,B).

Both embedded propositions/events remain asserted as appropriate, while the discourse relation marks that B conflicts with an expectation normally associated with A.

This captures structures such as:

a person verbally rebukes someone, yet continues affectionate behavior.

Contrast is mostly discourse/pragmatic and ordinarily not a magical predicate.

## 18. Private versus public naming

Name(Sign, referent, naming-context) already supports private labels.

A route name used only by one speaker can use that speaker's personal naming context rather than a community-wide naming system.

No additional identity mechanism is required.

## 19. Information source attribution

Narrative translation should preserve whether a Proposition is:

- narrator assertion;
- character assertion;
- character belief;
- observation;
- inference;
- world fact supplied by omniscient narration.

Back-translation must not silently upgrade a character's inference into objective truth.

## 20. Corpus consequence

The Yona chapter demonstrates why perception/inference distinctions are necessary even for magic-focused Cuspell.

A future detection spell must likewise distinguish:

- no target detected;
- target proven absent;
- evidence suggesting absence.

The same epistemic layer therefore benefits both ordinary narrative and magical sensing/divination.
