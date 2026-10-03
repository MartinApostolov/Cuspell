# Checkpoint 110 — Parameterized Historical Lexicalization Audit

_Status: audit + one pilot implementation_

## Trigger

Checkpoint 106 found that the current Old Name mechanism was heavily noun/Kind oriented.

That raised a structural vocabulary question:

> Can a pre-magic language lexicalize a common compositional verb/relation without promoting that meaning to a semantic root?

Examples include ordinary words such as give, kill, write, buy, sell, trade, teach, pray, dance, heal, and similar civilization vocabulary.

This checkpoint audits that question before broad Old Name expansion.

## Existing architecture before this checkpoint

Old Names already support:

- exact historical Signs;
- frozen name-unit mana cost;
- frozen world-concept meanings;
- Unit meanings;
- specification support for a frozen semantic expression.

However, the parser's expression Old Name path was **closed**: the frozen expression could return one semantic value, but the Old Name could not declare typed argument slots supplied at use time.

Therefore a historical word for a compositional transitive verb had no regular place to live.

The alternatives were:

1. keep every such verb as a multi-rune composition forever;
2. promote frequent verbs into semantic roots;
3. allow a frozen Old Name expression to declare typed parameters.

## Audit principle

Parameterized historical lexicalization is justified only when all of the following are true:

1. the meaning is already exactly expressible in current Cuspell semantics;
2. the frozen expansion has objective truth/execution conditions;
3. the arguments have explicit semantic types and fixed order;
4. the word is plausibly pre-magic historical vocabulary;
5. the Old Name does not add an otherwise missing semantic distinction;
6. modern speakers cannot create new privileged templates.

A parameterized Old Name therefore **compresses an existing composition**. It does not manufacture a new semantic primitive.

## Representative civilization-verb audit

| Candidate | Current semantic status | Parameterized Old Name finding |
| --- | --- | --- |
| give | Exact existing composition: concurrent `End Have(giver,theme)` + `Begin Have(recipient,theme)` | **Strong pilot.** Common, pre-magic, compositional, and already used in current design as the replacement for the removed Give root. |
| kill | Exact agentive composition: `Cause agent (End Life target)` | **Strong candidate.** No new kill primitive is needed. |
| die | Exact `End Life subject` | No template is structurally required because productive Begin/End state-boundary composition already expresses it compactly. An historical synonym could still exist. |
| create | `Begin Exist X`, optionally agentive through Cause | Usually already productive composition; a historical word may exist but does not justify a new primitive. |
| destroy | `End Exist X`, optionally agentive through Cause | Same result as create: composition already carries the distinction. |
| acquire / lose | `Begin Have` / `End Have` | Productive state-boundary composition already covers the core meaning. |
| marry / divorce | `Begin SpouseOf` / `End SpouseOf` where the intended meaning is change of spousal status | Usually no template needed for the semantic core. Ceremony/process detail is world/culture-specific. |
| write | Current `Exist` semantics explicitly treat creating/writing a Sign as agentive Cause of `Begin Exist(sign)` | **Candidate** when the historical word means creation of a Sign token. Material inscription details may require world data. |
| pay | Resource Transfer of currency/payment from payer to recipient, optionally with amount | **Candidate after currency/payment representation is fixed.** |
| exchange / trade | Normally two or more reciprocal Transfers, often concurrent | **Candidate for a culturally fixed transaction profile**, but not one universal core definition. |
| buy / sell | Payment + transfer/possession/ownership + legal/social context vary by culture | **Do not freeze a universal template yet.** A world/history package can define the exact transaction profile first. |
| borrow / lend | Temporary possession transfer plus expected/obligated return | **Potential cultural template**, but requires the obligation/return profile to be fixed. |
| inherit | Ownership/possession transfer constrained by death, kinship, law, will/contract, etc. | **World/legal template candidate**, not universal semantic core. |
| steal | Acquisition/transfer plus lack of relevant permission/ownership/legal conditions | **World/legal template candidate** only after the legal profile is explicit. |
| read | `Sense Vision sign` is not enough: reading may involve recognition/Meaning/Understand, and comprehension is not guaranteed | **Not currently an exact template.** This remains lexical/process pressure if later corpus requires a precise reading distinction. |
| teach | Could cause Know, Understand, or Can; successful learning is not guaranteed by teaching | **Not one exact composition.** Do not hide this ambiguity in an Old Name. |
| build | May create, join Parts, change Form, establish Whole, Purpose, etc. | **Not one exact composition.** Artifact/world construction profiles are needed. |
| cook | A family of food transformations; Heat is common but not universal | **Not one exact composition.** A genuine process distinction or world recipe/profile may be needed. |
| pray | May involve Worship, Say, Want, gratitude, request, silent practice, etc. | **Not one exact composition.** |
| dance | Manner of bodily movement not reducible to generic Move without losing the manner distinction | **Not one exact composition.** If needed, this is genuine lexical semantic pressure, not an Old Name-template problem. |
| heal | Checkpoint 107 already showed that healing can mean reduce Damage, end Ill, improve Health, reduce Pain, restore structure, or combinations | **Explicitly not one generic template.** |
| repair | May restore Whole, Joined relations, Form, function, or Parts depending on artifact | **Not one universal template.** |
| learn | Can be `Begin Know`, `Begin Understand`, or `Begin Can` depending on learned content | **Not one generic template.** |

