# Cuspell Rune Language — New Thread Handoff

Continue the design of a D&D-style freeform magic system based on a formal rune language.

## Core intent

The user previously made a rune-magic supplement where players combined runes to invent spells. It was fun but too subjective: caster and GM had to debate what rune combinations meant.

The remake should preserve free construction while making meanings objective.

The magical language should be a genuine compositional/formal language, not English written with custom glyphs.

The full language can be much larger than the subset useful for magic. Do **not** aggressively minimize the rune count yet. It is acceptable to have hundreds of candidate runes and trim later.

## Current notation

- `|` = word separator; syntax, 0 mana
- `.` = mandatory sentence/command terminator; syntax, 0 mana
- adjacent roots form one compound word: `RedGreen`
- `@` = one quantity/magnitude unit; costs 1
- `Opposite` = primitive semantic rune; costs 1
- advanced `x` = multiplication/compression operator; likely hidden from beginners; costs 1

Every meaning-bearing rune in a magical command costs mana.

A more linguistically efficient valid expression can genuinely cost less mana. This is intentional. Knowledge of the magical language itself should grant efficiency.

Example concept:
- 16 as `@@@@@@@@@@@@@@@@` is expensive
- once multiplication is learned, something like `@@@@x@@@@` can express 16 more cheaply

Do not “fix” this by charging the expanded value. The user explicitly likes magical compression reducing mana.

## Important decisions

### Complex commands ARE allowed

Do not impose “one action per spell.”

The user explicitly rejected that.

Current principle:

> If a complex sentence is valid, objective, and meaningful in the language, magic should execute it.

It can have multiple actions.

We can still later decide whether particular constructions such as loops/repetition exist, but do not ban complexity merely because it resembles programming.

### Language and magic are different layers

A concept may be needed in the complete language but irrelevant to spellcasting.

Beginning casters do not need the whole language.

Hidden/advanced runes are desirable.

### Compounds

Dutch-style right-headed compounding is an inspiration.

However, do NOT use the simplistic universal rule:

`AB = B which also satisfies A`

for every compound.

That works for things like `RedMatter`, but not for:

- `OppositeTo`
- `LightSense`
- `EndLife`

Current direction:

> Every root has a semantic type. Legal type combinations determine exactly how compounds compose.

The type system is the next design task.

## Negation / opposition

Keep these distinct:

- `NotX` = logical negation; does not satisfy X
- `ZeroX` = amount of X is zero
- `OppositeX` = reverse X along a formally defined reversible axis

Not every rune has an opposite.

Examples:
- `OppositeTo` = From
- `OppositeBefore` = After
- `OppositeMore` = Less
- `OppositeUp` = Down
- possibly `OppositeJoin` = Separate

But:
- `OppositeLife` is invalid unless an explicit Life axis is later defined
- `OppositeMatter` is not meaningful by default

Important:
`NotBefore` may include simultaneous.
`OppositeBefore` means specifically After.

A free `-` negative sign was proposed and rejected.

Negative 2 should be something like:

`Opposite@@`

so sign reversal costs mana.

## Color

RGB-style basis:

- `Red`
- `Green`
- `Blue`

Examples:
- `RedGreen` = equal Red + Green
- `GreenBlue`
- `RedBlue`
- `RedGreenBlue` = equal RGB balance, NOT automatically white

Brightness/intensity is separate.

Therefore balanced RGB can be gray or white depending on Light/intensity.

Black is better modeled as `ZeroLight`, not `NotRedGreenBlue`.

Unequal channel ratios may use `Part`, e.g. conceptually:

`RedPart@@@GreenPart@@@@@`

Exact syntax not final.

## Fundamental property families currently identified

- existence / ontology
- quantity / mathematics
- composition / structure
- physical state
- temperature
- light / color
- form / geometry
- space
- motion
- integrity / damage
- life
- mind
- time
- information / signs
- purpose / tools

## Strong candidate roots / concepts

Do not treat this as final. The project is intentionally overinclusive for now.

Reference/identity:
Thing, Self, You, This, Other, Same, Kind, Part, Whole

Logic:
Not, Opposite, And, Or, If, All, Some, Like

Quantity:
@, Zero, Part, More
advanced: x/Multiply, Divide, Power, Root

Space:
Space, At, To, In, Up, Near, Touch
likely derived: From, Down, Far

