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
subs = T["subgroups"]
assert len(subs) == 6
assert len({x["M"] for x in subs}) == 6
expected = {
    "<u,v>={0,u,v,uv}": ({"u", "v"}, 204, True),
    "<u,w>={0,u,w,uw}": ({"u", "w"}, 158, False),
    "<v,w>={0,v,w,vw}": ({"v", "w"}, 170, False),
    "<uv,w>={0,uv,w,uvw}": ({"w"}, 62, False),
    "<uw,v>={0,uw,v,uvw}": ({"v"}, 108, False),
    "<vw,u>={0,vw,u,uvw}": ({"u"}, 96, False),
}
for x in subs:
    signs, mass, ok = expected[x["M"]]
    assert set(x["allowed_single_signs"]) == signs
    assert x["allowed_mass"] == mass
    assert x["compatible_with_Q_ge_188"] is ok
assert T["excluded_h2_subgroup_choices_by_capacity"] == 5
assert T["remaining_h2_subgroup_choices_after_capacity"] == 1
assert T["surviving_allowed_mass"] == 204
assert T["surviving_Q_even_range"] == [188, 204]
assert T["unique_surviving_h2_stabilizer"].startswith("M=<u,v>")

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
assert not d["firewalls"]["h2_subgroup_exhaustion_assumes_exactly_two_single_signs"]
print("EX1-05C replay PASS: all six h=2 stabilizers exhausted; five fail capacity, only <u,v> reaches 188")
