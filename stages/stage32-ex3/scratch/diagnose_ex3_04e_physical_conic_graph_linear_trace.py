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
QTRACE = ROOT / "stages/stage32/residual-32-01-production/post1518-o210-q602-residue73-trace-spectrum.json"
OUT = ROOT / "stages/stage32-ex3/scratch/ex3-04e-physical-conic-graph-linear-trace.json"

v6 = json.loads(V6.read_text())
tang = json.loads(TANG.read_text())
gate = json.loads(GATE.read_text())
qtrace = json.loads(QTRACE.read_text())

pair = v6["witness"]["all140_pairings"]
assert len(pair) == 140
mult = pair[92:140]
assert len(mult) == 48
assert sum(mult) == 266
forced=gate["elliptic_prym_consequence"]["forced_degrees_by_retained_character"]
assert {k:v["degree"] for k,v in forced.items()} == {"chi_u":9,"chi_v":137,"chi_uv":9}
assert qtrace["fixed_target"]["Q"] == 602
assert qtrace["audited_input"]["canonical_residue_decimal"] == 73
assert qtrace["rational_trace"]["gauge_invariant_by_conjugation"] is True
q602_traces=set(qtrace["exact_spectrum"]["trace_values"])
assert q602_traces == set(range(-68,69,8))

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
# inversion over H gives one trivial block (the descended Bolza correspondence)
# and three nontrivial elliptic Prym blocks. We do NOT yet know which C1 curves
# are the four graphs, so this is a bounded localization diagnostic only.
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
norm_compatible=[]
q602_compatible=[]
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
    rec={"graph_side_ids_order_1_u_v_uv":list(ids),"linear_traces_order_1_u_v_uv":A,"block_linear_traces":blocks}
    norm_compatible.append(rec)
    if blocks["trivial"] in q602_traces:
        q602_compatible.append(rec)

out={
    "schema":"STAGE32EX3_EX3_04E_PHYSICAL_C1_GRAPH_LINEAR_TRACE_SCRATCH_V2",
    "status":"SCRATCH_PROVISIONAL_DIAGNOSTIC_NOT_RETAINED",
    "scope":"FIRST_24_PHYSICAL_C1_CONICS_ONLY_NOT_ALL_32_MODULAR_GRAPH_CONICS",
    "source_locks":{
        "q602_trace_spectrum":{
            "path":"stages/stage32/residual-32-01-production/post1518-o210-q602-residue73-trace-spectrum.json",
            "canonical_sha256":qtrace["canonical_sha256_without_this_field"],
            "canonical_residue":73,
            "trace_values":sorted(q602_traces),
            "gauge_invariant_by_conjugation":True
        }
    },
    "formulae":{
        "D_dot_KX":"2*(C.K)+sum_{six branch nodes} m_j",
        "GammaP_dot_Graph":"4*(D.KX)=8*(C.K)+4*sum m_j",
        "linear_trace_candidate":"105+81-GammaP.Graph",
        "H_fourier_trivial_block":"(A_1+A_u+A_v+A_uv)/4 = Tr_Q(T_downstairs)"
    },
    "rows":rows,
    "trace_histogram":dict(sorted(Counter(vals.values()).items())),
    "bounded_four_graph_search":{
        "ordered_distinct_quadruple_count":24*23*22*21,
        "norm_only_compatible_count":len(norm_compatible),
        "q602_trace_compatible_count":len(q602_compatible),
        "q602_trace_compatible":q602_compatible,
        "constraints":"chi_v trace in +-22,+-8 (norm137); chi_u,chi_uv traces in -6,0,6 (norm9); trivial trace in exact Q602 residue73 spectrum, valid across current 73/97/235 gauge orbit by conjugation invariance",
        "localization_if_zero":"If q602_trace_compatible_count=0, the four true H graph curves cannot all lie in physical C1 sides 1..24; at least one lies in the missing c=0 block 25..32. This is localization, not O210 exclusion.",
        "exclusion_credit":False,
        "reason":"The true H graph curves are not yet identified among all 32 modular C1 conics, and the last c=0 block of eight is absent from this first-pass incidence set."
    },
    "firewalls":{
        "physical_side_promoted_to_actual_H_graph":False,
        "missing_eight_c0_conics_ignored_for_exclusion":False,
        "localization_promoted_to_O210_exclusion":False,
        "O210_excluded":False,
        "Q602_excluded":False,
        "stage32_main_credit":False,
        "claim_dag_sync_triggered_by_this_scratch":False,
        "merge_authorized":False
    }
}
OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps({
    "success":True,
    "trace_histogram":out["trace_histogram"],
    "norm_only_compatible_count":len(norm_compatible),
    "q602_trace_compatible_count":len(q602_compatible),
    "q602_compatible":q602_compatible,
},indent=2,sort_keys=True))
