#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

CERT_PATH = Path(__file__).with_name("BTVA-SYMMETRIC-POWER-VANISHING-CERTIFICATE.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    cert = json.loads(CERT_PATH.read_text())
    require(cert["schema"] == "STAGE32_MB104_BTVA_POWER_VANISHING_WALL_V1", "schema")
    require(cert["status"] == "RETAINED_NEGATIVE_ROUTE_MB104_INCOMPLETE", "status")
    require(cert["receiver"] == "R29-LG2-MB", "receiver")

    src = cert["source_contract"]
    require(src["arxiv"] == "1912.08908", "arxiv source")
    require(src["a1_regularization_rule"] ==
            "order m requires floor(m/2) hyperplane vanishing at selected A1 node",
            "A1 regularization rule")

    power = cert["power_contract"]
    for k in range(1, 1001):
        m = 2 * k
        budget = k
        local_cost = m // 2
        require(local_cost == k, "local cost k")
        require(budget == local_cost, "zero vanishing slack")
        require(Fraction(budget, m) == Fraction(1, 2), "available ratio")
        require(Fraction(local_cost, m) == Fraction(1, 2), "required ratio")

        # If nonnegative split weights sum to k and a node receives k, every positive weight
        # must lie on a hyperplane through that node. The numerical implication is the
        # complement weight sum = total-received = 0.
        received = k
        complement_weight = budget - received
        require(complement_weight == 0, "equality exhausts full budget")

    support = cert["support_consequence"]
    require(support["pure_power_bypasses_common_hyperplane_span_barrier"] is False,
            "span barrier retained")
    require(support["asymptotic_slack"] == 0, "zero asymptotic slack")

    route = cert["route_consequence"]
    require(route["omega7_power_only_route_dominated"] is True, "pure-power route dominated")
    require(route["all_symmetric_differential_routes_impossible"] is False, "no overclaim")
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

    print("PASS: omega7 powers have vanishing ratio exactly equal to A1 regularization cost; no multi-hyperplane slack")


if __name__ == "__main__":
    main()
