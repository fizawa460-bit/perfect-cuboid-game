#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

CERT_PATH = Path(__file__).with_name("MULTIFIBRATION-RH-CAPACITY-CERTIFICATE.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    cert = json.loads(CERT_PATH.read_text())
    require(cert["schema"] == "STAGE32_MB104_MULTIFIBRATION_RH_CAPACITY_WALL_V1", "schema")
    require(cert["status"] == "RETAINED_NEGATIVE_ROUTE_MB104_INCOMPLETE", "status")
    require(cert["receiver"] == "R29-LG2-MB", "receiver")

    fib = cert["fibration_contract"]
    require(fib["total_fibrations"] == 28, "28 fibrations")
    require(fib["rank4_fibrations"] == 22, "22 rank4")
    require(fib["rank4_complementary_pairs"] == 11, "11 rank4 pairs")
    require(fib["rank3_fibrations"] == 6, "6 rank3")
    require(fib["rank4_pair_class_sum"] == "F+F'=H", "complementary class sum")
    require(fib["rank3_class_formula"] == "2F_Q=H-sum_{i in B_Q}E_i", "rank3 class formula")

    # Symbolic coefficient check: rank4 gives 11*d and rank3 gives at most 6*(d/2)=3*d.
    rank4_degree_coeff = Fraction(11, 1)
    rank3_degree_coeff = 6 * Fraction(1, 2)
    total_degree_coeff = rank4_degree_coeff + rank3_degree_coeff
    require(total_degree_coeff == 14, "sum map-degree coefficient")

    rh = cert["riemann_hurwitz_contract"]
    require(rh["per_nonconstant_map"] == "B_j=2g-2+2n_j", "RH formula")
    total_ramification_d_coeff = 2 * total_degree_coeff
    require(total_ramification_d_coeff == 28, "summed RH d coefficient")

    optimistic_charge = rh["optimistic_charge_per_branch"]
    require(optimistic_charge == 28, "optimistic all-map unit charge")
    optimistic_slope = Fraction(total_ramification_d_coeff, optimistic_charge)
    require(optimistic_slope == 1, "optimistic slope one")
    require(Fraction(1, 1) > Fraction(1, 4), "slope misses quarter threshold")
    require(rh["optimistic_unit_charging_sufficient"] is False, "unit charging not sufficient")

    threshold = cert["aggregate_charge_threshold"]
    # 28/q < 1/4 iff q > 112.
    require(28 * 4 == 112, "charge threshold arithmetic")
    require(threshold["required_for_slope_lt_quarter"] == "q>112", "q threshold")
    require(threshold["one_unit_per_map_gives_q_at_most"] == 28, "unit map charge cap")
    require(threshold["one_unit_per_map_route_structurally_insufficient"] is True,
            "simple unit charging wall")

    local = cert["local_jet_interface"]
    require(local["minimal_cusp_alone_forces_one_unit"] is False, "local jet firewall")
    require(local["current_local_packet_is_weaker_than_optimistic_capacity_test"] is True,
            "optimistic test stronger than retained packet")

    route = cert["route_consequence"]
    require(route["simple_summed_RH_unit_charging_dominated"] is True, "dominated route")
    require(route["all_fibration_arguments_proved_impossible"] is False, "no overclaim")
    require(route["finite_R8_bound_proved"] is False, "no R8 closure")
    require(route["MB104_complete"] is False, "MB104 remains open")

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

    print("PASS: even maximal 28-map unit ramification charging has R8 slope 1; MB104 still open")


if __name__ == "__main__":
    main()
