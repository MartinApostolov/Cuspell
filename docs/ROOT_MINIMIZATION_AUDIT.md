# Core Root Minimization Audit

_Status: pass 2 — reduction-first cleanup_

## Goal

Cuspell accumulated executable entries while closing corpus gaps. That was useful for discovering semantic distinctions, but it should not be mistaken for a final primitive-root inventory.

The current cleanup rule is now:

> A standalone core root must earn its place. If the same meaning can be expressed exactly and reasonably through existing composition, prefer composition.

This audit distinguishes:

- **primitive/root-worthy semantics**;
- **derived meanings that should be written compositionally**;
- **roots currently embedded inside draft Old Names, which may be redesigned during cleanup**;
- **temporary direct noun roots that should eventually migrate into the naming system**;
- **convenience vocabulary that may remain only if corpus readability justifies it**.

## Pass 1 result

The executable core had **306 entries** before this audit.

Pass 1 removes **11 exact-redundancy entries**, leaving **295**.

These removed forms do not carry unique semantics:

| Removed root | Canonical composition |
| --- | --- |
| After A B | Before B A |
| Less A B | More B A |
| AtLeast A B | More A B Or Equal A B |
| AtMost A B | More B A Or Equal A B |
| EvidenceAgainst I P | EvidenceFor I Not P |
| NotDetected E S | Not Detected E S |
| Never P I | Always Not P I |
| False | Not True |
| Claim S P | Assert S P |
| Lose A B | EndHave A B |
| Destroy X | EndExist X |

The corresponding standalone roots are removed rather than retained as aliases, because retaining aliases would not actually reduce the rune/root inventory.

### Inside/Outside correction

The first pass initially treated Inside as In and Outside as Not In. The detailed spatial specification disproved that simplification:

- In allows boundary contact;
- Inside requires strict interior placement without boundary contact;
- Not In merely says full containment fails;
- Outside requires no extent in the region interior.

Because the current geometry layer cannot reproduce those stricter predicates compositionally, Inside and Outside remain primitive Relations for now.

## Old Names do not block reduction during the design phase

Pass 2 demonstrates this rule in practice. Contain, Join, Separate, Get, Tell, See, Hear, Smell, and other roots were removed even though draft Old Names used them; the affected names were rebuilt from the surviving language.

Remaining descriptive roots such as `Big`, `Small`, `Long`, `Injured` and others are still open to reduction if a smaller general mechanism can preserve their meanings.

Draft Old Names are **not protected compatibility surfaces**. When a root is removed, rebuild the affected names as needed. During language design, their spellings, etymologies, nesting, and mana costs are allowed to change.

The historical freeze rule applies only after the language/history reaches an explicit freeze point.

## Pass 2 result

Pass 2 removes **11 additional compositional entries**, leaving **284** executable core entries.

| Removed root | Canonical composition |
| --- | --- |
| Contain R X | In X R |
| Get A B | BeginHave A B |
| Join A B | BeginJoined A B |
| Separate A B | EndJoined A B |
| Tell S I A | Say S I A |
| See E X | Sense E Vision X |
| Hear E X | Sense E Hearing X |
| Smell E X | Sense E Olfaction X |
| Taste E X | Sense E Gustation X |
| ChangeBy X Attr D | Change X Attr Add BeforeValue Attr X D |
| Converse Relation | write Relation directly with the intended role/argument order |

This means the corrected first two passes reduce the core from **306 to 284**, a reduction of **22 registered entries** without deleting a semantic distinction.

Affected draft Old Names were rebuilt from the surviving language. Some became longer and more expensive; that is acceptable during language design because the goal is a cleaner primitive system rather than preserving provisional compression.

## Tier 3 — candidates requiring real design work

These are not removed in the first two passes, but should be challenged next.

### Generalized state-boundary vocabulary

The exact wrappers Get, Join, and Separate are now removed.

Remaining candidates such as some readings of Learn would require proving that no extra acquisition/process meaning is lost before replacing them with BeginUnderstand / BeginKnow.

### Selection operators

Potentially reducible to a smaller generic extrema/ordering system:

- Nearest
- Farthest
- Highest
- Lowest

A good reduction would add **fewer** general mechanisms than the number of special selectors removed.

### Change helpers

ChangeBy is now removed in favor of Change + Add + BeforeValue.

Remaining candidates:

- Redistribute as an explicit change to DistributionOf;
- Increasing / Decreasing / Stable through a more general rate/change comparison system.

These still need exact type-preserving recipes before deletion.

### Modal/probability convenience

Potential family:

- PossibleTo
- ProbableTo
- CertainTo

They may be representable as one graded confidence/probability construction plus thresholds, but only if that semantics is made explicit. Do not collapse them merely because English treats them as related words.

### Frequency convenience

Potential family:

- Sometimes
- Often
- Rarely
- Always

OccurrenceRate already exists, but contextual frequency terms are not automatically identical to numeric thresholds. Reduction needs a principled contextual-standard model.

### Social/cognitive convenience

The recent cross-genre pass added useful distinctions, but some processes may still be compositional:

- Learn
- Teach
- Thank
- Apologize
- Deceive

These should be tested for readability and truth-condition preservation before keeping them as primitive roots.

## Temporary direct noun roots

The current core still contains direct noun-like roots that the naming architecture already treats as temporary:

- Cat
- Hand
- Human
- Water

These should eventually be migrated into world concepts + historically plausible Old Names if the historical vocabulary supports that move.

They should not be counted as permanent evidence that every common noun needs a primitive rune.

## Families that should not be collapsed casually

Reduction must preserve real semantic distinctions.

Examples already proven important:

- Same vs Equal
- If vs Counterfactual
- Intend vs Attempt
- Property vs Attribute
- Not vs Opposite
- Zero vs Not
- Life vs Exist
- Can vs epistemic possibility
- Old Name vs New Name

The goal is **fewer primitives**, not fewer meanings.

## Pass-2 method

For every candidate root:

1. write an exact compositional replacement;
2. verify that its truth conditions are identical;
3. verify parser/type correctness;
4. translate representative corpus examples both ways;
5. identify affected Old Names and redesign them if the root is removed;
6. compare rune cost/readability;
7. remove the root only if the composition remains clear enough.

This process should continue family by family rather than deleting dozens of roots merely because they look similar.

## Design-stage rule

The current Old Name inventory is provisional. Do not retain a primitive root merely to avoid editing an Old Name. Root minimization takes precedence; historical vocabulary is rebuilt afterward from the surviving language.
