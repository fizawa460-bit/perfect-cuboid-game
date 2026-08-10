#!/usr/bin/env python3
"""Deterministic audit for Stage14-4ck.

Finite computation verifies the exact complementary cross identity, recovery of
both switched products from the four agreement cells, and the binary-quartic
normal form.  The finite fiber histogram is diagnostic only; no asymptotic
quartic-incidence estimate is inferred from it.
"""

from collections import defaultdict
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve()
CH_AUDIT = HERE.parent / "eight_cell_residual_lift_audit.py"
spec = spec_from_file_location("stage14_4ch_audit", CH_AUDIT)
assert spec is not None and spec.loader is not None
ch = module_from_spec(spec)
spec.loader.exec_module(ch)


def F(a: int, b: int) -> int:
    return a * b * (b - a) * (b + a)


def audit_pair(a: dict[str, int], b: dict[str, int]):
    cells, triple, qs, hs = ch.residual_data(a, b)
    R, S, T, J, alpha, beta, gamma, delta = cells
    qk, qxi = qs
    hk_plus, hk_minus, hx_plus, hx_minus = hs

    r = a["r"] * b["r"]
    s = a["s"] * b["s"]
    X = a["x"] * b["x"]
    Y = a["y"] * b["y"]
    G = a["g"] * b["g"]

    # Complementary minus-factor cross identity.
    lhs_minus = G * qk * R * J * hx_minus
    rhs_minus = 2 * qxi * alpha * delta * hk_minus
    assert lhs_minus == rhs_minus

    # Switched products are recovered from agreement cells.
    den_st = qk * R * J
    den_bg = qxi * alpha * delta
    assert (hk_plus * hk_minus) % den_st == 0
    assert (hx_plus * hx_minus) % den_bg == 0
    st = (hk_plus * hk_minus) // den_st
    bg = (hx_plus * hx_minus) // den_bg
    assert st == S * T
    assert bg == beta * gamma

    # Binary-quartic normal form.
    A = alpha * r
    D = delta * s
    U = R * X
    V = J * Y
    assert A > 0 and D > A
    assert U > 0 and V > U
    lhs_F = G * qk * r * s * F(U, V)
    rhs_F = 2 * qxi * X * Y * F(A, D)
    assert lhs_F == rhs_F

    key = (
        triple,
        (a["x"], a["y"], b["x"], b["y"]),
        (a["r"], b["r"], a["s"], b["s"], a["g"], b["g"]),
    )
    agreement = (alpha, delta, R, J)
    return key, agreement, (st, bg)


def main() -> None:
    groups = ch.make_groups(420)
    checked = 0
    key_to_agreement: dict[tuple, set[tuple[int, int, int, int]]] = defaultdict(set)
    max_st = 0
    max_bg = 0

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                key, agreement, switch_products = audit_pair(a, b)
                key_to_agreement[key].add(agreement)
                max_st = max(max_st, switch_products[0])
                max_bg = max(max_bg, switch_products[1])
                checked += 1

    assert checked > 0
    max_finite_fiber = max(len(v) for v in key_to_agreement.values())

    # Exact dyadic ledger imported from 4ci/s7-24.
    theta_values = [Fraction(3, 16), Fraction(4, 16), Fraction(5, 16)]
    phi_values = [Fraction(2, 16), Fraction(3, 16), Fraction(4, 16)]
    survivors = []
    for theta in theta_values:
        for phi in phi_values:
            if theta - phi < 0 or theta - phi > Fraction(1, 8):
                continue
            if theta + phi < Fraction(3, 8):
                continue
            exponent = 2 * (theta + phi) - Fraction(1, 4)
            survivors.append((exponent, theta, phi))

    max_exp = max(x[0] for x in survivors)
    max_blocks = [(t, p) for e, t, p in survivors if e == max_exp]
    assert max_exp == Fraction(7, 8)
    assert max_blocks == [(Fraction(5, 16), Fraction(1, 4))]

    # The quartic is exactly completely split.
    for a, b in [(1, 2), (2, 5), (3, 8), (5, 13)]:
        assert F(a, b) == a * b * (b - a) * (b + a)

    print("Stage14-4ck audit: PASS")
    print(f"dual-cross finite pairs checked: {checked}")
    print(f"finite fixed residual/root/small-data agreement fiber max: {max_finite_fiber}")
    print(f"largest recovered S*T in sample: {max_st}")
    print(f"largest recovered beta*gamma in sample: {max_bg}")
    print("complementary minus-factor identity: exact")
    print("switched products from agreement cells: exact")
    print("binary quartic F(a,b)=ab(b-a)(b+a): exact")
    print("unique conditional 7/8 corner: theta=5/16, phi=1/4")
    print("asymptotic quartic agreement incidence: UNPROVED")


if __name__ == "__main__":
    main()