## Main audit result

The answer is **yes, but narrowly**.

Cuspell should support **parameterized expression Old Names** for meanings that are already exact compositions.

This avoids two bad outcomes:

- forcing common historical verbs to remain permanently verbose merely because they take arguments;
- restoring convenience roots whose only reason for existence is lexical frequency.

At the same time, the mechanism must not be used to fake semantic completeness. If current roots cannot preserve a verb's meaning, an Old Name template cannot solve that gap.

For example:

- Give can be a template because its current possession-change meaning is already exact.
- Dance cannot become exact merely by hiding `Move` inside a frozen name.
- Heal cannot become exact by hiding an arbitrary choice of one health transition.
- Buy cannot receive a supposedly universal template until its transaction semantics are actually fixed.

## Accepted mechanism

A frozen expression Old Name may optionally declare a list of typed parameters.

Machine shape:

```json
{
  "meaning": {
    "kind": "expression",
    "type": "EventSpec",
    "parameters": [
      {"name": "giver", "type": "Entity"},
      {"name": "theme", "type": "Entity"},
      {"name": "recipient", "type": "Entity"}
    ],
    "source": "Concurrent EndHave $giver $theme BeginHave $recipient $theme"
  }
}
```

The quoted Sign then behaves as a typed lexical head:

`«TransferHave» Self This You!`

The arguments are supplied in the registered parameter order.

### Required-only parameters for v1

Checkpoint 110 deliberately allows **required parameters only**.

There are no:

- hidden defaults;
- inferred omitted participants;
- optional template roles;
- named English role labels.

If later historical vocabulary genuinely requires optional template parameters, that must be audited separately. The ordinary Cuspell omission-marker mechanism is not automatically inherited by historical templates.

This keeps the first version mechanically simple and prevents templates from becoming a second irregular frame language.

## Lexical scope and binder safety

A frozen Old Name expression is **lexically scoped**.

Its source may refer only to:

- its declared parameters;
- frozen semantic material written in the registered source;
- normal explicit contextual references that are themselves part of the frozen meaning.

It may **not** capture a caller binder merely because the binder has the same variable name.

Example forbidden behavior:

- caller binds `x:Entity`;
- hidden template source contains `$x`;
- Old Name silently captures caller `$x`.

Checkpoint 110 changes closed expression Old Names to the same lexical-scope rule. No current registered Old Name used expression meaning before this checkpoint, so this closes a latent capture hole without changing existing vocabulary.

Actual arguments are parsed in the caller's scope and then structurally substituted into the frozen template AST.

The parser does not perform string interpolation.

## Type safety

Every template parameter declares one concrete semantic type.

