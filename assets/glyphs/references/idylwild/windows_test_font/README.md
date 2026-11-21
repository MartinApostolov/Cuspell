# Cuspell Compact WinTest — Windows rendering diagnosis

This is a separately named compatibility experiment. Do not replace or uninstall the existing Cuspell Compact font yet.

1. Install **CuspellCompactWinTest-Regular.ttf** as a new Windows font.
2. In VS Code set `editor.fontFamily` to `"'Cuspell Compact WinTest', Consolas, monospace"`.
3. Open the included offline `meaning_keyboard.html`, convert `Create :«This» At $«This» There Change $«This» Light «LightUnit» @!` and paste the glyph output in VS Code.
4. Also choose **Cuspell Compact WinTest** explicitly in Notepad. If both apps render runes, Windows font selection was the problem.

Spacing, all 234 PUA outlines and 13 approved punctuation are unchanged. The only new characters are display-only basic Latin fallback glyphs from DejaVu Sans Mono, under the included license. This adds no Cuspell meanings.
