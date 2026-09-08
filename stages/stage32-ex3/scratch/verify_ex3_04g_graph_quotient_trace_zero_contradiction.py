#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ART = ROOT / "stages/stage32-ex3/scratch/ex3-04g-graph-quotient-trace-zero-contradiction.json"
NOTE = ROOT / "stages/stage32-ex3/scratch/ex3-04g-graph-quotient-trace-zero-source-note.md"
REL = ROOT / "stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-x-relative-h-marked-node-action.json"
LOC = ROOT / "stages/stage33/33-12/diagnose_e3_v91c1v_actual_prime_known140_locator.py"
V6 = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
TANG = ROOT / "stages/stage33/33-07/exceptional-p1-tangent-coordinates.json"
BLOW = ROOT / "stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-beauville-blowup-picard-adapter-delta-lock.json"
COMMON = ROOT / "stages/stage32/residual-32-01-production/post1484-o210-q4-common-double-cover-cartesian-identity.json"
QTRACE = ROOT / "stages/stage32/residual-32-01-production/post1518-o210-q602-residue73-trace-spectrum.json"
PRYM = ROOT / "stages/stage32-ex3/scratch/ex3-04d-upstairs-h4-prym-rosati-fourier-gate.json"


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


art = json.loads(ART.read_text())
rel = json.loads(REL.read_text())
v6 = json.loads(V6.read_text())
tang = json.loads(TANG.read_text())
blow = json.loads(BLOW.read_text())
common = json.loads(COMMON.read_text())
qtrace = json.loads(QTRACE.read_text())
prym = json.loads(PRYM.read_text())
note = NOTE.read_text()

assert art["schema"] == "STAGE32EX3_EX3_04G_GRAPH_QUOTIENT_TRACE_ZERO_CONTRADICTION_SCRATCH_V1"
assert art["status"] == "SCRATCH_PROVISIONAL_TERMINAL_CANDIDATE_NOT_RETAINED_NOT_AUDITED"
assert art["fixed_target"]["row_id"] == "g1-d186"
assert art["fixed_target"]["O"] == 210
assert art["fixed_target"]["qprime"] == 4
assert art["fixed_target"]["projection_degrees"] == [105, 81]
assert art["fixed_target"]["Q"] == 602
assert art["fixed_target"]["surviving_marked_residues"] == [73, 97, 235]

# Exact repo-side source locks.
locks = art["source_locks"]
assert git_blob_sha(REL) == locks["relative_H_marking"]["blob_sha1"]
assert git_blob_sha(LOC) == locks["exact_C1_ordering"]["blob_sha1"]
assert git_blob_sha(V6) == locks["v6_witness"]["blob_sha1"]
assert git_blob_sha(TANG) == locks["physical_C1_node_incidence"]["blob_sha1"]
assert git_blob_sha(BLOW) == locks["resolved_double_cover_blowdown_adapter"]["blob_sha1"]
assert git_blob_sha(QTRACE) == locks["q602_trace_spectrum"]["blob_sha1"]
assert git_blob_sha(PRYM) == locks["upstairs_prym_norm_crosscheck"]["blob_sha1"]
assert rel["canonical_sha256_without_this_field"] == locks["relative_H_marking"]["canonical_sha256"]
assert v6["canonical_sha256_without_this_field"] == locks["v6_witness"]["canonical_sha256"]
assert v6["witness"]["all140_pairings_sha256"] == locks["v6_witness"]["all140_pairings_sha256"]
assert tang["canonical_sha256"] == locks["physical_C1_node_incidence"]["canonical_sha256"]
assert blow["canonical_sha256_without_this_field"] == locks["resolved_double_cover_blowdown_adapter"]["canonical_sha256"]
assert common["canonical_sha256_without_this_field"] == locks["common_cover_identity"]["canonical_sha256"]
assert qtrace["canonical_sha256_without_this_field"] == locks["q602_trace_spectrum"]["canonical_sha256"]

# Source-note lock for the external modular graph model. The verifier replays
# all algebra after these explicit source facts; it does not silently infer them.
for marker in [
    "arXiv:1009.0388",
    "u^2=2xy",
    "v^2=x^2-y^2",
    "w^2=x^2+y^2",
    "U=2*b1",
    "V=2*b2",
    "W=2*b3",
    "X=a1+c",
    "Y=-a1+c",
    "T=a2+i*a3",
    "Zc=a2-i*a3",
]:
    assert marker in note

