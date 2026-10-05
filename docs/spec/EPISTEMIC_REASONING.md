# Epistemic State, Evidence, Assertion, and Inference

_Status: current working specification_

This specification separates world truth from what a Mind believes, knows, expects, senses, infers, or asserts.

## 1. World truth and mental state are distinct

A Proposition may be true or false independently of any Mind.

A Mind may:

- Believe a Proposition;
- Know a Proposition/Information;
- assign Confidence to a Proposition;
- Expect a Proposition/EventSpec;
- receive EvidenceFor a Proposition;
- Infer a conclusion;
- Assert content.

None of these automatically makes an embedded Proposition true unless the relation itself is factive and its semantics require it.

## 2. Confidence

`Confidence mind proposition` returns Quantity:Confidence.

Canonical endpoints:

- `Zero` = complete rejection;
- `«ConfidenceUnit» @` = complete confidence.

World/mind models may use different internal calculations but expose a normalized Cuspell value.

## 3. Believe

`Believe mind proposition` is a persistent epistemic state.

It does not require the proposition to be true.

Believe is not reduced to a contextual High Confidence threshold because the registered belief state remains a distinct persistent Relation.

## 4. Know

`Know` has typed frames for Proposition and Information content.

Knowledge is factive in the semantic/world model and is not merely maximum Confidence.

A false high-confidence belief therefore remains Believe, not Know.

## 5. Possibility, probability, certainty

No standalone PossibleTo/ProbableTo/CertainTo roots remain.

Current compositions:

- possible to a Mind -> `More Confidence mind P Zero`;
- probable -> `High Confidence mind P`;
- certain -> `Equal Confidence mind P «ConfidenceUnit» @`.

Contextual High requires an objective threshold before magical execution can depend on it.

## 6. Evidence

`EvidenceFor information proposition` states epistemic support.

Evidence against P is:

`EvidenceFor information Not P`

Evidence is not Cause.

Comparing evidence strength, if a world/model exposes an ordered strength value, uses the ordinary `More` relation with argument order rather than a separate Less root.

## 7. Observation and detection

There is no Detected/NotDetected root.

Channel-specific detection is represented as occurrence of Sense:

`Happen Sense experiencer Vision stimulus interval`

or another explicit SenseChannel.

Non-detection is logical negation of the relevant occurrence proposition:

`Not Happen Sense experiencer Vision stimulus interval`

Failure to detect does not imply physical absence unless the sensing/world model guarantees that inference.

## 8. Expectation

`Expect` is a persistent prospective mental/model state over Proposition/EventSpec content.

It remains distinct from Confidence thresholds and from contextual habitual frequency.

## 9. Inference

`Infer mind evidence conclusion` is an EventSpec describing an inference episode.

Infer does not guarantee truth merely because a Mind reached the conclusion.

The relevant inference model may come from discourse/world context; exact magical reasoning must make any execution-relevant model objective.

## 10. Cause, evidence, explanation

Keep distinct:

- `Cause` — world causal dependence;
- `EvidenceFor` — epistemic support;
- `Explains` — explanatory/discourse relation;
- `About` — topicality.

English “because” can map to more than one of these, so the minimized core has no generic Because root.

## 11. Explanation

`Explanation` is an Information subtype.

`Explains explanation target` links it to a Proposition.

An open why-question may therefore bind an Explanation:

`x:Explanation Explains $x target?`

The resulting Question asks for Explanation values satisfying that relation.

## 12. Assert

`Assert speaker proposition recipient?` is a speech EventSpec with assertion force.

Occurrence of the assertion does not imply the asserted proposition is objectively true.

Assert remains distinct from plain Say because Say does not inherently carry assertion force.

## 13. Claims

There is no separate Claim root.

A claim in the relevant speech-act sense uses Assert; skepticism or evidential stance is represented outside the speech act.

## 14. Promise composition

There is no Promise root.

For speaker S, addressee/context A, and promised EventSpec E, the minimized meaning is built from:

- addressed `Say` of an `Obligated S E A` proposition; and
- `Begin Obligated S E A`.

Here `A` occupies the optional positional context slot. If that context is omitted inside a larger flat expression, use the ordinary `_` omission marker rather than a named role selector.

This separates the utterance from the performative beginning of the obligation state.

Whether the promise is later fulfilled is a separate fact.

## 15. Contrast

`Contrast A B` is a contextual discourse relation marking relevant tension/concession between the sides.

Plain And states both sides but does not encode that expectation relation.

## 16. Answers

`AnswerFor information question` states answerhood.

A known answer can be represented compositionally by binding Information that is both known and AnswerFor the QuestionContent.

Answerhood is distinct from truth, evidence, topicality, and mere response speech.

## 17. Meaning and interpretation

`Meaning sign content` is the contextual Sign-to-content interpretation relation.

It remains separate from About, EvidenceFor, Equal, and Name.

## 18. Bounded factual acquisition

Checkpoint 131 adds `Find` for one epistemic operation that the earlier layer deliberately lacked: acquiring a truthful answer that was not already available to the mind/execution context.

`Find mind scope proposition`

acquires the true yes/no polarity of the proposition.

`Find mind scope binder proposition`

acquires the complete satisfying binder answer within the permitted scope.

The explicit scope must participate in the query. It bounds information access rather than silently selecting a target. At execution time, otherwise unavailable facts used to answer must be licensed by that scope and world capability.

Blocked or incomplete access is failure, not a negative answer.

This keeps Find distinct from Question, Sense, Collect, Infer, Know, and AnswerFor.

## 19. Result

The current epistemic layer keeps distinct:

- truth;
- confidence;
- belief;
- knowledge;
- expectation;
- evidence;
- sensing/detection;
- inference;
- assertion;
- explanation;
- answerhood;
- semantic meaning;
- bounded factive acquisition through `Find`.

This prevents ordinary discourse shortcuts from becoming hidden magical assumptions.
