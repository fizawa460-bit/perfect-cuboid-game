#!/usr/bin/env python3
"""Extract the K_c Picard discriminant form and exact cc/ct action.

This is a bounded regression input for testing any proposed endpoint HS-d2
formula against the already hostile-audited K_c result (J2 survives, q1 dies).
No K_c audit credit is changed here.
"""
import ast, hashlib, json, pathlib, re
from stoll_cuboid_source import load_pinned_source, run_magma

HERE=pathlib.Path(__file__).resolve().parent
text,core,blob,source_attempt=load_pinned_source()
START='// Now repeat this for the K3 quotient obtained by forgetting c. See Section 6.'
END='// action of sign change of c'
i0=text.index(START); i1=text.index(END,i0); kcore=text[i0:i1]
extra=r'''
// Reconstruct endpoint Galois actions exactly as in the source-locked S computation.
actperm33 := func<g, perm | qPic(Big![e[perm[j]] : j in [1..#e]]) where e := Eltseq(g @@ qPic)>;
ccL33 := hom<L -> L | -i>;
ccPL33 := hom<R -> R | ccL33*Bang(L,R), [R.j : j in [1..7]]> where R := CoordinateRing(Pr6);
actcc33 := func<C | Curve(Pr6, [ccPL33(e) : e in DefiningEquations(C)])>;
permcc33 := [Position(C1s, actcc33(C)) : C in C1s]
 cat [#C1s+Position(C2s, actcc33(C)) : C in C2s]
 cat [#C1s+#C2s+Position(C3s, actcc33(C)) : C in C3s]
 cat [#Cs+Position(pts, Pr6![ccL33(a) : a in Eltseq(pt)]) : pt in pts];
GccS := Matrix(Integers(), [Eltseq(actperm33(Pic.j, permcc33)) : j in [1..64]]);
ctL33 := hom<L -> L | hom<GroundField(L) -> L | -s>, i>;
ctPL33 := hom<R -> R | ctL33*Bang(L,R), [R.j : j in [1..7]]> where R := CoordinateRing(Pr6);
actct33 := func<C | Curve(Pr6, [ctPL33(e) : e in DefiningEquations(C)])>;
permct33 := [Position(C1s, actct33(C)) : C in C1s]
 cat [#C1s+Position(C2s, actct33(C)) : C in C2s]
 cat [#C1s+#C2s+Position(C3s, actct33(C)) : C in C3s]
 cat [#Cs+Position(pts, Pr6![ctL33(a) : a in Eltseq(pt)]) : pt in pts];
GctS := Matrix(Integers(), [Eltseq(actperm33(Pic.j, permct33)) : j in [1..64]]);
assert GccS*pmPic*Transpose(GccS) eq pmPic;
assert GctS*pmPic*Transpose(GctS) eq pmPic;

// Pullback/pushforward identities from the K_c block give the exact 20x20 action.
TmpCC := MatKtoS*GccS*MatStoK;
TmpCT := MatKtoS*GctS*MatStoK;
assert forall{x : x in Eltseq(TmpCC) | x mod 2 eq 0};
assert forall{x : x in Eltseq(TmpCT) | x mod 2 eq 0};
GccK := Matrix(Integers(),20,20,[ExactQuotient(x,2) : x in Eltseq(TmpCC)]);
GctK := Matrix(Integers(),20,20,[ExactQuotient(x,2) : x in Eltseq(TmpCT)]);
I20:=IdentityMatrix(Integers(),20);
assert GccK*pmPicK*Transpose(GccK) eq pmPicK;
assert GctK*pmPicK*Transpose(GctK) eq pmPicK;
assert GccK^2 eq I20 and GctK^2 eq I20 and GccK*GctK eq GctK*GccK;
assert GccK*MatKtoS eq MatKtoS*GccS;
assert GctK*MatKtoS eq MatKtoS*GctS;

D,_,V := SmithForm(pmPicK);
diag:=[Abs(Integers()!D[j,j]):j in [1..20]];
pos:=[j:j in [1..20]|diag[j] gt 1]; mods:=[diag[j]:j in pos];
assert mods eq [4,8];
Vin:=V^-1;
Bcc:=Vin*Transpose(GccK^-1)*V;
Bct:=Vin*Transpose(GctK^-1)*V;
Pinv:=ChangeRing(pmPicK,Rationals())^-1;
Vinq:=ChangeRing(Vin,Rationals()); B8:=8*(Vinq*Pinv*Transpose(Vinq));
for r in pos do for c in pos do assert Denominator(B8[r,c]) eq 1; end for; end for;
printf "STAGE33_07_KC_DISC_BEGIN\n";
printf "MODS=%o\n",mods; printf "DET=%o\n",Determinant(pmPicK);
for a in [1..2] do
 printf "CC_ROW_%o=%o\n",a,[Integers()!Bcc[pos[a],pos[b]] mod mods[b]:b in [1..2]];
 printf "CT_ROW_%o=%o\n",a,[Integers()!Bct[pos[a],pos[b]] mod mods[b]:b in [1..2]];
 printf "B8_ROW_%o=%o\n",a,[Integers()!B8[pos[a],pos[b]] mod (a eq b select 16 else 8):b in [1..2]];
end for;
printf "STAGE33_07_KC_DISC_END\n";
'''
code='SetColumns(0);\nquick := true;\n'+core+'\n'+kcore+'\n'+extra
stdout,attempt=run_magma(code,300,'Stage33-07 Kc compact discriminant Magma')
(HERE/'kc-discriminant-compact-magma-stdout.txt').write_text(stdout,encoding='utf-8')
if 'STAGE33_07_KC_DISC_END' not in stdout or any(x in stdout for x in ('Runtime error','Internal error','Assertion failed')):
 print(stdout); raise SystemExit('Kc compact discriminant extraction failed')
