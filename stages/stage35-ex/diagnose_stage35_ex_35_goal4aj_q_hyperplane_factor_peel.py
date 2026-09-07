#!/usr/bin/env python3
"""Goal4AJ diagnostic: maximally peel known Q-defined hyperplane-orbit factors.

Reconstruct the exact 31 complete linear hyperplane divisors from Goal4AA,
group them into V4 Galois orbits using the retained 140-component actions,
and solve an exact bounded integer packing problem separately inside the known
degree-31 numerator and denominator divisors from the passing Goal4AJ packet.

This only peels explicit known linear factors.  It does not solve the residual
section problem and does not materialize F_B.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import hashlib
import json
import runpy
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4ag_degree25_residual.py'
PERMS=ROOT/'stages/stage33/33-07/galois-known-class-permutations.json'
base=runpy.run_path(str(BASE))
known=[[int(x) for x in r] for r in base['known']]
gram=base['gram']
H=[int(x) for x in list(base['H'])]
p=json.loads(PERMS.read_text())
cc=[int(x) for x in p['cc_permutation_1based']]
ct=[int(x) for x in p['ct_permutation_1based']]
assert len(known)==140 and len(cc)==len(ct)==140
assert p['canonical_sha256']=='e5db20f41948b73168ad5b62acb2f4b48a344e0543d2204c0d5ffdc3cae7cf30'

PACKET_SHA='c3c03a7be1d09ac61c29afb855febc0424c2f8818ba428efcc920861dc75a009'
PACKET_RUN=34086027177
PACKET_JOB=101630197014

NUM={2:21,3:1,4:1,5:1,6:1,7:21,9:3,10:10,12:10,13:18,14:4,15:12,16:1,17:3,18:12,19:12,22:12,23:10,24:1,27:1,30:1,38:13,40:13,58:9,60:9,65:1,67:1,93:26,94:3,95:2,96:21,97:2,98:21,99:26,100:3,101:22,102:2,103:3,104:23,105:15,106:37,107:36,108:14,109:20,110:17,111:13,112:22,113:27,114:12,115:12,116:21,117:1,118:11,119:11,120:1,121:11,122:1,123:1,124:11,125:18,126:13,127:13,128:18,129:13,130:12,131:12,132:13,133:6,134:8,135:8,136:6,137:6,138:6,139:6,140:6}
DEN={1:3,8:3,9:3,11:2,16:1,17:3,21:2,24:1,25:8,26:10,27:1,28:2,29:2,30:1,31:10,32:8,33:13,34:11,35:13,36:11,37:13,39:13,58:9,60:9,65:1,67:1,94:2,95:4,97:4,100:2,101:13,102:16,103:18,104:13,105:4,106:1,107:1,108:2,109:24,110:15,111:15,112:22,113:23,114:12,115:12,116:21,117:21,118:15,119:15,120:21,121:15,122:21,123:21,124:15,125:11,126:14,127:14,128:11,129:13,130:12,131:12,132:13,133:5,134:7,135:7,136:5,137:6,138:6,139:6,140:6}

def dense(d): return [int(d.get(j,0)) for j in range(1,141)]
A=dense(NUM); B=dense(DEN)

def picclass(vec): return [sum(vec[j]*known[j][u] for j in range(140)) for u in range(64)]
assert picclass(A)==[31*x for x in H]
assert picclass(B)==[31*x for x in H]

# Exact total transforms on the minimal resolution.
def pair_known(i,j):
    return sum(known[i][u]*gram[u,v]*known[j][v] for u in range(64) for v in range(64))
def total_transform(curves):
    out=[0]*140
    for i in curves: out[i-1]+=1
    for j in range(93,141):
        if any(pair_known(i-1,j-1)!=0 for i in curves): out[j-1]+=1
    return out

# Tiny exact Q(i,sqrt(2)) arithmetic, copied from the verified Goal4AA
# reconstruction, only for scalar-normalized source linear forms.
Z=(Fraction(0),)*4; ONE=(Fraction(1),Fraction(0),Fraction(0),Fraction(0))
II=(Fraction(0),Fraction(1),Fraction(0),Fraction(0)); SS=(Fraction(0),Fraction(0),Fraction(1),Fraction(0))
def add(x,y): return tuple(x[i]+y[i] for i in range(4))
def neg(x): return tuple(-t for t in x)
def mul(x,y):
    out=[Fraction(0)]*4; mons=[(0,0),(1,0),(0,1),(1,1)]
    for r,(ai,as_) in enumerate(mons):
      for t,(bi,bs) in enumerate(mons):
        ci=ai+bi; cs=as_+bs; c=x[r]*y[t]
        if ci>=2: c=-c; ci-=2
        if cs>=2: c*=2; cs-=2
        out[mons.index((ci,cs))]+=c
    return tuple(out)
IS=mul(II,SS)
def inv_pivot(x):
    cand=[ONE,neg(ONE),II,neg(II),SS,neg(SS),IS,neg(IS)]
    halfS=tuple(t/Fraction(2) for t in SS); minusHalfIS=tuple(-t/Fraction(2) for t in IS)
    inv=[ONE,neg(ONE),neg(II),II,halfS,neg(halfS),minusHalfIS,neg(minusHalfIS)]
    return inv[cand.index(x)]
def coeff(unit,sign=1):
    q={'1':ONE,'i':II,'s':SS}[unit]; return q if sign==1 else neg(q)
def form(*terms):
    v=[Z]*7
    for j,c in terms: v[j]=add(v[j],c)
    pivot=next(x for x in v if x!=Z); pinv=inv_pivot(pivot)
    return tuple(tuple((q.numerator,q.denominator) for q in mul(x,pinv)) for x in v)
def f1(j,u='1',sgn=1): return form((j,coeff(u,sgn)))
def f2(j,u,j2,u2='1',sgn2=1): return form((j,coeff(u)),(j2,coeff(u2,sgn2)))

curve_forms={}; degrees={}
def addcurve(idx,deg,forms): curve_forms[idx]=forms; degrees[idx]=deg
idx=1
for basec,specs in [(0,[(1,5),(2,4),(3,6)]),(1,[(2,3),(0,5),(4,6)]),(2,[(0,4),(1,3),(5,6)])]:
  for e1 in [1,-1]:
   for e2 in [1,-1]:
    for e3 in [1,-1]:
     es=[e1,e2,e3]; addcurve(idx,2,[f1(basec)]+[f2(x,'1',y,'1',es[t]) for t,(x,y) in enumerate(specs)]); idx+=1
for e3 in [1,-1]:
 for e2 in [1,-1]:
  for e1 in [1,-1]:
   addcurve(idx,2,[f1(6),f2(0,'i',3,'1',e1),f2(1,'i',4,'1',e2),f2(2,'i',5,'1',e3)]); idx+=1
assert idx==33
for b,(x,y,c0) in [(3,(1,2,0)),(4,(2,0,1)),(5,(0,1,2))]:
 for e1 in [1,-1]:
  for e2 in [1,-1]:
   addcurve(idx,4,[f1(b),f2(x,'i',y,'1',e1),f2(c0,'1',6,'1',e2)]); idx+=1
assert idx==45
for x,y,b3,b1,b2 in [(0,1,5,3,4),(1,2,3,4,5),(2,0,4,5,3)]:
 for e1 in [1,-1]:
  for e2 in [1,-1]:
   for e3 in [1,-1]:
    addcurve(idx,4,[f2(x,'1',y,'1',e1),f2(x,'s',b3,'1',e2),f2(b1,'1',b2,'1',e3)]); idx+=1
for x,b2,b3,b1 in [(0,4,5,3),(1,5,3,4),(2,3,4,5)]:
 for e3 in [1,-1]:
  for e2 in [1,-1]:
   for e1 in [1,-1]:
    addcurve(idx,4,[f2(x,'i',6,'1',e1),f2(b2,'i',b3,'1',e2),form((x,IS),(b1,coeff('1',e3)))]); idx+=1
assert idx==93

groups=defaultdict(set)
for ci,forms in curve_forms.items():
    for L in forms: groups[L].add(ci)
raw={L:sorted(cs) for L,cs in groups.items() if sum(degrees[i] for i in cs)==16}
anchor_class=picclass(total_transform(list(range(1,9))))
complete=[]
for L,cs in raw.items():
    v=total_transform(cs)
    if picclass(v)==anchor_class:
        complete.append((L,cs,v))
complete.sort(key=lambda t:repr(t[0]))
assert len(groups)==79 and len(raw)==43 and len(complete)==31
assert len({tuple(v) for _,_,v in complete})==31
Hvecs=[v for _,_,v in complete]
index={tuple(v):i for i,v in enumerate(Hvecs)}

def permute(v,perm):
    out=[0]*140
    for j,c in enumerate(v): out[perm[j]-1]+=c
    return out
cc_idx=[]; ct_idx=[]
for v in Hvecs:
    vc=tuple(permute(v,cc)); vt=tuple(permute(v,ct))
    if vc not in index or vt not in index:
        raise SystemExit('complete hyperplane packet not Galois stable')
    cc_idx.append(index[vc]); ct_idx.append(index[vt])

unseen=set(range(31)); orbits=[]
while unseen:
    seed=min(unseen); orb={seed}; todo=[seed]
    while todo:
        j=todo.pop()
        for k in (cc_idx[j],ct_idx[j]):
            if k not in orb: orb.add(k); todo.append(k)
    unseen-=orb; orbits.append(sorted(orb))
assert sum(len(o) for o in orbits)==31
orbit_sums=[]
for orb in orbits:
    orbit_sums.append([sum(Hvecs[h][j] for h in orb) for j in range(140)])

def solve(side):
    # one integer multiplicity per full Galois orbit; maximize peeled linear degree
    M=np.asarray(orbit_sums,dtype=float).T
    weights=np.asarray([len(o) for o in orbits],dtype=float)
    res=milp(-weights,integrality=np.ones(len(orbits),dtype=int),
             bounds=Bounds(np.zeros(len(orbits)),np.full(len(orbits),31.0)),
             constraints=LinearConstraint(M,-np.inf,np.asarray(side,dtype=float)),
             options={'time_limit':60.0,'mip_rel_gap':0.0})
    if not res.success or res.x is None: raise SystemExit('Q hyperplane factor peel ILP failed')
    mult=[int(round(x)) for x in res.x]
    peeled=[sum(mult[o]*orbit_sums[o][j] for o in range(len(orbits))) for j in range(140)]
    residual=[side[j]-peeled[j] for j in range(140)]
    assert all(x>=0 for x in residual)
    k=sum(mult[o]*len(orbits[o]) for o in range(len(orbits)))
    assert picclass(peeled)==[k*x for x in H]
    assert picclass(residual)==[(31-k)*x for x in H]
    for perm in (cc,ct):
        assert peeled==permute(peeled,perm) and residual==permute(residual,perm)
    return {'peeled_linear_degree':k,'residual_homogeneous_degree':31-k,
            'orbit_multiplicities':[{'orbit_hyperplane_indices_0based':orbits[o],'orbit_size':len(orbits[o]),'multiplicity':m} for o,m in enumerate(mult) if m],
            'peeled_support_count':sum(x!=0 for x in peeled),'residual_support_count':sum(x!=0 for x in residual),
            'residual_support_1based':{str(j+1):x for j,x in enumerate(residual) if x}}

num=solve(A); den=solve(B)
out={
 'schema':'STAGE35_EX_GOAL4AJ_Q_HYPERPLANE_FACTOR_PEEL_DIAGNOSTIC_V1',
 'source_locks':{'degree31_divisor_packet_sha256':PACKET_SHA,'degree31_divisor_packet_run':PACKET_RUN,'degree31_divisor_packet_job':PACKET_JOB,
                 'galois_known_class_permutations_sha256':p['canonical_sha256']},
 'retained_distinct_linear_form_count':len(groups),'raw_degree16_candidate_count':len(raw),
 'complete_linear_hyperplane_count':len(complete),'galois_orbit_count':len(orbits),'galois_orbit_sizes':[len(o) for o in orbits],
 'numerator':num,'denominator':den,
 'q_divisor_orbit_peel_exact':True,
 'literal_q_polynomial_factor_normalization_materialized':False,
 'strict_curve_symbolic_power_conditions_encoded':False,
 'global_degree31_linear_system_solved':False,
 'literal_numerator_coefficients_materialized':False,'literal_denominator_coefficients_materialized':False,
 'literal_F_B_materialized':False,'local_evaluations_computed':False,'brauer_manin_obstruction_obtained':False,
 'E1_proved':False,'stage35_closed':False,'theorem_credit':False,'endpoint_credit':False,
}
out['canonical_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
print('GOAL4AJ_Q_HYPERPLANE_FACTOR_PEEL_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
print('GOAL4AJ_Q_HYPERPLANE_FACTOR_PEEL=PASS')
