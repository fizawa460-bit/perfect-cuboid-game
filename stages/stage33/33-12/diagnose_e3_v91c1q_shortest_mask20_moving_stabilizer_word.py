#!/usr/bin/env python3
"""Extract the deterministic shortest A2_02 residue-stabilizer word that moves mask20.

No seed-level invariance is inferred. This only chooses the single exact word to
be tested on the V91C1D full Cech-Cartier seed in the next leaf.
"""
from __future__ import annotations
import hashlib,json,os,runpy
from collections import deque
from pathlib import Path
D=Path(__file__).resolve().parent; S33=D.parent
SRC=S33/'33-11f'/'stage33-11f-source-lock.json'; V84=D/'diagnose_e3_coordinate_automorphism_orbit_v84.py'
SRC_SHA='3c493c5863a1506e48622ec9180119b6b80f5ee0642fe20515916749b3138957'; V84_BLOB='e9c7e81cc59fb5203482071208d25ff1447edeb2'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o
def gitblob(data): return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def rowmul(v,M): return tuple(sum(v[i]*M[i][j] for i in range(len(v)))&1 for j in range(len(v)))
def colact(M,v): return tuple(sum(M[i][j]*v[j] for j in range(len(v)))&1 for i in range(len(v)))
def apply_source(v,word,names,acts):
 v=tuple(v)
 for name in word: v=rowmul(v,acts[names.index(name)])
 return v
def apply_target(v,word,gens):
 v=tuple(v)
 for name in word: v=colact(gens[name],v)
 return v
src=load(SRC,SRC_SHA); assert gitblob(V84.read_bytes())==V84_BLOB
ns=runpy.run_path(str(V84)); gens14=ns['gens14']; names=src['exact_source_actions']['action_names']; acts=src['exact_source_actions']['matrices']; assert set(names)==set(gens14)
start=tuple([0,1]+[0]*24); e3=tuple([0,0,1,0,1]+[0]*9)
# BFS in the joint source/target state space so the first qualifying word is truly shortest.
# Generator order is lexical for deterministic tie breaking.
gorder=sorted(names)
q=deque([(start,e3,())]); seen={(start,e3)}; witness=None; target_image=None
while q:
 sv,tv,w=q.popleft()
 if w and sv==start and tv!=e3:
  witness=list(w); target_image=tv; break
 for name in gorder:
  sv2=rowmul(sv,acts[names.index(name)]); tv2=colact(gens14[name],tv); st=(sv2,tv2)
  if st not in seen:
   seen.add(st); q.append((sv2,tv2,w+(name,)))
assert witness is not None
assert apply_source(start,witness,names,acts)==start
assert apply_target(e3,witness,gens14)==target_image!=e3
support=[i+1 for i,x in enumerate(target_image) if x]
mask=sum(x<<i for i,x in enumerate(target_image))
result={'success':True,'marker':'V91C1Q_SHORTEST_MASK20_MOVING_RESIDUE_STABILIZER_WORD','word':witness,'word_length':len(witness),'source_a2_02_residue_fixed':True,'mask20_moved':True,'mask20_target_image_decimal':mask,'mask20_target_image_support_one_based':support,'seed_level_transport_materialized':False,'credit':False}
print(json.dumps(result,sort_keys=True))
# Emit a successful warning annotation so the exact witness is retrievable through the checks API.
msg='word='+','.join(witness)+';length='+str(len(witness))+';target_mask='+str(mask)+';target_support='+','.join(map(str,support))
print('::warning file=stages/stage33/33-12/diagnose_e3_v91c1q_shortest_mask20_moving_stabilizer_word.py,title=V91C1Q_WITNESS::'+msg)
if os.environ.get('GITHUB_ENV'):
 with open(os.environ['GITHUB_ENV'],'a') as out:
  out.write('V91C1Q_WORD_LENGTH='+str(len(witness))+'\n')
  out.write('V91C1Q_TARGET_MASK='+str(mask)+'\n')
