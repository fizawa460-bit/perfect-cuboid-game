#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LEMMA = ROOT / "stages/stage13/13-13fb/wiener-bound-lemma.md"
REPORT = ROOT / "stages/stage13/data/13-13fb/wiener_bound_audit.json"


def fstr(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def build_report() -> dict:
    lemma = LEMMA.read_text(encoding="utf-8")

    # Tail p>=13: rho <= 1/4.
    a = Fraction(8, 3)
    b = Fraction(44, 9)
    m = Fraction(32, 9)
    ainv = Fraction(5, 3)
    binv = Fraction(25, 12)

    term_2m = 2 * m
    term_2ab = 2 * a * b
    term_b2 = b * b
    term_ab2 = a * b * b * Fraction(1, 4)  # rho^3 <= (1/4) rho^2
    e_bound = term_2m + term_2ab + term_b2 + term_ab2
    exact_constant = e_bound * ainv * binv * binv

    # Exceptional split prime p=5: rho_5 < 3/8.
    a5 = Fraction(6, 5)
    b5 = Fraction(63, 25)
    m5 = Fraction(18, 25)
    ainv5 = Fraction(11, 5)
    binv5 = Fraction(121, 40)
    e5 = 2 * m5 + 2 * a5 * b5 + b5 * b5 + a5 * b5 * b5
    c5 = e5 * ainv5 * binv5 * binv5

    required_tokens = [
        "A_\\vartheta(x)=\\frac{1-x^2}{1-2cx+x^2}",
        "B_\\vartheta(y)=\\frac{1+y}{1-2cy+y^2}",
        "C_{\\ell,p}(s_h,s_r,s_s)",
        "E_\\vartheta",
        "\\frac{17744}{243}",
        "\\frac{3465625}{6561}",
        "529p^{-5/4}",
        "p=5",
        "431.99676036",
        "PHASE_UNIFORM=true",
        "NEXT=13-13fc",
    ]
    missing_tokens = [token for token in required_tokens if token not in lemma]

    checks = {
        "rho_13_lt_quarter": 4**8 < 13**5,
        "tail_axis_constants": (
            a == Fraction(8, 3)
            and b == Fraction(44, 9)
            and m == Fraction(32, 9)
        ),
        "tail_error_terms": (
            term_2m == Fraction(64, 9)
            and term_2ab == Fraction(704, 27)
            and term_b2 == Fraction(1936, 81)
            and term_ab2 == Fraction(3872, 243)
        ),
        "tail_error_bound": e_bound == Fraction(17744, 243),
        "inverse_constants": ainv == Fraction(5, 3) and binv == Fraction(25, 12),
        "exact_constant": exact_constant == Fraction(3465625, 6561),
        "rounded_529_valid": exact_constant < 529,
        "wiener_exponent": 2 * Fraction(5, 8) == Fraction(5, 4),
        "rho_5_lt_three_eighths": 8**8 < 3**8 * 5**5,
        "p5_error_bound": e5 == Fraction(67059, 3125),
        "p5_constant": c5 == Fraction(10799919009, 25000000),
        "p5_lt_432": c5 < 432,
        "lemma_contract_tokens": not missing_tokens,
    }

    return {
        "stage": "13-13fb",
        "purpose": "deterministic algebra/constant consistency audit for the explicit Wiener lemma",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "tail": {
            "sigma": "5/8",
            "rho_majorant": "1/4",
            "a_bound_coefficient": fstr(a),
            "b_bound_coefficient": fstr(b),
            "m_bound_coefficient": fstr(m),
            "A_inverse_bound": fstr(ainv),
            "B_inverse_bound": fstr(binv),
            "E_terms": [fstr(term_2m), fstr(term_2ab), fstr(term_b2), fstr(term_ab2)],
            "E_bound": fstr(e_bound),
            "exact_constant": fstr(exact_constant),
            "exact_constant_decimal": float(exact_constant),
            "rounded_constant": 529,
            "prime_exponent": "5/4",
        },
        "p5": {
            "rho_majorant": "3/8",
            "a_bound": fstr(a5),
            "b_bound": fstr(b5),
            "m_bound": fstr(m5),
            "A_inverse_bound": fstr(ainv5),
            "B_inverse_bound": fstr(binv5),
            "E_bound": fstr(e5),
            "C_minus_1_bound": fstr(c5),
            "C_minus_1_bound_decimal": float(c5),
            "integer_majorant": 432,
        },
        "missing_lemma_tokens": missing_tokens,
        "scope": {
            "mathematical_role": "reproducibility/consistency check; the written lemma carries the proof",
            "phase_uniform": True,
            "retained_harmonic_uniform": True,
            "theorem_changed": False,
            "theorem_contract_reopen_required": False,
            "next": "13-13fc",
        },
    }


def canonical_json(data: dict) -> str:
    return json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true")
    parser.add_argument("--check-report", action="store_true")
    args = parser.parse_args()

    report = build_report()
    text = canonical_json(report)

    if args.write_report:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(text, encoding="utf-8")

    if args.check_report:
        if not REPORT.exists():
            print("missing committed report:", REPORT)
            return 2
        if REPORT.read_text(encoding="utf-8") != text:
            print("committed report is stale; regenerate with --write-report")
            return 3

    print(text, end="")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
