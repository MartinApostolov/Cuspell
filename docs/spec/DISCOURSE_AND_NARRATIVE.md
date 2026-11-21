# Discourse, Narrative, Modality, and Questions

_Status: current working specification_

This specification defines the discourse machinery that lets Cuspell operate as more than isolated magical commands. Surface examples use canonical v0.9.

## 1. Kind predication

A Kind can be predicated of an Entity.

Conceptually:

`InstanceOf(entity, Kind) -> Proposition`

Canonical examples:

`MatterSelf.`

`«LowExtent«MoveLifeThing»» This.`

A Kind does not silently select one member.

## 2. Utterance context

Ordinary discourse has a typed context containing at least:

- speaker;
- addressee(s);
- utterance time;
- utterance location;
- discourse reference time/interval;
- salient discourse referents;
- relevant language/naming context.

Contextual references such as Self, You, Here, Now, This, That, and They resolve against this structure.

A magical casting context is a stricter execution-oriented form of the same idea.

## 3. Nested speech contexts

Reported/direct speech may establish a nested utterance context.

Inside speech attributed to another speaker:

- Self resolves to that speaker;
- You resolves to the nested addressee;
- Here/Now resolve to the nested context unless explicitly anchored elsewhere.

This prevents an embedded first-person reference from accidentally resolving to the outer narrator/caster.

## 4. Quotation versus semantic content

Quotation preserves an exact Sign:

`«Yona»`

`«Yona's«SharpStick»»`

Reported content instead embeds semantic Information/Proposition/QuestionContent/CommandContent.

`Say` can carry Proposition, Information, or Sign content according to its registered frames.

Exact wording and semantic content are therefore distinct.

## 5. Discourse referents

Ordinary discourse may introduce referents that remain salient across sentence boundaries.

A discourse referent can record:

- resolved identity/value;
- type;
- descriptive information;
- Name relations;
- salience;
- number/collection status.

This is a discourse mechanism, not a magical search capability.

## 6. Anaphora

Contextual references such as This, That, and They resolve to sufficiently salient compatible referents.

If ordinary discourse leaves several equally valid antecedents, the expression is ambiguous.

For magical execution, an anaphoric reference must already resolve objectively enough for the Command. Magic does not choose the “most likely” antecedent at execution time.

## 7. Names

New Names are ordinary Name/reference data.

A New Name can identify a person, particular object, foreign/proper term, or newly coined world concept, but it does not become a magical semantic macro.

Old Names are separately registered historical vocabulary and may have a typed semantic reading with historical mana cost.

## 8. Narrative time

Cuspell prefers explicit temporal relations to grammatical tense that silently depends on viewpoint.

Core tools include:

- Now;
- Before;
- During;
- Simultaneous;
- temporal Overlap;
- Happen;
- temporal Extent(Event).

Common past/future meanings are written compositionally with `Before` and the relevant reference point.

A discourse reference time may supply context for ordinary narration, but magical execution requires objective temporal closure.

## 9. Ongoing and completed event descriptions

For EventSpecs:

`During E T` states occurrence/holding through the supplied temporal target according to the registered During frame.

For actual Event references:

`Before E T` can place the event before a reference boundary.

Ending an ongoing resolved Event uses the EventSpec-output frame of `End`; there is no separate Stop root.

Preventing future matching occurrence is a distinct `Prevent` EventSpec with explicit scope/interval.

## 10. Habitual and generic statements

Habitual occurrence is represented through `Rate` plus contextual thresholds.

Example conceptual meaning:

`High Rate E I`

= E occurs at a contextually high rate over interval I.

Generic/characteristic prevalence over a domain can similarly be represented through Count/Ratio plus contextual High rather than a separate Generic root.

Objective magic should use explicit thresholds/domains when contextual standards are not sufficient.

## 11. Subjective evaluation

Evaluation identifies an evaluator when subjectivity matters.

`Evaluate evaluator target`

produces an ordered EvaluationValue.

The contextual one-argument form may use the discourse evaluator:

`Evaluate target`

