#!/usr/bin/env python3
"""Compute the full generated residue-source stabilizer of A2_02 via Schreier generators.

The resulting proper14 fixed-space dimension is CONDITIONAL: a later leaf must
show that the actual full-surface A2_02 Cech H2 seed is fixed modulo the Kummer
kernel by the corresponding geometric words.  Residue-vector stabilizing alone
is not promoted to H2/Brauer stabilizing here.
"""
from __future__ import annotations
import hashlib,json,os,runpy
from collections import deque
from pathlib import Path
D=Path(__file__).resolve().parent; S33=D.parent
SRC=S33/'33-11f'/'stage33-11f-source-lock.json'; BR=S33/'33-07'/'proper-brauer2-from-discriminant.json'; V84=D/'diagnose_e3_coordinate_automorphism_orbit_v84.py'
SRC_SHA='3c493c5863a1506e48622ec9180119b6b80f5ee0642fe20515916749b3138957'; BR_SHA='c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf'; V84_BLOB='e9c7e81cc59fb5203482071208d25ff1447edeb2'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o
def gitblob(data): return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def rowmul(v,M): return tuple(sum(v[i]*M[i][j] for i in range(len(v)))&1 for j in range(len(v)))
def colact(M,v): return tuple(sum(M[i][j]*v[j] for j in range(len(v)))&1 for i in range(len(v)))
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
def apply_target(v,word,gens):
 v=tuple(v)
 for name in word: v=colact(gens[name],v)
 return v
def target_matrix(word,gens,n=14):
 cols=[apply_target([int(i==j) for i in range(n)],word,gens) for j in range(n)]
 return [[cols[j][i] for j in range(n)] for i in range(n)]
src=load(SRC,SRC_SHA); br=load(BR,BR_SHA); assert gitblob(V84.read_bytes())==V84_BLOB
ns=runpy.run_path(str(V84)); gens14=ns['gens14']; names=src['exact_source_actions']['action_names']; acts=src['exact_source_actions']['matrices']; assert set(names)==set(gens14)
start=tuple([0,1]+[0]*24); words={start:[]}; q=deque([start])
while q:
 v=q.popleft()
 for name,M in zip(names,acts):
  w=rowmul(v,M)
  if w not in words:
   words[w]=words[v]+[name]; q.append(w)
# Schreier generators: rep(v) g rep(vg)^-1. All named generators are involutions.
stab_words=[]; seen_target=set()
for v,wv in words.items():
 for name,M in zip(names,acts):
  w=rowmul(v,M); sw=wv+[name]+list(reversed(words[w]))
  # Exact source check: every Schreier word returns A2_02.
  z=start
  for nm in sw: z=rowmul(z,acts[names.index(nm)])
  assert z==start
  T=target_matrix(sw,gens14); key=tuple(tuple(r) for r in T)
  if key not in seen_target:
   seen_target.add(key); stab_words.append(sw)
# Start with exact Galois cc/ct fixedness already proved in V91C1G.
eq=[]; n=14
for M in (br['proper_Br2_cc_action_f2'],br['proper_Br2_ct_action_f2']):
 for j in range(n): eq.append([(M[i][j]^(1 if i==j else 0)) for i in range(n)])
base_dim=nullity(eq,n); assert base_dim==10
for sw in stab_words:
 T=target_matrix(sw,gens14)
 for i in range(n): eq.append([(T[i][j]^(1 if i==j else 0)) for j in range(n)])
aug_dim=nullity(eq,n)
e3=tuple([0,0,1,0,1]+[0]*9); e3_fixed=all(apply_target(e3,sw,gens14)==e3 for sw in stab_words)
result={'success':True,'marker':'V91C1P_A2_02_FULL_RESIDUE_STABILIZER_DIAGNOSTIC','source_orbit_size':len(words),'schreier_edge_count':len(words)*len(names),'distinct_target_stabilizer_actions':len(stab_words),'joint_v4_fixed_dimension_before':base_dim,'conditional_dimension_if_full_seed_stabilized_by_full_residue_stabilizer':aug_dim,'e3_mask20_fixed_by_full_residue_stabilizer_target_actions':e3_fixed,'seed_level_stabilizer_transport_materialized':False,'credit':False}
print(json.dumps(result,sort_keys=True))
if os.environ.get('GITHUB_ENV'):
 with open(os.environ['GITHUB_ENV'],'a') as out:
  out.write(f'V91C1P_AUG_DIM={aug_dim}\nV91C1P_ORBIT_SIZE={len(words)}\nV91C1P_TARGET_STAB_COUNT={len(stab_words)}\nV91C1P_E3_FIXED='+('true' if e3_fixed else 'false')+'\n')
print('::notice title=V91C1P_FULL_RESIDUE_STABILIZER::'+json.dumps(result,sort_keys=True,separators=(',',':')))
