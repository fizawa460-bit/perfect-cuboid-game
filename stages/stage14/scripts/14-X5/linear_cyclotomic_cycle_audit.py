#!/usr/bin/env python3
"""Deterministic audit for Stage14-X5.

The asymptotic theorem is algebraic: merged 4cg common-core coprimality kills
both quadratic cyclotomic branches in merged 4cl.  Finite physical enumeration
is used only as a regression/diagnostic and to verify the exact linear quotient
identities on frozen packets.
"""

from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve()
CL_AUDIT = HERE.parents[1] / "14-4" / "cyclotomic_quartic_allocation_audit.py"
spec = spec_from_file_location("stage14_4cl_audit", CL_AUDIT)
assert spec is not None and spec.loader is not None
cl = module_from_spec(spec)
spec.loader.exec_module(cl)


def linear_partition(modulus: int, minus_factor: int, plus_factor: int) -> tuple[int, int]:
    m = cl.oddpart(modulus)
    mm = gcd(m, minus_factor)
    mp = gcd(m, plus_factor)
    assert mm * mp == m
    assert gcd(mm, mp) == 1
    return mm, mp


def audit_pair(a: dict[str, int], b: dict[str, int]):
    # Reuse every 4cl legality check first.
    _, xi_three, k_three = cl.audit_pair(a, b)

    cells, triple, _, hs = cl.ck.ch.residual_data(a, b)
    R, S, T, J, alpha, beta, gamma, delta = cells
    C, u, v = triple
    hk_plus, hk_minus, hx_plus, hx_minus = hs

    r = a["r"] * b["r"]
    s = a["s"] * b["s"]
    X = a["x"] * b["x"]
    Y = a["y"] * b["y"]

    A = alpha * r
    D = delta * s
    U0 = R * X
    V0 = J * Y
    assert D > A > 0 and V0 > U0 > 0

    # Identify the 4cg common-core factors inside the 4cl quartic variables.
    assert hk_plus == D * D + A * A
    assert hk_minus == D * D - A * A
    assert hx_plus == V0 * V0 + U0 * U0
    assert hx_minus == V0 * V0 - U0 * U0

    xi_ag = R * J
    k_ag = alpha * delta

    # The exact 4cg locks that eliminate the quadratic branches.
    assert gcd(hk_plus, cl.oddpart(xi_ag)) == 1
    assert gcd(hx_plus, cl.oddpart(k_ag)) == 1
    assert hk_minus % cl.oddpart(xi_ag) == 0
    assert hx_minus % cl.oddpart(k_ag) == 0

    # Therefore the 4cl i-branch components are identically one.
    assert xi_three[2] == 1
    assert k_three[2] == 1

    mxm, mxp = linear_partition(xi_ag, D - A, D + A)
    mkm, mkp = linear_partition(k_ag, V0 - U0, V0 + U0)
    assert (mxm, mxp, 1) == xi_three
    assert (mkm, mkp, 1) == k_three

    # Exact residual quotient factorization after common-core cancellation.
    qxm = cl.oddpart(D - A) // mxm
    qxp = cl.oddpart(D + A) // mxp
    qkm = cl.oddpart(V0 - U0) // mkm
    qkp = cl.oddpart(V0 + U0) // mkp
    assert qxm * qxp == cl.oddpart(u)
    assert qkm * qkp == cl.oddpart(v)

    # Two-way, not three-way, square-root dominant-modulus lower bounds.
    assert max(mxm, mxp) ** 2 >= cl.oddpart(xi_ag)
    assert max(mkm, mkp) ** 2 >= cl.oddpart(k_ag)

    xi_dom = 0 if mxm >= mxp else 1
    k_dom = 0 if mkm >= mkp else 1
    return xi_dom, k_dom, (qxm, qxp, qkm, qkp), (C, u, v)


def main() -> None:
    groups = cl.ck.ch.make_groups(420)
    checked = 0
    branch_types: set[tuple[int, int]] = set()
    max_quotient_product = 0

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                xi_dom, k_dom, qs, _ = audit_pair(a, b)
                branch_types.add((xi_dom, k_dom))
                max_quotient_product = max(max_quotient_product, qs[0] * qs[1] * qs[2] * qs[3])
                checked += 1

    assert checked == 37
    # All four linear-linear dominant sign types really occur in the frozen data.
    assert branch_types == {(0, 0), (0, 1), (1, 0), (1, 1)}

    # Current proved saturation edge imported from merged s7-25.
    theta = Fraction(5, 16)
    for phi in [Fraction(3, 16), Fraction(7, 32), Fraction(1, 4)]:
        xi_dom_exp = phi
        k_dom_exp = theta
        xi_quot_exp = theta - phi
        k_quot_exp = phi + Fraction(1, 8) - theta
        assert xi_quot_exp >= 0
        assert k_quot_exp >= 0
        assert xi_quot_exp + k_quot_exp == Fraction(1, 8)
        assert xi_dom_exp + k_dom_exp >= Fraction(1, 2)

    # Endpoint checks quoted in the result.
    phi_lo = Fraction(3, 16)
    phi_hi = Fraction(1, 4)
    assert theta - phi_lo == Fraction(1, 8)
    assert phi_lo + Fraction(1, 8) - theta == 0
    assert theta - phi_hi == Fraction(1, 16)
    assert phi_hi + Fraction(1, 8) - theta == Fraction(1, 16)
    assert theta + phi_hi == Fraction(9, 16)

    print("Stage14-X5 audit: PASS")
    print(f"dual-cross physical pairs checked: {checked}")
    print("nontrivial xi quadratic branch occurrences: 0")
    print("nontrivial k quadratic branch occurrences: 0")
    print("surviving dominant branch types: (-,-),(-,+),(+,-),(+,+)")
    print("linear quotient products: Q_xi^- Q_xi^+=oddpart(u), Q_k^- Q_k^+=oddpart(v)")
    print(f"finite max four-quotient product diagnostic: {max_quotient_product}")
    print("top-edge dominant xi modulus exponent: phi")
    print("top-edge dominant k modulus exponent: 5/16")
    print("top-edge dominant quotient-product exponent <= 1/8")
    print("four-sign reciprocal linear factor-cycle incidence: UNPROVED")


if __name__ == "__main__":
    main()
