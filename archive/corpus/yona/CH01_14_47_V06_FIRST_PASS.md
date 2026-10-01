# Yona Chapters 1–14 + 47 — v0.6 First-Pass Stress Test

_Status: 2026-09-28 first broad sequential pass against surface v0.6; findings resolved in v0.7_

_Source: Yona [Cat Girl Evolution], Bedivere the Mad, Royal Road_

This pass expands the corpus from the previously audited Chapters 1, 2, 14, and 47 to a broad sweep of Chapters 1–14 plus Chapter 47.

The goal is twofold:

1. test whether current Cuspell can preserve the source meaning compositionally;
2. test whether the canonical v0.6 surface still reads like a plausible language rather than exposed parser notation.

This is intentionally a first pass, not an exhaustive line-by-line lexical census. Ordinary nouns, actions, anatomy, monsters, Skills, Classes, and setting-specific concepts are classified as LEXICON/WORLD unless they expose a reusable missing semantic construction.

Existing detailed passes remain authoritative historical evidence for Chapters 1, 2, 14, and 47:

- `CH01_REAUDIT_2026.md`
- `CH02_PASS_A.md`
- `CH14_REAUDIT_2026.md`
- `CH47_MANA_PASS.md`
- `RERUN_291_2026.md`

## Overall result

The language continues to converge strongly.

The sweep found **one repeated new structural gap**:

**G15 — counterfactual / alternate-history conditionals.**

Current `If` tests a Proposition in the actual evaluation context. `Past` moves a claim into earlier time, and `PossibleTo` expresses possibility. None of those constructions says:

- the antecedent is known not to have happened;
- evaluate a relevant alternative history in which it did happen;
- assert that the consequent would hold in that alternative history.

This distinction is required repeatedly in fresh chapters, including regret, missed opportunities, unreal alternatives, and comparisons between pre- and post-evolution capability.

No second new grammar/type-system blocker was found in Chapters 3–13.

### Chapter-level summary

| Chapter | Result | Main pressure |
|---|---|---|
| 1 — Quite the Mystery | structurally clean from prior rerun | discourse, ordinary vocabulary, compression |
| 2 — A Little Adventure | structurally clean from prior rerun | collections, orders, perception, ordinary vocabulary |
| 3 — Ichthyoid | **GRAMMAR: G15** | counterfactual regret/causal alternative; death, warning, responsibility |
| 4 — Abby | **GRAMMAR: G15** | missed alternative mutation; rankings, prerequisites, System records |
| 5 — Scratch | **GRAMMAR: G15** | unreal diagnostic inference; training/progression rules |
| 6 — Levels and More | structurally clean | partition/selectors, arithmetic, inference, competing goals |
| 7 — Encheloids | structurally clean | reflexive action, tactical reasoning, certainty before action |
| 8 — First Evolution | **GRAMMAR: G15** | unreal remaining-option branch; symbolic option representations |
| 9 — !@#$%^&*() House Cat | structurally clean | past possibility, thresholds, repeated movement, physical rules |
| 10 — A Strange, but Fortuitous Encounter | **GRAMMAR: G15** | pre-evolution sensory counterfactual; proportional comparison |
| 11 — Octopoids | structurally clean | mana depletion/recovery, necessary acquisition routes, unwilling target |
| 12 — High Class Kitty | **GRAMMAR: G15** | unreal mana-loss consequence; ownership/control/resource transfer |
| 13 — Silver Level Threat | structurally clean | POV shift, expected baseline, rate/trend, prediction |
| 14 — External Mana Manipulation | structurally clean from prior rerun | resource fields, Preserve, Control, Transfer |
| 47 — How Mana Works | structurally clean from prior rerun | foreign magic ontology, ordered scalar attributes, modality |

“Structurally clean” means the semantic content can be represented compositionally assuming required ordinary/world vocabulary exists. It does not mean every rendering is short or stylistically elegant.

---

## Chapter 3 — Ichthyoid

Source:
https://www.royalroad.com/fiction/129180/cat-girl-evolution-book-1-complete/chapter/2525499/3-ichthyoid

### C3-01 — uncertain perception of poor eyesight and clumsy movement

Source meaning: Yona infers that the approaching creature sees poorly because it fails to notice her, while also evaluating its movement as clumsy.

Status: **PASS-LONG / LEXICON**.

