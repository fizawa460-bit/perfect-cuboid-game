#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STAGE15 = ROOT / "stages/stage15"


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing marker: {needle}")


def p1_points(p: int):
    return [(x, 1) for x in range(p)] + [(1, 0)]


def root_counts(p: int):
    a_root = 0
    b_root = 0
    both = 0
    for m, n in p1_points(p):
        for r, s in p1_points(p):
            A = (m * m * r * r + n * n * s * s) % p
            B = (m * m * s * s + n * n * r * r) % p
            ar = A == 0
            br = B == 0
            a_root += ar
            b_root += br
            both += ar and br
    return a_root, b_root, both


def rho_split(p: int) -> Fraction:
    return Fraction(
        p**4 + 4 * p**3 + 22 * p**2 + 4 * p + 1,
        (p + 1) ** 2 * (p**2 + 6 * p + 1),
    )


def rho_split_from_tubes(p: int) -> Fraction:
    y_points = p**2 + 6 * p + 1
    n00 = p**2 + 2 * p + 5
    n10 = n01 = 2 * p - 6
    n11 = 8
    even_given_one_root = Fraction(1, p + 1)
    equal_given_two_roots = Fraction(p * p + 1, (p + 1) ** 2)
    return (
        Fraction(n00, y_points)
        + Fraction(n10 + n01, y_points) * even_given_one_root
        + Fraction(n11, y_points) * equal_given_two_roots
    )


def main() -> None:
    dy = (STAGE15 / "15-6dy/result.md").read_text(encoding="utf-8")
    dz = (STAGE15 / "15-6dz/result.md").read_text(encoding="utf-8")
    ea = (STAGE15 / "15-6ea/result.md").read_text(encoding="utf-8")

    for needle in (
        "STAGE15_6DY_LOCAL_MEASURE=UNIQUE_LABELED_PHYSICAL_TORIC_STATE",
        "STAGE15_6DY_EXISTENTIAL_BASE_PROJECTION_USED=false",
        "STAGE15_6DY_LOCAL_ACCEPTANCE=vp(A)==vp(B)_MOD_2",
        "STAGE15_6DY_INERT_PRIME_ACCEPTANCE=1",
        "STAGE15_6DY_SPLIT_LOCAL_DENSITY_EXACT=true",
        "STAGE15_6DY_K1_KGT1_LOCAL_BRANCH_SPLIT_EXACT=true",
    ):
        require(dy, needle)

    for needle in (
        "STAGE15_6DZ_FIXED_PRIME_REFINED_ASYMPTOTIC=true",
        "STAGE15_6DZ_FIXED_FINITE_SET_TENSOR=true",
        "STAGE15_6DZ_EXACTLY_TWO_REFINEMENT=true",
        "STAGE15_6DZ_ERROR_UNIFORM_IN_S=false",
        "STAGE15_6DZ_GROWING_MODULUS_USED=false",
    ):
        require(dz, needle)

    for needle in (
        "STAGE15_6EA_AR035_LITERAL_FIXED_RHO_HYPOTHESIS=false",
        "STAGE15_6EA_QUALITATIVE_ZERO_DENSITY_PROVED=true",
        "STAGE15_6EA_ZERO_DENSITY_INDEPENDENT_OF_STAGE15_5=true",
        "STAGE15_6EA_FIXED_POWER_FROM_LOCAL_PARITY_TENSOR=false",
        "STAGE15_6EA_EXHAUSTIVE_VIEW_AUDIT=true",
        "STAGE15_6EA_BLIND_REDISCOVERY=true",
        "STAGE15_6EA_CLOSURE_CANDIDATE=true",
        "CURRENT_SUBSTAGE=Stage15-6ea",
    ):
        require(ea, needle)

    # On P1(F_p)^2, split primes have two Gaussian components for each norm.
    # Their only self-intersections are the four torus-fixed corners blown up in Y.
    for p in (5, 13, 17, 29):
        a_root, b_root, both = root_counts(p)
        assert a_root == 2 * p
        assert b_root == 2 * p
        assert both == 8

        # Bl_4(P1 x P1) point count and strict-divisor residue partition.
        y_points = p**2 + 6 * p + 1
        n00 = p**2 + 2 * p + 5
        n10 = n01 = 2 * p - 6
        n11 = 8
        assert n00 + n10 + n01 + n11 == y_points

        rho = rho_split(p)
        assert rho == rho_split_from_tubes(p)
        assert 0 < rho < 1

        rejection = 1 - rho
        expected = Fraction(
            4 * p * (p - 1) ** 2,
            (p + 1) ** 2 * (p**2 + 6 * p + 1),
        )
        assert rejection == expected

        rho0 = Fraction(
            p**4 + 4 * p**3 + 14 * p**2 + 4 * p + 1,
            (p + 1) ** 2 * (p**2 + 6 * p + 1),
        )
        rho1 = Fraction(
            8 * p**2,
            (p + 1) ** 2 * (p**2 + 6 * p + 1),
        )
        assert rho0 + rho1 == rho

    # Inert primes have no non-base Gaussian-norm zeros modulo p.
    for p in (3, 7, 11, 19):
        a_root, b_root, both = root_counts(p)
        assert a_root == 2
        assert b_root == 2
        assert both == 0

    # Fixed finite split-prime products decrease, but each factor tends toward 1.
    prod = Fraction(1, 1)
    previous = prod
    for p in (5, 13, 17, 29):
        prod *= rho_split(p)
        assert prod < previous
        previous = prod

    print("Stage15-6 fixed-prime overlap dy-ea: PASS")


if __name__ == "__main__":
    main()
