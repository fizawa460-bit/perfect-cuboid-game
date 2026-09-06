#!/usr/bin/env python3
from __future__ import annotations
import json, runpy
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V61-0a8af929e004.json'
snaptext=SNAP.read_text(); orig=Path.read_text; sr=STATE.resolve()
def patched(self:Path,*a,**k):
    if self.resolve()==sr: return snaptext
    return orig(self,*a,**k)
Path.read_text=patched
try:
    gx=runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4x.py'))
    core=runpy.run_path(str(ROOT/'stages/stage35-ex/stage35_ex_35_goal4y_core.py'))
finally:
    Path.read_text=orig

inc=gx['incidence']
# C1s first block order: e1,e2,e3 in [1,-1], with (eps,delta,eta)=(-e1,-e2,-e3).
signs=[]
for e1 in [1,-1]:
  for e2 in [1,-1]:
    for e3 in [1,-1]: signs.append((-e1,-e2,-e3))
assert len(signs)==8
out=[]
for known_idx,hits in sorted(inc.items()):
    a,b=hits
    sa=signs[a-1]; sb=signs[b-1]
    dif=[k for k in range(3) if sa[k]!=sb[k]]
    assert len(dif)==1
    out.append({'known_index_1based':known_idx,'strict_hits_1based':hits,'strict_signs':[sa,sb],'edge':['eps','delta','eta'][dif[0]]})
print('GOAL4Z_BOUNDARY_INCIDENCE '+json.dumps(out,sort_keys=True))

# Express the Goal4Y lifted Pic(Sbar) 1-cocycle values in the exact upstream INDLIST divisor basis.
indlist=[1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20,21,22,23,25,26,27,29,33,34,35,37,38,41,45,49,53,69,93,94,95,96,97,98,99,101,102,103,104,105,106,107,109,110,111,113,117,118,119,120,121,125,126,127,129,133,135]
known=[[int(x) for x in r] for r in core['ns']['known']]
M=sp.Matrix([known[i-1] for i in indlist])
assert M.det()!=0
Minv=M.inv()
assert all(x.q==1 for x in Minv)
res=[]
for pos in core['positions']:
    f,_=core['h1_generator'](pos)
    item={'smith_position_0based':pos,'galois':{}}
    for g,label in [(1,'cc'),(2,'ct')]:
        p=core['liftP'](f[g])
        coeff=p*Minv
        assert all(x.q==1 for x in coeff)
        sparse={str(indlist[j]):int(coeff[0,j]) for j in range(64) if coeff[0,j]}
        item['galois'][label]=sparse
    res.append(item)
print('GOAL4Z_PICARD_LIFTS '+json.dumps(res,sort_keys=True))
