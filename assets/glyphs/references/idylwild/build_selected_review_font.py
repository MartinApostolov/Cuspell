#!/usr/bin/env python3
"""Build the Cuspell 234-survivor PC typing kit. No semantic assignments."""
from __future__ import annotations
import csv, hashlib, json, math, re, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.svgLib.path import parse_path
from fontTools.ttLib import TTFont
from shapely.geometry import Polygon, Point, LineString
from shapely.geometry.polygon import orient
from shapely.ops import unary_union

BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[3]
GEO=ROOT/'assets/glyphs/recovery/source_geometry.json'
ANA=BASE/'stylized/analysis'
PUN=BASE/'stylized/typography/player_facing'
DEST=BASE/'keyboard_kit'
FONT='CuspellCodexReview-Regular.ttf'
ZIP='Cuspell_Codex_Keyboard_Kit.zip'
ASC=850

def sample_path(d,mirror):
    recorder=RecordingPen();parse_path(d,recorder)
    contours=[];pts=[];current=(0.,0.)
    def add(pt):
        nonlocal current
        current=pt
        p=(600-pt[0] if mirror else pt[0],pt[1])
        if not pts or math.dist(pts[-1],p)>.000001:pts.append(p)
    def interpolate(seq,t):
        u=1-t
        if len(seq)==3:
            a,b,c=seq
            return (u*u*a[0]+2*u*t*b[0]+t*t*c[0],u*u*a[1]+2*u*t*b[1]+t*t*c[1])
        a,b,c,e=seq
        return (u**3*a[0]+3*u*u*t*b[0]+3*u*t*t*c[0]+t**3*e[0],u**3*a[1]+3*u*u*t*b[1]+3*u*t*t*c[1]+t**3*e[1])
    for command,args in recorder.value:
        if command=='moveTo':
            if pts:contours.append((pts,False))
            pts=[];add(args[0])
        elif command=='lineTo':add(args[0])
        elif command in ('curveTo','qCurveTo'):
            src=[current,*args]
            if len(src) not in (3,4) or src[-1] is None:raise ValueError('Unexpected SVG curve '+d[:100])
            length=sum(math.dist(a,b) for a,b in zip(src,src[1:]))
            n=max(8,min(100,math.ceil(length/5)))
            for j in range(1,n+1):add(interpolate(src,j/n))
        elif command in ('closePath','endPath'):
            if pts:contours.append((pts,command=='closePath'))
            pts=[]
        else:raise ValueError('Unknown drawing instruction '+command)
    if pts:contours.append((pts,False))
    return contours

def svg_shape(source):
    root=ET.fromstring(source)
    ink=[];strokes=[]
    def walk(el,flip=False):
        trans=el.get('transform')
        if trans:
            if re.fullmatch(r'translate\(600[, ]+0\)\s*scale\(-1[, ]+1\)',trans):flip=not flip
            else:raise ValueError('Unexpected transform '+trans)
        kind=el.tag.rsplit('}',1)[-1]
        if kind=='path':
            contours=sample_path(el.attrib['d'],flip)
            if el.get('fill','black').lower() not in ('none','transparent'):
                for pts,closed in contours:
                    if len(pts)>2:
                        p=Polygon(pts)
                        if not p.is_valid:p=p.buffer(0)
                        if not p.is_empty:ink.append(p)
            if el.get('stroke','none').lower() not in ('none','transparent'):
                radius=float(el.get('stroke-width','66'))/2
                for pts,closed in contours:
                    if len(pts)>1:
                        coords=pts+([pts[0]] if closed and pts[0]!=pts[-1] else [])
                        strokes.append(LineString(coords).buffer(radius,cap_style=1,join_style=1,quad_segs=6))
                    elif pts:strokes.append(Point(pts[0]).buffer(radius,quad_segs=8))
        elif kind=='circle':
            x=float(el.get('cx'));y=float(el.get('cy'));radius=float(el.get('r'))
            if flip:x=600-x
            if el.get('fill','black').lower() not in ('none','transparent'):
                ink.append(Point(x,y).buffer(radius,quad_segs=32))
        for child in el:walk(child,flip)
    walk(root)
    shape=None
    for part in ink:shape=part if shape is None else shape.symmetric_difference(part)
    if strokes:
        union=unary_union(strokes)
        shape=union if shape is None else shape.union(union)
    if shape is None or shape.is_empty:raise ValueError('Empty source artwork')
    if not shape.is_valid:shape=shape.buffer(0)
    return shape

