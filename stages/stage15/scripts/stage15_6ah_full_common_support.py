#!/usr/bin/env python3
from __future__ import annotations

import math


def l_plus(z1: tuple[int, int], z2: tuple[int, int]) -> int:
    a1, b1 = z1
    a2, b2 = z2
    return a1 * a2 + b1 * b2


def l_minus(z1: tuple[int, int], z2: tuple[int, int]) -> int:
    a1, b1 = z1
    a2, b2 = z2
    return a1 * b2 - b1 * a2


def norm(z: tuple[int, int]) -> int:
    return z[0] * z[0] + z[1] * z[1]


def gmul(z: tuple[int, int], w: tuple[int, int]) -> tuple[int, int]:
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c


def gconj(z: tuple[int, int]) -> tuple[int, int]:
    return z[0], -z[1]


def prime_factors(n: int) -> list[int]:
    n = abs(n)
    out: list[int] = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out.append(n)
    return out


def radical(n: int) -> int:
    return math.prod(prime_factors(n))


def good_common_support(
    w1: tuple[int, int],
    w2: tuple[int, int],
    bad_integer: int,
) -> int:
    """Squarefree rational norm support shared by w1,w2 away from bad primes."""
    shared = math.gcd(norm(w1), norm(w2))
    out = 1
    for p in prime_factors(shared):
        if bad_integer % p:
            out *= p
    return out


def split_support(
    z1: tuple[int, int], z2: tuple[int, int], J: int
) -> tuple[int, int]:
    """Split a squarefree good J uniquely between L_+ and L_-."""
    if J <= 0 or radical(J) != J:
        raise ValueError("J must be positive and squarefree")
    if math.gcd(J, norm(z1) * norm(z2)) != 1:
        raise ValueError("J must avoid both primitive point norms")

    lp = l_plus(z1, z2)
    lm = l_minus(z1, z2)
    jp = jm = 1
    for p in prime_factors(J):
        on_plus = lp % p == 0
        on_minus = lm % p == 0
        if on_plus == on_minus:
            raise ValueError(f"prime {p} must lie on exactly one resultant factor")
        if on_plus:
            jp *= p
        else:
            jm *= p
    if jp * jm != J or math.gcd(jp, jm) != 1:
        raise AssertionError("support split failed")
    return jp, jm


def residue_kernel_size(z1: tuple[int, int], jp: int, jm: int) -> int:
    """Brute-force regression for the CRT rank-one kernel modulo J=jp*jm."""
    if math.gcd(jp, jm) != 1:
        raise ValueError("CRT factors must be coprime")
    J = jp * jm
    if J > 500:
        raise ValueError("regression helper is intentionally small")
    if math.gcd(norm(z1), J) != 1:
        raise ValueError("first point must be a unit vector modulo J")
    total = 0
    for a in range(J):
        for b in range(J):
            z2 = (a, b)
            if l_plus(z1, z2) % jp == 0 and l_minus(z1, z2) % jm == 0:
                total += 1
    return total


def pair_square_identity(
    C: int,
    K: tuple[int, int],
    w1: tuple[int, int],
    w2: tuple[int, int],
) -> dict:
    """Verify T1*conj(T2)=C^2*N(K)*(w1*conj(w2))^2."""
    T1 = gmul((C, 0), gmul(K, gmul(w1, w1)))
    T2 = gmul((C, 0), gmul(K, gmul(w2, w2)))
    lhs = gmul(T1, gconj(T2))
    xi = gmul(w1, gconj(w2))
    rhs = gmul((C * C * norm(K), 0), gmul(xi, xi))
    if lhs != rhs:
        raise AssertionError("pair square identity failed")
    return {
        "C": C,
        "K": list(K),
        "w1": list(w1),
        "w2": list(w2),
        "T1": list(T1),
        "T2": list(T2),
        "xi": list(xi),
        "lhs": list(lhs),
        "rhs": list(rhs),
    }


def synthetic_report() -> dict:
    # Composite-support regression: neither 5 nor 13 is large by itself, but J=65
    # is the full CRT modulus. Both point norms are coprime to 65.
    z1 = (4, 1)
    z2 = (2, 7)
    J = 65
    jp, jm = split_support(z1, z2, J)
    if (jp, jm) != (5, 13):
        raise AssertionError("expected 5/13 support split")
    kernel = residue_kernel_size(z1, jp, jm)
    if kernel != J:
        raise AssertionError("CRT receiver must be one rank-one line modulo J")

    # Zero-overlap logical guard for the square-target algebra itself.
    # N(w1)=5 and N(w2)=13 are coprime, yet the pair-square identity is exact.
    w1 = (2, 1)
    w2 = (3, 2)
    zero_J = good_common_support(w1, w2, bad_integer=1)
    if zero_J != 1:
        raise AssertionError("expected zero extra common support")
    square = pair_square_identity(C=6, K=(1, 2), w1=w1, w2=w2)

    return {
        "composite": {
            "z1": list(z1),
            "z2": list(z2),
            "L_plus": l_plus(z1, z2),
            "L_minus": l_minus(z1, z2),
            "J": J,
            "J_plus": jp,
            "J_minus": jm,
            "residue_kernel_size": kernel,
        },
        "zero_overlap_guard": {
            "J": zero_J,
            "N_w1": norm(w1),
            "N_w2": norm(w2),
            "pair_square": square,
            "physical_witness": False,
            "purpose": "logical guard for the exact pair-square algebra only",
        },
    }


if __name__ == "__main__":
    report = synthetic_report()
    c = report["composite"]
    z = report["zero_overlap_guard"]
    print("STAGE15_6AH_FULL_COMMON_SUPPORT=PASS")
    print(
        f"COMPOSITE_J={c['J']} JPLUS={c['J_plus']} JMINUS={c['J_minus']} "
        f"KERNEL={c['residue_kernel_size']}"
    )
    print(f"ZERO_SUPPORT_J={z['J']} PAIR_SQUARE=PASS")