Sense/See, NotDetected, EvidenceFor, Infer/Believe, movement, and evaluator-relative judgments provide the structure. Creature anatomy and gait vocabulary are ordinary/world lexicon.

### C3-02 — tactical assessment against a much larger armed opponent

Source meaning: the opponent is many times Yona’s size and armed, so she judges a direct fight unwinnable.

Status: **PASS-LONG / LEXICON**.

Measured comparison, Have, Can/PossibleTo, Evaluate, and a hypothetical EventSpec are sufficient. Weapon vocabulary is lexicon.

### C3-03 — evidence establishes a death conclusion

Source meaning: lack of breathing plus glazed eyes and prior experience lead Yona to know Henry is dead.

Status: **PASS-LONG / LEXICON**.

Sense/Detected, EvidenceFor, Know, Life/Dead, and remembered Information are sufficient.

### C3-04 — earlier action would have prevented the present death

Source meaning: Yona believes that if she had completed the earlier quest in time, Henry would still be alive.

Status: **GRAMMAR — G15 COUNTERFACTUAL**.

`Past` plus ordinary `If` is not enough. The antecedent is known false in the actual history, while the sentence asserts a dependency in an alternative history.

This is the clearest first fresh structural failure.

### C3-05 — self-attributed fault

Source meaning: Yona treats her earlier inaction as causally/responsibly connected to the deaths.

Status: **PASS-LONG / LEXICON**.

Cause plus explicit agent/event history can preserve the causal core. A conventional Responsibility/Blame semantic molecule would improve ordinary-language compression but is not required for compositional completeness.

### C3-06 — dying request, warning, apology, and final words

Source meaning: a dying person warns Yona, asks her to flee, and conditionally asks her to deliver an apology if she escapes.

Status: **PASS-LONG / DISCOURSE / LEXICON**.

Ask/Tell, Directive/QuestionContent, If, Future, speaker/addressee context, and Sequence cover the structure. Social/action vocabulary remains lexicon.

### C3-07 — rescue plan under exclusive capability

Source meaning: Yona forms a plan because she believes she is now the only available agent capable of warning others.

Status: **PASS-LONG**.

Plan/Intend, Can, Unique/Count, and epistemic context are sufficient.

---

## Chapter 4 — Abby

Source:
https://www.royalroad.com/fiction/129180/cat-girl-evolution-book-1-complete/chapter/2525509/4-abby

### C4-01 — structured status record with known, locked, and selectable fields

Status: **PASS-LONG / WORLD**.

Information records, Name, numeric values, Unknown/Unavailable values, and setting-specific System fields are sufficient. This is data-heavy source material and is naturally record-like even before translation.

### C4-02 — Class and Profession unlock prerequisites

Status: **PASS / WORLD**.

Requires, SufficientFor/AvailableTo/Unlock, tier values, and temporal/event conditions directly fit the meaning.

### C4-03 — thousands of mutation options and evaluator-relative “best”

Status: **PASS-LONG / WORLD**.

Collections, Count, OrderedValue/Evaluate, Prefer, Should, and contextual situation parameters cover the choice discussion.

### C4-04 — recommendation justified by typical matchup and future capability

Status: **PASS-LONG / WORLD**.

Should, EvidenceFor/Because, Generic, Can, Future, and setting-specific affinity/skill data compose cleanly.

### C4-05 — a rejected earlier option would have enabled return

Source meaning: Abby points out that a mutation Yona did not choose would have allowed her to return to the mainland.

Status: **GRAMMAR — G15 COUNTERFACTUAL**.

The source requires reasoning about an unreal choice and its unreal consequence.

### C4-06 — extradimensional storage preserves the entry state of contents

Status: **PASS-LONG / WORLD**.

Containment, Transfer, state snapshots, and Preserve fit the semantic core; extradimensional storage behavior belongs to world ontology.

### C4-07 — promise of permanent loyalty

Status: **PASS-LONG / LEXICON**.

Promise/CommittedTo, Always/lifetime interval, goals, and social-role vocabulary are sufficient.

### C4-08 — narrator/POV switch to a goddess

Status: **PASS-LONG / DISCOURSE**.

Utterance/narrative contexts, proper names/references, Past/Present, and separate Minds handle the shift. The translation is more explicit than English but not structurally blocked.

---

## Chapter 5 — Scratch

Source:
https://www.royalroad.com/fiction/129180/cat-girl-evolution-book-1-complete/chapter/2525538/5-scratch

### C5-01 — probable injury used to justify resting instead of training

