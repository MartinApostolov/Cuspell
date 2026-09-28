# Yona Chapters 1–14 + 47 — v0.7 Full Source Rerun

_Status: 2026-09-28 fresh full-source semantic rerun against Cuspell v0.7; Attempt gap closed during rerun_

_Source: Yona [Cat Girl Evolution], Bedivere the Mad, Royal Road_

This rerun is deliberately stricter than the earlier broad pass.

The earlier Chapter 1/2/14/47 audits and the v0.6 Chapters 1–14 + 47 sweep were useful discovery passes, but this rerun went back to the live chapter text and asked again, from the beginning:

> Can current Cuspell preserve the semantic core and ordinary-language content of the passage, rather than merely paraphrasing around a missing meaning?

The source text itself remains external; this repository stores only locators, semantic paraphrases, findings, and short identifying descriptions under the corpus protocol.

## Sources reread

1. Chapter 1 — "Quite the Mystery"  
   https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2525425/1-quite-the-mystery
2. Chapter 2 — "A Little Adventure"  
   https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2525481/2-a-little-adventure
3. Chapter 3 — "Ichthyoid"  
   https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2525499/3-ichthyoid
4. Chapter 4 — "Abby"  
   https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2525509/4-abby
5. Chapter 5 — "Scratch"  
   https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2525538/5-scratch
6. Chapter 6 — "Levels and More"  
   https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2525552/6-levels-and-more
7. Chapter 7 — "Encheloids"  
   https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2525571/7-encheloids
8. Chapter 8 — "First Evolution"  
   https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2525578/8-first-evolution
9. Chapter 9 — "!@#$%^&*() House Cat"  
   https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2525593/9-house-cat
10. Chapter 10 — "A Strange, but Fortuitous Encounter"  
    https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2525620/10-a-strange-but-fortuitous-encounter
11. Chapter 11 — "Octopoids"  
    https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2529399/11-octopoids
12. Chapter 12 — "High Class Kitty"  
    https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2534518/12-high-class-kitty
13. Chapter 13 — "Silver Level Threat"  
    https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2540190/13-silver-level-threat
14. Chapter 14 — "External Mana Manipulation"  
    https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2540191/14-external-mana-manipulation
15. Chapter 47 — "How Mana Works"  
    https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2745177/47-how-mana-works

## Overall result

The rerun found **one real omission** in the current semantic inventory:

### G16 — Attempt / actual goal-directed effort

Earlier notes treated Try/Attempt as optional lexical compression. That was too optimistic.

The corpus repeatedly distinguishes:

- intending to do something;
- actually trying to do it;
- trying and failing;
- trying and partly succeeding;
- trying and succeeding.

Current `Intend(agent, goal)` only says that the agent has the goal as an intention. It does not entail that an effort episode happened.

The goal EventSpec itself is also insufficient because asserting the goal would incorrectly assert success.

Therefore the missing semantic core is:

`Attempt(agent: Entity, goal: EventSpec) -> EventSpec`

Meaning:

> the agent undertakes a real goal-directed effort episode aimed at realizing the goal.

Attempt does **not** entail that the goal occurs.

This is now implemented and executable.

No second new grammar/type-system gap was found.

After adding Attempt, the rerun found **no known remaining semantic-core or ordinary-language completeness blocker in Chapters 1–14 and 47**, assuming the necessary ordinary and setting-specific lexical/world entries are available.

This does not mean every source sentence has a short one-to-one rendering. Some meanings remain PASS-LONG and some style/pragmatic distinctions remain deliberately layered.

## Why Attempt is not just Intend

The distinction matters mechanically.

Conceptually:

`Intend Self MoveSelfHere.`

says the agent has moving-here as an intention.

`Past Attempt Self MoveSelfHere.`

says a real effort episode occurred.

The latter remains compatible with failure:

`Past Attempt Self MoveSelfHere And Not Past MoveSelfHere.`

and also with success:

`Past Attempt Self MoveSelfHere And Past MoveSelfHere.`

More exact success/failure descriptions can use the salient Attempt Event and its interval to constrain whether the embedded goal occurs during that attempt.

