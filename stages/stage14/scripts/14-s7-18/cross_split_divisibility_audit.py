#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-18."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import gcd, isqrt


def squarefree_kernel(n: int) -> int:
    n = abs(n)
    out = 1
    d = 2
    while d * d <= n:
        parity = 0
        while n % d == 0:
            n //= d
            parity ^= 1
        if parity:
            out *= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out *= n
    return out


def state(P: int, Q: int) -> dict[str, int]:
    assert 0 < P < Q and gcd(P, Q) == 1
    g = gcd(Q - P, Q + P)
    assert g in (1, 2)
    u = (Q - P) // g
    v = (Q + P) // g
    assert gcd(u, v) == 1

    km = squarefree_kernel(u)
    kp = squarefree_kernel(v)
    rr = u // km
    ss = v // kp
    r = isqrt(rr)
    s = isqrt(ss)
    assert r * r == rr and s * s == ss
    assert gcd(km, kp) == 1
    assert gcd(r, s) == 1

    k = km * kp
    xi = squarefree_kernel(P * Q)
    ww = (P * Q) // xi
    w = isqrt(ww)
    assert w * w == ww
    assert (2 * w) % g == 0
    z = 2 * w // g

    F = kp * kp * s**4 - km * km * r**4
    assert F == 4 * P * Q // (g * g)
    assert F == xi * z * z
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
        "k": k,
        "xi": xi,
        "z": z,
    }


def four_cells(a: dict[str, int], b: dict[str, int]) -> tuple[int, int, int, int]:
    assert a["k"] == b["k"]
    alpha = gcd(a["km"], b["km"])
    beta = gcd(a["km"], b["kp"])
    gamma = gcd(a["kp"], b["km"])
    delta = gcd(a["kp"], b["kp"])

    assert alpha * beta == a["km"]
    assert gamma * delta == a["kp"]
    assert alpha * gamma == b["km"]
    assert beta * delta == b["kp"]
    assert alpha * beta * gamma * delta == a["k"]

    vals = (alpha, beta, gamma, delta)
    for i in range(4):
        for j in range(i + 1, 4):
            assert gcd(vals[i], vals[j]) == 1
    return vals


def audit_finite_reduced_coordinates(X: int = 100) -> tuple[int, int]:
    states: list[dict[str, int]] = []
    for Q in range(2, X + 1):
        for P in range(1, Q):
            if gcd(P, Q) == 1:
                states.append(state(P, Q))

    groups: defaultdict[tuple[int, int], list[dict[str, int]]] = defaultdict(list)
    for st in states:
        groups[(st["xi"], st["k"])].append(st)

    collision_pairs = 0
    cross_split_pairs = 0
    for bucket in groups.values():
        for i in range(len(bucket)):
            for j in range(i + 1, len(bucket)):
                a = bucket[i]
                b = bucket[j]
                collision_pairs += 1
                alpha, beta, gamma, delta = four_cells(a, b)

                lhs_bracket = gamma**2 * a["s"]**4 * b["z"]**2 - beta**2 * b["s"]**4 * a["z"]**2
                rhs_bracket = beta**2 * a["r"]**4 * b["z"]**2 - gamma**2 * b["r"]**4 * a["z"]**2
                assert lhs_bracket % (alpha * alpha) == 0
                assert rhs_bracket % (delta * delta) == 0

                agree = alpha * delta
                switch = beta * gamma
                assert agree * switch == a["k"]

                # The proved necessary condition for every off-diagonal collision.
                assert agree * agree * a["xi"] <= 32 * X**4

                if switch > 1:
                    cross_split_pairs += 1

                # Same-split collisions can only occur below the fixed-split injectivity threshold.
                if a["km"] == b["km"] and a["kp"] == b["kp"]:
                    assert a["k"] * a["k"] * a["xi"] <= 32 * X**4

    assert collision_pairs > 0  # guard against a vacuous finite regression
    assert cross_split_pairs > 0
    return collision_pairs, cross_split_pairs


def audit_exponent_ledger() -> None:
    gamma = Fraction(3, 4)
    kappa = Fraction(3, 4)
    fixed_split_margin = 2 * kappa + gamma - 2
    switch_lower = kappa + gamma / 2 - 1
    endpoint_switch_lower = 1 + gamma / 2 - 1

    assert fixed_split_margin == Fraction(1, 4)
    assert switch_lower == Fraction(1, 8)
    assert endpoint_switch_lower == Fraction(3, 8)


def main() -> None:
    collisions, cross = audit_finite_reduced_coordinates()
    audit_exponent_ledger()
    print(f"finite same-(xi,k) collision pairs: {collisions}")
    print(f"finite cross-split collision pairs: {cross}")
    print("fixed-split injectivity / cross-split divisibility audit: PASS")
    print("critical exponent margins 1/4, 1/8, 3/8: PASS")


if __name__ == "__main__":
    main()
