#!/usr/bin/env python3
"""Verify source variant identifiers, reused vectors and true-source comparison."""
import json
from pathlib import Path
from xml.etree import ElementTree as ET
p = Path(__file__).resolve().parent
m = json.loads((p/"manifest.json").read_text())
assert m["batch"] == 18 and m["external_source_ids_covered"] == 288
assert m["remaining_external_source_ids"] == 11 and m["canonical_registry_changed"] is False
assert [r["id"] for r in m["glyphs"]] == [f"R{i:03}" for i in range(198,214)]
for row in m["glyphs"]:
    assert int(row["id"][1:]) - int(row["alternate_ink_partner"][1:]) == 112
    a = ET.parse(p/row["candidate_svg"]).getroot()
    b = ET.parse(p/row["geometry_shared_from"]).getroot()
    assert a.get("viewBox") == b.get("viewBox") == "0 0 600 1000"
    assert ET.tostring(a) == ET.tostring(b),row["id"]
    assert row["style_review"] == "AWAITING_USER_REVIEW"
for name, count in (("runic_comparison.svg",16),("variant_pair_check.svg",32)):
    content = (p/name).read_text()
    ET.fromstring(content)
    assert content.count('href="#source"') == count
    assert "data:image/png;base64," in content
ET.parse(p/"batch18_adapted.svg")
print("PASS: 16 Runic alternate source IDs, 16 reused vectors and real-source sheets")