A future compact `Succeed`, `Fail`, or `Manage` molecule may shorten this, but the core distinction is now compositional.

For magic, `Attempt Self MoveSelfHere!` commands an attempt. It does not silently guarantee Move succeeds. If the caster wants the Move itself, the caster must command Move.

---

# Chapter-by-chapter rerun

## Chapter 1 — Quite the Mystery

**Result: PASS-LONG / LEXICON / WORLD. No new grammar gap after G16.**

Rechecked:

- former/current identity and body state;
- generics and habitual routines;
- food, sleep, hunger, and graded state;
- names, social roles, definite reference, and dialogue;
- questions and unknown methods;
- decreasing spawn/resource rates;
- perception versus objective absence;
- evidence/inference;
- System prerequisites and unlocks;
- promises and future commitments;
- almost-threshold language;
- ongoing attempts/effort such as trying to ignore or accomplish an action.

The new Attempt root is the only correction needed from this rerun.

## Chapter 2 — A Little Adventure

**Result: PASS-LONG / LEXICON / WORLD.**

Rechecked:

- attempted grabbing/coaxing versus successful movement;
- simultaneous preparation;
- commands/orders;
- names and formerly introduced people;
- evidence from weapons/behavior;
- distance and choice evaluation;
- perception;
- repeated impacts and almost falling;
- fixed-size pairing through Partition;
- conditional standing orders;
- priority/evaluation;
- unknown displayed values;
- interrupted communication.

The earlier collection and discourse fixes remain sufficient.

## Chapter 3 — Ichthyoid

**Result: PASS-LONG / LEXICON.**

Rechecked:

- poor-vision inference;
- tactical capability judgments;
- repeated attempted attacks;
- blood loss/death;
- blame/responsibility and causal history;
- dying requests and warnings;
- unique available rescuer;
- the contrary-to-fact claim that earlier quest completion would have changed Henry's survival.

Counterfactual v0.7 resolves the alternate-history meaning. Attempt resolves the repeated failed attack effort.

## Chapter 4 — Abby

**Result: PASS-LONG / WORLD.**

Rechecked:

- structured status information;
- locked/available fields;
- prerequisites and unlocks;
- thousands of alternatives;
- evaluator-relative best/recommendation;
- affinity/skill world rules;
- preservation in storage;
- promises and permanent commitment;
- failed walking attempts;
- goddess POV/context shift;
- unreal rejected choices.

Counterfactual and Attempt cover the previously awkward cases.

## Chapter 5 — Scratch

**Result: PASS-LONG / WORLD / LEXICON.**

Rechecked:

- probable injury and recommendation;
- almost falling;
- purposeful practice;
- consistency/accuracy/versatility;
- negotiated promise before explanation;
- evolution-dependent Trait progression;
- actual practice attempts versus mere intention;
- past regret ("should have" style) under discourse reference time;
- counterfactual inference about whether enemies would have awakened Yona.

No new modal operator is required for the chapter: past-directed ordinary Should can be interpreted at the established discourse reference time.

## Chapter 6 — Levels and More

**Result: PASS-LONG / WORLD.**

Rechecked:

- exact Count and pair selection;
- weakest/clumsiest pair selection;
- stealth/hearing inference;
- almost-severed anatomy;
- attempts that miss;
- a Skill attempting to activate but failing;
- exact status arithmetic;
- base-plus-bonus values;
- almost reaching a threshold;
- "already/still" temporal content;
- necessity inferred from life history.

Attempt is important here because the Skill activation attempt and the failed intended result are explicitly distinguished.

## Chapter 7 — Encheloids

**Result: PASS-LONG / WORLD / LEXICON.**

Rechecked:

- reflexive movement before conscious comprehension;
- prospective tactics;
- "unless" as explicit If/Not structure;
- training/grinding attempts;
- changed damage after proficiency;
- Tier threshold;
- recommendation to wait until safe;
- life-binding world rule;
- a plan whose first step succeeds and later steps fail;
- one creature trying to help another and managing only part of the intended result.

Attempt plus ordinary goal occurrence/non-occurrence captures the effort/outcome split. `Until` remains compositional with an explicit interval endpoint/condition.

