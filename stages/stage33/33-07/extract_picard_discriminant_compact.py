#!/usr/bin/env python3
"""Extract the endpoint Picard discriminant form and V4 action compactly.

The expensive Smith transformation is done inside Magma.  Only the 14
nontrivial Smith coordinates, their cc/ct action, and the discriminant bilinear
form are emitted.  This avoids the slow 64x64 SymPy transformation path.
"""
import ast
import hashlib
import json
import pathlib
import re
from stoll_cuboid_source import load_pinned_source, run_magma

HERE = pathlib.Path(__file__).resolve().parent
_, core, blob, source_attempt = load_pinned_source()
extra = r'''
actperm := func<g, perm | qPic(Big![e[perm[j]] : j in [1..#e]]) where e := Eltseq(g @@ qPic)>;

ccL := hom<L -> L | -i>;
ccPL := hom<R -> R | ccL*Bang(L,R), [R.j : j in [1..7]]> where R := CoordinateRing(Pr6);
actcc := func<C | Curve(Pr6, [ccPL(e) : e in DefiningEquations(C)])>;
permcc := [Position(C1s, actcc(C)) : C in C1s]
 cat [#C1s+Position(C2s, actcc(C)) : C in C2s]
 cat [#C1s+#C2s+Position(C3s, actcc(C)) : C in C3s]
 cat [#Cs+Position(pts, Pr6![ccL(a) : a in Eltseq(pt)]) : pt in pts];
Gcc := Matrix(Integers(), [Eltseq(actperm(Pic.j, permcc)) : j in [1..64]]);

ctL := hom<L -> L | hom<GroundField(L) -> L | -s>, i>;
ctPL := hom<R -> R | ctL*Bang(L,R), [R.j : j in [1..7]]> where R := CoordinateRing(Pr6);
actct := func<C | Curve(Pr6, [ctPL(e) : e in DefiningEquations(C)])>;
permct := [Position(C1s, actct(C)) : C in C1s]
 cat [#C1s+Position(C2s, actct(C)) : C in C2s]
 cat [#C1s+#C2s+Position(C3s, actct(C)) : C in C3s]
 cat [#Cs+Position(pts, Pr6![ctL(a) : a in Eltseq(pt)]) : pt in pts];
Gct := Matrix(Integers(), [Eltseq(actperm(Pic.j, permct)) : j in [1..64]]);

I64 := IdentityMatrix(Integers(),64);
assert Gcc*pmPic*Transpose(Gcc) eq pmPic;
assert Gct*pmPic*Transpose(Gct) eq pmPic;
assert Gcc^2 eq I64 and Gct^2 eq I64 and Gcc*Gct eq Gct*Gcc;

// Request only the right Smith transformation V: D = ? * pmPic * V.
D, _, V := SmithForm(pmPic);
diag := [Abs(Integers()!D[j,j]) : j in [1..64]];
pos := [j : j in [1..64] | diag[j] gt 1];
mods := [diag[j] : j in pos];
assert mods eq [2 : j in [1..4]] cat [4 : j in [1..6]] cat [8 : j in [1..4]];
Vin := V^-1;
Bcc := Vin * Transpose(Gcc^-1) * V;
Bct := Vin * Transpose(Gct^-1) * V;
assert IsIntegral(Bcc) and IsIntegral(Bct);

// Discriminant bilinear form in Smith quotient coordinates y=z*V.
Pinv := ChangeRing(pmPic,Rationals())^-1;
Vinq := ChangeRing(Vin,Rationals());
Bd := Vinq * Pinv * Transpose(Vinq);
B8 := 8*Bd;
for r in pos do
 for c in pos do
  assert Denominator(B8[r,c]) eq 1;
 end for;
end for;

printf "STAGE33_07_DISC_COMPACT_BEGIN\n";
printf "MODS=%o\n", mods;
printf "PIC_DET=%o\n", Determinant(pmPic);
for a in [1..#pos] do
 printf "CC_ROW_%o=%o\n",a,[Integers()!Bcc[pos[a],pos[b]] : b in [1..#pos]];
 printf "CT_ROW_%o=%o\n",a,[Integers()!Bct[pos[a],pos[b]] : b in [1..#pos]];
 printf "B8_ROW_%o=%o\n",a,[Integers()!B8[pos[a],pos[b]] : b in [1..#pos]];
end for;
printf "STAGE33_07_DISC_COMPACT_END\n";
'''
code = 'SetColumns(0);\nquick := true;\n' + core + '\n' + extra
stdout, attempt = run_magma(code, 240, 'Stage33-07 compact Picard discriminant Magma')
(HERE / 'picard-discriminant-compact-magma-stdout.txt').write_text(stdout, encoding='utf-8')
if 'STAGE33_07_DISC_COMPACT_END' not in stdout or any(x in stdout for x in ('Runtime error','Internal error','Assertion failed')):
    print(stdout)
    raise SystemExit('compact Picard discriminant extraction failed')

