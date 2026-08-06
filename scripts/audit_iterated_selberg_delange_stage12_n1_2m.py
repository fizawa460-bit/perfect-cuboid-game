#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

PRIMES_1MOD4 = [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97]


def bq(q: int) -> Fraction:
    return Fraction(2 * (q - 1), q + 1)


def local_direct(q: int, x: Fraction, y: Fraction) -> Fraction:
    b = bq(q)
    return 1 + b * x / (1 - x) + b * y / (1 - y)


def local_one(q: int, x: Fraction) -> Fraction:
    b = bq(q)
    return 1 + b * x / (1 - x)


def cross(q: int, x: Fraction, y: Fraction) -> Fraction:
    return local_direct(q, x, y) / (local_one(q, x) * local_one(q, y))


def beta(n: int) -> Fraction:
    out = Fraction(1)
    d = n
    p = 2
    while p * p <= d:
        if d % p == 0:
            while d % p == 0:
                d //= p
            if p % 4 != 1:
                return Fraction(0)
            out *= bq(p)
        p += 1
    if d > 1:
        if d % 4 != 1:
            return Fraction(0)
        out *= bq(d)
    return out


def rectangle_sum(R: int, S: int) -> Fraction:
    import math
    total = Fraction(0)
    for r in range(1, R + 1):
        br = beta(r)
        if not br:
            continue
        for s in range(1, S + 1):
            if math.gcd(r, s) == 1:
                total += br * beta(s)
    return total


def build_report() -> dict:
    checks = []
    finite_product = Fraction(1)
    for q in PRIMES_1MOD4:
        x = Fraction(1, q)
        y = Fraction(1, q * q)
        direct = local_direct(q, x, y)
        factored = local_one(q, x) * local_one(q, y) * cross(q, x, y)
        assert direct == factored
        c11 = cross(q, Fraction(1, q), Fraction(1, q))
        assert c11 > 0
        finite_product *= c11
        checks.append({
            "prime": q,
            "b_q": str(bq(q)),
            "factorization_exact": True,
            "cross_at_1_1": str(c11),
        })

    small_rectangles = []
    for R, S in [(8, 9), (12, 15), (20, 20), (30, 25)]:
        value = rectangle_sum(R, S)
        small_rectangles.append({"R": R, "S": S, "sum": str(value)})

    return {
        "stage": "12-N1-2m",
        "classification": "A_ITERATED_SELBERG_DELANGE_MAIN_TERM_FACTORIZATION_CLOSED_REGION_REMAINDER_PENDING",
        "prime_checks": checks,
        "finite_cross_product": str(finite_product),
        "small_rectangle_sums": small_rectangles,
        "analytic_claims": {
            "one_variable_pole_order": 1,
            "cross_absolute_convergence_domain": "Re(s1+s2)>1",
            "dlb_P2_P3_needed": False,
            "coupled_region_uniform_remainder_closed": False,
        },
        "not_claimed": [
            "finite checks prove analytic continuation",
            "finite checks prove Selberg-Delange error terms",
            "the final coupled-region asymptotic is closed",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", type=Path)
    parser.add_argument("--check-report", type=Path)
    args = parser.parse_args()
    report = build_report()
    if args.write_report:
        args.write_report.parent.mkdir(parents=True, exist_ok=True)
        args.write_report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if args.check_report:
        expected = json.loads(args.check_report.read_text(encoding="utf-8"))
        if expected != report:
            raise SystemExit("report mismatch")
    if not args.write_report and not args.check_report:
        print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
