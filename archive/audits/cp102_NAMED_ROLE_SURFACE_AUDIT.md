# Checkpoint 102 — Named-Role Surface Audit

_Status: completed design audit; no syntax change in this checkpoint_

## Trigger

Current Cuspell allows zero-mana named-role tokens such as :path, :authority, :context, :instrument, and :basis.

Those English labels are not registered runes. They nevertheless change which semantic slot receives the following value.

That makes them meaning-bearing written material while the mana counter treats every :role token as free grammar. This conflicts with the active rule that every meaning-bearing written sign costs mana.

The issue is therefore not merely missing documentation or missing role vocabulary. It is a surface/semantic-layer leak.

## Scope

The executable lexicon contains:

- **205 registered entries**;
- **256 semantic frames**;
- **27 optional slots**;
- **20 distinct optional-slot role names**;
- **7 distinct role names currently marked named_only**;
- **10 named-only slot occurrences across 8 roots**.

The named-only roles are:

| Role label | Current uses |
| --- | --- |
| context | Obligated, Name |
| authority | two Permitted frames |
| profile | Transfer |
| instrument | two Cause frames |
| basis | GratefulTo |
| community | Reputation |
| offense | Forgive |

The general parser mechanism is broader than those seven names. Any frame slot can be selected by a :slot-name value form, and current player/spec examples also use :path and :source.

Across all optional slots the 20 distinct role names are:

predicate, alternative, period, recipient, goal, source, path, interval, context, authority, amount, profile, region, instrument, frame, threat, observer, basis, community, and offense.

Only three happen to match existing rune surfaces: Path, Interval, and Region. Those existing runes do **not** mean “fill this grammatical role”:

- Path is a Kind;
- Region is a Kind;
- Interval constructs a TimeInterval.

So even those three cannot simply be reused as role markers without introducing a new grammatical/semantic interpretation.

## Why named roles were useful

The mechanism currently solves two real parsing problems.

### 1. Skipping an earlier optional slot

Only three optional slot positions have later slots after them:

- Move.goal before optional source and path;
- Move.source before optional path;
- Transfer.amount before optional profile.

Examples such as “specify a path but no goal/source” need some way to say that the earlier positions are intentionally absent.

### 2. Preventing a broad optional tail from stealing an outer argument

Several frames end in a broad optional value, especially SemanticValue or Entity:

- Obligated(..., context?)
- Permitted(..., authority?)
- Name(..., context?)
- Cause(..., instrument?)
- GratefulTo(..., basis?)
- Reputation(..., community?)
- Forgive(..., offense?)

When such an expression is embedded inside another flat expression, the parser may be unable to know whether the next compatible token belongs to the inner optional tail or to the outer head. Checkpoint 101 exposed this directly with Name.

A replacement must therefore support both **gap skipping** and **explicit omission/closure of an optional tail**.

## Option 1 — semantic role runes

Proposal shape: a colon followed by a real rune, for example a Path rune, rather than a free English role label.

### Advantages

- role identity is explicit;
- meaning-bearing role material would no longer be free;
- can be readable when the role itself is an established semantic concept;
- could develop into a true semantic case/role system if Cuspell later wants one.

### Problems found by the audit

1. The current role vocabulary does not exist. Of 20 optional role labels, only 3 spellings collide with existing roots, and none of those roots currently has role-selector semantics.
2. Restricting the problem to the seven named-only labels does not help: **zero of those seven has an exact registered role rune**.
3. A uniform system would require either many new semantic role/case roots or a new grammatical reinterpretation that changes what ordinary runes mean after a colon.
4. The same English role label is not always one simple semantic relation. For example, source in motion and source in resource transfer are related but differently typed.
5. It duplicates information already fixed by a frame’s ordered slots.
6. It would charge extra mana for explicitly spelling a role even when the same semantic structure can be expressed positionally. That can be legitimate redundancy cost, but it does not by itself justify making the role vocabulary primitive.

### Audit verdict

**Not recommended as the minimal repair.**

