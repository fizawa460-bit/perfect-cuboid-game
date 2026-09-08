#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "stages" / "stage32-ex6" / "post1697-fsm16-modular-tensor-multibranch-contract.json"


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main() -> None:
    x = json.loads(PATH.read_text())
    assert x["schema"] == "STAGE32_EX6_FSM16_MODULAR_TENSOR_MULTIBRANCH_WALL_V2"
    assert x["status"] == "EXPLORATORY_EXACT_BOUNDED_WALL_ADAPTER_CORRECTED_NO_ENDPOINT_CREDIT"

    locks = x["stage32_source_locks"]
    an = ROOT / locks["AN_path"]
    ar = ROOT / locks["AR_path"]
    assert an.exists() and ar.exists()
    assert git_blob_sha1(an) == locks["AN_blob_sha1"]
    assert git_blob_sha1(ar) == locks["AR_blob_sha1"]

    an_text = an.read_text()
    ar_text = ar.read_text()
    assert "A=a1/4" in an_text and "B=a2/4" in an_text
    assert "m=min(A,B)" in an_text
    assert "a1=4*A" in ar_text and "a2=4*B" in ar_text
    assert "#minimal >= (266-t)-(80-t)=186" in ar_text

    s = x["source_proof_constants"]
    assert s["tensor_degree_factor"] == 16
    assert s["zero_lower_bound_per_degree_per_k"] == 2
    assert s["max_pole_order_per_minimal_cusp_branch_per_k"] == 8
    assert s["published_node_cap_under_bijective_normalization"] == 48

    v = x["v6_endpoint_inputs"]
    assert v["geometric_genus"] == 1
    assert v["degree"] == 186
    assert v["positive_node_support"] == 47
    assert v["normalization_points_over_exceptional_divisor"] == 266
    assert v["endpoint_t"] == 0
    assert v["actual_endpoint_normalization_bijective"] is False

    p = x["published_theorem_check"]
    assert p["genus_one_degree_upper_bound"] == 176 + 16 * v["geometric_genus"] == 192
    assert p["degree_slack"] == p["genus_one_degree_upper_bound"] - v["degree"] == 6
    assert p["excludes_v6"] is False

    c = x["counterfactual_47_node_bijective_check"]
    assert c["pole_budget_per_k"] == 8 * v["positive_node_support"] == 376
    assert c["genus_one_degree_upper_bound"] == 4 * v["positive_node_support"] == 188
    assert c["degree_slack"] == 2
    assert c["applicable_to_actual_O266_population"] is False
    assert c["excludes_v6"] is False

    b = x["branchwise_extension"]
    assert b["derived_bound"] == "d <= 16g - 16 + 4B"
    assert b["B"] == 266
    assert b["genus_one_degree_upper_bound"] == 1064
    assert b["degree_slack"] == 878
    assert b["excludes_v6"] is False

    a = x["stage32_fsm16_adapter"]
    assert a["adapter_source_locked"] is True
    assert a["a1_equals_4A"] is True and a["a2_equals_4B"] is True
    assert a["A_B_positive"] is True and a["A_plus_B_even"] is True
    assert a["exceptional_multiplicity"] == "min(A,B)"
    assert a["fsm16_minimal_cusp_pair"] == [4, 4]
    assert a["stage32_minimal_pair"] == [1, 1]
    assert a["minimal_pairs_equivalent"] is True

    o = x["O266_two_factor_minimal_branch_bound"]
    assert o["q81_node_upper_bound"] == 52
    assert o["q105_node_upper_bound"] == 28
    assert o["nonminimal_branch_upper_bound"] == 80
    assert o["minimal_branch_lower_bound"] == 266 - 80 == 186
    assert o["S_cusp_lower_bound"] == 186

    d = x["discrete_cusp_pole_budget"]
    assert d["required_total_pole_units_for_degree_186_genus_one"] == 2 * v["degree"] == 372
    assert d["positive_pole_units_per_minimal_branch"] == 8
    required = (372 + 7) // 8
    assert d["tensor_minimum_S_cusp_for_compatibility"] == required == 47
    assert d["tensor_exclusion_threshold_S_cusp_max"] == 46
    assert d["AR_exclusion_threshold_new_upper_bound_S_cusp_max"] == 185
    assert d["AR_lower_bound_margin_over_tensor_requirement"] == 186 - 47 == 139

    dom = x["dominance"]
    assert dom["upper_bound_on_S_cusp_strategy"] == "FSM16_CARDINALITY_ROUTE_STRICTLY_DOMINATED_BY_AR"
    assert dom["adapter_gap_closed"] is True
    assert dom["old_adapter_missing_statement_retracted"] is True

    decision = x["decision"]
    assert decision["fsm16_modular_tensor_O266"] == "NUMERICALLY_NONEXCLUDING"
    assert decision["fsm16_S_cusp_cardinality_route"] == "DOMINATED_BY_AR_MINIMAL_BRANCH_BOUND"
    assert decision["O266_endpoint_excluded"] is False
    assert decision["O264_descent_authorized"] is False

    f = x["firewalls"]
    assert all(f[k] is False for k in (
        "new_published_theorem_claimed",
        "branchwise_extension_claimed_as_published",
        "tensor_exact_pole_order_claimed_from_cardinality_alone",
        "global_v6_carrier_constructed",
        "endpoint_closure_credit",
        "perfect_cuboid_credit",
    ))

    print("PASS: Stage32 EX6 FSM16 modular tensor corrected V2 contract")


if __name__ == "__main__":
    main()
