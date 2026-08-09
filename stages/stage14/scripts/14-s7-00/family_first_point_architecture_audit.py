#!/usr/bin/env python3
"""Deterministic architecture audit for Stage14-s7-00.

Checks:
- merged s6-10 closure and merged 4bn exact active-direction receiver;
- exact Jacobi normalization of the moving direction quartic;
- exact degree-two Legendre-type quotient identity;
- fourth-power base-change parameter;
- base-height / physical-height exponent conversions;
- architecture locks: generic Mordell-Weil is a prerequisite, not a claimed result.
"""
from fractions import Fraction
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
S610 = ROOT / "stages/stage14/14-s6-10/result.md"
FOURBN = ROOT / "stages/stage14/14-4bn/result.md"
RESULT = ROOT / "stages/stage14/14-s7-00/result.md"


def check_predecessors():
    s610 = S610.read_text()
    fourbn = FOURBN.read_text()
    assert "STAGE14_S6_10=COMPLETE_ACTIVE_DIRECTION_OBSTRUCTION_AND_S6_METHOD_CLOSURE" in s610
    assert "S6_METHOD_CLOSED=true" in s610
    assert "STAGE14_4BN=EXACT_PHYSICAL_PAIR_BIJECTION_AND_ACTIVE_DIRECTION_REDUCTION" in fourbn
    assert "PHYSICAL_EDGE_TO_CROSS_SQUARE_PAIR_BIJECTION=true" in fourbn
    assert "PHYSICAL_EDGE_ACTIVE_DIRECTION_EXPONENT_EQUIVALENCE=true" in fourbn


def check_jacobi_identity():
    checks = 0
    quotient_checks = 0
    for b in range(2, 13):
        for a in range(1, b):
            if gcd(a, b) != 1:
                continue
            r = Fraction(a, b)
            lam = r ** 4
            assert lam == Fraction(a**4, b**4)

            # Universal anchor.
            x0 = Fraction(0, 1)
            f0 = (b * b * x0 * x0 - a * a) * (b * b - a * a * x0 * x0)
            assert -f0 == a * a * b * b

            # Branch positions in normalized u-coordinate.
            for u in (Fraction(1), Fraction(-1), Fraction(b * b, a * a), Fraction(-b * b, a * a)):
                rhs = (1 - u * u) * (1 - lam * u * u)
                assert rhs == 0

            # Evaluate the exact normalization at many rational x values.
            for q in range(1, 8):
                for p in range(-7, 8):
                    x = Fraction(p, q)
                    u = Fraction(b, a) * x
                    f = (b * b * x * x - a * a) * (b * b - a * a * x * x)
                    lhs = -f / Fraction(a * a * b * b)
                    rhs = (1 - u * u) * (1 - lam * u * u)
                    assert lhs == rhs
                    checks += 1

                    # Quotient identity.  If v^2=rhs and U=u^2,V=u*v,
                    # then V^2=U(1-U)(1-lambda U).
                    U = u * u
                    legendre_rhs = U * (1 - U) * (1 - lam * U)
                    assert legendre_rhs == U * rhs
                    quotient_checks += 1
    assert checks > 1000
    assert quotient_checks == checks
    return checks, quotient_checks


def check_exponent_ledger():
    # B = T^2 on dyadic direction-height boxes.
    assert 2 * Fraction(41, 42) == Fraction(41, 21)
    assert 2 * Fraction(61, 63) == Fraction(122, 63)
    assert Fraction(41, 21) - Fraction(122, 63) == Fraction(1, 63)
    assert 2 * Fraction(1, 2) == Fraction(1, 1)
    assert Fraction(41, 21) - Fraction(1, 1) == Fraction(20, 21)

    # Ambient primitive directions have two base coordinates.
    assert Fraction(2, 1) - Fraction(41, 21) == Fraction(1, 21)


def check_architecture_locks():
    text = RESULT.read_text()
    required = [
        "STAGE14_S7_00=COMPLETE_FAMILY_FIRST_NONBOUNDARY_POINT_ARCHITECTURE",
        "S6_METHOD_ACCEPTED_AS_CLOSED=true",
        "DIRECTION_FAMILY_JACOBI_NORMALIZATION_EXACT=true",
        "JACOBI_PARAMETER_IS_FOURTH_POWER_BASE_CHANGE=true",
        "LEGENDRE_TYPE_DEGREE_TWO_QUOTIENT_EXACT=true",
        "PHYSICAL_POINT_REQUIRES_SQUARE_U_LIFT=true",
        "CURRENT_ACTIVE_DIRECTION_EXPONENT_T=41/21",
        "ACTIVE_DIRECTION_SAVING_TO_CROSS_CEILING_T=1/63",
        "ACTIVE_DIRECTION_SAVING_TO_SQRT_T=20/21",
        "GENERIC_MORDELL_WEIL_GROUP_AUDITED=false",
        "GENERIC_NONBOUNDARY_SECTIONS_CLASSIFIED=false",
        "S7_GENERIC_SECTION_AUDIT_IS_MANDATORY=true",
        "S7_PRIMARY_GATE=GENERIC_MORDELL_WEIL_AND_SECTION_CLASSIFICATION",
        "PLAIN_POSITIVE_RANK_DENSITY_PRIMARY=false",
        "PLAIN_GLOBAL_SOLUBILITY_PRIMARY=false",
        "FIXED_FIBER_RECOUNT_PRIMARY=false",
        "TOTAL_SPACE_DETERMINANT_RESERVED_AFTER_SECTION_AUDIT=true",
        "MOVING_CANONICAL_PRIME_SPIN_SECONDARY=true",
        "S7_METHOD_CLOSED=false",
        "NEXT=Stage14-s7-01",
    ]
    for item in required:
        assert item in text, item


def main():
    check_predecessors()
    checks, quotient_checks = check_jacobi_identity()
    check_exponent_ledger()
    check_architecture_locks()

    print(f"jacobi rational identity checks={checks}")
    print(f"legendre quotient identity checks={quotient_checks}")
    print("MERGED_S6_10_BOUNDARY_AUDIT=true")
    print("MERGED_4BN_BOUNDARY_AUDIT=true")
    print("JACOBI_NORMALIZATION_AUDIT=true")
    print("FOURTH_POWER_BASE_CHANGE_AUDIT=true")
    print("LEGENDRE_QUOTIENT_AUDIT=true")
    print("BASE_HEIGHT_EXPONENT_LEDGER_AUDIT=true")
    print("GENERIC_SECTION_GATE_AUDIT=true")
    print("ROUTE_SELECTION_AUDIT=true")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
