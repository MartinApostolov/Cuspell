# Checkpoint 123 — Parameterized Expression Old Name Structural Audit

_Status: post-civilization structural/redundancy audit, target 2_

## Purpose

Checkpoint 110 generalized frozen expression Old Names so a historical word could take typed arguments and expand to an already-exact Cuspell composition.

The only current parameterized expression Old Name is:

`«TransferHave»` = give

with frozen meaning:

`Concurrent EndHave $giver $theme BeginHave $recipient $theme`.

Checkpoint 123 re-tests whether this mechanism is actually necessary, whether Give remains an exact pilot, whether the feature creates a macro/mana loophole, and whether its implementation/validation is tight enough to keep.

The audit tests these alternatives:

1. remove parameterized Old Names and keep every such meaning fully written;
2. restore convenience roots such as Give;
3. encode historical verbs as ordinary lexical compounds;
4. allow New Names/user aliases to behave as templates;
5. retain the dedicated historical-template mechanism, but only for exact frozen compositions.

## Current inventory

The current core Old Name registry contains:

- 197 concept/Kind Old Names;
- 6 Unit Old Names;
- 1 parameterized expression Old Name.

There is no base `Give` root.

`«TransferHave»` is therefore the only live example needed to decide whether the mechanism itself survives.

## Is the mechanism redundant?

No.

### Full ordinary composition

The exact Give meaning can always be written directly:

`Concurrent EndHave giver theme BeginHave recipient theme`.

That proves Give is not a semantic primitive.

It does **not** answer the historical-vocabulary question.

Natural/historical languages can lexicalize meanings that remain compositionally analyzable. If Cuspell forbids parameterized historical words, every pre-magic verb whose meaning takes participants must either:

- remain permanently verbose;
- become a semantic root;
- or gain another special lexical mechanism.

The first loses ordinary historical vocabulary; the second pollutes the semantic basis.

### Restoring Give as a root

Checkpoint 94 already proved that the former Give root added no independent meaning.

The exact former semantics were:

`Concurrent EndHave giver theme BeginHave recipient theme`.

Restoring Give merely because the historical language plausibly had a short word would reverse a valid semantic reduction.

A base root and a historical lexicalized composition are intentionally different layers.

**Result: do not restore Give.**

### Ordinary lexical compounds

The productive compound system combines descriptors/Kinds/Properties through registered compositional rules.

It does not provide lambda/function abstraction over an arbitrary open expression.

`TransferHave` as an unquoted productive compound cannot, by ordinary compound rules, mean:

- take three typed Entity arguments;
- use the theme argument twice;
- place the giver/theme inside EndHave;
- place recipient/theme inside BeginHave;
- coordinate both boundaries with Concurrent.

Adding a special compound rule that stores this open template would simply recreate parameterized expression Old Names under a different name while mixing historical vocabulary into productive morphology.

**Result: ordinary compounds are not a replacement.**

### New Names / arbitrary aliases

New Names are ordinary naming/reference facts.

Allowing:

`new-name = arbitrary frozen EventSpec template`

would let modern casters coin mana-saving spell macros.

That violates the language/magic boundary and the established historical-cutoff rule.

**Result: New Names must remain non-callable.**

## Give exactness re-check

Checkpoint 94's reduction still holds under current semantics.

Current relevant pieces remain:

- `Have(holder,theme) -> StateProposition`;
- `End Have(...) -> EventSpec`;
- `Begin Have(...) -> EventSpec`;
- `Concurrent(...EventSpec...) -> EventSpec`.

The former Give entry carried no additional:

- ownership transfer;
- permission;
- payment;
- gift motive;
- location;
- control;
- speech;
- beneficiary;
- manner.

Therefore:

`«TransferHave» giver theme recipient`

may still freeze exactly:

`Concurrent EndHave giver theme BeginHave recipient theme`.

The historical Sign's etymological units are Transfer + Have, but etymology is not the live semantic definition. That is already the general Old Name rule.

**Result: `«TransferHave»` remains a valid pilot.**

## Why the open-template feature is semantically legitimate

A parameterized expression Old Name does not create a new truth condition.

Its frozen source must already parse as the declared semantic type using only:

- declared parameters;
- frozen registered Cuspell material;
- explicit contextual references physically present in the frozen source.

At use time, caller arguments are parsed normally with their declared types and structurally substituted into the already-parsed template AST.

There is no textual interpolation.

This is equivalent to lexicalizing an existing typed expression with participant slots.

## Lexical scope

The frozen source is lexically scoped.

It cannot see arbitrary caller variables.

For example, if a hidden template mentions:

`$hidden`

without declaring a `hidden` parameter, a caller binder named `hidden` must not satisfy it.

That protection already existed in the parser and remains correct.

Checkpoint 123 also preserves the complementary rule:

> explicit arguments are parsed in caller scope.

So a caller may deliberately pass:

`$x`

as a written argument when `x` is in scope.

This is not capture; it is explicit parameter passing.

## Required-only interface remains correct

Checkpoint 110 intentionally restricted parameterized Old Names to required positional parameters.

Checkpoint 123 finds no evidence to add:

- optional parameters;
- hidden defaults;
- inferred participants;
- named English role labels;
- variadic historical frames.

All of those would create a second frame/omission grammar inside the Old Name registry.

The ordinary root/frame system already has the machinery for optional roles when semantics actually need them.

Historical templates therefore remain:

- typed;
- positional;
- required-only.

Extra written arguments are not swallowed.

## Mana audit

The mana rule remains:

- quoted Old Name pays its frozen historical `name_units` cost once;
- every explicitly written argument pays its normal current cost;
- hidden expansion roots do not add cost.

For Give:

