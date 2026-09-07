#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE / "ex1-05e-h4-modular-factor-projection-reduction.json"
UP05B = HERE / "ex1-05b-inertia-parity-stabilizer.json"
UP05D = HERE / "ex1-05d-b3-node-parity-h4-forcing.json"
ROOT = HERE.parent.parent
BIDEG = ROOT / "stage32/residual-32-01-production/post1484-v6-modular-factor-bidegree-source-note.md"
MONO = ROOT / "stage32/residual-32-01-production/post1473-specific-class-multibranch-product-cover-monodromy-extremal-wall.md"


def git_blob_sha1(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def load_canonical(path: Path):
    d = json.loads(path.read_text())
    expected = d.pop("canonical_sha256_without_this_field")
    canon = json.dumps(d, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    assert hashlib.sha256(canon.encode()).hexdigest() == expected
    return d, expected


d, expected = load_canonical(ART)
u05b = json.loads(UP05B.read_text())
u05d = json.loads(UP05D.read_text())
assert d["source_locks"]["ex1_05b"]["canonical_sha256"] == u05b["canonical_sha256_without_this_field"]
assert d["source_locks"]["ex1_05d"]["canonical_sha256"] == u05d["canonical_sha256_without_this_field"]
assert u05d["b3_parity_decision"]["h4_forced_at_component_stabilizer_layer"]

assert git_blob_sha1(BIDEG) == d["source_locks"]["v6_modular_factor_bidegree_source_note"]["blob_sha1"]
assert git_blob_sha1(MONO) == d["source_locks"]["product_cover_monodromy_notation_source"]["blob_sha1"]
btxt = BIDEG.read_text()
mtxt = MONO.read_text()
for anchor in ["`m_z=105`, `m_w=81`", "`q'=4`: `(n_z,n_w)=(105,81)`", "`O>=210`"]:
    assert anchor in btxt
for anchor in ["`Y -> N`", "degree `q' in {1,2,4}` over `Y`", "projection degrees `D -> X(8)` as `n1,n2`"]:
    assert anchor in mtxt

A = d["notation_adapter"]
assert A["h4_forced_input"]
assert "h=deg(Ctilde->D)=qprime" in A["component_degree_identity"]
assert "Q=deg Ram(D->N)=retained O" in A["ramification_identity"]

F = d["fixed_v6_projection_replay"]
assert F["modular_factor_degrees_N_to_X4"] == [105, 81]
assert F["h_equals_qprime"] == 4
assert F["full_component_degrees_Ctilde_to_X8"] == [105, 81]
assert sum(F["full_component_degrees_Ctilde_to_X8"]) == 186 == F["degree_sum"]
assert u05b["component_stabilizer_refinement"]["h4_case"]["degree_sum"] == "alpha+beta=186"
assert F["X8_to_C2_degree"] == F["Ctilde_to_D_degree"] == 4
assert F["both_vertical_maps_etale"]
assert F["descended_projection_degrees_D_to_C2"] == [105, 81]

H = d["h4_projection_ramification"]
assert H["C2_genus"] == 2
assert H["nonnegative_ramification_forces_Q_ge"] == 210
assert H["prior_Q_even_range"] == u05b["global_parity_consequences"]["Q_range_even"] == [186, 266]
Qvals = list(range(210, 267, 2))
assert H["refined_Q_even_range"] == [210, 266]
assert H["refined_Q_state_count"] == len(Qvals) == 29
assert H["old_s_refined_range"] == [12, 40]
assert H["r_range"] == [0, 28]

P = u05b["target"]["exceptional_pairings"]
assert len(P) == 48 and sum(P) == 266
odd = [m for m in P if m % 2]
odd_mass = sum(m for m in P if m % 2)
even_pos = sorted([m for m in P if m > 0 and m % 2 == 0], reverse=True)
extra_caps = sorted([m - (m % 2) for m in P], reverse=True)
C = d["contact_parity_refinement"]
assert len(odd) == C["odd_pairing_node_count"] == 26
assert odd_mass == C["odd_pairing_mass"] == 140
assert len(even_pos) == C["even_positive_pairing_node_count"] == 21
assert sum(even_pos) == C["even_positive_pairing_mass"] == 126
assert even_pos == C["even_positive_pairing_values_desc"]
assert extra_caps == C["extra_capacity_values_desc"]

cum_even = []
s = 0
for x in even_pos:
    s += x
    cum_even.append(s)
cum_extra = []
s = 0
for x in extra_caps:
    s += x
    cum_extra.append(s)

even_lb = []
ramified_lb = []
multibranch_lb = []
for r, Q in enumerate(Qvals):
    R105 = Q - 210
    R81 = Q - 162
    assert R105 == 2*r and R81 == 48 + 2*r
    assert R105 >= 0 and R81 >= 0
    assert R105 + R81 == 2*Q - 372
    k_even = next(i + 1 for i, v in enumerate(cum_even) if v >= Q - odd_mass)
    k_multi = next(i + 1 for i, v in enumerate(cum_extra) if v >= Q - len(odd))
    even_lb.append(k_even)
    ramified_lb.append(len(odd) + k_even)
    multibranch_lb.append(k_multi)
    assert (266 - Q)//2 == 28 - r
    assert Q - (28-r) == 182 + 3*r

L = d["residual_Q_state_ledger"]
assert L["r_values"] == list(range(29))
assert L["even_ramified_node_count_lower_bound_by_r"] == even_lb
assert L["ramified_surface_node_count_lower_bound_by_r"] == ramified_lb
assert L["multibranch_node_count_lower_bound_by_r"] == multibranch_lb
assert min(even_lb) == C["global_even_ramified_node_count_lower_bound_over_refined_range"] == 7
assert min(ramified_lb) == C["global_ramified_surface_node_count_lower_bound_over_refined_range"] == 33
assert min(multibranch_lb) == C["global_multibranch_node_count_lower_bound_over_refined_range"] == 19

D = d["decision"]
assert D["h4_Q_slack_states_before_modular_factor_replay"] == 41
assert D["h4_Q_slack_states_after_modular_factor_replay"] == 29
assert D["states_removed_by_Q_ge_210"] == 12
assert D["Q_below_210_excluded_within_h4"]
assert not D["all_h4_residual_configurations_disposed"]
assert d["exit"]["Q_slack_residual_ledger_complete"]
assert not d["exit"]["finite_residual_configuration_ledger_complete"]
assert not d["exit"]["all_residual_configurations_disposed"]
assert not d["exit"]["full_target_closure"]
assert not d["firewalls"]["stage32_unaudited_candidate_inherited_as_theorem"]
assert not d["firewalls"]["Q210_extremal_histogram_imported_without_local_adapter"]
assert not d["firewalls"]["finite_29_Q_state_ledger_promoted_to_realizability"]
assert not d["firewalls"]["h4_refinement_promoted_to_full_v6_exclusion"]
print("EX1-05E replay PASS: h=4 fixed V6 degrees 105/81 force Q>=210; 29 Q-states remain; ramified nodes>=33; multibranch nodes>=19")
