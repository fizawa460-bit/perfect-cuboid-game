#!/usr/bin/env python3
from __future__ import annotations
import json,runpy
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP61=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V61-0a8af929e004.json'
AA=ROOT/'stages/stage35-ex/35ex-35/goal4aa-second-class-qi-cyclic-linear-hyperplane-blocker.json'
Z=ROOT/'stages/stage35-ex/35ex-35/goal4z-one-explicit-biquaternion-second-qi-principalization.json'
PERMS=ROOT/'stages/stage33/33-07/galois-known-class-permutations.json'

aa=json.loads(AA.read_text()); z=json.loads(Z.read_text()); perms=json.loads(PERMS.read_text())
assert aa['schema']=='STAGE35_EX_35_GOAL4AA_QI_CYCLIC_LINEAR_HYPERPLANE_BLOCKER_V1'
assert z['schema']=='STAGE35_EX_35_GOAL4Z_ONE_EXPLICIT_BIQUATERNION_SECOND_QI_PRINCIPALIZATION_V1'

# Reuse the exact retained 140 classes / Gram matrix without reading giant payloads directly.
snap=SNAP61.read_text(); orig=Path.read_text; sr=STATE.resolve()
def patched(self:Path,*args,**kwargs):
    if self.resolve()==sr: return snap
    return orig(self,*args,**kwargs)
Path.read_text=patched
try:
    core=runpy.run_path(str(ROOT/'stages/stage35-ex/stage35_ex_35_goal4y_core.py'))
finally:
    Path.read_text=orig
known=[[int(x) for x in r] for r in core['ns']['known']]
gram=sp.Matrix(core['ns']['gram'])
assert len(known)==140 and all(len(r)==64 for r in known)

# Reconstruct the exact Goal4AA 69-support principal-divisor target.
formal=[0]*140; cc=[int(x) for x in perms['cc_permutation_1based']]
for k,v in z['class_B']['picard_lift_cc_indlist_coefficients'].items():
    i=int(k); c=int(v); formal[i-1]+=c; formal[cc[i-1]-1]+=c
for k,v in aa['class_B_principalization_target']['simplified_boundary_divisor_E_B'].items():
    formal[int(k)-1]-=int(v)
assert sum(x!=0 for x in formal)==69
P=[max(x,0) for x in formal]; N=[max(-x,0) for x in formal]

def cls(vec):
    return sp.Matrix([[sum(int(vec[j])*known[j][i] for j in range(140)) for i in range(64)]])
def pairing(a,b):
    return int((a*gram*b.T)[0])

def pair_known(i,j):
    a=sp.Matrix([known[i]]); b=sp.Matrix([known[j]])
    return pairing(a,b)

def total_transform(indices1):
    v=[0]*140
    for i in indices1: v[i-1]+=1
    for j in range(93,141):
        if any(pair_known(i-1,j-1)!=0 for i in indices1): v[j-1]+=1
    return v

Pc=cls(P); Nc=cls(N)
assert Pc==Nc
# A complete hyperplane section is the total transform of source linear section C1[1..8].
H=cls(total_transform(list(range(1,9))))
assert pairing(H,H)==16
assert pairing(H,Pc)==396
R=25*H-Pc
assert pairing(H,R)==4
r2=pairing(R,R)

# Exceptional rows are independent.  Use one invertible 48-column minor to solve
# whether R differs from a retained degree-4 strict configuration by a nonnegative
# exceptional divisor.
E=sp.Matrix([known[j] for j in range(92,140)])
assert E.rank()==48
_,piv=E.rref(); cols=list(piv[:48]); assert len(cols)==48
M=E[:,cols]; Minv=M.inv()
def exceptional_completion(base):
    d=R-sp.Matrix([base])
    dsel=sp.Matrix([[d[0,j] for j in cols]])
    c=dsel*Minv
    if any(x.q!=1 for x in c): return None
    ci=[int(x) for x in c]
    if any(x<0 for x in ci): return None
    if sp.Matrix([ci])*E!=d: return None
    return ci

matches=[]
# One retained degree-4 C2/C3 strict curve.
for j in range(32,92):
    c=exceptional_completion(known[j])
    if c is not None:
        matches.append({'strict_kind':'ONE_DEGREE4','strict_indices_1based':[j+1],
                        'exceptional_coefficients_nonzero':{str(93+k):v for k,v in enumerate(c) if v}})
# Or a degree-4 sum of two retained C1 conics, allowing multiplicity two.
for j in range(32):
    for k in range(j,32):
        base=[known[j][u]+known[k][u] for u in range(64)]
        c=exceptional_completion(base)
        if c is not None:
            matches.append({'strict_kind':'TWO_CONICS','strict_indices_1based':[j+1,k+1],
                            'exceptional_coefficients_nonzero':{str(93+t):v for t,v in enumerate(c) if v}})

out={
 'schema':'STAGE35_EX_GOAL4AG_DEGREE25_RESIDUAL_DIAGNOSTIC_V1',
 'formal_target_support_count':69,
 'positive_hyperplane_degree':396,
 'negative_hyperplane_degree':396,
 'surface_hyperplane_square':16,
 'homogeneous_ratio_degree_lower_bound':25,
 'degree25_common_residual_hyperplane_degree':4,
 'degree25_common_residual_square':r2,
 'retained_degree4_effective_completion_match_count':len(matches),
 'retained_degree4_effective_completion_matches':matches,
 'scope':'RETAINED_C2_C3_OR_TWO_C1_STRICT_PLUS_NONNEGATIVE_EXCEPTIONALS_ONLY',
 'explicit_F_B_materialized':False,
 'degree25_global_exhaustion_proved':False,
 'global_F_B_nonexistence_proved':False,
 'theorem_credit':False,
 'endpoint_credit':False,
 'E1_proved':False,
 'stage35_closed':False,
}
print('GOAL4AG_DEGREE25_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
