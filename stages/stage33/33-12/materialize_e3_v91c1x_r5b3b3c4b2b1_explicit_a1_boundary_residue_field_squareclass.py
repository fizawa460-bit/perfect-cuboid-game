#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as atlas
import materialize_e3_v91c1x_r5b3b3c4b1_exceptional_p1_targeted_residue_field_squareclass as b1mod

HERE = Path(__file__).resolve().parent
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
C2C = HERE / "e3-v91c1x-r5b3b3c2c-orbit-representative-strict-prime-decomposition-and-transport.json"
C4A = HERE / "e3-v91c1x-r5b3b3c4a-tame-residue-parity-and-cross-carrier-preflight.json"
B2A = HERE / "e3-v91c1x-r5b3b3c4b2a-strict-prime-cross-carrier-geometric-incidence.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b2b1-explicit-a1-boundary-residue-field-squareclass.json"

B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
C2C_SHA = "01fc321272106a1ce7c382783c4dcb128c164d21ee4deedf4060137ef9ed971a"
C4A_SHA = "fab3f7b1235370a3916b99b6909cd6c6363193ff271ee6b51cb9494b0668e525"
B2A_SHA = "ae207b31329f8248859dc96893243c4259e4d92d05beda1df8e65f2aac290d33"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
A1_FACTOR = "44afff33ba591a11904229fe7936cb41caa700bd759cda0a5106218250561491"
SPECIAL = ["LIN_008", "LIN_015", "LIN_020", "LIN_025"]
I = sp.I


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"canonical source lock moved {path.name}: claimed={claimed} actual={actual} expected={expected}")
    return obj


def clean(x):
    return sp.cancel(sp.expand(x))


def encode_rational_function(expr, vars_):
    expr = clean(expr)
    num, den = sp.fraction(expr)
    return {
        "numerator": atlas.encode_poly(num, vars_),
        "denominator": atlas.encode_poly(den, vars_),
    }