Status: **PASS-LONG**.

Believe/ProbableTo, Cause, Damage, Should/Prefer, and alternative EventSpecs suffice.

### C5-02 — almost falling and unprecedented hunger

Status: **PASS-LONG / LEXICON**.

Almost(EventSpec), ordered evaluation, Past experience, and hunger vocabulary fit.

### C5-03 — purposeful practice improves proficiency through several dimensions

Status: **PASS-LONG / WORLD**.

Purpose, Repeat, scalar descriptors, ChangeRate/Increasing, consistency/accuracy/versatility world attributes, and conditional thresholds fit.

### C5-04 — negotiated promise before answering

Status: **PASS-LONG / DISCOURSE**.

Promise, If, AnswerFor/Ask, future event content, and speaker/addressee context are sufficient.

### C5-05 — Trait progression depends on future evolutionary path

Status: **PASS-LONG / WORLD**.

Requires, Future, Change, PossibleTo, and conditional progression rules cover the structure.

### C5-06 — if monsters had been active, she would have awakened

Source meaning: Yona reasons from her current sensory capability that an unreal earlier monster-presence event would have caused her to wake.

Status: **GRAMMAR — G15 COUNTERFACTUAL**.

This is not merely a past conditional; the antecedent is asserted as contrary to the actual observed history.

### C5-07 — predicted future appearance of monsters

Status: **PASS-LONG**.

Expect/ProbableTo/Future and source evidence are sufficient.

---

## Chapter 6 — Levels and More

Source:
https://www.royalroad.com/fiction/129180/cat-girl-evolution-book-1-complete/chapter/2525552/6-levels-and-more

### C6-01 — enemies split into pairs and one pair is selected for clumsiness

Status: **PASS-LONG / LEXICON**.

Partition, Count, Filter, Lowest/Highest over an evaluation scale, and selection rules are sufficient.

### C6-02 — stealth and hearing limitations inferred from behavior

Status: **PASS-LONG / LEXICON**.

Sense/Hear, NotDetected, EvidenceFor, Believe, and intensity/distance relations fit.

### C6-03 — limb almost severed

Status: **PASS-LONG / LEXICON**.

Almost applied to the relevant damage/separation threshold preserves the meaning.

### C6-04 — displayed total includes a bonus component

Status: **PASS / WORLD**.

Exact arithmetic, Add, base/bonus fields, and Information records are sufficient.

### C6-05 — a stat is almost at a threshold

Status: **PASS**.

Ordered quantities plus Almost/ApproxEqual depending whether the intended standard is contextual or measured provide the distinction.

### C6-06 — logical necessity inferred from life history

Source meaning: if the speaker has never gone to bed after hard labor, then a necessary explanation is that they have never had such a day.

Status: **PASS-LONG**.

Requires/SufficientFor, Past, Never, and inference are enough. No new necessity operator is required for this passage.

---

## Chapter 7 — Encheloids

Source:
https://www.royalroad.com/fiction/129180/cat-girl-evolution-book-1-complete/chapter/2525571/7-encheloids

### C7-01 — reflexive movement occurs before conscious comprehension

Status: **PASS-LONG / LEXICON**.

Before/Sequence can order the movement event before the relevant Think/Know event. Lack of intention does not require a new event type; an EventSpec need not have an Intend relation.

### C7-02 — tactical hypothetical reasoning about attack methods

Status: **PASS-LONG / LEXICON**.

Can/PossibleTo, expected Duration/damage, If, and Plan suffice for ordinary prospective hypotheticals. These do not require alternate-history semantics unless the antecedent is explicitly contrary to fact.

### C7-03 — one claw causes a deeper cut than four claws

Status: **PASS-LONG / WORLD**.

More/Less over measured damage/depth, Count, Cause/Evidence, and comparative trials fit.

### C7-04 — two alternative origins for Tier-1 creatures

Status: **PASS-LONG / WORLD**.

Or, PossibleTo, evolution/spawn world processes, and causal influence express the alternatives.

### C7-05 — recommendation to wait until sufficiently certain no enemies remain

Status: **PASS-LONG**.

Should, CertainTo/Confidence, Know, Before/When, and Begin Evolution fit, though the surface expression is long.

### C7-06 — one character’s life is bound to another

Status: **WORLD / LEXICON**.

The dependency relation is setting ontology. If needed, it can be expressed through an explicit Rule/Trigger/Cause structure without changing the core grammar.

