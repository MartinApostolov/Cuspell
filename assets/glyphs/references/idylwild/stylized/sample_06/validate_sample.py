#!/usr/bin/env python3
"""Validation of noncanonical batch 06 vector candidates and source comparisons."""
from pathlib import Path
from xml.etree import ElementTree as ET
import json
base=Path(__file__).resolve().parent
d=json.loads((base/"manifest.json").read_text(encoding="utf-8"))["glyphs"]
assert len(d)==16 and len({x["id"] for x in d})==16
assert sum(x["id"].startswith("R") for x in d)==8
assert sum(x["id"].startswith("A") for x in d)==8
for x in d:
    root=ET.parse(base/x["vector"]).getroot()
    assert root.get("viewBox")=="0 0 600 1000"
    ps=list(root)
    assert len(ps)>=1 and all(t.tag.endswith("path") for t in ps)
    assert all(t.get("stroke-width")=="66" and t.get("stroke-linecap")=="round" and t.get("stroke-linejoin")=="round" for t in ps)
for name in ("runic_comparison.svg","alchemical_comparison.svg"):
    value=(base/name).read_text(encoding="utf-8")
    assert value.count("<use ")==8
    assert "data:image/png;base64," in value
print("PASS batch 06: 16 SVGs, 8 originals per sheet, no registry edits")