def build_certificate() -> dict:
    b3b2 = load_locked(B3B2, B3B2_SHA)
    c2c = load_locked(C2C, C2C_SHA)
    c4a = load_locked(C4A, C4A_SHA)
    b2a = load_locked(B2A, B2A_SHA)
    if b2a["next_exact_leaf"] != "V91C1X_R5B3B3C4B2B_STRICT_PRIME_TARGETED_RESIDUE_FIELD_SQUARECLASS_REDUCTION":
        raise SystemExit("C4B2A handoff moved")
    if b2a["strict_prime_tame_parity_after_incidence"]["total_targeted_strict_prime_residue_field_squareclass_rows_for_C4B2B"] != 28:
        raise SystemExit("C4B2A target count moved")

    inv_rows = b3b2["finite_linear_carrier_inventory"]["carrier_rows"]
    inv = {r["carrier_id"]: r for r in inv_rows}
    coeffs = {
        cid: sp.Matrix([atlas.decode_element(z) for z in inv[cid]["normalized_coefficients_Qi"]])
        for cid in inv
    }

    c4a_rows = c4a["strict_prime_preflight"]["rows"]
    boundary_rows = {
        r["carrier_id"]: r
        for r in c4a_rows
        if r["c1_normalized_factor_sha256"] == A1_FACTOR
    }
    if sorted(boundary_rows) != SPECIAL:
        raise SystemExit(f"C4A a1-boundary context set moved: {sorted(boundary_rows)}")

    rep_rows = {r["carrier_id"]: r for r in c2c["representative_strict_prime_decompositions"]["rows"]}
    expected_boundary_generators = {
        "LIN_008": ["a1", "b2+(a3)", "b3+(a2)", "c-(b1)"],
        "LIN_015": ["a1", "b2-(a3)", "b3+(a2)", "c-(b1)"],
        "LIN_020": ["a1", "b2+(a3)", "b3-(a2)", "c-(b1)"],
        "LIN_025": ["a1", "b2-(a3)", "b3-(a2)", "c-(b1)"],
    }
    signs = {
        "LIN_008": (-1, -1),
        "LIN_015": (1, -1),
        "LIN_020": (-1, 1),
        "LIN_025": (1, 1),
    }
    for cid in SPECIAL:
        cert = rep_rows[cid]["special_reducible_norm_prime_decomposition_certificate"]
        boundary = cert["boundary_prime"]
        if boundary["ideal_generators_on_singular_surface"] != expected_boundary_generators[cid]:
            raise SystemExit(f"C2C boundary ideal moved: {cid}")
        if boundary["quotient_model"] != "Q(i)[a2,a3,b1]/(b1^2-a2^2-a3^2)" or not boundary["quotient_is_domain"]:
            raise SystemExit(f"C2C boundary quotient contract moved: {cid}")

    s, t = sp.symbols("s t")
    a2 = clean(s * (1 - t*t) / (1 + t*t))
    a3 = clean(s * (2*t) / (1 + t*t))
    if clean(s*s - a2*a2 - a3*a3) != 0:
        raise SystemExit("boundary conic parametrization moved off b1^2=a2^2+a3^2")

    vars7 = sp.symbols("a1 a2 a3 b1 b2 b3 c")
    rows = []
    for cid in SPECIAL:
        crow = boundary_rows[cid]
        odd_ids = list(crow["combined_tame_residue_odd_linear_carrier_ids_under_single_carrier_valuation"])
        if len(odd_ids) != 2 or crow["combined_tame_residue_carrier_parity_zero_under_single_carrier_valuation"]:
            raise SystemExit(f"C4A boundary odd-carrier pattern moved: {cid}: {odd_ids}")
        sb2, sb3 = signs[cid]
        subs = {
            vars7[0]: 0,
            vars7[1]: a2,
            vars7[2]: a3,
            vars7[3]: s,
            vars7[4]: sb2 * a3,
            vars7[5]: sb3 * a2,
            vars7[6]: s,
        }
        per_carrier = []
        expr = sp.Integer(1)
        for oid in odd_ids:
            L = sum(coeffs[oid][j] * vars7[j] for j in range(7))
            pull = clean(L.subs(subs))
            if pull == 0:
                raise SystemExit(f"odd carrier vanishes identically on target boundary prime: {cid}/{oid}")
            expr = clean(expr * pull)
            per_carrier.append({
                "carrier_id": oid,
                "boundary_pullback_Qi_s_t_sha256": csha(encode_rational_function(pull, [s, t])),
            })

        # Every row should reduce to a rational square times the same linear factor t+1.
        if cid == "LIN_015":
            root = clean(2 * I * s / (1 + t*t))
        elif cid in ("LIN_020", "LIN_025"):
            root = clean(2 * s * t / (1 + t*t))
        else:
            root = clean(2 * s / (1 + t*t))
        if clean(expr - root*root*(t + 1)) != 0:
            raise SystemExit(f"explicit boundary residue identity moved: {cid}: {sp.factor(expr)}")

        # Reuse the exact Q(i)[t] squareclass convention from C4B1 after discarding the explicit square root.
        sq = b1mod.poly_squareclass(t + 1, t)
        if sq["square_trivial"] or sq["odd_irreducible_factor_count"] != 1:
            raise SystemExit(f"t+1 unexpectedly square in Q(i)(t): {cid}")
        rows.append({
            "carrier_id": cid,
            "c1_factor_sha256": A1_FACTOR,
            "c4a_strict_prime_id": list(crow["strict_prime_ids"]),
            "c4a_odd_carrier_ids": odd_ids,
            "boundary_prime_ideal_generators": expected_boundary_generators[cid],
            "boundary_function_field_model": "Frac(Q(i)[a2,a3,b1]/(b1^2-a2^2-a3^2))",
            "birational_parameterization": {
                "b1": "s",
                "a2": "s*(1-t^2)/(1+t^2)",
                "a3": "2*s*t/(1+t^2)",
                "inverse_parameter_on_generic_chart": "t=a3/(b1+a2)",
            },
            "per_odd_carrier_pullbacks": per_carrier,
            "combined_residue_Qi_s_t_sha256": csha(encode_rational_function(expr, [s, t])),
            "explicit_identity": "combined_residue = square_root^2 * (t+1)",
            "square_root_Qi_s_t_sha256": csha(encode_rational_function(root, [s, t])),
            "residual_squareclass_representative": "t+1",
            "residual_squareclass": sq,
            "classification": "NONSQUARE_AFTER_EXACT_A1_BOUNDARY_FUNCTION_FIELD_REDUCTION",
            "square_trivial_in_boundary_function_field": False,
        })

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b2b1.explicit_a1_boundary_residue_field_squareclass.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B2B1_EXPLICIT_A1_BOUNDARY_RESIDUE_FIELD_SQUARECLASS_REDUCTION",
        "role": "EXACT_NONCREDIT_SQUARECLASS_REDUCTION_ON_THE_FOUR_C2C_EXPLICIT_A1_BOUNDARY_STRICT_PRIMES_USING_THEIR_COMMON_RATIONAL_CONIC_FUNCTION_FIELD",
        "entry": {"authority": AUTHORITY, "stage33_progress": "6/11", "successor_pr": 1722},
        "source_locks": {
            "r5b3b2_sha256": B3B2_SHA,
            "r5b3b3c2c_sha256": C2C_SHA,
            "c4a_sha256": C4A_SHA,
            "c4b2a_sha256": B2A_SHA,
            "squareclass_convention_source": "C4B1 exceptional P1 exact Q(i)[t] factor-parity reducer",
        },
        "method": {
            "field": "Q(i)",
            "target_prime_count": 4,
            "common_boundary_quotient": "Q(i)[a2,a3,b1]/(b1^2-a2^2-a3^2)",
            "generic_birational_parameters": "Q(i)(s,t), b1=s, a2=s(1-t^2)/(1+t^2), a3=2st/(1+t^2)",
            "squareclass_test": "explicitly divide the combined odd-carrier product by a displayed square; the remainder is t+1, which has one odd irreducible linear factor in Q(i)[t]",
        },
        "strict_boundary_squareclass_reduction": {
            "target_prime_count": 4,
            "square_trivial_count": 0,
            "nonsquare_count": 4,
            "all_four_share_nontrivial_squareclass_t_plus_1": True,
            "rows": rows,
        },
        "exact_consequence": {
            "four_explicit_a1_boundary_strict_prime_residues_audited": True,
            "all_four_are_nonsquare": True,
            "current_eight_symbol_formal_candidate_is_ramified_on_each_of_these_four_strict_primes": True,
            "this_is_a_negative_checkpoint_for_the_current_literal_formal_symbol_candidate_not_a_stage33_endpoint_result": True,
            "remaining_C4B2B_strict_prime_squareclass_context_count": 24,
            "offboundary_codimension_one_residue_cancellation_verified": False,
            "unramifiedness_verified": False,
        },
        "next_exact_leaf": "V91C1X_R5B3B3C4B2B2_REMAINING_24_STRICT_PRIME_RESIDUE_FIELD_SQUARECLASS_PARTITION",
        "next_exact_step": "partition and reduce the 4 F14 residual, 2 F4 repeated-factor, and 18 unique-factor strict-prime residue fields; preserve the exact negative result that the current literal eight-symbol representative is already ramified at the four explicit a1 boundary primes",
        "credit_firewall": {
            "authority_promotion": False,
            "hostile_audit_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
            "offboundary_cancellation_credit": False,
            "unramifiedness_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build_certificate()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
        r = cert["strict_boundary_squareclass_reduction"]
        print(json.dumps({
            "success": True,
            "marker": cert["candidate"],
            "target_prime_count": r["target_prime_count"],
            "square_trivial_count": r["square_trivial_count"],
            "nonsquare_count": r["nonsquare_count"],
            "certificate_sha256": cert["canonical_sha256"],
            "next_exact_leaf": cert["next_exact_leaf"],
        }, sort_keys=True))
        return
    if not OUT.exists():
        raise SystemExit(f"missing materialized certificate: {OUT}")
    current = json.loads(OUT.read_text(encoding="utf-8"))
    if current != cert:
        raise SystemExit("materialized C4B2B1 certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
