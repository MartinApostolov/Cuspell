# Temporary Surface Syntax and Parsing

_Status: canonical transliteration syntax v0.2_

This file defines the current ASCII/Latin notation for writing and testing Cuspell before final rune glyphs are designed.

The semantic AST remains normative. The surface language is deliberately flatter than v0.1.

The central v0.2 change is:

- **whitespace separates expressions/phrases;**
- **`|` explicitly binds fields into one application phrase.**

Thus:

`Move|A|B|C`

is one application phrase, while:

`Move|A|B C`

contains the application phrase `Move(A,B)` followed in the token stream by a separate expression `C`.

Whitespace itself does not mean Sequence, And, or any other semantic relation.

## 1. Root tokens

Registered semantic roots are written as capitalized labels in transliteration:

`Life`

`Move`

`Opposite`

`Water`

Each registered root token corresponds to one meaning-bearing rune in the future script.

## 2. Compound words

Roots written directly adjacent with no whitespace or pipe form a lexical compound candidate.

Examples:

`RedMatter`

`OppositeBefore`

`EndLife`

`RedGreenBlue`

A compound is legal only when registered typed composition rules license it.

Adjacency is therefore lexical composition.

Pipe is syntactic application.

Whitespace is phrase separation.

These three operations are distinct.

## 3. Whitespace

Whitespace is now grammatically significant.

A whitespace boundary not bridged by a pipe terminates the current application phrase.

Examples:

`Move|A|B C`

tokenizes into two phrases:

1. `Move|A|B`
2. `C`

Likewise:

`Life|This Red|That`

contains two Proposition expressions in sequence in the source stream.

Whether a surrounding grammatical structure permits multiple expressions is a separate question.

Whitespace does **not** itself mean:

- then;
- and;
- sequence;
- conjunction;
- another magical action.

Therefore:

`!Move|A|B C.`

is not automatically equivalent to:

`!Sequence|{Move|A|B,C}.`

If command grammar expects exactly one EventSpec and receives two top-level expressions, the sentence is invalid unless an explicit structure consumes both.

## 4. Pipe binding

`|` is a zero-mana syntactic binding connector.

It says that the fields it connects belong to one application phrase.

Examples:

`Life|This`

`Move|This|Here`

`Same|A|B`

`Change|This|Heat|Q`

Pipe binding is stronger than whitespace.

For transliteration/readability, optional spaces around a written pipe are ignored:

`Move | A | B`

is identical to:

`Move|A|B`

because each whitespace boundary is explicitly bridged by `|`.

But:

`Move|A|B C`

has no pipe bridging the boundary before C, so C begins a new phrase.

## 5. Phrase

A **pipe phrase** is the maximal sequence of fields connected by pipes.

A phrase must parse to exactly one semantic expression.

Examples:

`Cat|Self`

`If|Life|This|EndLife|This`

`Equal|Duration|$e|Q`

A phrase may contain nested semantic applications without parentheses because registered frames and types determine how fields are consumed.

## 6. Typed prefix parsing inside a phrase

Pipe phrases use typed prefix parsing.

The first field is the outer head.

The parser then satisfies that head's declared frame from left to right.

If an argument slot expects a value that is itself produced by a functional Relation/Operator/Process expression, the next field may become a nested head and recursively consume following fields.

Example:

`Equal|Duration|$e|Q`

normalizes to:

`Equal(Duration($e), Q)`

because:

- Equal expects two comparable values;
- Duration is a function requiring one Event argument;
- Duration consumes `$e`;
- Q supplies Equal's second argument.

No parentheses are required.

Another example:

`If|Life|This|EndLife|This`

normalizes to:

`If(Life(This), EndLife(This))`

when the selected If frame expects a Proposition followed by an EventSpec.

## 7. Full-consumption rule

A pipe phrase is valid only if one legal parse consumes every field in the phrase.

Example:

`Move|A|B|C`

means a Move application with the declared positional prefix filled through the third supplied slot when the types are compatible.

It cannot silently parse as:

`Move(A,B)`

with an unused C, because C is pipe-bound into the same phrase.

By contrast:

`Move|A|B C`

explicitly ends the Move phrase before C.

## 8. Positional frame prefixes