---

## Chapter 8 — First Evolution

Source:
https://www.royalroad.com/fiction/129180/cat-girl-evolution-book-1-complete/chapter/2525578/8-first-evolution

### C8-01 — evolution immediately causes drowsiness and collapse risk

Status: **PASS-LONG / WORLD**.

Cause, Begin/Change, Almost(EventSpec), and world-specific evolution effects suffice.

### C8-02 — evolution choices are represented by food-like signs

Status: **PASS-LONG / WORLD**.

Sign, Meaning, Name, Collection, Sense, and option Information cleanly separate the representation from the actual evolution Kind/path.

### C8-03 — many choices are combined into one invalid/unclear evolution path

Status: **PASS-LONG / WORLD**.

Collections plus setting-specific combination/Transform rules can represent the data. No generic grammar rule needs to guess how thirteen incompatible options combine.

### C8-04 — if any choices remained, support would force a single choice

Source meaning: the support worker describes what he would do under an antecedent that is known false because all choices were consumed.

Status: **GRAMMAR — G15 COUNTERFACTUAL**.

This is another explicit unreal branch.

### C8-05 — combination might cause an explosion

Status: **PASS-LONG**.

PossibleTo/ProbableTo over a future EventSpec and evidence/uncertainty are sufficient.

### C8-06 — painted doors/windows are representations rather than functional openings

Status: **PASS-LONG / LEXICON**.

Sign/ShapeLike/Form can distinguish an image shaped like a Door/Window from InstanceOf Door/Window.

---

## Chapter 9 — !@#$%^&*() House Cat

Source:
https://www.royalroad.com/fiction/129180/cat-girl-evolution-book-1-complete/chapter/2525593/9-house-cat

### C9-01 — one action is explicitly first before another is acknowledged

Status: **PASS**.

Sequence/Before and First over an ordered event sequence fit directly.

### C9-02 — all stats more than doubled; some more than tripled

Status: **PASS / WORLD**.

All/Some, Multiply, More, BeforeValue/current values, and stat collections compose cleanly.

### C9-03 — explosion was possible but did not occur

Status: **PASS-LONG**.

Past PossibleTo(EventSpec) plus explicit Not Happen preserves past possibility without claiming a counterfactual dependency.

This is importantly different from G15.

### C9-04 — nested Traits produce threshold-dependent stat effects

Status: **PASS-LONG / WORLD**.

Contains/includes relations, scalar thresholds, If/Whenever, and stat Change/derived-value world rules suffice.

### C9-05 — repeated teleports preserve falling momentum

Status: **PASS-LONG / WORLD**.

Repeat, Move/Teleport, velocity/momentum world rules, and future Damage consequences fit. The physical law belongs to the world package.

### C9-06 — determination to improve Blink until a travel capability is reached

Status: **PASS-LONG**.

Intend/Plan, Purpose, Repeat/Continue, Can, and a terminal capability condition can express the core, though a compact Until surface form would improve readability.

---

## Chapter 10 — A Strange, but Fortuitous Encounter

Source:
https://www.royalroad.com/fiction/129180/cat-girl-evolution-book-1-complete/chapter/2525620/10-a-strange-but-fortuitous-encounter

### C10-01 — attack depth scales roughly proportionally with stat increase

Status: **PASS-LONG / WORLD**.

Ratio, Multiply, ApproxEqual, BeforeValue/AfterValue, and measured damage/depth fit.

### C10-02 — skill upgrade recommendation based on current stat distribution

Status: **PASS-LONG / WORLD**.

Evaluate/OrderedValue, Should, More/Less, Because/EvidenceFor, and stat world data are sufficient.

### C10-03 — sound detectable now but not before evolution

Source meaning: Yona judges that her earlier pre-evolution self would not have been capable of detecting a sound she can now detect.

Status: **GRAMMAR — G15 COUNTERFACTUAL**.

A mere past statement about actual detection is wrong; the source compares current capability with an unreal replay of the same stimulus under the earlier state.

### C10-04 — unknown-level marker supports a weak-enemy inference

Status: **PASS-LONG / WORLD**.

UnknownValueOf, Count/Sign structure, EvidenceFor, Infer/Believe, and setting-specific display rules suffice.

### C10-05 — camouflage matches bark in color/texture but can be detected under closer observation

Status: **PASS-LONG / LEXICON**.

Equal/ApproxEqual over ColorOf and texture attributes, Change, Sense/See, Distance, and visibility thresholds fit.

