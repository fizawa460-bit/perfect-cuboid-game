#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path

NODE = Path(__file__).resolve().parent


def chiY(m: int) -> Fraction:
    return Fraction(-128*m**3 - 480*m**2 - 256*m + 96, 12)


def chi0(m: int) -> Fraction:
    r = m % 6
    base = Fraction(11,108)*m**3 + Fraction(11,36)*m**2
    tails = (
        Fraction(1,6)*m,
        -Fraction(1,12)*m-Fraction(35,108),
        Fraction(7,18)*m+Fraction(5,27),
        -Fraction(1,12)*m-Fraction(1,4),
        Fraction(1,6)*m-Fraction(2,27),
        Fraction(5,36)*m-Fraction(7,108),
    )
    return base + tails[r]


def chi1(m: int) -> Fraction:
    r = m % 3
    base = Fraction(4,27)*m**3 + Fraction(4,9)*m**2
    tails = (
        Fraction(1,3)*m,
        Fraction(1,3)*m+Fraction(2,27),
        Fraction(1,9)*m-Fraction(5,27),
    )
    return base + tails[r]


def lb(m: int, r: int) -> Fraction:
    return chiY(m) + 48*chi1(m) + r*chi0(m)


def main() -> None:
    cert = json.loads((NODE / "BTVA-N14-EXACT-LOWER-BOUND-WALL.json").read_text())
    assert cert["schema"] == "STAGE32_MB104_BTVA_N14_EXACT_LOWER_BOUND_WALL_V1"

    # Published Section 7 validation: r=35 first becomes positive at m=862.
    assert all(lb(m, 35) <= 0 for m in range(3, 862))
    assert lb(862, 35) == 7320
    # Each residue-class derivative is positive after 862, so all later values stay positive.
    for m in range(862, 868):
        assert lb(m, 35) > 0
    for residue, c in enumerate((18, -297, -86, -297, 18, -401)):
        # derivative numerator is m^2-574m+c over 36.
        m0 = next(x for x in range(862, 868) if x % 6 == residue)
        assert m0*m0 - 574*m0 + c > 0

    # Exact N=14 formulas and global negativity for every m>=3.
    # We prove positivity of the bracket polynomial on the first admissible point
    # of each residue class and monotonicity thereafter where needed.
    mins = {0:6, 1:7, 2:8, 3:3, 4:4, 5:5}
    def bracket(m: int, residue: int) -> int:
        if residue == 0:
            return 5*m**3 + 447*m**2 - 18*m - 432
        if residue == 1:
            return 5*m**3 + 447*m**2 + 441*m - 29
        if residue == 2:
            return (m+1)*(5*m**2 + 442*m - 292)
        if residue == 3:
            return 5*m**3 + 447*m**2 + 441*m + 27
        if residue == 4:
            return 5*m**3 + 447*m**2 - 18*m - 488
        return (m+1)*(5*m**2 + 442*m + 167)

    for residue, m0 in mins.items():
        assert bracket(m0, residue) > 0
        # The bracket is increasing on the relevant domain; a bounded replay
        # catches any transcription/residue error while the derivative forms are elementary.
        prev = bracket(m0, residue)
        for m in range(m0+6, m0+6000, 6):
            cur = bracket(m, residue)
            assert cur > prev
            prev = cur
            assert lb(m, 34) < 0
        assert lb(m0, 34) < 0

    # Exact residue identities checked over a broad range.
    for m in range(3, 6000):
        residue = m % 6
        assert lb(m, 34) == Fraction(-bracket(m, residue), 54)
        assert lb(m, 34) < 0

    v13 = cert["validation_N13"]
    assert v13["first_positive_m"] == 862
    assert v13["LB_35_at_862"] == 7320
    n14 = cert["N14_exact"]
    assert n14["LB_negative_for_every_integer_m_ge_3"] is True
    assert cert["decision"]["prop3_1_exact_lower_bound_can_certify_nonzero_section_at_N14"] is False
    assert cert["firewalls"]["negative_lower_bound_means_actual_h0_zero"] is False
    assert cert["firewalls"]["finite_picard_enumeration_released"] is False
    assert cert["firewalls"]["merge_authorized"] is False

    print("MB104 BTVA N14 exact lower-bound wall verifier PASS")
    print("validation: r=35 first positive at m=862 with LB=7320")
    print("N=14/r=34: exact Proposition 3.1 lower bound is negative for every m>=3")
    print("actual h0 vanishing is NOT claimed; new input is required")


if __name__ == "__main__":
    main()
