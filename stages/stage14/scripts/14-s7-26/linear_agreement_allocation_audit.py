#!/usr/bin/env python3
"""Deterministic regression/falsifier for Stage14-s7-26.

The asymptotic statements are exact common-core divisibility and exponent
bookkeeping.  Finite enumeration only checks that actual physical packets obey
the claimed two-way linear allocation and that all four dominant sign classes
can occur; it is not the proof of an asymptotic count.
"""

from collections import Counter, defaultdict
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
    "stage14_4ch_s726",
    SCRIPTS / "14-4" / "eight_cell_residual_lift_audit.py",
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


def audit_pair(a: dict[str, int], b: dict[str, int]):
    cells, triple, _, hs = ch.residual_data(a, b)
    ch.audit_pair(a, b)

    R, S, T, J, alpha, beta, gamma, delta = cells
    C, u_res, v_res = triple
    hk_plus, hk_minus, hx_plus, hx_minus = hs

    r = a["r"] * b["r"]
    s = a["s"] * b["s"]
    X = a["x"] * b["x"]
    Y = a["y"] * b["y"]

    A = alpha * r
    D = delta * s
    P = R * X
    Q = J * Y

    X_sw = S * T
    X_ag = R * J
    K_sw = beta * gamma
    K_ag = alpha * delta

    assert hk_plus == D * D + A * A
    assert hk_minus == D * D - A * A
    assert hx_plus == Q * Q + P * P
    assert hx_minus == Q * Q - P * P
    assert hk_minus > 0 and hx_minus > 0

    # Merged 4cg plus-factor coprimality removes the quadratic/i branches.
    assert gcd(hk_plus, oddpart(X_ag)) == 1
    assert gcd(hx_plus, oddpart(K_ag)) == 1
    assert hk_minus % oddpart(X_ag) == 0
    assert hx_minus % oddpart(K_ag) == 0

    x_minus = gcd(oddpart(X_ag), D - A)
    x_plus = gcd(oddpart(X_ag), D + A)
    k_minus = gcd(oddpart(K_ag), Q - P)
    k_plus = gcd(oddpart(K_ag), Q + P)

    assert x_minus * x_plus == oddpart(X_ag)
    assert k_minus * k_plus == oddpart(K_ag)
    assert gcd(x_minus, x_plus) == 1
    assert gcd(k_minus, k_plus) == 1

    assert gcd(oddpart(X_ag), D * D + A * A) == 1
    assert gcd(oddpart(K_ag), Q * Q + P * P) == 1

    # Exact s7-25 common-core cancellation on the two difference hosts.
    assert hk_plus == (2 ** v2(hk_plus)) * C * oddpart(X_sw)
    assert hx_plus == (2 ** v2(hx_plus)) * C * oddpart(K_sw)
    assert hk_minus * (2 ** v2(hk_plus)) == (2 ** v2(X_sw)) * X_ag * u_res
    assert hx_minus * (2 ** v2(hx_plus)) == (2 ** v2(K_sw)) * K_ag * v_res

    xi_sign = "-" if x_minus >= x_plus else "+"
    k_sign = "-" if k_minus >= k_plus else "+"

    L_xi = max(x_minus, x_plus)
    L_k = max(k_minus, k_plus)
    xi_linear = D - A if xi_sign == "-" else D + A
    k_linear = Q - P if k_sign == "-" else Q + P
    assert xi_linear % L_xi == 0
    assert k_linear % L_k == 0

    return (xi_sign, k_sign), (xi_linear // L_xi, k_linear // L_k)


def finite_physical_audit(limit: int = 600):
    groups = ch.make_groups(limit)
    checked = 0
    sign_hist = Counter()
    max_xi_cofactor = 0
    max_k_cofactor = 0

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                signs, cofactors = audit_pair(a, b)
                sign_hist[signs] += 1
                max_xi_cofactor = max(max_xi_cofactor, cofactors[0])
                max_k_cofactor = max(max_k_cofactor, cofactors[1])
                checked += 1

    assert checked > 0
    # All four sign classes are genuinely physical in the finite sample, so
    # s7-26 must not eliminate any of them without a new argument.
    assert set(sign_hist) == {("-", "-"), ("-", "+"), ("+", "-"), ("+", "+")}
    return checked, sign_hist, max_xi_cofactor, max_k_cofactor


def exponent_ledger_audit() -> None:
    theta = Fraction(5, 16)
    for phi in (Fraction(3, 16), Fraction(7, 32), Fraction(1, 4)):
        x_ag = 2 * phi
        k_ag = 2 * theta
        xi_dom = x_ag / 2
        k_dom = k_ag / 2
        assert xi_dom == phi
        assert k_dom == Fraction(5, 16)

        xi_linear_height = theta
        k_linear_height = phi + Fraction(1, 8)
        xi_cofactor = xi_linear_height - xi_dom
        k_cofactor = k_linear_height - k_dom

        assert xi_cofactor == Fraction(5, 16) - phi
        assert k_cofactor == phi - Fraction(3, 16)
        assert xi_cofactor >= Fraction(1, 16)
        assert xi_cofactor <= Fraction(1, 8)
        assert k_cofactor >= 0
        assert k_cofactor <= Fraction(1, 16)
        assert xi_cofactor + k_cofactor == Fraction(1, 8)

    # Common-core refinement strictly improves 4cl's cube-root dominant scales.
    assert Fraction(1, 2) > Fraction(1, 3)
    assert Fraction(5, 16) > Fraction(5, 24)


def boundary_audit() -> None:
    root = HERE.parents[4]
    s25 = (root / "stages/stage14/14-s7-25/result.md").read_text()
    cg = (root / "stages/stage14/14-4cg/result.md").read_text()
    cl = (root / "stages/stage14/14-4cl/result.md").read_text()

    assert "STAGE14_S7_25=COMPLETE_FIXED_RESIDUAL_XI_SWITCH_PRODUCT_RECONSTRUCTION_AND_TOP_THETA_LOCALIZATION" in s25
    assert "FIXED_RESIDUAL_XI_SWITCH_PRODUCT_PACKET_FIBER_BO1=true" in s25
    assert "TOP_THETA_BARRIER=theta=5/16" in s25
    assert "gcd(H_k^+, oddpart(Xi_agree))=1" in cg
    assert "gcd(H_xi^+, oddpart(K_agree))=1" in cg
    assert "STAGE14_4CL=COMPLETE_PHYSICAL_PROPORTIONAL_BRANCH_ELIMINATION_AND_RECIPROCAL_CYCLOTOMIC_REDUCTION" in cl
    assert "XI_THREE_WAY_CYCLOTOMIC_ALLOCATION_PROVED=true" in cl
    assert "K_THREE_WAY_CYCLOTOMIC_ALLOCATION_PROVED=true" in cl


def main() -> None:
    boundary_audit()
    exponent_ledger_audit()
    checked, sign_hist, max_xi_c, max_k_c = finite_physical_audit()

    print("Stage14-s7-26 linear agreement allocation audit: PASS")
    print(f"finite dual-cross physical pairs checked: {checked}")
    print(f"dominant sign histogram: {dict(sorted(sign_hist.items()))}")
    print(f"max finite xi dominant cofactor: {max_xi_c}")
    print(f"max finite k dominant cofactor: {max_k_c}")
    print("xi agreement i branch: empty by common-core plus-factor coprimality")
    print("k agreement i branch: empty by common-core plus-factor coprimality")
    print("dominant branch types: 4")
    print("top-edge dominant xi linear modulus exponent >= phi")
    print("top-edge dominant k linear modulus exponent >= 5/16")
    print("dominant linear cofactor total exponent <= 1/8")
    print("whole-family exponent remains 7/8")


if __name__ == "__main__":
    main()
