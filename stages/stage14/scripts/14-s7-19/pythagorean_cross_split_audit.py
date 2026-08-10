#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-19.

Checks the exact cross-split -> primitive Pythagorean composition on a finite
reduced-coordinate sample.  This is a regression audit, not a proof by search.
"""

from collections import defaultdict
from fractions import Fraction
from math import gcd, isqrt


def squarefree_kernel(n: int) -> int:
    out = 1
    p = 2
    while p * p <= n:
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            out *= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out *= n
    return out


def kernel_square_root(n: int) -> tuple[int, int]:
    k = squarefree_kernel(n)
    q = n // k
    r = isqrt(q)
    assert r * r == q
    return k, r


def prime_divisors(n: int) -> list[int]:
    ans = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            ans.append(p)
            while n % p == 0:
                n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        ans.append(n)
    return ans


def legendre_is_plus_one(a: int, p: int) -> bool:
    assert p > 2
    return pow(a % p, (p - 1) // 2, p) == 1


def make_state(P: int, Q: int) -> dict[str, int]:
    g = gcd(Q - P, Q + P)
    assert g in (1, 2)
    u = (Q - P) // g
    v = (Q + P) // g
    km, r = kernel_square_root(u)
    kp, s = kernel_square_root(v)
    xi = squarefree_kernel(P * Q)
    F = v * v - u * u
    assert F % xi == 0
    z = isqrt(F // xi)
    assert xi * z * z == F
    k = km * kp
    assert gcd(km, kp) == 1
    assert gcd(k, xi * z) == 1
    return {
        "P": P,
        "Q": Q,
        "g": g,
        "u": u,
        "v": v,
        "km": km,
        "kp": kp,
        "r": r,
        "s": s,
        "xi": xi,
        "z": z,
        "k": k,
    }


def primitive_parameters(H0: int, L0: int, W0: int) -> tuple[int, int]:
    assert H0 * H0 == L0 * L0 + W0 * W0
    assert gcd(gcd(H0, L0), W0) == 1
    assert H0 % 2 == 1
    odd_leg = L0 if L0 % 2 else W0
    even_leg = W0 if L0 % 2 else L0
    m2_num = H0 + odd_leg
    n2_num = H0 - odd_leg
    assert m2_num % 2 == 0 and n2_num % 2 == 0
    m = isqrt(m2_num // 2)
    n = isqrt(n2_num // 2)
    assert m * m == m2_num // 2
    assert n * n == n2_num // 2
    assert m > n > 0
    assert gcd(m, n) == 1
    assert (m - n) % 2 == 1
    assert m * m + n * n == H0
    assert m * m - n * n == odd_leg
    assert 2 * m * n == even_leg
    return m, n


def audit_pair(a: dict[str, int], b: dict[str, int], X: int) -> None:
    assert a["xi"] == b["xi"]
    assert a["k"] == b["k"]
    assert (a["km"], a["kp"]) != (b["km"], b["kp"])

    alpha = gcd(a["km"], b["km"])
    beta = a["km"] // alpha
    gamma = b["km"] // alpha
    delta = gcd(a["kp"], b["kp"])

    assert a["km"] == alpha * beta
    assert a["kp"] == gamma * delta
    assert b["km"] == alpha * gamma
    assert b["kp"] == beta * delta
    assert alpha * beta * gamma * delta == a["k"]

    cells = [alpha, beta, gamma, delta]
    for i, x in enumerate(cells):
        for y in cells[i + 1 :]:
            assert gcd(x, y) == 1

    K_switch = beta * gamma
    K_agree = alpha * delta

    U1, V1 = a["u"], a["v"]
    U2, V2 = b["u"], b["v"]
    H = V1 * V2 + U1 * U2
    L = V1 * U2 + U1 * V2
    W = a["xi"] * a["z"] * b["z"]

    assert H * H == L * L + W * W
    assert H % K_switch == 0
    assert L % K_agree == 0
    assert gcd(a["k"], W) == 1

    d = gcd(gcd(H, L), W)
    assert gcd(d, a["k"]) == 1
    H0, L0, W0 = H // d, L // d, W // d
    assert H0 * H0 == L0 * L0 + W0 * W0
    assert gcd(gcd(H0, L0), W0) == 1
    assert H0 % K_switch == 0
    assert L0 % K_agree == 0
    assert (H0 * L0) % a["k"] == 0

    xi0 = a["xi"] // gcd(a["xi"], d)
    assert W0 % xi0 == 0
    assert gcd(a["k"], xi0) == 1

    # Quantitative primitive-gcd inequalities used in the stage proof.
    assert d * d * a["k"] <= H * H
    assert H <= 5 * X * X
    assert (5 * X * X * xi0) ** 2 >= (a["xi"] ** 2) * a["k"]

    m, n = primitive_parameters(H0, L0, W0)
    assert (m * m + n * n) % K_switch == 0

    for ell in prime_divisors(K_switch):
        if ell == 2:
            continue
        assert ell % 4 == 1
        assert legendre_is_plus_one(a["xi"], ell)


def main() -> None:
    X = 160
    groups: dict[tuple[int, int], list[dict[str, int]]] = defaultdict(list)
    for Q in range(2, X + 1):
        for P in range(1, Q):
            if gcd(P, Q) != 1:
                continue
            st = make_state(P, Q)
            groups[(st["xi"], st["k"])].append(st)

    cross_pairs = 0
    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                audit_pair(a, b, X)
                cross_pairs += 1

    assert cross_pairs > 0

    gamma = Fraction(3, 4)
    kappa_old = Fraction(3, 4)
    kappa_endpoint = Fraction(1, 1)

    switch_old = kappa_old + gamma / 2 - 1
    switch_endpoint = kappa_endpoint + gamma / 2 - 1
    xi0_old = gamma + kappa_old / 2 - 1
    xi0_endpoint = gamma + kappa_endpoint / 2 - 1
    d_endpoint = 1 - kappa_endpoint / 2

    assert switch_old == Fraction(1, 8)
    assert switch_endpoint == Fraction(3, 8)
    assert xi0_old == Fraction(1, 8)
    assert xi0_endpoint == Fraction(1, 4)
    assert d_endpoint == Fraction(1, 2)

    print("Stage14-s7-19 audit: PASS")
    print(f"finite cross-split collision pairs checked: {cross_pairs}")
    print("critical K_switch exponent >= 1/8")
    print("critical xi_0 exponent >= 1/8")
    print("4cd endpoint K_switch exponent >= 3/8")
    print("4cd endpoint xi_0 exponent >= 1/4")
    print("4cd endpoint primitive gcd exponent <= 1/2")


if __name__ == "__main__":
    main()
