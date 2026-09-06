#!/usr/bin/env python3
"""Diagnose a minimal proper14 coordinate projection separating the 10D joint-V4 fixed subspace."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
D=Path(__file__).resolve().parent; BR=D.parent/'33-07'/'proper-brauer2-from-discriminant.json'
BR_SHA='c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b); return o
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
def transpose(a): return [list(x) for x in zip(*a)]
br=load(BR,BR_SHA); G=br['proper_Br2_cc_action_f2']; H=br['proper_Br2_ct_action_f2']; n=14
# Row-vector fixed equations v*(g-I)=0: one equation per output coordinate j.
eq=[]
for M in (G,H):
 for j in range(n): eq.append([(M[i][j]^(1 if i==j else 0)) for i in range(n)])
B=nullspace(eq,n); assert len(B)==10==br['proper_Br2_joint_v4_fixed_dimension_f2']
# Select coordinate projections whose restrictions to the fixed-space basis have rank 10.
# The 14 coordinate functionals are columns of B; pivot columns of B are a minimal separating set.
_,piv=rref(B,n); assert len(piv)==10
sel=[p+1 for p in piv]
# Verify restriction B[:,sel] invertible.
R=[[row[p] for p in piv] for row in B]; assert len(rref(R,10)[1])==10
e3=[0]*14; e3[2]=1; e3[4]=1
assert all(sum(e3[i]*G[i][j] for i in range(n))%2==e3[j] for j in range(n))
assert all(sum(e3[i]*H[i][j] for i in range(n))%2==e3[j] for j in range(n))
print(json.dumps({'success':True,'joint_fixed_dimension_f2':10,'fixed_basis_f2':B,'minimal_coordinate_discriminator_positions_one_based':sel,'e3_discriminator_bits':[e3[p] for p in piv],'e3_mask_decimal':20},sort_keys=True))
