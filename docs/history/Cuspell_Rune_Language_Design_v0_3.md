# Cuspell Rune Language / Objective Freeform Magic
## Design State v0.3

This document consolidates the design work so far for a D&D-style magic supplement in which casters do not select prewritten spells. Instead, they construct commands in a formal rune language. The goal is to preserve the creativity of freeform rune magic while eliminating arguments over interpretation.

---

# 1. Core Goal

The old system allowed players to combine runes freely, but each combination required the GM and caster to negotiate what it meant.

The new system should be:

- **Objective:** a valid expression has a defined meaning.
- **Free:** players can construct effects that were never explicitly listed as spells.
- **Compositional:** complex meanings come from simpler runes and grammar.
- **Learnable:** the language can be revealed gradually to players.
- **Economical:** spell cost naturally follows from how much magical language must be written.
- **Potentially usable as a real language:** the full rune language may contain concepts that are irrelevant to spellcasting.
- **Not just English with replacement letters:** the language should have its own semantic roots and composition rules.

The strongest current metaphor is:

> The magical language is a formal instruction language for reality.

It borrows ideas from programming languages—strict syntax, types, unambiguous semantics—but a spell does **not** have to be a conventional program or script.

A complex grammatical sentence with multiple actions is allowed if it has a valid, objective meaning.

---

# 2. Important Design Decisions

## 2.1 A spell is a valid sentence/command

Earlier, a rule was proposed that a magical command could contain exactly one action.

**That rule was rejected.**

Current principle:

> If a caster can construct a complex sentence that is grammatically valid, semantically unambiguous, and meaningful in the rune language, the magical system should be able to execute it.

Complexity is naturally limited by mana cost because longer expressions require more runes.

The language should not arbitrarily forbid complexity merely because it resembles programming.

---

## 2.2 Language and magic vocabulary are separate concerns

The complete language can contain many runes.

There is currently **no need to minimize the inventory aggressively**.

If the language eventually contains 500 primitives or common semantic elements, that is acceptable. It can be trimmed later.

Likewise:

- A rune may be necessary for ordinary language but useless for magic.
- A rune may be extremely useful for magic but rare in ordinary conversation.
- Beginning casters do not need to know the full language.
- Hidden/advanced runes can be discoveries, rewards, research results, lost knowledge, etc.

This is a feature, not a problem.

---

# 3. Writing Conventions

Temporary Latin-script notation is being used until actual rune glyphs are designed.

## 3.1 Word separator

A normal space has been replaced with:

`|`

Example:

`Self|Know|This.`

`|` is currently punctuation / syntax, not a semantic rune.

**Mana cost: 0**

---

## 3.2 Sentence / command terminator

Every complete sentence or magical command ends with:

`.`

Example:

`Self|Know|This.`

`.` is syntax.

**Mana cost: 0**

---

## 3.3 Compound words

Roots written directly adjacent are one compound word:

`RedGreen`

while:

`Red|Green`

is two separate words.

This distinction is fundamental.

The language takes inspiration from Dutch-style compounding:

> The rightmost element is generally the grammatical head.

However, the earlier idea that every compound could simply mean “B that also satisfies A” was found to be too weak.

Examples such as:

`OppositeTo`
`LightSense`
`EndLife`

do not all use the same semantic relation.

Therefore the current direction is:

> **Compounds are typed. The semantic types of the components determine how they combine.**

This type system is the next major design task.

---

# 4. Mana Cost

Current core idea:

> Each meaning-bearing rune written in a magical command costs mana.

Examples:

- a semantic root costs 1
- each `@` costs 1
- `Opposite` costs 1
- an advanced operator such as `x` costs 1
- `|` costs 0
- `.` costs 0

Longer, more explicit spells are therefore more expensive.

This is intended to make linguistic efficiency mechanically valuable.

---

# 5. Quantity and Magnitude

## 5.1 Unary quantity

`@` represents one unit.

Examples:

`@` = 1  
`@@` = 2  
`@@@@@` = 5

This is especially useful for magical magnitude.

