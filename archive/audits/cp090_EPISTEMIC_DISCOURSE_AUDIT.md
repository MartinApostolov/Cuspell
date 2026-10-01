# Communication, Information, Epistemic, and Discourse Second-Pass Audit

_Status: checkpoint 90 — family-level reduction experiment complete; no net-safe reduction found_

## Scope

This audit tests the 15-root communication/information/epistemic/discourse family:

- `Assert`
- `Infer`
- `Say`
- `Sense`
- `About`
- `AnswerFor`
- `Believe`
- `Confidence`
- `Contrast`
- `EvidenceFor`
- `Explains`
- `Know`
- `Meaning`
- `Remember`
- `Understand`

The family shares many participant shapes — mind/content, sign/content,
information/proposition, speaker/content, evidence/conclusion — but repeated role
shape is not itself repeated meaning.

## Reduction rule

A proposed reduction counts only if the old truth conditions and event/state
distinctions can be reconstructed from fewer irreducible semantic distinctions.

A generic wrapper such as:

`EpistemicRelation mind content kind`

does not reduce the inventory if `kind` still needs independent atoms for Believe,
Know, Remember, Understand, EvidenceFor, and so on.

Likewise, moving a distinction into a world-model flag, hidden speech-force tag, or
Old Name does not remove the semantic primitive.

## Existing machinery tested

Relevant current machinery includes:

- `Confidence(mind, proposition) -> Quantity:Confidence`;
- `High`, `More`, `Equal`, and normalized confidence endpoints;
- `Begin` / `End` persistent-state transitions;
- `Cause`;
- `Say` with Proposition, Information, or Sign content;
- `Question` / `AnswerFor`;
- `Meaning` and `About`;
- `EvidenceFor` and `Explains`;
- `Sense` with explicit channel and interpreted-Sign frames;
- `Not`, `And`, quantification, and temporal relations.

Previous reduction work already removed many superficial wrappers:

- EvidenceAgainst -> EvidenceFor of Not P;
- Claim -> Assert;
- Tell -> addressed Say;
- See/Hear/Smell/Taste -> Sense + channel;
- Ask -> Say of QuestionContent;
- Detected -> Happen Sense;
- Read -> interpreted-Sign Sense;
- PossibleTo/ProbableTo/CertainTo -> Confidence comparisons;
- KnowAnswer -> existential Know + AnswerFor;
- Thank/Apologize/Consent/Refuse/Promise -> Say-based compositions;
- Because -> contextual Explains.

This audit therefore asks whether the surviving roots still contain another shared
basis rather than repeating those already-successful reductions.

## Experiment A — Believe from Confidence

This is the strongest apparent candidate.

The epistemic specification says belief correlates with Confidence meeting a belief
threshold, and `High Confidence mind P` already expresses contextual high
confidence.

However, the current registered meanings are not interchangeable:

- `Believe(mind,P)` is a persistent `StateProposition`;
- `High Confidence mind P` uses the general Quantity threshold frame and returns a
  `Proposition`, not a persistent state;
- `High` selects a contextually relevant standard, while Believe denotes the
  mind-model's actual belief state rather than whichever probability standard is
  currently salient;
- the same `High Confidence` machinery is already used for ordinary
  probability/probability-standard readings such as former `ProbableTo`.

Making belief exactly one High threshold would therefore either collapse belief and
contextual probability language or require a new explicit belief-threshold
selector/value. The latter would merely move the missing semantic distinction.

A future epistemic architecture could revisit this if belief-state classification
is formally defined as one canonical Confidence threshold and the state typing is
generalized independently.

**Result: retain Believe and Confidence separately.**

## Experiment B — Know from Believe + truth

A tempting classical composition is:

`And {Believe M P,P}`

This is not the current semantics of `Know`.

The project explicitly treats Know as factive knowledge and does not define
knowledge as mere true belief. A confidently held true belief need not automatically
qualify as knowledge under the world/mind model; justification/access/epistemic
status may matter.

The existing distinction is also useful operationally: false belief is representable
without making it Know, and teaching/learning facts use `Begin Know` rather than
merely changing confidence.

**Result: retain Know.**

## Experiment C — Remember from Know + past persistence

`Remember(mind,content)` is a memory/retention state over general SemanticValue
content.

It is not equivalent to current knowledge:

- remembered content can be inaccurate or non-propositional;
- one can know something now without remembering a prior episode/content as memory;
- memory manipulation and knowledge manipulation are separately modeled;
- `Remember` accepts arbitrary SemanticValue content, while Know has Proposition
  and Information frames.

Adding `Before Know` or `Persist Know` does not reconstruct the memory relation.

**Result: retain Remember.**

## Experiment D — Understand from Know

`Understand` is comprehension of semantic content rather than mere possession of
factive information.

A mind may know a proposition or possess Information without understanding a rule,
language, explanation, method, or theory represented by that content.

Conversely, Understand can target SemanticValues broader than the current Know
frames.

This distinction already matters in the Learn/Teach reductions, which deliberately
use `Begin Know` for facts/Information and `Begin Understand` for broader
comprehension.

**Result: retain Understand.**

## Experiment E — Assert from Say

`Say` is a medium-general utterance Process. It can carry:

- Proposition;
- Information;
- Sign;
- QuestionContent/CommandContent through their Information typing;
- social/deontic propositions used in consent, apology, promise, and similar speech.

`Assert` adds speech-force content: the speaker presents a Proposition as true and
publicly commits to that presentation.

Plain `Say speaker P` does not encode that assertion force. Replacing Assert with
Say would incorrectly make every propositional utterance an assertion, including
quoted, hypothetical, performative, or otherwise non-assertive uses.

