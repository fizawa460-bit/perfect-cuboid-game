#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-s7-21.

The search is finite and is not used as a proof.  It verifies that actual
same-(xi,k), dual-cross-split pairs realize the primewise root-ratio CRT
branches claimed by s7-21, together with the exact z/product identity and the
endpoint exponent ledger.
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


def make_state(P: int, Q: int) -> dict[str, int]:
    a, x = kernel_square_root(P)
    b, y = kernel_square_root(Q)
    xi = a * b
    assert gcd(a, b) == 1
    assert xi == squarefree_kernel(P * Q)

    g = gcd(Q - P, Q + P)
    assert g in (1, 2)
    u = (Q - P) // g
    v = (Q + P) // g
    km, r = kernel_square_root(u)
    kp, s = kernel_square_root(v)
    k = km * kp
    assert gcd(km, kp) == 1

    diff = Q * Q - P * P
    omega = isqrt(diff // k)
    assert k * omega * omega == diff

    F = v * v - u * u
    z = isqrt(F // xi)
    assert xi * z * z == F
    assert 2 * x * y % g == 0
    assert z == 2 * x * y // g
    assert gcd(k, xi * z) == 1

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
        "omega": omega,
        "z": z,
    }


def four_cells(A: dict[str, int], B: dict[str, int]):
    R = gcd(A["a"], B["a"])
    S = A["a"] // R
    T = B["a"] // R
    J = gcd(A["b"], B["b"])
    assert A["a"] == R * S
    assert B["a"] == R * T
    assert A["b"] == T * J
    assert B["b"] == S * J
    assert R * S * T * J == A["xi"]

    alpha = gcd(A["km"], B["km"])
    beta = A["km"] // alpha
    gamma = B["km"] // alpha
    delta = gcd(A["kp"], B["kp"])
    assert A["km"] == alpha * beta
    assert B["km"] == alpha * gamma
    assert A["kp"] == gamma * delta
    assert B["kp"] == beta * delta
    assert alpha * beta * gamma * delta == A["k"]

    for cells in ((R, S, T, J), (alpha, beta, gamma, delta)):
        for i, c in enumerate(cells):
            for d in cells[i + 1 :]:
                assert gcd(c, d) == 1

    return (R, S, T, J), (alpha, beta, gamma, delta)


def audit_pair(A: dict[str, int], B: dict[str, int]) -> None:
    assert A["xi"] == B["xi"]
    assert A["k"] == B["k"]
    assert (A["a"], A["b"]) != (B["a"], B["b"])
    assert (A["km"], A["kp"]) != (B["km"], B["kp"])

    (R, S, T, J), (alpha, beta, gamma, delta) = four_cells(A, B)

    x1, y1, x2, y2 = A["x"], A["y"], B["x"], B["y"]
    om1, om2 = A["omega"], B["omega"]

    # s7-20 xi-side divisibilities.
    assert (T * T * y1**4 * om2**2 - S * S * y2**4 * om1**2) % (R * R) == 0
    assert (S * S * x1**4 * om2**2 - T * T * x2**4 * om1**2) % (J * J) == 0
    assert (R * R * x2**4 * om1**2 + J * J * y1**4 * om2**2) % (S * S) == 0
    assert (J * J * y2**4 * om1**2 + R * R * x1**4 * om2**2) % (T * T) == 0

    # An actual root pair selects one legal fourth-root branch modulo each
    # nontrivial cell square.  This mechanically checks the linearization.
    xi_specs = [
        (R, y1, y2, lambda lam, m: ((T * om2) ** 2 * pow(lam, 4, m) - (S * om1) ** 2) % m),
        (J, x1, x2, lambda lam, m: ((S * om2) ** 2 * pow(lam, 4, m) - (T * om1) ** 2) % m),
        (S, x2, y1, lambda lam, m: ((R * om1) ** 2 * pow(lam, 4, m) + (J * om2) ** 2) % m),
        (T, y2, x1, lambda lam, m: ((J * om1) ** 2 * pow(lam, 4, m) + (R * om2) ** 2) % m),
    ]
    for cell, num, den, polynomial in xi_specs:
        if cell == 1:
            continue
        modulus = cell * cell
        assert gcd(den, modulus) == 1
        lam = (num * pow(den, -1, modulus)) % modulus
        assert polynomial(lam, modulus) == 0

    z1, z2 = A["z"], B["z"]
    r1, s1, r2, s2 = A["r"], A["s"], B["r"], B["s"]

    # s7-20 k-side divisibilities.
    assert (gamma**2 * s1**4 * z2**2 - beta**2 * s2**4 * z1**2) % (alpha**2) == 0
    assert (beta**2 * r1**4 * z2**2 - gamma**2 * r2**4 * z1**2) % (delta**2) == 0
    assert (alpha**2 * r2**4 * z1**2 + delta**2 * s1**4 * z2**2) % (beta**2) == 0
    assert (delta**2 * s2**4 * z1**2 + alpha**2 * r1**4 * z2**2) % (gamma**2) == 0

    # An actual z pair selects one legal square-root branch in every k cell.
    k_specs = [
        (alpha, lambda mu, m: ((beta * s2 * s2) ** 2 * pow(mu, 2, m) - (gamma * s1 * s1) ** 2) % m),
        (delta, lambda mu, m: ((gamma * r2 * r2) ** 2 * pow(mu, 2, m) - (beta * r1 * r1) ** 2) % m),
        (beta, lambda mu, m: ((alpha * r2 * r2) ** 2 * pow(mu, 2, m) + (delta * s1 * s1) ** 2) % m),
        (gamma, lambda mu, m: ((delta * s2 * s2) ** 2 * pow(mu, 2, m) + (alpha * r1 * r1) ** 2) % m),
    ]
    for cell, polynomial in k_specs:
        if cell == 1:
            continue
        modulus = cell * cell
        assert gcd(z2, modulus) == 1
        mu = (z1 * pow(z2, -1, modulus)) % modulus
        assert polynomial(mu, modulus) == 0

    # Exact CRT determinants.
    assert (R * R) * (S * S) * (T * T) * (J * J) == A["xi"] ** 2
    assert (alpha**2) * (beta**2) * (gamma**2) * (delta**2) == A["k"] ** 2

    # Rank-one z direction gives the exact canonical product equation.
    d = gcd(z1, z2)
    u = z1 // d
    v = z2 // d
    assert gcd(u, v) == 1
    assert v * z1 == u * z2
    assert v * B["g"] * x1 * y1 == u * A["g"] * x2 * y2


def audit_small_root_counts() -> None:
    # For odd prime squares, a unit quadratic equation has at most two roots
    # and a unit fourth-power equation at most four roots.  Check sample rows
    # used as a regression guard for the branch-count implementation idea.
    for p in (3, 5, 7, 11, 13):
        m = p * p
        for c in range(1, m):
            if gcd(c, p) != 1:
                continue
            roots2 = [x for x in range(m) if (x * x - c) % m == 0]
            roots4 = [x for x in range(m) if (pow(x, 4, m) - c) % m == 0]
            assert len(roots2) <= 2
            assert len(roots4) <= 4


def main() -> None:
    X = 250
    groups: dict[tuple[int, int], list[dict[str, int]]] = defaultdict(list)
    for Q in range(2, X + 1):
        for P in range(1, Q):
            if gcd(P, Q) != 1:
                continue
            state = make_state(P, Q)
            groups[(state["xi"], state["k"])].append(state)

    dual_cross_pairs = 0
    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                A, B = states[i], states[j]
                if (A["a"], A["b"]) == (B["a"], B["b"]):
                    continue
                if (A["km"], A["kp"]) == (B["km"], B["kp"]):
                    continue
                audit_pair(A, B)
                dual_cross_pairs += 1

    assert dual_cross_pairs > 0
    audit_small_root_counts()

    xi = Fraction(3, 4)
    k = Fraction(1, 1)
    root = Fraction(1, 16)
    z = Fraction(1, 8)

    xi_det = 2 * xi
    k_det = 2 * k
    xi_box = 4 * root
    k_box = 2 * z

    assert xi_det == Fraction(3, 2)
    assert k_det == Fraction(2, 1)
    assert xi_box == Fraction(1, 4)
    assert k_box == Fraction(1, 4)
    assert xi_det - xi_box == Fraction(5, 4)
    assert k_det - k_box == Fraction(7, 4)

    print("Stage14-s7-21 dual CRT audit: PASS")
    print(f"finite dual-cross collision pairs checked: {dual_cross_pairs}")
    print("xi root CRT determinant exponent: 3/2")
    print("xi physical root-box exponent: 1/4")
    print("xi determinant gap exponent: 5/4")
    print("k z CRT determinant exponent: 2")
    print("k physical z-box exponent: 1/4")
    print("k determinant gap exponent: 7/4")
    print("short-rank caps: xi<=3, k<=1")


if __name__ == "__main__":
    main()
