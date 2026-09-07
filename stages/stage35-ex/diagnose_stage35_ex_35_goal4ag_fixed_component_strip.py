#!/usr/bin/env python3
from __future__ import annotations
import json,runpy
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
base=runpy.run_path(str(ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4ag_degree25_residual.py'))
H=base['H']; Pc=base['Pc']; known=base['known']; gram=base['gram']
Hvec=[int(x) for x in list(H)]; Pvec=[int(x) for x in list(Pc)]
G=[[int(gram[i,j]) for j in range(64)] for i in range(64)]

def transform(v): return [sum(v[i]*G[i][j] for i in range(64)) for j in range(64)]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def qvec(a,b): return dot(transform(a),b)

# Precompute the 140x140 exact intersection packet once, then update pairings incrementally.
tknown=[transform(r) for r in known]
pairmat=[[dot(tknown[j],known[k]) for k in range(140)] for j in range(140)]
Hpair=[qvec(Hvec,r) for r in known]
Ppair=[qvec(Pvec,r) for r in known]
assert qvec(Hvec,Hvec)==16
assert all(pairmat[j][j]==-4 for j in range(92))
assert all(pairmat[j][j]==-2 for j in range(92,140))
assert all(Hpair[j] in (2,4) for j in range(92))
assert all(Hpair[j]==0 for j in range(92,140))

E=sp.Matrix([known[j] for j in range(92,140)])
_,piv=E.rref(); cols=list(piv[:48]); Einv=E[:,cols].inv()
def exceptional_coords(D):
    ds=sp.Matrix([[D[j] for j in cols]])
    c=ds*Einv
    if any(x.q!=1 for x in c): return None
    ci=[int(x) for x in c]
    if sp.Matrix([ci])*E!=sp.Matrix([D]): return None
    return ci

def strip(d):
    D=[d*Hvec[u]-Pvec[u] for u in range(64)]
    ints=[d*Hpair[k]-Ppair[k] for k in range(140)]
    counts=[0]*140; steps=0; hd=16*d-396; initial_degree=hd
    while True:
        if hd<0:
            return {'d':d,'initial_residual_degree':initial_degree,'result':'PROVED_NONEFFECTIVE_NEGATIVE_H_DEGREE',
                    'steps':steps,'final_h_degree':hd,'forced_support_count':sum(x!=0 for x in counts),
                    'forced_strict_multiplicity_sum':sum(counts[:92]),'forced_exceptional_multiplicity_sum':sum(counts[92:])}
        neg=[j for j,x in enumerate(ints) if x<0]
        if not neg: break
        j=min(neg,key=lambda t:(ints[t],t))
        D=[D[u]-known[j][u] for u in range(64)]
        ints=[ints[k]-pairmat[j][k] for k in range(140)]
        hd-=Hpair[j]; counts[j]+=1; steps+=1
        if steps>20000: raise SystemExit(f'fixed-component strip step cap at d={d}')
    if hd==0:
        c=exceptional_coords(D)
        result='SURVIVES_AS_NONNEGATIVE_EXCEPTIONAL' if c is not None and all(x>=0 for x in c) else 'PROVED_NONEFFECTIVE_H0_NOT_NONNEGATIVE_EXCEPTIONAL'
    else:
        result='SURVIVES_NEF_AGAINST_RETAINED_CURVES'
    return {'d':d,'initial_residual_degree':initial_degree,'result':result,'steps':steps,
            'final_h_degree':hd,'final_square':qvec(D,D),'forced_support_count':sum(x!=0 for x in counts),
            'forced_strict_multiplicity_sum':sum(counts[:92]),'forced_exceptional_multiplicity_sum':sum(counts[92:])}

lo,hi=25,128
rows=[strip(d) for d in range(lo,hi+1)]
proved=[r['d'] for r in rows if r['result'].startswith('PROVED_NONEFFECTIVE')]
survivors=[r['d'] for r in rows if r['result'].startswith('SURVIVES')]
contiguous=lo-1
for d in range(lo,hi+1):
    if d in proved and d==contiguous+1: contiguous=d
    else: break
out={
 'schema':'STAGE35_EX_GOAL4AG_FIXED_COMPONENT_STRIP_V2',
 'degree_range':[lo,hi],
 'proved_noneffective_degrees':proved,
 'first_surviving_degree':min(survivors) if survivors else None,
 'contiguous_noneffective_through':contiguous,
 'rows':rows,
 'logic':'NEGATIVE_INTERSECTION_WITH_RETAINED_IRREDUCIBLE_CURVE_FORCES_THAT_COMPONENT; H_IS_NEF_AND_POSITIVE_OFF_EXCEPTIONAL_LOCUS',
 'global_all_degree_exhaustion_proved':False,
 'explicit_F_B_materialized':False,
 'theorem_credit':False,
 'endpoint_credit':False,
 'E1_proved':False,
 'stage35_closed':False,
}
print('GOAL4AG_FIXED_STRIP_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
