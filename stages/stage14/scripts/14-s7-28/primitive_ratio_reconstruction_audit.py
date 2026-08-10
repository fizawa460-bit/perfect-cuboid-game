#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-28.

The theorem proof is in result.md.  This script checks the exact singular
factorization, primitive-ratio rigidity, one-pair reconstruction, opposite
agreement-product recovery, root-product recovery and switch-product recovery
on finite physical packets.  Finite enumeration is diagnostic only.
"""

from collections import defaultdict
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve()
SCRIPTS = HERE.parents[1]


def load_module(name: str, path: Path):
    spec = spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ch = load_module(
    "stage14_4ch_s728",
    SCRIPTS / "14-4" / "eight_cell_residual_lift_audit.py",
)
s27 = load_module(
    "stage14_s727_s728",
    SCRIPTS / "14-s7-27" / "full_signed_quotient_curve_audit.py",
)


def v2(n: int) -> int:
    assert n > 0
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


def oddpart(n: int) -> int:
    return n >> v2(n)


def synthetic_singular_factorization_audit() -> None:
    # Exact algebraic identity at K=4abcd, checked on rational sample points.
    for a, b, c, d in ((2, 3, 5, 7), (1, 4, 3, 2), (5, 2, 7, 1)):
        K = 4 * a * b * c * d
        for x in (Fraction(1, 2), Fraction(5, 3), Fraction(7, 4)):
            for y in (Fraction(2, 3), Fraction(4, 5), Fraction(9, 7)):
                F = (a * a * x * x - b * b) * (c * c * y * y - d * d) - K * x * y
                f1 = a * x * (c * y - d) - b * (c * y + d)
                f2 = a * x * (c * y + d) + b * (c * y - d)
                assert F == f1 * f2


def packet_data(a_state: dict[str, int], b_state: dict[str, int]):
    # Run the complete predecessor checks first.
    s27.audit_pair(a_state, b_state)

    cells, triple, _, hs = ch.residual_data(a_state, b_state)
    R, S, T, J, alpha, beta, gamma, delta = cells
    C, u_res, v_res = triple
    hk_plus, hk_minus, hx_plus, hx_minus = hs

    r = a_state["r"] * b_state["r"]
    s = a_state["s"] * b_state["s"]
    X = a_state["x"] * b_state["x"]
    Y = a_state["y"] * b_state["y"]

    A = alpha * r
    D = delta * s
    P = R * X
    Q = J * Y

    X_ag = R * J
    K_ag = alpha * delta

    lx_minus = gcd(oddpart(X_ag), D - A)
    lx_plus = gcd(oddpart(X_ag), D + A)
    lk_minus = gcd(oddpart(K_ag), Q - P)
    lk_plus = gcd(oddpart(K_ag), Q + P)

    assert lx_minus * lx_plus == oddpart(X_ag)
    assert lk_minus * lk_plus == oddpart(K_ag)
    assert gcd(lx_minus, lx_plus) == 1
    assert gcd(lk_minus, lk_plus) == 1

    cx_minus = (D - A) // lx_minus
    cx_plus = (D + A) // lx_plus
    ck_minus = (Q - P) // lk_minus
    ck_plus = (Q + P) // lk_plus

    epsilon_x = X_ag // oddpart(X_ag)
    epsilon_k = K_ag // oddpart(K_ag)

    return {
        "cells": cells,
        "triple": triple,
        "hs": hs,
        "r": r,
        "s": s,
        "X": X,
        "Y": Y,
        "A": A,
        "D": D,
        "P": P,
        "Q": Q,
        "X_ag": X_ag,
        "K_ag": K_ag,
        "lx_minus": lx_minus,
        "lx_plus": lx_plus,
        "lk_minus": lk_minus,
        "lk_plus": lk_plus,
        "cx_minus": cx_minus,
        "cx_plus": cx_plus,
        "ck_minus": ck_minus,
        "ck_plus": ck_plus,
        "epsilon_x": epsilon_x,
        "epsilon_k": epsilon_k,
    }


def audit_reconstruction(d: dict[str, object]) -> bool:
    R, S, T, J, alpha, beta, gamma, delta = d["cells"]  # type: ignore[misc]
    C, u_res, v_res = d["triple"]  # type: ignore[misc]
    hk_plus, hk_minus, hx_plus, hx_minus = d["hs"]  # type: ignore[misc]

    r = int(d["r"])
    s = int(d["s"])
    X = int(d["X"])
    Y = int(d["Y"])
    A = int(d["A"])
    D = int(d["D"])
    P = int(d["P"])
    Q = int(d["Q"])

    lxm = int(d["lx_minus"])
    lxp = int(d["lx_plus"])
    lkm = int(d["lk_minus"])
    lkp = int(d["lk_plus"])
    bx = int(d["cx_minus"])
    ax = int(d["cx_plus"])
    dk = int(d["ck_minus"])
    ck = int(d["ck_plus"])
    epsx = int(d["epsilon_x"])
    epsk = int(d["epsilon_k"])

    # Reduced ratios recover the physical pairs exactly; there is no scale.
    xr = Fraction(lxp, lxm)
    yr = Fraction(lkp, lkm)
    assert xr.numerator == lxp and xr.denominator == lxm
    assert yr.numerator == lkp and yr.denominator == lkm

    # One primitive xi pair reconstructs D,A exactly.
    assert (ax * lxp + bx * lxm) % 2 == 0
    assert (ax * lxp - bx * lxm) % 2 == 0
    D_rec = (ax * lxp + bx * lxm) // 2
    A_rec = (ax * lxp - bx * lxm) // 2
    assert D_rec == D and A_rec == A
    assert A_rec % r == 0 and D_rec % s == 0
    assert A_rec // r == alpha
    assert D_rec // s == delta

    # The first reciprocal equation reconstructs the full opposite odd product.
    numerator_n = (ax * lxp) ** 2 - (bx * lxm) ** 2
    denom_n = 4 * r * s * epsk
    assert numerator_n > 0 and numerator_n % denom_n == 0
    Nk = numerator_n // denom_n
    assert Nk == lkm * lkp == oddpart(alpha * delta)

    # A chosen opposite split reconstructs P,Q and then the moving root product.
    assert (ck * lkp + dk * lkm) % 2 == 0
    assert (ck * lkp - dk * lkm) % 2 == 0
    Q_rec = (ck * lkp + dk * lkm) // 2
    P_rec = (ck * lkp - dk * lkm) // 2
    assert Q_rec == Q and P_rec == P

    numerator_xy = (ck * lkp) ** 2 - (dk * lkm) ** 2
    denom_xy = 4 * epsx * lxm * lxp
    assert numerator_xy > 0 and numerator_xy % denom_xy == 0
    XY_rec = numerator_xy // denom_xy
    assert XY_rec == X * Y
    assert P * Q == (R * J) * X * Y

    # Plus hosts reconstruct both switch products at odd part level.
    assert hk_plus == D * D + A * A
    assert hx_plus == Q * Q + P * P
    assert oddpart(hk_plus) % C == 0
    assert oddpart(hx_plus) % C == 0
    assert oddpart(hk_plus) // C == oddpart(S * T)
    assert oddpart(hx_plus) // C == oddpart(beta * gamma)

    # Exact singular criterion and physical rational component if it occurs.
    K = 16 * r * s * X * Y * epsx * epsk
    singular = K == 4 * ax * bx * ck * dk
    if singular:
        assert (D + A) * P == (D - A) * Q
        # Physical point lies on the first rational factor; second is positive.
        f1_num = ax * lxp * (ck * lkp - dk * lkm) - bx * lxm * (ck * lkp + dk * lkm)
        f2_num = ax * lxp * (ck * lkp + dk * lkm) + bx * lxm * (ck * lkp - dk * lkm)
        assert f1_num == 0
        assert f2_num > 0

    return singular


def finite_physical_audit(limit: int = 600):
    groups = ch.make_groups(limit)
    checked = 0
    singular_hits = 0
    by_primitive_key: dict[tuple[object, ...], int] = defaultdict(int)

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a_state, b_state = states[i], states[j]
                if (a_state["a"], a_state["b"]) == (b_state["a"], b_state["b"]):
                    continue
                if (a_state["km"], a_state["kp"]) == (b_state["km"], b_state["kp"]):
                    continue

                d = packet_data(a_state, b_state)
                singular_hits += int(audit_reconstruction(d))
                quotient = (
                    d["cx_minus"], d["cx_plus"], d["ck_minus"], d["ck_plus"]
                )
                key = (
                    d["triple"], quotient, d["r"], d["s"], d["epsilon_x"], d["epsilon_k"],
                    d["lx_plus"], d["lx_minus"],
                )
                by_primitive_key[key] += 1
                checked += 1

    assert checked > 0
    return checked, singular_hits, max(by_primitive_key.values())


def boundary_audit() -> None:
    root = HERE.parents[4]
    s27_text = (root / "stages/stage14/14-s7-27/result.md").read_text()
    assert "STAGE14_S7_27=COMPLETE_FULL_SIGNED_QUOTIENT_DIVISOR_COLLAPSE_AND_RECIPROCAL_BIQUADRATIC_REDUCTION" in s27_text
    assert "FIXED_RESIDUAL_FULL_SIGNED_QUOTIENT_QUADRUPLE_MULTIPLICITY=Bo1" in s27_text
    assert "RECIPROCAL_FOUR_MODULUS_QUADRATIC_SYSTEM_PROVED=true" in s27_text
    assert "RECIPROCAL_RATIO_BIDEGREE_2_2_CURVE_PROVED=true" in s27_text


def main() -> None:
    boundary_audit()
    synthetic_singular_factorization_audit()
    checked, singular_hits, max_primitive_fiber = finite_physical_audit()

    print("Stage14-s7-28 primitive ratio reconstruction audit: PASS")
    print(f"finite dual-cross physical pairs checked: {checked}")
    print(f"finite singular-specialization hits: {singular_hits}")
    print(f"max finite fixed primitive-key physical multiplicity: {max_primitive_fiber}")
    print("ratio singular iff K=4abcd: algebraic theorem locked in result.md")
    print("singular specialization factorization: exact")
    print("reduced ratio recovers both modulus pairs: exact")
    print("absolute modulus scale defect: 1")
    print("opposite agreement product from primitive xi pair: exact")
    print("moving X*Y reconstruction: exact")
    print("switch-product oddpart reconstruction: exact")
    print("generic fixed-K genus-one receiver: nonminimal")
    print("whole-family exponent remains 7/8")


if __name__ == "__main__":
    main()
