#!/usr/bin/env python3
from __future__ import annotations
import json,runpy
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
base=runpy.run_path(str(ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4ag_degree25_residual.py'))
H=base['H']; Pc=base['Pc']; known=base['known']; gram=base['gram']
curves=[sp.Matrix([r]) for r in known]

def q(a,b): return int((a*gram*b.T)[0])
assert q(H,H)==16
assert all(q(curves[j],curves[j])==-4 for j in range(92))
assert all(q(curves[j],curves[j])==-2 for j in range(92,140))
assert all(q(H,curves[j]) in (2,4) for j in range(92))
assert all(q(H,curves[j])==0 for j in range(92,140))

E=sp.Matrix([known[j] for j in range(92,140)])
_,piv=E.rref(); cols=list(piv[:48]); Einv=E[:,cols].inv()
def exceptional_coords(D):
    ds=sp.Matrix([[D[0,j] for j in cols]])
    c=ds*Einv
    if any(x.q!=1 for x in c): return None
    ci=[int(x) for x in c]
    if sp.Matrix([ci])*E!=D: return None
    return ci

def strip(d):
    D=d*H-Pc; counts=[0]*140; steps=0
    initial_degree=q(H,D)
    while True:
        hd=q(H,D)
        if hd<0:
            return {'d':d,'initial_residual_degree':initial_degree,'result':'PROVED_NONEFFECTIVE_NEGATIVE_H_DEGREE',
                    'steps':steps,'final_h_degree':hd,'forced_support_count':sum(x!=0 for x in counts),
                    'forced_strict_multiplicity_sum':sum(counts[:92]),'forced_exceptional_multiplicity_sum':sum(counts[92:])}
        neg=[j for j,C in enumerate(curves) if q(D,C)<0]
        if not neg: break
        # Deterministic: most negative intersection, then smallest retained index.
        j=min(neg,key=lambda t:(q(D,curves[t]),t))
        D-=curves[j]; counts[j]+=1; steps+=1
        if steps>20000: raise SystemExit(f'fixed-component strip step cap at d={d}')
    hd=q(H,D)
    if hd==0:
        c=exceptional_coords(D)
        if c is None or any(x<0 for x in c):
            result='PROVED_NONEFFECTIVE_H0_NOT_NONNEGATIVE_EXCEPTIONAL'
        else:
            result='SURVIVES_AS_NONNEGATIVE_EXCEPTIONAL'
    else:
        result='SURVIVES_NEF_AGAINST_RETAINED_CURVES'
    return {'d':d,'initial_residual_degree':initial_degree,'result':result,'steps':steps,
            'final_h_degree':hd,'final_square':q(D,D),'forced_support_count':sum(x!=0 for x in counts),
            'forced_strict_multiplicity_sum':sum(counts[:92]),'forced_exceptional_multiplicity_sum':sum(counts[92:])}

rows=[strip(d) for d in range(25,65)]
proved=[r['d'] for r in rows if r['result'].startswith('PROVED_NONEFFECTIVE')]
survivors=[r['d'] for r in rows if r['result'].startswith('SURVIVES')]
contiguous=24
for d in range(25,65):
    if d in proved and d==contiguous+1: contiguous=d
    else: break
out={
 'schema':'STAGE35_EX_GOAL4AG_FIXED_COMPONENT_STRIP_V1',
 'degree_range':[25,64],
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
