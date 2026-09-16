#!/usr/bin/env python3
import json
from pathlib import Path

CERT_PATH = Path(__file__).with_name("BTVA-SPAN-DEGREE-CERTIFICATE.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    cert = json.loads(CERT_PATH.read_text())
    require(cert["schema"] == "STAGE32_MB104_BTVA_SPAN_DEGREE_REDUCTION_V1", "schema")
    require(cert["status"] == "RETAINED_PARTIAL_EXPLICIT_REDUCTION_MB104_INCOMPLETE", "status")
    require(cert["receiver"] == "R29-LG2-MB", "receiver")

    src = cert["source"]
    require(src["arxiv"] == "1912.08908", "source")
    require(src["ambient_dimension"] == 6, "ambient dimension")
    require(src["surface_degree"] == 16, "surface degree")

    g0 = cert["genus0_reduction"]
    require(g0["all_genus0_min_distinct_nodes"] == 6, "g0 node minimum")
    require(g0["known_plane_conics"] == 32, "known conic count")
    require(g0["nonconic_min_distinct_nodes"] == 7, "nonconic node minimum")
    require(g0["nonconic_node_support_spans_P6"] is True, "nonconic full span")
    require(g0["known_conics_excluded_from_MB_by_this_certificate"] is False,
            "known-conic adapter firewall")

    g1 = cert["genus1_reduction"]
    require(g1["if_s_le_4_degree_upper"] == 16, "g1 low-span degree cap")
    require(g1["s_le_4_finite_degree_window"] is True, "g1 finite low-span window")
    require(g1["s_5_degree_upper_from_source"] is False, "no s5 overclaim")
    require(g1["s_6_degree_upper_from_source"] is False, "no s6 overclaim")
    require(g1["hard_span_dimensions"] == [5, 6], "hard g1 span sectors")

    r8 = cert["R8_interface"]
    require(r8["fsm_bound"] == "d<=16g-16+4R8", "FSM interface")
    require(r8["span_controls_distinct_surface_nodes_not_normalization_multiplicity"] is True,
            "support/branch firewall")
    require(r8["source_theorem_bounds_R8"] is False, "no R8 overclaim")

    routing = cert["routing"]
    require(routing["low_span_genus1_population_has_explicit_degree_window"] is True,
            "low-span positive reduction")
    require(routing["global_MB105_released"] is False, "global MB105 gate")
    require(routing["known_conic_nodewise_branch_adapter_required_before_MB_exclusion"] is True,
            "known conic adapter gate")

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

    print("PASS: BTVA gives full-span g0 reduction and d<=16 for genus-one support span <=4; MB104 remains open")


if __name__ == "__main__":
    main()