### C10-06 — long-term decision by a distant observer

Status: **PASS-LONG / DISCOURSE**.

Separate narrative context, Evaluate, Expect, Plan/Intend, future conditions, and proper references handle the POV shift.

---

## Chapter 11 — Octopoids

Source:
https://www.royalroad.com/fiction/129180/cat-girl-evolution-book-1-complete/chapter/2529399/11-octopoids

### C11-01 — repeated attempted grabs, evasions, and failed attacks

Status: **PASS-LONG / LEXICON**.

Sequence/Concurrent, Move, Intend/Attempt decomposition, Almost, and ordinary combat verbs are enough. A dedicated Try/Attempt root remains a useful compression candidate but not a completeness requirement.

### C11-02 — camouflage changes after leaving the tree

Status: **PASS-LONG / LEXICON**.

ColorOf, texture attributes, Change, Before/After, and location conditions fit.

### C11-03 — mana depletion after repeated magical Skills, with estimated recovery time

Status: **PASS / WORLD**.

Mana quantity, ChangeBy/Transfer, Repeat, Duration, OccurrenceRate/ChangeRate, and probable recovery duration are sufficient.

### C11-04 — teleporting an unwilling creature

Status: **PASS-LONG / WORLD**.

Move/Teleport plus Not Want(target, event) preserves unwillingness. Permission/consent can be added when the source specifically asserts it, but is not required merely by “against its will.”

### C11-05 — meditation could accelerate resource recovery

Status: **PASS-LONG / WORLD**.

Can, Cause, ChangeRate/Increasing, Purpose, and resource quantity fit.

### C11-06 — Traits/Skills can be acquired only through a limited set of routes

Status: **PASS-LONG / WORLD**.

Requires plus Or over the permitted acquisition routes is compositionally sufficient.

### C11-07 — exception phrased as “unless”

Status: **PASS-LONG**.

Ordinary “unless P, Q” can be represented as an explicit If/Not relation without a new primitive.

---

## Chapter 12 — High Class Kitty

Source:
https://www.royalroad.com/fiction/129180/cat-girl-evolution-book-1-complete/chapter/2534518/12-high-class-kitty

### C12-01 — selfish support because a stronger Yona benefits Abby

Status: **PASS-LONG / WORLD**.

Because/Cause, Beneficiary, Evaluate/ImportantTo, and the life-binding world relation are sufficient.

### C12-02 — Tier threshold grants Class eligibility

Status: **PASS / WORLD**.

Requires, AvailableTo, Begin/Unlock, and tier values directly fit.

### C12-03 — Class choice is irreversible except under divine intervention

Status: **PASS-LONG / WORLD**.

Requires(Intervention, ChangeClass), Prevent/default rule structure, and temporal scope are enough. “Divine interference” is world ontology.

### C12-04 — meditation doubles mana recovery rate

Status: **PASS**.

ChangeRate, Ratio/Multiply, Mana quantity, During, and Happen fit directly.

### C12-05 — Skill controls only the user’s mana while it is external

Status: **PASS-LONG / WORLD**.

Have/source relation, Control, Outside, BodyOf, DistributionOf, and scope restrictions express the core.

### C12-06 — owned mana is shaped into a tool that moves ambient mana

Status: **PASS-LONG / WORLD**.

Control, Form/ShapeLike, Move/Transfer, Touch, Distribution, and source/destination resource structure fit. This reuses the architecture already pressure-tested in Chapter 14.

### C12-07 — nearly losing mana would have wasted prior meditation time

Source meaning: after recovering the mana, Yona reflects on the unreal consequence that would have followed if the loss had completed.

Status: **GRAMMAR — G15 COUNTERFACTUAL**.

This again requires an unreal alternative history, not merely Future/Past possibility.

### C12-08 — several possible explanations for an apparently impossible result

Status: **PASS-LONG / WORLD**.

PossibleTo, Or, EvidenceFor, Infer/Believe, and setting-specific rules cleanly represent the competing hypotheses.

---

## Chapter 13 — Silver Level Threat

Source:
https://www.royalroad.com/fiction/129180/cat-girl-evolution-book-1-complete/chapter/2540190/13-silver-level-threat

### C13-01 — hard POV shift to a new group of named characters

Status: **PASS-LONG / DISCOURSE**.

Narrative context, proper names, That/They-style discourse references, speaker/addressee context, and reference time handle the shift.

