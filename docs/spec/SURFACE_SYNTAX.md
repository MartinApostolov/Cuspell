# Temporary Surface Syntax and Parsing

_Status: canonical transliteration syntax v0.3_

This file defines the current ASCII/Latin notation used before final rune glyphs are designed.

The semantic AST remains normative.

## 1. The three visible joins

Cuspell now distinguishes three increasingly explicit ways for written material to relate.

### Adjacency: lexical composition

Registered roots written directly together form one lexical compound candidate.

Examples:

`SolidWater`

`NotLife`

`OppositeBefore`

`EndLife`

Adjacency is meaning-bearing lexical composition. A concatenation is legal only when registered compound rules license it.

### Whitespace: ordinary token separation

Whitespace is the normal way to write successive Cuspell words/runes.

Examples:

`SolidWater This.`

`Move This Here.`

`If Life This EndLife This.`

Whitespace does not itself mean application, And, Sequence, or any other semantic relation. The typed parser uses registered frames and result types to determine how the token stream composes.

### Pipe: hard application binding

`|` explicitly binds the connected tokens into one complete subexpression before the surrounding token stream is parsed.

Examples:

`Move|This|Here.`

is an explicit form of:

`Move This Here.`

while:

`Move|A|B C`

first creates the hard-bound subexpression `Move(A,B)`; `C` remains outside that group.

A pipe group must be complete by itself for the type expected at that location. The parser never lets later whitespace-separated tokens leak back inside it.

## 2. Typed prefix parsing

The ordinary whitespace stream uses typed prefix parsing.

A head selects one of its registered frames. Its arguments are recursively consumed from left to right according to each slot's required type.

Example:

`Equal Duration ThisEvent @@.`

can normalize to:

`Equal(Duration(ThisEvent), 2)`

when the types and dimensions are compatible.

Example:

`!If Life This EndLife This.`

normalizes to:

`Command(If(Life(This), End(Life(This))))`.

No parentheses or pipes are required when exactly one full type-correct parse exists.

## 3. Full-consumption and ambiguity rules

A complete sentence must have a parse that consumes every top-level token.

- zero full parses -> invalid;
- one semantic normal form -> valid;
- several parses with the same normal form -> valid;
- several distinct semantic normal forms -> ambiguous and invalid until rewritten.

The parser never chooses the most plausible interpretation.

Whitespace therefore gives no free conjunction or sequencing. For example, a complete Move followed by an unrelated EventSpec is invalid unless an explicit semantic structure such as Sequence consumes both.

## 4. Hard binding with pipe

A maximal pipe-connected group is parsed independently as one expression.

Equivalent when unambiguous:

`Move This Here`

`Move|This|Here`

Mixed form is allowed:

`If Life|This EndLife|This`

The two pipe groups are parsed first and then supplied to If.

A hard-bound group is useful when:

- the ordinary token stream would have more than one parse;
- the writer wants to force a boundary;
- a complex expression is easier to inspect with explicit structure.

Pipe is zero-mana syntax.

Spaces around a pipe are ignored:

`Move | This | Here`

is the same hard group as:

`Move|This|Here`.

## 5. Parentheses

Parentheses remain the strongest explicit grouping escape hatch.

They are useful when a desired group contains spaces or when pipe grouping would be visually awkward.

Example:

`If (Life This) (EndLife This)`

Parentheses are zero-mana syntax and do not alter semantic cost.

Canonical player-facing style should prefer ordinary spaces, then pipe only when useful, then parentheses for genuinely difficult cases.

## 6. Sentence mood and termination

Assertion has no mood prefix:

`Cat Self.`

Question:

`?Life This.`

Command:

`!Move This Here.`

Every complete sentence ends with `.`.

Mood marks and the terminator cost zero mana.

## 7. Role markers

Temporary role syntax remains:

`:role`

A role marker assigns the following expression to a named role in the currently active frame.

Examples:

`Move This Here :source There`

`Move This :path ThisPath`

This lets a writer skip optional positional roles without ambiguity.

Role markers are zero-mana grammar.

## 8. Collections

Finite structural collections remain:

`{A,B,C}`

Each item is a complete expression and may use ordinary space syntax:

`Sequence {Move This Here,EndLife Self}`

Braces and commas cost zero mana.

Variadic heads should prefer a collection when an unbounded whitespace stream would make the stopping point unclear.

## 9. Binders

Binder declaration:

`[a:Human]`

Reference:

`$a`

Example:

`All [a:Human] Life $a.`

Binder marks and variable labels are grammar and cost zero mana. Semantic Kind roots written in binder domains still cost normally.

Derived compound Kinds may appear as binder domains:

`All [a:SolidWater] ...`

when the compound is legal.

## 10. Quotation

Quotation remains:

`« ... »`

Quotation produces Sign/Information content instead of evaluating the enclosed expression at the outer semantic level.

The quotation marks cost zero mana; semantic runes physically written inside a magical quotation still count according to the existing mana rule.

## 11. Lexical compounds versus syntactic grouping

These must not be confused.

`SolidWater`

is one lexical compound expression built from adjacent meaning-bearing roots.

`Solid|Water`

is a hard syntactic application group and is not automatically the same thing.

Only registered lexical compound rules license adjacency meanings such as Property + Kind restriction.

This distinction will eventually be visible directly in the rune script.

## 12. Exact registered roots in transliteration

The temporary Latin spelling has one limitation the final rune script will not have: an exact registered root label can happen to contain text that could also be segmented into shorter root labels.

For transliteration, an exact registered root label wins before dynamic segmentation.

The final glyph system will distinguish one lexical rune from several adjacent runes physically, removing this textual artifact.

## 13. Mana cost

Current zero-mana syntax includes:

- whitespace;
- pipe;
- period;
- mood marks;
- parentheses;
- collection punctuation;
- role markers;
- binder/reference marks;
- quotation delimiters.

Meaning-bearing registered root occurrences still cost mana.

Normalization never refunds cost.

Thus `NotNotLife This.` may normalize semantically to `Life(This)` while still charging for both written Not roots and Life.

## 14. Canonical writing style

Use the least explicit notation that has one objective parse.

Preferred:

`SolidWater This.`

`!Move This Here.`

`All [a:Human] Life $a.`

`!If Life This EndLife This.`

Pipe is available when clarity or ambiguity requires it:

`!If Life|This EndLife|This.`

Parentheses are the final explicit grouping tool.

## 15. Future rune script

The final rune writing system can map these distinctions naturally:

- physically adjacent/combined glyphs -> lexical compound;
- ordinary spacing -> normal token sequence;
- connecting stroke/attachment mark -> pipe-like hard binding;
- enclosure -> parenthesized grouping;
- small case/role marks -> `:role`.

This keeps the current transliteration useful without forcing the final writing system to resemble source code.
