#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "post1697-product-cover-rh-equivalence-contract.json"
PARENT = HERE / "post1697-fsm16-f-residual-divisor-contract.json"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def main() -> None:
    x = json.loads(CONTRACT.read_text())
    p = json.loads(PARENT.read_text())

    assert x["schema"] == "STAGE32_EX6_PRODUCT_COVER_RH_EQUIVALENCE_WALL_V1"
    assert x["status"] == "EXPLORATORY_EXACT_BOUNDED_EQUIVALENCE_WALL_NO_ENDPOINT_CREDIT"

    c = x["carrier_inputs"]
    assert (c["row_id"], c["picard_class"], c["genus_N"], c["O"]) == ("g1-d186", "V6", 1, 266)
    assert c["all_exceptional_contacts_m1"] is True

    cv = x["cover_inputs"]
    O = c["O"]
    gY = 1 + O // 2
    assert gY == 134 == cv["genus_Y"]
    assert cv["beauville_cover_degree"] == 2
    assert cv["qprime"] == 4
    assert cv["D_to_Y_unramified"] is True
    two_gD_minus_2 = cv["qprime"] * (2 * gY - 2)
    gD = 1 + two_gD_minus_2 // 2
    assert two_gD_minus_2 == 1064
    assert gD == 533 == cv["genus_D"]
    assert cv["node_lifts_on_D_per_N_contact"] == 4
    assert cv["D_to_N_local_ramification_index_at_O_contact"] == 2

    pr = x["projection_inputs"]
    assert pr["X8_genus"] == 5
    assert pr["projection_degrees"] == [105, 81]
    base_twogminus2 = 2 * pr["X8_genus"] - 2
    R105 = two_gD_minus_2 - 105 * base_twogminus2
    R81 = two_gD_minus_2 - 81 * base_twogminus2
    assert R105 == pr["R105"] == 224
    assert R81 == pr["R81"] == 416
    assert R105 + R81 == pr["combined_total_ramification"] == 640

    la = x["local_adapter"]
    assert all(la[k] is True for k in (
        "A_equals_a1_over_4",
        "B_equals_a2_over_4",
        "m_equals_min_A_B",
        "X4_cusp_coordinate_is_X8_uniformizer_squared",
        "local_D_projection_degrees_are_A_B",
    ))
    assert la["endpoint_m"] == 1
    assert la["b_equals_abs_A_minus_B_over_2"] is True
    assert la["combined_ramification_per_D_lift"] == "2b"
    assert la["combined_ramification_per_N_node_contact"] == "8b"

    # Fail-close the endpoint local arithmetic for a range of allowed odd other entries.
    for b in range(0, 21):
        A, B = 1, 1 + 2 * b
        assert min(A, B) == 1
        assert (A + B) % 2 == 0
        assert abs(A - B) // 2 == b
        assert (A - 1) + (B - 1) == 2 * b
        assert cv["node_lifts_on_D_per_N_contact"] * (2 * b) == 8 * b

    ar = x["AR_slack"]
    assert ar["E_definition"] == "eta81+rho81+eta105+rho105"
    assert ar["E_nonnegative"] is True
    assert ar["qsum_formula"] == "q81_node+q105_node=80-E"

    eq = x["equivalence"]
    assert eq["combined_node_ramification_formula"] == "640-8E"
    assert eq["combined_nonnode_ramification_formula"] == "8E"
    assert eq["E_equals_product_cover_nonnode_ramification_over_8"] is True
    assert eq["degree_only_product_cover_RH_route"] == "EQUIVALENT_TO_AR_TWO_FACTOR_RH_SLACK"
    assert eq["support_or_incidence_equivalence_claimed"] is False

    # qsum is nonnegative, hence E is in [0,80]. Check the exact degree partition throughout.
    for E in range(81):
        qsum = 80 - E
        node = 8 * qsum
        nonnode = 8 * E
        assert node == 640 - 8 * E
        assert node + nonnode == pr["combined_total_ramification"]

    fb = x["fsm16_boundary"]
    assert p["residual_nonnode_budget"]["formula"] == fb["retained_normalization_residual_formula"] == "(1116+8E)k"
    assert fb["constant_identity"] == "1116=6*186"
    assert 1116 == 6 * 186
    assert fb["constant_identity_promoted_to_tensor_descent"] is False
    assert fb["fsm16_residual_upstairs_divisor_claimed"] is False
    assert fb["global_T_over_f_claimed"] is False

    # Historical source locks must resolve to actual blobs, not merely contract strings.
    for key, lock in x["source_locks"].items():
        assert git("cat-file", "-t", lock["head"]) == "commit", key
        actual = git("rev-parse", f'{lock["head"]}:{lock["path"]}')
        assert actual == lock["blob_sha1"], (key, actual, lock["blob_sha1"])
        assert git("cat-file", "-t", actual) == "blob", key

    d = x["decision"]
    assert d["product_cover_RH_adapter"] == "SOURCE_LOCKED"
    assert d["product_cover_nonnode_ramification"] == "8E"
    assert d["degree_only_route"] == "EQUIVALENT_TO_AR_TWO_FACTOR_RH_SLACK"
    assert d["O266_endpoint_excluded"] is False
    assert d["O264_descent_authorized"] is False

    r = x["reentry"]
    assert r["requires_beyond_total_ramification_degree"] is True
    assert len(r["candidate_inputs"]) == 4

    fw = x["firewalls"]
    assert all(fw[k] is False for k in (
        "global_v6_carrier_constructed",
        "normalization_residual_effective_claimed",
        "product_cover_residual_tensor_claimed",
        "support_incidence_identified",
        "endpoint_closure_credit",
        "stage32_main_credit",
        "perfect_cuboid_credit",
        "hostile_audit_credit",
        "merge_implied",
    ))

    print("PASS: Stage32 EX6 product-cover RH equivalence wall")
    print("gY=134 gD=533 R105=224 R81=416 total=640")
    print("combined nonnode product-cover ramification = 8E")
    print("decision: degree-only product-cover RH route is AR-equivalent; O266 remains open")


if __name__ == "__main__":
    main()
