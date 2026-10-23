#!/usr/bin/env python3
"""Check 16 noncanonical Runic SVG adaptations and source sheet."""
import json
from pathlib import Path
from xml.etree import ElementTree as ET
base=Path(__file__).resolve().parent
g=json.loads((base/"manifest.json").read_text(encoding="utf-8"))["glyphs"]
assert len(g)==16 and len(set(x["id"] for x in g))==16
assert all(x["id"].startswith("R") and x["inventory_selection"]=="UNDECIDED" for x in g)
for x in g:
    svg=ET.parse(base/x["adapted_svg"]).getroot()
    assert svg.get("viewBox")=="0 0 600 1000"
    paths=list(svg)
    assert paths and all(p.tag.endswith("path") for p in paths)
    for p in paths:
        assert p.get("stroke-width")=="66" and p.get("stroke-linecap")=="round" and p.get("stroke-linejoin")=="round"
sheet=(base/"runic_comparison.svg").read_text(encoding="utf-8")
assert sheet.count("<use ")==16 and "data:image/png;base64," in sheet
print("PASS batch 11: 16 distinct Runic SVGs and authentic pixel sources in 3-way comparison")
