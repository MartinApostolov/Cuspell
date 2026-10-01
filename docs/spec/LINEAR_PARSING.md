# Typed Linear Parsing

_Status: current parser algorithm for surface syntax v0.7_

This file specifies how canonical flat Cuspell becomes a semantic AST. Historical surface algorithms are archived under `archive/syntax/`.

## 1. Lexical stage

After sentence mood/termination is identified, the surface lexer recognizes:

- exact registered roots;
- licensed lexical compounds;
- concatenated registered-root tokens eligible for tight typed application;
- whitespace;
- role markers;
- binders/variable references;
- collection delimiters;
- quotation;
- SequenceEnd / ConcurrentEnd;
- parentheses and pipe fallback grouping;
- number notation.

Quoted Sign content is protected from ordinary surface parsing.

## 2. Outer token stream

Top-level whitespace separates ordinary written units while respecting quotation, parentheses, collections, and legacy compatibility forms.

Example:

`If LifeThis EndLifeThis`

becomes:

1. If
2. LifeThis
3. EndLifeThis

Whitespace contributes no semantic relation.

## 3. Core typed parser

Conceptually:

`parse(expected_type, token_index, context) -> set(node, next_index)`

For each compatible candidate:

1. identify the lexical entry/compound/tight expression;
2. select a registered typed frame;
3. recursively consume required arguments;
4. consider legal optional positional arguments;
5. process named roles;
6. propagate binder/event/discourse context;
7. compute the output type;
8. return the node plus next unread position.

Parsing keeps all legal candidates until full-consumption normalization determines whether the meaning is unique.

## 4. Ordinary nested application

`If LifeThis EndLifeThis!`

The command expects an EventSpec.

- If may produce EventSpec;
- its condition expects Proposition;
- LifeThis satisfies that slot;
- its consequent expects EventSpec;
- EndLifeThis satisfies that slot.

One complete typed tree consumes the sentence.

## 5. Tight adjacent application

If a token is not already an exact root or licensed compound, it may be segmented into registered roots and parsed as a private typed stream.

Examples:

`MatterSelf` -> Matter(Self)

`DensityThis` -> Density(This)

`NotLifeThis` -> Not(Life(This))

Resolution priority:

1. exact registered root;
2. licensed lexical compound;
3. uniquely typed tight application.

The tight token must consume every segmented root and produce one semantic normal form of the type expected by its outer position.

## 6. Descriptor versus invocation

Some entries can be used as a descriptor or invoked as a function depending on the slot type.

Example:

`Change This Density Q`

The Change frame expects an AttributeDescriptor, so Density is consumed as the descriptor.

In:

`BeforeValue Density This`

the value position causes Density to invoke its functional frame on This.

This is registered typing, not plausibility guessing.

## 7. Optional positional roles

Optional positional arguments form a contiguous prefix unless a named role explicitly skips ahead.

For Move:

1. theme required;
2. goal optional;
3. source optional;
4. path optional.

`Move A B C` binds theme=A, goal=B, source=C when types fit.

Skipping goal while supplying path requires:

`Move A :path P`

## 8. Named-role ownership

A role marker belongs to an active frame that declares that role.

If nested active frames could both accept the same role and typing cannot distinguish ownership, the expression is ambiguous and must be rewritten/grouped.

## 9. Sequence / Concurrent flat groups

When the parser encounters `Sequence` or `Concurrent` in an EventSpec position, it consumes a flat series of EventSpecs.

The group closes when:

- sentence/end-of-expression boundary is reached; or
- the matching `SequenceEnd` / `ConcurrentEnd` marker appears.

The explicit End marker contributes no semantic AST node and costs no mana.

A mismatched or free End marker is a syntax error.

## 10. And / Or infix parsing

Canonical `A And B` and `A Or B` are parsed as type-compatible infix conjunction/disjunction.

Same-operator chains flatten to one semantic structure.

Mixed bare And/Or is rejected unless grouping states the scope.

## 11. Collections

A collection token `{...}` is parsed as a semantic Collection value.

Each comma-separated member must independently form a complete expression compatible with the collection member type.

Collections are not used merely to make canonical And/Or or Sequence/Concurrent visible.

## 12. Binders and variables

Canonical binder token:

`name:Domain`

Variable reference:

`$name`

A binder extends parsing context for the scope in which its variable is valid.

Open-question binders may appear before the query expression so their variables are available while the question body is parsed.

Legacy bracketed binder syntax may remain compatibility-only.

## 13. Event-local context

Entering an EventSpec frame may establish a provisional enclosing-event context before all arguments finish parsing.

This supports shorthand such as:

`Change This Density Multiply @@ BeforeValue Density This`

where BeforeValue may refer to the uniquely enclosing Change event.

## 14. Quotation and Old Names

`«... »` first yields an exact Sign.

If the exact Sign is a registered Old Name, it may additionally yield the Old Name's declared typed semantic reading.

Unit-valued Old Names may head a quantity construction such as:

`«LengthUnit» @@`

New Names never expand as magical semantic macros.

## 15. Explicit grouping fallback

Parentheses parse an enclosed spaced expression independently.

Pipe hard-binding parses a connected group independently and prevents outer tokens from being borrowed into that group.

Example:

`Move|This|Here!`

is equivalent to the flat form when unambiguous.

Pipe/parentheses remain fallback/debug mechanisms rather than the canonical prose style.

## 16. Full-consumption rule

At sentence and explicit-group boundaries, no token may remain unread.

This prevents whitespace from silently becoming And/Sequence and prevents hard groups from leaking arguments.

## 17. Ambiguity rule

After semantic normalization:

- no full candidate -> invalid;
- one distinct normal form -> valid;
- several candidates with the same normal form -> valid;
- several different normal forms -> AmbiguousPhrase.

Do not use scoring or natural-language plausibility to break ties.

## 18. Diagnostics

Diagnostics should preserve source spans and prefer the furthest meaningful parse failure.

Important classes include:

- UnknownRoot;
- IllegalCompound;
- TypeMismatch;
- DimensionMismatch;
- ValueDomainMismatch;
- MissingRequiredRole;
- InvalidRole;
- FreeVariable;
- SemanticallyIncomplete;
- AmbiguousTightGroup / AmbiguousPhrase;
- contradictory constraint failures.

## 19. Mana accounting

Written semantic cost is counted from meaning-bearing signs before AST normalization.

Zero-mana grammar includes whitespace, sentence punctuation, role/binder marks, collection punctuation, SequenceEnd/ConcurrentEnd, quotation delimiters, and fallback grouping marks.

## 20. Complexity control

Typed backtracking may be memoized by expected type, token index, and context signature.

Pruning may use output types, arity bounds, dimensions, domains, and frame constraints, but optimization must never change the accepted language.

## 21. Reference examples

Canonical:

`Move This Here!`

`If LifeThis EndLifeThis!`

`More Evaluate MatterSelf Evaluate ThingSelf.`

`Sequence MoveSelfHere MoveSelfThere!`

`Permitted You Sequence MoveYouHere MoveYouThere SequenceEnd :authority Self.`

`g:Location At This $g?`

Fallback/debug equivalence:

`Move|This|Here!`

`If Life|This EndLife|This!`

Historical surface behavior belongs in compatibility tests and `archive/`, not in the canonical algorithm description.
