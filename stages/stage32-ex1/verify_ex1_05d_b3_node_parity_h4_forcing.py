#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE / "ex1-05d-b3-node-parity-h4-forcing.json"
UP05B = HERE / "ex1-05b-inertia-parity-stabilizer.json"
UP05C = HERE / "ex1-05c-inertia-class-capacity.json"

d = json.loads(ART.read_text())
expected = d.pop("canonical_sha256_without_this_field")
canon = json.dumps(d, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
assert hashlib.sha256(canon.encode()).hexdigest() == expected

u05b = json.loads(UP05B.read_text())
u05c = json.loads(UP05C.read_text())
assert d["v6_pairing_adapter"]["source_candidate_canonical_sha256"] == u05b["canonical_sha256_without_this_field"]
P = d["v6_pairing_adapter"]["all_48_exceptional_pairings"]
assert P == u05b["target"]["exceptional_pairings"]
assert len(P) == 48

I = d["inertia_index_adapter"]
I1 = I["b1_zero_u_sign"]
I2 = I["b2_zero_v_sign"]
I3 = I["b3_zero_w_sign"]
assert [len(I1), len(I2), len(I3)] == [16, 16, 16]
assert not (set(I1) & set(I2) or set(I1) & set(I3) or set(I2) & set(I3))
assert set(I1 + I2 + I3) == set(range(1, 49))
assert I["classes_pairwise_disjoint"] and I["classes_partition_1_through_48"]
assert I["b3_coordinate_test_equals_union_of_source_C2_b3_rows"]

vals = lambda inds: [P[k-1] for k in inds]
A = d["v6_pairing_adapter"]
assert vals(I1) == A["b1_values"]
assert vals(I2) == A["b2_values"]
assert vals(I3) == A["b3_values"]
assert [sum(A["b1_values"]), sum(A["b2_values"]), sum(A["b3_values"])] == [96, 108, 62]
assert A["class_mass_replay"] == {"b1_zero": 96, "b2_zero": 108, "b3_zero": 62}
assert u05c["divisor_mass_adapter"]["inertia_contact_masses"] == {
    "u_sign_b1_zero": 96,
    "v_sign_b2_zero": 108,
    "w_sign_b3_zero": 62,
}

D = d["b3_parity_decision"]
odd = [k for k in I3 if P[k-1] % 2]
assert odd == [1, 2, 3, 7, 41, 42, 47, 48]
assert odd == D["odd_b3_indices_1based"]
assert [P[k-1] for k in odd] == D["odd_b3_values"]
assert D["odd_b3_count"] == 8
assert not D["all_b3_even"]
assert D["h2_excluded"]
assert D["h4_forced_at_component_stabilizer_layer"]

assert d["source_replay"]["workflow_conclusion"] == "success"
assert d["source_replay"]["coordinate_and_C2_incidence_agree"]
assert d["exit"]["credit_ceiling"] == "BRANCH_EXCLUSION_CANDIDATE_UNAUDITED"
assert not d["exit"]["all_residual_configurations_disposed"]
assert not d["exit"]["full_target_closure"]
assert not d["firewalls"]["Magma_point_order_guessed"]
assert not d["firewalls"]["scratch_result_itself_authority"]
assert not d["firewalls"]["h4_forcing_promoted_to_full_v6_exclusion"]
print("EX1-05D replay PASS: b3 odd witness excludes h=2; h=4 forced at component-stabilizer layer")
