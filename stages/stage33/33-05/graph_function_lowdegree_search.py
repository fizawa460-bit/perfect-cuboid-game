#!/usr/bin/env python3
"""Exact low-degree graph-function search for the corrected 3D graph quotient.

This only certifies associated-graded node-parity classes.  It does not promote
these functions to a full L_{c,E} basis until the Creutz--Viray divisor and
extension conditions are checked together with the remaining graph direction.
"""
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent
u1,v1,u2,v2 = sp.symbols("u1 v1 u2 v2")

# Stable node labels from normalization_galois_skeleton.py.
nodes = {
    "e1": {u1:0,v1:1,u2:0,v2:1},
    "e2": {u1:0,v1:1,u2:1,v2:0},
    "e3": {u1:1,v1:1,u2:1,v2:1},
    "e4": {u1:1,v1:1,u2:-1,v2:1},
    "e5": {u1:-1,v1:1,u2:1,v2:1},
    "e6": {u1:-1,v1:1,u2:-1,v2:1},
    "e7": {u1:1,v1:0,u2:0,v2:1},
    "e8": {u1:1,v1:0,u2:1,v2:0},
}
labels=list(nodes)

forms = [
    ("F01", u1*(v2-u2)),
    ("F02", u1*(v2+u2)),
    ("F03", u2*(v1-u1)),
    ("F04", v1*u2-u1*v2),
    ("F05", v1*u2+u1*v2),
    ("F06", u2*(v1+u1)),
    ("F07", v2*(v1-u1)),
    ("F08", v1*v2-u1*u2),
    ("F09", v1*v2+u1*u2),
    ("F10", v2*(v1+u1)),
    ("F11", v1*(v2-u2)),
    ("F12", v1*(v2+u2)),
]

def bidegree(poly):
    out=set()
    for exps,_ in sp.Poly(sp.expand(poly),u1,v1,u2,v2).terms():
        out.add((exps[0]+exps[1],exps[2]+exps[3]))
    return out

supports=[]
for name,f in forms:
    assert bidegree(f)=={(1,1)}
    supp=[lab for lab in labels if sp.expand(f.subs(nodes[lab]))==0]
    if len(supp)!=4:
        raise SystemExit(f"{name} does not vanish at exactly four nodes: {supp}")
    supports.append(supp)
if len({tuple(s) for s in supports}) != 12:
    raise SystemExit("low-degree node supports are not distinct")

# H1(Gamma,F2) basis h_j=e_j+e8, j=1..7.  Every four-node support has even
# cardinality, hence its graph parity vector is just the first seven bits.
def hvec(supp):
    S=set(supp)
    return [int(f"e{j}" in S) for j in range(1,8)]

# Four nodal special-fiber relations already quotiented in LcE.
relations=[
    [1,1,0,0,0,0,0],
    [0,0,1,1,0,0,0],
    [0,0,0,0,1,1,0],
    [0,0,0,0,0,0,1],
]
# Convenient graph quotient basis from the prior exact leaf:
# q1=e1+e3, q2=e1+e5, q3=e1+e7.
qbasis=[
    [1,0,1,0,0,0,0],
    [1,0,0,0,1,0,0],
    [1,0,0,0,0,0,1],
]

def rank2(rows):
    if not rows: return 0
    a=[r[:] for r in rows]; rr=0; n=len(a[0])
    for c in range(n):
        p=next((i for i in range(rr,len(a)) if a[i][c]),None)
        if p is None: continue
        a[rr],a[p]=a[p],a[rr]
        for i in range(len(a)):
            if i!=rr and a[i][c]: a[i]=[x^y for x,y in zip(a[i],a[rr])]
        rr+=1
    return rr

def inspan(v, rows):
    return rank2(rows+[v])==rank2(rows)

