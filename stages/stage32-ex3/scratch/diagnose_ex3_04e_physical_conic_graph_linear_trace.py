#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from collections import defaultdict, Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
V6 = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
TANG = ROOT / "stages/stage33/33-07/exceptional-p1-tangent-coordinates.json"
GATE = ROOT / "stages/stage32-ex3/scratch/ex3-04d-upstairs-h4-prym-rosati-fourier-gate.json"
OUT = ROOT / "stages/stage32-ex3/scratch/ex3-04e-physical-conic-graph-linear-trace.json"

v6 = json.loads(V6.read_text())
tang = json.loads(TANG.read_text())
gate = json.loads(GATE.read_text())

pair = v6["witness"]["all140_pairings"]
assert len(pair) == 140
mult = pair[92:140]
assert len(mult) == 48
assert sum(mult) == 266
forced=gate["elliptic_prym_consequence"]["forced_degrees_by_retained_character"]
assert {k:v["degree"] for k,v in forced.items()} == {"chi_u":9,"chi_v":137,"chi_uv":9}

# Reconstruct exact first-24 physical C1 side -> six singular points from the
# checked-in Stage33 tangent certificate. Every incidence entry is source-locked
# to the pinned Testa-Stoll model by that certificate.
side_nodes: dict[int,set[int]] = defaultdict(set)
for ex in tang["exceptional_models"]:
    j = int(ex["exceptional_id"].split("_")[1])
    assert 1 <= j <= 48
    for rec in ex["physical_crossing_tangent_coordinates"]:
        side = int(rec["side_index_1based"])
        assert 1 <= side <= 24
        side_nodes[side].add(j)

assert sorted(side_nodes) == list(range(1,25))
assert all(len(side_nodes[s]) == 6 for s in range(1,25))

rows=[]
for s in range(1,25):
    nodes=sorted(side_nodes[s])
    c_dot_k=pair[s-1]
    node_mass=sum(mult[j-1] for j in nodes)
    d_dot_kx=2*c_dot_k+node_mass
    graph_intersection=4*d_dot_kx
    linear_trace=105+81-graph_intersection
    rows.append({
        "side_index_1based":s,
        "C_dot_K":c_dot_k,
        "exceptional_nodes_1based":nodes,
        "node_multiplicity_sum":node_mass,
        "D_dot_KX":d_dot_kx,
        "GammaP_dot_graph_candidate":graph_intersection,
        "H1_linear_trace_candidate":linear_trace,
    })

# A true H-orbit of four graph curves has four trace values A_h. Fourier
# inversion over H gives block traces. We do NOT know which physical sides are
# the four graphs, or their H labels, so exhaust ordered choices from these 24
# only as a bounded diagnostic. The trivial block is deliberately left free;
# constrain only the three nontrivial elliptic block traces by EX3-04d.
vals={r["side_index_1based"]:r["H1_linear_trace_candidate"] for r in rows}
allowed_137={-22,-8,8,22}
allowed_9={-6,0,6}
chars={
    "trivial": [1,1,1,1],
    # retained F2 labels converted to +/-1 values on [1,u,v,uv]
    "chi_u": [1,-1,1,-1],
    "chi_v": [1,1,-1,-1],
    "chi_uv":[1,-1,-1,1],
}
compatible=[]
# Ordered [1,u,v,uv]; graph sides must be distinct.
for ids in itertools.permutations(range(1,25),4):
    A=[vals[i] for i in ids]
    sums={name:sum(a*b for a,b in zip(row,A)) for name,row in chars.items()}
    if any(x%4 for x in sums.values()):
        continue
    blocks={name:x//4 for name,x in sums.items()}
    if blocks["chi_v"] not in allowed_137:
        continue
    if blocks["chi_u"] not in allowed_9 or blocks["chi_uv"] not in allowed_9:
        continue
    compatible.append({"graph_side_ids_order_1_u_v_uv":list(ids),"linear_traces_order_1_u_v_uv":A,"block_linear_traces":blocks})

out={
    "schema":"STAGE32EX3_EX3_04E_PHYSICAL_C1_GRAPH_LINEAR_TRACE_SCRATCH_V1",
    "status":"SCRATCH_PROVISIONAL_DIAGNOSTIC_NOT_RETAINED",
    "scope":"FIRST_24_PHYSICAL_C1_CONICS_ONLY_NOT_ALL_32_MODULAR_GRAPH_CONICS",
    "formulae":{
        "D_dot_KX":"2*(C.K)+sum_{six branch nodes} m_j",
        "GammaP_dot_Graph":"4*(D.KX)=8*(C.K)+4*sum m_j",
        "linear_trace_candidate":"105+81-GammaP.Graph",
    },
    "rows":rows,
    "trace_histogram":dict(sorted(Counter(vals.values()).items())),
    "bounded_four_graph_search":{
        "ordered_distinct_quadruple_count":24*23*22*21,
        "compatible_count":len(compatible),
        "compatible_first_200":compatible[:200],
        "truncated":len(compatible)>200,
        "constraints":"chi_v trace in +-22,+-8 (norm137); chi_u,chi_uv traces in -6,0,6 (norm9)",
        "exclusion_credit":False,
        "reason":"The true H graph curves are not yet identified among the 32 modular C1 conics, and the last c=0 block of eight is absent from this first-pass set."
    },
    "firewalls":{
        "physical_side_promoted_to_actual_H_graph":False,
        "missing_eight_c0_conics_ignored_for_exclusion":False,
        "O210_excluded":False,
        "Q602_excluded":False,
        "stage32_main_credit":False,
        "claim_dag_sync_triggered_by_this_scratch":False,
        "merge_authorized":False,
    }
}
OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps({
    "success":True,
    "trace_histogram":out["trace_histogram"],
    "min_trace":min(vals.values()),
    "max_trace":max(vals.values()),
    "compatible_count":len(compatible),
    "first_20":compatible[:20],
},indent=2,sort_keys=True))
