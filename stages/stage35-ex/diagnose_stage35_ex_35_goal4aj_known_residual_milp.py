#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csr_matrix, vstack

ROOT=Path(__file__).resolve().parents[2]
RR=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4ah_degree31_rr.py'
ns=runpy.run_path(str(RR))
known_int=[[int(x) for x in row] for row in ns['known']]
known=np.asarray(known_int,dtype=float)
D_int=[int(x) for x in ns['D']]
D=np.asarray(D_int,dtype=float)
cc=[int(x) for x in ns['cc']]
ct=[int(x) for x in ns['ct']]
forced=[int(x) for x in ns['counts']]
P=[int(x) for x in ns['P']]
N=[int(x) for x in ns['N']]
H=[int(x) for x in ns['H']]
Pc=[int(x) for x in ns['Pc']]
assert known.shape==(140,64) and D.shape==(64,)
assert len(cc)==len(ct)==len(forced)==len(P)==len(N)==140

# Exact Picard-class equations: sum_j x_j [C_j] = stripped D.
blocks=[csr_matrix(known.T)]
rhs=[*D.tolist()]
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
Aeq=vstack(blocks,format='csr'); beq=np.asarray(rhs,dtype=float)

# Bounded feasibility only. The strict coefficients are degree-bounded by H.D=96;
# 512 is a generous diagnostic cap for exceptional multiplicities.
res=milp(
    np.ones(140,dtype=float),
    integrality=np.ones(140,dtype=int),
    bounds=Bounds(np.zeros(140),np.full(140,512.0)),
    constraints=LinearConstraint(Aeq,beq,beq),
    options={'time_limit':120.0,'mip_rel_gap':0.0},
)

found=bool(res.x is not None and res.success)
out={
    'schema':'STAGE35_EX_GOAL4AJ_KNOWN_RESIDUAL_MILP_DIAGNOSTIC_V2',
    'bound_per_coefficient':512,
    'solver_success':bool(res.success),
    'solver_status':int(res.status),
    'solver_message':str(res.message),
    'q_invariant_nonnegative_retained140_stripped_decomposition_found':found,
    'literal_F_B_materialized':False,
    'local_evaluations_computed':False,
    'brauer_manin_obstruction_obtained':False,
    'E1_proved':False,
    'stage35_closed':False,
    'theorem_credit':False,
    'endpoint_credit':False,
}

if found:
    x=[int(round(v)) for v in res.x]
    def cls(coeff):
        return [sum(coeff[j]*known_int[j][u] for j in range(140)) for u in range(64)]
    def invariant(coeff):
        return all(coeff[j]==coeff[perm[j]-1] for perm in (cc,ct) for j in range(140))
    def support(coeff):
        return {str(j+1):v for j,v in enumerate(coeff) if v}
    def hdeg(coeff):
        return sum(v*(2 if j<32 else 4 if j<92 else 0) for j,v in enumerate(coeff))

    assert cls(x)==D_int and invariant(x) and all(v>=0 for v in x)
    assert hdeg(x)==96
    assert invariant(forced) and sum(forced)==325 and hdeg(forced)==4

    fullR=[forced[j]+x[j] for j in range(140)]
    Adiv=[P[j]+fullR[j] for j in range(140)]
    Bdiv=[N[j]+fullR[j] for j in range(140)]
    expected_R=[31*H[u]-Pc[u] for u in range(64)]
    expected_31H=[31*v for v in H]
    assert cls(fullR)==expected_R
    assert cls(Adiv)==expected_31H and cls(Bdiv)==expected_31H
    assert invariant(fullR) and invariant(Adiv) and invariant(Bdiv)
    assert hdeg(fullR)==100 and hdeg(Adiv)==496 and hdeg(Bdiv)==496
    assert all(v>=0 for v in fullR+Adiv+Bdiv)

    packet={
        'stripped_residual_support_1based':support(x),
        'forced_component_support_1based':support(forced),
        'full_common_residual_support_1based':support(fullR),
        'positive_part_support_1based':support(P),
        'negative_part_support_1based':support(N),
        'degree31_numerator_divisor_support_1based':support(Adiv),
        'degree31_denominator_divisor_support_1based':support(Bdiv),
    }
    canonical=json.dumps(packet,sort_keys=True,separators=(',',':')).encode()
    out.update({
        'exact_stripped_picard_recheck':True,
        'stripped_galois_symmetry_recheck':True,
        'stripped_residual_hyperplane_degree':96,
        'stripped_support_count':len(packet['stripped_residual_support_1based']),
        'forced_step_count':325,
        'forced_hyperplane_degree':4,
        'full_common_residual_hyperplane_degree':100,
        'full_common_residual_exact_class_31H_minus_Pc':True,
        'full_common_residual_galois_invariant':True,
        'numerator_divisor_exact_class_31H':True,
        'denominator_divisor_exact_class_31H':True,
        'numerator_divisor_hyperplane_degree':496,
        'denominator_divisor_hyperplane_degree':496,
        'numerator_divisor_galois_invariant':True,
        'denominator_divisor_galois_invariant':True,
        'divisor_packet_sha256':hashlib.sha256(canonical).hexdigest(),
        **packet,
    })

print('GOAL4AJ_KNOWN_RESIDUAL_MILP_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
print('GOAL4AJ_KNOWN_RESIDUAL_MILP_DONE')
