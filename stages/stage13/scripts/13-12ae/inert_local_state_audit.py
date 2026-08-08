#!/usr/bin/env python3
"""Stage13-12ae exact inert-prime local-state audit.

The theorem proof is in stages/stage13/13-12ae/result.md. This script checks all
inert primes below 200 but stores only aggregate validation, keeping the
committed report compact. Finite enumeration is diagnostic, not the proof of
the fixed-conductor residue transfer.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

OUT = Path("stages/stage13/data/13-12ae/inert_local_state_audit_report.json")


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for q in range(2, math.isqrt(n) + 1):
        if n % q == 0:
            return False
    return True


def chi(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def circle(p: int) -> set[tuple[int, int]]:
    return {
        (x, y)
        for x in range(p)
        for y in range(p)
        if (x * x + y * y - 1) % p == 0
    }


def hyperbola(p: int) -> set[tuple[int, int]]:
    return {
        (z, d)
        for z in range(p)
        for d in range(p)
        if (d * d - z * z - 1) % p == 0
    }


def hyperbola_from_u(p: int) -> set[tuple[int, int]]:
    inv2 = pow(2, -1, p)
    out: set[tuple[int, int]] = set()
    for u in range(1, p):
        ui = pow(u, -1, p)
        out.add((((u - ui) * inv2) % p, ((u + ui) * inv2) % p))
    return out


def local_formula_row(p: int) -> dict:
    C = circle(p)
    H = hyperbola(p)
    Hparam = hyperbola_from_u(p)
    total = len(C) * len(H)
    accepted = 0
    char_sum = 0
    zero_count = 0
    for x, _y in C:
        for z, _d in H:
            a = (x * x + z * z) % p
            c = chi(a, p)
            char_sum += c
            zero_count += int(a == 0)
            accepted += int(c >= 0)

    unit_acceptance = Fraction(p + 1, 2 * (p - 1))
    unrestricted_local = Fraction(p + 1, p - 1)
    positive_mass = Fraction(2, p - 1)
    positive_fraction = Fraction(2, p + 1)
    constrained_local = Fraction(p + 5, 2 * (p - 1))
    lam = Fraction(p + 5, 2 * (p + 1))
    positive_state_failures = sum(chi(z * z, p) < 0 for z in range(1, p))

    passed = (
        len(C) == p + 1
        and len(H) == p - 1
        and Hparam == H
        and total == p * p - 1
        and accepted == (p + 1) * (p + 1) // 2
        and char_sum == 2 * (p - 1)
        and zero_count == 4
        and positive_state_failures == 0
        and unrestricted_local == 1 + positive_mass
        and positive_fraction == positive_mass / unrestricted_local
        and constrained_local == unit_acceptance + positive_mass
        and lam == constrained_local / unrestricted_local
    )
    return {
        "p": p,
        "pass": passed,
        "hyperbola_parameterization_bijective": Hparam == H,
        "positive_state_failures": positive_state_failures,
        "lambda_le_3_over_4": lam <= Fraction(3, 4),
    }


def build_report() -> dict:
    inert_primes = [p for p in range(3, 200) if is_prime(p) and p % 4 == 3]
    rows = [local_formula_row(p) for p in inert_primes]
    failures = [row["p"] for row in rows if not row["pass"]]
    if failures:
        raise ArithmeticError(f"inert local identity failures: {failures}")
    if not all(row["lambda_le_3_over_4"] for row in rows if row["p"] >= 7):
        raise ArithmeticError("lambda <= 3/4 failed for inert p>=7")

    state_table = [
        {"state": "U", "valuations": "(a,b,c)=(0,0,0)", "allowed": True,
         "reason": "unit outer state", "W_p": "nontrivial finite residue test"},
        {"state": "R_b", "valuations": "a=0,b>=1,c=0", "allowed": True,
         "reason": "gcd(r,s)=1 and z is a unit",
         "W_p": "automatic because x=y=0 mod p and z is a unit"},
        {"state": "S_c", "valuations": "a=0,b=0,c>=1", "allowed": True,
         "reason": "gcd(r,s)=1 and z is a unit",
         "W_p": "automatic because x=y=0 mod p and z is a unit"},
        {"state": "H_positive", "valuations": "a>=1", "allowed": False,
         "reason": "inert p|h forces p|x,y,z, contradicting primitive gcd=1",
         "W_p": "not applicable"},
        {"state": "both_base_positive", "valuations": "b>=1,c>=1", "allowed": False,
         "reason": "forbidden by gcd(r,s)=1", "W_p": "not applicable"},
    ]

    return {
        "metadata": {
            "stage": "13-12ae",
            "scope": "exact inert-prime local factor, positive-valuation tail, and complete local-state audit",
            "proof_location": "stages/stage13/13-12ae/result.md",
            "finite_enumeration_is_proof": False,
        },
        "review_targets": {
            "grok_positive_valuation_tail": "repaired exactly",
            "qwen_positive_valuation_tail": "repaired exactly",
            "grok_local_state_completeness": "repaired by complete valuation table plus fixed residue transfer",
        },
        "exact_formulas": {
            "inert_h_factor": "1",
            "unrestricted_local_series": "1 + sum_{b>=1}Y^b + sum_{c>=1}Z^c = (1-YZ)/((1-Y)(1-Z))",
            "L_p_at_1_1_1": "(p+1)/(p-1)",
            "positive_valuation_mass": "2/(p-1)",
            "positive_valuation_fraction": "2/(p+1) <= 2/p",
            "absolute_C0": 2,
            "unit_acceptance": "(p+1)/(2(p-1))",
            "constrained_local": "(p+5)/(2(p-1))",
            "lambda_p": "(p+5)/(2(p+1)) = 1/2 + 2/(p+1)",
            "lambda_le_3_over_4_for_inert_p_ge_7": True,
            "explicit_p0_if_condition_is_p_gt_p0": 3,
        },
        "state_table": state_table,
        "fixed_residue_transfer": {
            "p_fixed_before_B_limit": True,
            "unit_state_space": "circle X^2+Y^2=1 times hyperbola D^2-Z^2=1",
            "hyperbola_parameter": "u=s/r -> (Z,D)=((u-u^-1)/2,(u+u^-1)/2)",
            "rational_unit_residues": "finite Dirichlet-character orthogonality",
            "gaussian_unit_residues": "fixed-conductor Gaussian ray-class character orthogonality",
            "principal_tuple": "reproduces untwisted zero-mode pole and local density",
            "nonprincipal_tuples": "lower order because at least one principal pole is removed",
            "growing_modulus_used": False,
            "OE_EE_dependency": "none at odd p; finite 2-adic factor cancels from local ratio",
        },
        "tagging": {
            "pair_overlap_injects_into_tagged_union": True,
            "two_tag_factor": "harmless upper multiplicity 2; enlarges the upper bound",
        },
        "validation": {
            "inert_primes_checked_below_200": len(rows),
            "failures": failures,
            "all_hyperbola_parameterizations_bijective": all(row["hyperbola_parameterization_bijective"] for row in rows),
            "all_positive_states_automatic": all(row["positive_state_failures"] == 0 for row in rows),
            "all_lambda_formulae_pass": all(row["pass"] for row in rows),
        },
        "status": {
            "STAGE13_12AE": "COMPLETE_EXACT_PADIC_LOCAL_CLOSURE",
            "P_ADIC_POSITIVE_VALUATION_TAIL": "REPAIRED_EXACTLY",
            "P_ADIC_ABSOLUTE_C0": 2,
            "LOCAL_STATE_REFINEMENT_COMPLETENESS": "REPAIRED",
            "PAIR_OVERLAP_LOWER_ORDER": "RESTORED_WITH_EXACT_LOCAL_FACTOR",
            "TRIPLE_OVERLAP_LOWER_ORDER": "RESTORED_WITH_EXACT_LOCAL_FACTOR",
            "EXACT_ONE_DIRECTIONAL_ASYMPTOTIC": "R03_CANDIDATE",
            "STAGE13_GLOBAL_REVIEW_STATUS": "PENDING_EXTERNAL_R03",
            "NEXT": "Stage13-12af",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