def grab(name):
 m=re.search(rf'^{name}=(.+)$',stdout,re.M)
 if not m: raise SystemExit(f'missing {name}')
 return ast.literal_eval(m.group(1))
mods=[int(x) for x in grab('MODS')]
det=int(re.search(r'^DET=(-?\d+)$',stdout,re.M).group(1))
if mods!=[4,8] or abs(det)!=32: raise SystemExit('Kc discriminant regression')
cc=[grab('CC_ROW_1'),grab('CC_ROW_2')]; ct=[grab('CT_ROW_1'),grab('CT_ROW_2')]; b8=[grab('B8_ROW_1'),grab('B8_ROW_2')]
cc=[[int(x) for x in r] for r in cc]; ct=[[int(x) for x in r] for r in ct]; b8=[[int(x) for x in r] for r in b8]
def mul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(2))%mods[j] for j in range(2)] for i in range(2)]
I=[[1,0],[0,1]]
if mul(cc,cc)!=I or mul(ct,ct)!=I or mul(cc,ct)!=mul(ct,cc): raise SystemExit('Kc mixed V4 regression')
cert={
 'schema':'STAGE33_07_KC_DISCRIMINANT_COMPACT_V1',
 'source_locks':{'upstream_git_blob_sha1':blob,'submitted_code_sha256':hashlib.sha256(code.encode()).hexdigest(),'stage33_05_audit':'stages/stage33/33-05/audit.md'},
 'source_fetch_attempt':source_attempt,'magma_request_attempt':attempt,
 'picard_rank':20,'picard_determinant':det,'discriminant_moduli':mods,
 'picard_discriminant_group':'Z/4 direct_sum Z/8','cc_action_mixed_moduli':cc,'ct_action_mixed_moduli':ct,
 'discriminant_bilinear_numerator_over_8_reduced':b8,
 'audited_Kc_Br2_invariant_dimension_f2':2,
 'audited_Kc_HS_d2_kernel_dimension_f2':1,
 'audited_Kc_HS_d2_kernel_basis':['J2'],
 'audited_Kc_HS_d2_nonzero_class':'q1',
 'proposed_endpoint_secondary_bockstein_validated':False,
 'role':'HS_D2_REGRESSION_INPUT_ONLY','theorem_credit':False,'endpoint_credit':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'kc-discriminant-compact.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'mods':mods,'cc':cc,'ct':ct,'b8':b8,'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
