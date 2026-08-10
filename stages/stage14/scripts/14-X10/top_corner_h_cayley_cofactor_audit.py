#!/usr/bin/env python3
"""Deterministic audit for Stage14-X10.

This script checks only the exact exponent bookkeeping and elementary
Cayley sign-allocation algebra claimed in 14-X10/result.md.  It is not a
numerical proof of the asymptotic physical theorem; the predecessor
physical identities are regression-tested separately by CI.
"""

from fractions import Fraction
from math import gcd, isqrt


F = Fraction

THETA = F(5, 16)
PHI = F(1, 4)
BARRIER = F(5, 8)


def divisors(n: int):
    n = abs(n)
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return out


def exponent_audit():
    chi = 2 * THETA + 2 * PHI - F(3, 4)
    mu = 2 * THETA - 2 * PHI
    nu = F(1, 4) + 2 * PHI - 2 * THETA

    assert chi == F(3, 8)
    assert mu == F(1, 8)
    assert nu == F(1, 8)

    qk = chi + mu
    qxi = chi + nu
    beta = F(1, 2) - THETA
    s_cell = F(3, 8) - PHI
    xy = F(1, 4)
    n_abcd = mu + nu

    assert qk == F(1, 2)
    assert qxi == F(1, 2)
    assert beta == F(3, 16)
    assert s_cell == F(1, 8)
    assert xy == F(1, 4)
    assert n_abcd == F(1, 4)

    # s7-32 one-host ledgers at the unique top corner.
    k_one_host = qk + beta
    xi_one_host = qxi + s_cell
    assert k_one_host == F(11, 16)
    assert xi_one_host == BARRIER

    # Sweep the physically allowed H exponent on a fine exact rational mesh.
    mesh = [F(i, 192) for i in range(0, 25)]  # 0 <= h <= 1/8
    large_h = 0
    hard_h = 0
    for h in mesh:
        if h > F(1, 8):
            continue

        structured_k = k_one_host - h
        c_bad = 2 * h
        c_star = chi - c_bad
        dominant = c_star / 2
        cofactor = F(1, 4) - dominant

        assert structured_k == F(11, 16) - h
        assert dominant == F(3, 16) - h
        assert cofactor == F(1, 16) + h
        assert dominant + cofactor == F(1, 4)

        if h > F(1, 16):
            large_h += 1
            assert structured_k < BARRIER
        else:
            hard_h += 1
            assert c_bad <= F(1, 8)
            assert c_star >= F(1, 4)
            assert dominant >= F(1, 8)
            assert cofactor <= F(1, 8)

    assert large_h > 0
    assert hard_h > 0

    # Exact threshold identities.
    h0 = F(1, 16)
    assert k_one_host - h0 == BARRIER
    assert 2 * h0 == F(1, 8)
    assert chi - 2 * h0 == F(1, 4)
    assert (chi - 2 * h0) / 2 == F(1, 8)
    assert F(1, 4) - (chi - 2 * h0) / 2 == F(1, 8)

    return {
        "chi": chi,
        "mu": mu,
        "nu": nu,
        "qk": qk,
        "qxi": qxi,
        "k_one_host": k_one_host,
        "xi_one_host": xi_one_host,
        "large_h_mesh_points": large_h,
        "hard_h_mesh_points": hard_h,
    }


def cayley_allocation_audit():
    """Exhaustively verify the elementary C-/C+ allocation on small data."""
    checks = 0
    dominant_checks = 0

    for m in range(1, 65):
        for n in range(1, 65):
            if m == n:
                # The physical balanced lambda=4 equality is eliminated by X6;
                # keep the algebra audit on the nonzero-difference branch.
                continue
            prod = abs((m - n) * (m + n))
            if prod == 0:
                continue
            for cstar in divisors(prod):
                if cstar <= 1 or cstar % 2 == 0:
                    continue
                if gcd(cstar, m * n) != 1:
                    continue

                cminus = gcd(cstar, abs(m - n))
                cplus = gcd(cstar, m + n)

                assert gcd(cminus, cplus) == 1
                assert cminus * cplus == cstar
                checks += 1

                csigma = max(cminus, cplus)
                assert csigma * csigma >= cstar

                if csigma == cminus:
                    e = abs(m - n)
                else:
                    e = m + n
                assert e > 0
                assert e % csigma == 0
                t = e // csigma
                assert t >= 1
                dominant_checks += 1

    assert checks > 100
    assert dominant_checks == checks
    return checks


def main():
    ex = exponent_audit()
    cayley_checks = cayley_allocation_audit()

    print("Stage14-X10 top-corner H/Cayley-cofactor audit: PASS")
    print("unique top corner: theta=5/16, phi=1/4")
    print("common-core exponent:", ex["chi"])
    print("u_res/v_res exponent max:", ex["mu"])
    print("q_k/q_xi exponent max:", ex["qk"])
    print("raw k one-host exponent:", ex["k_one_host"])
    print("xi one-host exponent:", ex["xi_one_host"])
    print("H threshold exponent: 1/16")
    print("hard-branch C_bad exponent max: 1/8")
    print("hard-branch C_star exponent min: 1/4")
    print("hard-branch dominant Cayley factor exponent min: 1/8")
    print("hard-branch short cofactor exponent max: 1/8")
    print("large-H mesh points power-saved:", ex["large_h_mesh_points"])
    print("small-H mesh points retained:", ex["hard_h_mesh_points"])
    print("finite Cayley allocation checks:", cayley_checks)
    print("current whole-family exponent remains 5/8")
    print("X10 additional whole-family power saving: false")
    print("X10 auxiliary H needed: false")


if __name__ == "__main__":
    main()
