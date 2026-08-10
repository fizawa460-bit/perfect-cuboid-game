#!/usr/bin/env python3
"""Deterministic audit for Stage14-4cq.

The proof boundary is in 14-4cq/result.md.  This script checks on the frozen
physical packet generator that the two common-core plus hosts admit the stated
gcd-square peel, that the surviving good common core sees two Cayley roots of
-1, and that the reciprocal Edwards equation forces the Cayley coefficient
difference-of-squares divisibility.  It also freezes the exponent ledger that
collapses the phi=1/4 saturation face to theta=phi=1/4.
"""

from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve()
SCRIPTS = HERE.parents[1]
ROOT = HERE.parents[4]


def load_module(name: str, path: Path):
    spec = spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cn = load_module(
    "stage14_4cn_for_4cq",
    SCRIPTS / "14-4" / "reciprocal_edwards_reduction_audit.py",
)
ch = cn.ch
oddpart = cn.oddpart


def divide_exact(a: int, b: int) -> int:
    assert b > 0 and a % b == 0
    return a // b


def audit_pair(a_state: dict[str, int], b_state: dict[str, int]):
    # Keep the complete 4cn physical regression first.
    cn.audit_pair(a_state, b_state)

    cells, triple, _, _ = ch.residual_data(a_state, b_state)
    R, S, T, J, alpha, beta, gamma, delta = cells
    C = triple[0]

    r = a_state["r"] * b_state["r"]
    s = a_state["s"] * b_state["s"]
    X = a_state["x"] * b_state["x"]
    Y = a_state["y"] * b_state["y"]

    A = alpha * r
    D = delta * s
    P = R * X
    Q = J * Y
    assert D > A > 0 and Q > P > 0

    # The common core divides both positive plus hosts.
    assert (D * D + A * A) % C == 0
    assert (Q * Q + P * P) % C == 0

    # Agreement allocation and full signed quotient coefficients.
    X_ag = R * J
    K_ag = alpha * delta
    lx_m = gcd(oddpart(X_ag), D - A)
    lx_p = gcd(oddpart(X_ag), D + A)
    lk_m = gcd(oddpart(K_ag), Q - P)
    lk_p = gcd(oddpart(K_ag), Q + P)

    assert lx_m * lx_p == oddpart(X_ag)
    assert lk_m * lk_p == oddpart(K_ag)
    assert gcd(lx_m, lx_p) == 1
    assert gcd(lk_m, lk_p) == 1

    bq = divide_exact(D - A, lx_m)
    aq = divide_exact(D + A, lx_p)
    dq = divide_exact(Q - P, lk_m)
    cq = divide_exact(Q + P, lk_p)

    eps_x = X_ag // oddpart(X_ag)
    eps_k = K_ag // oddpart(K_ag)
    assert eps_x in (1, 2)
    assert eps_k in (1, 2)

    # New exact coprimality used by 4cq.
    assert gcd(C, oddpart(K_ag)) == 1

    # Sequential gcd-square peel on the two host coordinate pairs.
    g_A = gcd(A, D)
    g_P = gcd(P, Q)
    assert (r * s) % g_A == 0
    assert (X * Y) % g_P == 0

    A0, D0 = A // g_A, D // g_A
    P0, Q0 = P // g_P, Q // g_P
    assert gcd(A0, D0) == 1
    assert gcd(P0, Q0) == 1

    peel_A = gcd(C, g_A * g_A)
    C1 = C // peel_A
    peel_P = gcd(C1, g_P * g_P)
    Cstar = C1 // peel_P
    Cbad = C // Cstar

    assert Cbad > 0
    assert ((r * s * X * Y) ** 2) % Cbad == 0

    assert (D0 * D0 + A0 * A0) % Cstar == 0
    assert (Q0 * Q0 + P0 * P0) % Cstar == 0

    if Cstar > 1:
        assert gcd(Cstar, A0 * D0 * P0 * Q0) == 1
        den_x = D0 - A0
        den_y = Q0 - P0
        assert gcd(Cstar, den_x) == 1
        assert gcd(Cstar, den_y) == 1

        x = ((D0 + A0) * pow(den_x, -1, Cstar)) % Cstar
        y = ((Q0 + P0) * pow(den_y, -1, Cstar)) % Cstar
        assert (x * x + 1) % Cstar == 0
        assert (y * y + 1) % Cstar == 0

        lam_num = 16 * r * s * X * Y * eps_x * eps_k
        lam_den = aq * bq * cq * dq
        assert gcd(lam_den, Cstar) == 1
        lam_mod = (lam_num * pow(lam_den, -1, Cstar)) % Cstar
        assert (lam_mod * x * y - 4) % Cstar == 0
        assert (lam_mod * lam_mod - 16) % Cstar == 0

        cayley_scale = 4 * r * s * X * Y * eps_x * eps_k
        quotient_scale = aq * bq * cq * dq
        cayley_delta = cayley_scale * cayley_scale - quotient_scale * quotient_scale
        assert cayley_delta % Cstar == 0

    singular = (
        4 * r * s * X * Y * eps_x * eps_k
        == aq * bq * cq * dq
    )
    return C, Cstar, Cbad, singular


