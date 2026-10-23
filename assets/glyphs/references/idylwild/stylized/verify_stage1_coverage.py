#!/usr/bin/env python3
"""Audit the full Idylwild Stage 1 candidate source coverage, not final glyph selection.

Run from anywhere: python assets/glyphs/references/idylwild/stylized/verify_stage1_coverage.py
"""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent
GLYPH_ROOT = ROOT.parents[2]
BASE = ROOT.parent
EXPECTED = {f"R{i:03d}" for i in range(1, 225)} | {f"A{i:03d}" for i in range(1, 76)}
assert len(EXPECTED) == 299

records = {}
manifest_ids = []
for batch in range(1, 20):
    folder = ROOT / f"sample_{batch:02d}"
    manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    items = next((manifest[k] for k in ("glyphs", "samples", "candidates", "decisions")
                  if isinstance(manifest.get(k), list)), None)
    assert items is not None, f"Missing candidate entries in batch {batch}"
    assert len(items) == (11 if batch == 19 else 16), (batch, len(items))
    expected_files = set()
    for item in items:
        source_id = item["id"]
        manifest_ids.append(source_id)
        assert source_id not in records, f"Repeated source ID: {source_id}"
        records[source_id] = item
        candidate = next((item[k] for k in ("candidate_svg", "svg", "vector", "adapted_svg",
                              "new_vector", "stylized_vector") if item.get(k)), None)
        assert candidate == f"svgs/{source_id}.svg", (batch, source_id, candidate)
        candidate_path = folder / candidate
        assert candidate_path.is_file(), f"Missing vector file: {candidate_path}"
        svg = ET.parse(candidate_path).getroot()
        assert svg.get("viewBox") == "0 0 600 1000", source_id
        expected_files.add(candidate_path.name)
        style_state = item.get("style_review") or item.get("style_approval")
        assert style_state in ("APPROVED", "APPROVED_REVISED"), (source_id, style_state)
        final_state = item.get("final_inventory_selection")
        # Early manifests also use decision/selection for pending final inventory votes.
        assert final_state not in ("KEEP", "ADOPTED", "REPLACED"), (source_id, final_state)
    on_disk = {p.name for p in (folder / "svgs").glob("*.svg")}
    assert expected_files == on_disk, (batch, expected_files - on_disk, on_disk - expected_files)

counts = Counter(manifest_ids)
assert set(counts) == EXPECTED, {
    "missing": sorted(EXPECTED - set(counts)),
    "unexpected": sorted(set(counts) - EXPECTED),
}
assert all(n == 1 for n in counts.values())
actual_svg_count = len(list(ROOT.glob("sample_*/svgs/*.svg")))
assert actual_svg_count == 299, actual_svg_count

# All 112 later Runic source IDs are recorded as alternate-source partners
# of earlier IDs. This is provenance, not a final shape-deduplication decision.
for i in range(113, 225):
    item = records[f"R{i:03d}"]
    partner = (item.get("alternate_ink_partner")
               or item.get("alternate_rendering_of")
               or item.get("apparent_artwork_variant_of")
               or item.get("likely_source_variant"))
    assert partner == f"R{i-112:03d}", (i, partner)

# The source archives are never replaced by derived/processed assets.
originals = BASE / "original"
known_archive_sha256 = {
    "idylwilds_runic_codex.zip": "1f5473b40e96fdaa980bc93993890a2f9e49d13ba0fdb6d5895bbacf5cb4cda5",
    "idylwilds_alchemical_codex.zip": "50ffd77d022dd0a62603f105dfc1b94ccff767e126622a3105ce03dc612dc055",
}
for filename, expected_hash in known_archive_sha256.items():
    path = originals / filename
    assert path.is_file(), path
    assert sha256(path.read_bytes()).hexdigest() == expected_hash, filename

# The 150 pre-existing canonical Cuspell glyphs are separate from the candidates.
canonical = GLYPH_ROOT / "recovery" / "generated" / "glyphs"
assert {p.name for p in canonical.glob("G*.svg")} == {
    f"G{i:03d}.svg" for i in range(1, 151)
}

print("PASS Stage 1: 19 batches, all R001–R224 and A001–A075 exactly once")
print("PASS: 299 editable SVGs, 112 Runic later-source partner links")
print("PASS: original Idylwild archive SHA-256 checks and 150 canonical G glyph files")
print("NOTE: no claim of 299 unique external glyphs or final inventory adoption")
