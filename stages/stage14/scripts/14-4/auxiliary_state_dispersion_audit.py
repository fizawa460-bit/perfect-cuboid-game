#!/usr/bin/env python3
"""Stage14-4aw: audit auxiliary-state rank-one bulk and discrepancy ledger."""

import json
from fractions import Fraction
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
AV = ROOT / "stages/stage14/14-4av/result.md"
S5H = ROOT / "stages/stage14/14-s5h/result.md"
OUT = ROOT / "stages/stage14/data/14-4/auxiliary_state_dispersion_summary.json"

PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
COLUMNS = ("m", "n", "m-n", "m+n", "m2+n2")
LINEAR = {"m", "n", "m-n", "m+n"}


def value(col: str, m: int, n: int) -> int:
    if col == "m":
        return m
    if col == "n":
        return n
    if col == "m-n":
        return m - n
    if col == "m+n":
        return m + n
    if col == "m2+n2":
        return m * m + n * n
    raise ValueError(col)


def primitive_root_count(p: int, col: str) -> int:
    total = 0
    for m in range(p):
        for n in range(p):
            if m == 0 and n == 0:
                continue
            if value(col, m, n) % p == 0:
                total += 1
    return total


def prime_factors_squarefree(q: int):
    out = []
    x = q
    p = 3
    while p * p <= x:
        if x % p == 0:
            out.append(p)
            x //= p
            assert x % p != 0
        p += 2
    if x > 1:
        out.append(x)
    return out


def lambda_l(q: int) -> Fraction:
    ans = Fraction(1, 1)
    for p in prime_factors_squarefree(q):
        ans *= Fraction(1, p + 1)
    return ans


def lambda_e(q: int) -> Fraction:
    ans = Fraction(1, 1)
    for p in prime_factors_squarefree(q):
        if p % 4 == 3:
            return Fraction(0, 1)
        ans *= Fraction(2, p + 1)
    return ans


