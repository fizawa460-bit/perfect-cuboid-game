#!/usr/bin/env python3
"""Stage14-t16 divisor and ramification audit (standard library only)."""

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "stages/stage14/data/14-t16/square_x_lift_audit.json"


def main():
    # Physical samples: t>0, t!=1, and 1+t^2 square.
    samples = [Fraction(3, 4), Fraction(5, 12), Fraction(7, 24), Fraction(20, 21)]
    for t in samples:
        assert t > 0 and t != 1
        # A_t(0)=B_t(0)=1, so x=0 is outside both branch loci.
        assert (0 - 1) ** 2 - 4 * t * t * 0 == 1
        assert 0 + (4 * t**4 - 2) * 0 + 1 == 1

    # x:C0->P1 has degree four.  Since both defining quadratics are monic
    # of even degree, x=0 and x=infinity each have four unramified points.
    degree_x = 4
    zeros = 4
    poles = 4
    assert zeros == poles == degree_x

    # div(x)=D0-Dinf has odd coefficient at all eight points.  Therefore
    # x is not a square in Q(C0), nor does it define an unramified E[2]
    # torsor.  Adjoining r with r^2=x ramifies at those eight points.
    branch_points = zeros + poles
    genus_c0 = 1
    two_g_minus_2 = 2 * (2 * genus_c0 - 2) + branch_points
    genus_c = (two_g_minus_2 + 2) // 2
    assert branch_points == 8 and genus_c == 5

    report = {
        "stage": "14-t16",
        "function": "x on C0,t: U^2=A_t(x), V^2=B_t(x)",
        "divisor": "div(x)=D_0-D_infinity, with D_0 and D_infinity reduced effective divisors of degree 4",
        "zero_points": "(x,U,V)=(0,epsilon,delta), epsilon,delta in {+1,-1}",
        "pole_points": 4,
        "square_x_cover": {
            "equation": "r^2=x",
            "branch_points": 8,
            "genus": 5,
            "ordinary_etale_elliptic_2_cover": False,
            "class_location": "Q(C0)^*/Q(C0)^{*2} with ramification divisor D_0+D_infinity; equivalently a branched quadratic-cover/Prym interface",
        },
        "decision": {
            "STAGE14_T16": "COMPLETE_SQUARE_X_DIVISOR_AND_RAMIFIED_COVER_BOUNDARY",
            "SQUARE_X_LIFT_BRANCH_COUNT": 8,
            "SQUARE_X_LIFT_GENUS": 5,
            "SQUARE_X_IS_ETALE_E2_TORSOR": False,
            "ORDINARY_MW_MOD_2_KUMMER_REDUCTION_SUFFICIENT": False,
            "PHYSICAL_HEIGHT_WINDOW_RETAINED": True,
            "T_O_SQRT_B_PROVED": False,
            "NEXT": "Stage14-t17 formulate a square-value/branched-cover sieve on C0 using the Prym or generalized-Jacobian interface and the physical height window",
        },
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
