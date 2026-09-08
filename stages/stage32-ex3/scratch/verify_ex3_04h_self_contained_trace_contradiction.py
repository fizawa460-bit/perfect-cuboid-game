#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ART = ROOT / "stages/stage32-ex3/scratch/ex3-04h-self-contained-trace-contradiction.json"

def blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def canonical_without(obj: dict, field: str = "canonical_sha256_without_this_field") -> str:
    x = dict(obj)
    x.pop(field, None)
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

a = json.loads(ART.read_text())
assert a["schema"] == "STAGE32EX3_EX3_04H_SELF_CONTAINED_TRACE_CONTRADICTION_V1"
assert a["status"] == "SCRATCH_PROVISIONAL_SELF_CONTAINED_TERMINAL_GATE_NOT_RETAINED_NOT_AUDITED"
assert canonical_without(a) == a["canonical_sha256_without_this_field"]
assert a["fixed_target"]["projection_degrees"] == [105, 81]
assert a["fixed_target"]["surviving_marked_residues"] == [73, 97, 235]

L = a["source_locks"]
paths = {k: ROOT / v["path"] for k,v in L.items()}
for k,v in L.items():
    assert blob(paths[k]) == v["blob_sha1"], f"blob drift: {k}"
for k in ["typed_cover_tower","relative_H_marking","v6_witness","physical_C1_node_incidence",
          "resolved_double_cover_blowdown_adapter","common_cover_identity","q602_trace_spectrum"]:
    obj = json.loads(paths[k].read_text())
    if "canonical_sha256_without_this_field" in obj:
        got = canonical_without(obj)
    else:
        got = obj.get("canonical_sha256")
    assert got == L[k]["canonical_sha256"], f"canonical drift: {k}"

tower = json.loads(paths["typed_cover_tower"].read_text())
assert tower["fixed_target"]["O"] == 210 and tower["fixed_target"]["qprime"] == 4
assert tower["degree_adapter"]["n_pair_D_to_X8"] == [105,81]
assert tower["common_cover_identity"]["same_quadratic_extension"] is True

note = paths["modular_graph_source_note"].read_text()
for marker in ["arXiv:1009.0388","Section 4","Section 7","u^2=2xy","v^2=x^2-y^2","w^2=x^2+y^2",
               "U=2*b1","V=2*b2","W=2*b3","X=a1+c","Y=-a1+c","T=a2+i*a3","Zc=a2-i*a3",
               "32 conics","six singularities"]:
    assert marker in note

rel = json.loads(paths["relative_H_marking"].read_text())
v6 = json.loads(paths["v6_witness"].read_text())
tang = json.loads(paths["physical_C1_node_incidence"].read_text())
blow = json.loads(paths["resolved_double_cover_blowdown_adapter"].read_text())
common = json.loads(paths["common_cover_identity"].read_text())
qtrace = json.loads(paths["q602_trace_spectrum"].read_text())

assert rel["modular_to_stoll"]["u=TTprime"] == "g7*g9"
assert rel["modular_to_stoll"]["v=RT"] == "g7*g8"
assert rel["modular_to_stoll"]["uv=RTprime"] == "g8*g9"
H = {"1":(1,1,1),"u_H":(-1,1,-1),"v_H":(-1,-1,1),"u_H*v_H":(1,-1,-1)}
signs = [(e1,e2,e3) for e1 in (1,-1) for e2 in (1,-1) for e3 in (1,-1)]
indices = []
for eps_u,eps_v,eps_w in H.values():
    e = (-eps_v,-eps_u,-eps_w)
    indices.append(17 + signs.index(e))
assert indices == [24,21,18,19] == a["graph_geometry"]["C1_indices"]

side_nodes = defaultdict(set)
for ex in tang["exceptional_models"]:
    j = int(ex["exceptional_id"].split("_")[1])
    for rec in ex["physical_crossing_tangent_coordinates"]:
        side_nodes[int(rec["side_index_1based"])].add(j)
