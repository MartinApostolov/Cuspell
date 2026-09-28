# Yona Chapters 1–50 Vocabulary

_Status: source-backed Yona world/New Name inventory extension through Chapter 50_

This document extends the earlier Chapters 1–14 + 47 vocabulary audit. It records setting-specific vocabulary only; Cuspell core roots and historical Old Names remain in their own registries.

## Package boundary

Yona-specific vocabulary lives in:

- `world/yona/concepts.json`
- `world/yona/new_names.json`

and is loaded explicitly with:

`Language.load(root, world_package="yona")`

The package now contains **177 Yona world concepts and 180 New Name entries**.

These names do not become magical macros. Their component words do not inherit Old-Name compression merely because the English-looking label contains ordinary words.

## Major additions from Chapters 15–50

### System/world ontology

- `«Title»`
- `«Named Monster»`
- `«Named Type»`
- `«Territory»`
- `«Dungeon»`
- `«Dungeon Core»`
- `«Soul Weapon»`
- `«Party»`
- `«Sin Trait»`
- `«Mental Magic»`

Named-monster type values:

- `«Leader»`
- `«Hermit»`
- `«Infiltrator»`
- `«Disaster»`

Additional ordered technical values:

- `«Mithril»` rank
- `«High»` proficiency

### Exact Chapter 21 Skill upgrades

The source displays five choices for External Mana Manipulation - Anatomical Constructs.

Registered as explicit upgrade names where they remain options:

- `«External Mana Manipulation - Greater Anatomical Constructs»`
- `«External Mana Manipulation - Advanced Anatomical Constructs»`
- `«External Mana Manipulation - Detailed Anatomical Constructs»`
- `«External Mana Manipulation - Anatomical Weapons»`

The selected fifth name, `«External Mana Manipulation - Anatomical Constructs of the Glutton»`, is registered as the resulting Skill. Its source-visible option spelling is identical to the resulting Skill name, so it does not need a second ambiguous Name entry.

`«Emma»` is separately registered as Yona's nickname for that Skill. It is an ordinary later nickname/reference, not magical compression.

### Named evolution choices

Chapter 28 explicitly exposes:

- `«Yona, the Devourer»`
- `«Yona, the Glutton»`
- `«Yona, the Gastronome»`

Associated exact Skills/Traits include:

- `«Devour»`
- `«Area Scan»`
- `«Aura of the Devourer»`
- `«Homebody»`
- `«Perfect Disguise»`
- `«Custom Namecard»`

### Gluttony sub-Traits

Source-visible names include:

- `«Poison Immunity»`
- `«Calorie Burner»`
- `«Stuffed»`
- `«Hungry»`
- `«Strong Teeth»`
- `«Iron Stomach»`
- `«Discerning Palate»`
- `«Diverse Tastes»`

These are Yona System Trait names even where a comparable ordinary-language predicate exists in core.

### Classes and Professions

Exact source-backed Class names now include:

- `«Trident Warrior»`
- `«Beginner Mana Vivitect»`
- `«Beginner Spatial Mage»`
- `«Capable Mana Vivitect»`
- `«Beginner Fire Mana Vivitect»`
- `«Beginner Space Mana Vivitect»`
- `«Wannabe Vivitect»`
- `«Mana Asura»`
- `«Wannabe Mana Cloner»`
- `«Beginner Mana Avatar Pilot»`
- `«Advanced Artillery Mage»`
- `«Advanced Barrier Mage»`

Professions include:

- `«Taste Tester»`
- `«Campfire Cook»`
- `«Cook»`
- `«Manager»`
- `«Carpenter»`

### Additional Skills and progression labels

Source-backed Skills/options include:

- `«Anatomical Blueprint»`
- `«Phantom Limb Control»`
- `«Anchor Point»`
- `«Anatomical Analysis»`
- `«Internal Mana Manipulation - Fleshbender»`
- `«Heavy Blow»`
- `«Split Focus»`
- `«Internal Mana Manipulation»`
- `«Mana Exoskeleton»`
- `«Avatar Control»`
- `«External Mana Manipulation - Brachial Constructs of the Glutton»`
- `«External Mana Manipulation - Body Constructs of the Glutton»`
- `«Appraise»`
- `«Timer»`
- `«Culinary Analysis»`
- `«Critical Culinary Analysis»`
- `«Detailed Critical Culinary Analysis»`
- `«Greater Detailed Critical Culinary Analysis»`
- `«Mana Shield»`
- `«Fire Burst»`
- `«Fire Arrow»`
- `«Greater Ember»`
- `«Spiral Mana Burst»`
- `«Greater Mana Shield»`
- `«Autonomous Mana Shield»`
- `«Mana Shield Construct»`
- `«Shell Construct»`

### Titles, Soul Weapons, people, places, and species

New source-visible names include Titles such as:

- `«Second Lifer»`
- `«System Breaker»`
- `«Nameworthy»`
- `«Named»`
- `«Taker of Names I»`
- `«Dungeon Pioneer I»`
- `«Dungeon Destroyer I»`
- `«Ruler of the Shallows»`
- `«Bubble Witch»`

Soul Weapon:

- `«Gluttonous Greatsword»`

Specific world names include Skarn, Lauren, Flarn, Chad, Indarius Pike, Riverfork, Ryantown, Triore, Rabbit Dungeon, Rabbit Dungeon Core, and other explicitly displayed identities.

Species/monster labels include Medusoid, Karkinoid, Crystal Pseudo-Drake, and Yona's longer evolved System species label.

## What was not promoted to core

The Chapters 15–50 pass did **not** justify new general grammar.

Healing/regrowth, expulsion, control/subjugation, combat intent, world resistance, and similar meanings remain compositionally expressible with existing core semantics plus objective world rules.

Telepathy remains intentionally unresolved at the history/lexicon boundary. Chapter 50 proves that telepathic communication occurs in Yona, and `«Mental Magic»` is now registered as a Yona technical term, but the source does not decide whether generic telepathy belongs to Cuspell's pre-magic Old vocabulary.

## Source rule

Only exact names visible in the source are registered. When a chapter says that other options exist without naming them, those options remain absent from the registry.
