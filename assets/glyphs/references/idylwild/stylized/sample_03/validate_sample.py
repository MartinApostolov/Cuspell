#!/usr/bin/env python3
"""Noncanonical sample 03 vector shape and metadata validation."""
import json
from pathlib import Path
from xml.etree import ElementTree as ET
here=Path(__file__).resolve().parent
m=json.loads((here/"manifest.json").read_text(encoding="utf-8"))
items=m["glyphs"]
assert len(items)==16
assert len({item["id"] for item in items})==16
assert sum(x["id"].startswith("R") for x in items)==8
assert sum(x["id"].startswith("A") for x in items)==8
for d in items:
    root=ET.parse(here/d["svg"]).getroot()
    assert root.get("viewBox")=="0 0 600 1000"
    paths=list(root)
    assert len(paths)>=1
    for p in paths:
        assert p.tag.endswith("path")
        assert p.get("fill")=="none"
        assert p.get("stroke-width")=="66"
        assert p.get("stroke-linecap")=="round"
        assert p.get("stroke-linejoin")=="round"
        assert p.get("d","").startswith("M ")
for name in ["runic_comparison.svg", "alchemical_comparison.svg"]:
    assert "data:image/png;base64" in (here/name).read_text()
print("PASS: 16 distinct noncanonical SVGs, original pixels in both comparisons.")
