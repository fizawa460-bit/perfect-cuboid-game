#!/usr/bin/env python3
"""Extract the seven coordinate-sign actions on the endpoint discriminant module.

The pinned Testa--Stoll model has seven coordinate sign involutions on
(a1,a2,a3,b1,b2,b3,c).  We descend each to Pic(S), transport it through the
same Smith basis as the retained endpoint Picard discriminant calculation, and
use the standard anti-isometry A_Pic -> A_T: the underlying mixed-modulus
matrix is unchanged while the quadratic form changes sign.

The retained cc/ct matrices are recomputed in the same run and required to
match picard-discriminant-compact.json literally, which locks the Smith-coordinate
convention rather than merely its conjugacy class.
"""
import ast,hashlib,json,pathlib,re
from stoll_cuboid_source import load_pinned_source,run_magma
HERE=pathlib.Path(__file__).resolve().parent
TGT=json.loads((HERE/'picard-discriminant-compact.json').read_text())
TGT_LOCK='4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0'
if TGT['canonical_sha256']!=TGT_LOCK:raise SystemExit('endpoint compact lock moved')
text,core,blob,source_attempt=load_pinned_source()
extra=r'''
actperm := func<g, perm | qPic(Big![e[perm[j]] : j in [1..#e]]) where e := Eltseq(g @@ qPic)>;
act := func<sch, subs | Curve(Pr6, [Evaluate(e, subs) : e in DefiningEquations(sch)])>;
function actpt2(pt, subs)
  i0 := 1; while pt[i0] eq 0 do i0 +:= 1; end while;
  pteqns := [Pr6.j*pt[i0] - Pr6.i0*pt[j] : j in [1..7] | j ne i0];
  return Rep(Points(Scheme(Pr6, [Evaluate(e, subs) : e in pteqns])));
end function;
signsubs := [
 [-a1,a2,a3,b1,b2,b3,c], [a1,-a2,a3,b1,b2,b3,c], [a1,a2,-a3,b1,b2,b3,c],
 [a1,a2,a3,-b1,b2,b3,c], [a1,a2,a3,b1,-b2,b3,c], [a1,a2,a3,b1,b2,-b3,c],
 [a1,a2,a3,b1,b2,b3,-c]
];
signperms := [[Position(C1s,act(C,su)):C in C1s]
 cat [#C1s+Position(C2s,act(C,su)):C in C2s]
 cat [#C1s+#C2s+Position(C3s,act(C,su)):C in C3s]
 cat [#Cs+Position(pts,actpt2(pt,su)):pt in pts] : su in signsubs];
signPic := [Matrix(Integers(),[Eltseq(actperm(Pic.j,p)):j in [1..64]]) : p in signperms];
assert forall{g:g in signPic|g*pmPic*Transpose(g) eq pmPic and g^2 eq IdentityMatrix(Integers(),64)};
assert forall{i:i in [1..7]|forall{j:j in [1..7]|signPic[i]*signPic[j] eq signPic[j]*signPic[i]}};
prodsg:=IdentityMatrix(Integers(),64); for g in signPic do prodsg *:= g; end for; assert prodsg eq IdentityMatrix(Integers(),64);
// Recompute cc/ct in the same Smith run as a literal coordinate-convention lock.
ccL := hom<L -> L | -i>;
ccPL := hom<R -> R | ccL*Bang(L,R), [R.j : j in [1..7]]> where R := CoordinateRing(Pr6);
actcc := func<C | Curve(Pr6, [ccPL(e) : e in DefiningEquations(C)])>;
permcc := [Position(C1s,actcc(C)):C in C1s]
 cat [#C1s+Position(C2s,actcc(C)):C in C2s]
 cat [#C1s+#C2s+Position(C3s,actcc(C)):C in C3s]
 cat [#Cs+Position(pts,Pr6![ccL(a):a in Eltseq(pt)]):pt in pts];
ccPic:=Matrix(Integers(),[Eltseq(actperm(Pic.j,permcc)):j in [1..64]]);
ctL:=hom<L -> L | hom<GroundField(L) -> L | -s>, i>;
ctPL:=hom<R -> R | ctL*Bang(L,R), [R.j:j in [1..7]]> where R:=CoordinateRing(Pr6);
actct:=func<C | Curve(Pr6,[ctPL(e):e in DefiningEquations(C)])>;
permct := [Position(C1s,actct(C)):C in C1s]
 cat [#C1s+Position(C2s,actct(C)):C in C2s]
 cat [#C1s+#C2s+Position(C3s,actct(C)):C in C3s]
 cat [#Cs+Position(pts,Pr6![ctL(a):a in Eltseq(pt)]):pt in pts];
ctPic:=Matrix(Integers(),[Eltseq(actperm(Pic.j,permct)):j in [1..64]]);
Sm,U,V:=SmithForm(pmPic); diag:=[Abs(Integers()!Sm[j,j]):j in [1..64]];
nz:=[j:j in [1..64]|diag[j] gt 1]; mods:=[diag[j]:j in nz];
function discmat(g)
 B:=V^-1*Transpose(g)*V;
 return [[Integers()!(B[nz[r],nz[c]] mod mods[c]):c in [1..#nz]]:r in [1..#nz]];
end function;
sgdisc:=[discmat(g):g in signPic]; ccdisc:=discmat(ccPic); ctdisc:=discmat(ctPic);
printf "STAGE33_07_SIGN_BEGIN\n";
printf "MODS=%o\n",mods; printf "CC=%o\n",ccdisc; printf "CT=%o\n",ctdisc; printf "SIGNS=%o\n",sgdisc;
printf "STAGE33_07_SIGN_END\n";
'''
code='SetColumns(0);\nquick := true;\n'+core+'\n'+extra
stdout,attempt=run_magma(code,240,'Stage33-07 endpoint coordinate-sign discriminant Magma')
if 'STAGE33_07_SIGN_END' not in stdout or any(x in stdout for x in ('Runtime error','Internal error','Assertion failed')):
    print(stdout);raise SystemExit('endpoint coordinate-sign extraction failed')
