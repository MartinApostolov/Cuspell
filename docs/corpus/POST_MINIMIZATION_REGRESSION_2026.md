# Post-Minimization Book Corpus Regression — 2026-10-01

_Status: PASS against the previously recorded translation pressure after root minimization through checkpoint 83_

## Scope

This is a regression pass over the three book corpora already used to stress Cuspell:

1. **Yona [Cat Girl Evolution]** — all previously audited published story material through numbered Chapter 168 plus 94.5;
2. **Jane Austen, _Pride and Prejudice_** — the prior full 61-chapter public-domain pass;
3. **Mary Wollstonecraft Shelley, _Frankenstein; Or, The Modern Prometheus_ (1818)** — the prior full-novel public-domain pass.

This pass does **not** invent a new source corpus. It re-checks the semantic pressure and translation conclusions already recorded in the corpus documents against the minimized current language.

The purpose is specifically to catch regressions caused by deleting or rewriting roots before beginning another round of deeper primitive-family reduction.

## Method

The regression used four layers:

- the existing corpus records and their recorded pressure categories;
- all existing executable corpus, discourse, modality, question/knowledge, cross-genre, Yona-vocabulary, and root-minimization regressions;
- a new dedicated executable book-corpus sweep in `tests/test_corpus_post_minimization_regression.py`;
- full language/world-package validation, including the opt-in Yona package.

The dedicated sweep deliberately exercises meanings that previously depended on roots later removed by minimization, alongside retained roots whose exact semantics matter to the books.

The complete suite now runs **515 tests** and passes on Python 3.11 and 3.12.

## Result

**PASS — no semantic regression or new G17-style gap was found.**

The root-minimization work did not make any of the previously audited book meanings inexpressible.

No removed root needed to be restored.

No new semantic type, grammar family, core root, Old Name, or Yona New Name was required by this regression pass.

## Yona through Chapter 168

The previous Yona conclusions still hold.

The executable sweep re-checks representative pressure across:

- narrator/body Kind naming after noun migration;
- concurrent actions;
- density and mass/volume manipulation;
- Attempt and goal/non-success distinctions;
- sensing and explicit detection/non-detection;
- question/answer knowledge;
- discontinuous teleportation semantics through `End At` + `Begin At`;
- resource transfer after Redistribute removal;
- ordinary combat/action vocabulary;
- evasive and reflexive action;
- locomotion manner distinctions retained by the final unresolved audit.

Representative current forms include:

- former Past-style narration -> `Before ... Now`;
- detection -> `Happen Sense ...`;
- non-detection -> `Not Happen Sense ...`;
- Teleport -> simultaneous/discontinuous `End At` + `Begin At`;
- Redistribute -> `Transfer`;
- KnowAnswer -> existential known `Information` linked by `AnswerFor`;
- removed noun roots -> their current Old Names/world concepts.

The final retained action distinctions—Bite, Climb, Fall, Dodge, Reflexive, Jump, Limp, and Stab—still parse in the ordinary narrative contexts that motivated them.

The Yona package also still exposes the later published-world vocabulary needed by the prior Chapter 51–168 pass, including System/Skill/Traits/Classes, Dungeon vocabulary, Connection/Telepathy, Path Change, Epithets, Skill Morph/Merge/Evolution, First Event, Soul Weapon vocabulary, and Divine Intuition.

The earlier world-ontology questions remain exactly what they were before minimization: Soul, Divine, generic undead/reanimation, Curse/Blessing/Sacred, and similar objective setting classifications still belong to future world modeling rather than a grammar repair.

## Pride and Prejudice

The full-novel social/discourse findings still survive the minimized language.

The regression re-checks:

- Love, Trust, Respect, Admire, gratitude, shame and forgiveness;
- Reputation as an ordered social attribute;
- preference/evaluation after removal of Prefer;
- advice/ought-style evaluation after removal of Should;
- kinship after removal of SiblingOf;
- marriage/engagement/property relations;
- consent and refusal after removal of the Consent/Refuse roots;
- promise/commitment after removal of Promise;
- apology and thanks after removal of Apologize/Thank;
- learning/teaching after removal of Learn/Teach;
- successful deception after removal of Deceive;
- counterfactual reflection.

Important current compositional replacements include:

- siblinghood -> shared-parent quantification plus non-identity;
- preference -> ordered `Evaluate`;
- Should -> contextual `High Evaluate`;
- Consent -> addressed `Say` of authority-scoped `Permitted`;
- Refuse -> addressed `Say` of the negation of that permission;
- Promise -> `Say` of an `Obligated` state plus `Begin Obligated`;
- Learn -> typed `Begin Know` / `Begin Can` / `Begin Understand`;
- Teach -> agentive `Cause` of that learner-state transition;
- Apologize -> addressed `Say` of `RemorseFor`;
- Thank -> addressed `Say` of `GratefulTo`;
- Deceive -> causation of a false `Believe` state.

No social, discourse, tense, or epistemic gap reappeared.

## Frankenstein (1818)

The full-novel epistemic/causal/narrative findings also survive.

The regression re-checks:

- intention, planning and Attempt;
- failed attempts without goal success;
- causation of a Life-state transition for animation-style semantics;
- responsibility for events;
- evidence both for a proposition and for its negation;
- learning, understanding and memory;
- fear, grief, remorse, compassion and hatred;
- nested reported belief through speech;
- counterfactual reasoning;
- forgiveness.

The physical rules that make Frankenstein-style creation actually work remain world-ontology/execution questions, exactly as in the original corpus pass. The language can still describe parts, causation, Life-state transition, identity-relevant relations, knowledge, responsibility and testimony; the world model must decide what physical operations are sufficient to create or animate a living being.

Likewise, courts, legal guilt, inheritance law, marriage law, and other institutions remain world/institution data rather than missing grammar.

## Historical corpus documents

Several older corpus files intentionally preserve the vocabulary and failure history that existed when those passes were written. They therefore still mention superseded roots such as `Past`, `Tell`, `Ask`, `Prefer`, `Should`, `Consent`, `Refuse`, `Promise`, `Learn`, and others.

Those mentions are historical evidence, not current canonical syntax.

The permanent executable regression now tests the current minimized replacements, so those historical documents do not need to be rewritten merely to make the old audit history look current.

## Conclusion

The reduction work through checkpoint 83 did **not** break the three already-audited book corpora.

Current status remains:

- no new grammar family required;
- no new semantic type required;
- no restored deleted root required;
- no new corpus gap found;
- Yona world vocabulary remains loadable;
- cross-genre social/cognitive coverage remains intact.

This gives a clean regression checkpoint before any deeper second-pass family audit of the 130 surviving semantic primitive candidates.