def qcoords(v):
    for mask in range(8):
        w=[0]*7
        coeff=[]
        for j,b in enumerate(qbasis):
            bit=(mask>>j)&1; coeff.append(bit)
            if bit: w=[x^y for x,y in zip(w,b)]
        if inspan([x^y for x,y in zip(v,w)], relations):
            return coeff
    raise SystemExit("vector escaped graph quotient basis")

base_name,base_form=forms[0]
ratio_records=[]
ratio_vectors=[]
for idx in range(1,len(forms)):
    name,f=forms[idx]
    v=[a^b for a,b in zip(hvec(supports[idx]),hvec(supports[0]))]
    ratio_vectors.append(v)
    ratio_records.append({
        "ratio_id": f"{name}_OVER_{base_name}",
        "function": sp.sstr(sp.cancel(f/base_form)),
        "numerator": sp.sstr(f),
        "denominator": sp.sstr(base_form),
        "node_parity_h1": v,
        "graph_quotient_coordinates_q1_q2_q3": qcoords(v),
    })

ambient_rank=rank2(relations)
full_rank=rank2(relations+ratio_vectors)-ambient_rank
if full_rank!=2:
    raise SystemExit(f"expected low-degree quotient span rank 2, got {full_rank}")

selected=[]; basis=relations[:]; r=rank2(basis)
for rec,v in zip(ratio_records,ratio_vectors):
    nr=rank2(basis+[v])
    if nr>r:
        selected.append(rec); basis.append(v); r=nr
    if len(selected)==2: break
if len(selected)!=2:
    raise SystemExit("failed to extract two low-degree graph directions")
# With the stable enumeration above the selected functions are F03/F01 and
# F04/F01, giving q1+q2+q3 and q3 respectively.
if [x["graph_quotient_coordinates_q1_q2_q3"] for x in selected] != [[1,1,1],[0,0,1]]:
    raise SystemExit("selected graph quotient coordinates regressed")

cert={
    "schema":"STAGE33_05_LOWDEGREE_GRAPH_FUNCTION_SEARCH_V1",
    "node_labels":nodes and labels,
    "candidate_bidegree_11_form_count":12,
    "candidate_forms":[{"id":n,"form":sp.sstr(f),"node_support":s} for (n,f),s in zip(forms,supports)],
    "base_form":{"id":base_name,"form":sp.sstr(base_form)},
    "graph_quotient_dimension":3,
    "lowdegree_ratio_graph_quotient_span_dimension":2,
    "selected_explicit_lowdegree_graph_functions":selected,
    "selected_span":"<q3, q1+q2+q3> = <q3, q1+q2>",
    "remaining_associated_graded_graph_dimension":1,
    "remaining_direction_can_be_taken_as":"q1=e1+e3 (equivalently q2 modulo the selected span)",
    "full_explicit_LcE_basis_materialized":False,
    "creutz_viray_divisor_conditions_for_selected_functions_complete":False,
    "extension_mixing_complete":False,
    "xalpha_matrix_materialized":False,
    "q_relevant_surviving_dimension_certified":False,
    "next_exact_leaf":"L33-05-SYNTHESIZE-ONE-RESIDUAL-GRAPH-FUNCTION-AND-CHECK-CV-DIVISORS-THEN-XALPHA",
    "theorem_credit":False,
    "endpoint_credit":False,
}
canonical=json.dumps(cert,sort_keys=True,separators=(",",":")).encode()
cert["canonical_sha256"]=hashlib.sha256(canonical).hexdigest()
(ROOT/"lowdegree-graph-functions.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({
    "success":True,
    "candidate_forms":12,
    "lowdegree_graph_span_dimension":2,
    "remaining_graph_dimension":1,
    "selected_functions":[x["function"] for x in selected],
    "selected_coordinates":[x["graph_quotient_coordinates_q1_q2_q3"] for x in selected],
    "next_exact_leaf":cert["next_exact_leaf"],
    "certificate_sha256":cert["canonical_sha256"],
},indent=2,sort_keys=True))
