#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-s6-02/result.md"
UPSTREAM = ROOT / "stages/stage14/14-s6-01/result.md"


def assert_contains(path: Path, needles: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


def same_p1(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return a[0] * b[1] == a[1] * b[0]


def pythagorean_samples(limit: int = 18):
    out = []
    for m in range(2, limit + 1):
        for n in range(1, m):
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            S = 2 * m * n
            X = m * m - n * n
            H = m * m + n * n
            assert S * S + X * X == H * H
            out.append((S, X, H))
    return out


def check_pencil_roots_and_det() -> int:
    samples = pythagorean_samples()
    d0, d1, d2 = 3, -5, 7
    checks = 0
    for S, X, H in samples[:40]:
        roots = [(0, 1), (1, 0), (1, 1), (-X * X, S * S)]
        for i in range(4):
            for j in range(i + 1, 4):
                assert not same_p1(roots[i], roots[j]), (S, X, H, roots)
        for lam, mu in [(1, 2), (2, 3), (5, -2), (-3, 4)]:
            diag = (
                d0 * (lam - mu),
                -d1 * lam,
                d2 * mu,
                -(lam * S * S + mu * X * X),
            )
            det_diag = diag[0] * diag[1] * diag[2] * diag[3]
            formula = (
                d0
                * d1
                * d2
                * lam
                * mu
                * (lam - mu)
                * (lam * S * S + mu * X * X)
            )
            assert det_diag == formula
            checks += 1
    return checks


def projective_points_mod_p(p: int):
    # canonical representative: first nonzero coordinate equals 1
    pts = []
    for idx in range(4):
        prefix = [0] * idx + [1]
        tail_len = 3 - idx
        total = p ** tail_len
        for code in range(total):
            tail = []
            z = code
            for _ in range(tail_len):
                tail.append(z % p)
                z //= p
            pts.append(tuple(prefix + tail))
    return pts


def check_finite_field_smoothness() -> int:
    # Only a regression for good reductions; the proof in result.md is characteristic zero.
    S, X, H = 20, 21, 29
    d0, d1, d2 = 3, 5, 7
    checks = 0
    for p in (11, 13, 17):
        if any(v % p == 0 for v in (S, X, H, d0, d1, d2)):
            continue
        for u0, u1, u2, D in projective_points_mod_p(p):
            q1 = (d0 * u0 * u0 - d1 * u1 * u1 - S * S * D * D) % p
            q2 = (d2 * u2 * u2 - d0 * u0 * u0 - X * X * D * D) % p
            if q1 or q2:
                continue
            g1 = (
                2 * d0 * u0 % p,
                -2 * d1 * u1 % p,
                0,
                -2 * S * S * D % p,
            )
            g2 = (
                -2 * d0 * u0 % p,
                0,
                2 * d2 * u2 % p,
                -2 * X * X * D % p,
            )
            # Rank < 2 iff all 2x2 minors vanish.
            dependent = True
            for i in range(4):
                for j in range(i + 1, 4):
                    if (g1[i] * g2[j] - g1[j] * g2[i]) % p:
                        dependent = False
                        break
                if not dependent:
                    break
            assert not dependent, (p, (u0, u1, u2, D))
            checks += 1
    assert checks > 0
    return checks


def line_count(U: int, V: int, ell: int, rho: int) -> int:
    c = 0
    for x in range(1, U + 1):
        for y in range(1, V + 1):
            if (x - rho * y) % ell == 0 or (x + rho * y) % ell == 0:
                c += 1
    return c


def check_two_line_rectangle_bound() -> int:
    checks = 0
    for ell in (5, 7, 11, 13, 17):
        for rho in range(1, ell):
            for U, V in ((3, 4), (5, 11), (12, 7), (20, 23), (31, 9)):
                actual = line_count(U, V, ell, rho)
                # Generous absolute constant for the exact O-shape proved in result.md.
                rhs = 6 * (Fraction(U * V, ell) + min(U, V) + 1)
                assert actual <= rhs, (ell, rho, U, V, actual, rhs)
                checks += 1
    return checks


def check_sector_ledger() -> None:
    assert Fraction(41, 42) - Fraction(1, 2) == Fraction(10, 21)
    # If ell >= T and max(U,V) >= T, each nonconstant term in the
    # rectangle estimate is <= UV/T.
    for T in (2, 3, 5, 7, 11):
        for U, V in ((T, T), (T, 2 * T), (3 * T, T + 1), (1, T)):
            assert Fraction(U * V, T) <= Fraction(U * V, 1)
            assert min(U, V) <= Fraction(U * V, max(U, V))
            assert Fraction(U * V, max(U, V)) <= Fraction(U * V, T)


def main() -> None:
    assert_contains(
        UPSTREAM,
        [
            "STAGE14_S6_01=COMPLETE_INTEGRAL_GLOBAL_SMALL_POINT_WITNESS_PACKETIZATION",
            "ODD_KERNEL_EDGE_PACKET_FACTORIZATION=true",
            "FIXED_PACKET_TWO_QUADRIC_SYSTEM_EXACT=true",
        ],
    )
    det_checks = check_pencil_roots_and_det()
    smooth_checks = check_finite_field_smoothness()
    line_checks = check_two_line_rectangle_bound()
    check_sector_ledger()

    flags = [
        "STAGE14_S6_02=COMPLETE_GENUS_ONE_PACKET_GEOMETRY_AND_LARGE_PRIME_INCIDENCE_SECTOR",
        "FIXED_PACKET_PENCIL_DETERMINANT_EXACT=true",
        "FIXED_PACKET_SMOOTH_GENUS_ONE_PROVED=true",
        "POSITIVE_DIMENSIONAL_TORSION_BOUNDARY_COMPONENT=false",
        "ONE_SQUARE_VARIABLE_ELIMINATION_EXACT=true",
        "CONIC_PLUS_SQUARE_LIFT_EXACT=true",
        "CANONICAL_EDGE_LARGE_PRIME_TWO_LINE_INCIDENCE=true",
        "EDGE_LINE_RECTANGLE_BOUND_PROVED=true",
        "LARGE_EDGE_KERNEL_LONG_VARIABLE_SECTOR_POWER_SAVING_PROVED=true",
        "FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false",
        "POST_LOCAL_SAVING_REQUIRED_FOR_SQRT_B_UPPER_BOUND=10/21",
        "NEXT=Stage14-s6-03",
    ]
    assert_contains(RESULT, flags)

    print(f"pencil determinant/root checks: {det_checks}")
    print(f"good-reduction smooth projective points checked: {smooth_checks}")
    print(f"two-line rectangle regressions: {line_checks}")
    print("exponent ledger: 41/42 - 1/2 = 10/21")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