This remains a viable future design direction only if Cuspell deliberately adopts semantic case/role runes as a first-class language feature. That would be a larger language-design project, not a cleanup of the current parser leak.

## Option 2 — one meaning-free omission marker

Proposal shape: _

The marker means only:

> the current optional positional slot is deliberately left unspecified; advance to the next slot.

It does not name the slot. The frame and position already determine which slot is being omitted.

Examples of the intended shape:

Move This _ _ ThisPath!

= omit goal, omit source, supply path.

Transfer resource source destination _ profile!

= omit amount, supply profile.

For an embedded expression with a broad optional tail:

Name «Road» This _

= omit the optional naming context and finish that frame before the outer expression continues.

### Advantages

- one grammar symbol instead of a role vocabulary;
- zero mana is justified because the marker carries no role identity or world/semantic concept;
- works with every optional slot, including future frames;
- preserves positional/type-driven Cuspell;
- solves both actual reasons named roles exist: internal gaps and optional-tail closure;
- adds no roots and no semantic frames;
- keeps internal slot names as implementation metadata only;
- makes two commands with the same supplied semantic arguments normalize the same way regardless of whether an omission marker was needed for parsing.

### Costs / open points

- _ is visually more formal than ordinary prose;
- repeated gaps can look mechanical, for example Move This _ _ path;
- it should be legal **only** where the current frame position is optional;
- it must be rejected for required slots and outside a frame;
- if an optional value is actually supplied and an embedding is still ambiguous, fallback grouping may still be needed;
- the exact glyph/transliteration can be changed later; the important design is a single meaning-free positional omission marker.

The audit found only **three optional positions** where skipping is needed to reach a later slot, so repeated placeholders should be uncommon.

### Audit verdict

**Best general replacement.**

It solves the grammar problem without inventing semantic vocabulary and matches the existing principle that zero-cost syntax may express structure but not semantic role identity.

## Option 3 — redesign every affected frame

Possible examples include:

- remove Cause’s optional instrument and express instrumentality through existing Use machinery where exact;
- split contextual and explicit forms of social relations;
- restructure Permitted;
- introduce separate relations for contextual dimensions such as naming community/authority.

### Advantages

- some individual frames may become semantically cleaner;
- can eliminate optional arguments that are not truly part of a root’s core meaning;
- may reduce ambiguity independently of surface syntax.

### Problems found by the audit

1. It cannot eliminate the general need for optional-slot grammar. Move still has optional goal/source/path, and Transfer still has an optional amount before another optional value.
2. Several optional dimensions are genuine semantic arguments rather than accidental parser baggage: naming context, gratitude basis, reputation community, offense, etc.
3. Reworking all affected roots would turn one grammar defect into multiple semantic redesigns.
4. Some cases deserve local review, but they should not be used to avoid having a general omission rule.

### Audit verdict

**Useful as targeted cleanup, not as the general solution.**

In particular, Permitted and Cause deserve follow-up review after the generic role-marker problem is fixed.

## Recommended direction

Adopt **Option 2** as the general grammar mechanism:

1. remove canonical :role value syntax;
2. keep frame slot labels internal only;
3. add one zero-mana positional omission marker;
4. initially use _ in transliteration unless a better neutral symbol is chosen;
5. make the marker legal only for an optional current slot;
6. allow repeated markers when multiple optional positions are skipped;
7. use ordinary positional values when the optional argument is present;
8. retain parentheses/pipe as fallback grouping for genuinely ambiguous embeddings;
9. separately audit whether any affected frames should be semantically simplified after migration.

This is a recommendation from the audit, **not yet an implemented syntax change**.

## Migration surface

Current regression/spec material actively uses at least:

- :context
- :authority
- :profile
- :instrument
- :basis
- :offense
- :path
- :source

The heaviest observed current dependencies are :context and :authority.

A migration pass must update parser behavior, surface v0.7, player rules, current specs, current tests, and mana accounting. Historical archive material should remain unchanged.

## Relation to Distance

Distance does not use named-role syntax.

The role-marker defect should be resolved **before** the remaining Distance lexical audit so the language’s basic argument/omission grammar is stable first.
