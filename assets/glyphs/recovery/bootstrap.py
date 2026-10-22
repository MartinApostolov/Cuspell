#!/usr/bin/env python3
"""Restore build script and editable source from durable, split Brotli archives."""
from pathlib import Path
import base64
import brotli

root = Path(__file__).resolve().parent
payload = root / "payload"
segments = [payload / f"source.part{i:02}.b64" for i in range(1, 9)]
encoded = "".join(p.read_text().strip() for p in segments)
if len(encoded) != 35184:
    raise SystemExit(f"Source archive incomplete: {len(encoded)} chars, expected 35184")
data = brotli.decompress(base64.b64decode(encoded))
(root / "source_geometry.json").write_bytes(data)
script = brotli.decompress(base64.b64decode((payload / "restore.py.br.b64").read_text().strip()))
(root / "restore.py").write_bytes(script)
print(f"Recovered {len(data)} bytes of editable source and {len(script)} bytes of builder.")