- `«TransferHave»` historical cost = 2;
- `Self` = 1;
- `This` = 1;
- `You` = 1.

Therefore:

`«TransferHave» Self This You!`

costs:

**5 mana**.

The fully written exact composition:

`Concurrent EndHave Self This BeginHave You This!`

costs:

**9 mana**.

This compression is intentional.

### Parameter reuse

The Give template uses `theme` twice internally, while the speaker writes the theme once.

That is not a zero-mana alias exploit.

A lexical item is allowed to encode participant co-reference just as an ordinary root frame can package internal semantic structure around one supplied participant.

The safety boundary is registration:

- only frozen pre-magic Old Names receive the compression;
- New Names/player aliases do not;
- the template source is fixed and validated;
- arguments still cost their written mana.

There is therefore no need to charge a parameter again merely because its semantic value appears multiple times inside the registered lexical meaning.

## Structural validation gap found

Checkpoint 110 validated the JSON/schema shape of parameters, but the whole-registry validator did not compile frozen expression source.

An invalid template could therefore remain in `old_names.json` until somebody actually invoked it.

Examples of latent bad data included:

- undeclared/free variables;
- invalid frozen syntax;
- type-invalid source;
- recursive template use;
- declared parameters never used by the meaning.

This is inconsistent with the repository's source-of-truth policy: frozen expression Old Names are executable language data, not documentation.

## Checkpoint 123 validation repair

Whole-registry validation now compiles every frozen expression Old Name under the same lexical template scope used at runtime.

Registry validation catches:

- invalid template syntax;
- undeclared/free variables;
- type-invalid expansion;
- recursive Old Name expansion;
- unused declared parameters.

Parameter objects are also restricted to the supported fields:

- `name`;
- `type`;
- `required`.

Because the current version is required-only:

- `required` may only be true;
- fields such as `default` are invalid rather than silently ignored.

This closes the most important remaining macro-like loophole: hidden registry metadata can no longer pretend to define semantics the parser does not actually enforce.

## Why unused parameters are invalid

A declared argument that does not occur in the frozen meaning is semantically dead.

Keeping it would:

- make callers pay mana for a value that changes nothing;
- make the lexical interface misrepresent the frozen semantics;
- create room for later accidental/default-style behavior.

Therefore every declared parameter must appear in the parsed frozen expression at least once.

Repeated use remains valid and intentional.

## Candidate expansion audit

Checkpoint 110 listed other historical verbs that might someday fit this mechanism.

Checkpoint 123 does **not** add any.

Examples:

- kill may be exactly compositional in a suitable agentive reading;
- die/create/destroy/acquire/lose are already compact productive transitions;
- write/pay/trade may depend on a more specific historical/world profile;
- buy/sell/borrow/lend/inherit/steal remain legal/cultural profiles;
- read/teach/build/cook/pray/dance/heal/repair/learn still do not have one universally exact current composition.

The existence of the mechanism is not permission to fill the Old Name registry with speculative verbs.

Each new parameterized Old Name still requires its own evidence that:

1. the historical lexicalization is warranted;
2. the current frozen composition is exact.

## Regression changes

Checkpoint 123 adds five regressions:

1. caller binders may be passed explicitly as typed arguments;
2. extra template arguments are rejected;
3. registry validation rejects an undeclared/free variable in frozen source;
4. registry validation rejects an unused declared parameter;
5. registry validation rejects unsupported hidden/default parameter metadata.

Existing Give tests are tightened to assert:

- no base Give root exists;
- `old.core.give` is the only parameterized expression Old Name;
- named Give and direct composition normalize identically;
- exact mana costs are 5 vs 9.

Suite size rises:

- **661 -> 666 tests**.

## Inventory effect

No base entry, semantic primitive candidate, constructor, frame, Old Name, New Name, or world concept is added or removed.

Inventory remains:

- **212 registered base entries**;
- **131 semantic primitive candidates**;
- **55 formal constructors**;
- **265 semantic frames**;
- **48 multi-frame entries**;
- **204 Old Names**;
- **197 core world concepts**.

The Old Name distribution remains:

- **197 concept/Kind Old Names**;
- **6 Unit Old Names**;
- **1 parameterized expression Old Name**.

## Result

**KEEP AND TIGHTEN: parameterized expression Old Names.**

Checkpoint 123 concludes:

1. the feature is not redundant with ordinary compounds, New Names, or the root system;
2. restoring Give would undo a valid semantic reduction;
3. `«TransferHave»` remains an exact pilot under current semantics;
4. parameterized Old Names remain required, typed, positional, and lexically scoped;
5. explicit caller-scope arguments are allowed, hidden caller capture is not;
6. optional/default/variadic/named-role template interfaces remain unjustified;
7. repeated parameter use inside a frozen meaning is legitimate lexical co-reference compression;
8. frozen expression source is now compiled during whole-registry validation;
9. undeclared variables, type-invalid source, recursion, unused parameters, and unsupported/default parameter metadata invalidate the registry;
10. the mechanism does not justify adding any further parameterized Old Name without independent lexical/semantic evidence.

## Structural audit closure

The dedicated post-civilization reduction/redundancy audit is now complete:

- checkpoints 118–121 re-test productive additions;
- checkpoint 122 audits typed world-Kind classification;
- checkpoint 123 audits parameterized expression Old Names.

No additional semantic root or structural mechanism is introduced by the closure pass.

## Next work

Return to the remaining current-maintenance priority:

**finish reconciling grammar/spec/examples with canonical surface v0.8.**

After current grammar/spec normalization is clean:

1. keep the player-facing projection mechanically aligned;
2. define/test the beginner Cuspell subset;
3. return to rune/glyph visual design only after the writing system is stable enough.