A spell with magnitude 5 literally contains more runes than the same spell with magnitude 1 and therefore costs more.

---

## 5.2 Compression is allowed to reduce mana

A major design decision:

> If a player learns a more efficient valid way to express a number or idea, the spell may genuinely cost less mana.

This is intentional.

Example advanced operator:

`x` = multiplication

A beginner might write sixteen as:

`@@@@@@@@@@@@@@@@`

A knowledgeable caster might write:

`@@@@x@@@@`

Both may describe 16, but the second uses fewer runes and therefore costs less.

This makes knowledge of the magical language itself a form of power.

`x` does **not** have to be part of the starting rune set.

Advanced mathematical or semantic compression can be discovered later.

---

# 6. Negation, Opposites, Zero, and Negative Values

These must be distinguished.

## 6.1 `Not`

`NotX` means that something does not satisfy X.

It is logical negation / complement.

Example:

`NotLife`

includes nonliving things.

A rock can be `NotLife`.

Therefore `NotLife` does **not** mean “dead.”

---

## 6.2 `Opposite`

`Opposite` is a primitive rune candidate.

It costs 1 mana.

Definition:

> `OppositeX` reverses X along a formally defined reversible axis.

Not every rune has an opposite.

Valid candidate examples:

`OppositeTo` = From / away-from direction  
`OppositeBefore` = After  
`OppositeMore` = Less  
`OppositeUp` = Down  
`OppositeJoin` = Separate, if Join is formally modeled as a reversible structural axis/process

Invalid examples unless the ontology later defines an axis:

`OppositeLife`  
`OppositeMatter`  
`OppositeMind`

There is no single objective opposite for these.

Important distinction:

`NotBefore`

means “not before,” which may include simultaneous.

`OppositeBefore`

means specifically “after.”

---

## 6.3 Negative numbers

A free `-` symbol was proposed and rejected.

Negative quantity should use a meaning-bearing rune, so it has a mana cost.

Example:

`Opposite@@`

= -2

This costs:

- `Opposite` = 1
- `@` = 1
- `@` = 1

Total semantic cost: 3.

An advanced compressed negative number might be:

`Opposite@@x@@@`

depending on finalized numeric grammar.

---

## 6.4 Zero

A `Zero` concept is strongly indicated.

Zero is not the same as Not and not the same as Opposite.

Examples:

`ZeroLight` = no light  
`NotLight` = not satisfying whatever `Light` means as a property/category  
`OppositeLight` = invalid unless Light is later placed on a formal reversible axis

This distinction is important.

---

# 7. Color System

Color is currently modeled using RGB-like basis properties.

Primitive candidates:

`Red`
`Green`
`Blue`

Examples:

`RedGreen` = equal Red + Green component  
`GreenBlue` = equal Green + Blue  
`RedBlue` = equal Red + Blue  
`RedGreenBlue` = equal RGB balance

These may correspond to familiar colors depending on light intensity:

- Red + Green → yellow-like
- Green + Blue → cyan-like
- Red + Blue → magenta-like
- balanced RGB at high intensity → white
- balanced RGB at lower intensity → gray
- zero visible light → black

Therefore:

`RedGreenBlue`

does **not** automatically mean White.

Brightness/intensity must be represented separately.

---

## 7.1 Unequal color ratios

`Part` is a candidate for expressing ratios.

Example concept:

`RedPart@@@GreenPart@@@@@`

might represent a Red:Green ratio of 3:5.

Exact syntax is not final.

Ratios should probably normalize, so 3:5 and 6:10 describe the same chromatic proportion.

A separate intensity/magnitude can determine brightness.

This avoids having to write literal RGB values such as 128,128,128.

---

# 8. Fundamental Property Families

The ontology is currently being organized into families.

Different families may have different combination rules.

## 8.1 Existence / ontology

Describes what kind of thing something fundamentally is.

Candidates:

`Thing`
`Matter`
`Life`
`Mind`
`Space`
`Time`

---

## 8.2 Quantity / mathematics

Candidates:

`@`
`Zero`
`Part`
`More`
`Opposite`
advanced `x`

