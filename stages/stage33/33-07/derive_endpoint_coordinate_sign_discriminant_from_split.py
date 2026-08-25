#!/usr/bin/env python3
"""Derive endpoint discriminant q, cc, ct and seven coordinate signs from split rows.

All ten expensive objects (Gram, cc, ct, seven signs) are extracted separately
from the same pinned Testa--Stoll source.  This script performs the Smith
reduction locally and transports every action through one common Smith basis.
No action matrix from a different Smith convention is mixed in.
"""
import hashlib,json
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp

HERE=Path(__file__).resolve().parent
TGT=json.loads((HERE/'picard-discriminant-compact.json').read_text())
TGT_LOCK='4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0'
if TGT.get('canonical_sha256')!=TGT_LOCK:
    raise SystemExit('retained endpoint compact lock moved')
Psrc=json.loads((HERE/'picard-gram-rows.json').read_text())
ccsrc=json.loads((HERE/'picard-action-cc.json').read_text())
ctsrc=json.loads((HERE/'picard-action-ct.json').read_text())
NAMES=('a1','a2','a3','b1','b2','b3','c')
ssrc=[json.loads((HERE/f'picard-action-sign-{n}.json').read_text()) for n in NAMES]
blob=Psrc['upstream_git_blob_sha1']
if ccsrc['upstream_git_blob_sha1']!=blob or ctsrc['upstream_git_blob_sha1']!=blob or any(x['upstream_git_blob_sha1']!=blob for x in ssrc):
    raise SystemExit('split source blob mismatch')
if any(x.get('coordinate')!=n for x,n in zip(ssrc,NAMES)):
    raise SystemExit('coordinate sign row ordering regression')

P=sp.Matrix(Psrc['picard_gram_64x64'])
Gcc=sp.Matrix(ccsrc['picard_action_64x64'])
Gct=sp.Matrix(ctsrc['picard_action_64x64'])
Gs=[sp.Matrix(x['picard_action_64x64']) for x in ssrc]
I64=sp.eye(64)
if P.shape!=(64,64) or any(G.shape!=(64,64) for G in [Gcc,Gct]+Gs):
    raise SystemExit('split matrix shape regression')
if P.rank()!=64 or abs(int(P.det()))!=2**28:
    raise SystemExit('Picard Gram rank/determinant regression')
for name,G in [('cc',Gcc),('ct',Gct)]+list(zip(NAMES,Gs)):
    if G*P*G.T!=P or G*G!=I64:
        raise SystemExit(f'Picard action regression {name}')
if Gcc*Gct!=Gct*Gcc:
    raise SystemExit('Picard cc/ct failed commute')
if any(G*Gcc!=Gcc*G or G*Gct!=Gct*G for G in Gs):
    raise SystemExit('Picard coordinate sign/Galois commutation failed')
if any(Gs[i]*Gs[j]!=Gs[j]*Gs[i] for i in range(7) for j in range(7)):
    raise SystemExit('Picard coordinate signs failed commute')
prod=I64
for G in Gs:
    prod=prod*G
if prod!=I64:
    raise SystemExit('projective seven-coordinate-sign relation failed on Picard')

D,S,T=smith_normal_decomp(P,domain=ZZ)
if S*P*T!=D:
    raise SystemExit('Smith decomposition identity failed')
diag=[abs(int(D[i,i])) for i in range(64)]
mods=[d for d in diag if d>1]
pos=[i for i,d in enumerate(diag) if d>1]
if mods!=[2]*4+[4]*6+[8]*4 or len(pos)!=14:
    raise SystemExit(f'endpoint Smith regression {mods}')
Tin=T.inv()
if any(sp.Rational(x).q!=1 for x in Tin):
    raise SystemExit('Smith right transform inverse lost integrality')

def induced(G):
    # Row discriminant quotient A_Pic = Z^64 / (Z^64 P), Smith coordinates y=z*T.
    B=Tin*G.inv().T*T
    if any(sp.Rational(x).q!=1 for x in B):
        raise SystemExit('nonintegral Smith-conjugated action')
    M=[[int(B[pos[i],pos[j]])%mods[j] for j in range(14)] for i in range(14)]
    return M

# Discriminant bilinear/quadratic form in this same Smith basis.
Pinv=P.inv()
Bd=Tin*Pinv*Tin.T
B8=8*Bd
for i in pos:
    for j in pos:
        if sp.Rational(B8[i,j]).q!=1:
            raise SystemExit('split B8 denominator regression')
b8=[]
for a,i in enumerate(pos):
    row=[]
    for b,j in enumerate(pos):
        m=16 if a==b else 8
        row.append(int(B8[i,j])%m)
    b8.append(row)

cc=induced(Gcc);ct=induced(Gct);signs=[induced(G) for G in Gs]

def well(M):
    return all((mods[i]*int(M[i][j]))%mods[j]==0 for i in range(14) for j in range(14))
def comp(A,B):
    return [[sum(int(A[i][k])*int(B[k][j]) for k in range(14))%mods[j] for j in range(14)] for i in range(14)]
def ident():
    return [[(1 if i==j else 0)%mods[j] for j in range(14)] for i in range(14)]
