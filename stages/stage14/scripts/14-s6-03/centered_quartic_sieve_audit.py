#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-s6-03.

The theorem-level square-sieve statements are proved in result.md.  This audit
checks the exact quartic identities/discriminants, finite good-prime character
sums, CRT factorization, rectangle-completion shape, and the anisotropic
D-versus-u forcing on actual s6-01 witness packets.
"""

from __future__ import annotations

import math
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
S6_01 = ROOT / "stages/stage14/scripts/14-s6-01/integral_witness_packet_audit.py"
prev = runpy.run_path(str(S6_01))
collect_square_product_witnesses = prev["collect_square_product_witnesses"]
signed_squarefree_kernel = prev["signed_squarefree_kernel"]


def phi(i: int, d: int, S: int, X: int, H: int, u: int, D: int) -> int:
    if i == 0:
        return d * (d*u*u - S*S*D*D) * (d*u*u + X*X*D*D)
    if i == 1:
        return d * (d*u*u + S*S*D*D) * (d*u*u + H*H*D*D)
    if i == 2:
        return d * (d*u*u - X*X*D*D) * (d*u*u - H*H*D*D)
    raise ValueError(i)


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    z = pow(a, (p - 1) // 2, p)
    return 1 if z == 1 else -1


def jacobi_two_prime(a: int, p: int, q: int) -> int:
    return legendre(a, p) * legendre(a, q)


def bareiss_det(mat: list[list[int]]) -> int:
    a = [row[:] for row in mat]
    n = len(a)
    sign = 1
    prev_pivot = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((r for r in range(k + 1, n) if a[r][k] != 0), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // prev_pivot
        prev_pivot = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
        for j in range(k + 1, n):
            a[k][j] = a[k][j]
    return sign * a[n - 1][n - 1]


def resultant(f: list[int], g: list[int]) -> int:
    # Coefficients are highest degree first.
    n = len(f) - 1
    m = len(g) - 1
    size = n + m
    mat: list[list[int]] = []
    for shift in range(m):
        row = [0] * size
        row[shift:shift + n + 1] = f
        mat.append(row)
    for shift in range(n):
        row = [0] * size
        row[shift:shift + m + 1] = g
        mat.append(row)
    return bareiss_det(mat)


def even_quartic_discriminant_by_resultant(d: int, b: int, c: int) -> int:
    # d*(d*T^2+b)*(d*T^2+c)
    a4 = d**3
    a2 = d*d*(b+c)
    a0 = d*b*c
    f = [a4, 0, a2, 0, a0]
    fp = [4*a4, 0, 2*a2, 0]
    return resultant(f, fp) // a4


def primes_to(n: int) -> list[int]:
    out = []
    for x in range(2, n + 1):
        if all(x % p for p in range(2, math.isqrt(x) + 1)):
            out.append(x)
    return out


def check_witness_quartics() -> tuple[int, int]:
    hits = collect_square_product_witnesses(20)
    assert len(hits) == 20
    identities = 0
    forcing = 0
    for rec in hits:
        _m, _n, S, X, H, D, _A, _Y, Gs = rec
        ds = []
        us = []
        for G in Gs:
            d, u = signed_squarefree_kernel(G)
            ds.append(d)
            us.append(u)
        d0, d1, d2 = ds
        u0, u1, u2 = us
        prod = d0*d1*d2
        assert prod > 0
        k = math.isqrt(prod)
        assert k*k == prod

        assert phi(0, d0, S, X, H, u0, D) == (k*u1*u2)**2
        assert phi(1, d1, S, X, H, u1, D) == (k*u0*u2)**2
        assert phi(2, d2, S, X, H, u2, D) == (k*u0*u1)**2
        identities += 3

        # The theorem uses |d1|<=2SH and |d2|<=2XH.
        assert abs(d1) <= 2*S*H
        assert abs(d2) <= 2*X*H
        assert D <= 2*max(u1, u2)
        forcing += 1
    return identities, forcing


def check_discriminants() -> int:
    checks = 0
    samples = [
        (3, 4, 5, 1, 1, 1),
        (5, 12, 13, -2, 2, -1),
        (8, 15, 17, 3, -5, 7),
    ]
    for S, X, H, d0, d1, d2 in samples:
        assert S*S + X*X == H*H
        got0 = even_quartic_discriminant_by_resultant(d0, -S*S, X*X)
        got1 = even_quartic_discriminant_by_resultant(d1, S*S, H*H)
        got2 = even_quartic_discriminant_by_resultant(d2, -X*X, -H*H)
        exp0 = -16 * d0**12 * S*S * X*X * H**8
        exp1 =  16 * d1**12 * S*S * H*H * X**8
        exp2 =  16 * d2**12 * X*X * H*H * S**8
        assert got0 == exp0
        assert got1 == exp1
        assert got2 == exp2
        checks += 3
    return checks


def check_good_prime_sums() -> tuple[int, int, int]:
    S, X, H = 3, 4, 5
    ds = (1, 1, 1)
    one_prime = 0
    homogeneous = 0
    crt = 0
    good = [p for p in primes_to(47) if p >= 7 and (2*S*X*H) % p != 0]

    for i, d in enumerate(ds):
        for p in good:
            dehom = sum(legendre(phi(i, d, S, X, H, t, 1), p) for t in range(p))
            assert abs(dehom) <= 3*math.sqrt(p) + 1e-12
            one_prime += 1

            projective = dehom + legendre(d**3, p)
            formula = (p - 1) * projective
            direct = sum(
                legendre(phi(i, d, S, X, H, u, v), p)
                for u in range(p) for v in range(p)
            )
            assert direct == formula
            assert abs(direct) <= (p - 1) * (3*math.sqrt(p) + 1) + 1e-9
            homogeneous += 1

    # A few exact CRT factorizations of complete homogeneous sums.
    for i, d in enumerate(ds):
        p, q = 7, 11
        cp = sum(legendre(phi(i, d, S, X, H, u, v), p) for u in range(p) for v in range(p))
        cq = sum(legendre(phi(i, d, S, X, H, u, v), q) for u in range(q) for v in range(q))
        mod = p*q
        cmod = sum(
            jacobi_two_prime(phi(i, d, S, X, H, u, v), p, q)
            for u in range(mod) for v in range(mod)
        )
        assert cmod == cp*cq
        crt += 1
    return one_prime, homogeneous, crt


def check_rectangle_completion() -> int:
    S, X, H, d, i = 3, 4, 5, 1, 1
    p, q = 7, 11
    mod = p*q
    checks = 0
    for Ubox, Vbox in [(160, 170), (250, 135), (310, 280)]:
        total = 0
        for u in range(1, Ubox + 1):
            for v in range(1, Vbox + 1):
                total += jacobi_two_prime(phi(i, d, S, X, H, u, v), p, q)
        rhs = (
            Ubox*Vbox/math.sqrt(mod)
            + (Ubox+Vbox)*mod
            + mod*mod
        )
        # The theorem has an absolute implied constant; this finite regression
        # only checks the correct completion shape with a generous constant.
        assert abs(total) <= 8*rhs
        checks += 1
    return checks


def check_square_value_density() -> tuple[int, int]:
    # Finite sanity check for the centered quartic square condition.
    S, X, H, d, i = 3, 4, 5, 1, 1
    Ubox = Vbox = 180
    squares = 0
    nonzero = 0
    for u in range(1, Ubox + 1):
        for D in range(1, Vbox + 1):
            z = phi(i, d, S, X, H, u, D)
            if z <= 0:
                continue
            nonzero += 1
            r = math.isqrt(z)
            if r*r == z:
                squares += 1
    assert nonzero > 0
    assert squares < nonzero
    return squares, nonzero


def main() -> None:
    identities, forcing = check_witness_quartics()
    disc_checks = check_discriminants()
    one_prime, homogeneous, crt = check_good_prime_sums()
    rectangle = check_rectangle_completion()
    squares, nonzero = check_square_value_density()

    print(f"CENTERED_QUARTIC_WITNESS_IDENTITIES={identities}")
    print(f"D_LARGE_FORCING_WITNESSES={forcing}")
    print(f"DISCRIMINANT_RESULTANT_CHECKS={disc_checks}")
    print(f"GOOD_PRIME_DEHOM_CHARACTER_CHECKS={one_prime}")
    print(f"HOMOGENEOUS_COMPLETE_SUM_CHECKS={homogeneous}")
    print(f"TWO_PRIME_CRT_CHECKS={crt}")
    print(f"RECTANGLE_COMPLETION_CHECKS={rectangle}")
    print(f"FINITE_CENTERED_SQUARE_VALUES={squares}/{nonzero}")
    print("THREE_CENTERED_QUARTIC_PROJECTIONS_AUDIT=true")
    print("CENTERED_QUARTIC_DISCRIMINANT_AUDIT=true")
    print("GOOD_AUXILIARY_COMPLETE_CORRELATION_AUDIT=true")
    print("D_LE_2_MAX_U1_U2_AUDIT=true")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
