# Third-party Cuspell glyph candidate comparison — Idylwild (CC0)

These are **reference candidates**, **not registered Cuspell runes**.
The canonical 150-glyph registry and its semantic assignments (currently
none) are unchanged. Do not infer that 224 + 75 is 299 non-overlapping new
Cuspell designs: the packs contain historical inspirations, variant artwork,
and some similar shapes.

## Original source archives

| Source pack | Author | Declared license | Unique indexed designs | Verified original SHA-256 |
| --- | --- | --- | ---: | --- |
| [Idylwild's Runic Codex](https://opengameart.org/content/idylwilds-runic-codex) | Idylwild | CC0 | 224 (672 PNG variants) | `1f5473b40e96fdaa980bc93993890a2f9e49d13ba0fdb6d5895bbacf5cb4cda5` |
| [Idylwild's Alchemical Codex](https://opengameart.org/content/idylwilds-alchemical-codex) | Idylwild | CC0 | 75 (225 PNG variants) | `50ffd77d022dd0a62603f105dfc1b94ccff767e126622a3105ce03dc612dc055` |

The ZIP files in `original/` are byte-for-byte copies of the **user-uploaded
original archives**, acquired through the source pages above. Their SHA-256
checksums are asserted by tests and the import workflow; a changed upstream
archive is **not** silently accepted. Please retain these original ZIPs
intact to preserve editable source assets and provenance.

## Comparison sheets

- `reviews/01_runic_vs_alchemical.png` — all 224 numbered Runic symbols
  alongside all 75 Alchemical symbols, using one icon variant per design.
- `reviews/02_runic_vs_alchemical_vs_cuspell.png` — the same collections
  alongside all 150 **current canonical** Cuspell SVG glyphs.
- `reviews/comparison_manifest.json` — validated source hashes, counts
  and which current Cuspell registry was used.

The comparison is for **visual evaluation** only; none of the external
symbols is assigned a root, replacing a current glyph, or promoted to
canonical status. Future adoption requires a separate user review and
documented source/provenance.

## Rebuild and verification

`compare_codices.py` uses Pillow and CairoSVG; it reads both ZIPs and
`../../recovery/source_geometry.json` without changing any canonical
glyph source. Reproduce it with:

```sh
python -m pip install pillow cairosvg
python assets/glyphs/references/idylwild/compare_codices.py
PYTHONPATH=src python -m unittest discover -s tests -p "test_idylwild_reference_assets.py" -v
```

GitHub workflow `.github/workflows/idylwild-comparison.yml` downloads
the two public source ZIPs, **verifies them against the user-uploaded
checksums**, performs archive tests, renders both comparisons using
the full Cuspell registry, then commits the verified ZIPs and generated
images back to `main`. Upstream download, hash, validation, or rendering
failure aborts the job rather than committing misleading outputs.

License source: the linked OpenGameArt pages, both marked CC0. These
asset packs include historical/alchemical motifs; CC0 concerns the
pack creators' artwork, not any exclusivity over an underlying motif.
