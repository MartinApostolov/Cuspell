#!/usr/bin/env python3
"""Regenerate 150 glyphs from canonical editable source, not the old base payload.

pip install brotli fonttools shapely cairosvg pillow
The original v0.14 R1 geometry and guide markers live under evidence/.
The historical base payload is for disaster recovery, not routine builds.
"""
from pathlib import Path
import base64, brotli, json, re, io, hashlib
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.svgLib.path import parse_path
from shapely.geometry import Polygon, LineString
from shapely.geometry.polygon import orient
from shapely.ops import unary_union
from shapely.validation import make_valid

ROOT=Path(__file__).resolve().parent
PAY=ROOT/'payload'
# Preserve all hand edits: regenerate FROM canonical source, never reset from
# the original v0.13 baseline payload.
raw=(ROOT/'source_geometry.json').read_bytes()
D=json.loads(raw)
evidence=json.loads(brotli.decompress(base64.b64decode(
    (ROOT/'evidence'/'v0.14_R1_confirmed_source.br.b64').read_text().strip())))
guide_markers=json.loads(brotli.decompress(base64.b64decode(
    (ROOT/'evidence'/'v0.14_R1_guide_markers.br.b64').read_text().strip())))
assert evidence['pack']=='v0.14_R1'
assert len(guide_markers)==100
assert len(D['glyphs'])==150
OUT=ROOT/'generated'
(OUT/'glyphs').mkdir(parents=True,exist_ok=True)
(OUT/'gesture_guides').mkdir(parents=True,exist_ok=True)
(OUT/'fonts').mkdir(parents=True,exist_ok=True)
(OUT/'source_geometry.json').write_bytes(raw)

for name,info in D['glyphs'].items():
    svg=info['svg']+'\n'
    (OUT/'glyphs'/f'{name}.svg').write_text(svg)
    # Original v0.14 R1 guides survive as either full source (16 new
    # candidates) or exact start/end marker markup (84 unchanged old glyphs).
    # Other IDs still have outline copies, NOT authentic stroke directions.
    guide_key=f'gesture_guides/{name}.svg'
    if info['confidence']=='EXACT_V014_R1' and guide_key in evidence['contents']:
        guide=evidence['contents'][guide_key]
    elif name in guide_markers and info['confidence']=='EXACT_V013':
        base=svg.strip()
        header,body=base.split('\\n',1)
        assert header.startswith('<svg ') and body.endswith('</svg>')
        inner=body[:-len('</svg>')].rstrip()
        guide=(header+'\\n'
            +'<rect x=".5" y=".5" width="599" height="999" fill="white" stroke="#bbb"/>\\n'
            +inner+'\\n'+guide_markers[name]+'\\n</svg>')
    else:
        guide=svg
    (OUT/'gesture_guides'/f'{name}.svg').write_text(guide)

# SVG center-lines and filled screen traces are converted into scalable font outlines.
def sample_paths(svg):
    paths=[];mir=bool(re.search(r'<g\\s+transform="translate\\(600(?:,|\\s+)0\\)\\s*scale\\(-1(?:,|\\s+)1\\)"',svg))
    for d in re.findall(r'<path\b[^>]*?\bd="([^"]+)"',svg):
        rec=RecordingPen();parse_path(d,rec)
        seq=[];old=None;first=None
        def commit():
            if len(seq)>=3:paths.append(seq[:])
            elif len(seq)==2:paths.append(seq[:])
        for typ,data in rec.value:
            if typ=='moveTo':
                commit(); old=data[0];first=old;seq=[old]
            elif typ=='lineTo':old=data[0];seq.append(old)
            elif typ=='curveTo':
                a,b,c=data
                for n in range(1,17):
                    t=n/16;u=1-t
                    seq.append((u**3*old[0]+3*u*u*t*a[0]+3*u*t*t*b[0]+t**3*c[0],u**3*old[1]+3*u*u*t*a[1]+3*u*t*t*b[1]+t**3*c[1]))
                old=c
            elif typ=='qCurveTo':
                nodes=list(data)
                if nodes[-1] is None:nodes[-1]=first
                for j in range(len(nodes)-1):
                    a,b=nodes[j:j+2]
                    for n in range(1,17):
                        t=n/16;u=1-t
                        seq.append((u*u*old[0]+2*u*t*a[0]+t*t*b[0],u*u*old[1]+2*u*t*a[1]+t*t*b[1]))
                    old=b
            elif typ=='closePath':
                if seq[-1]!=first:seq.append(first)
                commit();seq=[]
            elif typ=='endPath':commit();seq=[]
        commit()
    if mir:paths=[[(600-x,y) for x,y in path] for path in paths]
    return paths

