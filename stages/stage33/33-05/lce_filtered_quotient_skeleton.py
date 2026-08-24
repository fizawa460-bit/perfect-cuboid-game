#!/usr/bin/env python3
"""Exact filtered quotient skeleton for the corrected 5D Creutz--Viray space.

This certifies the associated-graded decomposition after quotienting the eight
special-fiber K* directions (one squareclass relation), and materializes the two
Jacobian quotient functions.  It deliberately does not claim that the three
graph-cycle functions or the x-alpha matrix have yet been synthesized.
"""
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent
t = sp.symbols("t")
s2 = sp.sqrt(2)
q = sp.expand(t**4 - 6*t**2 + 1)
roots = [1+s2, -(1+s2), s2-1, 1-s2]
assert sp.expand(sp.prod(t-r for r in roots) - q) == 0

# Choose r4 as base branch point.  On z^2=q(t), each ratio has divisor twice
# a difference of ramification points and hence represents Jac[2].
r1, r2, r3, r4 = roots
f1 = sp.cancel((t-r1)/(t-r4))
f2 = sp.cancel((t-r2)/(t-r4))
f3 = sp.cancel((t-r3)/(t-r4))
# f1*f2*f3 is q/(t-r4)^4, a square in the common normalization because z^2=q.
assert sp.cancel(f1*f2*f3 - q/(t-r4)**4) == 0

# Raw filtration coordinates over F2:
#   J+_1,J+_2,J-_1,J-_2, h1,...,h7, ell1
# with h_j=e_j+e8 a basis of H1(Gamma), Gamma=two vertices with 8 edges.
raw_dim = 12
Jp1,Jp2,Jm1,Jm2 = range(4)
h0 = 4
ell1 = 11

def vec(*inds):
    v=[0]*raw_dim
    for i in inds: v[i]^=1
    return v

# K*/K*2 -> L*/L*2 relations at filtration level.
# Four smooth common ramification fibers identify the two component Jac[2]
# summands; the q squareclass removes the third apparent root relation, leaving 2.
diag_jac = [vec(Jp1,Jm1), vec(Jp2,Jm2)]

# Nodal special fibers t=0,1,-1,infinity occur in edge pairs
# (e1,e2),(e3,e4),(e5,e6),(e7,e8). In the h_j=e_j+e8 basis these are:
nodal_graph = [
    vec(h0+0,h0+1),
    vec(h0+2,h0+3),
    vec(h0+4,h0+5),
    vec(h0+6),
]

# The eighth special-fiber direction has nonzero ell1 graded coordinate.  Its
# lower-filtration mixing is not needed for the associated-graded dimension;
# record only the leading ell1 direction rather than inventing a lift.
ell_relation_leading = vec(ell1)
relations = diag_jac + nodal_graph + [ell_relation_leading]


def rank2(rows):
    a=[r[:] for r in rows]; m=len(a); n=len(a[0]) if a else 0; rr=0
    for c in range(n):
        p=next((i for i in range(rr,m) if a[i][c]),None)
        if p is None: continue
        a[rr],a[p]=a[p],a[rr]
        for i in range(m):
            if i!=rr and a[i][c]: a[i]=[x^y for x,y in zip(a[i],a[rr])]
        rr+=1
    return rr

assert rank2(diag_jac)==2
assert rank2(nodal_graph)==4
assert rank2(relations)==7
assert raw_dim-rank2(relations)==5

# Graph quotient H1(Gamma)/<four nodal pair cycles> has dimension 3.
graph_rel = [r[h0:h0+7] for r in nodal_graph]
assert rank2(graph_rel)==4
graph_quot_dim = 7-rank2(graph_rel)
assert graph_quot_dim==3

# Convenient quotient cycle labels.  These are classes, not yet explicit
# rational functions ell_C on the normalization.
graph_quotient_cycle_reps = [
    "e1+e3",
    "e1+e5",
    "e1+e7",
]

cert={
    "schema":"STAGE33_05_LCE_FILTERED_QUOTIENT_SKELETON_V1",
    "source_lock":{
        "creutz_viray":"Proposition 4.4, Lemma 6.6, Theorem 5.2 of On Brauer groups of double covers of ruled surfaces",
        "common_normalization":"z^2=t^4-6*t^2+1",
    },
    "raw_LE_mod_squares_dimension":12,
    "raw_filtration_dimensions":{
        "Jac_B_2":4,
        "H1_Gamma":7,
        "ell1":1,
        "ellc":0,
    },
    "Ktimes_relation_dimension":7,
    "Ktimes_relation_associated_graded":{
        "diagonal_Jac_dimension":2,
        "nodal_pair_cycle_dimension":4,
        "ell1_leading_dimension":1,
    },
    "LcE_dimension":5,
    "LcE_associated_graded_quotient":{
        "Jac_quotient_dimension":2,
        "graph_quotient_dimension":3,
        "ell1_quotient_dimension":0,
    },
    "explicit_jacobian_quotient_functions": [
        {"class":"J1","pair_in_L":"(f1,1)","f1":sp.sstr(f1)},
        {"class":"J2","pair_in_L":"(f2,1)","f2":sp.sstr(f2)},
    ],
    "jacobian_diagonal_identification":"(f,1)=(1,f) modulo diagonal K* and squares",
    "third_branch_ratio_relation":"f1*f2*f3=q/(t-r4)^4 is square on z^2=q",
    "graph_quotient_cycle_representatives":graph_quotient_cycle_reps,
    "explicit_graph_cycle_functions_materialized":False,
    "full_explicit_LcE_basis_materialized":False,
    "associated_graded_cc_action_on_quotient":"identity",
    "full_LcE_cc_action_materialized":False,
    "xalpha_matrix_materialized":False,
    "q_relevant_surviving_dimension_certified":False,
    "next_exact_leaf":"L33-05-SYNTHESIZE-3-GRAPH-FUNCTIONS-THEN-XALPHA",
    "theorem_credit":False,
    "endpoint_credit":False,
}
canonical=json.dumps(cert,sort_keys=True,separators=(",",":")).encode()
cert["canonical_sha256"]=hashlib.sha256(canonical).hexdigest()
(ROOT/"lce-filtered-quotient-skeleton.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({
    "success":True,
    "LcE_dimension":5,
    "Jac_quotient_dimension":2,
    "graph_quotient_dimension":3,
    "explicit_jacobian_functions":2,
    "remaining_graph_function_count":3,
    "next_exact_leaf":cert["next_exact_leaf"],
    "certificate_sha256":cert["canonical_sha256"],
},indent=2,sort_keys=True))