Time:
Time, Before
likely derived: After, Now, Duration

Actions/change:
Do, Happen, Make, End, Change, Move, Join
possible: Keep, Begin, Cause, Use, Give, Get, Open

Relations:
With, Have, For
possible: By, Using, About, Against, Among

Matter/physics:
Matter, Solid, Liquid, Gas, Force
possible: Energy, Plasma, Mass, Density, Hard, Flexible, Brittle, Sharp, Smooth, Pressure, Charge, Magnetic, Chemical, Element, Atom, Molecule

Temperature:
Heat

Light/color:
Light, Red, Green, Blue

Sound/waves:
Sound
possible: Vibration, Frequency, Wave

Form:
Form, Size
possible: Length, Point, Line, Surface, Volume, Angle, Round, Flat, Straight, Curve, Center, Edge, Hole, Symmetry

Integrity:
Whole, Damage
derived candidates: Broken, Repair, Cut, Crush, Burn, Wound, Heal

Life:
Life
possible: Grow, Reproduce, Eat, Breathe, Plant, Animal, Human, Disease, Poison

Mind:
Mind, Think, Know, Want, Feel, Sense
derived candidates: LightSense = sight, SoundSense = hearing

Information:
Sign, Say
possible: Meaning, Information, Word, Language, Question, Answer, True, Name, Rule, Command, Record, Memory

Purpose:
For
possible: Use, Tool
derived candidates: Weapon, Container, House, Door, Sword, Food, Medicine

Magic:
Magic, Mana, Persist, Trigger, Repeat, Copy etc. are candidates, not settled.

## Stress-test findings

The system could already plausibly express:
- red
- yellow
- black
- inside
- seeing
- knowing
- wanting
- some movement actions
- damage / repair concepts

But these exposed missing machinery:
- Water: `LiquidMatter` is too broad
- Stone: `SolidMatter` is too broad
- Tree: generic Life properties do not uniquely identify it
- Hand: `PartLifeMatter` too broad
- Fire: Heat + Light + Gas is not necessarily uniquely fire
- House: needs purpose/structure/enclosure
- Door: needs boundary + purpose
- Sword: needs geometry/material/purpose
- Sleep: not yet precisely representable
- Yesterday: needs temporal measurement/reference

This leads to a major unresolved problem:

> How does the language identify specific kinds/nouns such as Water, Iron, Oak, Wolf, Human, Hand, Sword without either making every noun primitive or allowing arbitrary aliases to become cheap magical compression?

Possible ideas:
- Kind categories
- semantic molecules
- stable definitions
- reference by example (“same Kind as This”)
- combination of those

Arbitrary player-defined aliases must NOT automatically reduce spell mana.

## Inspirations already considered

Study/use ideas from:
- Natural Semantic Metalanguage (semantic primes + semantic molecules)
- aUI (small meaningful elements combine)
- Blissymbolics (meaning-based graphical compounds)
- Dutch compounding (right-headed compounds)
- Lojban (parser-level syntax, semantic roles; also a warning that unambiguous syntax does not guarantee unambiguous compound meaning)
- Ithkuil (explicit semantic roles; avoid its complexity)
- Toki Pona (stress test for whether a primitive is really necessary; avoid context dependence in magic)

## NEXT TASK

Design the semantic **type system**.

Candidate types include:
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
- Event
- Kind
- Form
- Location
- Time-reference

The goal is to define legal operations such as:

`Property + Entity -> Entity`

`Opposite + Axis -> Axis`

`Phenomenon + Sense -> specialized Sense`

`Quantity + scalar Property -> measured Property`

and determine whether root order changes legality/meaning.

The type system should make compound meanings objective and should reject invalid combinations without GM interpretation.

After that:
1. stress-test typed compounds
2. define complex sentence grammar / semantic roles
3. solve specific-kind nouns
4. formalize numbers/measurement
5. formalize magical execution and failures
6. split full language / magical subset / beginner subset / hidden advanced vocabulary
7. eventually design actual rune glyphs

## Tone / design preference

Do not rush to minimize.

The user likes emergent cleverness and rewards for discovering more efficient language.

The aim is not “simple spell list with weird syntax.”

The aim is:

> a real formal/compositional language where understanding the language lets players invent objective magical commands.