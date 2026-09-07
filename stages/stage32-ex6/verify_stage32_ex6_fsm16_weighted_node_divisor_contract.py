#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "stages" / "stage32-ex6" / "post1697-fsm16-weighted-node-divisor-contract.json"
AN = ROOT / "stages" / "stage32" / "residual-32-01-production" / "post1648an-a1-strict-transform-delta-feasibility-source-note.md"
AR = ROOT / "stages" / "stage32" / "residual-32-01-production" / "post1648ar-two-factor-slack-minimal-branches-source-note.md"


def main() -> None:
    x = json.loads(PATH.read_text())
    assert x["schema"] == "STAGE32_EX6_FSM16_WEIGHTED_NODE_DIVISOR_WALL_V1"
    assert x["status"] == "EXPLORATORY_EXACT_BOUNDED_WALL_NO_ENDPOINT_CREDIT"
    assert AN.exists() and AR.exists()

    ep = x["endpoint_inputs"]
    assert ep["O"] == 266
    assert ep["genus"] == 1
    assert ep["node_branch_count"] == 266
    assert ep["endpoint_t"] == 0
    assert ep["all_exceptional_multiplicities_one"] is True

    a = x["branch_adapter"]
    assert all(a[k] is True for k in (
        "a1_equals_4A",
        "a2_equals_4B",
        "A_plus_B_even",
        "m_equals_min_A_B",
        "b_equals_abs_A_minus_B_over_2",
    ))
    assert a["endpoint_other_entry_formula"] == "1+2b"
    assert a["a1_plus_a2_formula"] == "8+8b"

    loc = x["fsm16_local_divisor"]
    assert loc["signed_order_formula"] == "(a1+a2-16)k"
    assert loc["endpoint_signed_order_formula"] == "8(b-1)k"
    assert loc["b0_pole_order_per_k"] == 8
    assert loc["b1_signed_order_per_k"] == 0
    assert loc["b_ge_2_is_zero_contribution"] is True

    n = x["node_sum"]
    assert n["sum_b_equals"] == "q81_node+q105_node"
    assert n["q81_node_upper_bound"] == 52
    assert n["q105_node_upper_bound"] == 28
    assert n["qsum_upper_bound"] == 80
    assert n["signed_node_divisor_formula_per_k"] == "8(q81_node+q105_node-266)"
    assert 8 * (n["qsum_upper_bound"] - ep["node_branch_count"]) == -1488
    assert n["maximum_signed_node_divisor_per_k"] == -1488
    assert n["minimum_forced_node_pole_debt_per_k"] == 1488
    assert 8 * ep["node_branch_count"] == 2128
    assert n["maximum_possible_node_pole_debt_per_k_from_nonnegative_q"] == 2128

    s = x["slack_refinement"]
    assert s["E_definition"] == "eta81+rho81+eta105+rho105"
    assert s["E_nonnegative"] is True
    assert s["qsum_formula"] == "80-E"
    assert s["signed_node_divisor_formula"] == "-(1488+8E)k"
    assert s["genus_one_total_divisor_degree"] == 0
    assert s["required_nonnode_signed_divisor_formula"] == "(1488+8E)k"
    assert s["minimum_required_nonnode_signed_divisor_per_k"] == 1488

    r = x["reentry"]
    assert r["minimum_contradiction_upper_bound"] == "D_nonnode < 1488k"
    assert r["sharp_slack_refined_upper_bound"] == "D_nonnode < (1488+8E)k"
    assert r["current_nonnode_upper_bound_source_locked"] is False
    assert r["S_cusp_cardinality_is_current_target"] is False

    d = x["decision"]
    assert d["fsm16_weighted_node_divisor"] == "EXACT_POLE_DEBT_THRESHOLD_OBTAINED"
    assert d["O266_endpoint_excluded"] is False
    assert d["O264_descent_authorized"] is False

    f = x["firewalls"]
    assert all(f[k] is False for k in (
        "fsm16_tensor_holomorphic_on_resolved_surface_claimed",
        "nonnode_upper_bound_claimed",
        "global_v6_carrier_constructed",
        "endpoint_closure_credit",
        "perfect_cuboid_credit",
    ))

    print("PASS: Stage32 EX6 FSM16 weighted node-divisor wall contract")


if __name__ == "__main__":
    main()