## Chapter 8 — First Evolution

**Result: PASS-LONG / WORLD.**

Rechecked:

- evolution options represented by food-like Signs;
- representation versus actual evolution identity;
- combining many options;
- System resolution/calibration;
- a known-false remaining-option branch;
- trying a dangerous combination function;
- possible explosion;
- fake painted doors/windows.

Counterfactual handles the unreal option branch. Attempt handles attempted resolution/combination without asserting success.

## Chapter 9 — !@#$%^&*() House Cat

**Result: PASS-LONG / WORLD / DISCOURSE.**

Rechecked:

- first/next ordered actions;
- more-than-double/triple comparisons;
- past possibility without counterfactual dependency;
- repeated teleport practice and retained momentum;
- intention to train until a capability threshold;
- Class instability;
- hard POV shift to Oakville;
- exact small counts and "only" restrictions;
- permissions and prerequisites;
- attempted jumping/training.

The chapter confirms that Past possibility and Counterfactual must remain distinct.

## Chapter 10 — A Strange, but Fortuitous Encounter

**Result: PASS-LONG / WORLD.**

Rechecked:

- proportional stat/damage comparison;
- evaluator-relative Skill recommendation;
- pre-evolution sensory counterfactual;
- weak-enemy inference from unknown-level signs;
- camouflage similarity;
- Blink combat attempts with misjudged timing and partial success;
- longer-term observer planning.

Attempt is required to preserve "tried to teleport to X" when the actual teleport endpoint differed from the intended one.

## Chapter 11 — Octopoids

**Result: PASS-LONG / WORLD.**

Rechecked:

- coordinated attempts to grab;
- camouflage;
- healing and food;
- trying Snatch on a living target and discovering that it works;
- mana depletion/recovery;
- unwilling teleport;
- recommendation not to fight;
- possible meditation acceleration;
- restricted routes for Skill/Trait acquisition;
- "unless" exception structure.

No new exception operator is required: the chapter's unless meanings normalize to explicit If/Not structures.

## Chapter 12 — High Class Kitty

**Result: PASS-LONG / WORLD / DISCOURSE.**

This chapter was especially useful on rerun.

Rechecked:

- selfish support and life-binding;
- Class eligibility;
- irreversible choice except under an exceptional condition;
- mana recovery rate;
- External Mana Manipulation ownership restriction;
- multiple attempted recovery methods where some do nothing, one slightly works, and later methods work differently;
- past-directed "should have" criticism;
- expected capability from a Skill description;
- counterfactual near-loss of mana;
- method effectiveness;
- resistance and resource transfer;
- failed chase;
- future threat prediction.

Attempt closes the major missed distinction.

Past-directed Should does not require a new tense-on-modality grammar in these passages because the connected dialogue establishes the earlier reference situation. Epistemic "should have" cases can instead normalize to Expect / Requires / SufficientFor / evidence structures where appropriate.

## Chapter 13 — Silver Level Threat

**Result: PASS-LONG / WORLD / DISCOURSE.**

Rechecked:

- POV shift to a new group;
- three independent signs of danger;
- missing population and visible blood;
- mana density above an expected/normal baseline;
- increasing mana density;
- scouting priorities;
- "only fight if necessary";
- retreat command;
- expected arrival deadline;
- inability to fight back before death;
- final belief that survival is impossible.

"Only fight if necessary" can be expanded with the relevant goal and `Requires`/permission structure. "Ryan should have joined us by now" is epistemic expectation and temporal deadline, not recommendation-Should.

No new operator is required.

## Chapter 14 — External Mana Manipulation

**Result: PASS-LONG / WORLD.**

Rechecked:

- unknown method/knowledge;
- divine-world hypotheses;
- Class progression rules;
- mana amount/density/distribution;
- preserving size while changing density;
- moving resource from center to edge;
- ShapeLike/Form versus actual Hand Kind;
- Touch versus Joined;
- Control loss after separation;
- repeated attempts to form/manipulate parts;
- partial success/failure;
- sensing mana without proving absence when not sensed.

The existing field/distribution and control architecture remains sufficient. Attempt closes the repeated effort/outcome wording.

