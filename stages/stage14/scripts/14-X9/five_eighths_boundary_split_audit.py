#!/usr/bin/env python3
"""Deterministic audit for Stage14-X9.

X9 imports the merged s7-31 5/8 theorem and separates its two exact
saturation mechanisms.  The asymptotic arguments are in result.md; this audit
locks the Fraction ledger, predecessor theorem boundaries, the upper-edge
common-residual identities, the lower coreless identities, and the fact that
the former X8 2/3 corner is strictly subcritical after s7-31.
"""

from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[4]


def predecessor_boundary_audit() -> None:
    x8 = (ROOT / "stages/stage14/14-X8/result.md").read_text()
    s31 = (ROOT / "stages/stage14/14-s7-31/result.md").read_text()
    cr = (ROOT / "stages/stage14/14-4cr/result.md").read_text()
    x7 = (ROOT / "stages/stage14/14-X7/result.md").read_text()

    assert "STAGE14_X8=COMPLETE_TWO_SIDED_DUAL_CAYLEY_MINIMAX_AND_TWO_THIRDS_PROMOTION" in x8
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=2/3" in x8

    assert "STAGE14_S7_31=COMPLETE_FIXED_OUTER_COMMON_GCD_SQUARE_DIVISIBILITY_AND_5_8_BOUND" in s31
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8" in s31
    assert "OPPOSITE_QUOTIENT_COMMON_GCD_ODDPART_SQUARE_DIVIDES_C_URES=true" in s31
    assert "FIXED_OUTER_NONPRIMITIVE_ROOT_PAIR_BOUND=1+M/C" in s31
    assert "DYADIC_FIXED_OUTER_BLOCK_EXPONENT=max(2theta,1-2theta)" in s31

    assert "STAGE14_4CR=COMPLETE_TWO_THIRDS_PROMOTION_AND_CAYLEY_GAUSSIAN_ORIENTATION_FACTORIZATION" in cr
    assert "CAYLEY_GOOD_CORE_SIGN_ALLOCATION_PROVED=true" in cr
    assert "CAYLEY_C_MINUS_OPPOSITE_GAUSSIAN_ORIENTATION=true" in cr
    assert "CAYLEY_C_PLUS_SAME_GAUSSIAN_ORIENTATION=true" in cr
    assert "REMAINING_RECEIVER=TwoThirdsCayleyGaussianCommonGcdRootProductIncidence" in cr

    assert "STAGE14_X7=COMPLETE_SELF_GENERATED_FOUR_ROOT_UNCHARGING_AND_GAUSSIAN_QUOTIENT_RESULTANT_REDUCTION" in x7
    assert "FOUR_ROOT_CROSS_RESULTANT_DICTIONARY_PROVED=true" in x7
    assert "PRIVATE_GENERATED_PRIME_FORCES_CROSS_SPACING=false" in x7


def allowed(theta: Fraction, phi: Fraction) -> bool:
    return (
        Fraction(3, 16) <= theta <= Fraction(5, 16)
        and Fraction(1, 8) <= phi <= Fraction(1, 4)
        and theta >= phi
        and theta - phi <= Fraction(1, 8)
        and theta + phi >= Fraction(3, 8)
    )


def e31(theta: Fraction) -> Fraction:
    return max(2 * theta, 1 - 2 * theta)


def rational_strip_audit() -> tuple[int, int]:
    # 1/192 contains all distinguished fractions 3/16, 5/16, 7/24, 1/4.
    vals = [Fraction(n, 192) for n in range(24, 61)]
    checked = 0
    saturating = 0
    upper_seen = False
    lower_seen = False

    for theta in vals:
        for phi in vals:
            if not allowed(theta, phi):
                continue
            checked += 1
            e = e31(theta)
            assert e <= Fraction(5, 8)
            if e == Fraction(5, 8):
                saturating += 1
                if theta == Fraction(5, 16):
                    assert Fraction(3, 16) <= phi <= Fraction(1, 4)
                    upper_seen = True
                else:
                    assert theta == Fraction(3, 16)
                    assert phi == Fraction(3, 16)
                    lower_seen = True

    assert checked > 0
    assert saturating > 0
    assert upper_seen
    assert lower_seen
    return checked, saturating


def former_x8_corner_audit() -> None:
    theta = Fraction(7, 24)
    phi = Fraction(1, 4)
    assert allowed(theta, phi)
    e = e31(theta)
    assert e == Fraction(7, 12)
    assert Fraction(2, 3) - e == Fraction(1, 12)
    assert Fraction(5, 8) - e == Fraction(1, 24)