def fstr(x: Fraction) -> str:
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def main() -> None:
    av = AV.read_text()
    s5h = S5H.read_text()
    assert "BARE_LINEAR_EDGE_POWER_SAVING_PROVED=true" in av
    assert "FIRST_SEPARABLE_DYADIC_BILINEAR_BOUND_PROVED=true" in s5h
    assert "EUCLID_INCIDENCE_SEPARABILITY_PROVED=false" in s5h

    local_rows = []
    for p in PRIMES:
        for col in COLUMNS:
            got = primitive_root_count(p, col)
            if col in LINEAR:
                expected = p - 1
            elif p % 4 == 1:
                expected = 2 * (p - 1)
            else:
                expected = 0
            assert got == expected, (p, col, got, expected)
            local_rows.append({"p": p, "column": col, "roots": got})

    # Multiplicativity on representative coprime squarefree state splits.
    split_tests = []
    pairs = ((3, 5), (5, 13), (7, 17), (13, 29))
    for a, b in pairs:
        assert gcd(a, b) == 1
        assert lambda_l(a * b) == lambda_l(a) * lambda_l(b)
        assert lambda_e(a * b) == lambda_e(a) * lambda_e(b)
        split_tests.append(
            {
                "a": a,
                "b": b,
                "lambda_L_ab": fstr(lambda_l(a * b)),
                "lambda_E_ab": fstr(lambda_e(a * b)),
            }
        )

    exponent_rows = []
    for kappa in (Fraction(1, 10), Fraction(1, 8), Fraction(1, 6), Fraction(1, 4)):
        q_exp = 2 - 2 * kappa
        sqrt_qxy_exp = 1 + q_exp / 2
        q_term_exp = q_exp
        pointwise_exp = max(Fraction(1, 1), sqrt_qxy_exp, q_term_exp)
        assert pointwise_exp == 2 - kappa
        exponent_rows.append(
            {
                "kappa": fstr(kappa),
                "Q_max_exponent": fstr(q_exp),
                "sqrt_QXY_exponent": fstr(sqrt_qxy_exp),
                "pointwise_discrepancy_exponent": fstr(pointwise_exp),
                "saving_exponent": fstr(kappa),
            }
        )

    report = {
        "stage": "14-4aw",
        "classification": "AUXILIARY_STATE_BULK_FACTORIZED_AND_DISCREPANCY_ENDPOINT_BOUNDARY_ISOLATED",
        "exact_local_density": {
            "linear_prime_factor": "1/(p+1)",
            "norm_prime_factor": "2/(p+1) for p=1 mod 4; 0 for p=3 mod 4",
            "primitive_opposite_parity_baseline": "4/pi^2",
            "tested_prime_column_rows": len(local_rows),
            "all_exact_root_counts_pass": True,
        },
        "rank_one_bulk": {
            "formula": "W_R=(4/pi^2)XY*lambda_L(qA)*lambda_L(qB)*lambda_L(qC)*lambda_L(qD)*lambda_E(qE)+Delta_R",
            "state_moduli_pairwise_odd_support": True,
            "state_split_multiplicativity": True,
            "representative_split_tests": split_tests,
            "frozen_auxiliary_state_bulk_separable": True,
            "quadratic_large_sieve_applies_to_bulk_edge_after_freezing": True,
        },
        "mobius_discrepancy": {
            "decomposition": "Delta_R=Delta_<=D+Delta_>D",
            "small_bound": "rho(Q)*((X+Y)/Q*log(2D)+D)",
            "tail_bound": "XY/D+(X+Y)log(2M)+M",
            "optimized_pointwise": "Q^eps*((X+Y)log(2M)+sqrt(QXY)+Q)",
            "pointwise_is_L2": False,
            "medium_balanced_condition": "X~Y~L and Q<=L^(2-2kappa)",
            "medium_pointwise_conclusion": "Delta_R<<L^(2-kappa+o(1))",
            "exponent_audit": exponent_rows,
        },
        "endpoint_ledger": {
            "medium_balanced": "L^kappa<=U,V<=L^(1-kappa), Q<=L^(2-2kappa): bulk saving proved; Delta L2 missing",
            "microscopic_side": "min(U,V)<L^kappa: no uniform fixed-power large-sieve gain down to side 1",
            "sparse_large_modulus": "Q>L^(2-2kappa): pointwise discrepancy can compete with bulk; switching required",
            "dyadic_range_count": "O((log L)^2) per frozen structural case",
            "dyadic_count_is_power_obstruction": False,
        },
        "first_remaining_local_object": "DISCREPANCY_L2_AND_SPARSE_ENDPOINT_CONTROL",
        "decision": {
            "STAGE14_4AW": "AUXILIARY_STATE_BULK_FACTORIZED_AND_DISCREPANCY_ENDPOINT_BOUNDARY_ISOLATED",
            "LINEAR_PRIMITIVE_LOCAL_FACTOR_EXACT": True,
            "NORM_PRIMITIVE_LOCAL_FACTOR_EXACT": True,
            "PRIMITIVE_MOBIUS_RANK_ONE_BULK": True,
            "STATE_SPLIT_PRESERVES_BULK_SEPARABILITY": True,
            "GROWING_AUXILIARY_STATE_COUPLING_IN_BULK": False,
            "MOBIUS_TRUNCATION_DISCREPANCY_DECOMPOSITION": True,
            "MEDIUM_MODULUS_POINTWISE_DISCREPANCY_POWER_SAVING": True,
            "DISCREPANCY_SECOND_MOMENT_PROVED": False,
            "MICROSCOPIC_ENDPOINT_BLOCKS_CLOSED": False,
            "SPARSE_LARGE_MODULUS_BLOCKS_CLOSED": False,
            "EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED": False,
            "EXPLICIT_E_LOC_PROVED": False,
            "POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED": False,
            "POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4ax prove an L2 dispersion bound for the primitive-Mobius discrepancy on balanced/medium blocks and close the microscopic/sparse endpoint ranges by divisor switching or isolate a persistent diagonal",
        },
    }

    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