Possible later concepts:

Add
Divide
Power
Root
Ratio
Sequence

---

## 8.3 Composition / structure

Candidates:

`Part`
`Whole`
`Join`
possibly derived `OppositeJoin` = Separate

---

## 8.4 Physical state

Candidates:

`Solid`
`Liquid`
`Gas`

Possible:

`Plasma`

These may be mutually exclusive states within the same family.

Example:

`SolidRedMatter` can be valid because Solid and Red belong to different families.

A direct simultaneous `SolidLiquidMatter` may be invalid or impossible depending on the finalized model.

---

## 8.5 Temperature

Candidate primitive:

`Heat`

Cold should preferably be represented as lower Heat rather than as an independent fundamental substance/property.

`OppositeHeat` should **not** automatically mean Cold.

A negative *change* in Heat can be represented using Opposite on the quantity/change.

---

## 8.6 Light / color

Candidates:

`Light`
`Red`
`Green`
`Blue`

Derived concepts can include yellow, cyan, magenta, white, gray, black, brightness, darkness, etc.

---

## 8.7 Form / geometry

Candidates under consideration:

`Form`
`Size`
`Length`
`Point`
`Line`
`Surface`
`Volume`
`Angle`
`Round`
`Flat`
`Straight`
`Curve`
`Center`
`Edge`
`Hole`
`Symmetry`

This family is unresolved and may grow substantially.

---

## 8.8 Space

Candidates:

`Space`
`At`
`To`
`In`
`Up`
`Near`
`Touch`
`Around`
`Through`
`Between`
`Center`
`Edge`
`Surface`

Likely derived:

`From` = `OppositeTo`
`Down` = `OppositeUp`
`Far` = `OppositeNear`

Important:

`OppositeIn` should not automatically mean Outside.

There is a distinction between:

- reversing a relation
- negating a relation
- reversing participant roles

For example “A is in B,” “B contains A,” and “A is outside B” are three different relationships.

---

## 8.9 Motion

Candidate:

`Move`

Directional meaning should reuse Space rather than invent many motion verbs.

Examples:

Push-like behavior may be Move + away/from  
Pull-like behavior may be Move + toward/to  
Rise may be Move + Up  
Fall may be Move + Down

---

## 8.10 Integrity / damage

Candidates:

`Whole`
`Damage`

Possible derived concepts:

Broken
Repair
Cut
Crush
Burn
Wound
Heal

This allows repair and healing to potentially share underlying rules.

“Heal” can be modeled as restoration of integrity in living matter rather than requiring a primitive Heal law.

---

## 8.11 Life

Candidate primitive:

`Life`

Other concepts to test:

Grow
Reproduce
Eat
Breathe
Plant
Animal
Human
Disease
Poison

Possible derived:

Birth = BeginLife  
Death = EndLife  
Dead = previously Life, no longer Life  
Undead = must describe the actual resulting state rather than relying on an English category

---

## 8.12 Mind

Candidates:

`Mind`
`Think`
`Know`
`Want`
`Feel`
`Sense`

Possible derived:

`LightSense` → sight  
`SoundSense` → hearing

Other uncertain concepts:

Remember
Forget
Sleep
Dream
Pain
Fear
Attention
Believe

---

## 8.13 Time

Candidates:

`Time`
`Before`

Likely derived:

After = `OppositeBefore`
Now = `ThisTime`
Duration = quantity of Time
Always = AllTime

Need a clean way to describe historical properties.

A temporary concept such as `FormerLife` was used for “dead,” but `Former` is not yet accepted as primitive.

Ideally “formerly X” is derivable from temporal grammar.

---

## 8.14 Information / signs

This emerged as an important family.

Candidates:

`Sign`
`Meaning`
`Information`
`Say`

Possible concepts:

Word
Language
Write
Read
Speak
Question
Answer
True
False
Name
Rule
Command
Record
Memory

A useful working idea:

`LightSign` → visual sign  
`SoundSign` → spoken/audible sign

---

## 8.15 Purpose / tools

Candidates:

`For`
possibly `Use`

Potential derived concepts:

