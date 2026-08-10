#!/usr/bin/env python3
"""Deterministic audit for Stage14-X5.

Verifies the exact coupled difference-square equations and their elimination to a
fixed-coefficient bidegree-(2,2) ratio curve on the frozen physical dual-cross
family.  Finite fibers are diagnostics only; no asymptotic rational-point bound
is inferred.
"""

from collections import defaultdict
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve()
CM_AUDIT = HERE.parents[1] / "14-4" / "signed_linear_reciprocal_audit.py"
spec = spec_from_file_location("stage14_4cm_audit", CM_AUDIT)
assert spec is not None and spec.loader is not None
cm = module_from_spec(spec)
spec.loader.exec_module(cm)


def audit_pair(a: dict[str, int], b: dict[str, int]):
    # First run every merged 4cm legality/reduction assertion.
    cm.audit_pair(a, b)

    cells, triple, _, hs = cm.ch.residual_data(a, b)
    R, S, T, J, alpha, beta, gamma, delta = cells
    C, u_res, v_res = triple
    _, hk_minus, _, hx_minus = hs

    r = a["r"] * b["r"]
    s = a["s"] * b["s"]
    X = a["x"] * b["x"]
    Y = a["y"] * b["y"]

    A = alpha * r
    D = delta * s
    U = R * X
    V = J * Y
    assert D > A > 0 and V > U > 0
    assert hk_minus == D * D - A * A
    assert hx_minus == V * V - U * U

    RJ_o = cm.oddpart(R * J)
    N_o = cm.oddpart(alpha * delta)

    m_minus = gcd(RJ_o, D - A)
    m_plus = gcd(RJ_o, D + A)
    n_minus = gcd(N_o, V - U)
    n_plus = gcd(N_o, V + U)
    assert m_minus * m_plus == RJ_o
    assert n_minus * n_plus == N_o
    assert gcd(m_minus, m_plus) == 1
    assert gcd(n_minus, n_plus) == 1

    # Full integral residual/2-primary quotients.
    assert (D - A) % m_minus == 0
    assert (D + A) % m_plus == 0
    assert (V - U) % n_minus == 0
    assert (V + U) % n_plus == 0
    a_minus = (D - A) // m_minus
    a_plus = (D + A) // m_plus
    b_minus = (V - U) // n_minus
    b_plus = (V + U) // n_plus

    epsilon_k = (alpha * delta) // N_o
    epsilon_xi = (R * J) // RJ_o
    assert epsilon_k & (epsilon_k - 1) == 0
    assert epsilon_xi & (epsilon_xi - 1) == 0

    c = 4 * epsilon_k * r * s
    d = 4 * epsilon_xi * X * Y

    lhs1 = (a_plus * m_plus) ** 2 - (a_minus * m_minus) ** 2
    rhs1 = c * n_minus * n_plus
    lhs2 = (b_plus * n_plus) ** 2 - (b_minus * n_minus) ** 2
    rhs2 = d * m_minus * m_plus
    assert lhs1 == rhs1
    assert lhs2 == rhs2

    # Exact rational ratio elimination of the two absolute scales.
    x = Fraction(m_plus, m_minus)
    y = Fraction(n_plus, n_minus)
    assert x.numerator == m_plus and x.denominator == m_minus
    assert y.numerator == n_plus and y.denominator == n_minus

    left_ratio = (a_plus * a_plus * x * x - a_minus * a_minus)
    right_ratio = (b_plus * b_plus * y * y - b_minus * b_minus)
    kappa = c * d
    assert left_ratio * right_ratio == kappa * x * y

    model = (a_minus, a_plus, b_minus, b_plus, c, d)
    ratio = (x, y)
    signs = (
        "-" if m_minus >= m_plus else "+",
        "-" if n_minus >= n_plus else "+",
    )
    return model, ratio, signs, (C, u_res, v_res)


def main() -> None:
    groups = cm.ch.make_groups(420)
    checked = 0
    models: dict[tuple, set[tuple[Fraction, Fraction]]] = defaultdict(set)
    sign_types: set[tuple[str, str]] = set()

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                model, ratio, signs, _ = audit_pair(a, b)
                models[model].add(ratio)
                sign_types.add(signs)
                checked += 1

    assert checked == 37
    assert sign_types == {("-", "-"), ("-", "+"), ("+", "-"), ("+", "+")}
    max_model_ratio_fiber = max(len(v) for v in models.values())

    # The compactified equation has bidegree (2,2), hence arithmetic genus 1.
    bidegree = (2, 2)
    arithmetic_genus = (bidegree[0] - 1) * (bidegree[1] - 1)
    assert arithmetic_genus == 1

    print("Stage14-X5 audit: PASS")
    print(f"dual-cross physical pairs checked: {checked}")
    print("coupled reciprocal difference-square equations: exact")
    print("ratio elimination: exact Fraction identity")
    print("surviving sign types: (-,-),(-,+),(+,-),(+,+)")
    print("ratio curve bidegree: (2,2)")
    print("ratio curve arithmetic genus: 1")
    print(f"finite fixed-coefficient-model max ratio fiber: {max_model_ratio_fiber}")
    print("uniform nonsingularity: UNPROVED")
    print("physical height/lift transfer: UNPROVED")
    print("charged-once ratio-biquadratic incidence: UNPROVED")


if __name__ == "__main__":
    main()
