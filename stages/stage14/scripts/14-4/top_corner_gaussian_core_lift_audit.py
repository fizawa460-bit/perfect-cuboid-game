#!/usr/bin/env python3
"""Deterministic audit for Stage14-4ct.

Checks:
- odd residual-host gcd peel identities on a finite exhaustive box;
- all surviving good-core primes split in Z[i];
- exact d | v identity;
- gcd-stratified exponent ledger E <= 5/8-rho;
- frozen theorem-boundary tokens.
"""

from fractions import Fraction
from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4ct/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/top_corner_gaussian_core_lift_summary.json"


def oddpart(n: int) -> int:
    while n and n % 2 == 0:
        n //= 2
    return n


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors_from_factorization(fac: dict[int, int]) -> list[int]:
    ds = [1]
    for p, e in fac.items():
        nxt = []
        pe = 1
        for _ in range(e + 1):
            nxt.extend(d * pe for d in ds)
            pe *= p
        ds = nxt
    return ds


def audit_integer_lemma(limit: int = 48) -> int:
    checks = 0
    for A in range(1, limit + 1):
        for B in range(1, limit + 1):
            N_odd = oddpart(A * A + B * B)
            g = oddpart(gcd(A, B))
            A0, B0 = A // g, B // g
            N0_odd = oddpart(A0 * A0 + B0 * B0)

            for C in divisors_from_factorization(factor(N_odd)):
                if C % 2 == 0:
                    continue
                v = N_odd // C
                C_bad = gcd(C, g * g)
                C_good = C // C_bad
                d = (g * g) // C_bad

                assert N0_odd % C_good == 0
                assert v % d == 0
                assert N0_odd // C_good == v // d
                assert C_bad * C_good == C
                assert C_bad * d == g * g

                # A primitive sum of two squares has no 3 mod 4 odd prime.
                for p in factor(C_good):
                    assert p % 4 == 1, (A, B, C, C_good, p)
                checks += 1
    return checks


def audit_exponent_ledger() -> int:
    # At the top corner C has exponent 3/8 and v has exponent <=1/8.
    # rho = log_B g, sigma = log_B d.  For fixed g, d|g^2 is
    # divisor-many, so the charged-once host exponent is exactly bounded by
    # 1/8 + rho + delta + (1/8-sigma), where
    # delta = 3/8 - 2rho + sigma.
    checks = 0
    eighth = Fraction(1, 8)
    three_eighths = Fraction(3, 8)
    five_eighths = Fraction(5, 8)

    # Rational grid is only an algebraic regression; the proof in result.md
    # is symbolic.
    step = Fraction(1, 192)
    for ir in range(0, 49):  # rho up to 1/4
        rho = ir * step
        for isg in range(0, 25):  # sigma up to 1/8
            sigma = isg * step
            if sigma > 2 * rho:
                continue  # d|g^2
            delta = three_eighths - 2 * rho + sigma
            if delta < 0:
                continue
            t_exp = eighth - sigma
            if t_exp < 0:
                continue  # d|v, v<=B^1/8
            E = eighth + rho + delta + t_exp
            assert E == five_eighths - rho
            assert E <= five_eighths
            if rho > 0:
                assert E < five_eighths
            else:
                assert delta == three_eighths
            checks += 1
    return checks


def audit_boundary() -> None:
    text = RESULT.read_text()
    required = [
        "STAGE14_4CT=COMPLETE_TOP_CORNER_RESIDUAL_HOST_GCD_PEEL_AND_PRIMITIVE_GAUSSIAN_COMMON_CORE_LIFT",
        "UNIQUE_FIVE_EIGHTHS_SATURATION_THETA=5/16",
        "UNIQUE_FIVE_EIGHTHS_SATURATION_PHI=1/4",
        "RESIDUAL_HOST_EXCESS_SQUARE_DIVIDES_VRES=true",
        "CANONICAL_GOOD_COMMON_CORE_GAUSSIAN_DIVISOR_EXISTS=true",
        "RESIDUAL_HOST_CANONICAL_FACTORIZATION=W_S=g*Pi_C*T_C",
        "GCD_STRATIFIED_XI_HOST_BLOCK_EXPONENT=5/8-rho",
        "FIVE_EIGHTHS_SATURATION_REQUIRES_RESIDUAL_HOST_GCD=Bo1",
        "FIVE_EIGHTHS_SATURATION_GOOD_COMMON_CORE_EXPONENT=3/8",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8",
        "NEW_WHOLE_FAMILY_POWER_SAVING_BELOW_5_8_PROVED=false",
        "REMAINING_RECEIVER=TopCornerPrimitiveXiResidualGaussianCoreAgreementIncidence",
        "MAINLINE_H_NEEDED=false",
        "NEXT=Stage14-4cu",
    ]
    for token in required:
        assert token in text, token

    data = json.loads(SUMMARY.read_text())
    assert data["current_physical_upper_bound_exponent"] == "5/8"
    assert data["new_whole_family_power_saving_below_5_8_proved"] is False
    assert data["canonical_factorization"]["d_divides_v_res_odd"] is True
    assert data["remaining_receiver"] == "TopCornerPrimitiveXiResidualGaussianCoreAgreementIncidence"
    assert data["mainline_h_needed"] is False


def main() -> None:
    integer_checks = audit_integer_lemma()
    ledger_checks = audit_exponent_ledger()
    audit_boundary()
    print(f"Stage14-4ct integer lemma checks: {integer_checks}")
    print(f"Stage14-4ct exponent ledger checks: {ledger_checks}")
    print("Stage14-4ct audit: PASS")


if __name__ == "__main__":
    main()