Tool
Weapon
Container
House
Door
Sword
Clothing
Food
Medicine

The stress test showed that purpose/function is important to defining many ordinary nouns.

---

# 9. Stress Test Results

A set of ordinary concepts was tested against the early ontology.

## Concepts that were relatively easy

Red → `Red`  
Yellow → `RedGreen`  
Black → likely `ZeroLight`  
Inside → `In`  
See → `LightSense`  
Know → `Know`  
Want → `Want`  
Injury → Damage + living matter  
Repair → restore Whole  
Throw → can likely be expressed as Move with appropriate spatial relations

---

## Concepts exposing missing machinery

### Water

`LiquidMatter` is too broad.

Water cannot be uniquely identified merely as “liquid matter.”

### Stone

`SolidMatter` is too broad.

### Tree

`Life` plus a few generic properties is not enough to uniquely identify tree.

### Hand

`PartLifeMatter` is far too broad.

### Fire

A combination such as Heat + Light + Gas is not automatically unique to fire.

### House

Needs purpose, enclosure, structure, etc.

### Door

Needs boundary, movability, purpose/function.

### Sword

Needs geometry, material properties, purpose/function.

### Sleep

Cannot yet be defined precisely.

### Hear

Revealed need for Sound.

### Speak / Read

Revealed need for Sign / Information concepts.

### Yesterday

Revealed need for temporal measurement/reference.

---

# 10. Specific Kinds / Nouns Remain Unsolved

A major open problem:

How does the language refer to specific kinds such as:

Water
Iron
Oak
Wolf
Human
Hand
Sword

without either:

1. giving every possible noun a primitive rune, or
2. requiring absurdly long descriptions, or
3. allowing arbitrary cheap aliases that break mana balance?

Possible approaches discussed:

- stable definition words
- natural “Kind” categories
- reference by example (“same kind as this”)
- a mixture of these
- semantic molecules / conventional reusable compounds

Important constraint:

> Arbitrary user-defined aliases should not automatically become magical compression.

A caster should not be able to define `Bob` as “gigantic city-destroying explosion” and then cast `Bob|@.` cheaply.

Only compression mechanisms that are actually part of the magical language should reduce mana.

This remains an open design problem.

---

# 11. Candidate Rune Inventory

The inventory was intentionally allowed to grow.

Status labels:

- **E** = Essential candidate
- **D** = Probably derivable
- **M** = Magic-specific / advanced operator
- **U** = Uncertain

These are provisional, not final.

---

## 11.1 Reference / identity / category

E:
- Thing
- Self
- You
- This
- Other
- Same
- Kind
- Part
- Whole

U:
- Person
- Body
- Group
- Name

D:
- People
- OneOf

---

## 11.2 Logic

E:
- Not
- Opposite
- And
- Or
- If
- All
- Some
- Like

U:
- Because
- Can
- Maybe
- True
- Only

D:
- False
- None
- Different
- Either
- Both

---

## 11.3 Quantity / mathematics

E:
- @
- Zero
- Part
- More

D:
- Less
- Equal
- Many
- Few

U:
- Very
- Add
- Ratio
- Sequence
- Between

M:
- x / Multiply
- Divide
- Power
- Root

---

## 11.4 Space

E:
- Space
- At
- To
- In
- Up
- Near
- Touch

U:
- Contain
- Side
- Around
- Through
- Between
- Center
- Edge
- Surface

D:
- From
- Down
- Far
- Across
- Inside
- Outside
- Here

---

## 11.5 Time

E:
- Time
- Before

U:
- During
- Start
- Moment
- Again

E/U:
- End

D:
- After
- Now
- Duration
- Always
- Never
- Former

---

## 11.6 Actions / change

E:
- Do
- Happen
- Make
- End
- Change
- Move
- Join

U:
- Keep
- Begin
- Cause
- Use
- Give
- Get
- Open
D:
- Separate
- Stop
- Take
- Lose
- Break
- Repair
- Create
- Destroy

---

## 11.7 Relations / semantic roles

E:
- With
- Have
- For

