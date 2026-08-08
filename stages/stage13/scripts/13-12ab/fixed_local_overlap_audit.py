#!/usr/bin/env python3
"""Stage13-12ab audit for the fixed-local overlap repair.

The theorem proof is in stages/stage13/13-12ab/result.md.  This script checks
the explicit finite-field part and records the fixed-set squeeze ledger.  It
does not pretend that finite enumeration proves the global Euler-factor
replacement lemma; that analytic step is written in result.md.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

OUT = Path("stages/stage13/data/13-12ab/fixed_local_overlap_audit_report.json")


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


def normalized_counts(p: int) -> tuple[int, int, int]:
    circle = [
        (x, y)
        for x in range(p)
        for y in range(p)
        if (x * x + y * y - 1) % p == 0
    ]
    hyperbola = [
        (z, d)
        for z in range(p)
        for d in range(p)
        if (d * d - z * z - 1) % p == 0
    ]
    total = len(circle) * len(hyperbola)
    accepted = 0
    char_sum = 0
    for x, _y in circle:
        for z, _d in hyperbola:
            a = (x * x + z * z) % p
            c = chi(a, p)
            char_sum += c
            accepted += int(c >= 0)
    return total, accepted, char_sum


def affine_counts(p: int, normalized_total: int, normalized_accepted: int) -> tuple[int, int]:
    # P != 0: scale the P=1 count by p-1.
    # P = 0 and primitive: inertness forces x=y=0, while d=+-z and z!=0.
    p_nonzero_total = (p - 1) * normalized_total
    p_nonzero_accepted = (p - 1) * normalized_accepted
    p_zero_primitive = 2 * p - 2
    return (
        p_nonzero_total + p_zero_primitive,
        p_nonzero_accepted + p_zero_primitive,
    )


def local_rows() -> list[dict]:
    rows = []
    for p in range(3, 80):
        if not is_prime(p) or p % 4 != 3:
            continue
        nt, na, cs = normalized_counts(p)
        at, aa = affine_counts(p, nt, na)
        expected_nt = p * p - 1
        expected_na = (p + 1) * (p + 1) // 2
        expected_cs = 2 * (p - 1)
        expected_at = (p - 1) * (p * p + 1)
        expected_aa = (p - 1) * (p * p + 2 * p + 5) // 2
        unit_ratio = na / nt
        affine_ratio = aa / at
        rows.append({
            "p": p,
            "normalized_total": nt,
            "normalized_accepted": na,
            "normalized_character_sum": cs,
            "expected_normalized_total": expected_nt,
            "expected_normalized_accepted": expected_na,
            "expected_character_sum": expected_cs,
            "unit_acceptance": unit_ratio,
            "unit_acceptance_formula": (p + 1) / (2 * (p - 1)),
            "primitive_affine_total": at,
            "primitive_affine_accepted": aa,
            "expected_primitive_affine_total": expected_at,
            "expected_primitive_affine_accepted": expected_aa,
            "primitive_affine_acceptance": affine_ratio,
            "primitive_affine_acceptance_formula": (p * p + 2 * p + 5) / (2 * (p * p + 1)),
            "affine_below_two_thirds": affine_ratio < 2 / 3 if p >= 11 else None,
            "pass": (
                nt == expected_nt
                and na == expected_na
                and cs == expected_cs
                and at == expected_at
                and aa == expected_aa
            ),
        })
    return rows


def build_report() -> dict:
    rows = local_rows()
    failures = sum(not row["pass"] for row in rows)
    inert_ge_11 = [row for row in rows if row["p"] >= 11]
    if failures:
        raise ArithmeticError("finite-field identity failure")
    if not all(row["affine_below_two_thirds"] for row in inert_ge_11):
        raise ArithmeticError("expected <2/3 affine diagnostic failed")

    squeeze = [
        {
            "k": k,
            "upper_factor_if_lambda_le_3_over_4": (3.0 / 4.0) ** k,
        }
        for k in (1, 2, 4, 8, 16, 32)
    ]

    return {
        "metadata": {
            "stage": "13-12ab",
            "scope": "fixed-local overlap transfer audit and inert-prime finite-field validator",
        },
        "review_issue": {
            "old_7jf_fixed_modulus_transfer_accepted_without_repair": False,
            "repair": (
                "Refine the 13-12aa p-local state by finite unit residues; a fixed local "
                "condition replaces exactly one Euler factor. For fixed S, the global "
                "series is multiplied by a finite product of analytic local quotients."
            ),
        },
        "fixed_local_factor_lemma": {
            "identity": "D_ell,S = D_ell * product_{p in S}(L^W_p,ell/L_p,ell)",
            "S_fixed_before_B_limit": True,
            "growing_modulus_used": False,
            "zero_mode_pole_order_unchanged": True,
            "nonzero_harmonic_new_zeta_pole_created": False,
            "category_kernel_changed": False,
            "proof_location": "stages/stage13/13-12ab/result.md",
        },
        "local_test": {
            "condition": "x^2+z^2 in QR_0(F_p)",
            "necessary_for_second_integral_face": True,
            "prime_family": "p=3 mod 4",
            "unit_stratum_acceptance": "(p+1)/(2(p-1)) = 1/2 + 1/(p-1)",
            "positive_valuation_tail": "O(1/p) with absolute constant from the fixed-degree local coefficient majorant",
            "full_local_acceptance": "lambda_p <= 1/2 + O(1/p)",
            "consequence": "exists p0 with lambda_p <= 3/4 for every inert p>p0",
        },
        "finite_field_checks": {
            "checked_inert_primes_below_80": len(rows),
            "failures": failures,
            "rows": rows,
        },
        "fixed_set_squeeze": {
            "pair_limsup": "limsup O_qr/(B log^3 B) <= 2 D_q (3/4)^k for every fixed k",
            "order_of_limits": "first B->infinity with S_k fixed; only then k->infinity",
            "factors": squeeze,
            "pair_overlap_lower_order": True,
            "triple_overlap_lower_order": True,
        },
        "exact_one_transfer": {
            "raw_input": "Stage13-12aa non-circular A_q ~ kappa I_q/(3 pi^3) B(log B)^3",
            "result": "N_q ~ kappa I_q/(3 pi^3) B(log B)^3",
            "total": "N1 ~ kappa/(24 pi) B(log B)^3",
            "normalized_limit_restored": True,
        },
        "status": {
            "claude_major_fixed_modulus_transfer_repaired": True,
            "pair_overlap_lower_order_restored": True,
            "triple_overlap_lower_order_restored": True,
            "exact_one_directional_asymptotic_restored": True,
            "stage13_repair_chain_complete": True,
            "stage13_external_review_status": "PENDING_EXTERNAL_R02",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
