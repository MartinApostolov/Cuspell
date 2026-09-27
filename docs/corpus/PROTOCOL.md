# Corpus Translation Stress-Test Protocol

_Status: working methodology v0.1_

This protocol uses real prose to test whether Cuspell can function as a language rather than only as a spell-description notation.

## Purpose

A parser/type-checker tests whether the written rules are internally formal enough.

A translation corpus tests whether the language can express ordinary human meanings that were not chosen to fit the existing grammar.

The two tests are complementary.

## Translation pipeline

For each source unit:

1. identify the source locator;
2. write a semantic paraphrase rather than copying large source passages;
3. identify discourse context/referents;
4. attempt a Cuspell translation;
5. produce a literal English back-translation from the Cuspell expression alone;
6. compare the back-translation with the source meaning;
7. classify the result;
8. record any missing vocabulary/grammar or ambiguity;
9. update the language only when the problem is genuinely structural;
10. convert resolved defects into permanent regression cases.

## Status labels

- **PASS** — current Cuspell expresses the meaning cleanly.
- **PASS-LONG** — meaning is expressible, but unnaturally verbose; candidate for lexicalization/grammar compression.
- **LEXICON** — grammar works but a useful lexical entry is missing.
- **GRAMMAR** — required semantic/grammatical construction is missing.
- **DISCOURSE** — failure concerns anaphora, salience, tense/aspect, speaker context, or other discourse machinery.
- **WORLD** — expression depends on setting ontology/physics/metaphysics not yet supplied.
- **SOURCE-AMBIGUOUS** — the source itself leaves multiple readings; translation must choose one.
- **CUSPELL-DEFECT** — current rules produce ambiguity, contradiction, or an unintended meaning.
- **STYLE-LOSS** — propositional meaning survives but humor, tone, metaphor, emphasis, irony, rhythm, etc. are not yet represented.

A unit may receive more than one label.

## What to store

For copyrighted external sources, the repository should store:

- source title/author;
- chapter URL;
- chapter/paragraph or line locator;
- short source snippets only when needed for identification;
- semantic paraphrase;
- Cuspell attempt;
- literal back-translation;
- classification;
- design finding.

Do not mirror full chapters into this repository.

## Translation levels

Each test may distinguish three targets.

### Semantic core

Truth conditions / event structure / participants / temporal relations.

This is the minimum requirement for a formal magical language.

### Ordinary-language content

Speaker perspective, modality, genericity, tense/aspect, reference, evaluation, reported speech, etc.

This is required if Cuspell is to function as a broader naturalistic language.

### Style/pragmatics

Humor, irony, register, emphasis, politeness, metaphor, narrative voice.

These can be layered later and should not block core semantic testing.

## Regression rule

Whenever a corpus sentence exposes a structural defect and the language is changed to resolve it:

- add or update the relevant normative spec;
- add a regression example to the semantic stress tests or a corpus-specific executable test later;
- record the reason in the corpus file;
- do not delete the original failure history.

## Initial corpus

First source:

**Yona [Cat Girl Evolution]**, Bedivere the Mad, Royal Road.

Reason for selection:

- first-person narrative;
- dialogue;
- fantasy ontology;
- mana and magic;
- body transformation/evolution;
- game/system concepts;
- combat;
- social and mundane scenes.

The first pass starts with Chapter 1 for general discourse pressure, then jumps to magic/evolution-heavy chapters before attempting broad sequential coverage.
