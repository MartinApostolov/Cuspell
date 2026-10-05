# Checkpoint 130 — Post-Create Beginner Spellcraft Re-audit

_Status: completed targeted repair after fresh-identity Create_

## Trigger

Checkpoint 129 added `Create` as explicit fresh Entity allocation.

The level-0-to-2 beginner corpus had been written before that semantic existed. The user also noticed that Light and Faerie Fire had collapsed to the same Cuspell recipe.

This pass therefore re-checks the existing starter examples for two things:

1. places where pre-Create approximations can now be improved;
2. exact duplicate Cuspell recipes that may hide a real semantic distinction.

This is not a second full SRD spell audit.

## 1. Light versus Faerie Fire

Previous starter rows:

- Light -> `Change This Light «LightUnit» @!`
- Faerie Fire -> `Change This Light «LightUnit» @!`

That collapse was unnecessary.

The retained Light analogue is a single selected object's Light output:

`Change This Light «LightUnit» @!`

Faerie Fire is now the explicitly distributed group effect:

`Each They x:Entity Change $x Light «LightUnit» @!`

The D&D advantage mechanic and exact area-selection rule remain outside the language benchmark.

**Result: repaired accidental semantic collapse without adding a root.**

## 2. Magic Missile and the fresh-result use problem

Previous Magic Missile analogue:

`Move This There!`

Its own note admitted that it assumed a prepared projectile because fresh creation did not exist.

After checkpoint 129, fresh projectile allocation exists, but the first Create frame exposed a new composition problem:

`Create x:Entity profile`

scoped `$x` only through the post-creation Proposition profile.

That meant the newly created identity could not directly participate in a later EventSpec inside the same Create expression. A spell could create a projectile, but could not immediately move that exact fresh projectile without first making it recoverable through a Name/relation and selecting it again.

That is too weak for ordinary spell composition and would force a global-variable-like workaround.

### Repair

Create keeps one semantic frame but gains an optional final slot:

`Create(result:Binder<Entity>, profile:Proposition, continuation?:EventSpec) -> EventSpec`

The binder scopes through both the profile and the optional continuation.

Example:

`Create x:Entity Matter $x And At $x Here Move $x There!`

Semantics:

1. allocate exactly one fresh Entity;
2. realize the binder domain + profile;
3. if present, evaluate/execute the continuation against the resulting world state with the fresh binder still in scope.

The binder still does not escape the Create expression.

Ordinary non-rollback execution applies: if creation succeeds and the continuation later fails, the already-created Entity is not silently erased.

This does not add a new root or frame. It extends the existing Create frame with one optional typed slot.

### Updated Magic Missile analogue

`Repeat @@@ Create x:«SharpMoveAttackThing» At $x Here Move $x There!`

This allocates three distinct fresh arrow-like projectile identities and immediately moves each toward the selected destination.

Force damage and automatic-hit mechanics remain outside the benchmark.

**Result: pre-Create prepared-projectile assumption removed.**

## 3. Fresh creation returns to the beginner projection

The starter grows from 47 to 50 registered signs. Fresh creation adds:

- `Matter`;
- `Create`.

The audit also removes contextual `They` from the executable teaching projection and adds:

- `Collect`;
- `Member`.

This gives beginner multi-target spells an objective collection source instead of a contextual plural reference. A fourth teaching tier now covers fresh creation.

The starter Old Names used by examples are now:

- `«HeatUnit»`;
- `«LightUnit»`;
- cat `«LowExtent«MoveLifeThing»»`;
- arrow `«SharpMoveAttackThing»`.

The Cat and Arrow words are ordinary historical vocabulary, not spell-name macros.

A new Find Familiar-like pressure example is added:

`Create x:«LowExtent«MoveLifeThing»» Life $x And At $x Here And Like $x Self!`

It creates one fresh living friendly cat-like creature. Telepathy, dismissal, spirit metaphysics, and other D&D familiar rules are deliberately not copied.

The beginner corpus now contains 48 level-0-to-2 reference effects.

## 4. Objective multi-target closure

The first Faerie Fire repair used:

