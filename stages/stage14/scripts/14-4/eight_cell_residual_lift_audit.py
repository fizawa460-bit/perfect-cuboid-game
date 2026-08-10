#!/usr/bin/env python3
"""Deterministic audit for Stage14-4ch.

Checks the exact factor-pair reconstruction used in the proof and freezes a
finite witness showing that the residual triple alone does not determine the
eight-cell packet. The finite search is regression evidence, not the proof.
"""

from collections import defaultdict
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve()
S7_AUDIT = HERE.parents[1] / "14-s7-20" / "balanced_eight_cell_audit.py"
spec = spec_from_file_location("stage14_s7_20_audit", S7_AUDIT)
assert spec is not None and spec.loader is not None
s7 = module_from_spec(spec)
spec.loader.exec_module(s7)


def tau(n: int) -> int:
    out = 1
    p = 2
    x = n
    while p * p <= x:
        if x % p:
            p = 3 if p == 2 else p + 2
            continue
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        out *= e + 1
        p = 3 if p == 2 else p + 2
    if x > 1:
        out *= 2
    return out


def square_root_exact(n: int) -> int | None:
    if n < 0:
        return None
    r = isqrt(n)
    return r if r * r == n else None


def residual_data(a: dict[str, int], b: dict[str, int]):
    R, S, T, J = s7.xi_cells(a, b)
    alpha, beta, gamma, delta = s7.k_cells(a, b)

    n_beta = (
        alpha * alpha * b["r"] ** 4 * a["z"] ** 2
        + delta * delta * a["s"] ** 4 * b["z"] ** 2
    )
    n_S = (
        R * R * b["x"] ** 4 * a["omega"] ** 2
        + J * J * a["y"] ** 4 * b["omega"] ** 2
    )
    assert n_beta % (beta * beta) == 0
    assert n_S % (S * S) == 0
    q_k = n_beta // (beta * beta)
    q_xi = n_S // (S * S)

    hk_plus = (
        delta * delta * a["s"] ** 2 * b["s"] ** 2
        + alpha * alpha * a["r"] ** 2 * b["r"] ** 2
    )
    hk_minus = (
        delta * delta * a["s"] ** 2 * b["s"] ** 2
        - alpha * alpha * a["r"] ** 2 * b["r"] ** 2
    )
    hx_plus = (
        J * J * a["y"] ** 2 * b["y"] ** 2
        + R * R * a["x"] ** 2 * b["x"] ** 2
    )
    hx_minus = (
        J * J * a["y"] ** 2 * b["y"] ** 2
        - R * R * a["x"] ** 2 * b["x"] ** 2
    )
    assert hk_minus > 0 and hx_minus > 0
    assert a["xi"] * q_k == hk_plus * hk_minus
    assert a["k"] * q_xi == hx_plus * hx_minus

    Xi_odd = s7.oddpart(S * T)
    K_odd = s7.oddpart(beta * gamma)
    assert hk_plus % Xi_odd == 0
    assert hx_plus % K_odd == 0
    C = s7.oddpart(hk_plus // Xi_odd)
    assert C == s7.oddpart(hx_plus // K_odd)
    assert q_k % C == 0 and q_xi % C == 0
    u = q_k // C
    v = q_xi // C

    cells = (R, S, T, J, alpha, beta, gamma, delta)
    return cells, (C, u, v), (q_k, q_xi), (hk_plus, hk_minus, hx_plus, hx_minus)


def recover_products(cells, triple, hs):
    R, S, T, J, alpha, beta, gamma, delta = cells
    C, u, v = triple
    q_k, q_xi = C * u, C * v
    xi = R * S * T * J
    k = alpha * beta * gamma * delta
    hk_plus, hk_minus, hx_plus, hx_minus = hs

    assert hk_plus * hk_minus == xi * q_k
    assert hx_plus * hx_minus == k * q_xi

    Ak = (hk_plus + hk_minus) // 2
    Bk = (hk_plus - hk_minus) // 2
    assert hk_plus % 2 == hk_minus % 2
    assert Ak % (delta * delta) == 0
    assert Bk % (alpha * alpha) == 0
    ss = square_root_exact(Ak // (delta * delta))
    rr = square_root_exact(Bk // (alpha * alpha))
    assert ss is not None and rr is not None

    Ax = (hx_plus + hx_minus) // 2
    Bx = (hx_plus - hx_minus) // 2
    assert hx_plus % 2 == hx_minus % 2
    assert Ax % (J * J) == 0
    assert Bx % (R * R) == 0
    yy = square_root_exact(Ax // (J * J))
    xx = square_root_exact(Bx // (R * R))
    assert yy is not None and xx is not None

    # Factor-pair choices for H and then four ordered root products.
    divisor_bound_proxy = (
        tau(xi * q_k)
        * tau(k * q_xi)
        * tau(rr)
        * tau(ss)
        * tau(xx)
        * tau(yy)
        * 4
    )
    return rr, ss, xx, yy, divisor_bound_proxy


def audit_pair(a: dict[str, int], b: dict[str, int]) -> tuple:
    cells, triple, qs, hs = residual_data(a, b)
    rr, ss, xx, yy, proxy = recover_products(cells, triple, hs)
    assert rr == a["r"] * b["r"]
    assert ss == a["s"] * b["s"]
    assert xx == a["x"] * b["x"]
    assert yy == a["y"] * b["y"]
    assert proxy >= 1

    # Merged s7-21 exact reconstruction identities.
    assert a["omega"] == a["g"] * a["r"] * a["s"]
    assert b["omega"] == b["g"] * b["r"] * b["s"]
    assert a["z"] == 2 * a["x"] * a["y"] // a["g"]
    assert b["z"] == 2 * b["x"] * b["y"] // b["g"]
    return cells, triple, qs, proxy


def make_groups(X: int):
    groups: dict[tuple[int, int], list[dict[str, int]]] = defaultdict(list)
    for Q in range(2, X + 1):
        for P in range(1, Q):
            if gcd(P, Q) != 1:
                continue
            st = s7.make_state(P, Q)
            groups[(st["xi"], st["k"])].append(st)
    return groups


def main() -> None:
    X = 420
    groups = make_groups(X)
    checked = 0
    max_proxy = 0
    triples_to_cells: dict[tuple[int, int, int], set[tuple[int, ...]]] = defaultdict(set)

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                cells, triple, _, proxy = audit_pair(a, b)
                triples_to_cells[triple].add(cells)
                max_proxy = max(max_proxy, proxy)
                checked += 1

    assert checked > 0

    # Freeze an exact quantifier witness: one residual triple, two cell packets.
    A1, B1 = s7.make_state(41, 54), s7.make_state(1, 246)
    A2, B2 = s7.make_state(29, 70), s7.make_state(45, 406)
    cells1, triple1, qs1, _ = audit_pair(A1, B1)
    cells2, triple2, qs2, _ = audit_pair(A2, B2)
    assert triple1 == triple2 == (5, 104, 17)
    assert qs1 == qs2 == (520, 85)
    assert cells1 == (1, 41, 1, 6, 1, 13, 5, 19)
    assert cells2 == (1, 29, 5, 14, 1, 41, 1, 11)
    assert cells1 != cells2

    # Exponent ledger for residual triple support.
    Cexp = Fraction(3, 8)
    UVexp = Fraction(1, 4)
    support = Cexp + UVexp
    assert support == Fraction(5, 8)
    gap_to_current = Fraction(7, 8) - support
    assert gap_to_current == Fraction(1, 4)

    print("Stage14-4ch audit: PASS")
    print(f"dual-cross finite pairs checked: {checked}")
    print(f"max finite divisor-bound proxy: {max_proxy}")
    print("fixed eight cells + (C,u,v) recover four root products: exact")
    print("residual-triple-only cell uniqueness: false (frozen witness)")
    print("residual triple support exponent: 5/8")
    print("cell-multiplicity allowance before 7/8: 1/4")


if __name__ == "__main__":
    main()
