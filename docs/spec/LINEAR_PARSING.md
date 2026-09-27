# Linear Pipe-Phrase Parsing

_Status: parser algorithm specification v0.1_

This file defines how the v0.2 flat surface syntax is converted into semantic expressions.

It exists separately from SURFACE_SYNTAX so an implementation can follow a precise algorithm without rediscovering the intended parse strategy.

## 1. Input units

The lexer produces:

- semantic root tokens;
- compound-root candidates;
- pipe connectors;
- whitespace boundaries;
- sentence/mood marks;
- role markers;
- binders and variable references;
- grouping/list/quotation delimiters;
- numeric/arithmetic sugar tokens.

Whitespace is significant unless bridged by a pipe.

## 2. Phrase segmentation

Before semantic parsing, split the sentence body into maximal **pipe phrases**.

A boundary belongs to the same phrase when an explicit pipe crosses it.

Equivalent:

`Move|A|B`

`Move | A | B`

Not equivalent:

`Move|A|B C`

which becomes:

- phrase 1: Move | A | B
- phrase 2: C

Parentheses, collections, and quotations establish their own nested segmentation contexts.

## 3. Field stream

A pipe phrase is represented as an ordered field stream.

Example:

`Equal|Duration|$e|Q`

becomes:

1. Equal
2. Duration
3. $e
4. Q

The parser's job is to build exactly one semantic expression that consumes all fields.

## 4. Candidate root resolution

Each field is resolved to one or more candidate lexical/grammar entries.

Examples:

- a registered root;
- a registered compound parse;
- an Attribute descriptor;
- a role marker;
- a binder;
- an arithmetic-sugar partial operator.

If a field cannot resolve at all, parsing fails with UnknownRoot/InvalidRootSegmentation.

## 5. Recursive typed consumption

Core function conceptually:

`parse(expected_type, field_index, context) -> set of (node, next_index)`

The parser considers candidate entries whose output/result type can satisfy expected_type.

For callable entries, it:

1. selects a legal frame;
2. creates a provisional node/context;
3. consumes that frame's arguments from left to right;
4. recursively parses each argument according to its declared expected type;
5. applies role markers and contextual defaults only where the frame explicitly allows them;
6. returns the node plus the first unconsumed field.

## 6. Outermost parse

At phrase level, the first field is always treated as the outer head unless explicit grouping syntax says otherwise.

The parser considers every legal frame of that head.

A valid phrase parse must finish exactly at the end of the field stream.

No trailing pipe-bound field may be ignored.

## 7. Type-directed nesting example

Surface:

`Equal|Duration|$e|Q`

Assume:

- Equal(value,value) -> Proposition
- Duration(Event) -> Quantity<Time>
- $e : Event
- Q : Quantity<Time>

Parse:

1. Equal is outer head.
2. first Equal slot expects comparable value.
3. Duration can produce Quantity<Time>, so it becomes nested head.
4. Duration consumes $e.
5. second Equal slot consumes Q.
6. phrase ends exactly.

Result:

`Equal(Duration($e),Q)`

## 8. Descriptor versus invocation

Some lexical entries can appear either:

- as a function/Attribute to invoke;
- as a descriptor/value naming that function for another frame.

The expected slot type decides which interpretation is legal.

Example:

`Change|This|Density|Q`

Change's second slot expects AttributeDescriptor, so Density is consumed as the descriptor itself.

But:

`BeforeValue|Density|This`

BeforeValue expects a value expression, so Density must be invoked and consumes This.

This is not contextual guessing; both usages are declared typed frames.

## 9. Optional positional arguments

A callable frame can declare:

- required positional slots;
- optional positional slots;
- named-only roles.

Optional positional slots may be supplied only as a contiguous prefix.

Phrase end is a hard signal that later optional roles are omitted.

Example:

Move frame:
- theme required
- goal optional
- source optional
- path optional

Then:

`Move|A|B`

has theme=A, goal=B.

`Move|A|B|C`

has theme=A, goal=B, source=C if types fit.

If source is omitted but path is supplied, path must be role-marked.

## 10. Role markers

When the parser encounters a role marker inside a phrase:

- it must belong to the currently active callable frame;
- it changes the expected role for the next parsed expression;
- that role may not already be bound unless the frame permits repetition.

Role markers may not attach upward through an unknown number of nested calls.

If more than one active frame could legally receive the marker, explicit grouping is required.

## 11. Provisional event context

When parsing a Process/EventSpec, the parser may push a provisional event-boundary context before all result constraints have been parsed.

This allows event-local functions such as:

`BeforeValue|Density|This`

inside a Change target to resolve the omitted event parameter to the nearest uniquely enclosing EventSpec.

The context is popped when that EventSpec finishes parsing.

## 12. Variadic frames

Variadic parsing is restricted.

A variadic frame may consume remaining compatible arguments only when:

- it is the final consumer in the current phrase; or
- an explicit collection/group boundary delimits its arguments.

Canonical syntax uses collections for unbounded arity.

Example:

`And|{P1,P2,P3}`

rather than an unrestricted ambiguous flat stream.

## 13. Grouping override

Parentheses create one explicit nested expression field.

Conceptually:

`Equal|(Duration|$e)|Q`

is lexed as:

1. Equal
2. grouped-expression(Duration|$e)
3. Q

The grouped expression is parsed independently and contributes one field value to the outer phrase.

Grouping therefore overrides type-driven boundary inference.

## 14. Collections

Collection/list delimiters create explicit item boundaries.

Each item is parsed as one expression.

Example:

`Sequence|{Move|A|B,EndLife|C}`

The Sequence head consumes one Sequence/EventSpec-list value.

The comma has no semantic cost.

## 15. Space-separated phrases

After each phrase is parsed independently, the sentence grammar decides whether the resulting expression sequence is legal.

Space does not create AST nodes.

Examples:

`Move|A|B C`

parses to two expressions:

- Move(A,B)
- C

but a Command sentence expecting one EventSpec rejects the unconsumed second expression.

An explicit semantic operator must combine them if both belong to one command.

## 16. Ambiguity handling

Keep all legal full-consumption parses until normalization.

If:
- none remain -> invalid;
- exactly one semantic normal form remains -> valid;
- more than one distinct normal form remains -> AmbiguousPhrase.

Do not use:
- shortest parse;
- most common frame;
- source-language intuition;
- lexical frequency;
- "probably intended" scoring.

## 17. Error locality

Diagnostics should identify the earliest field where all candidate parses fail, plus expected types/roles where possible.

Example:

`Move|Rock|HeatValue`

could report:

- Move goal expects Location;
- HeatValue has Quantity<Thermal>;
- no alternate Move frame licenses that slot.

## 18. Cost accounting

The lexer counts written meaning-bearing root occurrences independently of the AST.

Pipe, whitespace, grouping, role markers, binders, and sentence punctuation cost zero.

Normalization/compression of the AST never changes the source rune count.

## 19. Parse complexity controls

Because typed backtracking can grow rapidly, implementations may memoize:

`(expected_type, field_index, context_signature)`

and prune candidate frames when:
- output type cannot unify;
- minimum remaining arity exceeds fields left;
- dimensions/domains are already incompatible.

Optimization must not change accepted language.

## 20. Reference implementation tests

At minimum, the parser must correctly distinguish:

`Move|A|B|C`

one phrase, one Move application with three supplied positional slots,

from:

`Move|A|B C`

two phrases.

It must also flatten uniquely typed nested structures such as:

`If|Life|This|EndLife|This`

and:

`Preserve|Volume|This|Change|This|Density|Multiply|@@|BeforeValue|Density|This`

without requiring parentheses when only one full typed parse exists.