def to_glyph(shape,compact=False):
    pen=TTGlyphPen(None);xlist=[];count=0
    polys=list(shape.geoms) if shape.geom_type=='MultiPolygon' else [shape]
    for poly in polys:
        if poly.geom_type!='Polygon':continue
        poly=orient(poly,sign=1.)
        for ring in [poly.exterior,*poly.interiors]:
            points=[]
            for x,y in list(ring.coords)[:-1]:
                p=(round(x+(-90 if compact else 25)),round(ASC-y))
                if not points or points[-1]!=p:points.append(p)
            if len(set(points))<3:continue
            pen.moveTo(points[0])
            for point in points[1:]:pen.lineTo(point)
            pen.closePath()
            xlist.extend(x for x,y in points);count+=1
    if not count:raise ValueError('Degenerate shape')
    return pen.glyph(),((420 if compact else 650),min(xlist))

def sources():
    sel=json.loads((ANA/'potential_overlap_groups.json').read_text())
    snap=json.loads((ANA/'FRESH_SURVIVOR_A_R_SOURCE_SNAPSHOT_2026_11_21.json').read_text())
    geo=json.loads(GEO.read_text())['glyphs']
    excluded=set(sel['final_inventory_exclusion_summary']['direct_source_ids'])
    reserved={x['id'] for x in sel['final_inventory_typography_reserve']['entries']}
    glyphs=[{'id':id,'collection':'Cuspell','svg':src['svg']} for id,src in geo.items()
            if re.fullmatch(r'G\d{3}',id) and id not in excluded]
    glyphs += [{'id':x['id'],'collection':('Alchemical' if x['id'].startswith('A') else 'Runic'),'svg':x['svg']} for x in snap['eligibleFiles']]
    glyphs.sort(key=lambda x:x['id'])
    if snap['progress']!=140 or len(glyphs)!=234 or len({x['id'] for x in glyphs})!=234:raise ValueError('Expected 234 unique selected designs')
    if {x['id'] for x in glyphs}&(excluded|reserved):raise ValueError('Excluded or punctuation-reserved glyph included')
    manifest=json.loads((PUN/'manifest.json').read_text())
    punct=[{**x,'svg':(PUN/x['file']).read_text()} for x in manifest['entries']]
    if len(punct)!=13 or len(set(x['character'] for x in punct))!=13:raise ValueError('Missing approved punctuation')
    return glyphs,punct

def font_and_map(glyphs,punct):
    order=['.notdef','space']+[('punct_'+p['id']) for p in punct]+[g['id'] for g in glyphs]
    fb=FontBuilder(1000,isTTF=True);fb.setupGlyphOrder(order)
    blank=TTGlyphPen(None).glyph()
    outlines={'.notdef':blank,'space':TTGlyphPen(None).glyph()}
    metrics={'.notdef':(650,0),'space':(320,0)}
    cmap={0x20:'space'};rows=[]
    for index,item in enumerate(glyphs):
        name=item['id'];outlines[name],metrics[name]=to_glyph(svg_shape(item['svg']))
        cp=0xE000+index;cmap[cp]=name
        rows.append({'collection':item['collection'],'id':name,'codepoint':'U+%04X'%cp,'character':chr(cp)})
    for p in punct:
        name='punct_'+p['id']
        outlines[name],metrics[name]=to_glyph(svg_shape(p['svg']),True)
        cmap[ord(p['character'])]=name
    fb.setupCharacterMap(cmap)
    fb.setupGlyf(outlines)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=ASC,descent=-250,lineGap=120)
    fb.setupNameTable({'familyName':'Cuspell 234 Review','styleName':'Regular',
        'uniqueFontIdentifier':'Cuspell234Review-2026-11','fullName':'Cuspell 234 Review Regular',
        'psName':'Cuspell234Review-Regular','version':'Version 1.0; 2026-11',
        'description':'234 unassigned glyphs plus 13 approved punctuation designs'})
    fb.setupOS2(sTypoAscender=ASC,sTypoDescender=-250,sTypoLineGap=120,
                usWinAscent=ASC,usWinDescent=250,fsType=0)
    fb.setupPost();fb.setupMaxp()
    DEST.mkdir(parents=True,exist_ok=True)
    fb.save(str(DEST/FONT))
    check=TTFont(DEST/FONT)
    known=check.getBestCmap()
    assert all(known[0xE000+i]==r['id'] for i,r in enumerate(rows))
    assert all(known[ord(p['character'])]=='punct_'+p['id'] for p in punct)
    assert len(set(known.values()))==len(known)==248
    check.close()
    try:
        extra=TTFont(DEST/FONT);extra.flavor='woff2';extra.save(DEST/'CuspellCodexReview-Regular.woff2');extra.close()
    except Exception as exc:print('Optional WOFF2 unavailable:',exc)
    return rows

