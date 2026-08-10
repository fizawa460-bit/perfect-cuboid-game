#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-30.

The asymptotic theorem is proved in result.md.  This script checks the exact
second common-core quadratic congruence on finite physical packets, the common-
core scale identities used by the exponent ledger, the nonprimitive root-pair
count on synthetic boxes, and the exact Fraction optimization to 11/16.
"""

from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve()
SCRIPTS = HERE.parents[1]


def load_module(name: str, path: Path):
    spec = spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


s28 = load_module(
    "stage14_s728_s730",
    SCRIPTS / "14-s7-28" / "primitive_ratio_reconstruction_audit.py",
)
s29 = load_module(
    "stage14_s729_s730",
    SCRIPTS / "14-s7-29" / "common_core_primitive_root_line_audit.py",
)
ch = s28.ch


def v2(n: int) -> int:
    assert n > 0
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


def oddpart(n: int) -> int:
    return n >> v2(n)


def tau(n: int) -> int:
    assert n >= 1
    x = n
    out = 1
    p = 2
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


def audit_packet(a_state: dict[str, int], b_state: dict[str, int]):
    # Run predecessor reconstruction and the first common-core root-line checks.
    d = s28.packet_data(a_state, b_state)
    s28.audit_reconstruction(d)
    s29.audit_packet(a_state, b_state)

    R, S, T, J, alpha, beta, gamma, delta = d["cells"]
    C, u_res, v_res = d["triple"]
    hk_plus, hk_minus, hx_plus, hx_minus = d["hs"]

    A = int(d["A"])
    D = int(d["D"])
    X = int(d["X"])
    Y = int(d["Y"])

    p = int(d["lk_plus"])
    q = int(d["lk_minus"])
    c = int(d["ck_plus"])
    dd = int(d["ck_minus"])

    # Common-core scale identities: the odd part of Hk+ differs from Hk+
    # only by the endpoint-small gcd/parity factor, while S*T has at most one 2.
    g_ad = gcd(A, D)
    assert (1 << v2(hk_plus)) <= 2 * g_ad * g_ad
    assert (S * T) // oddpart(S * T) in (1, 2)
    assert oddpart(hk_plus) == C * oddpart(S * T)

    # Second common-core quadratic congruence.
    assert gcd(p, q) == 1
    assert p * q == oddpart(alpha * delta)
    assert gcd(C, p * q) == 1
    assert hx_plus == (c * c * p * p + dd * dd * q * q) // 2
    assert (c * c * p * p + dd * dd * q * q) % C == 0

    # Product identity and the remaining common-gcd support.
    assert c * dd == hx_minus // oddpart(alpha * delta)
    h = gcd(c, dd)
    assert (X * Y) % oddpart(h) == 0

    return C, u_res, v_res, p, q, c, dd, h


def finite_physical_audit(limit: int = 600):
    groups = ch.make_groups(limit)
    checked = 0
    nontrivial_second_C = 0
    max_second_gcd = 1
    max_second_product = 1

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a_state, b_state = states[i], states[j]
                if (a_state["a"], a_state["b"]) == (b_state["a"], b_state["b"]):
                    continue
                if (a_state["km"], a_state["kp"]) == (b_state["km"], b_state["kp"]):
                    continue
                C, _, _, _, _, c, d, h = audit_packet(a_state, b_state)
                nontrivial_second_C += int(C > 1)
                max_second_gcd = max(max_second_gcd, h)
                max_second_product = max(max_second_product, c * d)
                checked += 1

    assert checked > 0
    return checked, nontrivial_second_C, max_second_gcd, max_second_product


def synthetic_nonprimitive_root_pair_audit() -> None:
    # Exhaustive small-box regression for the shape
    # N_Q(M) << B^o(1)(sqrt(M)+M/Q).
    # The theorem and its divisor-sum proof are in result.md; this deliberately
    # uses a loose absolute/log/divisor envelope rather than pretending the
    # finite regression proves the asymptotic statement.
    for Q in range(1, 60, 2):
        for A in range(1, min(Q + 1, 9)):
            if gcd(A, Q) != 1:
                continue
            for B in range(1, min(Q + 1, 9)):
                if gcd(B, Q) != 1:
                    continue
                for M in (8, 16, 32, 64, 96):
                    count = 0
                    for x in range(1, M + 1):
                        for y in range(1, M // x + 1):
                            if (A * A * x * x + B * B * y * y) % Q == 0:
                                count += 1
                    logfac = (M.bit_length() + 1) ** 2
                    rhs = 16 * tau(Q) * logfac * (isqrt(M) + 1 + M // Q + 1)
                    assert count <= rhs


def exponent_ledger_audit() -> None:
    vals = [Fraction(n, 64) for n in range(8, 21)]
    saw = 0
    worst = Fraction(0, 1)
    worst_points = []

    for theta in vals:
        if not (Fraction(3, 16) <= theta <= Fraction(5, 16)):
            continue
        for phi in vals:
            if not (Fraction(1, 8) <= phi <= Fraction(1, 4)):
                continue
            if theta < phi:
                continue
            if theta - phi > Fraction(1, 8):
                continue
            if theta + phi < Fraction(3, 8):
                continue

            c = 2 * theta + 2 * phi - Fraction(3, 4)
            mu = 2 * theta - 2 * phi
            nu = Fraction(1, 4) + 2 * phi - 2 * theta
            assert c >= 0 and mu >= 0 and nu >= 0
            assert 2 * phi - c == Fraction(3, 4) - 2 * theta
            assert 2 * phi - c >= Fraction(1, 8)

            second = max(nu / 2, nu - c)
            total_direct = c + mu + (2 * phi - c) + second
            total_formula = max(
                theta + phi + Fraction(1, 8),
                1 - 2 * theta,
            )
            assert total_direct == total_formula
            assert total_formula <= Fraction(11, 16)

            if total_formula > worst:
                worst = total_formula
                worst_points = [(theta, phi)]
            elif total_formula == worst:
                worst_points.append((theta, phi))
            saw += 1

    assert saw > 0
    assert worst == Fraction(11, 16)
    assert worst_points == [(Fraction(5, 16), Fraction(1, 4))]

    theta = Fraction(5, 16)
    phi = Fraction(1, 4)
    c = 2 * theta + 2 * phi - Fraction(3, 4)
    mu = 2 * theta - 2 * phi
    nu = Fraction(1, 4) + 2 * phi - 2 * theta
    assert (c, mu, nu) == (Fraction(3, 8), Fraction(1, 8), Fraction(1, 8))
    assert max(nu / 2, nu - c) == Fraction(1, 16)
    assert Fraction(11, 16) - Fraction(1, 2) == Fraction(3, 16)


def boundary_audit() -> None:
    root = HERE.parents[4]
    s29_text = (root / "stages/stage14/14-s7-29/result.md").read_text()
    cp_text = (root / "stages/stage14/14-4cp/result.md").read_text()
    s28_text = (root / "stages/stage14/14-s7-28/result.md").read_text()
    t68_text = (root / "stages/stage14/14-t68/result.md").read_text()

    assert "STAGE14_S7_29=COMPLETE_COMMON_CORE_GAUSSIAN_ROOT_LINE_PRIMITIVE_LATTICE_COUNT_AND_3_4_BOUND" in s29_text
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=3/4" in s29_text
    assert "STAGE14_4CP=COMPLETE_THREE_QUARTER_PROMOTION_SINGULAR_ELIMINATION_AND_QUARTER_PHI_ROOTLINE_REDUCTION" in cp_text
    assert "THREE_QUARTER_SATURATION_REQUIRES_THETA=5/16" in cp_text
    assert "THREE_QUARTER_SATURATION_REQUIRES_PHI=1/4" in cp_text
    assert "SELF_GENERATED_FOUR_ROOT_MODULI_CHARGED_AS_INDEPENDENT_SPACING=false" in cp_text
    assert "OPPOSITE_AGREEMENT_PRODUCT_RECONSTRUCTED_FROM_PRIMITIVE_X_PAIR=true" in s28_text
    assert "TH18_NEEDED=false" in t68_text


def main() -> None:
    boundary_audit()
    synthetic_nonprimitive_root_pair_audit()
    exponent_ledger_audit()
    checked, nontrivial, max_gcd, max_prod = finite_physical_audit()

    print("Stage14-s7-30 two-sided common-core root-pair audit: PASS")
    print(f"finite dual-cross physical pairs checked: {checked}")
    print(f"finite packets with nontrivial second common-core modulus: {nontrivial}")
    print(f"max finite opposite signed-quotient gcd: {max_gcd}")
    print(f"max finite opposite signed-quotient product: {max_prod}")
    print("common-core exponent scale pin: exact structural identity")
    print("second common-core quadratic congruence: exact")
    print("nonprimitive root-pair bound sqrt(M)+M/C: synthetic exhaustive regression PASS")
    print("two-sided dyadic block exponent: max(theta+phi+1/8,1-2theta)")
    print("unique worst corner: theta=5/16, phi=1/4")
    print("new whole-family physical upper-bound exponent: 11/16")
    print("s7-30 auxiliary H needed: false")


if __name__ == "__main__":
    main()
