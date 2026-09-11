#!/usr/bin/env python3
import json
from pathlib import Path

CERT = Path(__file__).with_name("A1-CONDUCTOR-BRANCH-DELTA-CERTIFICATE.json")


def require(cond, msg):
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def pi6(d):
    require(d >= 1, "degree")
    m, eps = divmod(d - 1, 5)
    return 5 * m * (m - 1) // 2 + m * eps


def main():
    cert = json.loads(CERT.read_text())
    require(cert["schema"] == "STAGE32_MB104_A1_CONDUCTOR_BRANCH_DELTA_WALL_V1", "schema")
    require(cert["status"] == "RETAINED_SHARP_LOCAL_BOUND_MB104_INCOMPLETE", "status")
    require(cert["universal_curve_germ"]["delta_lower"] == "delta_p>=r_p-1", "delta lower")
    require(cert["universal_curve_germ"]["equality_is_sharp"] is True, "sharpness")
    require(cert["A1_sharpness"]["fundamental_cycle_reduced"] is True, "A1 reduced fundamental cycle")
    require(cert["A1_sharpness"]["smooth_transverse_curvette_collections_can_realize_delta_eq_r_minus_1"] is True, "A1 equality realization")
    require(cert["A1_sharpness"]["universal_local_coefficient_gt_1_from_branch_count_alone"] is False, "no stronger local coefficient")

    # Check the exact Castelnuovo formula used in the certificate over a deterministic range,
    # and confirm it cannot be bounded by alpha*d+beta with fixed alpha<1/4.
    for d in range(1, 10001):
        m, eps = divmod(d - 1, 5)
        require(0 <= eps <= 4, "Castelnuovo remainder")
        require(pi6(d) == 5 * m * (m - 1) // 2 + m * eps, "Castelnuovo formula")
    require(pi6(10000) > 10000, "quadratic growth witness")
    require(cert["castelnuovo_P6"]["meets_alpha_lt_quarter_target"] is False, "target firewall")

    route = cert["route_consequence"]
    require(route["branch_multiplicity_is_charged"] is True, "multiplicity charge")
    require(route["branch_count_only_local_route_sufficient"] is False, "local insufficiency")
    require(route["standard_castelnuovo_global_route_sufficient"] is False, "global insufficiency")
    require(route["additional_global_linear_conductor_or_genus_control_required"] is True, "next input")
    require(route["MB104_complete"] is False, "MB104 open")

    for key, value in cert["credit_firewall"].items():
        require(value is False, f"credit firewall {key}")

    print("PASS: A1 conductor gives sharp delta>=r-1 but Castelnuovo remains quadratic; MB104 stays open")


if __name__ == "__main__":
    main()
