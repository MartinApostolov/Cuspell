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

The canonical language-level scale is ordered and normalized:

- `Zero` = complete rejection;
- `«ConfidenceUnit» @` = complete confidence.

World/mind models may compute confidence using probabilities, scores, evidence systems, or other internal representations, but the value exposed to Cuspell is mapped into this canonical interval.

The important language facts are that confidence values are ordered, comparable, and have fixed language-level endpoints.

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

- probable(mind, P): `High Confidence mind P`, meaning Confidence above the relevant contextual/registered probability standard;
- possible(mind, P): `More Confidence mind P Zero`, meaning the mind assigns positive Confidence to P;
- certain(mind, P): `Equal Confidence mind P «ConfidenceUnit» @`, meaning complete confidence on the normalized scale.

`ProbableTo`, `PossibleTo`, and `CertainTo` are no longer standalone roots. Certainty uses the exact upper endpoint rather than contextual `High`.

For magical execution or exact technical reasoning, contextual thresholds must be made objective by explicit or registered world calibration.

## 6. Evidence

Use:

EvidenceFor(information, proposition, reasoner/model?) -> Proposition/Relation.

Evidence against proposition P is written compositionally as EvidenceFor(information, Not(P), model?) rather than requiring a second root.

Evidence means that, under the relevant inference model, the Information bears on rational confidence in the represented Proposition.

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

Use the Relation:

Detected(experiencer/result, phenomenon/value, channel?).

Failure to detect is written as Not(Detected(...)); it is not a separate NotDetected root.

Not(Detected(Sound)) does not imply Equal(SoundLevel, Zero) unless the Sense/measurement model guarantees that inference.

This distinction is mandatory for objective magic and useful in ordinary prose.

## 9. Expectation

Introduce:

Expect(mind/model, proposition-or-EventSpec, context) -> state-predicate Proposition.

Expectation is a prospective belief about what normally/future-likely occurs.

It can be derived from contextual recurrence (`High Rate ...`) or Generic knowledge but is represented separately as a mental/model state.

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

The English gloss "because" can express all three, so there is no generic `Because` root in the minimized core.

Use the typed relation that is actually intended:

- physical/world causation: `Cause`;
- evidential support: `EvidenceFor`;
- ordinary discourse explanation: contextual `Explains reason target`.

Magical/technical Cuspell should prefer the objective typed relation rather than rely on contextual discourse explanation.

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

## 15. Claims in discourse

The minimized core uses Assert for the speech act. English “claim” does not require a separate root merely because the narrator may be skeptical.

The formal semantic core does not encode that skepticism in the speech-act verb; outer discourse/evidence relations can do that.

## 16. Promise

There is no separate `Promise` root in the minimized core.

For speaker S, addressee A, and promised EventSpec E:

`And {Say S CommittedTo S E A A,Begin CommittedTo S E A}`

is the Promise meaning. The first EventSpec is the addressed utterance of the commitment content; the second begins the social commitment state in the addressee/context. `Say` does not itself entail that its propositional content was already true, while `Begin CommittedTo` supplies the performative state transition.

Whether S later fulfills E remains a separate fact.

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