`Each They x:Entity Change $x Light «LightUnit» @!`

CI correctly rejected it because `They` is a context-dependent plural reference and magical execution requires objective references.

The executable starter therefore does not teach `They` as a magic target. Faerie Fire now selects members of an explicitly designated Group:

`Each Collect x:Entity Member $x This y:Entity Change $y Light «LightUnit» @!`

This adds one net starter sign relative to the old projection: `They` leaves, while `Collect` and `Member` enter.

**Result: multi-target beginner magic is explicit and execution-objective.**

## 5. Exact duplicate recipe audit

After the repairs, every remaining exact duplicate starter recipe was reviewed.

### Intentionally shared objective slices

#### Heat increase

`Change This Heat Add BeforeValue Heat This «HeatUnit» @!`

Used by:

- Fire Bolt;
- Prestidigitation;
- Heat Metal.

These differ strongly in D&D delivery, scale, or targeting, but the selected Cuspell benchmark slice is exactly the same objective Heat increase.

#### Generic forced/remote movement

`Move This There!`

Used by:

- Mage Hand;
- Thunderwave;
- Gust of Wind.

The selected benchmark slice is movement of an explicitly designated Entity to an explicitly designated destination. Continuous wind physics, burst pressure, and spectral-hand presentation are not being claimed.

Magic Missile is no longer in this group because fresh projectile creation is now available.

#### Health restoration target

`Change You Health Health Self!`

Used by:

- Cure Wounds;
- Healing Word.

The objective Health result is deliberately the same. D&D range/action economy is outside the benchmark.

#### Form copy

`Change Self Form Form This!`

Used by:

- Disguise Self;
- Alter Self;
- Enlarge/Reduce.

This is still a deliberately coarse practical-effect slice. Disguise Self's true persistent illusion mechanism remains part of the separate shared-illusion pressure family; the starter example does not claim to preserve that metaphysical distinction.

#### Movement capability

`Begin CanYouMoveYouThere!`

Used by:

- Longstrider;
- Enhance Ability.

Enhance Ability is represented only by one selected capability-improvement slice.

#### Visual concealment

`Prevent SenseThisVisionYou ThisInterval!`

Used by:

- Invisibility;
- Pass without Trace.

Both remain partial one-observer/one-channel concealment slices. Broader stealth/trace behavior is not silently inferred.

### Regression rule

The test suite now records the complete expected set of exact duplicate recipes.

A new undeclared exact duplicate therefore fails tests instead of silently entering the starter corpus.

## 6. Additional drift found

The player guide still listed `Extent` in the 47-sign transformation tier even though checkpoint 127 had removed it from the machine manifest after the Enlarge/Reduce execution-closure repair.

That stale player entry is removed.

The corrected teaching counts are:

- direct manipulation: 20;
- persistent/protective: +15 = 35;
- transformation/programming: +13 = 48 (`They` removed; `Collect` + `Member` added);
- fresh creation: +2 = 50.

## 7. Inventory effect

None.

The semantic inventory remains:

- 214 registered base entries;
- 133 semantic primitive candidates;
- 55 formal constructors;
- 268 semantic frames;
- 49 multi-frame entries.

Create gains one optional slot, not another frame.

## Decision

**KEEP LIGHT AS SINGLE-TARGET ILLUMINATION; MAKE FAERIE FIRE EXPLICITLY DISTRIBUTED.**

**EXTEND CREATE WITH AN OPTIONAL IMMEDIATE CONTINUATION SO ITS FRESH RESULT CAN BE USED IN THE SAME COMMAND.**

**ADD MATTER + CREATE TO THE BEGINNER TEACHING PROJECTION, AND REPLACE CONTEXTUAL THEY WITH OBJECTIVE COLLECT + MEMBER FOR EXECUTABLE MULTI-TARGET SPELLS.**

**REGRESSION-GUARD ALL REMAINING EXACT DUPLICATE STARTER RECIPES AS INTENTIONAL.**

## Next work

Return to advanced spellcraft gap 2:

**bounded acquisition of previously unknown Information / divination.**
