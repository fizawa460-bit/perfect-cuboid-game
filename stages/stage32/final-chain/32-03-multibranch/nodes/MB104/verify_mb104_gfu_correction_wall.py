#!/usr/bin/env python3
import json
from pathlib import Path

CERT_PATH = Path(__file__).with_name("GFU-MULTIBRANCH-CORRECTION-CERTIFICATE.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    cert = json.loads(CERT_PATH.read_text())
    require(cert["schema"] == "STAGE32_MB104_GFU_MULTIBRANCH_CORRECTION_WALL_V1", "schema")
    require(cert["status"] == "RETAINED_NEGATIVE_ROUTE_MB104_INCOMPLETE", "status")
    require(cert["receiver"] == "R29-LG2-MB", "receiver")

    src = cert["source"]
    require(src["arxiv"] == "1804.07671", "source")
    require(src["theorem_3_1_degree"] == "-d+M+4g-4", "exact degree formula")
    require(src["corollary_3_3_smooth_node_bound"] == "d<=4g+44", "smooth-node corollary")

    mb = cert["mb_adapter"]
    require(mb["M_definition"] == "M=sum_i D.E_i=sum_i M_i", "M adapter")
    require(mb["R8_le_M"] is True, "R8<=M")
    for key in [
        "published_formula_contains_negative_branch_excess_term",
        "published_formula_contains_negative_exceptional_delta_term",
        "published_formula_contains_negative_total_delta_term",
    ]:
        require(mb[key] is False, f"no hidden correction {key}")
    require(mb["direct_nonintegral_locus_bound"] == "d<=M+4g-4", "direct bound")
    require(mb["direct_formula_upper_bounds_M_or_R8"] is False, "wrong-direction firewall")

    smooth = cert["smooth_node_specialization"]
    require(smooth["each_met_node_has_single_transverse_branch"] is True, "smooth-node semantics")
    require(smooth["M_le_48"] is True, "M<=48")
    require(smooth["recovers_d_le_4g_plus_44"] is True, "recover corollary")

    route = cert["route_consequence"]
    require(route["published_GFU_reuse_closes_R8"] is False, "GFU route remains open")
    require(route["branch_excess_or_delta_cancellation_would_be_new_theorem"] is True,
            "new-theorem boundary")
    require(route["finite_R8_bound_proved"] is False, "no R8 bound")
    require(route["MB104_complete"] is False, "MB104 open")

    fw = cert["credit_firewall"]
    for key in [
        "MB104_complete",
        "finite_degree_window_proved",
        "finite_picard_enumeration_released",
        "r29_lg2_mb_discharged",
        "receiver_credit",
        "effectivity_credit",
        "final_milestone_credit",
        "theorem_credit",
        "endpoint_credit",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
        "merge_authorized",
    ]:
        require(fw[key] is False, f"credit firewall {key}")

    print("PASS: published GFU correction is exactly M and contains no retained branch-excess/delta cancellation")


if __name__ == "__main__":
    main()
