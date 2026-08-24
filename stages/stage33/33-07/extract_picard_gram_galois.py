#!/usr/bin/env python3
"""Extract the exact Picard Gram matrix and cc/ct action from pinned Stoll code.

Reuse the already-audited Stage33-04 upstream/Magma transport adapter instead of
introducing a second network/source-lock implementation.
"""
import ast, hashlib, json, pathlib, re, runpy, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

HERE=pathlib.Path(__file__).resolve().parent
adapter=runpy.run_path(str(HERE.parent/'33-04'/'extract_boundary_galois.py'))
core=adapter['core']; blob=adapter['actual_blob']
urlopen_retry=adapter['urlopen_retry']; MAGMA_URL=adapter['MAGMA_URL']; MAGMA_REFERER=adapter['MAGMA_REFERER']

extra=r'''
actperm := func<g, perm | qPic(Big![e[perm[j]] : j in [1..#e]]) where e := Eltseq(g @@ qPic)>;
ccL := hom<L -> L | -i>;
ccPL := hom<R -> R | ccL*Bang(L,R), [R.j : j in [1..7]]> where R := CoordinateRing(Pr6);
actcc := func<C | Curve(Pr6, [ccPL(e) : e in DefiningEquations(C)])>;
permcc := [Position(C1s, actcc(C)) : C in C1s]
 cat [#C1s+Position(C2s, actcc(C)) : C in C2s]
 cat [#C1s+#C2s+Position(C3s, actcc(C)) : C in C3s]
 cat [#Cs+Position(pts, Pr6![ccL(a) : a in Eltseq(pt)]) : pt in pts];
ccPic := Matrix(Integers(), [Eltseq(actperm(Pic.j, permcc)) : j in [1..64]]);
ctL := hom<L -> L | hom<GroundField(L) -> L | -s>, i>;
ctPL := hom<R -> R | ctL*Bang(L,R), [R.j : j in [1..7]]> where R := CoordinateRing(Pr6);
actct := func<C | Curve(Pr6, [ctPL(e) : e in DefiningEquations(C)])>;
permct := [Position(C1s, actct(C)) : C in C1s]
 cat [#C1s+Position(C2s, actct(C)) : C in C2s]
 cat [#C1s+#C2s+Position(C3s, actct(C)) : C in C3s]
 cat [#Cs+Position(pts, Pr6![ctL(a) : a in Eltseq(pt)]) : pt in pts];
ctPic := Matrix(Integers(), [Eltseq(actperm(Pic.j, permct)) : j in [1..64]]);
assert ccPic*pmPic*Transpose(ccPic) eq pmPic;
assert ctPic*pmPic*Transpose(ctPic) eq pmPic;
printf "STAGE33_07_PIC_BEGIN\n";
printf "P=%o\n", [[pmPic[r,c] : c in [1..64]] : r in [1..64]];
printf "CC=%o\n", [[ccPic[r,c] : c in [1..64]] : r in [1..64]];
printf "CT=%o\n", [[ctPic[r,c] : c in [1..64]] : r in [1..64]];
printf "STAGE33_07_PIC_END\n";
'''
code='SetColumns(0);\nquick := true;\n'+core+'\n'+extra
payload=urllib.parse.urlencode({'input':code}).encode()
req=urllib.request.Request(MAGMA_URL,data=payload,headers={
 'Content-Type':'application/x-www-form-urlencoded','Accept':'text/html, application/xml, application/xhtml+xml',
 'Referer':MAGMA_REFERER,'User-Agent':'perfect-cuboid-stage33/2.1'},method='POST')
resp,attempt=urlopen_retry(req,180,'Stage33-07 Picard Magma')
with resp: raw=resp.read().decode('utf-8',errors='replace')
root=ET.fromstring(raw); lines=[]
for result in root.findall('.//results'):
 for line in result.findall('.//line'): lines.append(''.join(line.itertext()))
stdout='\n'.join(lines)+'\n'
(HERE/'picard-gram-galois-magma-stdout.txt').write_text(stdout,encoding='utf-8')
if 'STAGE33_07_PIC_END' not in stdout or any(x in stdout for x in ('Runtime error','Internal error','Assertion failed')):
 print(stdout); raise SystemExit('Picard extraction failed')
def seq(name):
 m=re.search(rf'^{name}=(.+)$',stdout,re.M)
 if not m: raise SystemExit(f'missing {name}')
 return ast.literal_eval(m.group(1))
P,CC,CT=seq('P'),seq('CC'),seq('CT')
if any(len(M)!=64 or any(len(r)!=64 for r in M) for M in (P,CC,CT)): raise SystemExit('matrix shape regression')
out={'schema':'STAGE33_07_PICARD_GRAM_GALOIS_SOURCE_LOCK_V1','upstream_git_blob_sha1':blob,
 'submitted_code_sha256':hashlib.sha256(code.encode()).hexdigest(),'magma_request_attempt':attempt,
 'picard_gram_64x64':P,'cc_picard_action_64x64':CC,'ct_picard_action_64x64':CT}
can=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_sha256']=hashlib.sha256(can).hexdigest()
(HERE/'picard-gram-galois.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({'success':True,'rank':64,'canonical_sha256':out['canonical_sha256']},indent=2,sort_keys=True))
