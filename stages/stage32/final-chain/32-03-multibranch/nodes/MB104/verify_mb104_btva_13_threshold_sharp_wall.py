#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path

NODE = Path(__file__).resolve().parent


def main() -> None:
    cert = json.loads((NODE / "BTVA-13-THRESHOLD-SHARP-WALL.json").read_text())
    assert cert["schema"] == "STAGE32_MB104_BTVA_13_THRESHOLD_SHARP_WALL_V1"

    chi0 = Fraction(11, 108)
    chi1 = Fraction(16, 108)
    c35 = Fraction(1, 108)

    # Section 7 value plus Proposition 3.3 increment gives the full affine formula.
    def C(r: int) -> Fraction:
        return c35 + (r - 35) * chi0

    assert C(35) == Fraction(1, 108)
    assert C(34) == Fraction(-5, 54)
    assert C(35) - C(34) == chi0

    # Recover the underlying global RR cubic coefficient as a consistency check.
    chiY = C(35) - 48 * chi1 - 35 * chi0
    assert chiY == Fraction(-32, 3)

    for r in range(0, 49):
        assert C(r) == Fraction(11 * r - 384, 108)
        assert (C(r) > 0) == (r >= 35)

    for N in range(0, 49):
        r = 48 - N
        assert (C(r) > 0) == (N <= 13)

    assert cert["exact_replay"]["coefficient_formula"] == "C(r)=(11*r-384)/108"
    assert cert["decision"]["threshold_13_is_sharp_for_this_lower_bound_method"] is True
    assert cert["decision"]["direct_prop3_1_asymptotic_extension_to_N14_closes"] is False
    assert cert["firewalls"]["negative_lower_bound_means_no_actual_sections"] is False
    assert cert["firewalls"]["finite_picard_enumeration_released"] is False
    assert cert["firewalls"]["merge_authorized"] is False

    print("MB104 BTVA support-13 sharp-threshold verifier PASS")
    print("C(r)=(11r-384)/108; C(35)=1/108; C(34)=-5/54")
    print("positive cubic lower-bound coefficient iff N<=13")
    print("N>=14 requires a genuinely stronger input")


if __name__ == "__main__":
    main()