## Chapter 47 — How Mana Works

**Result: PASS-LONG / WORLD.**

Rechecked:

- foreign mana-system explanation;
- potency versus amount;
- stability/volatility;
- ordered comparisons;
- preserving mana amount while changing potency;
- recommendations;
- explicit permission/authority;
- analogies;
- training through repeated attempts;
- learning Skills;
- stable versus volatile attribute behavior;
- construct control;
- comparative smoothness;
- telepathic communication;
- storing/releasing spells and regaining control.

The chapter repeatedly uses "try" while teaching a technique, confirming Attempt as a reusable semantic molecule rather than just an English wording preference.

---

# Rechecked suspected gaps that did NOT require new grammar

## Only

The corpus uses "only" in several semantic roles:

- exactly one member;
- unique capable person;
- exact small Count;
- restriction to one permitted option/source;
- "only if" necessary condition;
- focus/emphasis.

All truth-conditional uses in the audited chapters can be expanded with Count/Unique, All/Not, Filter, Requires, explicit domain restriction, or equivalent existing structures.

A compact generic Only root remains useful compression, but it is not a completeness blocker here.

## Still / already / yet

These can be expanded with:

- Present/Past;
- Completed;
- Ongoing/Continue;
- Always over an explicit interval;
- explicit Not + temporal relation.

They remain good compression candidates but did not expose a missing semantic distinction.

## Unless

The audited uses normalize to explicit conditional negation such as "if not P, Q" or a restriction using Requires/Prevent.

No primitive Unless is required.

## Until

The audited cases have an identifiable endpoint/event/condition and can use an explicit TimeInterval, Before/When, or equivalent event-boundary structure.

No primitive Until is required.

## Instead

Core truth conditions can be represented by the chosen event plus explicit non-occurrence/rejection of the alternative, with Contrast where the discourse relation matters.

Most residual effect is discourse/style.

## Even / emphasis / scalar surprise

The underlying proposition and ordered comparison survive. The focus/surprise contribution is style/pragmatics unless explicitly needed as Information about an evaluator's expectation.

## Should have

The reread contains several different English "should have" readings.

They should not be forced into one operator:

- past recommendation/regret -> contextual Should evaluated at the established past discourse reference situation;
- expected arrival/state -> Expect plus temporal relations;
- a result that was expected from a rule/capability -> Requires/SufficientFor/Expect/evidence;
- counterfactual consequence -> Counterfactual where appropriate.

The current architecture can keep these readings distinct.

## Succeed / fail / manage / work

After adding Attempt, the semantic cores are compositional:

- Attempt = effort happened;
- goal occurrence in the relevant attempt episode = success;
- goal non-occurrence in that episode = failure;
- method/effectiveness can additionally use Cause/SufficientFor/ChangeRate/etc.

Compact Succeed/Fail/Manage/Work molecules may be worthwhile ordinary vocabulary, especially for readability, but the audited chapters do not require new grammar for them.

---

# Correction to earlier audits

`RERUN_291_2026.md` classified "compact Attempt/Try lexicalization" as non-blocking compression.

The broader full-source rerun shows that classification was too weak.

Without Attempt, Cuspell could represent:

- intention without action; or
- successful goal occurrence;

but not directly represent the middle truth condition:

> a real effort episode occurred, whether or not the goal succeeded.

The historical file is preserved; this rerun supersedes that specific conclusion.

---

# Final conclusion after G16 closure

After the Attempt addition and executable regressions:

- no known grammar/type-system gap remains in Chapters 1–14 + 47;
- no known reusable semantic-molecule gap remains that blocks semantic-core or ordinary-language translation of the audited passages;
- remaining missing material is ordinary/world-specific vocabulary, compression, automatic discourse resolution, or style/pragmatics;
- surface v0.7's infix Or and flat Concurrent survived the full rerun without exposing a new ambiguity;
- Counterfactual remained necessary and distinct from Past possibility/ordinary If.

The full executable suite passes **334 tests** on Python 3.11 and Python 3.12 at this checkpoint.

The next useful corpus pressure is therefore fresh source material beginning with Chapter 15, not speculative expansion of the grammar.
