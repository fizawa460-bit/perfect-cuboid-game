#!/usr/bin/env python3
"""Finite exact orbit of the retained B1 mask25 under geometric coordinate automorphisms.

Generators are the two certified coordinate swaps and seven certified coordinate
sign changes in the historical Picard64 basis.  Each generator is descended
exactly to the ordered proper14 discriminant basis.  This is an orbit diagnostic
only: literal Cech transport is materialized only in a later source-bound leaf.
"""
from __future__ import annotations

import hashlib, json, runpy, sys
from collections import deque
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

def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def mm2(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B)))&1 for j in range(len(B[0]))] for i in range(len(A))]

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
 n=len(basis); d=len(target)
 a=[[basis[j][i]&1 for j in range(n)]+[target[i]&1] for i in range(d)]
 r=0; piv=[]
 for c in range(n):
  p=next((i for i in range(r,d) if a[i][c]),None)
  if p is None: continue
  a[r],a[p]=a[p],a[r]
  for i in range(d):
   if i!=r and a[i][c]: a[i]=[x^y for x,y in zip(a[i],a[r])]
  piv.append(c); r+=1
 x=[0]*n
 for rr,c in enumerate(piv): x[c]=a[rr][-1]
 got=[0]*d
 for bit,row in zip(x,basis):
  if bit: got=[a^b for a,b in zip(got,row)]
 assert got==[z&1 for z in target]
 return x

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

def bits_to_mask(v): return sum((b&1)<<i for i,b in enumerate(v))
def act_beta(M,beta): return tuple(sum(M[i][j]*beta[j] for j in range(14))&1 for i in range(14))

old=runpy.run_path(str(OLD))['load'](); sign=runpy.run_path(str(SIGN))['load']()
bridge=json.loads(BRIDGE.read_text()); adj=json.loads(ADJ.read_text()); v79=json.loads(V79.read_text())
assert csha(bridge)==BRIDGE_SHA and csha(adj)==ADJ_SHA and csha(v79)==V79_SHA
assert old['canonical_sha256']==bridge['source_locks']['retained_old_picard_base_sha256']
assert sign['canonical_sha256']==bridge['source_locks']['retained_old_picard_signs_sha256']
G=old['picard_gram_64x64']; Gi=inv(G)
zbs=adj['degree2_picard_adjoint']['target_AT2_basis_picard_covectors_zS_14x64']
ubasis=[]
for z in zbs:
 two=[2*q for q in rowmul(z,Gi)]; assert all(q.denominator==1 for q in two)
 ubasis.append([int(q)&1 for q in two])
assert rank_f2(ubasis)==14

def descend(A64):
 M=[]
 for u in ubasis:
  up=[int(x)&1 for x in rowmul(u,A64)]
  M.append(solve_f2(ubasis,up))
 return M

acs=bridge['actual_coordinate_swaps_in_historical_magma_picard_basis']
gens64={
 'swap12':acs['swap12_action_64x64'],
 'swap13':acs['swap13_action_64x64'],
}
for name in sign['coordinate_order']:
 gens64['sign_'+name]=sign['picard_actions_64x64'][name]
I14=[[int(i==j) for j in range(14)] for i in range(14)]
gens14={}
for name,A64 in gens64.items():
 M=descend(A64); assert mm2(M,M)==I14
 gens14[name]=M

start=tuple(v79['b1_matrix']['columns_f2'][3]); target=tuple(v79['e3_membership']['target_coordinate_f2'])
assert bits_to_mask(start)==25 and bits_to_mask(target)==20
q=deque([start]); word={start:[]}
while q:
 v=q.popleft()
 for name,M in gens14.items():
  w=act_beta(M,v)
  if w not in word:
   word[w]=word[v]+[name]; q.append(w)
found=target in word
# Track which sign quotient B1 is sent to by swaps in a word; sign changes do not change index.
def quotient_image(w):
 idx=1
 for name in w:
  if name=='swap12':
   idx={1:2,2:1,3:3}[idx]
  elif name=='swap13':
   idx={1:3,3:1,2:2}[idx]
 return idx
wtarget=word.get(target)
print(json.dumps({
 'success':True,
 'marker':'V84_EXACT_COORDINATE_AUTOMORPHISM_ORBIT_DIAGNOSTIC',
 'bridge_canonical_sha256':BRIDGE_SHA,
 'adjoint_canonical_sha256':ADJ_SHA,
 'v79_canonical_sha256':V79_SHA,
 'generator_names':list(gens14),
 'generator_count':len(gens14),
 'all_generators_involutive_on_proper14':True,
 'orbit_size_from_mask25':len(word),
 'orbit_masks_decimal':sorted(bits_to_mask(v) for v in word),
 'start_mask':25,
 'target_mask':20,
 'target_in_coordinate_automorphism_orbit':found,
 'shortest_word_to_target':wtarget,
 'shortest_word_length':None if wtarget is None else len(wtarget),
 'target_route_sign_quotient':None if wtarget is None else 'B'+str(quotient_image(wtarget)),
 'literal_cech_transport_materialized':False,
 'genuine_e3_full_surface_H2_mu2_lift_materialized':False,
 'merge_allowed':False,
},sort_keys=True))
