#!/usr/bin/env python3
"""Validate batch 08 stylized candidate assets and comparison sheets."""
import json
from pathlib import Path
from xml.etree import ElementTree as ET
b=Path(__file__).resolve().parent
items=json.loads((b/"manifest.json").read_text(encoding="utf-8"))["glyphs"]
assert len(items)==16 and len({x["id"] for x in items})==16
assert sum(x["id"].startswith("R") for x in items)==8
assert sum(x["id"].startswith("A") for x in items)==8
for x in items:
    svg=ET.parse(b/x["svg"]).getroot()
    assert svg.get("viewBox")=="0 0 600 1000"
    paths=list(svg)
    assert paths and all(p.tag.endswith("path") for p in paths)
    assert all(p.get("stroke-width")=="66" and p.get("stroke-linecap")=="round" and p.get("stroke-linejoin")=="round" for p in paths)
for sheet in ("runic_comparison.svg","alchemical_comparison.svg"):
    txt=(b/sheet).read_text(encoding="utf-8")
    assert txt.count("<use ")==8 and "data:image/png;base64," in txt
print("PASS: sixteen candidates; original source sprites, vector geometry and review sheets.")
