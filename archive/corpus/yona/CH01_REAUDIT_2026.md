# Yona Chapter 1 — Current-Language Re-audit

_Status: 2026-09-27 re-audit against executable Cuspell main (202-test checkpoint)_

_Source: Yona [Cat Girl Evolution], Bedivere the Mad, Chapter 1 "Quite the Mystery"_
_Source URL: https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2525425/1-quite-the-mystery_

This file does not replace CH01_PASS_A/B/C. Those files preserve the historical failures that originally drove language design. This re-audit asks a different question: **which of those Chapter 1 failures are still failures in current Cuspell?**

The result is substantially better than the original pass. Most former core-grammar defects have been resolved.

## Former architecture gaps now resolved

The current executable language now directly supports or has regression coverage for:

- Kind predication / InstanceOf (Cat Self);
- Former versus current state and Former versus logical Not;
- Generic claims distinct from strict All;
- Habitual events distinct from one-time actuality;
- Most quantification;
- subjective evaluation (Evaluate, ImportantTo);
- preference (Like, Prefer);
- ability and modality (Can, Intend, Obligated, Permitted);
- concurrent event composition (Concurrent, Simultaneous);
- event ordering (Sequence, Before, After, During, When);
- open typed questions, including Location, Human, Method, and Explanation binders;
- Process cessation/prevention (Stop, Prevent);
- assertion/claim content remaining distinct from narrator/world truth;
- promises containing future EventSpecs;
- evidence versus causation (EvidenceFor / EvidenceAgainst);
- belief/knowledge and epistemic thresholds (Believe, Know, PossibleTo, ProbableTo, CertainTo, Confidence);
- nearest/unique/extremum selection and collection/binder typing;
- exact dimensional quantities, arithmetic, Power/Root, and registered Units.

Representative formerly failing IDs whose structural issue is now resolved include:
A01, A05, A07, A11, A13, A16, A18, A21, A23, A24, A25 (semantic core), A30, B06, B09, B12, B14 (core), B17, B19, B20, B22, B24, C01, C06, C07, C10, C12, C14, C16, C17, C21, C24-C26, C30-C31, C34-C35.

Many of these still need ordinary vocabulary or discourse referents, but they no longer require redesigning the basic expression/type system.

## Remaining Chapter 1 language gaps

### 1. Cross-sentence reference, proper names, and definite reference — DISCOURSE

This is now the largest Chapter 1 structural gap.

The language can bind variables inside an expression, but ordinary prose needs durable discourse referents across sentences:

- introduce a person as "Sally";
- later use "she", "the wife", "that fisherman", "the old man", etc.;
- resolve a definite description to a previously salient entity;
- preserve speaker/addressee shifts through dialogue.

This affects A02-A04, A08-A10, A22, A25-A29, A33; B01-B08 and many later B cases; and numerous C cases.

This should be an ordinary-language discourse layer, not magical free reference.

### 2. Aspect and graded frequency — DISCOURSE / GRAMMAR

Habitual, Repeat, During, and temporal relations cover much of the old gap, but Chapter 1 still needs compact semantics for:

- still / continue doing;
- already / yet;
- ongoing-progressive readings;
- sometimes / often / rarely rather than merely habitual;
- "kept doing X" and "was still doing X".

This remains visible in A14, A31; B08, B23; C18-C20, C22 and similar narration.

### 3. Rate and trend — GRAMMAR

The written measurement spec discusses Rate/Increasing/Decreasing, but the executable language still lacks a generic Rate/ChangeRate value and trend predicates.

This remains the main issue in B11/B26 and related C21-style prose. Current arithmetic can represent quantities once such a rate exists; the missing piece is the semantic value/function layer.

### 4. Ordered subjective evaluation — GRAMMAR

Evaluate now returns an EvaluationValue, but More/Less currently compare Quantities only.

Therefore Cuspell can say that an evaluator assigns a value, but it cannot yet generically express:

- "X is better than Y to me";
- "the best time";
- "more important";
- ordered comparisons over arbitrary evaluation scales

without defining a separate scalar Attribute/Quantity for that evaluation.

This is the remaining core issue behind A19 and B03 and some later preference/reasoning language.

### 5. Prerequisite / enabling condition distinct from ordinary If — GRAMMAR

Chapter 1 distinguishes "P must be completed before Q becomes available" from a mere material conditional.

If, Obligated, Trigger, and temporal relations cover nearby meanings, but a reusable prerequisite/enabling relation is still missing. C09 therefore remains a real semantic gap even though most of its surrounding System/game vocabulary is world data.

### 6. Near-threshold / "almost" semantics — GRAMMAR

ApproxEqual now handles quantities with explicit tolerance. That solves exact approximate measurement, but ordinary prose also needs a generic near-threshold notion such as:

- almost hungry;
- nearly tired;
- almost finished.

C23 remains unresolved as a general semantic construction.

### 7. Sense/perception as a reusable semantic family — LEXICON / SEMANTIC MOLECULE

The Information/epistemic architecture is now capable of preserving the distinction between "I did not detect X" and "X objectively has value zero." However, executable roots for sensory acts/channels such as Sense, See, Hear, Smell, and Taste are not currently registered.

Most Chapter 1 perception cases therefore look like data/lexicon work, not a new type-system problem, but a canonical Sense semantic molecule would avoid duplicating frames for every channel.

### 8. Purpose / "in order to" — MINOR GRAMMAR

Intend and MethodFor cover many goal-directed readings, but Chapter 1 contains actions whose purpose is stated without necessarily asserting a standing intention. A general event-purpose relation would make A34 and similar prose cleaner.

## Primarily lexicon/world gaps, not grammar

A large fraction of the old failures are now simply missing ordinary vocabulary or setting ontology, for example:

- Owner / spouse / profession / fisherman;
- food, fish, bread, milk;
- sleep/hunger/tiredness;
- doors/windows/open/locked;
- village/market/shore;
- body/anatomy vocabulary;
- Quest/System/Skill/game concepts;
- emotions and social evaluations;
- blood/injury/death vocabulary beyond the current Life/Exist structure.

These should not count as evidence that the grammar is unfinished.

## Chapter 1 conclusion

The historical Chapter 1 pass originally exposed many architecture defects. On current Cuspell, the majority of those defects are gone.

The unresolved language-architecture set is now concentrated in:

1. discourse reference/naming;
2. aspect and graded frequency;
3. rate/trend values;
4. ordered evaluation;
5. prerequisites/enabling conditions;
6. generic near-threshold "almost";
7. a reusable perception molecule;
8. a minor purpose relation.

That is a much smaller target than the original Chapter 1 findings.
