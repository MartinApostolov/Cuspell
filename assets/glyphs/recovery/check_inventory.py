#!/usr/bin/env python3
"""Check glyph IDs, visual approval metadata, and pending slots before rebuilding.

Pure standard-library; safe to run without rebuilding the archived font.
"""
import json
from pathlib import Path

d=json.loads((Path(__file__).resolve().parent/'source_geometry.json').read_text())
glyphs=d['glyphs']
ids={f'G{i:03d}' for i in range(1,151)}
assert set(glyphs)==ids, f'Bad registry keys: extra={set(glyphs)-ids}; missing={ids-set(glyphs)}'
active,pending=[],[]
for gid in sorted(ids):
    g=glyphs[gid]
    svg=g.get('svg')
    state=g.get('lifecycle')
    if state=='pending_design':
        assert svg is None, f'{gid}: pending slot has a current SVG'
        assert g.get('approval')=='awaiting_user_review'
        pending.append(gid)
    else:
        assert state!='retired', f'{gid}: retired ID slot not compacted'
        assert isinstance(svg,str) and '<svg' in svg and '</svg>' in svg, f'{gid}: missing active SVG'
        active.append(gid)
    if g.get('mirror_of'):
        target=g['mirror_of']
        assert target in ids and target!=gid, f'{gid}: invalid mirror reference {target}'
        assert glyphs[target].get('lifecycle')==state, f'{gid}: mirror lifecycle mismatch'
assert len(active)+len(pending)==150
assert len(active)==150 and not pending, f'Expected 150 final approved design slots; pending={pending}'
assert 'G151' not in glyphs and 'G152' not in glyphs
assert glyphs['G145'].get('pairing')=='single'
assert glyphs['G146'].get('pairing')=='single'
assert glyphs['G147'].get('approval')=='approved_current_user'
assert glyphs['G148'].get('approval')=='approved_current_user'
assert glyphs['G148'].get('mirror_of')=='G147'
assert glyphs['G149'].get('approval')=='approved_current_user'
assert glyphs['G150'].get('approval')=='approved_current_user'
assert glyphs['G150'].get('mirror_of')=='G149'
print(f'PASS: {len(active)} active, {len(pending)} pending, 150 contiguous IDs; pending={pending}')
