#!/usr/bin/env python3
"""Verify V91C1N minimal coordinate discriminator on the proper14 joint-V4 fixed subspace."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
D=Path(__file__).resolve().parent
BR=D.parent/'33-07'/'proper-brauer2-from-discriminant.json'
C=D/'e3-v91c1n-minimal-joint-v4-fixed-coordinate-discriminator.json'
BR_SHA='c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf'
C_SHA='e4e35e567ce160150f21be77f0e157937aa800ffac84365020b4fcf331504b7c'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text(encoding='utf-8')); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o
def rref(rows,n):
 a=[[x&1 for x in r] for r in rows if any(x&1 for x in r)]; piv=[]; rr=0
 for c in range(n):
  p=next((i for i in range(rr,len(a)) if a[i][c]),None)
  if p is None: continue
  a[rr],a[p]=a[p],a[rr]
  for i in range(len(a)):
   if i!=rr and a[i][c]: a[i]=[x^y for x,y in zip(a[i],a[rr])]
  piv.append(c); rr+=1
  if rr==len(a): break
 return a[:rr],piv
def nullspace(eq,n):
 r,piv=rref(eq,n); free=[j for j in range(n) if j not in piv]; out=[]
 for f in free:
  v=[0]*n; v[f]=1
  for row,p in zip(r,piv): v[p]=row[f]
  out.append(v)
 return out
br=load(BR,BR_SHA); c=load(C,C_SHA); n=14
G=br['proper_Br2_cc_action_f2']; H=br['proper_Br2_ct_action_f2']
eq=[]
for M in (G,H):
 for j in range(n): eq.append([(M[i][j]^(1 if i==j else 0)) for i in range(n)])
B=nullspace(eq,n)
assert len(B)==10==br['proper_Br2_joint_v4_fixed_dimension_f2']
_,piv=rref(B,n); sel=[p+1 for p in piv]
assert sel==[1,2,3,4,5,6,7,8,9,11]
R=[[row[p] for p in piv] for row in B]
assert len(rref(R,10)[1])==10
e3=[0]*14; e3[2]=1; e3[4]=1
bits=[e3[p] for p in piv]
assert bits==[0,0,1,0,1,0,0,0,0,0]
assert c['coordinate_discriminator']['positions_one_based']==sel
assert c['coordinate_discriminator']['restriction_rank_f2']==10
assert c['coordinate_discriminator']['injective_on_joint_v4_fixed_subspace'] is True
assert c['coordinate_discriminator']['no_nine_coordinate_projection_can_be_injective'] is True
assert c['e3_target']['proper14_mask_decimal']==20
assert c['e3_target']['discriminator_bits']==bits
assert c['exact_consequence']['source_bound_a2_02_discriminator_bits_materialized'] is False
assert c['exact_consequence']['a2_02_marked_brauer_image_computed'] is False
assert c['exact_consequence']['a2_02_marked_brauer_image_equal_mask20'] is False
assert c['entry_chain']['audit_pass_credit_for_batch_candidates'] is False
assert c['credit_firewall']['stage33_progress']=='6/11'
assert c['credit_firewall']['merge_allowed'] is False
print(json.dumps({'success':True,'marker':'V91C1N_MINIMAL_FIXED_SUBSPACE_COORDINATE_DISCRIMINATOR','certificate_sha256':C_SHA,'positions_one_based':sel,'e3_bits':bits,'source_bits_materialized':False},sort_keys=True))
