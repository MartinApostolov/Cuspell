#!/usr/bin/env python3
"""Validate noncanonical stylization batch 07, including comparison imagery."""
from pathlib import Path
from xml.etree import ElementTree as ET
import json
folder=Path(__file__).resolve().parent
m=json.loads((folder/"manifest.json").read_text(encoding="utf-8"))
items=m["glyphs"]
assert len(items)==16 and len({x["id"] for x in items})==16
assert sum(x["id"].startswith("R") for x in items)==8
assert sum(x["id"].startswith("A") for x in items)==8
for info in items:
    assert info["fixed_root_mapping"] is None
    svg=ET.parse(folder/info["adapted_svg"]).getroot()
    assert svg.get("viewBox")=="0 0 600 1000"
    paths=list(svg)
    assert paths and all(p.tag.endswith("path") for p in paths)
    assert all(p.get("stroke-width")=="66" and p.get("stroke-linecap")=="round" and p.get("stroke-linejoin")=="round" for p in paths)
for fn in ("runic_comparison.svg","alchemical_comparison.svg"):
    contents=(folder/fn).read_text(encoding="utf-8")
    assert contents.count("<use ")==8
    assert "data:image/png;base64," in contents
print("PASS: 16 IDs, 16 candidate vectors, two embedded-source visual comparisons")