### C13-02 — three independent signs indicate the village is abnormal

Status: **PASS-LONG / LEXICON**.

Absence/quantification, Sense/See, blood evidence, Mana density, And, EvidenceFor, and Infer/Know are sufficient.

### C13-03 — mana density is higher than the contextually expected baseline

Status: **PASS-LONG**.

This can be expanded compositionally by introducing the expected/normal comparison value through Expect/Generic/world-model information and comparing actual Density with More. A compact ExpectedValue/NormalValue molecule could shorten this pattern but is not required.

### C13-04 — mana density is currently increasing

Status: **PASS**.

ChangeRate and Increasing over an interval fit directly.

### C13-05 — if untreated, the disturbance may become permanent, spread, and worsen

Status: **PASS-LONG / WORLD**.

If, Future, PossibleTo, Cause, Change, Persist/Always where appropriate, and world propagation rules are sufficient.

### C13-06 — command to retreat while a stronger fighter remains

Status: **PASS-LONG / LEXICON**.

Directive/Tell, Obligated/Should depending force, Sequence/Concurrent, and combat vocabulary fit.

### C13-07 — a fighter is later than expected

Status: **PASS-LONG**.

Expect plus Before/After and the reference time express the epistemic “should have arrived by now” reading without overloading recommendation-Should.

### C13-08 — characters conclude survival is no longer possible

Status: **PASS-LONG / DISCOURSE**.

Believe, Not PossibleTo, evidence, and group discourse context suffice.

---

## Chapters 1, 2, 14, and 47

The 291-test rerun already established structural translation completeness for these chapters after the earlier gap-closure work.

This v0.6 sweep did not uncover a reason to reverse that conclusion.

Their remaining pressure is still primarily:

- ordinary/world vocabulary;
- compression;
- explicit discourse-reference forms;
- stylistic/pragmatic loss;
- surface readability under nested semantic structures.

---

# New structural finding: G15 counterfactual / alternate-history semantics

## Why current operators are insufficient

Current Cuspell has:

- `If(condition, consequent, alternative?)` — evaluates a condition in the actual evaluation context;
- `Past(X)` — places X before the reference/utterance time;
- `PossibleTo(P)` — modal possibility;
- Cause/Evidence/Expect/Believe — causal and epistemic relations.

Those can express:

- an actual past conditional;
- a past possibility that did not occur;
- a causal claim about actual events;
- an expectation about a future event.

They do **not** by themselves express:

> In a relevant alternative history where a known-false antecedent had held, the consequent would have held.

That requires an explicit alternate-history/counterfactual semantic construction.

## Repeated corpus pressure

Fresh examples occur in at least:

- Chapter 3 — doing the quest earlier would have left Henry alive;
- Chapter 4 — choosing a rejected mutation would have enabled return;
- Chapter 5 — if enemies had been active during sleep, Yona would have awakened;
- Chapter 8 — if any evolution options remained, support would force a single choice;
- Chapter 10 — the same faint sound would not have been detectable before evolution;
- Chapter 12 — losing the recovered mana would have wasted the prior meditation.

This is repeated enough that it should be treated as a real language feature rather than a one-off paraphrase problem.

## Design constraint before implementation

Do not simply redefine ordinary `If` to cover this.

Actual-world conditional control is already important for magic. Counterfactual reasoning needs separate semantics because false antecedents must not make arbitrary consequences vacuously acceptable.

A later design pass should decide whether Cuspell uses:

- a contextual ordinary-language Counterfactual operator;
- an explicit hypothetical-history/world constructor;
- an intervention-style construction;
- or a layered pair where ordinary discourse has a contextual form but magical/objective use requires an explicit alternative-state specification.

No implementation decision is made by this corpus pass.

---

# Surface/readability findings under v0.6

The v0.6 changes are a clear improvement.

Short local predicates, ordinary conjunction, and event chains no longer force visible AST punctuation:

- tight adjacency handles forms like `LifeThis`;
- `A And B` reads like language;
- `Sequence E1 E2 ...` reads like an ordered clause chain;
- sentence-final `.` / `?` / `!` is substantially more natural than leading mood syntax;
- actual Collection syntax remains justified when a group is genuinely one value.

The fresh prose nevertheless provides concrete pressure for the remaining temporary-looking forms.

## S1 — Or should probably mirror And

The chapters repeatedly use ordinary alternatives:

