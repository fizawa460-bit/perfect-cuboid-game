#!/usr/bin/env python3
from __future__ import annotations
import json, runpy
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V61-0a8af929e004.json'
snaptext=SNAP.read_text(); orig=Path.read_text; sr=STATE.resolve()
def patched(self:Path,*a,**k):
    if self.resolve()==sr: return snaptext
    return orig(self,*a,**k)
Path.read_text=patched
try:
    ns=runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4x.py'))
finally:
    Path.read_text=orig

inc=ns['incidence']
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
