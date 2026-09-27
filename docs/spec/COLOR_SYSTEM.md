# Color System

_Status: working specification v0.1_

Cuspell keeps the existing RGB-like basis while separating chromatic proportion from visible intensity.

## Core representation

A `ColorProfile` contains:

- Red/Green/Blue channel proportions;
- total visible Light intensity.

Balanced RGB alone therefore does not determine a brightness/lightness class.

## Channel roots

Registered roots:

- Red
- Green
- Blue

They form a commutative/associative blend family.

Unweighted adjacency means equal included proportions:

- `RedGreen` = 1:1
- `GreenBlue` = 1:1
- `RedBlue` = 1:1
- `RedGreenBlue` = 1:1:1

Intensity remains separate.

Repeated identical channel roots do not encode weighting.

## Weighted chroma

Use Ratio with explicit key/value associations.

Temporary syntax:

`Ratio|{Red:@@@,Green:@@@@@}`

means Red:Green = 3:5.

The braces, commas, and association colon are zero-mana structural syntax. Ratio, channel roots, and numeric runes are meaning-bearing.

Common scaling normalizes, so 3:5 and 6:10 denote the same chromatic proportion.

## Exact profile construction

Use a provisional profile constructor:

`ColorValue|(Ratio|{Red:@@@,Green:@@@@@})|:light|Q`

where Q is a typed visible-Light quantity.

The final rune name for the constructor can be improved during glyph/lexicon polish.

## Color attribute

Use:

`ColorOf(subject) -> ColorProfile`

as the functional Attribute for exact comparison/change.

Thus Change can set ColorOf to a complete profile.

For compact Kind/property restriction, Red/Green/Blue still provide registered chromatic predicates, so `RedMatter` remains valid.

## Conventional derived colors

Registered semantic molecules can include:

- Yellow = RedGreen chroma
- Cyan = GreenBlue chroma
- Magenta = RedBlue chroma

Balanced RGB at high registered intensity can produce the conventional bright neutral profile; balanced lower intensity produces neutral gray profiles.

Exact zero visible Light corresponds to the zero-intensity dark profile; `ZeroLight` expresses that exact condition.

## Optics

The base game model may treat ColorOf as standardized visible appearance.

A detailed physics module can split emission, reflectance, transmittance, and illumination while deriving ColorOf from them.

Transparency/Transmittance and Reflectance remain separate optical Attributes.

Visibility is observer-sensitive and is handled by VisibleTo or the underlying optical interaction model; changing Color alone does not automatically create invisibility.

## Result

The color system now supports:

- equal-channel compounds;
- weighted ratios;
- separate visible intensity;
- exact structured profile values;
- a functional ColorOf Attribute.

This closes the weighted-color syntax gap without reusing structural Part.
