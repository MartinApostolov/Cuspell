# Canonical Player Writing Rules

These are the rules a player is expected to treat as current Cuspell.

## 1. Sentence mood is final

- `.` — assertion
- `?` — question
- `!` — command

The same mark ends the sentence.

## 2. Normal Cuspell is flat

Whitespace separates larger units. It carries no meaning by itself.

## 3. Heads come before their arguments

`Move This Here!`

A Relation, Process, Operator, or other head is written first; its arguments follow.

## 4. Types and frame order determine attachment

Arguments are consumed left to right according to the head's registered frame. The language does not choose a reading because it sounds more plausible.

## 5. Tight adjacency makes a local unit

Exact roots are recognized first, then licensed compounds, then one uniquely typed tight local application.

Examples: `LifeThis`, `DensityThis`, `EndLifeThis`.

## 6. A complete sentence must have one meaning

Every written unit must be consumed. Several parses are acceptable only when they normalize to the same semantic meaning. Distinct surviving meanings make the writing ambiguous and invalid.

## 7. Omission never means "guess"

Required roles must be present. Optional roles may be left unspecified, but the language does not silently fill them from presumed intent.

## Common reusable constructions

**And / Or** use spoken order:

`LifeThis And MagicThis.`

`LifeThis Or MagicThis.`

A same-operator chain stays flat. Mixed bare And/Or must make its grouping explicit.

**Sequence / Concurrent** take flat event lists:

`Sequence MoveSelfHere MoveSelfThere!`

`Concurrent MoveSelfHere MoveYouThere!`

Sentence end closes the list. When later sentence material must follow, use the matching zero-mana grammatical closer:

`Permitted You Sequence MoveYouHere MoveYouThere SequenceEnd Self.`

`SequenceEnd` and `ConcurrentEnd` are part of canonical flat Cuspell.

For the less common constructions, see [ADVANCED_GRAMMAR.md](ADVANCED_GRAMMAR.md).
