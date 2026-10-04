# Checkpoint 118 — Authority Exact-Reduction Audit

_Status: post-civilization reduction/redundancy audit, target 1_

## Purpose

Checkpoint 115 added:

`Authority(holder,scope) -> StateProposition`

for persistent recognized social/institutional standing to issue or validate binding rules, permissions, obligations, or decisions for a supplied scope.

That addition was deliberately provisional. The post-checkpoint-117 audit therefore starts with the user's specific question:

> Can `Authority` be removed in favor of `Permitted` / `Obligated` / Rule/Law plus world-model facts without losing objective meaning?

This checkpoint re-tests the relation from current machine truth rather than preserving it merely because checkpoint 115 added it.

## Current candidate

`Authority(holder,scope)`

Current frame:

- holder: `Entity`;
- scope: `SemanticValue`;
- output: `StateProposition`;
- persistent state predicate.

Its intended truth condition is not "the holder is allowed to do something." It is:

> the holder has recognized standing/competence for a scope such that the world's social/institutional rules treat relevant acts or decisions by that holder as normatively valid or binding.

The setting determines what produces that standing: appointment, election, delegation, kinship, contract, office, ritual recognition, sovereignty, or some other objective rule.

## Candidate reduction 1 — Permitted

The most obvious replacement is some form of:

`Permitted(holder,event,source?)`

This fails exactness.

`Permitted` concerns a particular `EventSpec`. It says that an action is allowed or consented to.

`Authority` concerns recognized standing over a reusable scope.

### Permission without authority

A court clerk may be permitted to announce a judgment, file a document, or speak during a proceeding.

That permission does not imply that the clerk's own ruling becomes legally binding.

Likewise a visitor may be permitted to speak in a council chamber without having authority to enact a law.

So:

`Permitted(A,E,...)`

can be true while:

`Authority(A,S)`

is false.

### Authority does not mean permission to every act in the scope

A judge can hold authority in a court while not being permitted to destroy evidence, accept a bribe, or perform unrelated acts there.

Authority therefore cannot mean "all events in this scope are permitted to the holder."

### Type mismatch

The current frames expose the distinction directly:

- `Authority(...)` -> `StateProposition`;
- `Permitted(...)` -> `Proposition`.

Authority can therefore participate in persistent-state transitions such as:

`Begin Authority Self This!`

and:

`End Authority Self This!`

The permission relation does not currently denote that persistent standing.

This type difference is not by itself the philosophical proof, but it correctly reflects the deeper truth-condition difference.

**Result: `Permitted` is not an exact reduction.**

## Candidate reduction 2 — Obligated + Permitted

A richer proposal is to represent authority as a structured bundle of permissions and obligations.

That also fails.

`Obligated(agent,event,context?)` states a duty concerning an EventSpec. It can record duties associated with an office, institution, contract, or other context.

But duties of office are not the same thing as competence of office.

An official can:

- be obligated to hear a case;
- be permitted to sign a decision;
- still lack authority over a different jurisdiction.

Conversely an official may retain authority while having no present duty to exercise it.

A bundle of current permissions/obligations therefore does not identify the separate question:

> whose qualifying decision will the world recognize as binding?

**Result: the deontic bundle does not reduce Authority.**

## Candidate reduction 3 — Rule / Law + world facts

Cuspell already has Rule/Law vocabulary that can identify normative rules.

Could a world simply store a Rule/Law saying who has authority, with no productive Authority relation?

Only if the world stores a new fact whose content is already equivalent to Authority.

Rule/Law classification does not by itself supply the relational predicate:

`holder has recognized standing over scope`.

If the world model contains an internal relation such as:

`recognized_decision_maker(holder,scope)`

then removing the Cuspell root has not reduced the semantics. It has merely hidden the same semantic distinction behind the world interface, making it unavailable for ordinary Cuspell assertions, questions, selection, or state changes.

World ontology should decide **when** Authority is true, not erase the language's ability to state that it is true.

**Result: world data can ground Authority but cannot replace its language-level meaning without losing expressibility.**

## Candidate reduction 4 — Can + Cause

Another tempting reconstruction is:

- holder `Can` perform an act that
- `Cause`s a permission, obligation, rule, or decision state.

This also fails.

### Capability is not legitimacy

`Can(agent,event)` is persistent capability.

A person may be physically, socially, technologically, or magically capable of producing an outcome without recognized authority.

A coercive ruler, forger, hacker, kidnapper, or occupying power may be able to make others comply or alter records while lacking the recognized standing represented by Authority.

