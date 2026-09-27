# Typed Linear Parsing

_Status: parser algorithm specification v0.2 for surface syntax v0.3_

This file specifies how ordinary whitespace tokens and explicit pipe binding become a semantic AST.

## 1. Lexical stage

After mood and sentence termination are removed, the surface lexer recognizes:

- registered root/compound tokens;
- whitespace;
- pipe connectors;
- parentheses;
- collections and commas;
- binders/references;
- role markers;
- quotation delimiters;
- numeric notation.

Whitespace around `|` is normalized away.

## 2. Top-level token stream

Top-level whitespace splits the sentence into ordinary tokens while respecting parentheses, collections, binders, and quotation.

Example:

`If Life This EndLife This`

becomes:

1. If
2. Life
3. This
4. EndLife
5. This

A token containing pipe is instead a hard-bound group:

`If Life|This EndLife|This`

becomes three outer tokens:

1. If
2. hard-group(Life, This)
3. hard-group(EndLife, This)

## 3. Core parser

Conceptually:

`parse(expected_type, token_index, context) -> set(node, next_index)`

For each candidate lexical entry whose output can satisfy the expected type:

1. select a registered frame;
2. recursively consume required arguments;
3. consider legal optional positional prefixes;
4. process role-marked arguments;
5. compute the result type;
6. return the resulting AST node and next unread token.

Parsing keeps every legal candidate until full-consumption normalization decides whether the sentence is unique.

## 4. Ordinary nested application

Surface:

`If Life This EndLife This`

In command mood the outer expected type is EventSpec.

- If can produce EventSpec when its consequent does.
- its condition expects Proposition;
- Life can produce Proposition by consuming This;
- its consequent expects EventSpec;
- EndLife can produce EventSpec by consuming This.

The full token stream therefore produces one typed tree.

## 5. Pipe group

When a token contains pipe, split that token into pipe fields and parse those fields as a private token stream.

The group must:

- have one complete parse of the type expected by its outer slot;
- consume every pipe field;
- not borrow later outer tokens.

Thus:

`Move|A|B C`

offers the outer parser:

1. one already-complete Move(A,B) expression;
2. C.

If no outer frame consumes both, the sentence fails full consumption.

## 6. Parenthesized group

A parenthesized region is likewise parsed independently as one expression and contributes one value to the surrounding stream.

Unlike pipe, parentheses may enclose whitespace directly.

## 7. Descriptor versus invocation

Some roots can denote a function/Attribute descriptor or invoke that function depending on the expected slot type.

Example:

`Change This Density Q`

Change's attribute slot expects AttributeDescriptor, so Density is consumed as the descriptor.

In:

`BeforeValue Density This`

BeforeValue expects a value, so Density invokes its functional frame and consumes This.

This is registered typed behavior, not guessing.

## 8. Optional positional roles

Optional positional arguments form a contiguous prefix.

For the working Move frame:

1. theme required;
2. goal optional;
3. source optional;
4. path optional.

Therefore:

`Move A B C`

binds theme=A, goal=B, source=C when the types fit.

Skipping goal but supplying path requires a role marker:

`Move A :path P`.

## 9. Role-marker ownership

A role marker belongs to the active frame that uniquely declares the role.

If nested active frames could both legally receive the same marker and typing cannot distinguish them, the expression is ambiguous and must use pipe or parentheses to establish the intended boundary.

## 10. Collections

A collection is one outer token whose comma-separated items are independently parsed complete expressions.

`Sequence {Move This Here,EndLife Self}`

therefore gives Sequence one Collection<EventSpec>.

## 11. Event-local context

When a Process/EventSpec frame begins parsing, it may push a provisional event context before all target/result expressions are consumed.

This supports event-local shorthand such as:

`Change This Density Multiply @@ BeforeValue Density This`

where BeforeValue can resolve its omitted Event argument to the uniquely enclosing Change EventSpec.

## 12. Full-consumption rule

At sentence and explicit-group boundaries, no token may remain unread.

This prevents whitespace from silently meaning And/Sequence and prevents pipe groups from leaking arguments across their boundary.

## 13. Ambiguity rule

After normalizing candidate ASTs:

- no full candidate -> invalid;
- one distinct normal form -> valid;
- several candidates with one identical normal form -> valid;
- several different normal forms -> AmbiguousPhrase.

Do not use parse scoring or natural-language intuition to break ties.

## 14. Diagnostics

Diagnostics should report the furthest point where candidate parses fail and, where possible:

- expected type;
- actual type;
- illegal compound;
- unknown root;
- free variable;
- invalid/missing role;
- ambiguous hard group;
- unconsumed-token/full-consumption failure.

## 15. Cost accounting

Mana is counted from written semantic root occurrences before AST normalization.

Whitespace, pipe, grouping punctuation, role markers, binders, and sentence punctuation are free grammar.

## 16. Complexity control

Typed backtracking can be memoized by a key such as:

`(expected_type, token_index, context_signature)`.

Pruning may use impossible output types, arity bounds, dimensions, and domains, but optimization must not alter the accepted language.

## 17. Reference tests

The implementation must distinguish all of these:

`Move This Here.`

normal inferred application.

`Move|This|Here.`

equivalent explicit hard binding.

`Move|This Here.`

hard group Move(This) plus outer Here; not equivalent to Move(This,Here).

`If Life This EndLife This.`

nested inference using ordinary spaces.

`If Life|This EndLife|This.`

same semantic result with explicit inner groups.
