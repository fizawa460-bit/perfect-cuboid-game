#!/usr/bin/env python3
"""Derive the proper geometric Br[4] Galois module from the Picard discriminant.

The smooth cuboid resolution is simply connected, so H^2 is a free unimodular
lattice.  Pic(Sbar) is primitive of rank 64 and its orthogonal complement T has
rank 14.  For a primitive sublattice of a unimodular lattice, the discriminant
modules A_Pic and A_T are canonically anti-isometric and Galois-equivariant.

If the exact Picard Smith form is 1^50,4^14, then A_T=(Z/4)^14.  Since T has
rank 14 and |A_T|=4^14 with exponent 4, 4*T^*=T.  Hence

    Br(Sbar)[4] = Hom(T,Z/4) = T^*/4T^* = T^*/T = A_T,

so the full proper Br[4] Galois action is recovered from the Picard
discriminant action.  No semisimple l-adic approximation is used.
"""

import hashlib
import json
import math
from pathlib import Path

import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp, smith_normal_form

HERE=Path(__file__).resolve().parent
src=json.loads((HERE/'picard-gram-galois.json').read_text())
P=sp.Matrix(src['picard_gram_64x64'])
CC=sp.Matrix(src['cc_picard_action_64x64'])
CT=sp.Matrix(src['ct_picard_action_64x64'])
I64=sp.eye(64)
if P.shape!=(64,64) or CC.shape!=(64,64) or CT.shape!=(64,64): raise SystemExit('shape regression')
if P.rank()!=64: raise SystemExit('Picard Gram lost rank')
if CC*P*CC.T!=P or CT*P*CT.T!=P: raise SystemExit('Galois action does not preserve Picard pairing')
if CC*CC!=I64 or CT*CT!=I64 or CC*CT!=CT*CC: raise SystemExit('cc/ct V4 action regression')

D,S,T=smith_normal_decomp(P,domain=ZZ)
if D != S*P*T: raise SystemExit('Smith decomposition identity failed')
diag=[abs(int(D[i,i])) for i in range(64)]
det_abs=abs(int(P.det()))
if math.prod(diag)!=det_abs: raise SystemExit('Smith determinant regression')
nontrivial=[d for d in diag if d>1]
expected=(diag.count(1)==50 and nontrivial==[4]*14 and det_abs==4**14)

cert={
 'schema':'STAGE33_07_PROPER_BRAUER4_FROM_PICARD_DISCRIMINANT_V1',
 'source_locks':{
  'picard_gram_galois_sha256':src['canonical_sha256'],
  'picard_rank':64,
  'proper_transcendental_rank':14,
  'unimodular_ambient_H2':'smooth simply-connected compact cuboid resolution; integral Poincare duality',
  'primitive_picard_embedding':'NS=H^(1,1) intersect H^2(Z) is primitive',
 },
 'picard_smith_diagonal':diag,
 'picard_discriminant_abs':det_abs,
 'picard_discriminant_power_of_two': (det_abs & (det_abs-1)==0),
 'expected_1pow50_4pow14':expected,
 'brauer4_reconstruction_complete':False,
 'unit_status':'RUNNING_REPAIR',
 'unit_closed':False,
 'stage33_progress':'6/11',
 'stage33_08_released':False,
 'theorem_credit':False,
 'endpoint_credit':False,
 'perfect_cuboid_nonexistence_claim':False,
}