CSS="""@font-face{font-family:Cuspell234;src:url('CuspellCodexReview-Regular.ttf') format('truetype')}
:root{font-family:system-ui,Arial,sans-serif;background:#f3f6fa;color:#223247}
body{margin:0 auto;max-width:1320px;padding:20px}
h1{margin-bottom:4px}p{line-height:1.5}.muted{color:#576a80}
button,input,select,textarea{font:inherit}button{border:1px solid #b6c7d8;background:white;border-radius:8px;padding:8px 10px;cursor:pointer}
button:hover{background:#e4edf6}button.active{background:#253e60;color:white}
.toolbar{background:#edf3f9;border:1px solid #c7d5e3;border-radius:10px;padding:14px}
.controls{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:10px 0}
#work{display:block;width:100%;box-sizing:border-box;min-height:126px;border:1px solid #adc1d5;border-radius:8px;background:white;font:34px Cuspell234;padding:12px;line-height:1.5;resize:vertical}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(90px,1fr));gap:8px;margin:18px 0}
.tile{min-height:91px;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:5px}
.glyph{font:42px Cuspell234;line-height:1.2}.tile small{font-size:11px;color:#667a8b}
.notice{background:white;padding:13px;border-radius:9px;border:1px solid #d8e1ed}
@media print{.toolbar{display:none}.grid{grid-template-columns:repeat(12,1fr)}.tile{break-inside:avoid}}
"""

def pages(rows,punct):
    data=json.dumps(rows,ensure_ascii=True,separators=(',',':'))
    marks=json.dumps([{'id':p['id'],'character':p['character']} for p in punct],ensure_ascii=True,separators=(',',':'))
    header='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>'+CSS+'</style>'
    body=header+"""<title>Cuspell 234 Glyph Keyboard</title></head><body>
<h1>Cuspell · 234-glyph review keyboard</h1>
<p class="muted">234 surviving glyphs and 13 punctuation marks. No glyph-to-meaning assignments. Recommended testing 32–34px, minimum 20px.</p>
<div class="toolbar"><div class="controls" id="tabs">
<button class="active" data-group="All">All 234</button>
<button data-group="Cuspell">Cuspell originals</button><button data-group="Runic">Runic</button><button data-group="Alchemical">Alchemical</button></div>
<div class="controls"><label>Find ID <input id="search" type="search" placeholder="G060, R076, A043, E000"></label>
<label>Font size <select id="size"><option>20</option><option>32</option><option selected>34</option><option>42</option><option>48</option></select>px</label></div>
<textarea id="work" spellcheck="false" aria-label="Your glyph writing"></textarea>
<div class="controls"><button id="copy">Copy glyph text</button><button id="space">Space</button><button id="enter">New line</button><button id="clear">Clear</button><button id="save">Save text</button><a href="chart.html">Full chart</a></div>
<div class="controls" id="marks"></div><span id="status" class="muted"></span></div>
<div id="grid" class="grid"></div>
<div class="notice">For Windows, install <code>CuspellCodexReview-Regular.ttf</code> and select <strong>Cuspell 234 Review</strong> in your editor. Keep this page in the same folder as the TTF. Private Use Area U+E000–U+E0E9 is temporary: no meanings are assigned. The old 449-symbol comparison font is no longer this package.</div>
<script>
const GLYPHS=__GLYPHS__, MARKS=__MARKS__, $=s=>document.querySelector(s);
let group='All'; const area=$('#work');
function insert(t){const a=area.selectionStart,b=area.selectionEnd;area.value=area.value.slice(0,a)+t+area.value.slice(b);area.selectionStart=area.selectionEnd=a+t.length;area.focus()}
function render(){const q=$('#search').value.trim().toLowerCase(),grid=$('#grid');grid.textContent='';let n=0;
for(const g of GLYPHS){if(group!=='All'&&g.collection!==group)continue;if(q&&!((g.id+' '+g.codepoint+' '+g.collection).toLowerCase().includes(q)))continue;
const b=document.createElement('button'),visual=document.createElement('span'),label=document.createElement('small');
b.className='tile';visual.className='glyph';visual.textContent=g.character;label.textContent=g.id;b.title=g.codepoint;b.append(visual,label);b.onclick=()=>insert(g.character);grid.append(b);n++;}
$('#status').textContent='Showing '+n+' / 234 glyphs'}
for(const b of document.querySelectorAll('[data-group]'))b.onclick=()=>{group=b.dataset.group;for(const button of document.querySelectorAll('[data-group]'))button.classList.toggle('active',button===b);render()};
for(const mark of MARKS){const b=document.createElement('button');b.textContent=mark.character+' · '+mark.id.replaceAll('_',' ');b.onclick=()=>insert(mark.character);$('#marks').append(b)}
$('#search').oninput=render;$('#size').onchange=()=>area.style.fontSize=$('#size').value+'px';
$('#space').onclick=()=>insert(' ');$('#enter').onclick=()=>insert(String.fromCharCode(10));$('#clear').onclick=()=>area.value='';
$('#copy').onclick=async()=>{try{await navigator.clipboard.writeText(area.value);$('#status').textContent='Copied'}catch(e){area.select();document.execCommand('copy');$('#status').textContent='Select and copy the text'}};
$('#save').onclick=()=>{const u=URL.createObjectURL(new Blob([area.value],{type:'text/plain;charset=utf-8'})),a=document.createElement('a');a.href=u;a.download='cuspell-test-text.txt';a.click();URL.revokeObjectURL(u)};
render();
</script></body></html>"""
    (DEST/'keyboard.html').write_text(body.replace('__GLYPHS__',data).replace('__MARKS__',marks),encoding='utf8')
    chart=header+"""<title>Cuspell glyph chart</title></head><body><h1>Cuspell · 234-glyph chart</h1>
<p class="muted">Print this chart or open the <a href="keyboard.html">click-to-type keyboard</a>. Designs are not yet assigned meanings.</p>
<div class="grid" id="grid"></div><script>const glyphs=__GLYPHS__;
for(const g of glyphs){const tile=document.createElement('div'),symbol=document.createElement('span'),label=document.createElement('small');
tile.className='tile';tile.style.cssText='background:white;border:1px solid #cbd6e1';symbol.className='glyph';symbol.textContent=g.character;label.textContent=g.id+' '+g.codepoint;
tile.append(symbol,label);document.querySelector('#grid').append(tile);}</script></body></html>"""
    (DEST/'chart.html').write_text(chart.replace('__GLYPHS__',data),encoding='utf8')
    with (DEST/'glyph_map.csv').open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=['collection','id','codepoint','character'])
        w.writeheader();w.writerows(rows)

