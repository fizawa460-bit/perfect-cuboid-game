#!/usr/bin/env python3
"""Diagnose whether exact geometric stabilizers of A2_02 can further cut the V91C1G proper14 fixed-space.

This is a target-selection diagnostic only.  It deliberately does not infer that
fixing the 26D residue-source basis vector fixes the full A2_02 Cech H2 class;
that requires a later source-bound seed-level transport check.
"""
from __future__ import annotations
import hashlib,json,runpy
from pathlib import Path
D=Path(__file__).resolve().parent
S33=D.parent
SRC=S33/'33-11f'/'stage33-11f-source-lock.json'
BR=S33/'33-07'/'proper-brauer2-from-discriminant.json'
V84=D/'diagnose_e3_coordinate_automorphism_orbit_v84.py'
SRC_SHA='3c493c5863a1506e48622ec9180119b6b80f5ee0642fe20515916749b3138957'
BR_SHA='c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf'
V84_BLOB='e9c7e81cc59fb5203482071208d25ff1447edeb2'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text(encoding='utf-8')); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o
def git_blob_sha(data): return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def rowmul(v,M): return [sum(v[i]*M[i][j] for i in range(len(v)))&1 for j in range(len(v))]
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
def nullity(eq,n): return n-len(rref(eq,n)[1])
src=load(SRC,SRC_SHA); br=load(BR,BR_SHA)
assert git_blob_sha(V84.read_bytes())==V84_BLOB
ns=runpy.run_path(str(V84)); gens14=ns['gens14']
names=src['exact_source_actions']['action_names']; acts=src['exact_source_actions']['matrices']
assert names==['sign_a1','sign_a2','sign_a3','sign_b1','sign_b2','sign_b3','sign_c','swap12','swap13']
assert set(gens14)==set(names)
e2=[0]*26; e2[1]=1
fixed_names=[name for name,M in zip(names,acts) if rowmul(e2,M)==e2]
# cc/ct use row-vector convention on proper14; coordinate automorphisms use V84 beta -> M beta column convention.
eq=[]; n=14
for M in (br['proper_Br2_cc_action_f2'],br['proper_Br2_ct_action_f2']):
 for j in range(n): eq.append([(M[i][j]^(1 if i==j else 0)) for i in range(n)])
base_dim=nullity(eq,n); assert base_dim==10
for name in fixed_names:
 M=gens14[name]
 for i in range(n): eq.append([(M[i][j]^(1 if i==j else 0)) for j in range(n)])
aug_dim=nullity(eq,n)
e3=[0]*14; e3[2]=1; e3[4]=1
def colact(M,v): return [sum(M[i][j]*v[j] for j in range(n))&1 for i in range(n)]
e3_fixed_names=[name for name in fixed_names if colact(gens14[name],e3)==e3]
result={'success':True,'marker':'V91C1O_A2_02_GEOMETRIC_STABILIZER_DIAGNOSTIC','source_basis':'A2_02','source_generator_fixed_names':fixed_names,'source_generator_fixed_count':len(fixed_names),'joint_v4_fixed_dimension_before':base_dim,'candidate_dimension_if_full_seed_fixed_under_source_generator_stabilizers':aug_dim,'e3_mask20_fixed_by_source_generator_stabilizers':len(e3_fixed_names)==len(fixed_names),'e3_fixed_names':e3_fixed_names,'seed_level_geometric_transport_materialized':False,'credit':False}
print(json.dumps(result,sort_keys=True))
print('::notice title=V91C1O_GEOMETRIC_STABILIZER::'+json.dumps(result,sort_keys=True,separators=(',',':')))