- alternative creature origins;
- alternate Skill/Trait acquisition routes;
- multiple possible explanations;
- mutually exclusive choices.

If `Or` remains visibly prefix/collection-shaped while `And` is infix, ordinary prose has an unnecessary asymmetry.

Corpus evidence now supports the deferred surface candidate:

`LifeThis Or MagicThis.`

This is a surface-language improvement, not a semantic change.

## S2 — Concurrent should probably mirror Sequence

Combat chapters repeatedly describe overlapping actions: one creature attacks while another dodges, group members act simultaneously, and resource recovery occurs during another process.

If `Concurrent` still exposes collection-like grouping while `Sequence` is flat, frequent action prose falls back toward parser notation.

Corpus evidence now supports the deferred candidate:

`Concurrent EventA EventB!`

with a zero-mana `ConcurrentEnd` only when the concurrent group must close before later material.

Again, this is a surface change, not a semantic redesign.

## S3 — binders and role marks remain visibly transliterational

Forms such as:

- `a:Human`
- `$a`
- `:authority`
- `:source`

remain useful and objective, but generalized rules and dialogue-heavy permission/knowledge passages make them visibly look like formal notation.

This does not currently justify changing them. It does confirm that final rune/glyph design should make these grammatical functions look native rather than programming-language-like.

## S4 — deeply nested epistemic/deontic clauses remain long

Examples such as:

- recommending that someone wait until they are sufficiently certain a condition holds before starting another event;
- reporting a directive about a future conditional event;
- explaining why one option is likely better for an evaluator under a particular situation

are expressible, but can become PASS-LONG.

This is currently a compression/readability problem, not a completeness problem.

## S5 — System/status passages naturally look data-like

Chapters 4, 9, and 12 contain literal structured status displays. Cuspell can represent them as Information records/field propositions, but they should not be used as evidence that all ordinary prose ought to look like records.

The source itself changes register into data display, so a data-like Cuspell rendering is acceptable there.

---

# Lexicon/world queue exposed by Chapters 3–13

The pass reinforces rather than overturns the current separation between grammar and vocabulary.

High-volume future lexicon/world work includes:

- common combat actions: grab, dodge, bite, claw, stab, limp, sever;
- anatomy: eyes, wrists, tendons, organs, skin, bones, stomach;
- social/emotional language: apology, blame/responsibility, embarrassment, stubbornness;
- environmental nouns: tree, branch, shore, village, dock, road;
- monster/animal Kinds;
- weapons;
- System/Skill/Class/Species/Trait/Affinity/Level/Tier/Proficiency concepts;
- exact skill effects and upgrade rules;
- mana ownership/resource behavior;
- normal/expected environmental baselines;
- conventional action-compression roots such as Try/Attempt.

These should continue to be added only as their semantic families are needed.

---

# First-pass conclusion

The broad 1–14 + 47 sweep does **not** suggest another foundational rewrite.

Instead it produces a narrow result:

1. current Cuspell remains structurally strong across a much wider prose sample;
2. **G15 counterfactual/alternate-history semantics is the one repeated new semantic gap**;
3. `Or` and `Concurrent` now have real corpus evidence for the same flat surface treatment already given to `And` and `Sequence`;
4. binders/role markers remain acceptable formal transliteration but should be watched for final-language aesthetics;
5. most other failures are ordinary vocabulary, world ontology, compression, or style.

Recommended next step:

- design G15 without weakening the objective actual-world meaning of `If`;
- then add executable regressions for representative Chapter 3/5/10 cases;
- after that, decide whether to apply the now-evidence-backed `Or` and `Concurrent` surface cleanup;
- continue fresh corpus pressure from Chapter 15.


---

# Post-pass v0.7 resolution

The two follow-up tasks identified by this pass are now implemented.

## G15

`Counterfactual(antecedent, consequent)` supplies the missing contrary-to-actual alternate-history relation without changing actual-world `If`.

The root is contextual ordinary-language semantics. A magical Command containing it remains SemanticallyIncomplete until an explicit objective hypothetical-history construction exists.

## Surface

The corpus-backed surface candidates are now canonical:

- `A Or B` for proposition disjunction;
- explicit grouping when And and Or are mixed;
- `Concurrent E1 E2 ...` for concurrent events;
- `ConcurrentEnd` only when later material follows.

The resulting canonical transliteration is surface syntax v0.7.

Executable regressions pass on Python 3.11 and 3.12 as part of the 328-test suite.