def main():
    glyphs,punct=sources()
    rows=font_and_map(glyphs,punct);pages(rows,punct)
    sha=hashlib.sha256((DEST/FONT).read_bytes()).hexdigest()
    counts={k:sum(x['collection']==k for x in rows) for k in ('Cuspell','Runic','Alchemical')}
    info={'status':'complete_pc_test_font','font_family':'Cuspell 234 Review','font':FONT,
        'num_cuspell':counts['Cuspell'],'num_runic':counts['Runic'],
        'num_alchemical':counts['Alchemical'],'num_total':234,'punctuation_count':13,
        'private_use_range':['E000','E0E9'],'font_sha256':sha,'root_meanings_assigned':False,
        'recommended_size_px':[32,34],'minimum_size_px':20}
    (DEST/'font_manifest.json').write_text(json.dumps(info,indent=2)+'\n')
    (DEST/'SOURCES.txt').write_text('Cuspell 234 Review: 94 original Cuspell designs and 140 stylized Idylwild Runic/Alchemical designs. Idylwild source artwork CC0. Original source ZIPs, SVGs and exclusion history are preserved in the repository. 13 punctuation glyphs are separately approved. Temporary private-use codepoints assign no meanings.\n')
    (DEST/'README.md').write_text('# Cuspell 234 PC testing kit\n\n1. Download and extract Cuspell_Codex_Keyboard_Kit.zip.\n2. Install CuspellCodexReview-Regular.ttf. Select font family Cuspell 234 Review in your word processor.\n3. Open keyboard.html from the extracted folder, click glyphs to type, and copy/paste the result. chart.html is the printable catalog.\n4. Test at 32–34px or larger (minimum 20px). Report spacing or glyph problems before assigning meanings.\n\nContains exactly 234 unassigned signs and 13 approved punctuation marks. Private use U+E000–U+E0E9 maps to glyph IDs in glyph_map.csv. No semantic mappings yet.\n')
    names=[FONT,'keyboard.html','chart.html','glyph_map.csv','font_manifest.json','README.md','SOURCES.txt']
    if (DEST/'CuspellCodexReview-Regular.woff2').exists():names.insert(1,'CuspellCodexReview-Regular.woff2')
    with zipfile.ZipFile(DEST/ZIP,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=8) as z:
        for name in names:z.write(DEST/name,name)
    with zipfile.ZipFile(DEST/ZIP) as z:assert z.testzip() is None
    print('PASS: 234 glyphs, 13 punctuation, keyboard.html, chart.html and single-download ZIP')

if __name__=='__main__': main()