I=ident()
def transform_form(M):
    return [[sum(int(M[i][a])*b8[a][b]*int(M[j][b]) for a in range(14) for b in range(14)) for j in range(14)] for i in range(14)]
def preserves_q(M):
    C=transform_form(M)
    return all((C[i][j]-b8[i][j])%(16 if i==j else 8)==0 for i in range(14) for j in range(14))
for name,M in [('cc',cc),('ct',ct)]+list(zip(NAMES,signs)):
    if not well(M) or comp(M,M)!=I or not preserves_q(M):
        raise SystemExit(f'finite q/action regression {name}')
if comp(cc,ct)!=comp(ct,cc):
    raise SystemExit('finite cc/ct failed commute')
if any(comp(M,cc)!=comp(cc,M) or comp(M,ct)!=comp(ct,M) for M in signs):
    raise SystemExit('finite coordinate sign/Galois commutation failed')
if any(comp(signs[i],signs[j])!=comp(signs[j],signs[i]) for i in range(7) for j in range(7)):
    raise SystemExit('finite coordinate signs failed commute')
prod=I
for M in signs:
    prod=comp(prod,M)
if prod!=I:
    raise SystemExit('finite seven-sign product relation failed')
if any((b8[i][j]-b8[j][i])%(16 if i==j else 8) for i in range(14) for j in range(14)):
    raise SystemExit('split discriminant form symmetry regression')

# Basis-independent regressions against the retained compact endpoint package.
# We deliberately do not demand literal matrices because SymPy and Magma can
# choose different Smith bases.  The exact same pinned Picard lattice/action is
# the load-bearing source; these checks catch gross convention regressions.
def fixed_log2(M,power):
    # brute force is impossible on the whole group; compute kernel order of M-I
    # on the power-torsion subgroup via a small presentation Smith calculation.
    # Enumerate only generators of G[2^power] and compute image size by row-space
    # over the mixed cyclic target through exact finite closure.
    lim=[min(m,2**power) for m in mods]
    gens=[]
    for i,(m,l) in enumerate(zip(mods,lim)):
        step=m//l
        v=[0]*14;v[i]=step;gens.append(v)
    dif=[]
    for v in gens:
        y=[sum(v[i]*int(M[i][j]) for i in range(14))%mods[j] for j in range(14)]
        dif.append([(y[j]-v[j])%mods[j] for j in range(14)])
    # Exact image subgroup by closure; at most 2^14 elements for the 2-torsion
    # and still small for these fixed-action regressions after incremental sets.
    image={(0,)*14}
    for v,l in zip(dif,lim):
        old=list(image);nxt=set(image);cur=(0,)*14
        for a in range(1,l):
            cur=tuple((cur[j]+v[j])%mods[j] for j in range(14))
            for x in old:nxt.add(tuple((x[j]+cur[j])%mods[j] for j in range(14)))
        image=nxt
    import math
    domain=1
    for l in lim:domain*=l
    return (domain//len(image)).bit_length()-1
# Retained known fixed logs: cc=(10,15,18), ct=(13,19,22) for [2],[4],all.
if fixed_log2(cc,1)!=10 or fixed_log2(ct,1)!=13:
    raise SystemExit('split endpoint fixed-Q2 regression against retained package')

cert={
 'schema':'STAGE33_07_ENDPOINT_COORDINATE_SIGN_DISCRIMINANT_ACTIONS_SPLIT_V2',
 'source_locks':{
   'testa_stoll_git_blob_sha1':blob,
   'retained_endpoint_compact_sha256':TGT_LOCK,
   'picard_gram_rows_sha256':Psrc['canonical_sha256'],
   'picard_cc_rows_sha256':ccsrc['canonical_sha256'],
   'picard_ct_rows_sha256':ctsrc['canonical_sha256'],
   'picard_sign_rows_sha256':{n:x['canonical_sha256'] for n,x in zip(NAMES,ssrc)},
 },
 'coordinate_order':list(NAMES),
 'discriminant_moduli':mods,
 'picard_determinant':int(P.det()),
 'discriminant_bilinear_numerator_over_8_reduced':b8,
 'quadratic_value_convention':'q_Pic(x)=x*B8*x^T/8 mod 2Z; use -B8 for T, which has the same isometry group/action matrices',
 'cc_action_mixed_moduli':cc,
 'ct_action_mixed_moduli':ct,
 'sign_actions_mixed_moduli':signs,
 'all_actions_well_defined_involutions_and_q_isometries':True,
 'seven_sign_involutions_commute':True,
 'seven_sign_product_identity':True,
 'signs_commute_with_cc_ct':True,
 'split_smith_basis_literal_match_to_retained_compact_not_assumed':True,
 'split_cc_fixed_Q2_log2':10,
 'split_ct_fixed_Q2_log2':13,
 'picard_to_transcendental_rule':'same finite action matrices under anti-isometry; T quadratic form is negative Picard form',
 'actual_index512_glue_identified':False,
 'stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'endpoint-coordinate-sign-discriminant-actions-split.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'coordinate_sign_count':7,'mods':mods,'cc_fix2':10,'ct_fix2':13,'canonical_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
