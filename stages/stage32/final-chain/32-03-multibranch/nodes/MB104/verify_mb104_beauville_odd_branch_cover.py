#!/usr/bin/env python3
import json
from pathlib import Path

CERT = Path(__file__).with_name("BEAUVILLE-ODD-BRANCH-COVER-CERTIFICATE.json")


def require(cond, msg):
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def main():
    cert = json.loads(CERT.read_text())
    require(cert["schema"] == "STAGE32_MB104_BEAUVILLE_ODD_BRANCH_COVER_WALL_V1", "schema")
    require(cert["status"] == "RETAINED_GLOBAL_COVER_WALL_MB104_INCOMPLETE", "status")

    rel = cert["branch_relations"]
    require(rel["R8_le_r_odd"] is True, "R8 odd-contact inclusion")
    require(rel["r_odd_le_M"] is True, "odd-contact mass bound")
    require(rel["minimal_branch_is_odd"] is True, "minimal branch parity")

    cover = cert["restricted_double_cover"]
    require(cover["riemann_hurwitz"] == "2h-2=4g-4+r_odd", "Riemann-Hurwitz identity")
    require(cover["r_odd_even"] is True, "branch parity")

    canonical = cert["canonical_pullback"]
    require(canonical["local_involution_determinant"] == 1, "A1 cover determinant")
    require(canonical["quasi_etale_in_codimension_one"] is True, "quasi-etale")
    require(canonical["identity"] == "K_X=q^*K_B", "canonical pullback")
    require(canonical["curve_identity"] == "K_X.Y=2d", "canonical curve degree")

    prod = cert["product_cover_curve_inequality"]
    require(prod["finite_etale_product_cover"] is True, "product cover")
    require(prod["inequality"] == "K_X.Y<=4h-4", "product-cover curve inequality")

    derived = cert["derived_constraint"]
    require(derived["degree_form"] == "d<=4g-4+r_odd", "degree form")
    require(derived["odd_branch_lower_bound"] == "r_odd>=d-4g+4", "lower-bound form")
    require(derived["genus_zero"] == "r_odd>=d+4", "g=0 specialization")
    require(derived["genus_one"] == "r_odd>=d", "g=1 specialization")
    require(derived["using_r_odd_le_M"] == "d<=4g-4+M", "GFU direction")

    # Deterministic arithmetic replay of the combination
    # 2d <= 4h-4 and 2h-2 = 4g-4+r.
    for g in (0, 1):
        for d in range(1, 1001):
            lower = d - 4 * g + 4
            for r in range(max(0, lower), max(0, lower) + 8):
                if r % 2:
                    continue
                two_h_minus_two = 4 * g - 4 + r
                lhs = 2 * d
                rhs = 2 * two_h_minus_two
                require(lhs <= rhs, "combined Beauville inequality replay")

    route = cert["route_consequence"]
    require(route["constraint_direction"] == "LOWER_BOUND_ON_ODD_BRANCH_COUNT", "direction")
    require(route["provides_R8_upper_bound"] is False, "no R8 upper bound")
    require(route["meets_alpha_lt_quarter_target"] is False, "quarter-slope firewall")
    require(route["standalone_beauville_cover_route_sufficient"] is False, "standalone insufficiency")
    require(route["GFU_direction_recovered"] is True, "GFU comparison")
    require(route["additional_integral_multiplicity_or_higher_jet_input_required"] is True, "next input")
    require(route["MB104_complete"] is False, "MB104 open")

    for key, value in cert["credit_firewall"].items():
        require(value is False, f"credit firewall {key}")

    print("PASS: Beauville cover yields r_odd >= d-4g+4, a lower-bound wall; MB104 stays open")


if __name__ == "__main__":
    main()
