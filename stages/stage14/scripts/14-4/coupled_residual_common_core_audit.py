#!/usr/bin/env python3
"""Deterministic audit for Stage14-4cg.

Checks the pairwise residual-norm collapse and common-plus-core coupling on a
finite same-(xi,k) sample. This is a regression audit, not proof by search.
"""

from collections import defaultdict
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve()
S7_AUDIT = HERE.parents[1] / "14-s7-20" / "balanced_eight_cell_audit.py"
spec = spec_from_file_location("stage14_s7_20_audit", S7_AUDIT)
assert spec is not None and spec.loader is not None
s7 = module_from_spec(spec)
spec.loader.exec_module(s7)


def audit_pair(a: dict[str, int], b: dict[str, int]) -> None:
    assert a["xi"] == b["xi"]
    assert a["k"] == b["k"]

    R, S, T, J = s7.xi_cells(a, b)
    alpha, beta, gamma, delta = s7.k_cells(a, b)

    n_beta = (
        alpha * alpha * b["r"] ** 4 * a["z"] ** 2
        + delta * delta * a["s"] ** 4 * b["z"] ** 2
    )
    n_gamma = (
        delta * delta * b["s"] ** 4 * a["z"] ** 2
        + alpha * alpha * a["r"] ** 4 * b["z"] ** 2
    )
    n_S = (
        R * R * b["x"] ** 4 * a["omega"] ** 2
        + J * J * a["y"] ** 4 * b["omega"] ** 2
    )
    n_T = (
        J * J * b["y"] ** 4 * a["omega"] ** 2
        + R * R * a["x"] ** 4 * b["omega"] ** 2
    )

    assert n_beta % (beta * beta) == 0
    assert n_gamma % (gamma * gamma) == 0
    assert n_S % (S * S) == 0
    assert n_T % (T * T) == 0

    q_beta = n_beta // (beta * beta)
    q_gamma = n_gamma // (gamma * gamma)
    q_S = n_S // (S * S)
    q_T = n_T // (T * T)

    assert q_beta == q_gamma
    assert q_S == q_T
    q_k = q_beta
    q_xi = q_S

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

    assert hk_minus > 0
    assert hx_minus > 0
    assert a["xi"] * q_k == hk_plus * hk_minus
    assert a["k"] * q_xi == hx_plus * hx_minus

    K_switch = beta * gamma
    Xi_switch = S * T
    K_agree = alpha * delta
    Xi_agree = R * J

    assert (
        a["g"] * b["g"] * K_switch * hk_plus
        == 2 * Xi_switch * hx_plus
    )

    K_odd = s7.oddpart(K_switch)
    Xi_odd = s7.oddpart(Xi_switch)
    assert hk_plus % Xi_odd == 0
    assert hx_plus % K_odd == 0

    c_k = s7.oddpart(hk_plus // Xi_odd)
    c_xi = s7.oddpart(hx_plus // K_odd)
    assert c_k == c_xi
    C = c_k

    assert gcd(C, s7.oddpart(Xi_agree)) == 1
    assert gcd(C, s7.oddpart(K_agree)) == 1
    assert q_k % C == 0
    assert q_xi % C == 0


def main() -> None:
    X = 300
    groups: dict[tuple[int, int], list[dict[str, int]]] = defaultdict(list)

    for Q in range(2, X + 1):
        for P in range(1, Q):
            if gcd(P, Q) != 1:
                continue
            st = s7.make_state(P, Q)
            groups[(st["xi"], st["k"])].append(st)

    checked = 0
    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                cross_k = (a["km"], a["kp"]) != (b["km"], b["kp"])
                cross_xi = (a["a"], a["b"]) != (b["a"], b["b"])
                if not (cross_k and cross_xi):
                    continue
                audit_pair(a, b)
                checked += 1

    assert checked > 0

    theta_hi = Fraction(5, 16)
    phi_hi = Fraction(1, 4)
    common_core_max = 2 * theta_hi + 2 * phi_hi - Fraction(3, 4)
    assert common_core_max == Fraction(3, 8)

    theta = Fraction(1, 4)
    phi = Fraction(3, 16)
    u_exp = 2 * theta - 2 * phi
    v_exp = Fraction(1, 4) + 2 * phi - 2 * theta
    assert u_exp >= 0 and v_exp >= 0
    assert u_exp + v_exp == Fraction(1, 4)

    print("Stage14-4cg audit: PASS")
    print(f"cross-k/cross-xi same-(xi,k) pairs checked: {checked}")
    print("q_beta=q_gamma and q_S=q_T: exact")
    print("common odd plus-core survives in both residual norms: exact")
    print("endpoint common-core exponent <= 3/8")
    print("reduced residual product exponent <= 1/4")


if __name__ == "__main__":
    main()
