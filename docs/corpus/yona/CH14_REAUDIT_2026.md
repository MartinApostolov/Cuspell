# Yona Chapter 14 — Current-Language Re-audit

_Status: 2026-09-27 re-audit against executable Cuspell main (202-test checkpoint)_

_Source: Yona [Cat Girl Evolution], Bedivere the Mad, Chapter 14 "External Mana Manipulation"_
_Source URL: https://www.royalroad.com/fiction/129180/yona-cat-girl-evolution/chapter/2540191/14-external-mana-manipulation_

The original CH14_MAGIC_PASS deliberately targeted mana manipulation, shaped constructs, body-like structures, measurements, perception, and skill progression. Several of the important gaps it exposed have since been implemented.

## Former Chapter 14 defects now resolved

### Relative pre-state values — RESOLVED / EXECUTABLE

The old M10 problem ("twice the previous density") is now directly represented with BeforeValue plus dimensional arithmetic.

Executable regression already exists for the semantic shape:

Change This Density Multiply @@ BeforeValue Density This

BeforeValue/AfterValue also have event-local shorthand inside an enclosing EventSpec.

### Preserve an invariant during a change — RESOLVED / EXECUTABLE

The old M09 problem ("increase density while keeping size/volume fixed") is now represented by Preserve wrapping the Change EventSpec.

Executable corpus regression exists for:

Preserve Volume This Change This Density Multiply @@ BeforeValue Density This

### Approximate measured equality — PARTLY RESOLVED

ApproxEqual now exists as a typed relation and requires an explicit tolerance. This is correct for objective/magical use.

The prose phrase corresponding to M11 ("almost ten times the initial density") can therefore be translated exactly if the intended tolerance is supplied or contextually fixed. Ordinary-language "almost" without an explicit scale still remains a broader discourse/threshold issue.

### Shape resemblance versus actual Kind identity — RESOLVED / EXECUTABLE

M14/M15 are now supported by the explicit distinction between ShapeLike and Kind predication. A hand-shaped mana construct does not become a biological Hand merely because its form resembles one.

This distinction has permanent executable regression coverage.

### Touch versus structural connection — RESOLVED / EXECUTABLE

M17 is directly represented by separate Touch and Joined relations and has executable regression coverage.

### Control as a separate state relation — RESOLVED / EXECUTABLE

Control(controller,target) now exists independently of location, contact, possession, or joining.

### Dimensional quantity arithmetic — RESOLVED / EXECUTABLE

The chapter's density comparisons and multiplicative changes now sit on a real dimension system:

- Add requires matching dimensions;
- Multiply/Divide combine dimensions;
- Power/Root transform dimension vectors;
- registered Units normalize to canonical scale;
- incompatible quantities produce DimensionMismatch.

This is much stronger than the system available during the original Chapter 14 pass.

## Remaining Chapter 14 gaps

### 1. Spatial resource fields / distributions — REAL SEMANTIC GAP

M02, M12, and part of M21 still expose a genuine missing abstraction.

The story treats mana not only as a scalar reserve but as something distributed over space:

- mana inside versus outside a body;
- density varying across a construct;
- center depleted while edges are denser;
- ambient mana density varying by Region/material.

Cuspell currently has scalar quantities, regions, location relations, and Density, but no generic field/distribution value such as:

Field(resource, region) -> spatially varying Quantity
or
Distribution(resource, entity/region) -> field

This is probably the most important remaining Chapter 14 architecture gap.

### 2. Resource transfer / flow — SEMANTIC MOLECULE / LEXICON

M02 and M22 repeatedly move a resource from one container/location to another.

Current Change/Have/Move semantics can describe pieces of this, but a reusable Transfer/Flow process would be substantially cleaner:

Transfer(resource, amount, source, destination)

This looks like a useful semantic molecule rather than a new foundational grammar mechanism.

### 3. Rate/trend values — REAL GRAMMAR GAP

M23 says mana digestion/conversion becomes more efficient over time.

The written measurement spec already anticipates Rate/Increasing/Decreasing, but they are not executable yet. This is the same rate/trend gap found in Chapter 1.

### 4. Sensory capability channels — LEXICON / WORLD

M01/M21/M24 rely heavily on sensing mana as a dedicated channel.

The Information architecture can carry the result, and Can can represent capability, but a generic Sense/Perception family is not yet executable.

### 5. Anatomy and structure vocabulary — LEXICON / WORLD

M05-M07, M13, M16 need ordinary structural vocabulary:

- finger/digit;
- joint;
- segment;
- hollow/interior/boundary;
- anatomical part relations;
- geometry descriptors.

The current Hand Kind plus ShapeLike/Joined/Part-like semantics are enough architecturally; the missing material is mostly vocabulary/ontology.

### 6. Skill/proficiency progression — WORLD MODEL

M24/M25 describe training changing a capability from active/effortful to passive and changing proficiency categories.

That is not a core Cuspell grammar problem. It belongs in a world/system package describing Skills, proficiency, unlock conditions, and capability changes.

## Chapter 14 conclusion

The old magic-heavy pass has improved markedly.

The two most important language-level gaps remaining from this chapter are:

1. **spatial fields/distributions**;
2. **generic rate/trend semantics**.

Resource Transfer/Flow and Sense are useful reusable semantic molecules. Anatomy and proficiency are primarily lexicon/world-package work.

The major earlier defects around relative values, preserving invariants, typed density arithmetic, resemblance versus identity, contact versus joining, and control have been resolved and regression-tested.