# Retained H marking and exact sign action.
assert rel["modular_to_stoll"]["u=TTprime"] == "g7*g9"
assert rel["modular_to_stoll"]["v=RT"] == "g7*g8"
assert rel["modular_to_stoll"]["uv=RTprime"] == "g8*g9"
H = {
    "1": (1, 1, 1),
    "u_H": (-1, 1, -1),
    "v_H": (-1, -1, 1),
    "u_H*v_H": (1, -1, -1),
}
assert list(H) == art["graph_quotient_identification"]["H_elements_order"]
assert [list(H[h]) for h in H] == art["graph_quotient_identification"]["H_sign_patterns_order_u_v_w"]
assert all(eu * ev * ew == 1 for eu, ev, ew in H.values())

# Exact C1 group-3 transcription must remain present in the retained Stage33
# source. Its global indices are 17..24, with nested e1,e2,e3 order [+1,-1].
loc_text = LOC.read_text()
for marker in [
    'add_known("C1", 3',
    '[a3, a1 + e1*b2, a2 + e2*b1, b3 + e3*c]',
]:
    assert marker in loc_text
signs: list[tuple[int, int, int]] = []
for e1 in (1, -1):
    for e2 in (1, -1):
        for e3 in (1, -1):
            signs.append((e1, e2, e3))
assert len(signs) == 8

actual_indices = []
actual_es = []
for h, (eps_u, eps_v, eps_w) in H.items():
    e = (-eps_v, -eps_u, -eps_w)
    actual_es.append(e)
    actual_indices.append(17 + signs.index(e))
assert actual_indices == [24, 21, 18, 19]
assert actual_indices == art["graph_quotient_identification"]["C1_indices_in_actual_H_order"]
assert sorted(actual_indices) == art["graph_quotient_identification"]["C1_index_set"]
assert actual_es == [(-1,-1,-1), (-1,1,1), (1,1,-1), (1,-1,1)]

# Reconstruct exact physical-side -> six exceptional-node incidence.
side_nodes: dict[int, set[int]] = defaultdict(set)
for ex in tang["exceptional_models"]:
    j = int(ex["exceptional_id"].split("_")[1])
    assert 1 <= j <= 48
    for rec in ex["physical_crossing_tangent_coordinates"]:
        side = int(rec["side_index_1based"])
        assert 1 <= side <= 24
        side_nodes[side].add(j)
assert sorted(side_nodes) == list(range(1, 25))
assert all(len(side_nodes[s]) == 6 for s in range(1, 25))

pair = v6["witness"]["all140_pairings"]
assert len(pair) == 140
mult = pair[92:140]
assert len(mult) == 48
assert sum(mult) == 266

c_dot_k = [pair[s - 1] for s in actual_indices]
incident_mass = [sum(mult[j - 1] for j in side_nodes[s]) for s in actual_indices]
assert c_dot_k == [0, 0, 14, 9]
assert incident_mass == [41, 41, 24, 34]
assert c_dot_k == art["exact_graph_intersections"]["C_dot_K"]
assert incident_mass == art["exact_graph_intersections"]["incident_node_mass"]

# Revalidate the load-bearing resolved-cover/blow-down formulas from the
# retained exact adapter.
adapter = blow["resolved_double_cover_adapter"]
assert adapter["resolved_quotient"] == "pi:Xtilde->Btilde finite degree 2, branched on the 48 exceptional curves"
assert adapter["upstairs_strict_transform"] == "Dtilde=pi^*C"
assert adapter["pullback_square_formula"] == "Dtilde^2=2*C^2"
assert adapter["exceptional_contact_formula"] == "Dtilde.Etilde_j=C.E_j=m_j"
assert blow["x_side_exact_lock"]["D_square"] == 3874

# For a physical C1 graph quotient K_h, Ltilde_h=pi^*K_h has multiplicity one
# at each of its six fixed-point lifts. Blow-down gives the exact +sum(m_j)
# correction; q:P->X then contributes degree 4 by projection formula.
d_dot_l = [2 * ck + m for ck, m in zip(c_dot_k, incident_mass)]
gamma_graph = [4 * x for x in d_dot_l]
assert d_dot_l == [41, 41, 52, 52]
assert gamma_graph == [164, 164, 208, 208]
assert d_dot_l == art["exact_graph_intersections"]["D_dot_L"]
assert gamma_graph == art["exact_graph_intersections"]["GammaP_dot_Graph"]