def upper_edge_audit() -> int:
    theta = Fraction(5, 16)
    count = 0
    for n in range(36, 49):  # phi in [3/16,1/4] on denominator 192.
        phi = Fraction(n, 192)
        if not allowed(theta, phi):
            continue

        chi = 2 * theta + 2 * phi - Fraction(3, 4)
        mu = 2 * theta - 2 * phi
        nu = Fraction(1, 4) + 2 * phi - 2 * theta
        first = 2 * phi - chi
        second = max(Fraction(0), nu - chi)

        assert chi == 2 * phi - Fraction(1, 8)
        assert mu == Fraction(5, 8) - 2 * phi
        assert nu == 2 * phi - Fraction(3, 8)
        assert first == Fraction(1, 8)
        assert second == 0
        assert chi + mu == Fraction(1, 2)
        assert chi + mu + first + second == Fraction(5, 8)
        assert Fraction(1, 4) <= chi <= Fraction(3, 8)
        assert chi / 2 >= Fraction(1, 8)
        count += 1

    assert count > 0
    return count


def lower_corner_audit() -> None:
    theta = phi = Fraction(3, 16)
    assert allowed(theta, phi)

    chi = 2 * theta + 2 * phi - Fraction(3, 4)
    mu = 2 * theta - 2 * phi
    nu = Fraction(1, 4) + 2 * phi - 2 * theta
    first = 2 * phi - chi
    second = max(Fraction(0), nu - chi)

    assert chi == 0
    assert mu == 0
    assert nu == Fraction(1, 4)
    assert first == Fraction(3, 8)
    assert second == Fraction(1, 4)
    assert first + second == Fraction(5, 8)

    # X6/X7 value scales at the lower coreless corner.
    agreement = 2 * theta
    xi_switch = Fraction(3, 4) - 2 * phi
    uv = 2 * phi
    assert agreement == Fraction(3, 8)
    assert xi_switch == Fraction(3, 8)
    assert uv == Fraction(3, 8)


def current_result_boundary_audit() -> None:
    result = (ROOT / "stages/stage14/14-X9/result.md").read_text()
    required = [
        "STAGE14_X9=COMPLETE_FIVE_EIGHTHS_PROMOTION_AND_UPPER_CORE_LOWER_CORELESS_BOUNDARY_SPLIT",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8",
        "IMPROVEMENT_OVER_X8_TWO_THIRDS=1/24",
        "X8_TWO_THIRDS_SATURATION_SUPERSEDED=true",
        "TWO_THIRDS_CAYLEY_GAUSSIAN_COMMON_GCD_ROOT_PRODUCT_RECEIVER_MINIMAL=false",
        "UPPER_EDGE_C_URES_EXPONENT=1/2",
        "UPPER_EDGE_FIRST_PRIMITIVE_PAIR_EXPONENT=1/8",
        "UPPER_EDGE_OPPOSITE_QUOTIENT_PAIR_EXPONENT=0",
        "LOWER_CORNER_COMMON_CORE_EXPONENT=0",
        "LOWER_CORNER_FIRST_PRIMITIVE_PAIR_EXPONENT=3/8",
        "LOWER_CORNER_OPPOSITE_QUOTIENT_PAIR_EXPONENT=1/4",
        "LOWER_CORNER_BALANCED_REAL_GAUSSIAN_VALUE_TRIAD=true",
        "REMAINING_RECEIVER=FiveEighthsSeparatedUpperCayleyLowerCorelessReciprocalEnergy",
        "X9_AUXILIARY_H_NEEDED=false",
        "NEXT_RECOMMENDED=Stage14-X10",
    ]
    for marker in required:
        assert marker in result, marker


def main() -> None:
    predecessor_boundary_audit()
    checked, saturating = rational_strip_audit()
    former_x8_corner_audit()
    upper_points = upper_edge_audit()
    lower_corner_audit()
    current_result_boundary_audit()

    print("Stage14-X9 five-eighths boundary split audit: PASS")
    print(f"balanced rational mesh points checked: {checked}")
    print(f"mesh points saturating 5/8: {saturating}")
    print(f"upper-edge phi mesh points checked: {upper_points}")
    print("current whole-family exponent: 5/8")
    print("improvement over X8 2/3: 1/24")
    print("former X8 corner exponent under s7-31: 7/12")
    print("upper edge: C*u_res exponent 1/2, first pair 1/8, second pair 0")
    print("lower corner: C exponent 0, first pair 3/8, second pair 1/4")
    print("lower corner real/Gaussian/UV triad exponent: 3/8")
    print("4cr common-gcd fixed-power receiver: superseded by s7-31")
    print("X9 additional saving below merged 5/8: false")
    print("X9 auxiliary H needed: false")


if __name__ == "__main__":
    main()