def outline(info):
    svg=info['svg'];paths=sample_paths(svg);is_stroke='fill="none"' in svg
    if is_stroke:
        geom=unary_union([LineString(pts).buffer(33,cap_style=1,join_style=1,resolution=8) for pts in paths if len(pts)>1])
    else:
        geom=Polygon()
        for pts in paths:
            if len(pts)<3:continue
            shape=Polygon(pts)
            if not shape.is_valid:shape=make_valid(shape)
            geom=geom.symmetric_difference(shape)
    if not geom.is_valid:geom=make_valid(geom)
    pen=TTGlyphPen(None)
    shapes=[geom] if geom.geom_type=='Polygon' else list(getattr(geom,'geoms',[]))
    for p in shapes:
        if p.geom_type!='Polygon' or p.area<1:continue
        p=orient(p,1)
        for ring in [p.exterior,*p.interiors]:
            pts=list(ring.coords)
            if len(pts)<4:continue
            f=lambda a:(round(a[0]),round(1000-a[1]))
            pen.moveTo(f(pts[0]))
            for coord in pts[1:-1]:pen.lineTo(f(coord))
            pen.closePath()
    return pen.glyph()

ids=[f'G{i:03d}' for i in range(1,151)]
pen=TTGlyphPen(None);nd=pen.glyph()
glyphs={'.notdef':nd,'space':nd}
for k in ids:glyphs[k]=outline(D['glyphs'][k])
fb=FontBuilder(1000,isTTF=True)
fb.setupGlyphOrder(['.notdef','space']+ids)
fb.setupCharacterMap({32:'space',**{0xE000+i:f'G{i:03}' for i in range(1,151)}})
fb.setupGlyf(glyphs)
fb.setupHorizontalMetrics({k:(600,0) for k in glyphs})
fb.setupHorizontalHeader(ascent=850,descent=-150)
fb.setupNameTable({'familyName':'Cuspell Recovered Prototype','styleName':'Regular','fullName':'Cuspell Recovered Prototype Regular','psName':'CuspellRecoveredPrototype-Regular'})
fb.setupOS2(sTypoAscender=850,sTypoDescender=-150,usWinAscent=1000,usWinDescent=200)
fb.setupPost();fb.setupMaxp();font=fb.font
font.save(OUT/'fonts'/'CuspellRecoveredPrototype-Regular.ttf')
try:
    font.flavor='woff2';font.save(OUT/'fonts'/'CuspellRecoveredPrototype-Regular.woff2')
except ImportError:pass

preview='''<!doctype html><meta charset="utf-8"><title>Cuspell Recovery</title><style>@font-face{font-family:Cuspell;src:url(fonts/CuspellRecoveredPrototype-Regular.woff2)} body{font:16px system-ui;background:#f5f8f8;color:#193139}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:10px}.card{text-align:center;background:#fff;border:1px solid #cadadb;border-radius:8px;padding:10px}.rune{font:96px Cuspell;line-height:1.15}</style><h1>Cuspell Glyph Recovery · 150 candidates</h1><p>This is not the lost original v0.19. Check the confidence metadata before accepting shapes.</p><main>'''
for i,name in enumerate(ids,1):
    category=D['glyphs'][name]['confidence']
    preview+=f'<div class="card"><div class="rune">&#{0xE000+i};</div>{name}<small><br>{category}</small></div>'
(OUT/'preview.html').write_text(preview+'</main>')
(OUT/'RECOVERY_NOTICE.md').write_text('# Recovered candidates, not original v0.19\n\nThe recovery includes 84 exact v0.13 SVGs, 16 exact v0.14 R1 SVGs, 100 v0.14 R1 guide directions (16 full original files and 84 reconstructed from original start/end marker data), 20 screenshot traces, 2 tentatively identified traces, and 28 description approximations. Later lost v0.19 geometry is not restored; all meanings remain unassigned. Guides for G101-G150 are placeholder outlines, NOT recovered original stroke order.\n')
(OUT/'SHA256SUMS.txt').write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(OUT)}\n' for p in sorted(OUT.rglob('*')) if p.is_file() and p.name!='SHA256SUMS.txt' and p.suffix!='.zip' and p.suffix!='.zip'))
print('Restored',len(ids),'glyph SVGs and regenerated fonts in',OUT)