if expected:
 # Row quotient A_Pic = Z^64 / Z^64 P.  Since D=S*P*T and left
 # multiplication by S does not change the row lattice, y=x*T identifies
 # A_Pic with Z^64/Z^64 D.  For row Picard coordinates, the induced action
 # on dual parameters z is z -> z*G^{-T}; conjugate by T to Smith coords.
 Tin=T.inv()
 survivors=[i for i,d in enumerate(diag) if d==4]
 if len(survivors)!=14: raise SystemExit('survivor count regression')
 def disc_action(G):
  A=G.inv().T
  B=Tin*A*T
  if any(x.q!=1 for x in B): raise SystemExit('nonintegral discriminant action conjugate')
  M=sp.Matrix([[int(B[r,c])%4 for c in survivors] for r in survivors])
  return M
 MCC=disc_action(CC); MCT=disc_action(CT); I14=sp.eye(14)
 if any(int(x)%4 for x in (MCC*MCC-I14)): raise SystemExit('cc discriminant action not involutive mod4')
 if any(int(x)%4 for x in (MCT*MCT-I14)): raise SystemExit('ct discriminant action not involutive mod4')
 if any(int(x)%4 for x in (MCC*MCT-MCT*MCC)): raise SystemExit('discriminant V4 action not commuting mod4')

 def gf2_rank(rows):
  a=[[int(x)&1 for x in row] for row in rows]
  if not a:return 0
  r=0
  for c in range(len(a[0])):
   p=next((i for i in range(r,len(a)) if a[i][c]),None)
   if p is None:continue
   a[r],a[p]=a[p],a[r]
   for i in range(len(a)):
    if i!=r and a[i][c]: a[i]=[x^y for x,y in zip(a[i],a[r])]
   r+=1
  return r

 # Column form of fixed equations: (M-I)^T x=0 for cc and ct.
 C=(MCC-I14).T.col_join((MCT-I14).T)
 Cint=sp.Matrix([[int(x) for x in row] for row in C.tolist()])
 Csnf=smith_normal_form(Cint,domain=ZZ)
 cdiag=[abs(int(Csnf[i,i])) for i in range(min(Csnf.rows,Csnf.cols)) if Csnf[i,i]!=0]
 rankC=len(cdiag)
 log2_kernel=2*(14-rankC)+sum(int(math.log2(math.gcd(4,s))) for s in cdiag)
 rank_mod2=gf2_rank(Cint.tolist())
 fixed_mod2_dim=14-rank_mod2
 # If K ~= (Z/4)^a + (Z/2)^b, then a+b=dim K[2] and 2a+b=log2|K|.
 a=log2_kernel-fixed_mod2_dim
 b=2*fixed_mod2_dim-log2_kernel
 if a<0 or b<0 or a+b!=fixed_mod2_dim: raise SystemExit('fixed subgroup invariant-factor reconstruction failed')

 cert.update({
  'picard_discriminant_group':'(Z/4)^14',
  'transcendental_discriminant_group':'(Z/4)^14',
  'four_Tdual_equals_T':True,
  'proper_geometric_Br4_group':'(Z/4)^14',
  'proper_geometric_Br2_group':'(Z/2)^14',
  'brauer4_identified_with_transcendental_discriminant_module':True,
  'galois_action_factors_through_picard_V4_on_Br4':True,
  'br4_cc_action_14x14_mod4':MCC.tolist(),
  'br4_ct_action_14x14_mod4':MCT.tolist(),
  'br4_fixed_equation_integer_smith_nonzero_diagonal':cdiag,
  'proper_Br2_GQ_invariant_dimension_f2':fixed_mod2_dim,
  'proper_Br4_GQ_invariant_group':f'(Z/4)^{a} direct_sum (Z/2)^{b}',
  'proper_Br4_GQ_invariant_order_log2':log2_kernel,
  'proper_Br4_GQ_invariant_order4_rank':a,
  'proper_Br4_GQ_invariant_order2_rank':b,
  'brauer4_reconstruction_complete':True,
  'next_residual_kernel':'R33-BR2A-TWO-PRIMARY-LOCALIZATION-TORSOR-AND-HS-D2-USING-EXACT-BR4-V4-MODULE',
  'next_exact_leaf':'L33-07-COMPUTE-RELATIVE-LOCALIZATION-CONNECTING-MAP-AND-HS-D2-IN-BR4-V4-COORDINATES',
 })
else:
 cert.update({
  'new_residual_kernel':'R33-BR2A-PICARD-DISCRIMINANT-NOT-4POWER-FREE-RANK14',
  'next_exact_leaf':'L33-07-RECONSTRUCT-TWO-ADIC-TRANSCENDENTAL-LATTICE-BEYOND-DISCRIMINANT',
 })

raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'proper-brauer4-picard-discriminant.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({
 'success':True,
 'picard_discriminant_abs':det_abs,
 'nontrivial_smith':nontrivial,
 'brauer4_reconstruction_complete':cert['brauer4_reconstruction_complete'],
 'proper_Br2_GQ_invariant_dimension_f2':cert.get('proper_Br2_GQ_invariant_dimension_f2'),
 'proper_Br4_GQ_invariant_group':cert.get('proper_Br4_GQ_invariant_group'),
 'next':cert.get('next_exact_leaf'),
 'certificate_sha256':cert['canonical_sha256'],
},indent=2,sort_keys=True))
