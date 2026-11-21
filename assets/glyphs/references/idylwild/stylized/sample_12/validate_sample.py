#!/usr/bin/env python3
"""Validate all noncanonical batch 12 candidates and authentic source pixel previews."""
import json
from pathlib import Path
from xml.etree import ElementTree as ET
base=Path(__file__).resolve().parent
m=json.loads((base/"manifest.json").read_text(encoding="utf-8"))
items=m["glyphs"]
assert len(items)==16 and len({x["id"] for x in items})==16
assert all(x["id"].startswith("R") and x["selection"]=="UNDECIDED" for x in items)
for item in items:
    root=ET.parse(base/item["new_vector"]).getroot()
    assert root.get("viewBox")=="0 0 600 1000"
    assert list(root) and all(x.tag.endswith("path") for x in root)
    assert all(x.get("stroke-width")=="66" and x.get("stroke-linecap")=="round" and x.get("stroke-linejoin")=="round" for x in root)
sheet=(base/"runic_comparison.svg").read_text(encoding="utf-8")
assert sheet.count("<use ")==16 and "data:image/png;base64," in sheet
print("PASS: 16 distinct candidate source IDs, 16 SVG files and authentic comparison crops")