U:
- Of
- By
- Using
- About
- Against
- Among
- Exchange

D:
- Without
- Mine

---

## 11.8 Matter / physics

E:
- Matter
- Solid
- Liquid
- Gas
- Force

E/U:
- Energy

U:
- Plasma
- Mass
- Density
- Hard
- Flexible
- Brittle
- Sharp
- Smooth
- Pressure
- Charge
- Magnetic
- Chemical
- Element
- Atom
- Molecule
- Metal
- Organic

D:
- Soft
- Rough

---

## 11.9 Temperature

E:
- Heat

D/U:
- Temperature

D:
- Cold
- Hot
- HeatChange

---

## 11.10 Light / color

E:
- Light
- Red
- Green
- Blue

U:
- Transparent
- Reflect

D/U:
- Opaque

D:
- Yellow
- Cyan
- Magenta
- White
- Gray
- Black
- Bright
- Dark
- Glow

---

## 11.11 Waves / sound

E:
- Sound

U:
- Vibration
- Frequency
- Wave

D:
- Loud
- Quiet

---

## 11.12 Form / geometry

E:
- Form
- Size

E/U:
- Length
- Point
- Line
- Surface

U:
- Width
- Volume
- Angle
- Round
- Flat
- Straight
- Curve
- Center
- Edge
- Hole
- Symmetry

D/U:
- Height

---

## 11.13 Integrity

E:
- Whole
- Damage

D:
- Broken
- Repair
- Cut
- Crush
- Burn
- Wound
- Heal

---

## 11.14 Life

E:
- Life

U:
- Grow
- Reproduce
- Eat
- Breathe
- Plant
- Animal
- Human
- Disease

D/U:
- Blood
- Poison

D:
- Birth
- Death
- Dead
- Undead

---

## 11.15 Mind

E:
- Mind
- Think
- Know
- Want
- Feel
- Sense

U:
- Remember
- Sleep
- Dream
- Pain
- Fear
- Attention
- Believe

D/U:
- Smell
- Taste
- Forget

D:
- See
- Hear
- TouchSense

---

## 11.16 Information / language

E:
- Sign
- Say

E/U:
- Meaning
- Information

U:
- Word
- Language
- Question
- Answer
- True
- Name
- Rule
- Command
- Record
- Memory

D/U:
- Number

D:
- Write
- Read
- Speak
- HearSpeech
- False

---

## 11.17 Purpose / tools

E:
- For

U:
- Use
- Tool

D:
- Weapon
- Container
- House
- Door
- Sword
- Clothing
- Food
- Medicine

---

## 11.18 Social / ordinary language

Mostly U unless later derived:

- Good
- Bad
- Help
- Friend
- Enemy
- Give
- Have
- Owe
- Promise
- Agree
- Ask
- Tell
- Teach
- Learn
- Work
- Play
- Love
- Hate

Possible derived:
- Harm
- Disagree

These may be necessary for a full language without being useful or valid for magic.

---

## 11.19 Magic-specific / advanced

M or M/U candidates:

- Magic
- Mana
- x / Multiply
- Persist
- Trigger
- Repeat
- Copy

Potentially derived magical concepts:

Dispel = EndMagic  
Range = distance quantity  
Duration = Time quantity  
Area = spatial form/extent  
Transform = Change  
Summon = Move something to a location rather than creating it  
Teleport = special Move  
Enchant = persistent Magic associated with Thing

No decision has yet been made on whether Repeat, Trigger, persistent conditionals, etc. are valid magical grammar.

They should not be banned merely because they seem program-like; the actual language semantics should decide.

---

# 12. Natural / Constructed Language Inspirations

Several real systems were identified as useful design references.

These are inspirations, not things to copy wholesale.

## Natural Semantic Metalanguage (NSM)

Useful for:

- asking which meanings are difficult to reduce further
- semantic-prime inventories
- semantic molecules / reusable complex concepts

Its goals differ from this project because NSM describes human meaning, while the rune language must also describe objective physical/magical states.

---

## aUI

Useful for:

- small meaningful elements combining into larger semantic units
- treating the smallest written elements as morphemes rather than letters

---

## Blissymbolics

Useful for:

- graphical meaning-based symbols
- generative compounds
- a relatively small set of key semantic elements supporting a much larger vocabulary

---

## Dutch compounding

Useful for:

- head-final/right-headed compound intuition
- making compound structure predictable

Do not copy natural-language irregularity.

---

## Lojban

Useful for:

- parser-like grammatical precision
- defined semantic roles / argument places

Major warning:

- syntactic clarity alone does not guarantee semantic clarity
- modifier compounds can still have multiple plausible interpretations

The rune language must therefore formalize semantic composition more strictly.

---

## Ithkuil

Useful for:

- explicit semantic roles
- encoding precise relations morphologically

Avoid its extreme complexity.

---

## Toki Pona

Useful as a stress test for whether a primitive is truly necessary.

Warning:

- it relies heavily on context
- magical execution cannot rely on “you know what I meant”

---

# 13. Rejected or Superseded Ideas

These should not silently return without discussion.

## Rejected: one action per magical command

Old proposal:

> A magical command may contain exactly one Action and it must be first.

Rejected.

Current rule:

> Any grammatically and semantically valid complex sentence should be allowed.

---

## Rejected: free minus sign

Old proposal:

`-@@`

with `-` costing nothing.

Rejected.

Negative values should require a meaning-bearing operation such as `Opposite`, so changing sign has a cost.

---

## Superseded: universal “A modifies B” compound rule

Old proposal:

`AB` always means “B which also satisfies A.”

This works for some property/entity compounds but not for all meaningful compounds.

Current direction:

> typed composition rules determine the meaning of compounds.

---

## Rejected: arbitrary aliases as free magical compression

A short name should not automatically allow a complex magical definition to be cast cheaply.

Only genuine language operators/semantic constructions recognized by the magic system can produce mana savings.

---

# 14. Current Most Important Open Question

The next major design task is the **type system**.

Provisional type candidates:

- Entity
- Property
- Quantity
- Action
- Relation
- Reference
- State
- Phenomenon
- Axis
- Information
- perhaps Event
- perhaps Kind
- perhaps Form
- perhaps Location / Time-reference

The goal is to define legal typed compositions such as:

`Property + Entity -> restricted Entity`

`Opposite + Axis -> inverse Axis`

`Phenomenon + Sense -> Sense specialized to that phenomenon`

`Quantity + scalar Property -> measured Property`

and determine which root orderings are legal or invalid.

This is intended to prevent semantic ambiguity inside compound words.

After the type system, major upcoming tasks are:

1. Test typed compounding against the candidate inventory.
2. Define complex sentence grammar / semantic roles.
3. Solve specific kinds and nouns (water, iron, oak, wolf, hand, sword).
4. Formalize numbers and measurement.
5. Formalize magical execution of valid commands.
6. Define what happens with impossible, contradictory, underspecified, or underpowered commands.
7. Split the complete language into:
   - ordinary language inventory
   - magically meaningful vocabulary
   - beginner caster vocabulary
   - hidden/advanced vocabulary
8. Eventually design actual rune glyphs.

---

# 15. Design Philosophy Going Forward

When deciding whether a new primitive rune is needed:

1. Do not reject it merely to keep the rune count low.
2. First ask whether it makes the language clearer and more objective.
3. Later test whether it can be derived cleanly.
4. If derivation is awkward or ambiguous, keep the primitive.
5. Ordinary language requirements and spellcasting requirements may diverge.
6. Context-dependent interpretation is acceptable for natural human conversation only if needed, but magical commands should resolve objectively.
7. A spell's creativity should come from composition, not GM negotiation.
8. Language mastery should be mechanically valuable.
9. Discovering shorter valid expressions may reduce mana cost.
10. The system should reward understanding the language rather than memorizing a spell list.

---

# 16. One-Sentence Summary

> Build a typed, compositional rune language capable of ordinary expression, then let magic execute valid sentences from that language, with each meaning-bearing rune costing mana and linguistic compression providing real mechanical efficiency.