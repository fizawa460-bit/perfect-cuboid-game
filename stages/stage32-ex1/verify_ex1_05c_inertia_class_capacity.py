#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE / "ex1-05c-inertia-class-capacity.json"

d = json.loads(ART.read_text())
expected = d.pop("canonical_sha256_without_this_field")
canon = json.dumps(d, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
assert hashlib.sha256(canon.encode()).hexdigest() == expected

A = d["divisor_mass_adapter"]
assert [sum(A["C2_pairings"][k]) for k in ("b1_zero", "b2_zero", "b3_zero")] == [90, 78, 124]
assert [186 - A["C2_pairing_sums"][k] for k in ("b1_zero", "b2_zero", "b3_zero")] == [96, 108, 62]
assert sum(A["inertia_contact_masses"].values()) == 266

T = d["h2_capacity_test"]
assert T["forbid_u"]["allowed_mass"] == 108 + 62 == 170
assert T["forbid_v"]["allowed_mass"] == 96 + 62 == 158
assert T["forbid_w"]["allowed_mass"] == 96 + 108 == 204
assert not T["forbid_u"]["compatible_with_Q_ge_188"]
assert not T["forbid_v"]["compatible_with_Q_ge_188"]
assert T["forbid_w"]["compatible_with_Q_ge_188"]
assert T["excluded_h2_subgroup_choices"] == 2
assert T["remaining_h2_subgroup_choices"] == 1

P = d["h2_parity_gate"]
assert P["forbidden_class_total_mass"] == 62
assert P["forbidden_class_half_excess_if_viable"] == 31
assert P["Q_even_range_if_h2"] == [188, 204]
for t in range(9):
    Q = 188 + 2*t
    assert (204-Q)//2 == 8-t
    assert Q-(8-t) == 180+3*t

assert d["exit"]["credit_ceiling"] == "BRANCH_EXCLUSION_CANDIDATE_UNAUDITED"
assert not d["exit"]["full_target_closure"]
assert not d["firewalls"]["aggregate_mass_used_to_guess_individual_parity"]
assert not d["firewalls"]["Magma_point_order_guessed"]
print("EX1-05C replay PASS")
