#!/usr/bin/env python3
"""Deterministic audit for Stage14-X8.

The theorem proof is in stages/stage14/14-X8/result.md.  This script locks the
merged predecessor boundaries, verifies the exact common-core scale
substitution, exhausts a fine rational grid of the balanced strip, and checks
the unique 2/3 saturation ledger with exact Fraction arithmetic.
"""

from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[4]


def in_strip(theta: Fraction, phi: Fraction) -> bool:
    return (
        Fraction(3, 16) <= theta <= Fraction(5, 16)
        and Fraction(1, 8) <= phi <= Fraction(1, 4)
        and theta >= phi
        and theta - phi <= Fraction(1, 8)
        and theta + phi >= Fraction(3, 8)
    )


def common_core_exponent(theta: Fraction, phi: Fraction) -> Fraction:
    return 2 * theta + 2 * phi - Fraction(3, 4)


def s7_30_exponent(theta: Fraction, phi: Fraction) -> Fraction:
    return max(
        theta + phi + Fraction(1, 8),
        1 - 2 * theta,
    )


def dual_cayley_exponent_raw(theta: Fraction, phi: Fraction) -> Fraction:
    c = common_core_exponent(theta, phi)
    return Fraction(1, 2) + 2 * phi - c


def dual_cayley_exponent_pinned(theta: Fraction) -> Fraction:
    return Fraction(5, 4) - 2 * theta


def combined_exponent(theta: Fraction, phi: Fraction) -> Fraction:
    return min(s7_30_exponent(theta, phi), dual_cayley_exponent_raw(theta, phi))


def algebraic_substitution_audit() -> None:
    # Verify the exact cancellation symbolically on enough independent rational
    # inputs; the identity itself is immediate from the definitions above.
    samples = [
        (Fraction(3, 16), Fraction(3, 16)),
        (Fraction(1, 4), Fraction(1, 4)),
        (Fraction(7, 24), Fraction(1, 4)),
        (Fraction(5, 16), Fraction(1, 4)),
    ]
    for theta, phi in samples:
        if not in_strip(theta, phi):
            continue
        assert dual_cayley_exponent_raw(theta, phi) == dual_cayley_exponent_pinned(theta)


def exact_case_split_audit() -> None:
    theta0 = Fraction(7, 24)
    target = Fraction(2, 3)

    # Left side: phi<=1/4 and theta<=7/24 imply both s7-30 branches <=2/3.
    assert theta0 + Fraction(1, 4) + Fraction(1, 8) == target
    assert 1 - 2 * Fraction(3, 16) == Fraction(5, 8) < target

    # Right side: theta>=7/24 implies the dual-Cayley branch <=2/3.
    assert dual_cayley_exponent_pinned(theta0) == target

    # Equality data.
    phi0 = Fraction(1, 4)
    c0 = common_core_exponent(theta0, phi0)
    assert c0 == Fraction(1, 3)
    assert s7_30_exponent(theta0, phi0) == target
    assert dual_cayley_exponent_raw(theta0, phi0) == target
    assert combined_exponent(theta0, phi0) == target


def rational_strip_exhaustion() -> tuple[int, Fraction, list[tuple[Fraction, Fraction]]]:
    # 1/192 mesh contains all named rational endpoints: 3/16, 5/16, 1/8,
    # 1/4 and the new 7/24 crossing.  This is a deterministic regression, not
    # a replacement for the case-split proof in result.md.
    den = 192
    checked = 0
    worst = Fraction(0)
    equality = []

    for ti in range(0, den + 1):
        theta = Fraction(ti, den)
        for pi in range(0, den + 1):
            phi = Fraction(pi, den)
            if not in_strip(theta, phi):
                continue
            checked += 1
            c = common_core_exponent(theta, phi)
            assert c >= 0
            assert dual_cayley_exponent_raw(theta, phi) == dual_cayley_exponent_pinned(theta)
            e = combined_exponent(theta, phi)
            assert e <= Fraction(2, 3)
            if e > worst:
                worst = e
                equality = [(theta, phi)]
            elif e == worst:
                equality.append((theta, phi))

    assert checked > 0
    assert worst == Fraction(2, 3)
    assert equality == [(Fraction(7, 24), Fraction(1, 4))]
    return checked, worst, equality


