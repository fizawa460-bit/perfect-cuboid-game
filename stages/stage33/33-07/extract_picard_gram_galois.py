#!/usr/bin/env python3
"""Extract compact Picard-discriminant/Galois data from pinned Stoll code.

The previous pilot proved the full 64x64 Picard Gram and cc/ct matrices are
computed successfully, but printing all three matrices exceeded the public
Magma calculator output cap.  This version performs the Smith reduction and
induced discriminant action inside Magma and returns only compact invariants
and 14x14 mod-4 matrices.
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
assert ccPic^2 eq IdentityMatrix(Integers(),64);
assert ctPic^2 eq IdentityMatrix(Integers(),64);
assert ccPic*ctPic eq ctPic*ccPic;
Sm, U, V := SmithForm(pmPic);
diag := [Abs(Integers()!Sm[j,j]) : j in [1..64]];
surv := [j : j in [1..64] | diag[j] eq 4];
cc4 := [];
ct4 := [];
if #surv eq 14 then
  // Row quotient A_Pic=Z^64/Z^64*pmPic.  In Smith coordinates y=x*V,
  // the dual-parameter action is V^-1*G^-T*V.  Since ccPic,ctPic are
  // involutions, G^-T=Transpose(G).
  Bcc := V^-1 * Transpose(ccPic) * V;
  Bct := V^-1 * Transpose(ctPic) * V;
  cc4 := [[Integers()!(Bcc[surv[r],surv[c]] mod 4) : c in [1..14]] : r in [1..14]];
  ct4 := [[Integers()!(Bct[surv[r],surv[c]] mod 4) : c in [1..14]] : r in [1..14]];
end if;
printf "STAGE33_07_PIC_BEGIN\n";
printf "RANK=%o\n", Rank(pmPic);
printf "DET=%o\n", Determinant(pmPic);
printf "DIAG=%o\n", diag;
printf "SURV=%o\n", surv;
printf "CC4=%o\n", cc4;
printf "CT4=%o\n", ct4;
printf "STAGE33_07_PIC_END\n";
'''
code='SetColumns(0);\nquick := true;\n'+core+'\n'+extra
payload=urllib.parse.urlencode({'input':code}).encode()
req=urllib.request.Request(MAGMA_URL,data=payload,headers={
 'Content-Type':'application/x-www-form-urlencoded','Accept':'text/html, application/xml, application/xhtml+xml',
 'Referer':MAGMA_REFERER,'User-Agent':'perfect-cuboid-stage33/2.2'},method='POST')
resp,attempt=urlopen_retry(req,180,'Stage33-07 Picard discriminant Magma')
with resp: raw=resp.read().decode('utf-8',errors='replace')
root=ET.fromstring(raw); lines=[]
for result in root.findall('.//results'):
 for line in result.findall('.//line'): lines.append(''.join(line.itertext()))
stdout='\n'.join(lines)+'\n'
(HERE/'picard-gram-galois-magma-stdout.txt').write_text(stdout,encoding='utf-8')
if 'STAGE33_07_PIC_END' not in stdout or any(x in stdout for x in ('Runtime error','Internal error','Assertion failed')):
 print(stdout); raise SystemExit('Picard discriminant extraction failed')
def scalar(name):
 m=re.search(rf'^{name}=([^\n]+)$',stdout,re.M)
 if not m: raise SystemExit(f'missing {name}')
 return int(m.group(1).strip())
def seq(name):
 m=re.search(rf'^{name}=(.+)$',stdout,re.M)
 if not m: raise SystemExit(f'missing {name}')
 return ast.literal_eval(m.group(1))
rank=scalar('RANK'); det=scalar('DET'); diag=seq('DIAG'); surv=seq('SURV'); cc4=seq('CC4'); ct4=seq('CT4')
if rank!=64 or len(diag)!=64: raise SystemExit('Picard compact shape regression')
if cc4 and (len(cc4)!=14 or any(len(r)!=14 for r in cc4)): raise SystemExit('cc4 shape regression')
if ct4 and (len(ct4)!=14 or any(len(r)!=14 for r in ct4)): raise SystemExit('ct4 shape regression')
out={'schema':'STAGE33_07_PICARD_DISCRIMINANT_GALOIS_SOURCE_LOCK_V2','upstream_git_blob_sha1':blob,
 'submitted_code_sha256':hashlib.sha256(code.encode()).hexdigest(),'magma_request_attempt':attempt,
 'picard_rank':rank,'picard_determinant':det,'picard_smith_diagonal':diag,
 'smith_order4_positions_1based':surv,'cc_discriminant_action_14x14_mod4':cc4,'ct_discriminant_action_14x14_mod4':ct4,
 'full_64x64_matrices_printed':False,'calculator_output_cap_avoided':True}
can=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_sha256']=hashlib.sha256(can).hexdigest()
(HERE/'picard-gram-galois.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({'success':True,'rank':rank,'determinant':det,'nontrivial_smith':[d for d in diag if d>1],
 'order4_coordinate_count':len(surv),'canonical_sha256':out['canonical_sha256']},indent=2,sort_keys=True))
