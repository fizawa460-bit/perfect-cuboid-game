#!/usr/bin/env python3
"""Extract compact Picard-discriminant/Galois data from pinned Stoll code.

All 64x64 arithmetic is performed inside Magma.  We return the Smith invariants
and the induced cc/ct action on the 14 nontrivial discriminant coordinates with
their actual mixed moduli (2,4,8), avoiding the calculator output cap and the
false earlier assumption that all 14 factors had order four.
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
nz := [j : j in [1..64] | diag[j] gt 1];
mods := [diag[j] : j in nz];
// Row quotient A_Pic=Z^64/Z^64*pmPic.  In Smith coordinates y=x*V,
// the dual-parameter action is V^-1*G^-T*V.  cc and ct are involutions.
Bcc := V^-1 * Transpose(ccPic) * V;
Bct := V^-1 * Transpose(ctPic) * V;
ccdisc := [[Integers()!(Bcc[nz[r],nz[c]] mod mods[c]) : c in [1..#nz]] : r in [1..#nz]];
ctdisc := [[Integers()!(Bct[nz[r],nz[c]] mod mods[c]) : c in [1..#nz]] : r in [1..#nz]];
printf "STAGE33_07_PIC_BEGIN\n";
printf "RANK=%o\n", Rank(pmPic);
printf "DET=%o\n", Determinant(pmPic);
printf "DIAG=%o\n", diag;
printf "NZ=%o\n", nz;
printf "MODS=%o\n", mods;
printf "CCDISC=%o\n", ccdisc;
printf "CTDISC=%o\n", ctdisc;
printf "STAGE33_07_PIC_END\n";
'''
code='SetColumns(0);\nquick := true;\n'+core+'\n'+extra
payload=urllib.parse.urlencode({'input':code}).encode()
req=urllib.request.Request(MAGMA_URL,data=payload,headers={
 'Content-Type':'application/x-www-form-urlencoded','Accept':'text/html, application/xml, application/xhtml+xml',
 'Referer':MAGMA_REFERER,'User-Agent':'perfect-cuboid-stage33/2.5'},method='POST')
resp,attempt=urlopen_retry(req,180,'Stage33-07 Picard discriminant Magma')
with resp: raw=resp.read().decode('utf-8',errors='replace')
root=ET.fromstring(raw); lines=[]
for result in root.findall('.//results'):
 for line in result.findall('.//line'): lines.append(''.join(line.itertext()))
stdout='\n'.join(lines)+'\n'; (HERE/'picard-gram-galois-magma-stdout.txt').write_text(stdout,encoding='utf-8')
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
rank=scalar('RANK'); det=scalar('DET'); diag=seq('DIAG'); nz=seq('NZ'); mods=seq('MODS'); cc=seq('CCDISC'); ct=seq('CTDISC')
if rank!=64 or len(diag)!=64 or len(nz)!=14 or len(mods)!=14: raise SystemExit('Picard compact shape regression')
if mods != [2]*4+[4]*6+[8]*4: raise SystemExit(f'unexpected discriminant moduli {mods}')
if len(cc)!=14 or any(len(r)!=14 for r in cc) or len(ct)!=14 or any(len(r)!=14 for r in ct): raise SystemExit('discriminant action shape regression')

def well_defined(M):
 return all((mods[i]*int(M[i][j]))%mods[j]==0 for i in range(14) for j in range(14))
def prod(A,B,i,j): return sum(int(A[i][k])*int(B[k][j]) for k in range(14))%mods[j]
def identity(M): return all(prod(M,M,i,j)==(1 if i==j else 0)%mods[j] for i in range(14) for j in range(14))
def commute(A,B): return all(prod(A,B,i,j)==prod(B,A,i,j) for i in range(14) for j in range(14))
if not well_defined(cc) or not well_defined(ct): raise SystemExit('mixed-modulus action not well-defined')
if not identity(cc) or not identity(ct) or not commute(cc,ct): raise SystemExit('mixed discriminant V4 relation failed')
out={'schema':'STAGE33_07_PICARD_DISCRIMINANT_GALOIS_SOURCE_LOCK_V3','upstream_git_blob_sha1':blob,
 'submitted_code_sha256':hashlib.sha256(code.encode()).hexdigest(),'magma_request_attempt':attempt,
 'picard_rank':rank,'picard_determinant':det,'picard_smith_diagonal':diag,
 'nontrivial_smith_positions_1based':nz,'discriminant_moduli':mods,
 'cc_discriminant_action_mixed_moduli':cc,'ct_discriminant_action_mixed_moduli':ct,
 'mixed_action_well_defined':True,'cc_ct_involutions_and_commute_on_discriminant':True,
 'picard_discriminant_group':'(Z/2)^4 direct_sum (Z/4)^6 direct_sum (Z/8)^4',
 'full_64x64_matrices_printed':False,'calculator_output_cap_avoided':True}
can=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_sha256']=hashlib.sha256(can).hexdigest()
(HERE/'picard-gram-galois.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({'success':True,'rank':rank,'determinant':det,'discriminant_moduli':mods,
 'mixed_discriminant_action_exact':True,'canonical_sha256':out['canonical_sha256']},indent=2,sort_keys=True))