# Common-cover group square must be the exact H quotient used above.
gsq = common["group_quotient_square"]
assert gsq["P"] == "Z x Z with diagonal G action"
assert gsq["H"] == "Gamma'[4]/Gamma[8] ~= V4, order 4, normal index 2"
assert gsq["X"] == "P/H_diag (Beauville cover surface)"
assert gsq["C0"] == "Z/H"
assert common["verdict"]["common_double_cover_identity_for_actual_carrier"] is True

# Linear trace formula and H-Fourier decomposition.
A = [105 + 81 - x for x in gamma_graph]
assert A == [22, 22, -22, -22]
assert A == art["exact_graph_intersections"]["twisted_linear_traces"]
chars = art["H_character_linear_trace"]["character_table_order_1_u_v_uv"]
blocks = {}
for name, row in chars.items():
    total = sum(c * a for c, a in zip(row, A))
    assert total % 4 == 0
    blocks[name] = total // 4
assert blocks == {"trivial": 0, "chi_u": 0, "chi_v": 22, "chi_uv": 0}
assert blocks == art["H_character_linear_trace"]["block_rational_linear_traces"]
assert art["H_character_linear_trace"]["forced_downstairs_trace"] == 0

# Independent normalization check against the previously derived Prym norms.
forced = prym["elliptic_prym_consequence"]["forced_degrees_by_retained_character"]
deg = {k: v["degree"] for k, v in forced.items()}
assert deg == {"chi_u": 9, "chi_v": 137, "chi_uv": 9}
for ch in ("chi_u", "chi_v", "chi_uv"):
    tr = blocks[ch]
    assert tr % 2 == 0
    re = tr // 2
    im2 = deg[ch] - re * re
    assert im2 >= 0 and math.isqrt(im2) ** 2 == im2
assert art["H_character_linear_trace"]["prym_norm_crosscheck"]["linear_traces_0_22_0_are_norm_compatible"] is True

# Q602 shell contradiction. The post1518 spectrum is explicitly trace-gauge
# invariant on the audited {73,97,235} orbit and excludes zero.
assert qtrace["fixed_target"]["Q"] == 602
assert qtrace["audited_input"]["canonical_residue_decimal"] == 73
assert qtrace["rational_trace"]["gauge_invariant_by_conjugation"] is True
assert qtrace["rational_trace"]["trace_mod8"] == 4
allowed = qtrace["exact_spectrum"]["trace_values"]
assert allowed == [-68,-60,-52,-44,-36,-28,-20,-12,-4,4,12,20,28,36,44,52,60,68]
assert 0 not in allowed
assert blocks["trivial"] == 0
assert art["q602_contradiction"]["contradiction"] is True

# Credit / terminal-candidate firewall.
assert art["population_scope"]["finite_monodromy_sample_used"] is False
assert art["population_scope"]["all_O210_cover_configurations_under_fixed_target_disposed_if_source_chain_is_accepted"] is True
assert art["diagnostic_verdict"]["provisional_O210_cover_geometry_excluded"] is True
assert art["diagnostic_verdict"]["terminal_candidate"] == "O210_COVER_GEOMETRY_EXCLUDED"
assert art["diagnostic_verdict"]["audit_ready_full_target_closure"] is False
for key in [
    "hostile_audit_credit",
    "stage32_main_credit",
    "claim_dag_sync_triggered_by_this_scratch",
    "retained_consolidation_performed",
    "merge_authorized",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
]:
    assert art["firewalls"][key] is False

print(json.dumps({
    "success": True,
    "actual_graph_C1_indices_order_1_u_v_uv": actual_indices,
    "C_dot_K": c_dot_k,
    "incident_mass": incident_mass,
    "GammaP_dot_Graph": gamma_graph,
    "twisted_linear_traces": A,
    "H_character_linear_traces": blocks,
    "Q602_zero_allowed": False,
    "provisional_terminal_candidate": "O210_COVER_GEOMETRY_EXCLUDED",
    "audit_ready_full_target_closure": False,
    "stage32_main_credit": False,
}, indent=2, sort_keys=True))