At use time:

- the argument must parse as that type;
- arguments are consumed left to right;
- all declared parameters are required;
- the frozen result must match the expected output type.

A future Old Name Sign may have several registered historical meanings only under the normal Old Name ambiguity/type-resolution rules, and all identical Signs must continue to have the same historical mana cost.

## Mana rule

Parameterized Old Names keep the existing Old Name mana rule.

The quoted historical Sign pays its frozen `name_units` cost.

Each **written argument** pays its normal mana cost.

The internal frozen semantic expansion does **not** add its root-by-root cost.

That is legitimate historical lexical compression, not a modern alias exploit.

New Names never receive this behavior.

## Pilot Old Name — give

Checkpoint 110 adds one pilot parameterized Old Name:

`«TransferHave»` = give

Historical units:

- Transfer;
- Have.

Frozen mana cost:

**2**

Parameters:

1. giver: Entity
2. theme: Entity
3. recipient: Entity

Frozen meaning:

`Concurrent EndHave $giver $theme BeginHave $recipient $theme`

Example:

`«TransferHave» Self This You!`

means the same current Cuspell event as:

`Concurrent EndHave Self This BeginHave You This!`

The pilot deliberately uses **Have**, not `Own`.

Therefore this Old Name means transfer of possession/holding under the current canonical Give reduction. It does not silently assert:

- legal ownership transfer;
- permission;
- payment;
- gift motive;
- permanent transfer.

Those meanings remain separate.

## Why Give is a strong pilot

Give is unusually suitable because the repository had already made the semantic decision before this audit:

the removed Give root is represented canonically by concurrent loss/acquisition of `Have`.

Checkpoint 110 therefore does not invent a new definition merely to test the feature.

It lexicalizes an already-established exact composition.

## What this mechanism does not do

Parameterized Old Names do **not**:

- add base semantic roots;
- count as semantic primitive candidates;
- let New Names become macros;
- let players invent cheap spell aliases;
- make an imprecise composition precise;
- bypass typing;
- bypass semantic validation;
- bypass magical execution closure;
- infer missing participants;
- capture caller variables;
- create a separate English-style role-label grammar.

They are one extension of the existing historical Old Name mechanism.

## Learning-complexity effect

The seven universal writing rules remain unchanged.

The player-facing structural-construction count also remains unchanged because this is an extension of the existing **quotation / exact Sign / Old Name** construction rather than a new punctuation or word-order system.

The new rule is:

> A registered historical expression Old Name may behave as a typed head whose required arguments follow in declared order.

That is the same head-before-arguments pattern already used by ordinary roots.

## Inventory effect

Base language inventory is unchanged:

- **210 registered base entries**;
- **129 semantic primitive candidates**;
- **55 formal constructors**;
- **263 semantic frames**;
- **48 multi-frame base entries**.

Old Name vocabulary changes:

- **102 -> 103 Old Names**;
- 96 concept/Kind Old Names;
- 6 Unit Old Names;
- **1 parameterized expression Old Name**.

The parameterized Give word does not count as a base rune.

## Civilization-audit consequence

Checkpoint 110 closes the final structural question from checkpoint 106.

Cuspell now has a regular place for all five broad vocabulary outcomes:

1. irreducible productive meaning -> semantic root;
2. ordinary stable world Kind/concept -> world concept + Old Name where historically lexicalized;
3. exact historical closed expression -> expression Old Name;
4. exact historical parameterized composition -> parameterized expression Old Name;
5. individual/new/local name -> New Name.

The next civilization-vocabulary work can therefore proceed domain by domain without deciding ad hoc whether every common verb must become a root.

## Next work

Begin balanced historical vocabulary expansion with the first high-priority domain:

**basic anatomy**.

For every proposed anatomy item, decide:

- whether existing roots can describe it naturally on demand;
- whether it is common enough to deserve a historical Old Name;
- what objective world concept/classifier it needs;
- whether any apparent noun gap exposes a real semantic distinction instead.

Do not add every English anatomy noun automatically.
