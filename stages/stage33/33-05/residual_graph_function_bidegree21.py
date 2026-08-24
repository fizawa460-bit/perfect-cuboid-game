#!/usr/bin/env python3
"""Bounded exact synthesis of the one residual graph direction q1=e1+e3.

The prior (1,1) search spans two of the three graph quotient directions.  This
leaf tests only the next bidegree (2,1), constructs one explicit same-bidegree
ratio with node parity q1, and stops.  It certifies the associated-graded graph
channel only; Creutz--Viray divisor conditions and extension mixing remain open.
"""
import hashlib
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parent
u1,v1,u2,v2=sp.symbols("u1 v1 u2 v2")

nodes={
 "e1":{u1:0,v1:1,u2:0,v2:1},
 "e2":{u1:0,v1:1,u2:1,v2:0},
 "e3":{u1:1,v1:1,u2:1,v2:1},
 "e4":{u1:1,v1:1,u2:-1,v2:1},
 "e5":{u1:-1,v1:1,u2:1,v2:1},
 "e6":{u1:-1,v1:1,u2:-1,v2:1},
 "e7":{u1:1,v1:0,u2:0,v2:1},
 "e8":{u1:1,v1:0,u2:1,v2:0},
}
labels=list(nodes)

# Two simple exact bidegree-(2,1) forms.  The first vanishes at e1 only;
# the second vanishes at e3 only among the eight branch-intersection nodes.
F_e1=sp.expand(u1**2*u2 + u1**2*v2 + u2*v1**2)
F_e3=sp.expand(u1**2*u2 - u1**2*v2 + u1*u2*v1 + u1*v1*v2 - u2*v1**2 - v1**2*v2)


def bidegrees(poly):
    return sorted({(ex[0]+ex[1],ex[2]+ex[3]) for ex,_ in sp.Poly(poly,u1,v1,u2,v2).terms()})

if bidegrees(F_e1)!=[(2,1)] or bidegrees(F_e3)!=[(2,1)]:
    raise SystemExit("bidegree regression")


def support(poly):
    return [lab for lab in labels if sp.expand(poly.subs(nodes[lab]))==0]

s1=support(F_e1); s3=support(F_e3)
if s1 != ["e1"] or s3 != ["e3"]:
    raise SystemExit(f"singleton-support regression: {s1}, {s3}")

# The ratio therefore has odd node order exactly on e1 and e3.  In the stable
# graph quotient basis q1=e1+e3, q2=e1+e5, q3=e1+e7 this is precisely q1.
ratio=sp.cancel(F_e1/F_e3)
node_parity=[int(lab in {"e1","e3"}) for lab in labels]
qcoords=[1,0,0]

# Regression against the previous low-degree 2D span <q3, q1+q2+q3>.
low=json.loads((ROOT/"lowdegree-graph-functions.json").read_text())
if low["lowdegree_ratio_graph_quotient_span_dimension"] != 2:
    raise SystemExit("low-degree graph span regression")
selected=[x["graph_quotient_coordinates_q1_q2_q3"] for x in low["selected_explicit_lowdegree_graph_functions"]]
if selected != [[1,1,1],[0,0,1]]:
    raise SystemExit("prior selected quotient coordinates regressed")


def rank2(rows):
    a=[r[:] for r in rows]; rr=0
    if not a:return 0
    for c in range(len(a[0])):
        p=next((i for i in range(rr,len(a)) if a[i][c]),None)
        if p is None:continue
        a[rr],a[p]=a[p],a[rr]
        for i in range(len(a)):
            if i!=rr and a[i][c]: a[i]=[x^y for x,y in zip(a[i],a[rr])]
        rr+=1
    return rr

if rank2(selected+[qcoords]) != 3:
    raise SystemExit("residual q1 did not complete graph quotient")

# B+/- have bidegree (2,2); a nonzero (2,1) form cannot contain either entire
# branch component.  This only prevents the trivial denominator/numerator
# pathology; it is not the full Creutz--Viray divisor check.
cert={
 "schema":"STAGE33_05_RESIDUAL_GRAPH_FUNCTION_BIDEGREE21_V1",
 "source_lock":{"lowdegree_graph_functions_sha256":low["canonical_sha256"]},
 "searched_bidegree":[2,1],
 "bounded_search_only":True,
 "numerator":sp.sstr(F_e1),
 "denominator":sp.sstr(F_e3),
 "function":sp.sstr(ratio),
 "numerator_node_support":s1,
 "denominator_node_support":s3,
 "node_parity_e1_to_e8":node_parity,
 "graph_quotient_coordinates_q1_q2_q3":qcoords,
 "prior_lowdegree_graph_span_dimension":2,
 "completed_associated_graded_graph_span_dimension":3,
 "associated_graded_graph_channel_complete":True,
 "associated_graded_LcE_has_explicit_function_for_all_5_directions":True,
 "creutz_viray_divisor_conditions_complete":False,
 "extension_mixing_complete":False,
 "explicit_actual_LcE_basis_materialized":False,
 "xalpha_matrix_materialized":False,
 "q_relevant_surviving_dimension_certified":False,
 "next_exact_leaf":"L33-05-CHECK-5-FUNCTION-CV-DIVISORS-AND-EXTENSION-MIXING-THEN-XALPHA",
 "theorem_credit":False,
 "endpoint_credit":False,
}
canonical=json.dumps(cert,sort_keys=True,separators=(",",":")).encode()
cert["canonical_sha256"]=hashlib.sha256(canonical).hexdigest()
(ROOT/"residual-graph-function-bidegree21.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({
 "success":True,
 "residual_graph_function":cert["function"],
 "graph_coordinates":qcoords,
 "completed_graph_span_dimension":3,
 "associated_graded_explicit_function_count":5,
 "next_exact_leaf":cert["next_exact_leaf"],
 "certificate_sha256":cert["canonical_sha256"],
},indent=2,sort_keys=True))