def corner_scale_audit() -> None:
    theta = Fraction(7, 24)
    phi = Fraction(1, 4)
    c = common_core_exponent(theta, phi)

    mu = 2 * theta - 2 * phi
    nu = Fraction(1, 4) + 2 * phi - 2 * theta
    first_pair = 2 * phi - c
    sqrt_term = nu / 2
    quotient_modulus_term = nu - c

    assert c == Fraction(1, 3)
    assert mu == Fraction(1, 12)
    assert nu == Fraction(1, 6)
    assert first_pair == Fraction(1, 6)
    assert sqrt_term == Fraction(1, 12)
    assert quotient_modulus_term == -Fraction(1, 6)

    s_count = c + mu + first_pair + sqrt_term
    d_count = Fraction(1, 2) + 2 * phi - c
    assert s_count == Fraction(2, 3)
    assert d_count == Fraction(2, 3)

    # X7 Gaussian quotient norm: H_k^+ exponent 2theta, divide by C.
    gaussian_quotient_norm = 2 * theta - c
    xi_switch = Fraction(3, 4) - 2 * phi
    assert gaussian_quotient_norm == Fraction(1, 4)
    assert xi_switch == Fraction(1, 4)

    assert Fraction(11, 16) - Fraction(2, 3) == Fraction(1, 48)
    assert Fraction(2, 3) - Fraction(1, 2) == Fraction(1, 6)


def superseded_corner_audit() -> None:
    # s7-30's former top corner is killed to 5/8 by the dual ledger.
    theta = Fraction(5, 16)
    phi = Fraction(1, 4)
    assert dual_cayley_exponent_raw(theta, phi) == Fraction(5, 8)

    # 4cq's former symmetric corner is killed to 5/8 by the two-sided ledger.
    theta = Fraction(1, 4)
    phi = Fraction(1, 4)
    assert s7_30_exponent(theta, phi) == Fraction(5, 8)


def boundary_audit() -> None:
    x7 = (ROOT / "stages/stage14/14-X7/result.md").read_text()
    s30 = (ROOT / "stages/stage14/14-s7-30/result.md").read_text()
    cq = (ROOT / "stages/stage14/14-4cq/result.md").read_text()

    assert "STAGE14_X7=COMPLETE_SELF_GENERATED_FOUR_ROOT_UNCHARGING_AND_GAUSSIAN_QUOTIENT_RESULTANT_REDUCTION" in x7
    assert "SECOND_DETERMINANT_SPACING_FROM_POINTWISE_FOUR_ROOT_DATA=false" in x7
    assert "STAGE14_S7_30=COMPLETE_TWO_SIDED_COMMON_CORE_QUADRATIC_ROOT_PAIR_COUNT_AND_11_16_BOUND" in s30
    assert "COMMON_CORE_SCALE_EXPONENT=2*theta+2*phi-3/4" in s30
    assert "DYADIC_TWO_SIDED_BLOCK_EXPONENT=max(theta+phi+1/8,1-2*theta)" in s30
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=11/16" in s30
    assert "STAGE14_4CQ=COMPLETE_DUAL_COMMON_CORE_CAYLEY_DIVISOR_COLLAPSE_AND_SYMMETRIC_QUARTER_QUARTER_REDUCTION" in cq
    assert "ALTERNATIVE_DUAL_CAYLEY_BLOCK_EXPONENT=1/2+2phi-c" in cq
    assert "DUAL_COMMON_CORE_CAYLEY_DIVISOR_LOCK_PROVED=true" in cq


def main() -> None:
    boundary_audit()
    algebraic_substitution_audit()
    exact_case_split_audit()
    corner_scale_audit()
    superseded_corner_audit()
    checked, worst, equality = rational_strip_exhaustion()

    print("Stage14-X8 two-sided / dual-Cayley minimax audit: PASS")
    print(f"balanced rational mesh points checked: {checked}")
    print(f"worst combined exponent on mesh: {worst}")
    print(f"unique mesh saturation: theta={equality[0][0]}, phi={equality[0][1]}")
    print("common-core scale pin: c=2theta+2phi-3/4")
    print("dual-Cayley after scale pin: 5/4-2theta")
    print("whole-family exponent promoted: 2/3")
    print("improvement over 11/16: 1/48")
    print("new saturation: theta=7/24, phi=1/4, c=1/3")
    print("gap to sqrt scale: 1/6")
    print("X8 auxiliary H needed: false")


if __name__ == "__main__":
    main()
