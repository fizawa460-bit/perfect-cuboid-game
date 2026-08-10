#!/usr/bin/env python3
"""Deterministic audit for Stage14-4cn.

The asymptotic claims are proved in result.md by exact algebra. This script
checks primitive ratio recovery, reciprocal Edwards normalization, the
lambda=4 factorization, and merged s7-27 regression on finite physical packets.
Finite singular/smooth counts are diagnostic only.
"""

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
    "stage14_4ch_4cn",
    SCRIPTS / "14-4" / "eight_cell_residual_lift_audit.py",
)
s727 = load_module(
    "stage14_s727_4cn",
    SCRIPTS / "14-s7-27" / "full_signed_quotient_curve_audit.py",
)


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def audit_pair(a: dict[str, int], b: dict[str, int]):
    s727.audit_pair(a, b)

    cells, triple, _, _ = ch.residual_data(a, b)
    R, S, T, J, alpha, beta, gamma, delta = cells

    r = a["r"] * b["r"]
    s = a["s"] * b["s"]
    X = a["x"] * b["x"]
    Y = a["y"] * b["y"]

    A = alpha * r
    D = delta * s
    P = R * X
    Q = J * Y
    assert D > A > 0 and Q > P > 0

    X_ag = R * J
    K_ag = alpha * delta
    lx_m = gcd(oddpart(X_ag), D - A)
    lx_p = gcd(oddpart(X_ag), D + A)
    lk_m = gcd(oddpart(K_ag), Q - P)
    lk_p = gcd(oddpart(K_ag), Q + P)

    assert gcd(lx_m, lx_p) == 1
    assert gcd(lk_m, lk_p) == 1
    assert lx_m * lx_p == oddpart(X_ag)
    assert lk_m * lk_p == oddpart(K_ag)

    # Primitive ratios recover the four odd moduli exactly.
    xr = Fraction(lx_p, lx_m)
    yr = Fraction(lk_p, lk_m)
    assert xr.numerator == lx_p and xr.denominator == lx_m
    assert yr.numerator == lk_p and yr.denominator == lk_m

    cx_m = (D - A) // lx_m
    cx_p = (D + A) // lx_p
    ck_m = (Q - P) // lk_m
    ck_p = (Q + P) // lk_p

    eps_x = X_ag // oddpart(X_ag)
    eps_k = K_ag // oddpart(K_ag)

    # Original reciprocal equations are exact filters on the canonical lift.
    assert (lx_p * cx_p) ** 2 - (lx_m * cx_m) ** 2 == (
        4 * r * s * eps_k * lk_m * lk_p
    )
    assert (lk_p * ck_p) ** 2 - (lk_m * ck_m) ** 2 == (
        4 * X * Y * eps_x * lx_m * lx_p
    )

    u = Fraction(cx_p * lx_p, cx_m * lx_m)
    v = Fraction(ck_p * lk_p, ck_m * lk_m)
    assert u == Fraction(D + A, D - A)
    assert v == Fraction(Q + P, Q - P)
    assert u > 1 and v > 1

    lam = Fraction(
        16 * r * s * X * Y * eps_x * eps_k,
        cx_m * cx_p * ck_m * ck_p,
    )
    assert lam > 0
    assert (u * u - 1) * (v * v - 1) == lam * u * v

    singular = lam == 4
    if singular:
        assert u * v - u - v - 1 == 0
        assert D * (Q - P) == A * (Q + P)
        assert Q * (D - A) == P * (D + A)

    return triple, singular, lam


def factorization_audit() -> None:
    for u in range(-7, 8):
        for v in range(-7, 8):
            lhs = (u * u - 1) * (v * v - 1) - 4 * u * v
            rhs = (u * v - u - v - 1) * (u * v + u + v - 1)
            assert lhs == rhs

    u = Fraction(3, 1)
    v = Fraction(2, 1)
    assert (u * u - 1) * (v * v - 1) == 4 * u * v
    assert u * v - u - v - 1 == 0


def boundary_audit() -> None:
    root = HERE.parents[4]
    cm = (root / "stages/stage14/14-4cm/result.md").read_text()
    s27 = (root / "stages/stage14/14-s7-27/result.md").read_text()
    assert "STAGE14_4CM=COMPLETE_QUADRATIC_BRANCH_ELIMINATION_AND_TOP_THETA_SIGNED_LINEAR_QUOTIENT_REDUCTION" in cm
    assert "STAGE14_S7_27=COMPLETE_FULL_SIGNED_QUOTIENT_DIVISOR_COLLAPSE_AND_RECIPROCAL_BIQUADRATIC_REDUCTION" in s27
    assert "FIXED_RESIDUAL_FULL_SIGNED_QUOTIENT_QUADRUPLE_MULTIPLICITY=Bo1" in s27
    assert "RECIPROCAL_RATIO_BIDEGREE_2_2_CURVE_PROVED=true" in s27


def main() -> None:
    boundary_audit()
    factorization_audit()

    groups = ch.make_groups(600)
    checked = 0
    singular = 0
    lambdas: set[Fraction] = set()
    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                _, is_singular, lam = audit_pair(a, b)
                checked += 1
                singular += int(is_singular)
                lambdas.add(lam)

    assert checked > 0
    print("Stage14-4cn reciprocal Edwards reduction audit: PASS")
    print(f"finite dual-cross physical pairs checked: {checked}")
    print(f"distinct finite physical lambda values: {len(lambdas)}")
    print(f"finite physical lambda=4 packets: {singular}")
    print("primitive ratio -> four odd moduli fiber: exactly 1")
    print("original reciprocal equation after primitive lift: exact filter")
    print("canonical equation: (u^2-1)(v^2-1)=lambda*u*v")
    print("physical lambda positivity: exact")
    print("lambda=4 rational factorization: exact")
    print("smooth lambda!=4 genus-one classification: theorem in result.md")
    print("whole-family exponent remains 7/8")


if __name__ == "__main__":
    main()
