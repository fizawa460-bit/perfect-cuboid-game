#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def require_text(path: Path, needles: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


def squarefree_kernel(n: int) -> int:
    assert n > 0
    out = 1
    p = 2
    x = n
    while p * p <= x:
        e = 0
        while x % p == 0:
            x //= p
            e ^= 1
        if e:
            out *= p
        p += 1 if p == 2 else 2
    if x > 1:
        out *= x
    return out


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    v = pow(a, (p - 1) // 2, p)
    return -1 if v == p - 1 else v


def audit_predecessors() -> None:
    require_text(
        ROOT / "stages/stage14/14-s7-14/result.md",
        [
            "STAGE14_S7_14=COMPLETE_LARGE_SHARED_LABEL_SHELL_AND_TRANSVERSE_K_COLLISION_RECEIVER",
            "TRANSVERSE_LABEL_K=ker(Q^2-P^2)",
            "GCD_K_XI=1",
            "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8",
        ],
    )
    require_text(
        ROOT / "stages/stage14/14-t50/result.md",
        [
            "STAGE14_T50=COMPLETE_BAD_AUXILIARY_BOUND_AND_SELECTOR_SENSITIVE_TWO_MODULUS_BOUNDARY",
            "EXTERNAL_BAD_AUXILIARY_AGGREGATE_BOUND_PROVED=true",
            "SELECTOR_SENSITIVE_TWO_MODULUS_SECOND_MOMENT_REQUIRED=true",
            "TH14_NEEDED=true",
        ],
    )


def audit_parity_normalized_k_split() -> None:
    checks = 0
    for Q in range(2, 121):
        for P in range(1, Q):
            if gcd(P, Q) != 1:
                continue
            A0 = Q - P
            B0 = Q + P
            g = gcd(A0, B0)
            assert g in (1, 2)
            A = A0 // g
            B = B0 // g
            assert gcd(A, B) == 1

            km = squarefree_kernel(A)
            kp = squarefree_kernel(B)
            k = squarefree_kernel(Q * Q - P * P)
            assert gcd(km, kp) == 1
            assert km * kp == k
            assert is_square(A // km)
            assert is_square(B // kp)

            r = isqrt(A // km)
            s = isqrt(B // kp)
            xi = squarefree_kernel(P * Q)
            hh = (P * Q) // xi
            assert is_square(hh)
            h = isqrt(hh)
            lhs = kp * kp * s**4 - km * km * r**4
            eps = 4 if g == 1 else 1
            rhs = eps * xi * h * h
            assert lhs == rhs, (P, Q, g, km, kp, lhs, rhs)
            assert gcd(k, xi) == 1
            checks += 1
    assert checks > 3000


def centered_identity(ks: list[int], primes: list[int]) -> tuple[int, int, int]:
    # c_s(p) is the Legendre value, including 0 at bad divisibility primes.
    c = [[legendre(k, p) for p in primes] for k in ks]
    n = len(ks)
    Pn = len(primes)

    left = 0
    for s in range(n):
        for t in range(n):
            if s == t:
                continue
            a_st = sum(c[s][j] * c[t][j] for j in range(Pn))
            left += a_st * a_st

    right = 0
    for i in range(Pn):
        for j in range(Pn):
            G = sum(c[s][i] * c[s][j] for s in range(n))
            D = sum((c[s][i] ** 2) * (c[s][j] ** 2) for s in range(n))
            right += G * G - D

    counts = Counter(ks)
    coff = sum(r * (r - 1) for r in counts.values())
    bad = max(sum(1 for p in primes if k % p == 0) for k in ks)
    lower = coff * max(Pn - 2 * bad, 0) ** 2
    return left, right, lower


def audit_centered_frobenius_identity() -> None:
    # First no-bad test: repeated squarefree labels give exact P^2 contribution.
    ks = [3, 5, 5, 7, 11, 15, 15, 19]
    primes = [29, 37, 41, 53, 61, 73, 89]
    left, right, lower = centered_identity(ks, primes)
    assert left == right
    assert left >= lower

    # Second test includes bad auxiliary divisors and exercises the P-2b bound.
    ks2 = [5, 5, 13, 13, 17, 29, 29, 37]
    primes2 = [13, 17, 29, 37, 41, 53, 61, 73]
    left2, right2, lower2 = centered_identity(ks2, primes2)
    assert left2 == right2
    assert left2 >= lower2
    assert right2 >= 0


def audit_raw_near_linear_countermodel() -> None:
    # A1 <= H * O(1) does not imply a power saving for A1-H.
    # Pair every label twice: H=N, A1=2N, C_off=N.
    for m in [4, 10, 50, 100]:
        rs = [2] * m
        H = sum(rs)
        A1 = sum(r * r for r in rs)
        C = sum(r * (r - 1) for r in rs)
        assert A1 == 2 * H
        assert C == H


def audit_exponent_contract() -> None:
    hmax = Fraction(1, 8)
    total = Fraction(7, 8)
    sumsq = hmax + total
    assert sumsq == 1

    rho = Fraction(1, 7)
    assert rho > hmax
    conditional = sumsq - rho
    assert conditional == Fraction(6, 7)
    assert Fraction(7, 8) - conditional == Fraction(1, 56)

    # General centered theorem gives exponent 1-rho on the critical shell.
    for rho2 in [Fraction(9, 64), Fraction(3, 20), Fraction(1, 6)]:
        assert rho2 > Fraction(1, 8)
        assert 1 - rho2 < Fraction(7, 8)


def audit_boundary() -> None:
    require_text(
        ROOT / "stages/stage14/14-s7-15/result.md",
        [
            "STAGE14_S7_15=COMPLETE_CENTERED_XI_K_COLLISION_AMPLIFIER_AND_TH14_CONTRACT",
            "CENTERED_FROBENIUS_IDENTITY_EXACT=true",
            "RAW_A1_NEAR_LINEAR_ALONE_BEATS_7_8=false",
            "CENTERED_NATURAL_SCALE_THEOREM_PROVED=false",
            "CONDITIONAL_AUXILIARY_PRIME_EXPONENT=1/7",
            "CONDITIONAL_PHYSICAL_UPPER_BOUND_EXPONENT=6/7",
            "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8",
            "TH14_NEEDED=true",
            "TH14_S7_REQUEST=CenteredXiKCollisionSecondMoment",
            "NEXT=Stage14-s7-16",
        ],
    )


def main() -> None:
    audit_predecessors()
    audit_parity_normalized_k_split()
    audit_centered_frobenius_identity()
    audit_raw_near_linear_countermodel()
    audit_exponent_contract()
    audit_boundary()
    print("STAGE14_S7_15_AUDIT=PASS")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8")
    print("CONDITIONAL_CENTERED_TARGET=6/7")
    print("TH14_NEEDED=true")


if __name__ == "__main__":
    main()
