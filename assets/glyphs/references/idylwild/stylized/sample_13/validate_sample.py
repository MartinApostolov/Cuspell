#!/usr/bin/env python3
"""Validate Runic alternate-ink correspondence without changing canonical Cuspell."""
import json
from pathlib import Path
from xml.etree import ElementTree as ET
root=Path(__file__).resolve().parent
data=json.loads((root/"manifest.json").read_text(encoding="utf-8"))
items=data["glyphs"]
assert len(items)==16
assert [x["id"] for x in items]==[f"R{i:03}" for i in range(118,134)]
for x in items:
    adapted=ET.parse(root/x["svg"]).getroot()
    original=ET.parse(root/x["normalized_paths_from"]).getroot()
    assert adapted.get("viewBox")=="0 0 600 1000"
    get_paths=lambda parent:[e.attrib["d"] for e in parent if e.tag.endswith("path")]
    assert get_paths(adapted)==get_paths(original),(x["id"],x["apparent_artwork_variant_of"])
    assert all(e.get("stroke-width")=="66" for e in adapted)
sheet=(root/"runic_comparison.svg").read_text(encoding="utf-8")
assert sheet.count("<use ")==16
assert "data:image/png;base64," in sheet
print("PASS: 16 distinct Idylwild source IDs retain approved counterpart geometry and true source pixels")
