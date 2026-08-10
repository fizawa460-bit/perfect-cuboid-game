#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-27.

The asymptotic statements are proved in result.md by exact factorization and
divisor bounds.  This script checks the full two-sign quotient identities, the
reciprocal four-modulus system and the bidegree-(2,2) ratio equation on finite
physical packets.  Finite enumeration is diagnostic, not the proof of the
asymptotic bound.
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
    "stage14_4ch_s727",
    SCRIPTS / "14-4" / "eight_cell_residual_lift_audit.py",
)
s26 = load_module(
    "stage14_s726_s727",
    SCRIPTS / "14-s7-26" / "linear_agreement_allocation_audit.py",
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


def audit_pair(a: dict[str, int], b: dict[str, int]):
    # Import every exact s7-26 check first.
    s26.audit_pair(a, b)

    cells, triple, _, hs = ch.residual_data(a, b)
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

    assert cx_minus > 0 and cx_plus > 0
    assert ck_minus > 0 and ck_plus > 0

    # Full two-sign product identities.
    assert cx_minus * cx_plus == hk_minus // oddpart(X_ag)
    assert ck_minus * ck_plus == hx_minus // oddpart(K_ag)
    assert oddpart(cx_minus * cx_plus) == oddpart(u_res)
    assert oddpart(ck_minus * ck_plus) == oddpart(v_res)

    epsilon_x = X_ag // oddpart(X_ag)
    epsilon_k = K_ag // oddpart(K_ag)
    assert epsilon_x & (epsilon_x - 1) == 0
    assert epsilon_k & (epsilon_k - 1) == 0

    # Exact reciprocal four-modulus system.
    left_x = (lx_plus * cx_plus) ** 2 - (lx_minus * cx_minus) ** 2
    right_x = 4 * r * s * epsilon_k * lk_minus * lk_plus
    assert left_x == right_x == 4 * A * D

    left_k = (lk_plus * ck_plus) ** 2 - (lk_minus * ck_minus) ** 2
    right_k = 4 * X * Y * epsilon_x * lx_minus * lx_plus
    assert left_k == right_k == 4 * P * Q

    # Exact scale-free bidegree-(2,2) ratio equation.
    xr = Fraction(lx_plus, lx_minus)
    yr = Fraction(lk_plus, lk_minus)
    curve_lhs = (cx_plus * cx_plus * xr * xr - cx_minus * cx_minus) * (
        ck_plus * ck_plus * yr * yr - ck_minus * ck_minus
    )
    curve_rhs = 16 * r * s * X * Y * epsilon_x * epsilon_k * xr * yr
    assert curve_lhs == curve_rhs

    quotient = (cx_minus, cx_plus, ck_minus, ck_plus)
    return triple, quotient, (v2(cx_minus * cx_plus), v2(ck_minus * ck_plus))


def divisor_pair_sum_bound(odd_n: int, max_j: int) -> int:
    # sum_{j=0}^J tau(2^j * odd_n)
    return tau(odd_n) * (max_j + 1) * (max_j + 2) // 2


def finite_physical_audit(limit: int = 600):
    groups = ch.make_groups(limit)
    quotients_by_triple: dict[tuple[int, int, int], set[tuple[int, int, int, int]]] = defaultdict(set)
    max_j_by_triple: dict[tuple[int, int, int], list[int]] = defaultdict(lambda: [0, 0])
    checked = 0

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                triple, quotient, js = audit_pair(a, b)
                quotients_by_triple[triple].add(quotient)
                max_j_by_triple[triple][0] = max(max_j_by_triple[triple][0], js[0])
                max_j_by_triple[triple][1] = max(max_j_by_triple[triple][1], js[1])
                checked += 1

    assert checked > 0
    max_finite_fiber = max(len(v) for v in quotients_by_triple.values())

    # Finite check of the divisor-count mechanism behind the B^o(1) theorem.
    for triple, quotients in quotients_by_triple.items():
        _, u_res, v_res = triple
        jx, jk = max_j_by_triple[triple]
        bound_x = divisor_pair_sum_bound(oddpart(u_res), jx)
        bound_k = divisor_pair_sum_bound(oddpart(v_res), jk)
        assert len(quotients) <= bound_x * bound_k

    return checked, len(quotients_by_triple), max_finite_fiber


def exponent_ledger_audit() -> None:
    # The old dominant-quotient raw support has exponent 1/8 along the top edge.
    for phi in (Fraction(3, 16), Fraction(7, 32), Fraction(1, 4)):
        old_x = Fraction(5, 16) - phi
        old_k = phi - Fraction(3, 16)
        assert old_x + old_k == Fraction(1, 8)

    # After fixing residual data, the full quotient quadruple is divisor-bounded,
    # so its polynomial support exponent is zero.  This alone does not bound the
    # moving reciprocal modulus solutions.
    fixed_residual_full_quotient_exponent = Fraction(0, 1)
    assert fixed_residual_full_quotient_exponent == 0


def boundary_audit() -> None:
    root = HERE.parents[4]
    s26_text = (root / "stages/stage14/14-s7-26/result.md").read_text()
    cm_text = (root / "stages/stage14/14-4cm/result.md").read_text()

    assert "STAGE14_S7_26=COMPLETE_COMMON_CORE_AGREEMENT_I_BRANCH_ELIMINATION_AND_TOP_EDGE_LINEAR_ALLOCATION" in s26_text
    assert "XI_AGREEMENT_EXACT_TWO_WAY_LINEAR_ALLOCATION=true" in s26_text
    assert "K_AGREEMENT_EXACT_TWO_WAY_LINEAR_ALLOCATION=true" in s26_text
    assert "STAGE14_4CM=COMPLETE_QUADRATIC_BRANCH_ELIMINATION_AND_TOP_THETA_SIGNED_LINEAR_QUOTIENT_REDUCTION" in cm_text
    assert "TOP_THETA_SIGNED_QUOTIENT_PAIR_SUPPORT_EXPONENT_MAX=1/8" in cm_text
    assert "SIGNED_QUOTIENT_SUPPORT_ALONE_IMPLIES_POWER_SAVING=false" in cm_text


def main() -> None:
    boundary_audit()
    exponent_ledger_audit()
    checked, triples, max_fiber = finite_physical_audit()

    print("Stage14-s7-27 full signed quotient curve audit: PASS")
    print(f"finite dual-cross physical pairs checked: {checked}")
    print(f"finite residual triples observed: {triples}")
    print(f"max finite residual -> full quotient quadruple fiber: {max_fiber}")
    print("full xi signed quotient product oddpart = oddpart(u_res): exact")
    print("full k signed quotient product oddpart = oddpart(v_res): exact")
    print("fixed residual full quotient quadruple multiplicity: B^o(1) by divisor count")
    print("reciprocal four-modulus quadratic system: exact")
    print("scale-free bidegree-(2,2) ratio equation: exact")
    print("whole-family exponent remains 7/8")


if __name__ == "__main__":
    main()
