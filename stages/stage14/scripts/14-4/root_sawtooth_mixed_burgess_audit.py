#!/usr/bin/env python3
"""Deterministic audit for Stage14-4bd.

This audit checks the exact algebra/exponent bookkeeping used by 14-4bd:
- merged 4bc boundary flags;
- divisor-level whole-E Jacobi identities on finite primitive Euclid pairs;
- Walsh complement pairing;
- handoff-band implication beta<=1 => alpha>99/200;
- Kerr d=1,r=3 specialization;
- exact mixed-squarefree saving margins;
- committed JSON summary consistency.

The external mixed Burgess theorem itself is not re-proved computationally.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import product
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4bd/result.md"
PREV = ROOT / "stages/stage14/14-4bc/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/root_sawtooth_mixed_burgess_summary.json"


def factor(n: int) -> dict[int, int]:
    n = abs(n)
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def odd_core(n: int) -> int:
    out = 1
    for p, e in factor(n).items():
        if p != 2 and e % 2:
            out *= p
    return out


def divisors_squarefree(n: int) -> list[int]:
    ps = list(factor(n))
    out = [1]
    for p in ps:
        out += [d * p for d in list(out)]
    return sorted(out)


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    z = pow(a, (p - 1) // 2, p)
    return -1 if z == p - 1 else z


def jacobi_squarefree(a: int, q: int) -> int:
    if q == 1:
        return 1
    ans = 1
    for p in factor(q):
        z = legendre(a, p)
        if z == 0:
            return 0
        ans *= z
    return ans


def assert_prev_flags() -> None:
    text = PREV.read_text()
    needed = [
        "FINAL_ROOT_SAWTOOTH_KERNEL_EXPLICIT=true",
        "ROOT_SAWTOOTH_HANDOFF_BAND=R_E>-1/200",
        "MAIN_TRACK_RECIPROCAL_TARGET_SAVING=1/200",
        "COMPLETE_POSITIVE_RECIPROCAL_EXPONENT_PROVED=false",
    ]
    for flag in needed:
        assert flag in text, flag


def audit_e_identities() -> tuple[int, int]:
    identity_checks = 0
    complement_checks = 0
    for m in range(2, 90):
        for n in range(1, m):
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            E = m * m + n * n
            e = odd_core(E)
            # Every odd prime in the squareclass kernel of a primitive sum of
            # two squares is 1 mod 4.
            assert all(p % 4 == 1 for p in factor(e))

            columns = [
                (odd_core(m), "AB"),
                (odd_core(n), "AB"),
                (odd_core(m - n), "CD"),
                (odd_core(m + n), "CD"),
            ]
            for core, kind in columns:
                for q in divisors_squarefree(core):
                    assert gcd(q, e) == 1
                    lhs = jacobi_squarefree(q, e)
                    rhs = 1 if kind == "AB" else jacobi_squarefree(2, q)
                    assert lhs == rhs, (m, n, q, e, lhs, rhs)
                    identity_checks += 1

            # Representative d1 built from arbitrary choices of the four
            # pairwise-disjoint linear squareclass pieces.
            cores = [c for c, _ in columns]
            choices = [[1, c] if c != 1 else [1] for c in cores]
            for picked in product(*choices):
                d1 = 1
                for x in picked:
                    d1 *= x
                if gcd(d1, e) != 1:
                    continue
                for v in divisors_squarefree(e):
                    w = e // v
                    lhs = jacobi_squarefree(d1, v)
                    rhs = jacobi_squarefree(d1, e) * jacobi_squarefree(d1, w)
                    assert lhs == rhs, (m, n, d1, e, v, w, lhs, rhs)
                    assert min(v, w) <= isqrt(e) + 1
                    complement_checks += 1
    return identity_checks, complement_checks


def R_E(alpha: Fraction, beta: Fraction) -> Fraction:
    kappa = max(beta / 2, min(alpha, beta))
    return alpha + beta + max(Fraction(0), Fraction(1) - kappa) - 2


def audit_handoff() -> int:
    checks = 0
    # Fine exact rational grid.  The symbolic inequality used in result.md is
    # stronger; this is a regression check against sign/case mistakes.
    for ai in range(0, 401):
        alpha = Fraction(ai, 400)
        for bi in range(0, 401):
            beta = Fraction(bi, 400)
            if beta > 1:
                continue
            if R_E(alpha, beta) > -Fraction(1, 200):
                assert alpha > Fraction(99, 200), (alpha, beta, R_E(alpha, beta))
                checks += 1
    return checks


def audit_kerr_and_margins() -> dict[str, Fraction]:
    d = Fraction(1)
    D = d * (d + 1) / 2
    r = Fraction(3)
    upper = Fraction(1, 2) + Fraction(1, 4) / (r - D / 2)
    qexp = (
        Fraction(1, 4) / r
        + D / (8 * r * (r - D / 2))
        + Fraction(1, 4) / (r * (r - D / 2))
    )
    assert D == 1
    assert upper == Fraction(3, 5)
    assert qexp == Fraction(2, 15)

    alpha = Fraction(99, 200)
    gamma = Fraction(103, 100)
    delta1 = alpha / 3 - Fraction(2, 15) * gamma
    delta2 = alpha / 2 - Fraction(1, 5) * gamma
    assert delta1 == Fraction(83, 3000)
    assert delta2 == Fraction(83, 2000)
    assert delta1 > Fraction(1, 100)
    assert delta2 > Fraction(1, 100)

    final_delta = min(Fraction(1, 200), Fraction(1, 100))
    b_exp = (Fraction(2) - final_delta) / 2
    assert final_delta == Fraction(1, 200)
    assert b_exp == Fraction(399, 400)
    return {
        "upper": upper,
        "qexp": qexp,
        "delta1": delta1,
        "delta2": delta2,
        "final_delta": final_delta,
        "b_exp": b_exp,
    }


def audit_summary(vals: dict[str, Fraction]) -> None:
    obj = json.loads(SUMMARY.read_text())
    assert obj["stage"] == "14-4bd"
    assert obj["e_walsh"]["small_side_orientation_exact"] is True
    assert obj["handoff_geometry"]["alpha_lower_bound"] == "99/200"
    assert obj["residual_character"]["q0_exponent_max"] == "3/100"
    assert obj["mixed_burgess"]["valid_interval_upper_exponent"] == "3/5"
    assert obj["mixed_burgess"]["specialized_bound"] == "N^(2/3)*Q^(2/15+o(1))"
    assert obj["exact_margin"]["kerr_term_saving"] == "83/3000"
    assert obj["exact_margin"]["completion_term_saving"] == "83/2000"
    assert obj["reciprocal_error"]["M_scale_saving"] == "1/200"
    assert obj["reciprocal_error"]["B_scale_bound"] == "B^(399/400+o(1))"
    assert vals["upper"] == Fraction(3, 5)
    assert vals["qexp"] == Fraction(2, 15)


def audit_result_flags() -> None:
    text = RESULT.read_text()
    flags = [
        "STAGE14_4BD=ROOT_SAWTOOTH_HANDOFF_CLOSED_AND_COMPLETE_RECIPROCAL_EXPONENT_FROZEN",
        "E_WALSH_SMALL_SIDE_ORIENTATION_EXACT=true",
        "HANDOFF_FORCES_ALPHA_GT_99_OVER_200=true",
        "KERR_SQUAREFREE_MIXED_THEOREM_IMPORTED=true",
        "ROOT_SAWTOOTH_HANDOFF_BAND_CLOSED=true",
        "ROOT_SAWTOOTH_SAVING_EXPONENT=1/100",
        "COMPLETE_POSITIVE_RECIPROCAL_EXPONENT_PROVED=true",
        "COMPLETE_RECIPROCAL_SAVING_EXPONENT_M_SCALE=1/200",
        "COMPLETE_RECIPROCAL_ERROR_B_SCALE=B^(399/400+o(1))",
        "EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false",
        "NEXT=Stage14-4be",
    ]
    for flag in flags:
        assert flag in text, flag


def main() -> None:
    assert_prev_flags()
    ident, comp = audit_e_identities()
    handoff = audit_handoff()
    vals = audit_kerr_and_margins()
    audit_summary(vals)
    audit_result_flags()
    print("Stage14-4bd audit: OK")
    print(f"whole-E divisor identity checks: {ident}")
    print(f"Walsh complement checks: {comp}")
    print(f"handoff grid checks: {handoff}")
    print(f"Kerr d=1,r=3 upper exponent: {vals['upper']}")
    print(f"Kerr d=1,r=3 Q exponent: {vals['qexp']}")
    print(f"worst Kerr saving margin: {vals['delta1']}")
    print(f"worst completion saving margin: {vals['delta2']}")
    print(f"frozen reciprocal saving: {vals['final_delta']}")
    print(f"B-scale exponent: {vals['b_exp']}")


if __name__ == "__main__":
    main()