def seq(name):
    m=re.search(rf'^{name}=(.+)$',stdout,re.M)
    if not m:raise SystemExit('missing '+name)
    return ast.literal_eval(m.group(1))
mods=seq('MODS');cc=seq('CC');ct=seq('CT');signs=seq('SIGNS')
if mods!=[2]*4+[4]*6+[8]*4:raise SystemExit('endpoint moduli regression')
if cc!=TGT['cc_action_mixed_moduli'] or ct!=TGT['ct_action_mixed_moduli']:
    raise SystemExit('Smith-coordinate convention moved: cc/ct literal mismatch')
if len(signs)!=7 or any(len(M)!=14 or any(len(r)!=14 for r in M) for M in signs):raise SystemExit('sign action shape regression')
def compose(A,B):return [[sum(int(A[i][k])*int(B[k][j]) for k in range(14))%mods[j] for j in range(14)] for i in range(14)]
I=[[1 if i==j else 0 for j in range(14)] for i in range(14)]
def well(M):return all((mods[i]*int(M[i][j]))%mods[j]==0 for i in range(14) for j in range(14))
if any(not well(M) or compose(M,M)!=I for M in signs):raise SystemExit('sign action hom/involution regression')
if any(compose(signs[i],signs[j])!=compose(signs[j],signs[i]) for i in range(7) for j in range(7)):raise SystemExit('sign actions failed commute')
prod=I
for M in signs:prod=compose(prod,M)
if prod!=I:raise SystemExit('projective seven-sign relation failed')
if any(compose(M,cc)!=compose(cc,M) or compose(M,ct)!=compose(ct,M) for M in signs):raise SystemExit('rational sign/Galois commutation failed')
cert={'schema':'STAGE33_07_ENDPOINT_COORDINATE_SIGN_DISCRIMINANT_ACTIONS_V1','source_locks':{'testa_stoll_git_blob_sha1':blob,'endpoint_picard_discriminant_sha256':TGT_LOCK},'coordinate_order':['a1','a2','a3','b1','b2','b3','c'],'discriminant_moduli':mods,'sign_actions_mixed_moduli':signs,'cc_action_mixed_moduli':cc,'ct_action_mixed_moduli':ct,'cc_ct_literal_coordinate_lock_match':True,'seven_sign_involutions_commute':True,'seven_sign_product_identity':True,'signs_commute_with_cc_ct':True,'picard_to_transcendental_rule':'same mixed-modulus action matrix under the retained anti-isometry; q_T=-q_P','submitted_code_sha256':hashlib.sha256(code.encode()).hexdigest(),'source_fetch_attempt':source_attempt,'magma_request_attempt':attempt,'actual_index512_glue_identified':False,'stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'endpoint-coordinate-sign-discriminant-actions.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'coordinate_sign_count':7,'cc_ct_literal_lock_match':True,'canonical_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
