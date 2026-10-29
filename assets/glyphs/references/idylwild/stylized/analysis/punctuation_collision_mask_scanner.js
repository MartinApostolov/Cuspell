(()=>{
const M={
".":["M 301 787 L 301 790"],":":["M 301 384 L 301 387","M 301 698 L 301 701"],
"?":["M 168 300 C 179 213 247 167 318 171 C 403 173 455 254 440 349 C 430 411 376 443 308 480 C 262 504 265 555 271 615","M 275 790 L 275 793"],
"!":["M 301 184 C 305 340 301 491 300 660","M 300 789 L 300 792"],
"«":["M 262 302 C 215 388 181 445 145 500 C 187 557 218 616 262 703","M 447 302 C 400 388 366 445 330 500 C 372 557 403 616 447 703"],
"»":["M 153 302 C 200 388 234 445 270 500 C 228 557 197 616 153 703","M 338 302 C 385 388 419 445 455 500 C 413 557 382 616 338 703"],
"$":["M 424 301 C 366 236 244 239 190 319 C 124 425 213 484 304 502 C 409 525 461 595 413 681 C 364 763 232 764 173 690","M 301 156 L 301 843"],
"(":["M 413 169 C 299 233 248 352 246 499 C 247 644 303 768 413 830"],
")":["M 187 169 C 301 233 352 352 354 499 C 353 644 297 768 187 830"],
"_":["M 150 835 C 240 834 357 836 450 835"],
"{":["M 439 166 C 323 168 289 225 292 317 L 292 408 C 291 467 250 485 184 500 C 250 515 291 533 292 592 L 292 683 C 289 775 323 832 439 834"],
"}":["M 161 166 C 277 168 311 225 308 317 L 308 408 C 309 467 350 485 416 500 C 350 515 309 533 308 592 L 308 683 C 311 775 277 832 161 834"],
",":["M 314 743 L 314 747","M 314 783 C 305 817 292 839 270 858"]
};
const W=60,H=100;
function raster(svg){
const a=new Uint8Array(W*H),rev=/scale\(-1[, ]+1\)/.test(svg);
function pt(x,y,r){x=(rev?600-x:x)/10;y/=10;r/=10;for(let v=Math.max(0,Math.floor(y-r));v<=Math.min(H-1,Math.ceil(y+r));v++)for(let u=Math.max(0,Math.floor(x-r));u<=Math.min(W-1,Math.ceil(x+r));u++)if((u-x)**2+(v-y)**2<=r*r)a[v*W+u]=1}
function line(p,q,r){let n=Math.max(1,Math.ceil(Math.hypot(p[0]-q[0],p[1]-q[1])/6));for(let t=0;t<=n;t++)pt(p[0]+(q[0]-p[0])*t/n,p[1]+(q[1]-p[1])*t/n,r)}
for(const m of svg.matchAll(/<path\b[^>]*>/g)){
let tag=m[0],d=(tag.match(/\bd="([^"]+)"/)||[])[1];if(!d)continue;
let sw=+(tag.match(/stroke-width="([^"]+)"/)||[])[1]||66,fill=/fill="(?:black|#[a-f\d]{3,8})"/i.test(tag),stroke=!fill||/stroke="(?!none)/.test(tag);
let t=d.match(/[MLHVQCZmlhvqcz]|-?\d+(?:\.\d+)?/g)||[],i=0,cmd="",p=[0,0],start=[0,0],c=[],polys=[],guard=0;
while(i<t.length&&guard++<30000){
if(/^[MLHVQCZmlhvqcz]$/.test(t[i])){cmd=t[i++].toUpperCase();if(cmd==="Z"){if(stroke)line(p,start,sw/2);if(c.length)polys.push(c);c=[];p=start;continue}}
let n={M:2,L:2,H:1,V:1,Q:4,C:6}[cmd];if(!n||i+n>t.length)break;
if(cmd==="M"){if(c.length)polys.push(c);p=[+t[i++],+t[i++]];start=p;c=[p];cmd="L";continue}
let x=p,b,cp,cp2;if(cmd==="L")b=[+t[i++],+t[i++]];else if(cmd==="H")b=[+t[i++],p[1]];else if(cmd==="V")b=[p[0],+t[i++]];
else if(cmd==="Q"){cp=[+t[i++],+t[i++]];b=[+t[i++],+t[i++]]}
else if(cmd==="C"){cp=[+t[i++],+t[i++]];cp2=[+t[i++],+t[i++]];b=[+t[i++],+t[i++]]}
if(cmd==="L"||cmd==="H"||cmd==="V"){if(stroke)line(p,b,sw/2);c.push(b)}
else {let prev=p;for(let j=1;j<=20;j++){let z=j/20,k=1-z;
let xy=cmd==="Q"?[k*k*p[0]+2*k*z*cp[0]+z*z*b[0],k*k*p[1]+2*k*z*cp[1]+z*z*b[1]]:[k*k*k*p[0]+3*k*k*z*cp[0]+3*k*z*z*cp2[0]+z*z*z*b[0],k*k*k*p[1]+3*k*k*z*cp[1]+3*k*z*z*cp2[1]+z*z*z*b[1]];
if(stroke)line(prev,xy,sw/2);c.push(xy);prev=xy}}
p=b}
if(c.length)polys.push(c);
if(fill){const contours=polys.filter(p=>p.length>=3).map(p=>p.map(([x,y])=>[(rev?600-x:x)/10,y/10]));for(let y=0;y<H;y++)for(let x=0;x<W;x++){let hit=false;for(const poly of contours){let inside=false;for(let u=0,v=poly.length-1;u<poly.length;v=u++){let a=poly[u],b=poly[v];if((a[1]>y)!==(b[1]>y)&&x<(b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0])inside=!inside}if(inside)hit=!hit}if(hit)a[y*W+x]=1}}
}
for(const m of svg.matchAll(/<circle\b[^>]*>/g)){let tag=m[0],g=k=>+(tag.match(new RegExp(k+'="([^"]+)"'))||[])[1],cx=g('cx'),cy=g('cy'),r=g('r');if(Number.isFinite(cx+cy+r))for(let j=0;j<60;j++){let th=j*Math.PI/30;pt(cx+r*Math.cos(th),cy+r*Math.sin(th),33)}}
let n=0;for(const v of a)n+=v;return {a,n}
}
const refs=Object.fromEntries(Object.entries(M).map(([k,paths])=>[k,raster('<svg>'+paths.map(d=>'<path d="'+d+'" fill="none" stroke="black" stroke-width="66"/>').join('')+'</svg>')]));
function dice(p,q,dx,dy,rev){let common=0;if(!p.n||!q.n)return 0;for(let y=0;y<H;y++)for(let x=0;x<W;x++)if(p.a[y*W+x]){let tx=(rev?W-1-x:x)+dx,ty=y+dy;if(tx>=0&&tx<W&&ty>=0&&ty<H&&q.a[ty*W+tx])common++}return 2*common/(p.n+q.n)}
function score(svg){const src=raster(svg);let ret={};for(const [key,ref] of Object.entries(refs)){let best=0,mirror=false;for(const r of [false,true])for(let x of [-3,0,3])for(let y of [-5,0,5]){let v=dice(src,ref,x,y,r);if(v>best){best=v;mirror=r}}ret[key]=[+best.toFixed(3),mirror]}return ret}
return {score,ink:raster,refs:Object.fromEntries(Object.entries(refs).map(([k,v])=>[k,v.n]))}
})()