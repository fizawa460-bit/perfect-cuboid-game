#!/usr/bin/env python3
from __future__ import annotations

import json
import runpy
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csr_matrix, vstack

ROOT=Path(__file__).resolve().parents[2]
RR=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4ah_degree31_rr.py'
ns=runpy.run_path(str(RR))
known=np.asarray([[int(x) for x in row] for row in ns['known']],dtype=float)
D=np.asarray([int(x) for x in ns['D']],dtype=float)
cc=[int(x) for x in ns['cc']]
ct=[int(x) for x in ns['ct']]
assert known.shape==(140,64) and D.shape==(64,)
assert len(cc)==len(ct)==140

# Exact Picard-class equations: sum_j x_j [C_j] = D.
blocks=[csr_matrix(known.T)]
rhs=[*D.tolist()]
# Require the literal retained divisor to descend under both retained Galois generators.
rows=[]
for perm in (cc,ct):
    for j,k1 in enumerate(perm):
        k=k1-1
        if j<k:
            row=np.zeros(140,dtype=float); row[j]=1.0; row[k]=-1.0
            rows.append(row)
if rows:
    blocks.append(csr_matrix(np.asarray(rows)))
    rhs.extend([0.0]*len(rows))
A=vstack(blocks,format='csr')
b=np.asarray(rhs,dtype=float)

# Bounded feasibility only. The strict coefficients are automatically degree-bounded
# by H.D=96; 512 is a generous diagnostic cap for exceptional multiplicities.
c=np.ones(140,dtype=float)
res=milp(
    c,
    integrality=np.ones(140,dtype=int),
    bounds=Bounds(np.zeros(140),np.full(140,512.0)),
    constraints=LinearConstraint(A,b,b),
    options={'time_limit':120.0,'mip_rel_gap':0.0},
)

found=bool(res.x is not None and res.success)
support={}
exact_ok=False
sym_ok=False
hdeg=None
if found:
    x=[int(round(v)) for v in res.x]
    # Fail closed against floating MILP acceptance: recheck all 64 equations over Z.
    lhs=[sum(x[j]*int(ns['known'][j][u]) for j in range(140)) for u in range(64)]
    exact_ok=(lhs==[int(v) for v in ns['D']])
    sym_ok=all(x[j]==x[perm[j]-1] for perm in (cc,ct) for j in range(140))
    assert exact_ok and sym_ok and all(v>=0 for v in x)
    support={str(j+1):v for j,v in enumerate(x) if v}
    hdeg=sum(v*(2 if j<32 else 4 if j<92 else 0) for j,v in enumerate(x))
    assert hdeg==96

out={
    'schema':'STAGE35_EX_GOAL4AJ_KNOWN_RESIDUAL_MILP_DIAGNOSTIC_V1',
    'bound_per_coefficient':512,
    'solver_success':bool(res.success),
    'solver_status':int(res.status),
    'solver_message':str(res.message),
    'q_invariant_nonnegative_retained140_decomposition_found':found,
    'exact_picard_recheck':exact_ok,
    'galois_symmetry_recheck':sym_ok,
    'residual_hyperplane_degree':hdeg,
    'support_count':len(support),
    'support_1based':support,
    'literal_F_B_materialized':False,
    'local_evaluations_computed':False,
    'brauer_manin_obstruction_obtained':False,
    'E1_proved':False,
    'stage35_closed':False,
    'theorem_credit':False,
    'endpoint_credit':False,
}
print('GOAL4AJ_KNOWN_RESIDUAL_MILP_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
print('GOAL4AJ_KNOWN_RESIDUAL_MILP_DONE')
