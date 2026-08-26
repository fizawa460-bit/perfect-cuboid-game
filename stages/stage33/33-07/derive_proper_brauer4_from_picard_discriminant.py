#!/usr/bin/env python3
"""Derive the proper geometric Br[4] Galois module from Picard discriminant data.

For the smooth simply-connected cuboid resolution, H^2 is a free unimodular
lattice. Pic(Sbar) is primitive of rank 64 and T=Pic^perp has rank 14. Hence
A_Pic and A_T are Galois-equivariantly anti-isometric. If A_Pic=(Z/4)^14,
then 4*T^*=T and

    Br(Sbar)[4] = Hom(T,Z/4) = T^*/4T^* = T^*/T = A_T.

Thus the exact mod-4 Galois action computed on the Picard discriminant is the
proper geometric Br[4] action. No semisimple l-adic inference is used.
"""

import hashlib
import json
import math
from pathlib import Path

import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_form

HERE=Path(__file__).resolve().parent
src=json.loads((HERE/'picard-gram-galois.json').read_text())
diag=[abs(int(x)) for x in src['picard_smith_diagonal']]
det_abs=abs(int(src['picard_determinant']))
rank=int(src['picard_rank'])
if rank!=64 or len(diag)!=64: raise SystemExit('Picard compact shape regression')
if math.prod(diag)!=det_abs: raise SystemExit('Smith determinant regression')
nontrivial=[d for d in diag if d>1]
expected=(diag.count(1)==50 and nontrivial==[4]*14 and det_abs==4**14)

cert={
 'schema':'STAGE33_07_PROPER_BRAUER4_FROM_PICARD_DISCRIMINANT_V2',
 'source_locks':{
  'picard_discriminant_galois_sha256':src['canonical_sha256'],
  'picard_rank':64,
  'proper_transcendental_rank':14,
  'unimodular_ambient_H2':'smooth simply-connected compact cuboid resolution; integral Poincare duality',
  'primitive_picard_embedding':'NS=H^(1,1) intersect H^2(Z) is primitive',
 },
 'picard_smith_diagonal':diag,
 'picard_discriminant_abs':det_abs,
 'picard_discriminant_power_of_two': (det_abs>0 and det_abs & (det_abs-1)==0),
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

if expected:
 MCC=sp.Matrix([[int(x)%4 for x in row] for row in src['cc_discriminant_action_14x14_mod4']])
 MCT=sp.Matrix([[int(x)%4 for x in row] for row in src['ct_discriminant_action_14x14_mod4']])
 if MCC.shape!=(14,14) or MCT.shape!=(14,14): raise SystemExit('compact Br4 action shape regression')
 I14=sp.eye(14)
 if any(int(x)%4 for x in (MCC*MCC-I14)): raise SystemExit('cc discriminant action not involutive mod4')
 if any(int(x)%4 for x in (MCT*MCT-I14)): raise SystemExit('ct discriminant action not involutive mod4')
 if any(int(x)%4 for x in (MCC*MCT-MCT*MCC)): raise SystemExit('discriminant V4 action not commuting mod4')

 # Fixed equations in column form: (M-I)^T x=0 mod 4 for cc and ct.
 C=(MCC-I14).T.col_join((MCT-I14).T)
 Cint=sp.Matrix([[int(x) for x in row] for row in C.tolist()])
 Csnf=smith_normal_form(Cint,domain=ZZ)
 cdiag=[abs(int(Csnf[i,i])) for i in range(min(Csnf.rows,Csnf.cols)) if Csnf[i,i]!=0]
 rankC=len(cdiag)
 log2_kernel=2*(14-rankC)+sum(int(math.log2(math.gcd(4,s))) for s in cdiag)
 fixed_mod2_dim=14-gf2_rank(Cint.tolist())
 # K=(Z/4)^a +(Z/2)^b: a+b=dim K[2], 2a+b=log2|K|.
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