assert all(len(side_nodes[s]) == 6 for s in range(1,25))

pair = v6["witness"]["all140_pairings"]
mult = pair[92:140]
assert len(pair) == 140 and len(mult) == 48 and sum(mult) == 266
c_dot_k = [pair[s-1] for s in indices]
mass = [sum(mult[j-1] for j in side_nodes[s]) for s in indices]
assert c_dot_k == [0,0,14,9]
assert mass == [41,41,24,34]

adapter = blow["resolved_double_cover_adapter"]
assert adapter["resolved_quotient"] == "pi:Xtilde->Btilde finite degree 2, branched on the 48 exceptional curves"
assert adapter["upstairs_strict_transform"] == "Dtilde=pi^*C"
assert adapter["exceptional_contact_formula"] == "Dtilde.Etilde_j=C.E_j=m_j"
d_dot_l = [2*x+y for x,y in zip(c_dot_k,mass)]
gamma = [4*x for x in d_dot_l]
assert d_dot_l == [41,41,52,52]
assert gamma == [164,164,208,208]

gsq = common["group_quotient_square"]
assert gsq["P"] == "Z x Z with diagonal G action"
assert gsq["H"] == "Gamma'[4]/Gamma[8] ~= V4, order 4, normal index 2"
assert gsq["X"] == "P/H_diag (Beauville cover surface)"
assert gsq["C0"] == "Z/H"
assert common["verdict"]["common_double_cover_identity_for_actual_carrier"] is True

A = [186-x for x in gamma]
assert A == [22,22,-22,-22]
chars = {
    "trivial":[1,1,1,1],
    "chi_u":[1,-1,1,-1],
    "chi_v":[1,1,-1,-1],
    "chi_uv":[1,-1,-1,1],
}
blocks = {k: sum(c*x for c,x in zip(row,A))//4 for k,row in chars.items()}
assert blocks == {"trivial":0,"chi_u":0,"chi_v":22,"chi_uv":0}
assert a["graph_geometry"]["H_character_linear_traces"] == blocks
assert a["graph_geometry"]["forced_downstairs_trace"] == 0

assert qtrace["fixed_target"]["Q"] == 602
assert qtrace["rational_trace"]["gauge_invariant_by_conjugation"] is True
assert qtrace["rational_trace"]["trace_mod8"] == 4
allowed = qtrace["exact_spectrum"]["trace_values"]
assert allowed == [-68,-60,-52,-44,-36,-28,-20,-12,-4,4,12,20,28,36,44,52,60,68]
assert 0 not in allowed and blocks["trivial"] == 0
assert a["q602_contradiction"]["contradiction"] is True

dom = a["population_domination"]
assert dom["finite_monodromy_sample_used"] is False
assert dom["does_not_claim_those_enumerations_were_run"] is True
assert dom["all_fixed_O210_cover_configurations_disposed_if_source_chain_is_accepted"] is True
assert a["verdict"]["self_contained_without_scratch_prym_dependency"] is True
assert a["verdict"]["provisional_terminal_candidate"] == "O210_COVER_GEOMETRY_EXCLUDED"
for k in ["hostile_audit_credit","stage32_main_credit","retained_consolidation_performed",
          "merge_authorized","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"]:
    assert a["firewalls"][k] is False

print(json.dumps({
    "success": True,
    "C1_indices": indices,
    "C_dot_K": c_dot_k,
    "incident_node_mass": mass,
    "GammaP_dot_Graph": gamma,
    "twisted_linear_traces": A,
    "H_character_linear_traces": blocks,
    "Q602_zero_allowed": False,
    "self_contained_without_scratch_prym_dependency": True,
    "provisional_terminal_candidate": "O210_COVER_GEOMETRY_EXCLUDED",
    "retained": False,
    "hostile_audited": False
}, indent=2, sort_keys=True))
