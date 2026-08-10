#!/usr/bin/env python3
"""Deterministic audit for Stage14-4cm.

Checks the complementary odd-part identities, elimination of both quadratic
cyclotomic branches, the full two-way signed allocation of agreement support,
and the top-theta quotient exponent ledger.  Finite fiber histograms are
reported as diagnostics only and are not promoted to asymptotic theorems.
"""

from collections import defaultdict
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve()
CH_AUDIT = HERE.parent / "eight_cell_residual_lift_audit.py"
spec = spec_from_file_location("stage14_4ch_audit", CH_AUDIT)
assert spec is not None and spec.loader is not None
ch = module_from_spec(spec)
spec.loader.exec_module(ch)


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def audit_pair(a: dict[str, int], b: dict[str, int]):
    cells, triple, _, hs = ch.residual_data(a, b)
    R, S, T, J, alpha, beta, gamma, delta = cells
    _, u_res, v_res = triple
    _, hk_minus, _, hx_minus = hs

    r = a["r"] * b["r"]
    s = a["s"] * b["s"]
    X = a["x"] * b["x"]
    Y = a["y"] * b["y"]

    A = alpha * r
    D = delta * s
    U = R * X
    V = J * Y

    assert D > A > 0
    assert V > U > 0
    assert hk_minus == D * D - A * A
    assert hx_minus == V * V - U * U

    RJ_o = oddpart(R * J)
    N_o = oddpart(alpha * delta)

    # New exact complementary odd-part identities.
    assert oddpart(hk_minus) == RJ_o * oddpart(u_res)
    assert oddpart(hx_minus) == N_o * oddpart(v_res)

    # The agreement support lies completely in the two linear factors.
    xi_minus = gcd(RJ_o, D - A)
    xi_plus = gcd(RJ_o, D + A)
    xi_quad = gcd(RJ_o, D * D + A * A)
    assert xi_quad == 1
    assert gcd(xi_minus, xi_plus) == 1
    assert xi_minus * xi_plus == RJ_o

    k_minus = gcd(N_o, V - U)
    k_plus = gcd(N_o, V + U)
    k_quad = gcd(N_o, V * V + U * U)
    assert k_quad == 1
    assert gcd(k_minus, k_plus) == 1
    assert k_minus * k_plus == N_o

    # Choose a dominant signed branch on each side.
    xi_sign, xi_dom, xi_factor = (
        ("-", xi_minus, D - A)
        if xi_minus >= xi_plus
        else ("+", xi_plus, D + A)
    )
    k_sign, k_dom, k_factor = (
        ("-", k_minus, V - U)
        if k_minus >= k_plus
        else ("+", k_plus, V + U)
    )

    assert xi_factor % xi_dom == 0
    assert k_factor % k_dom == 0
    t_xi = xi_factor // xi_dom
    t_k = k_factor // k_dom
    assert t_xi >= 1 and t_k >= 1

    switch_product = S * T
    key = (triple, xi_sign, k_sign, t_xi, t_k)
    return key, switch_product, (xi_dom, k_dom), (xi_quad, k_quad)


def main() -> None:
    groups = ch.make_groups(420)
    checked = 0
    key_to_switch: dict[tuple, set[int]] = defaultdict(set)
    max_finite_quotient_fiber = 0
    min_xi_dom = None
    min_k_dom = None

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                key, switch_product, doms, quads = audit_pair(a, b)
                assert quads == (1, 1)
                key_to_switch[key].add(switch_product)
                min_xi_dom = doms[0] if min_xi_dom is None else min(min_xi_dom, doms[0])
                min_k_dom = doms[1] if min_k_dom is None else min(min_k_dom, doms[1])
                checked += 1

    assert checked > 0
    max_finite_quotient_fiber = max(len(v) for v in key_to_switch.values())

    # Exact top-theta ledger imported from merged s7-25.
    theta = Fraction(5, 16)
    phis = [Fraction(3, 16), Fraction(13, 64), Fraction(7, 32), Fraction(15, 64), Fraction(1, 4)]
    for phi in phis:
        xi_dom_exp = phi
        k_dom_exp = theta
        xi_q_exp = theta - phi
        k_q_exp = phi + Fraction(1, 8) - theta
        assert xi_dom_exp >= Fraction(3, 16)
        assert k_dom_exp == Fraction(5, 16)
        assert xi_q_exp >= 0
        assert k_q_exp >= 0
        assert xi_q_exp + k_q_exp == Fraction(1, 8)

    assert theta - Fraction(3, 16) == Fraction(1, 8)
    assert Fraction(3, 16) + Fraction(1, 8) - theta == 0
    assert theta - Fraction(1, 4) == Fraction(1, 16)
    assert Fraction(1, 4) + Fraction(1, 8) - theta == Fraction(1, 16)

    print("Stage14-4cm audit: PASS")
    print(f"dual-cross finite pairs checked: {checked}")
    print("complementary minus odd-part identities: exact")
    print("xi quadratic cyclotomic branch finite hits: 0")
    print("k quadratic cyclotomic branch finite hits: 0")
    print("dominant branch types remaining: 4 signed linear-linear types")
    print("top-theta xi dominant modulus exponent: phi")
    print("top-theta k dominant modulus exponent: 5/16")
    print("signed quotient-pair support exponent: 1/8")
    print(f"finite residual/sign/quotient -> switch-product max fiber: {max_finite_quotient_fiber}")
    print(f"smallest finite xi dominant modulus: {min_xi_dom}")
    print(f"smallest finite k dominant modulus: {min_k_dom}")
    print("asymptotic signed-quotient switch-product fiber theorem: UNPROVED")


if __name__ == "__main__":
    main()
