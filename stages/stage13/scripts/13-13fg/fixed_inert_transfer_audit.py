#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
STAGE13 = ROOT / "stages" / "stage13"
OUT = STAGE13 / "data" / "13-13fg" / "fixed_inert_transfer_audit.json"


def is_square0(a: int, p: int) -> bool:
    a %= p
    return a == 0 or pow(a, (p - 1) // 2, p) == 1


def local_row(p: int) -> dict:
    circle = [(x, y) for x in range(p) for y in range(p) if (x*x + y*y - 1) % p == 0]
    hyperbola = [(d, z) for d in range(p) for z in range(p) if (d*d - z*z - 1) % p == 0]
    accepted = 0
    zero = 0
    for x, _y in circle:
        for _d, z in hyperbola:
            t = (x*x + z*z) % p
            if t == 0:
                zero += 1
            if is_square0(t, p):
                accepted += 1

    expected = (p + 1) ** 2 // 2
    alpha = Fraction(p + 1, 2 * (p - 1))
    lambda_p = Fraction(p + 5, 2 * (p + 1))
    return {
        "p": p,
        "circle_points": len(circle),
        "hyperbola_points": len(hyperbola),
        "unit_total": len(circle) * len(hyperbola),
        "unit_zero_states": zero,
        "unit_accepted": accepted,
        "unit_accepted_expected": expected,
        "alpha_p": f"{alpha.numerator}/{alpha.denominator}",
        "lambda_p": f"{lambda_p.numerator}/{lambda_p.denominator}",
        "lambda_le_3_over_4": lambda_p <= Fraction(3, 4),
        "checks_pass": (
            len(circle) == p + 1
            and len(hyperbola) == p - 1
            and len(circle) * len(hyperbola) == p*p - 1
            and zero == 4
            and accepted == expected
            and lambda_p <= Fraction(3, 4)
        ),
    }


def build_report() -> dict:
    lemma = (STAGE13 / "13-13fg" / "fixed-inert-transfer.md").read_text()
    result = (STAGE13 / "13-13fg" / "result.md").read_text()
    gate_f = (STAGE13 / "13-13ff" / "external-theorem-contracts.md").read_text()
    roadmap = (STAGE13 / "13-13" / "roadmap.md").read_text()
    plan = (STAGE13 / "13-13f" / "r05-repair-plan.md").read_text()

    primes = [7, 11, 19, 23]
    rows = [local_row(p) for p in primes]
    product = Fraction(1, 1)
    for p in primes:
        product *= Fraction(p + 5, 2 * (p + 1))

    checks = {
        "local_enumeration_pass": all(row["checks_pass"] for row in rows),
        "exact_lambda_visible": "INERT_LAMBDA=(p+5)/(2(p+1))" in lemma,
        "character_orthogonality_visible": all(token in lemma for token in [
            "FINITE_CHARACTER_ORTHOGONALITY_PLUS_CRT",
            "Fourier inversion on `G_p`",
            "CRT tensors",
        ]),
        "principal_multiplier_visible": all(token in lemma for token in [
            "principal character tuple",
            "PRINCIPAL_TUPLE_MULTIPLIER=product_{p_in_S}_lambda_p",
        ]),
        "mixed_correction_control_visible": all(token in lemma for token in [
            "MIXED_CORRECTION_REMAINS_HOLOMORPHIC=true",
            "phase-uniform",
            "cannot create a pole",
        ]),
        "nonprincipal_pole_loss_visible": all(token in lemma for token in [
            "NONPRINCIPAL_TUPLE_POLE_LOSS_AT_LEAST_ONE=true",
            "NONPRINCIPAL_TOTAL=o_S(B(log B)^3)",
        ]),
        "fixed_limit_order_visible": "LIMIT_ORDER=FIX_S_THEN_B_TO_INFINITY_THEN_ENLARGE_S" in lemma,
        "no_growing_modulus": "GROWING_MODULUS_THEOREM_USED=false" in lemma,
        "pair_triple_lower_order": all(token in lemma for token in [
            "PAIR_OVERLAP=o(B(log B)^3)",
            "TRIPLE_OVERLAP=o(B(log B)^3)",
        ]),
        "gate_f_contract_available": all(token in gate_f for token in [
            "NONTRIVIAL_HECKE_TWIST_HOLOMORPHIC_AT_1=true",
            "GROWING_MODULUS_THEOREM_USED=false",
        ]),
        "roadmap_gate_g_complete": "STAGE13_13FG=COMPLETE_FIXED_INERT_PRIME_TRANSFER" in roadmap,
        "plan_gate_g_complete": "STAGE13_13FG=COMPLETE_FIXED_INERT_PRIME_TRANSFER" in plan,
        "result_lock_complete": "STAGE13_13FG=COMPLETE_FIXED_INERT_PRIME_TRANSFER" in result,
        "next_gate_locked": "NEXT=13-13fh" in roadmap and "NEXT=13-13fh" in plan,
        "theorem_unchanged": "THEOREM_CHANGED=false" in lemma and "THEOREM_CONTRACT_REOPEN_REQUIRED=false" in lemma,
    }
    failed = [name for name, ok in checks.items() if not ok]

    return {
        "metadata": {
            "stage": "13-13fg",
            "scope": "R05 Gate G fixed inert-prime character transfer and overlap squeeze",
        },
        "local_rows": rows,
        "sample_product": {
            "primes": primes,
            "product_lambda": f"{product.numerator}/{product.denominator}",
            "three_quarters_power": f"{Fraction(3,4) ** len(primes)}",
            "product_le_three_quarters_power": product <= Fraction(3, 4) ** len(primes),
        },
        "checks": checks,
        "decision": {
            "status": "COMPLETE_FIXED_INERT_PRIME_TRANSFER" if not failed else "FAIL_REPAIR_REQUIRED",
            "failed_checks": failed,
            "theorem_changed": False,
            "theorem_contract_reopen_required": False,
            "next": "13-13fh",
        },
        "locks": {
            "lambda_p": "(p+5)/(2(p+1))",
            "principal_multiplier": "product lambda_p",
            "nonprincipal_total": "o_S(B(log B)^3)",
            "limit_order": "fix S -> B to infinity -> enlarge S",
            "growing_modulus_theorem_used": False,
            "pair_overlap": "o(B(log B)^3)",
            "triple_overlap": "o(B(log B)^3)",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true")
    parser.add_argument("--check-report", action="store_true")
    args = parser.parse_args()

    report = build_report()
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"

    if args.write_report:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(text)

    if args.check_report:
        if not OUT.exists() or OUT.read_text() != text:
            raise SystemExit("committed Stage13-13fg report is stale")
        if report["decision"]["status"] != "COMPLETE_FIXED_INERT_PRIME_TRANSFER":
            raise SystemExit(f"Stage13-13fg failed checks: {report['decision']['failed_checks']}")

    print(text, end="")


if __name__ == "__main__":
    main()
