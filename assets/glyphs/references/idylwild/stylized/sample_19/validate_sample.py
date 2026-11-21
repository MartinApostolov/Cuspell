#!/usr/bin/env python3
"""Validate Batch 19 source provenance, exact copied vector shapes and comparison evidence."""
import json
from pathlib import Path
from xml.etree import ElementTree as ET

p = Path(__file__).resolve().parent
m = json.loads((p / "manifest.json").read_text(encoding="utf-8"))
rows = m["glyphs"]
assert m["batch"] == 19
assert (m["external_source_ids_covered"], m["runic_source_ids_covered"], m["alchemical_source_ids_covered"], m["remaining_external_source_ids"]) == (299, 224, 75, 0)
assert m["canonical_registry_changed"] is False and m["root_assignments_changed"] is False
assert [r["id"] for r in rows] == [f"R{n:03d}" for n in range(214, 225)]
assert len(list((p / "svgs").glob("R*.svg"))) == 11
for row in rows:
    assert int(row["id"][1:]) - int(row["alternate_ink_partner"][1:]) == 112
    current = ET.parse(p / row["candidate_svg"]).getroot()
    earlier = ET.parse(p / row["geometry_shared_from"]).getroot()
    assert current.get("viewBox") == earlier.get("viewBox") == "0 0 600 1000"
    assert ET.tostring(current) == ET.tostring(earlier), row["id"]
    assert row["style_review"] == "AWAITING_USER_REVIEW"
    assert row["final_inventory_selection"] == "UNDECIDED"
for name, count in (("runic_comparison.svg", 11), ("variant_pair_check.svg", 22)):
    raw = (p / name).read_text(encoding="utf-8")
    ET.fromstring(raw)
    assert raw.count('href="#source"') == count, name
    assert "data:image/png;base64," in raw, name
ET.parse(p / "batch19_adapted.svg")
print("PASS: Batch 19 11 source IDs, 299 total, reused approved paths, source-image comparison")