Every callable root declares one or more ordered frames.

Optional positional roles may be supplied only as a contiguous prefix.

Example working Move frame:

1. theme — required
2. goal — optional/strongly typical
3. source — optional
4. path — optional

Therefore:

`Move|A`

may produce a meaningful but execution-incomplete EventSpec.

`Move|A|B`

binds theme=A, goal=B.

`Move|A|B|C`

binds theme=A, goal=B, source=C.

`Move|A|B|C|D`

binds theme=A, goal=B, source=C, path=D.

To skip an earlier optional slot while supplying a later one, use a role marker.

## 9. Type-directed nesting

Whether a field is treated as a direct argument value or as a nested head depends on the expected slot type and the field's registered frames.

Example conceptually:

`Preserve|Volume|This|Change|This|Density|Multiply|@@|BeforeValue|Density|This`

can normalize to:

`Preserve(
  Volume(This),
  Change(
    This,
    Density,
    Multiply(
      2,
      BeforeValue(Density(This))
    )
  )
)`

provided the selected frames/types uniquely license that parse.

Important details:

- `Volume` is parsed as a function when the slot expects a value, so it consumes `This`.
- `Density` in Change's attribute slot is parsed as an Attribute descriptor, not automatically as `Density(This)`.
- `Density` inside BeforeValue is parsed as the value function and therefore consumes `This`.
- `BeforeValue(value)` may use the nearest enclosing EventSpec boundary context as defined in RELATIVE_CHANGE_AND_FIELDS.

The type system therefore provides much of the grouping structure.

## 10. Ambiguity rule

Type-directed parsing is not permission to guess.

For each phrase:

- zero legal full-consumption parses -> invalid;
- one legal full-consumption parse -> valid;
- multiple parses that normalize to the same AST -> valid;
- multiple parses with different meanings -> ambiguous and invalid until rewritten.

The parser never selects the parse that "sounds most natural."

## 11. Explicit grouping

Parentheses remain available as zero-mana hard grouping when:

- several typed parses remain;
- the writer wants to force a particular subexpression boundary;
- a nested variadic structure cannot be inferred safely.

Example:

`Equal|(Duration|$e)|Q`

remains legal, but under v0.2 the shorter:

`Equal|Duration|$e|Q`

is preferred when unambiguous.

Parentheses are now an escape hatch rather than the normal style.

## 12. Role markers

Temporary role syntax remains:

`:role`

A role marker is a zero-mana grammatical field that assigns the following expression to a named role of the current head.

Examples:

`Move|This|Here|:source|There`

`Move|This|:path|PathRef`

`CastLikeProcess|Target|:power|@@@@`

A role marker does not break the pipe phrase when pipe-connected.

A role marker is legal only if the active frame declares that role.

## 13. Standard role labels

Current parser-level roles include:

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

Final glyph grammar may encode these through case marks or spatial attachment.

## 14. Sentence terminator

Every complete sentence ends with:

`.`

The terminator is zero-mana syntax.

A period also gives the parser a hard end boundary.

## 15. Mood

Assertion has no prefix:

`Cat|Self.`

Question:

`?Life|This.`

Command:

`!EndLife|This.`

Mood marks remain zero-mana grammar.

## 16. Multiple phrases inside a sentence

Whitespace can separate multiple expressions, but a sentence must still have a grammatical structure that consumes them.

Valid possibilities include:

- explicit discourse constructions;
- collection/list syntax;
- quotation;
- a grammar form that deliberately accepts multiple phrases.

A magical Command normally expects one complete EventSpec/control expression after `!`.

Therefore bare juxtaposition is not a free replacement for `And` or `Sequence`.

This preserves the rule that semantic ordering/conjunction is meaning-bearing.

## 17. Collections

Finite collection/list syntax remains:

`{A,B,C}`

Braces and commas are zero-mana syntax.

Each item is parsed as its own expression.

Pipe phrases inside items may remain flat:

`{Move|A|B,EndLife|C}`

A typed list can then serve variable-arity structures.

Example:

`Sequence|{Move|A|B,EndLife|C}`

## 18. Variadic heads

A variadic head may consume all remaining compatible arguments only when the phrase/frame makes the boundary unique.

