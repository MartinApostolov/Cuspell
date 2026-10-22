#!/usr/bin/env python3
"""Validate experimental batch 04, with no dependency on the canonical registry."""
from pathlib import Path
import json
import xml.etree.ElementTree as ET
base=Path(__file__).resolve().parent
m=json.loads((base/"manifest.json").read_text(encoding="utf-8"))
items=m["glyphs"]
assert len(items)==16 and len({s["id"] for s in items})==16
assert sum(s["id"].startswith("R") for s in items)==8
assert sum(s["id"].startswith("A") for s in items)==8
for s in items:
  root=ET.parse(base/s["svg"]).getroot()
  assert root.attrib["viewBox"]=="0 0 600 1000"
  paths=[p for p in root if p.tag.endswith("path")]
  assert paths
  for p in paths:
    assert p.get("d","").startswith("M ")
    assert p.get("stroke-width")=="66"
    assert p.get("stroke-linecap")=="round"
    assert p.get("stroke-linejoin")=="round"
    assert p.get("fill")=="none"
for file in ["runic_comparison.svg","alchemical_comparison.svg"]:
  text=(base/file).read_text(encoding="utf-8")
  assert text.count("<use ")==8
  assert "data:image/png;base64," in text
print("PASS 16 candidate SVGs; comparison sheets contain 8 source sprites each")
