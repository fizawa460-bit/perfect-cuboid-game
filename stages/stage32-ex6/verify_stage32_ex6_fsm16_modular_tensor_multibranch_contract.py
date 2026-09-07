#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "stages" / "stage32-ex6" / "post1697-fsm16-modular-tensor-multibranch-contract.json"


def main() -> None:
    x = json.loads(PATH.read_text())
    assert x["schema"] == "STAGE32_EX6_FSM16_MODULAR_TENSOR_MULTIBRANCH_WALL_V1"
    assert x["status"] == "EXPLORATORY_EXACT_BOUNDED_WALL_NO_ENDPOINT_CREDIT"

    s = x["source_proof_constants"]
    assert s["tensor_degree_factor"] == 16
    assert s["zero_lower_bound_per_degree_per_k"] == 2
    assert s["max_pole_order_per_normalization_branch_per_k"] == 8
    assert s["published_node_cap_under_bijective_normalization"] == 48

    v = x["v6_endpoint_inputs"]
    assert v["geometric_genus"] == 1
    assert v["degree"] == 186
    assert v["positive_node_support"] == 47
    assert v["normalization_points_over_exceptional_divisor"] == 266
    assert v["actual_endpoint_normalization_bijective"] is False

    p = x["published_theorem_check"]
    assert p["genus_one_degree_upper_bound"] == 176 + 16 * v["geometric_genus"] == 192
    assert p["degree_slack"] == p["genus_one_degree_upper_bound"] - v["degree"] == 6
    assert p["excludes_v6"] is False

    c = x["counterfactual_47_node_bijective_check"]
    assert c["pole_budget_per_k"] == s["max_pole_order_per_normalization_branch_per_k"] * v["positive_node_support"] == 376
    assert c["genus_one_degree_upper_bound"] == 4 * v["positive_node_support"] == 188
    assert c["degree_slack"] == c["genus_one_degree_upper_bound"] - v["degree"] == 2
    assert c["applicable_to_actual_O266_population"] is False
    assert c["excludes_v6"] is False

    b = x["branchwise_extension"]
    assert b["derived_bound"] == "d <= 16g - 16 + 4B"
    assert b["B"] == v["normalization_points_over_exceptional_divisor"] == 266
    assert b["genus_one_degree_upper_bound"] == 4 * b["B"] == 1064
    assert b["degree_slack"] == b["genus_one_degree_upper_bound"] - v["degree"] == 878
    assert b["excludes_v6"] is False

    d = x["discrete_cusp_pole_budget"]
    assert d["minimal_modular_cusp_pair"] == [4, 4]
    assert d["minimal_sum"] == 8
    assert d["next_allowed_sum_at_least"] == 16
    assert d["positive_pole_units_per_minimal_branch"] == 8
    assert d["required_total_pole_units_for_degree_186_genus_one"] == 2 * v["degree"] == 372
    required = (d["required_total_pole_units_for_degree_186_genus_one"] + 7) // 8
    assert d["minimum_minimal_cusp_branches_for_compatibility"] == required == 47
    assert d["exclusion_threshold_maximal_minimal_cusp_branches"] == required - 1 == 46
    assert d["adapter_to_stage32_AN_FSM_locked"] is False

    decision = x["decision"]
    assert decision["fsm16_modular_tensor_O266"] == "NUMERICALLY_NONEXCLUDING"
    assert decision["O266_endpoint_excluded"] is False
    assert decision["O264_descent_authorized"] is False

    f = x["firewalls"]
    assert all(f[k] is False for k in (
        "new_published_theorem_claimed",
        "branchwise_extension_claimed_as_published",
        "AN_FSM_identified_with_FSM16_cusp_parameters",
        "global_v6_carrier_constructed",
        "endpoint_closure_credit",
        "perfect_cuboid_credit",
    ))

    print("PASS: Stage32 EX6 FSM16 modular tensor multibranch wall contract")


if __name__ == "__main__":
    main()
