# Temporary Surface Syntax and Parsing

_Status: canonical transliteration syntax v0.1_

This file defines a deterministic ASCII/Latin notation for writing and testing Cuspell before actual rune glyphs are designed.

The semantic AST is normative. Future glyph design may encode the same grammar differently.

## 1. Root tokens

Registered semantic roots are written as capitalized labels in transliteration:

`Life`

`Move`

`Opposite`

`Water`

Each root token corresponds to one meaning-bearing rune when the real script is designed.

## 2. Compound words

Adjacent root tokens with no separator form one compound word.

Examples:

`RedMatter`

`OppositeBefore`

`EndLife`

`RedGreenBlue`

In Latin transliteration, capitalization identifies root boundaries for humans/parser dictionaries.

A compound is not valid merely because the roots can be written adjacent; typed compound rules must license its parse.

## 3. Word/expression separator

`|` separates words/arguments in linear syntax.

It is grammar and costs zero mana.

Example:

`Life|This`

## 4. Sentence terminator

Every complete sentence ends with:

`.`

The terminator is zero-mana syntax.

## 5. Mood

### Assertion

No prefix:

`Life|This.`

### Question

`?` prefix:

`?Life|This.`

### Command

`!` prefix:

`!EndLife|This.`

Mood marks are zero-mana grammar.

## 6. Grouping

Parentheses form one nested expression:

`( ... )`

They cost zero mana.

Examples:

`If|(Life|This)|(EndLife|This)`

`Equal|(Duration|$e)|@@TimeUnit`

A parser never relies on visual spacing.

## 7. Head-first application

Clause/application syntax is head-first.

A head Word is followed by arguments in its registered canonical frame order.

Examples:

`Life|This`

= Life(This)

`In|This|RegionRef`

= In(This, RegionRef)

`Move|This|Here`

= Move(theme=This, goal=Here)

The head's type/frame determines how many positional arguments are legal.

## 8. Nested arguments

Any argument that is itself a multi-token expression must be grouped.

Example:

`Equal|(Duration|$e)|@@TimeUnit`

Without grouping, a parse that would be ambiguous is invalid.

## 9. Positional frame rule

Every Relation/Process/Operator declares a compact positional prefix.

Only that declared prefix may be supplied positionally.

Optional/noncanonical roles use explicit role markers.

This prevents a parser from guessing where optional arguments belong.

Example Move compact frame:

1. theme
2. goal

Source/path/power can be role-marked.

## 10. Role markers

Temporary syntax:

`:role`

A role marker applies to the following grouped/atomic argument.

Example:

`Move|This|Here|:source|There`

`:power|@@@@`

Role names in this file are transliteration labels for grammatical case/slot marks, not semantic roots.

They cost zero mana.

A role marker is legal only when the head declares that role.

## 11. Standard role labels

Current parser-level labels include:

- `:theme`
- `:agent`
- `:experiencer`
- `:stimulus`
- `:content`
- `:source`
- `:goal`
- `:recipient`
- `:instrument`
- `:beneficiary`
- `:result`
- `:location`
- `:time`
- `:duration`
- `:cause`
- `:path`
- `:power`
- `:period`
- `:lifetime`

Actual rune grammar may represent these with case marks/placement rather than literal labels.

## 12. Binders

Binder declaration:

`[a:Domain]`

Bound reference:

`$a`

Examples in abstract linear syntax:

`All|[a:Human]|(Life|$a)`

`Collect|[h:Human]|(In|$h|RoomRef)`

Variable letters are zero-mana parser labels.

Binder scope is the smallest containing grouped expression/operator frame that declares it unless explicitly extended by that frame.

Free variables are invalid in a completed sentence.

## 13. Process result binders

A result-producing Process can bind its declared result using a role marker plus binder:

`Create|WaterProfile|:result|[w:Entity]`

Within the containing Sequence/group:

`$w`

refers to the fresh result.

The declared binder type must match the Process result type.

## 14. Event binders

An executed/constructed Event can similarly bind an EventRef when the control structure supports it.

Temporary:

`:event|[e:Event]`

Then:

`Begin|$e`

`Duration|$e`

can refer to the concrete Event in later sequence structure where semantically valid.

## 15. Finite collection literals

Temporary grammar:

`{A,B,C}`

Braces and commas are syntax and cost zero mana.

Each listed semantic expression retains its own rune cost.

Collection literals are typed; incompatible members require an explicitly broader common type or are invalid.

## 16. Sequence literals

An ordered brace list used where `Sequence<T>` is expected preserves order.

Example conceptual command:

`!Sequence|{(Repair|This|Template),(BeginLife|This)}.`

Sequence itself is meaning-bearing; braces merely encode its arguments.

## 17. Variable-arity operators

Variable-arity semantic Operators should consume a Collection/Sequence argument rather than relying on "read until it feels finished."

Examples:

`And|{P1,P2,P3}`

`Or|{P1,P2}`

`Join|{A,B,C}`

This keeps parsing deterministic.

## 18. Quotation

Temporary quotation notation:

`« ... »`

Quotation causes enclosed syntax to be treated as Sign/Information content rather than executed/interpreted at the enclosing semantic level.

The delimiters cost zero.

Semantic roots physically written inside a quoted magical Command still count as written semantic runes for mana-accounting if the quotation is itself part of that Command.

## 19. Numbers

Unary numbers remain adjacent @:

`@@@@`

Arithmetic can use registered operator notation.

For testing, `x` remains infix-compatible in numeric words where unambiguous:

`@@@@x@@@@`

More complex numeric expressions should be grouped.

The parser uses fixed precedence from NUMBER_AND_MEASUREMENT.

## 20. Zero-mana syntax list

Current zero-mana syntax:

- `|`
- `.`
- `!`
- `?`
- `(` `)`
- `{` `}`
- commas inside collection literals
- role/case markers
- binder marks/labels
- variable-reference marks
- quotation delimiters

These structures determine grammar, not world semantics.

## 21. Mana-bearing material

Mana-bearing items include every written registered semantic root/operator/value rune, including when used inside compounds.

Examples:

`RedMatter` normally contains two semantic runes.

`Water` may be one registered semantic rune even if its dictionary recognition rule is complex.

`@@@@x@@@@` contains nine semantic runes.

## 22. Whitespace

Whitespace is typographic only and ignored around syntax tokens.

It never carries grammar.

## 23. Parse uniqueness

A completed expression is valid only if:

- root segmentation is unique under the registered lexicon/compound rules;
- grouping/frame assignment is unique;
- all legal parses normalize to one semantic structure.

Otherwise it must be rewritten/grouped.

## 24. Canonical serialization

The eventual reference parser should provide a canonical serialization of the AST for testing.

For example, surface:

`!Move|This|Here|:power|@@@@.`

may normalize internally to something like:

`Command(Move(theme=This,goal=Here),Power=4)`

The internal form is diagnostic only; the player writes Cuspell surface syntax.

## 25. Future rune script

Actual glyph design may encode:

- compounds by spatial attachment;
- case/role by small marks;
- grouping by enclosures;
- mood by sentence marks;
- binders by connecting strokes or labels.

The glyph system must preserve the same unambiguous AST.

Visual beauty must not introduce semantic ambiguity.
