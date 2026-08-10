#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-20.

Checks the dual xi-split divisibility theorem, the odd-support identity for the
s7-19 primitive gcd, and the positive switched-cell square divisibilities on a
finite reduced-coordinate sample.  This is a regression audit, not proof by
search.
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


def oddpart(n: int) -> int:
    while n % 2 == 0:
        n //= 2
    return n


def make_state(P: int, Q: int) -> dict[str, int]:
    assert gcd(P, Q) == 1

    a, x = kernel_square_root(P)
    b, y = kernel_square_root(Q)
    xi = a * b
    assert xi == squarefree_kernel(P * Q)
    assert gcd(a, b) == 1

    g = gcd(Q - P, Q + P)
    assert g in (1, 2)
    u = (Q - P) // g
    v = (Q + P) // g
    km, r = kernel_square_root(u)
    kp, s = kernel_square_root(v)
    k = km * kp
    assert gcd(km, kp) == 1

    F = v * v - u * u
    z = isqrt(F // xi)
    assert F == xi * z * z
    assert gcd(k, xi * z) == 1

    omega = isqrt((Q * Q - P * P) // k)
    assert Q * Q - P * P == k * omega * omega
    assert gcd(xi, k * omega) == 1

    return {
        "P": P,
        "Q": Q,
        "a": a,
        "b": b,
        "x": x,
        "y": y,
        "xi": xi,
        "g": g,
        "u": u,
        "v": v,
        "km": km,
        "kp": kp,
        "r": r,
        "s": s,
        "k": k,
        "z": z,
        "omega": omega,
    }


def xi_cells(a: dict[str, int], b: dict[str, int]) -> tuple[int, int, int, int]:
    R = gcd(a["a"], b["a"])
    S = a["a"] // R
    T = b["a"] // R
    J = gcd(a["b"], b["b"])

    assert a["a"] == R * S
    assert a["b"] == T * J
    assert b["a"] == R * T
    assert b["b"] == S * J
    assert R * S * T * J == a["xi"] == b["xi"]

    cells = [R, S, T, J]
    for i, x in enumerate(cells):
        for y in cells[i + 1 :]:
            assert gcd(x, y) == 1
    return R, S, T, J


def k_cells(a: dict[str, int], b: dict[str, int]) -> tuple[int, int, int, int]:
    alpha = gcd(a["km"], b["km"])
    beta = a["km"] // alpha
    gamma = b["km"] // alpha
    delta = gcd(a["kp"], b["kp"])

    assert a["km"] == alpha * beta
    assert a["kp"] == gamma * delta
    assert b["km"] == alpha * gamma
    assert b["kp"] == beta * delta
    assert alpha * beta * gamma * delta == a["k"] == b["k"]

    cells = [alpha, beta, gamma, delta]
    for i, x in enumerate(cells):
        for y in cells[i + 1 :]:
            assert gcd(x, y) == 1
    return alpha, beta, gamma, delta


def audit_pair(a: dict[str, int], b: dict[str, int], X: int) -> tuple[bool, bool]:
    assert a["xi"] == b["xi"]
    assert a["k"] == b["k"]

    R, S, T, J = xi_cells(a, b)
    Xi_agree = R * J
    Xi_switch = S * T

    # Dual agreement divisibilities, eq. (3.3).
    dy = T * T * a["y"] ** 4 * b["omega"] ** 2 - S * S * b["y"] ** 4 * a["omega"] ** 2
    dx = S * S * a["x"] ** 4 * b["omega"] ** 2 - T * T * b["x"] ** 4 * a["omega"] ** 2
    assert dy % (R * R) == 0
    assert dx % (J * J) == 0

    # Every off-diagonal same-(xi,k) pair obeys the necessary agreement bound.
    assert Xi_agree * Xi_agree * a["k"] <= 2 * X ** 4

    # Positive switched-xi square divisibilities, eqs. (7.1)-(7.2).
    eS = R * R * b["x"] ** 4 * a["omega"] ** 2 + J * J * a["y"] ** 4 * b["omega"] ** 2
    eT = J * J * b["y"] ** 4 * a["omega"] ** 2 + R * R * a["x"] ** 4 * b["omega"] ** 2
    assert eS > 0 and eT > 0
    assert eS % (S * S) == 0
    assert eT % (T * T) == 0

    # s7-19 primitive gcd: odd xi-support in d is exactly the switched P/Q support.
    H = a["v"] * b["v"] + a["u"] * b["u"]
    L = a["v"] * b["u"] + a["u"] * b["v"]
    W = a["xi"] * a["z"] * b["z"]
    assert H * H == L * L + W * W
    d = gcd(gcd(H, L), W)
    assert oddpart(gcd(a["xi"], d)) == oddpart(Xi_switch)
    xi0 = a["xi"] // gcd(a["xi"], d)
    assert oddpart(xi0) == oddpart(Xi_agree)

    cross_k = (a["km"], a["kp"]) != (b["km"], b["kp"])
    if cross_k:
        alpha, beta, gamma, delta = k_cells(a, b)

        # Positive switched-k square divisibilities, eqs. (6.3)-(6.4).
        e_beta = alpha * alpha * b["r"] ** 4 * a["z"] ** 2 + delta * delta * a["s"] ** 4 * b["z"] ** 2
        e_gamma = delta * delta * b["s"] ** 4 * a["z"] ** 2 + alpha * alpha * a["r"] ** 4 * b["z"] ** 2
        assert e_beta > 0 and e_gamma > 0
        assert e_beta % (beta * beta) == 0
        assert e_gamma % (gamma * gamma) == 0

        # Agreement divisibilities inherited from s7-18.
        d_alpha = gamma * gamma * a["s"] ** 4 * b["z"] ** 2 - beta * beta * b["s"] ** 4 * a["z"] ** 2
        d_delta = beta * beta * a["r"] ** 4 * b["z"] ** 2 - gamma * gamma * b["r"] ** 4 * a["z"] ** 2
        assert d_alpha % (alpha * alpha) == 0
        assert d_delta % (delta * delta) == 0

    cross_xi = (a["a"], a["b"]) != (b["a"], b["b"])
    return cross_k, cross_xi


def main() -> None:
    X = 180
    groups: dict[tuple[int, int], list[dict[str, int]]] = defaultdict(list)

    for Q in range(2, X + 1):
        for P in range(1, Q):
            if gcd(P, Q) != 1:
                continue
            st = make_state(P, Q)
            groups[(st["xi"], st["k"])].append(st)

    pairs = 0
    cross_k_pairs = 0
    cross_xi_pairs = 0
    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                cross_k, cross_xi = audit_pair(states[i], states[j], X)
                pairs += 1
                cross_k_pairs += int(cross_k)
                cross_xi_pairs += int(cross_xi)

    assert pairs > 0
    assert cross_k_pairs > 0
    assert cross_xi_pairs > 0

    gamma = Fraction(3, 4)
    kappa_old = Fraction(3, 4)
    kappa_endpoint = Fraction(1, 1)

    xi_switch_old = gamma + kappa_old / 2 - 1
    xi_switch_endpoint = gamma + kappa_endpoint / 2 - 1
    assert xi_switch_old == Fraction(1, 8)
    assert xi_switch_endpoint == Fraction(1, 4)

    # Endpoint balanced windows.
    k_product_lo = Fraction(3, 8)
    k_product_hi = Fraction(5, 8)
    k_cell_lo = k_product_lo / 2
    k_cell_hi = k_product_hi / 2
    assert k_cell_lo == Fraction(3, 16)
    assert k_cell_hi == Fraction(5, 16)

    xi_product_lo = Fraction(1, 4)
    xi_product_hi = gamma - xi_product_lo
    xi_cell_lo = xi_product_lo / 2
    xi_cell_hi = xi_product_hi / 2
    assert xi_product_hi == Fraction(1, 2)
    assert xi_cell_lo == Fraction(1, 8)
    assert xi_cell_hi == Fraction(1, 4)

    print("Stage14-s7-20 audit: PASS")
    print(f"same-(xi,k) off-diagonal pairs checked: {pairs}")
    print(f"cross-k-split pairs checked: {cross_k_pairs}")
    print(f"cross-xi-split pairs checked: {cross_xi_pairs}")
    print("critical Xi_switch exponent >= 1/8")
    print("4cd endpoint Xi_switch exponent >= 1/4")
    print("4cd endpoint k cell exponents in [3/16,5/16]")
    print("4cd endpoint xi cell exponents in [1/8,1/4]")


if __name__ == "__main__":
    main()