The converse also holds: an office-holder can retain authority while temporarily unconscious, imprisoned, unable to communicate, or otherwise incapable of exercising it.

### Causation is about effects, not standing

`Cause` can describe a particular event or causative EventSpec.

A particular unauthorized act might in fact cause a new obligation-like social state through threat, promise, deception, or force.

That does not establish general institutional competence.

Authority is a standing fact that helps determine the normative significance of later acts; it is not identical to one act's causal history.

**Result: `Can` + `Cause` is not exact.**

## Candidate reduction 5 — Control / Own / Have

These fail for the same reason identified in checkpoint 115 and survive re-test.

- factual Control can exist without legitimacy;
- recognized Authority can exist despite weak factual Control;
- ownership of an object or territory need not confer public authority;
- possession does not confer jurisdiction.

These relations can correlate with authority in particular worlds but do not define it.

## Decisive countermodel

The cleanest exactness test uses two allowed world states.

Assume worlds W1 and W2 have identical current facts about:

- every `Permitted` proposition;
- every `Obligated` state;
- every Rule/Law item;
- every `Can` capability;
- every `Control`, `Own`, and `Have` fact;
- every already-completed causal event.

There are two otherwise identical office-holders, A and B.

In W1, the constitution/ritual/appointment rule recognizes A as the decision-maker for scope S.

In W2, it recognizes B instead.

No current permission, obligation, control, capability, or completed causal fact has to differ before either person exercises the office.

Yet the institutional effect of a qualifying later act differs:

- in W1, A's decision is recognized as binding;
- in W2, B's is.

Therefore the existing candidate relations do not determine the truth of:

`Authority(A,S)`.

An exact reduction would need to introduce some other fact encoding recognized normative competence. That fact would be Authority under another name.

## Parser and type-system consequence

The current parser has a clean one-frame relation:

`Authority(Entity,SemanticValue) -> StateProposition`.

This is useful because scopes are not restricted to one ontology family. A scope may be a case, court, polity, group, territory, ritual, office, contract, subject matter, or another objectively defined value.

Replacing that with per-event permissions would:

- narrow a reusable scope relation into EventSpec facts;
- require potentially unbounded enumeration;
- lose the state-transition meaning used by Begin/End;
- make jurisdiction harder to state and query;
- still fail the decisive countermodel.

Parser usability therefore gets worse while semantics become weaker.

## Old Name dependency check

Current Old Names directly depending on Authority include:

- Judge;
- Polity/state;
- Government;
- Priest.

Citizen depends on Polity and is therefore indirectly affected.

These dependencies are not a reason to keep the root by themselves; design-stage Old Names may be rewritten.

However there is no exact existing replacement for the historical idea those names currently foreground:

- Judge without adjudicative standing becomes merely a person associated with a Court;
- Polity without recognized public authority becomes merely a law-associated human Group;
- Government without authority becomes merely a Group associated with a Polity or factual Control;
- Priest without recognized ritual/religious standing becomes merely a worshipper.

The Old Names therefore supply additional lexical pressure consistent with the semantic result, not circular justification for it.

## Mana consequence

No inventory or cost change is made.

Authority remains one meaning-bearing rune/sign occurrence with rune cost 1.

A longer construction would not qualify as legitimate mana-saving reduction because none of the tested constructions is semantically equivalent.

## Result

**KEEP AS IRREDUCIBLE SEMANTIC BASIS: `Authority`.**

Checkpoint 118 concludes:

1. Authority is not permission.
2. Authority is not a bundle of current permissions and obligations.
3. Authority is not capability.
4. Authority is not factual control, possession, ownership, or causation.
5. Rule/Law world data can determine who has authority, but replacing the language relation with an opaque world-only predicate would merely hide the same necessary semantic distinction.
6. The exact countermodel with identical deontic/control/capability facts but different recognized decision-makers proves the reduction invalid.

The registered inventory therefore remains:

- **212 registered base entries**;
- **131 semantic primitive candidates**;
- **55 formal constructors**;
- **265 semantic frames**;
- **48 multi-frame entries**.

No Old Name or world concept needs rewriting in this checkpoint.

## Next reduction target

Continue the post-civilization reduction audit with the checkpoint-107 body-state additions:

- `Health`;
- `Pain`;
- `Ill`.

Test each independently against the stabilized Attribute/Property/state machinery rather than assuming checkpoint 107's restoration remains final.
