#!/usr/bin/env python3
import json
from pathlib import Path

CERT_PATH = Path(__file__).with_name("BTVA-LOW-SUPPORT-FINITENESS-CERTIFICATE.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    cert = json.loads(CERT_PATH.read_text())
    require(cert["schema"] == "STAGE32_MB104_BTVA_LOW_SUPPORT_FINITE_V1", "schema")
    require(cert["status"] == "RETAINED_PARTIAL_FINITE_NON_EFFECTIVE_MB104_INCOMPLETE", "status")
    require(cert["receiver"] == "R29-LG2-MB", "receiver")

    src = cert["source_theorem"]
    require(src["arxiv"] == "1912.08908", "source arxiv")
    require(src["support_cutoff"] == 13, "support cutoff")
    require(src["first_euler_lower_bound_positive_m"] == 862, "m threshold")
    require(src["explicit_curve_list_supplied"] is False, "no explicit list")
    require(src["explicit_global_degree_cap_supplied"] is False, "no explicit degree cap")

    adap = cert["mb_adapter"]
    require(adap["support_variable"] == "N=#{i:r_i>0}", "support adapter")
    require(adap["N_counts_distinct_surface_nodes_not_normalization_branches"] is True,
            "support/branch separation")
    require(adap["N_le_13_sector_finite"] is True, "low-support finiteness")
    require(adap["potentially_infinite_sector_requires_N_ge"] == 14, "remaining support sector")
    require(adap["published_theorem_bounds_R8"] is False, "no R8 overclaim")
    require(adap["current_local_packet_supplies_R8_as_function_of_N"] is False,
            "no hidden branch cap")

    prod = cert["production_firewall"]
    require(prod["mathematical_finiteness_is_explicit_enumeration"] is False,
            "finiteness/enumeration firewall")
    require(prod["finite_degree_window_for_N_le_13_materialized"] is False,
            "no materialized degree window")
    require(prod["MB105_enumeration_released"] is False, "MB105 gate")
    require(prod["remaining_N_ge_14_sector_closed"] is False, "high-support remains open")

    boundary = cert["new_theorem_boundary"]
    require(boundary["corollary_3_4_regularizes_at_selected_A1_nodes_via_hyperplane_twist"] is True,
            "Corollary 3.4 interface")
    require(boundary["published_argument_is_support_span_based"] is True,
            "published support/span semantics")
    require(boundary["branchwise_meromorphic_R8_upper_adapter_present_in_source"] is False,
            "new-theorem firewall")

    fw = cert["credit_firewall"]
    for key in [
        "MB104_complete",
        "finite_degree_window_proved_population_wide",
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

    print("PASS: BTVA reduces possible infinite MB104 population to distinct-node support N>=14; no effective degree window claimed")


if __name__ == "__main__":
    main()
