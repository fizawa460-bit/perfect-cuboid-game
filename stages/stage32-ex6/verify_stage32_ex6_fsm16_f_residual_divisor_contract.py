#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "stages" / "stage32-ex6" / "post1697-fsm16-f-residual-divisor-contract.json"
PARENT = ROOT / "stages" / "stage32-ex6" / "post1697-fsm16-weighted-node-divisor-contract.json"
AR = ROOT / "stages" / "stage32" / "residual-32-01-production" / "post1648ar-two-factor-slack-minimal-branches-source-note.md"


def main() -> None:
    x = json.loads(PATH.read_text())
    p = json.loads(PARENT.read_text())

    assert x["schema"] == "STAGE32_EX6_FSM16_F_RESIDUAL_DIVISOR_WALL_V1"
    assert x["status"] == "EXPLORATORY_EXACT_REENTRY_THRESHOLD_NO_ENDPOINT_CREDIT"
    assert PARENT.exists() and AR.exists()
    assert p["schema"] == "STAGE32_EX6_FSM16_WEIGHTED_NODE_DIVISOR_WALL_V1"

    c = x["carrier_inputs"]
    assert c["degree_d"] == 186
    assert c["genus"] == 1
    assert c["O"] == 266
    assert c["E_definition"] == "eta81+rho81+eta105+rho105"
    assert c["E_nonnegative"] is True

    f = x["fsm16_f_divisor"]
    assert f["f_zero_divisor_class"] == "2k*K_Btilde"
    assert f["f_not_identically_zero_on_curve"] is True
    assert f["f_nonzero_at_all_48_nodes"] is True
    assert f["curve_degree_equals_K_intersection"] is True
    assert f["pullback_f_zero_degree_formula"] == "2kd"
    assert 2 * c["degree_d"] == 372
    assert f["pullback_f_zero_degree_per_k"] == 372
    assert f["all_f_divisor_contribution_is_nonnode"] is True
    assert f["published_tensor_zero_statement"] == "at_least_2kd"

    pb = x["parent_nonnode_budget"]
    ps = p["slack_refinement"]
    assert pb["required_nonnode_signed_divisor_formula"] == ps["required_nonnode_signed_divisor_formula"]
    assert pb["minimum_required_nonnode_signed_divisor_per_k"] == ps["minimum_required_nonnode_signed_divisor_per_k"] == 1488

    r = x["residual_nonnode_budget"]
    assert r["definition"] == "D_res_nonnode := D_nonnode - deg(div(f)|_N)"
    assert 1488 - 372 == 1116
    assert r["formula"] == "(1116+8E)k"
    assert r["minimum_per_k"] == 1116
    assert r["uniform_closing_upper_bound"] == "D_res_nonnode <= 1115k"
    assert r["sharp_closing_upper_bound"] == "D_res_nonnode < (1116+8E)k"

    i = x["independence"]
    assert i["f_divisor_degree_derived_from_stage32_factor_RH_ledger"] is False
    assert i["q_eta_rho_reuse_as_independent_cap_allowed"] is False
    assert i["independent_residual_upper_bound_source_locked"] is False

    d = x["decision"]
    assert d["fsm16_f_divisor_contribution_per_k"] == 372
    assert d["fsm16_residual_nonnode_minimum_per_k"] == 1116
    assert d["fsm16_f_zeros_alone_close_endpoint"] is False
    assert d["O266_endpoint_excluded"] is False
    assert d["O264_descent_authorized"] is False

    fw = x["firewalls"]
    assert all(fw[key] is False for key in (
        "residual_divisor_effective_claimed",
        "formal_T_over_f_descends_as_global_surface_tensor_claimed",
        "residual_nonnode_upper_bound_claimed",
        "global_v6_carrier_constructed",
        "endpoint_closure_credit",
        "perfect_cuboid_credit",
        "hostile_audit_credit",
        "merge_implied",
    ))

    print("PASS: Stage32 EX6 FSM16 f-divisor residual wall contract")


if __name__ == "__main__":
    main()