def exponent_ledger_audit() -> None:
    # s7-29 block exponent.
    theta = Fraction(5, 16)
    phi = Fraction(1, 4)
    old = 2 * phi + Fraction(1, 4)
    assert old == Fraction(3, 4)

    # On phi=1/4, the exact size identity is c=2theta-1/4.
    c = 2 * theta - Fraction(1, 4)
    dual = Fraction(1, 2) + 2 * phi - c
    assert c == Fraction(3, 8)
    assert dual == Fraction(5, 8)

    # The former theta=5/16 corner is therefore strictly saved.
    assert old - dual == Fraction(1, 8)

    # At the symmetric quarter-quarter corner the two ledgers meet at 3/4.
    theta = Fraction(1, 4)
    phi = Fraction(1, 4)
    c = 2 * theta - Fraction(1, 4)
    old = 2 * phi + Fraction(1, 4)
    dual = Fraction(1, 2) + 2 * phi - c
    assert c == Fraction(1, 4)
    assert old == dual == Fraction(3, 4)

    # General quarter-phi identity: dual = 5/4 - 2theta.
    for num in range(4, 6):
        theta = Fraction(num, 16)
        c = 2 * theta - Fraction(1, 4)
        dual = Fraction(1, 2) + Fraction(1, 2) - c
        assert dual == Fraction(5, 4) - 2 * theta


def boundary_audit() -> None:
    cp = (ROOT / "stages/stage14/14-4cp/result.md").read_text()
    s29 = (ROOT / "stages/stage14/14-s7-29/result.md").read_text()
    x6 = (ROOT / "stages/stage14/14-X6/result.md").read_text()

    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=3/4" in cp
    assert "REMAINING_RECEIVER=QuarterPhiCommonCorePrimitiveFourRootQuadraticValueEnergy" in cp
    assert "PRIMITIVE_ROOT_LINE_DYADIC_COUNT_PROVED=true" in s29
    assert "TOP_THETA_LAMBDA4_SINGULAR_BRANCH_EMPTY=true" in x6


def main() -> None:
    boundary_audit()
    exponent_ledger_audit()

    groups = ch.make_groups(600)
    checked = 0
    singular = 0
    nontrivial_good = 0
    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a_state, b_state = states[i], states[j]
                if (a_state["a"], a_state["b"]) == (b_state["a"], b_state["b"]):
                    continue
                if (a_state["km"], a_state["kp"]) == (b_state["km"], b_state["kp"]):
                    continue
                _, Cstar, _, is_singular = audit_pair(a_state, b_state)
                checked += 1
                singular += int(is_singular)
                nontrivial_good += int(Cstar > 1)

    assert checked > 0
    print("Stage14-4cq dual common-core Cayley audit: PASS")
    print(f"finite dual-cross physical pairs checked: {checked}")
    print(f"finite nontrivial good common-core packets: {nontrivial_good}")
    print(f"finite lambda=4 packets (diagnostic only): {singular}")
    print("dual gcd-square peel: exact")
    print("Cstar Cayley lambda^2 == 16 congruence: exact")
    print("fixed residual/quotient + XY -> C divisor-many: theorem in result.md")
    print("former theta=5/16,phi=1/4 corner bound: 5/8")
    print("remaining 3/4 saturation corner: theta=phi=1/4")
    print("whole-family exponent remains 3/4")


if __name__ == "__main__":
    main()