Derived ordinary meanings include:

- preference: `More Evaluate E A Evaluate E B`;
- importance/desirability: `High Evaluate E X`.

There are no separate Prefer or ImportantTo roots in the minimized core.

## 12. Capability, intention, planning, permission, obligation

These remain distinct:

- `Can agent EventSpec` — capability;
- `Intend agent EventSpec` — intention;
- `Plan agent EventSpec` — planning relation;
- `Permitted ...` — permission/authorization;
- `Obligated ...` — obligation/duty;
- `Want ...` — desire;
- `Attempt agent EventSpec` — actual effort episode.

They are not interchangeable.

### Recommendation / “should”

There is no separate Should root.

A contextual recommendation reading is represented as:

`High Evaluate agent EventSpec`

This remains distinct from Obligated.

### Consent / refusal

There are no standalone Consent/Refuse roots.

Consent can be represented by addressed speech asserting the relevant authority-scoped permission.

Refusal can be represented by addressed speech asserting its negation.

## 13. Learning / teaching

There are no standalone Learn/Teach roots.

Acquisition is a state transition such as:

- `Begin Know learner content`;
- `Begin Can learner EventSpec`;
- `Begin Understand learner content`.

Teaching is agentive causation of the corresponding acquisition transition.

## 14. Gratitude, apology, and promises

These common social acts use existing semantic content rather than dedicated speech-act roots.

Examples conceptually:

- thanks -> addressed `Say` of `GratefulTo`;
- apology -> addressed `Say` of `RemorseFor`;
- promise -> speech of an obligation plus beginning that obligation state.

Speech does not automatically entail sincerity or later fulfillment.

## 15. Open questions

Yes/no question:

`LifeThis?`

Open question:

`:«This»:This ParentOf $«This» Self?`

The leading binder introduces the unknown and its type; the query asks for values that make the proposition true.

Another example:

`g:Location Intend You Move You $g?`

This asks for a Location value filling the goal in the represented intention.

Question formation does not itself perform magical Find/Reveal.

Embedded questions use the semantic `Question` constructor and `QuestionContent`.

## 16. Answers

`AnswerFor information question` links Information to QuestionContent.

Knowing an answer can be written compositionally by existentially binding Information that is both known and AnswerFor the question.

Answerhood is distinct from truth, evidence, topicality, or mere response speech.

## 17. Evidence, explanation, and discourse contrast

Current relations keep these distinctions:

- `EvidenceFor` — epistemic support;
- `Explains` — explanatory relation;
- `About` — topicality;
- `Contrast` — discourse tension/concession.

Plain And does not replace Contrast; EvidenceFor does not replace AnswerFor or Explains.

## 18. Counterfactuals

`Counterfactual antecedent consequent` states the consequent in the relevant contrary-to-actual alternative-history context where the antecedent holds.

It does not assert either clause in actual history and is distinct from epistemic Confidence.

The selected alternative-history relation remains contextual in ordinary discourse. A magical Command cannot rely on that context until a future objective world/hypothetical-state construction exists.

## 19. Concurrent narration

Concurrent events use the same canonical flat construction as magical commands:

`Concurrent E1 E2 ...`

Sentence end closes the group, or a standalone `:` closes it before later material.

Concurrent differs from:

- And — joint realization without required overlap;
- Sequence — ordered realization.

## 20. Discourse versus magical strictness

Ordinary discourse may use:

- anaphora;
- contextual evaluation;
- generic/habitual thresholds;
- discourse reference time;
- proper-name shorthand;
- contextual counterfactual worlds.

Before such content becomes executable magic, every execution-relevant reference/standard must resolve objectively enough for the Command.

This preserves one broad language without letting narrative context become GM guesswork.

## 21. Current boundary

The broad discourse architecture is established and has survived Yona plus cross-genre novel pressure.

Remaining work is refinement rather than a new top-level grammar family:

- better automatic multi-sentence discourse resolution;
- more explicit reference/salience modeling;
- continued parser/spec alignment;
- world-specific institutional semantics where required.
