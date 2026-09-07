#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
P = HERE / "ex1-04-global-coupling-ledger.json"

obj = json.loads(P.read_text())
claimed = obj.pop("canonical_sha256_without_this_field")
raw = json.dumps(obj, ensure_ascii=False, indent=2).encode()
actual = hashlib.sha256(raw).hexdigest()
assert actual == claimed, (actual, claimed)

f = obj["fixed_global_equalities"]
assert f["D_square"] == 758
assert f["K_dot_D"] == 186
assert f["arithmetic_genus"] == 473
assert f["normalization_genus"] == 1
assert f["total_delta"] == 472
assert f["delta_partition"] == "delta_E + delta_U = 472"
assert f["exceptional_contact_mass"] == 266
assert f["positive_exceptional_support"] == 47
assert f["node_fiber_excess_upper_bound"] == 219

n = obj["normalization_nonbijectivity_coupling"]
assert n["exhaustive_disjunction"] == "NODE_MULTIBRANCH or SMOOTH_LOCUS_MULTIBRANCH"
assert n["if_delta_U_zero"] == "node multibranch is required at one of the 38 nonunit-contact nodes"
assert n["if_no_node_multibranch"] == "smooth-locus multibranch is required, hence delta_U>=1"
assert n["node_multibranch_does_not_imply"] == "delta_E>0"

s = obj["surface_node_interface"]
assert s["nonunit_candidate_nodes"] == 38
assert s["labeled_local_contact_envelopes"] == 1188
assert s["unit_contact_nodes"] == 9
assert s["unit_contact_nodes_delta_E"] == 0
assert s["contact_mass_bounds_delta_E"] is False
assert s["node_fiber_excess_is_delta"] is False

u = obj["smooth_locus_interface"]
assert u["delta_U_range"] == [0, 472]
assert u["singular_point_count_upper_bound"] == 472
assert u["total_branch_excess_upper_bound"] == 472
assert u["canonical_six_point_multiplicity_budget"] == 186
assert u["multiplicity_budget_converted_to_delta_bound"] is False

k = obj["known140_interface"]
assert k["effective_decomposition_exists"] is True
assert k["member_level_singularity_constraint_obtained"] is False

g = obj["global_budget_result"]
assert g["contradiction_obtained"] is False
assert g["positive_member_obtained"] is False
assert g["global_coupling_ledger_complete"] is True
assert g["global_delta_contact_intersection_budget_closed_for_terminal_exclusion"] is False

ar = obj["arsenal_check"]
assert ar["policy_followed"] is True
assert ar["directly_applicable_formal_card_found"] is False

ex = obj["exit"]
assert ex["global_coupling_ledger_complete"] is True
assert ex["global_budget_contradiction"] is False
assert ex["global_delta_contact_intersection_budget_closed"] is False
assert ex["branch_exclusion_credit"] is False
assert ex["full_target_closure"] is False

fw = obj["firewalls"]
assert not any([
    fw["exceptional_mass_identified_with_delta"],
    fw["node_fiber_excess_identified_with_delta"],
    fw["known140_decomposition_promoted_to_member_singularity_data"],
    fw["arsenal_nonmatch_treated_as_repository_absence"],
    fw["numerical_residual_ledger_promoted_to_realizability"],
    fw["stage32_main_credit"],
    fw["receiver_credit"],
    fw["theorem_credit"],
    fw["endpoint_credit"],
    fw["perfect_cuboid_existence_claim"],
    fw["perfect_cuboid_nonexistence_claim"],
])
print("EX1-04 global coupling ledger: PASS", claimed)
