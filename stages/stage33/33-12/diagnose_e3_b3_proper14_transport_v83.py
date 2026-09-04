#!/usr/bin/env python3
"""Exact bounded diagnostic: descend S=swap13*sign(a2) to proper14.

This computes the induced action on the ordered 14-dimensional 2-primary
Picard-discriminant basis used by the retained proper14 Brauer coordinates.
It then transports the exact B1 rank-one generator mask25 to the B3 route.
No B3 Cech/literal-geometric credit is granted by this diagnostic alone.
"""
from __future__ import annotations

import hashlib, json, runpy, sys
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
S07=HERE.parent/'33-07'; S09=HERE.parent/'33-09'
sys.path.insert(0,str(S07))
OLD=S07/'picard_base_rows_retained.py'
SIGN=S07/'picard_coordinate_sign_rows_retained.py'
BRIDGE=S09/'marked-picard-basis-bridge-certified.json'
ADJ=HERE/'j2-picard-adjoint-proper-br2.json'
V79=HERE/'e3-b1-full-gysin-matrix-xalpha-correction-v79.json'
BRIDGE_SHA='039e3792e950ac5bf94adf6538c229640da231000a5e1b159a80e2323a812a92'
ADJ_SHA='066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8'
V79_SHA='29acced201721df4ad65bda071914bf71a4b5d7098dce86a541cdd41f2085921'


def csha(o):
 b=dict(o); h=b.pop('canonical_sha256'); assert h==hashlib.sha256(json.dumps(b,sort_keys=True,separators=(',',':')).encode()).hexdigest(); return h

def mm(A,B):
 return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def inv(A):
 n=len(A); m=[[Fraction(A[i][j]) for j in range(n)]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
 for c in range(n):
  p=next(r for r in range(c,n) if m[r][c]); m[c],m[p]=m[p],m[c]
  q=m[c][c]; m[c]=[x/q for x in m[c]]
  for r in range(n):
   if r!=c and m[r][c]:
    q=m[r][c]; m[r]=[m[r][j]-q*m[c][j] for j in range(2*n)]
 return [r[n:] for r in m]

def rowmul(v,M): return [sum(v[k]*M[k][j] for k in range(len(v))) for j in range(len(M[0]))]

def solve_f2(basis,target):
 # row reduction of augmented system B^T c = target^T
 n=len(basis); d=len(target)
 a=[[basis[j][i]&1 for j in range(n)]+[target[i]&1] for i in range(d)]
 r=0; pivot_cols=[]
 for c in range(n):
  p=next((i for i in range(r,d) if a[i][c]),None)
  if p is None: continue
  a[r],a[p]=a[p],a[r]
  for i in range(d):
   if i!=r and a[i][c]: a[i]=[x^y for x,y in zip(a[i],a[r])]
  pivot_cols.append(c); r+=1
 for i in range(r,d):
  if not any(a[i][:-1]) and a[i][-1]: return None
 x=[0]*n
 for rr,c in enumerate(pivot_cols): x[c]=a[rr][-1]
 # verify
 got=[0]*d
 for bit,row in zip(x,basis):
  if bit: got=[a^b for a,b in zip(got,row)]
 assert got==[z&1 for z in target]
 return x

def bits_to_mask(bits): return sum((b&1)<<i for i,b in enumerate(bits))

old=runpy.run_path(str(OLD))['load'](); sign=runpy.run_path(str(SIGN))['load']()
bridge=json.loads(BRIDGE.read_text()); adj=json.loads(ADJ.read_text()); v79=json.loads(V79.read_text())
assert csha(bridge)==BRIDGE_SHA and csha(adj)==ADJ_SHA and csha(v79)==V79_SHA
assert old['canonical_sha256']==bridge['source_locks']['retained_old_picard_base_sha256']
assert sign['canonical_sha256']==bridge['source_locks']['retained_old_picard_signs_sha256']
G=old['picard_gram_64x64']; Gi=inv(G)
S13=bridge['actual_coordinate_swaps_in_historical_magma_picard_basis']['swap13_action_64x64']
A2=sign['picard_actions_64x64']['a2']; S64=mm(S13,A2)
I64=[[int(i==j) for j in range(64)] for i in range(64)]
assert mm(S64,S64)==I64 and mm(mm(S64,G),[list(x) for x in zip(*S64)])==G
zbs=adj['degree2_picard_adjoint']['target_AT2_basis_picard_covectors_zS_14x64']
# u_i = 2*z_i*G^-1 mod 2 is the ordered A_NS[2]=A_T[2] basis representative.
ubasis=[]
for z in zbs:
 x=rowmul(z,Gi); two=[2*q for q in x]
 assert all(q.denominator==1 for q in two)
 ubasis.append([int(q)&1 for q in two])
# exact F2 rank check by solving each unit relation is implicit below; require all
# basis rows independent using elimination on their 64-bit row masks.
def rank_f2(rows):
 a=[r[:] for r in rows]; rr=0
 for c in range(len(a[0])):
  p=next((i for i in range(rr,len(a)) if a[i][c]),None)
  if p is None: continue
  a[rr],a[p]=a[p],a[rr]
  for i in range(len(a)):
   if i!=rr and a[i][c]: a[i]=[x^y for x,y in zip(a[i],a[rr])]
  rr+=1
 return rr
assert rank_f2(ubasis)==14
# Rows of S64 are images of the historical Picard basis, so a row lattice
# coordinate x transforms as x*S64. Descend each discriminant basis element.
M=[]
for u in ubasis:
 up=[int(x)&1 for x in rowmul(u,S64)]
 coeff=solve_f2(ubasis,up); assert coeff is not None
 M.append(coeff)
I14=[[int(i==j) for j in range(14)] for i in range(14)]
assert mm(M,M)==I14
beta25=v79['b1_matrix']['columns_f2'][3]
assert bits_to_mask(beta25)==25
# Contragradient action on a Brauer functional. S is an involution, hence
# beta'_i=beta(S e_i)=sum_j M_ij beta_j.
betaS=[sum(M[i][j]*beta25[j] for j in range(14))&1 for i in range(14)]
maskS=bits_to_mask(betaS)
target=v79['e3_membership']['target_coordinate_f2']; targetmask=bits_to_mask(target)
assert targetmask==20
print(json.dumps({
 'success':True,
 'marker':'V83_EXACT_S_PROPER14_TRANSPORT_DIAGNOSTIC',
 'bridge_canonical_sha256':BRIDGE_SHA,
 'adjoint_canonical_sha256':ADJ_SHA,
 'v79_canonical_sha256':V79_SHA,
 'proper14_discriminant_basis_rank_f2':14,
 'S64_factorization':'swap13 * sign(a2)',
 'S64_involution_and_gram_isometry':True,
 'S_proper14_action_14x14':M,
 'S_proper14_action_involution':True,
 'B1_generator_mask':25,
 'B3_transported_generator_coordinate_f2':betaS,
 'B3_transported_generator_mask':maskS,
 'e3_target_mask':20,
 'e3_target_equals_B3_transported_generator':maskS==20,
 'b3_literal_cech_transport_materialized':False,
 'genuine_e3_full_surface_H2_mu2_lift_materialized':False,
 'merge_allowed':False,
},sort_keys=True))
