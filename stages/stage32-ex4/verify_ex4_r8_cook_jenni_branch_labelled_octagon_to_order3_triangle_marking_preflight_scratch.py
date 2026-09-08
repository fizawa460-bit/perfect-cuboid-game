#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART_PATH = ROOT / "stages/stage32-ex4/ex4-r8-cook-jenni-branch-labelled-octagon-to-order3-triangle-marking-preflight-scratch.json"
R7_PATH = ROOT / "stages/stage32-ex4/ex4-r7-triangle-group-regular-octagon-marking-preflight-scratch.json"

art = json.loads(ART_PATH.read_text())
r7 = json.loads(R7_PATH.read_text())

raw = dict(art)
expected = raw.pop("canonical_sha256_without_this_field")
canon = json.dumps(raw, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
assert hashlib.sha256(canon).hexdigest() == expected == "b6a57fe08df323f5ade287a00e6746a0e44a3407a1ac84f1ec6e9f8aa7ded6ab"

assert art["source_locks"]["r7"]["canonical_sha256"] == r7["canonical_sha256_without_this_field"]
assert art["prior_r7"]["residual_phase_count"] == 4
assert art["typed_adapter_test"]["algebraic_branch_labels_to_cook_double_cover_octagon"]["provided"] is True
assert art["typed_adapter_test"]["cook_double_cover_octagon_to_PQ_weierstrass_strata"]["provided"] is True
assert art["typed_adapter_test"]["cook_order3_action_on_PQ_labels"]["provided"] is True
assert art["typed_adapter_test"]["absolute_P1_P2_to_zero_infinity_ordered_assignment"]["provided"] is False
assert art["typed_adapter_test"]["absolute_Q1_algebraic_label"]["provided"] is False
assert art["typed_adapter_test"]["cook_R_to_kuusalo_f1_literal_binding"]["provided"] is False
assert art["typed_adapter_test"]["cook_U_to_kuusalo_f2_literal_binding"]["provided"] is False

pq = art["source_exact_data"]["figure3_PQ_tessellation"]
assert pq["Q_index_cycle_under_R"] == "Q_i -> Q_{i+1} mod 8"
assert pq["U_example_cycle"] == ["P1", "Q8", "Q1", "P1"]

phase = art["finite_phase_replay"]
assert phase["candidate_k_before_r8"] == [0,1,2,3]
assert phase["candidate_k_after_r8"] == [0,1,2,3]
assert phase["residual_phase_count"] == 4
assert phase["cook_independently_selects_one_k"] is False
assert phase["literal_B8_k0_source_selected"] is False
assert phase["r4_candidate_cycles_through_infinity"] == {
    "k0": ["infinity","+i","-1","infinity"],
    "k1": ["infinity","-1","-i","infinity"],
    "k2": ["infinity","-i","+1","infinity"],
    "k3": ["infinity","+1","+i","infinity"],
}

assert art["decision"]["source_lane_classification"] == "STRUCTURAL_PQ_ADAPTER_EXACT_ABSOLUTE_CYCLIC_PHASE_NONPRUNING"
assert art["decision"]["r4_fourfold_phase_reduced"] is False
assert art["decision"]["absolute_delta0inf_retained_W_line_identified"] is False
assert art["decision"]["absolute_Q602_residue_identified"] is False
assert art["decision"]["conditional_residue97_only"] is True
assert art["decision"]["next_exact_route"] == "EX4-R9_JENNI_ORIGINAL_PQ_ALGEBRAIC_PHASE_SOURCE_RECOVERY"

for key, value in art["firewalls"].items():
    assert value is False, key

print("Stage32EX4 R8 Cook/Jenni P-Q phase preflight: PASS")
print("Cook gives branch-labelled double-cover and P/Q order-3 structural adapter")
print("absolute Q-index algebraic cyclic phase is not source-bound in replayable data")
print("R4 four B8 conjugates survive; residue97 remains conditional")