def grab(name):
    m = re.search(rf'^{name}=(.+)$', stdout, re.M)
    if not m:
        raise SystemExit(f'missing {name}')
    return ast.literal_eval(m.group(1))

mods = [int(x) for x in grab('MODS')]
det = int(re.search(r'^PIC_DET=(-?\d+)$', stdout, re.M).group(1))
if mods != [2]*4 + [4]*6 + [8]*4 or abs(det) != 2**28:
    raise SystemExit('endpoint discriminant regression')

cc=[]; ct=[]; b8=[]
for r in range(1,15):
    cc.append([int(x) for x in grab(f'CC_ROW_{r}')])
    ct.append([int(x) for x in grab(f'CT_ROW_{r}')])
    b8.append([int(x) for x in grab(f'B8_ROW_{r}')])
if any(len(row)!=14 for M in (cc,ct,b8) for row in M):
    raise SystemExit('compact row length regression')

# Reduce row-action matrices by target-coordinate moduli.
def red(M):
    return [[M[i][j] % mods[j] for j in range(14)] for i in range(14)]
cc=red(cc); ct=red(ct)

def well(M):
    return all((mods[i]*M[i][j]) % mods[j] == 0 for i in range(14) for j in range(14))
def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(14)) % mods[j] for j in range(14)] for i in range(14)]
I=[[1 if i==j else 0 for j in range(14)] for i in range(14)]
I=red(I)
if not well(cc) or not well(ct):
    raise SystemExit('mixed-modulus action not well-defined')
if mul(cc,cc)!=I or mul(ct,ct)!=I or mul(cc,ct)!=mul(ct,cc):
    raise SystemExit('mixed-modulus V4 relation failed')
if any(b8[i][j] != b8[j][i] for i in range(14) for j in range(14)):
    raise SystemExit('discriminant form lost symmetry')

# Preserve q modulo 2: off-diagonal numerator differences are mod 8,
# diagonal differences are mod 16 because q is valued in Q/2Z.
def transform_form(M):
    return [[sum(M[i][a]*b8[a][b]*M[j][b] for a in range(14) for b in range(14)) for j in range(14)] for i in range(14)]
for name,M in [('cc',cc),('ct',ct)]:
    C=transform_form(M)
    for i in range(14):
        for j in range(14):
            mod = 16 if i==j else 8
            if (C[i][j]-b8[i][j]) % mod:
                raise SystemExit(f'{name} does not preserve discriminant quadratic form at {i},{j}')

cert={
    'schema':'STAGE33_07_PICARD_DISCRIMINANT_COMPACT_V1',
    'source_locks':{
        'upstream_git_blob_sha1':blob,
        'submitted_code_sha256':hashlib.sha256(code.encode()).hexdigest(),
    },
    'source_fetch_attempt':source_attempt,
    'magma_request_attempt':attempt,
    'picard_rank':64,
    'picard_determinant':det,
    'discriminant_moduli':mods,
    'picard_discriminant_group':'(Z/2)^4 direct_sum (Z/4)^6 direct_sum (Z/8)^4',
    'cc_action_mixed_moduli':cc,
    'ct_action_mixed_moduli':ct,
    'discriminant_bilinear_numerator_over_8':b8,
    'quadratic_value_convention':'q(x)=x*B8*x^T/8 mod 2Z',
    'mixed_action_well_defined':True,
    'cc_ct_involutions_and_commute':True,
    'cc_ct_preserve_discriminant_quadratic_form':True,
    'transcendental_discriminant_form_is_negative_of_picard_form':True,
    'actual_index512_k3_glue_identified':False,
    'next_exact_leaf':'L33-07-MATCH-INDEX512-ISOTROPIC-GLUE-TO-EXACT-DISCRIMINANT-FORM-AND-V4-ACTION',
    'unit_status':'RUNNING_REPAIR',
    'stage33_progress':'6/11',
    'stage33_08_released':False,
    'theorem_credit':False,
    'endpoint_credit':False,
    'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode()
cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'picard-discriminant-compact.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({
    'success':True,
    'mods':mods,
    'quadratic_form_exact':True,
    'v4_action_exact':True,
    'next_exact_leaf':cert['next_exact_leaf'],
    'certificate_sha256':cert['canonical_sha256'],
},indent=2,sort_keys=True))
