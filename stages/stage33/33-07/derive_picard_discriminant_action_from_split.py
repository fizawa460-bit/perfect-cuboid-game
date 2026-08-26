#!/usr/bin/env python3
"""Derive the exact mixed-modulus Picard discriminant V4 action.

Consumes three bounded extraction certificates (Gram, cc, ct).  All Smith
reduction and quotient arithmetic is performed locally with exact integers.
For a primitive Picard lattice in unimodular H^2, the transcendental
discriminant module is Galois-equivariantly anti-isometric, so this is also the
exact cc/ct action on A_T up to the canonical anti-isometry.
"""
import hashlib, json
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp

HERE=Path(__file__).resolve().parent
p=json.loads((HERE/'picard-gram-rows.json').read_text())
cc=json.loads((HERE/'picard-action-cc.json').read_text())
ct=json.loads((HERE/'picard-action-ct.json').read_text())
P=sp.Matrix(p['picard_gram_64x64'])
Gcc=sp.Matrix(cc['picard_action_64x64'])
Gct=sp.Matrix(ct['picard_action_64x64'])
I=sp.eye(64)
if P.shape!=(64,64) or Gcc.shape!=(64,64) or Gct.shape!=(64,64): raise SystemExit('shape regression')
if P.rank()!=64: raise SystemExit('Picard Gram rank regression')
if Gcc*P*Gcc.T!=P or Gct*P*Gct.T!=P: raise SystemExit('Picard action does not preserve pairing')
if Gcc*Gcc!=I or Gct*Gct!=I or Gcc*Gct!=Gct*Gcc: raise SystemExit('cc/ct V4 regression')

D,S,T=smith_normal_decomp(P,domain=ZZ)
if D != S*P*T: raise SystemExit('Smith decomposition identity failed')
diag=[abs(int(D[i,i])) for i in range(64)]
mods=[d for d in diag if d>1]
pos=[i for i,d in enumerate(diag) if d>1]
if mods != [2]*4+[4]*6+[8]*4 or len(pos)!=14: raise SystemExit(f'endpoint Smith regression {mods}')
if abs(int(P.det())) != 2**28: raise SystemExit('endpoint determinant regression')
Tin=T.inv()

def induced(G):
    # Row quotient A_Pic=Z^64/(Z^64 P).  Smith coordinates are y=z*T.
    # For row coordinates z on the dual quotient, G acts by G^{-T}.
    B=Tin*G.inv().T*T
    if any(sp.Rational(x).q!=1 for x in B): raise SystemExit('nonintegral Smith-conjugated action')
    B=sp.Matrix([[int(B[i,j]) for j in range(64)] for i in range(64)])
    M=[[int(B[pos[i],pos[j]])%mods[j] for j in range(14)] for i in range(14)]
    return M
Mcc=induced(Gcc); Mct=induced(Gct)

def well_defined(M):
    return all((mods[i]*M[i][j])%mods[j]==0 for i in range(14) for j in range(14))
def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(14))%mods[j] for j in range(14)] for i in range(14)]
def ident(): return [[(1 if i==j else 0)%mods[j] for j in range(14)] for i in range(14)]
if not well_defined(Mcc) or not well_defined(Mct): raise SystemExit('mixed action not well-defined')
if mul(Mcc,Mcc)!=ident() or mul(Mct,Mct)!=ident() or mul(Mcc,Mct)!=mul(Mct,Mcc): raise SystemExit('mixed V4 relation failed')

cert={
 'schema':'STAGE33_07_PICARD_DISCRIMINANT_V4_ACTION_SPLIT_V1',
 'source_locks':{
  'picard_gram_sha256':p['canonical_sha256'],
  'picard_cc_action_sha256':cc['canonical_sha256'],
  'picard_ct_action_sha256':ct['canonical_sha256'],
  'upstream_git_blob_sha1':p['upstream_git_blob_sha1'],
 },
 'picard_rank':64,
 'picard_determinant':int(P.det()),
 'discriminant_moduli':mods,
 'picard_discriminant_group':'(Z/2)^4 direct_sum (Z/4)^6 direct_sum (Z/8)^4',
 'cc_action_mixed_moduli':Mcc,
 'ct_action_mixed_moduli':Mct,
 'mixed_action_well_defined':True,
 'cc_ct_involutions_and_commute':True,
 'transcendental_discriminant_action_same_up_to_anti_isometry':True,
 'actual_index512_k3_glue_identified':False,
 'next_exact_leaf':'L33-07-ENUMERATE-COORDINATE-SIGN-STABLE-INDEX512-ISOTROPIC-GLUE-MATCHING-THIS-DISCRIMINANT-V4-MODULE',
 'unit_status':'RUNNING_REPAIR',
 'stage33_progress':'6/11',
 'stage33_08_released':False,
 'theorem_credit':False,
 'endpoint_credit':False,
 'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'picard-discriminant-v4-action.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'mods':mods,'v4_action_exact':True,'next':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