To avoid ambiguity, the canonical style for arbitrary-length argument sets remains a collection/list.

Preferred:

`And|{P1,P2,P3}`

rather than relying on an unrestricted variadic pipe chain.

Small fixed-arity conventional frames may still use direct pipes.

## 19. Binders

Binder syntax remains:

`[a:Human]`

Bound reference:

`$a`

The v0.2 flat form allows:

`All|[a:Human]|Life|$a`

instead of:

`All|[a:Human]|(Life|$a)`

when the parse is unique.

Likewise:

`Collect|[h:Human]|In|$h|RoomRef`

Binders and variable-reference marks are zero-mana grammar.

## 20. Result and event binders

Result/event binder syntax remains role-based.

Example conceptual structure:

`Create|WaterProfile|:result|[w:Entity]`

Within the containing scope, `$w` denotes the result.

Event bindings may similarly use:

`:event|[e:Event]`

The exact enclosing scope rules remain defined by the consuming control structure.

## 21. Quotation

Quotation remains:

`« ... »`

Quotation creates Sign/Information content instead of evaluating the enclosed material at the outer level.

Whitespace and pipes inside quotation remain part of the quoted syntax.

Quotation delimiters cost zero mana.

Semantic runes physically written inside quoted content still count when the quote itself is part of a magical Command, according to existing mana rules.

## 22. Arithmetic

The canonical parser-facing arithmetic form may use ordinary registered heads:

`Multiply|@@|Q`

`Add|A|B`

`Power|A|B`

The existing compact numeric notation such as:

`@@@@x@@@@`

remains permitted as lexical arithmetic sugar when its parse is unique.

A one-sided compact form may also be supported:

`@@x|Q`

normalizing to:

`Multiply(@@, Q)`

if the machine-readable syntax package registers `x` as an open infix continuation.

The fully explicit head form remains the reference form for parser diagnostics.

## 23. Zero-mana syntax

Current zero-mana syntax includes:

- whitespace phrase boundaries;
- `|` binding connector;
- `.`
- `!`
- `?`
- parentheses;
- collection braces/commas;
- role/case markers;
- binder marks/labels;
- variable-reference marks;
- quotation delimiters.

These marks organize semantic material but do not themselves denote world concepts.

## 24. Mana-bearing material

Every written registered semantic rune/operator/value remains mana-bearing.

Examples:

`RedMatter`

normally contains two semantic runes.

`Water`

may be one semantic rune even if its recognition rule is complex.

`Move|This|Here`

contains the semantic roots Move, This, Here; the pipes cost zero.

## 25. Line breaks

A line break is whitespace and therefore ends a phrase unless a pipe explicitly bridges it.

This permits readable formatting:

`Preserve | Volume | This |`
newline
`Change | This | Density | Multiply | @@ | BeforeValue | Density | This`

because the pipe at the boundary continues the phrase.

Without a bridging pipe, the newline begins a new phrase.

## 26. Canonical style

Prefer the flattest uniquely parseable form.

Preferred:

`If|Life|This|EndLife|This.`

instead of:

`If|(Life|This)|(EndLife|This).`

Preferred:

`All|[a:Human]|Life|$a.`

instead of grouped forms when both normalize identically.

Use grouping only when it carries necessary parse information or materially improves human readability.

## 27. Canonical serialization

The reference parser should serialize a validated phrase to a stable AST form.

Example surface:

`!Move|This|Here|:power|@@@@.`

may normalize to:

`Command(Move(theme=This,goal=Here),Power=4)`

Example surface:

`Equal|Duration|$e|Q.`

may normalize to:

`Assertion(Equal(Duration($e),Q))`

The serialization is diagnostic/tooling data, not player syntax.

## 28. Future rune script

Final rune writing may represent:

- lexical compounds by attached glyphs;
- pipe binding by a connecting stroke/line;
- whitespace by literal separation;
- role/case by small marks;
- grouping by enclosures;
- binders by linking marks;
- mood by sentence marks.

The conceptual distinction should survive:

> touching/merged glyphs = lexical compound;
> connected glyphs = one application phrase;
> separated glyphs = separate expressions.

This gives the eventual rune script a natural visual grammar rather than making it resemble parenthesized programming notation.