A generic speech-force system could revisit this only if several speech-act roots can
share fewer independently defined force features. One hidden `AssertForce` value
would not be a reduction.

**Result: retain Assert and Say separately.**

## Experiment F — Infer from EvidenceFor + Begin Believe/Know

`Infer(mind,evidence,conclusion)` is an actual reasoning EventSpec.

`EvidenceFor(I,P)` is a static support relation.

Neither `Begin Believe` nor `Begin Know` identifies the reasoning process:

- belief may begin through persuasion, memory, perception, coercion, or other causes;
- an inference can fail to produce lasting belief;
- evidence can support a proposition without any mind performing an inference;
- a valid inference need not make the conclusion objectively true, so Know cannot
  stand in generally.

A composition such as `Cause evidence Begin Believe` would additionally misuse
Information as the causal agent/event and still lose the inference-rule/process
meaning.

**Result: retain Infer.**

## Experiment G — EvidenceFor from About / Meaning / Cause

These relations answer different questions:

- `About(I,X)` — what the Information is about;
- `Meaning(S,C)` — what content a Sign conveys;
- `EvidenceFor(I,P)` — whether Information supports a Proposition;
- `Cause(E1,E2)` — causal dependence.

Information can be about a proposition without supporting it. A Sign can mean a
claim without providing evidence for it. Evidence can support a causal claim without
causing the claimed event.

EvidenceAgainst was reducible because polarity is supplied by `Not P`; the support
relation itself remains irreducible.

**Result: retain EvidenceFor.**

## Experiment H — Explains from EvidenceFor or Cause

`Explains` relates an Explanation, or contextually a reason Proposition, to a
target Proposition.

It is deliberately broader/different from physical causation and epistemic support:

- an explanation may be mathematical, structural, definitional, intentional, or
  causal;
- evidence may support a proposition without explaining why it is true;
- a cause may exist without being represented as an explanation.

The former generic Because root was removed by routing its discourse reading through
Explains, which makes Explains the reusable abstraction rather than evidence that it
is redundant.

**Result: retain Explains.**

## Experiment I — Meaning from About

This was tested in the first exact-reduction audit and still fails.

`Meaning(Sign,content)` is an interpretation relation between a representation and
its conveyed content, with language/context-sensitive ambiguity allowed.

`About(Information,topic)` is subject-matter/topicality of already represented
Information.

A sign can mean Information that is about something else. Therefore the two
relations compose rather than substitute for one another.

**Result: retain Meaning and About.**

## Experiment J — AnswerFor from About / Meaning / EvidenceFor

An answer to a question is not merely information about the question, nor a Sign
meaning the question, nor evidence for the question object.

`AnswerFor(answer,QuestionContent)` supplies the typed answer relation needed by
open-question composition:

`Some i:Information And {Know M $i,AnswerFor $i Q}`

Without AnswerFor, Cuspell would need a new question-resolution relation of equal
semantic specificity.

**Result: retain AnswerFor.**

## Experiment K — Sense from information acquisition / Meaning

`Sense` is an actual perceptual EventSpec with channel/stimulus roles.

Meaning is static sign interpretation and cannot replace perception. Conversely raw
Sense does not guarantee successful semantic interpretation.

The contextual interpreted-Sign Sense frame already absorbed the former Read root,
which is exactly the useful compression available here. Removing Sense would require
reintroducing channel-specific perception processes or a generic acquisition event
with an equally primitive sensory-mode distinction.

**Result: retain Sense.**

## Experiment L — Contrast from And / Expect / Confidence

This was also tested in the first audit.

`Contrast(A,B)` preserves the represented sides while marking discourse tension,
concession, or violated expectation.

`And {A,B}` asserts/co-represents both sides but lacks the discourse relation.

Trying to reconstruct Contrast with an explicit Expect or Confidence state would
incorrectly require a particular mind/expectation holder and would turn a discourse
coherence relation into an epistemic state.

A future general discourse-relation architecture could revisit Contrast, but one
`ContrastKind` tag would be fake compression.

**Result: retain Contrast.**

## Generic wrapper count test

Possible wrappers include:

- `MentalState(mind,content,mode)`;
- `InformationRelation(info,target,mode)`;
- `Speech(speaker,content,force)`;
- `DiscourseRelation(a,b,mode)`.

Exact reconstruction would still require independent atoms for:

- assertion force;
- inference process;
- sensory acquisition;
- topicality;
- answerhood;
- belief;
- confidence degree;
- contrast;
- evidential support;
- explanation;
- factive knowledge;
- sign interpretation;
- memory;
- comprehension.

That is not fewer distinctions than the current family, and the wrapper roots would
increase the visible semantic inventory.

**Result: reject generic enum-shaped compression.**

## Count result

No root is removed and no new epistemic/discourse wrapper is added.

Current inventory remains:

- **206 registered base entries**;
- **126 semantic primitive candidates**;
- **54 formal constructors**;
- **16 reference forms**;
- **10 domain values**;
- **0 unresolved candidates**;
- **0 derived candidates**.

The communication/information/epistemic/discourse family remains **15 semantic
primitive candidates**.

## Design conclusion

This family has already benefited heavily from earlier compositional reductions.
Most convenience speech, question, confidence, sensing, and teaching wrappers have
already disappeared into the surviving general machinery.

The remaining fifteen roots occupy different semantic layers rather than duplicating
one another: utterance vs assertion force, perception vs interpretation, support vs
explanation, belief vs factive knowledge vs memory vs comprehension, and discourse
contrast vs logical conjunction.

The next second-pass family should be **time and event occurrence**, followed by the
small operational/body-state family and then foundational ontology/classification.
