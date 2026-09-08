#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b3b3b_classify_20_novel_carriers_and_unify_27 as b3b3b

HERE = Path(__file__).resolve().parent
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
B3B3B = HERE / "e3-v91c1x-r5b3b3b-classify-20-novel-carriers-and-unify-27.json"
OUT = HERE / "e3-v91c1x-r5b3b3c1-modular-irreducibility-scratch.json"
B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
B3B3B_SHA = "7f52f0988cb82983afc0759272e2420e73944b4258940aeffc8a9923816c4a7d"
PRIMES = (5, 13, 17, 29, 37)
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def mod_factor_pattern(zpoly: sp.Poly, p: int):
    mp = sp.Poly(zpoly.as_expr(), *b3b3b.BASE, modulus=p)
    if mp.is_zero or mp.total_degree() != 16:
        return {"prime": p, "usable": False, "reason": "DEGREE_DROP_OR_ZERO"}
    coeff, factors = sp.factor_list(mp.as_expr(), *b3b3b.BASE, modulus=p)
    pattern = sorted([int(sp.Poly(f, *b3b3b.BASE, modulus=p).total_degree()) for f, m in factors for _ in range(int(m))])
    irreducible = len(factors) == 1 and int(factors[0][1]) == 1 and pattern == [16]
    return {
        "prime": p,
        "usable": True,
        "factor_degree_multiset": pattern,
        "distinct_factor_count": len(factors),
        "irreducible_mod_p": irreducible,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    b3b2 = b3b3b.load(B3B2, B3B2_SHA)
    b3 = b3b3b.load(B3B3B, B3B3B_SHA)
    rows = {r["carrier_id"]: r for r in b3b2["finite_linear_carrier_inventory"]["carrier_rows"]}
    cls = b3["unified_27_classification"]
    off_ids = list(cls["off_boundary_carrier_ids"])
    novel_meta = {r["carrier_id"]: r for r in b3["novel_20_exact_norm_classification"]["carrier_rows"]}
    if len(off_ids) != 20:
        raise SystemExit("expected exactly 20 off-boundary carriers")

    out_rows = []
    for index, cid in enumerate(off_ids, 1):
        row = rows[cid]
        poly = b3b3b.full_sign_norm_poly(row["normalized_coefficients_Qi"])
        coeffs_rational = all(c.is_Rational is True for c in poly.coeffs())
        print(f"[{index:02d}/20] {cid} degree={poly.total_degree()} rational={coeffs_rational}", flush=True)
        if not coeffs_rational:
            out_rows.append({
                "carrier_id": cid,
                "normalized_full_sign_norm_sha256": novel_meta[cid]["normalized_full_sign_norm_sha256"],
                "all_norm_coefficients_rational": False,
                "qi_irreducibility_witness_prime": None,
                "prime_trials": [],
            })
            continue
        qpoly = sp.Poly(poly.as_expr(), *b3b3b.BASE, domain=sp.QQ)
        _, zpoly = qpoly.clear_denoms(convert=True)
        trials = []
        witness = None
        for p in PRIMES:
            trial = mod_factor_pattern(zpoly, p)
            trials.append(trial)
            print(f"  p={p}: {trial.get('factor_degree_multiset')} irr={trial.get('irreducible_mod_p')}", flush=True)
            if trial.get("irreducible_mod_p"):
                witness = p
                break
        out_rows.append({
            "carrier_id": cid,
            "normalized_full_sign_norm_sha256": novel_meta[cid]["normalized_full_sign_norm_sha256"],
            "all_norm_coefficients_rational": True,
            "integer_content_primitive_after_clear_denoms": int(sp.gcd_list([int(c) for c in zpoly.coeffs()])) in (-1, 1),
            "qi_irreducibility_witness_prime": witness,
            "prime_trials": trials,
        })

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c1.modular_irreducibility_scratch.v1",
        "stage": "33-12",
        "role": "SCRATCH_NONCREDIT_FINITE_FIELD_IRREDUCIBILITY_WITNESS_DIAGNOSTIC",
        "entry": {"pr": 1695, "authority": AUTHORITY, "stage33_progress": "6/11"},
        "source_locks": {
            "r5b3b2_sha256": B3B2_SHA,
            "r5b3b3b_sha256": B3B3B_SHA,
        },
        "mathematical_scope": {
            "tested_primes_split_in_Qi": list(PRIMES),
            "witness_rule": "FOR_A_PRIMITIVE_RATIONAL_NORM_POLYNOMIAL_A_DEGREE_PRESERVING_IRREDUCIBLE_REDUCTION_AT_P_CONGRUENT_1_MOD_4_IS_A_SUFFICIENT_IRREDUCIBILITY_WITNESS_OVER_Q(i)",
            "diagnostic_only_until_CONSOLIDATED_WITH_EXACT_SOURCE_AND_FIREWALL_CHECKS": True,
        },
        "result": {
            "off_boundary_count": len(out_rows),
            "all_norm_coefficients_rational": all(r["all_norm_coefficients_rational"] for r in out_rows),
            "witnessed_irreducible_over_Qi_count": sum(r["qi_irreducibility_witness_prime"] is not None for r in out_rows),
            "unwitnessed_carrier_ids": [r["carrier_id"] for r in out_rows if r["qi_irreducibility_witness_prime"] is None],
            "carrier_rows": out_rows,
        },
        "credit_firewall": {
            "authority_promotion": False,
            "hostile_audit_credit": False,
            "offboundary_norm_irreducible_factorization_materialized": False,
            "resolved_surface_prime_decomposition_credit": False,
            "combined_tame_residue_credit": False,
            "stage33_close_credit": False,
            "merge_allowed": False,
        },
    }
    body = dict(cert)
    cert["canonical_sha256"] = csha(body)
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
