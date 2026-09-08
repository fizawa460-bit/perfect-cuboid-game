#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b3b2_a2_02_formal_tame_symbol_hidden_carrier_inventory as b3b2mat

HERE = Path(__file__).resolve().parent
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
B3B3A = HERE / "e3-v91c1x-r5b3b3a-match-27-carriers-to-retained-33.json"
OUT = HERE / "e3-v91c1x-r5b3b3b-classify-20-novel-carriers-and-unify-27.json"
B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
B3B3A_SHA = "36bd375d08b4ebd852bb101851b108fae7e76780f2a35b6ea033948f9ddb8e77"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"

a1, a2, a3, b1, b2, b3, c = sp.symbols("a1 a2 a3 b1 b2 b3 c")
BASE = (a1, a2, a3)
RADICALS = (b1, b2, b3, c)
COORDS = (a1, a2, a3, b1, b2, b3, c)
SQUARES = {
    b1: a2*a2 + a3*a3,
    b2: a1*a1 + a3*a3,
    b3: a1*a1 + a2*a2,
    c: a1*a1 + a2*a2 + a3*a3,
}


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical lock moved: {path.name}")
    return obj


def reduce_quadratic(expr, var, square):
    poly = sp.Poly(sp.expand(expr), var)
    even = 0
    odd = 0
    for (k,), coef in poly.terms():
        if k % 2 == 0:
            even += coef * square ** (k // 2)
        else:
            odd += coef * square ** ((k - 1) // 2)
    return sp.expand(even**2 - square*odd**2)


def full_sign_norm(expr):
    out = expr
    for var in RADICALS:
        out = reduce_quadratic(out, var, SQUARES[var])
    return sp.expand(out)


def enc_qi(x):
    x = sp.cancel(sp.expand(x))
    xc = sp.cancel(sp.conjugate(x))
    re = sp.cancel((x + xc) / 2)
    im = sp.cancel((x - xc) / (2*sp.I))
    if re.is_Rational is not True or im.is_Rational is not True:
        raise SystemExit(f"coefficient escaped Q(i): {x}")
    return [int(sp.numer(re)), int(sp.denom(re)), int(sp.numer(im)), int(sp.denom(im))]


def normalized_factor_record(factor, exponent):
    p = sp.Poly(sp.expand(factor), *BASE, extension=sp.I)
    if not p.terms():
        raise SystemExit("zero norm factor")
    lead = p.terms()[0][1]
    p = sp.Poly(sp.expand(p.as_expr()/lead), *BASE, extension=sp.I)
    rows = [
        {"monomial_exponents": list(mon), "coefficient_Qi": enc_qi(coef)}
        for mon, coef in p.terms()
    ]
    expr = sp.expand(p.as_expr())
    coord = next((name for name, var in (("a1", a1), ("a2", a2), ("a3", a3)) if sp.expand(expr-var) == 0), None)
    return {
        "degree": int(p.total_degree()),
        "exponent_in_norm": int(exponent),
        "normalized_terms": rows,
        "coordinate_factor": coord,
    }


def linear_expr(coeffs):
    vals = [b3b2mat.atlas.decode_element(z) for z in coeffs]
    return sp.expand(sum(q*x for q, x in zip(vals, COORDS)))


def factor_novel_carrier(row):
    norm = full_sign_norm(linear_expr(row["normalized_coefficients_Qi"]))
    if sp.Poly(norm, *BASE, extension=sp.I).total_degree() != 16:
        raise SystemExit(f"full sign norm degree moved: {row['carrier_id']}")
    _, factors = sp.factor_list(norm, *BASE, extension=sp.I)
    frecs = [normalized_factor_record(f, e) for f, e in factors]
    if sum(r["degree"]*r["exponent_in_norm"] for r in frecs) != 16:
        raise SystemExit(f"degree accounting moved: {row['carrier_id']}")
    noncoord = [r for r in frecs if r["coordinate_factor"] is None]
    boundary_only = not noncoord
    return {
        "carrier_id": row["carrier_id"],
        "projective_linear_form_Qi_sha256": row["projective_linear_form_Qi_sha256"],
        "appears_in_pi_D": row["appears_in_pi_D"],
        "appears_in_f_D": row["appears_in_f_D"],
        "full_sign_norm_total_degree": 16,
        "norm_factorization_over_Qi": frecs,
        "boundary_only": boundary_only,
        "classification": "BOUNDARY_ONLY_COORDINATE_NORM_SUPPORT" if boundary_only else "OFF_BOUNDARY_NONCOORDINATE_NORM_SUPPORT",
        "noncoordinate_factor_count": len(noncoord),
        "noncoordinate_factor_degree_exponent_pairs": [[r["degree"], r["exponent_in_norm"]] for r in noncoord],
    }


def build_certificate():
    b3b2 = load(B3B2, B3B2_SHA)
    b3b3a = load(B3B3A, B3B3A_SHA)
    inv = b3b2["finite_linear_carrier_inventory"]
    part = b3b3a["match_partition"]
    if inv["unique_projective_linear_carrier_count"] != 27:
        raise SystemExit("R5B3B2 27-carrier count moved")
    if (part["matched_retained_33_count"], part["novel_relative_to_retained_33_count"]) != (7, 20):
        raise SystemExit("R5B3B3A 7+20 partition moved")
    if (part["pi_D_matched_count"], part["pi_D_novel_count"], part["f_D_matched_count"], part["f_D_novel_count"]) != (0, 20, 7, 0):
        raise SystemExit("R5B3B3A pi/f partition moved")

    current = {r["carrier_id"]: r for r in inv["carrier_rows"]}
    partition = {r["carrier_id"]: r for r in part["carrier_rows"]}
    novel_rows = [factor_novel_carrier(current[cid]) for cid in part["novel_carrier_ids"]]
    novel = {r["carrier_id"]: r for r in novel_rows}

    unified = []
    for base in inv["carrier_rows"]:
        cid = base["carrier_id"]
        p = partition[cid]
        if p["matches_retained_stage33_07_carrier"]:
            boundary_only = bool(p["retained_boundary_only"])
            classification = p["retained_classification"]
            source = "REUSED_RETAINED_STAGE33_07_SIGN_NORM_CLASSIFICATION"
            factors = None
        else:
            nr = novel[cid]
            boundary_only = nr["boundary_only"]
            classification = nr["classification"]
            source = "R5B3B3B_EXACT_FULL_SIGN_NORM_FACTORIZATION"
            factors = nr["norm_factorization_over_Qi"]
        unified.append({
            "carrier_id": cid,
            "projective_linear_form_Qi_sha256": base["projective_linear_form_Qi_sha256"],
            "appears_in_pi_D": base["appears_in_pi_D"],
            "appears_in_f_D": base["appears_in_f_D"],
            "classification_source": source,
            "boundary_only": boundary_only,
            "classification": classification,
            "novel_norm_factorization_over_Qi": factors,
        })

    boundary = [r for r in unified if r["boundary_only"]]
    off = [r for r in unified if not r["boundary_only"]]
    novel_boundary = [r for r in novel_rows if r["boundary_only"]]
    novel_off = [r for r in novel_rows if not r["boundary_only"]]
    pattern_hist = {}
    for r in novel_rows:
        key = json.dumps(r["noncoordinate_factor_degree_exponent_pairs"], separators=(",", ":"))
        pattern_hist[key] = pattern_hist.get(key, 0) + 1

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3b.classify_20_novel_carriers_and_unify_27.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3B_CLASSIFY_20_NOVEL_PI_CARRIERS_AND_UNIFY_ALL_27_BY_FULL_SIGN_NORM",
        "role": "EXACT_NONCREDIT_FULL_SIGN_NORM_CLASSIFICATION_OF_ALL_R5B3B2_TAME_SYMBOL_LINEAR_CARRIERS_BEFORE_PRIME_DECOMPOSITION",
        "entry": {"pr": 1695, "authority": AUTHORITY, "stage33_progress": "6/11"},
        "source_locks": {
            "r5b3b2_formal_symbol_carrier_inventory_sha256": B3B2_SHA,
            "r5b3b3a_retained_new_partition_sha256": B3B3A_SHA,
        },
        "surface_sign_norm_model": {
            "base_coordinates": ["a1", "a2", "a3"],
            "quadratic_radicals": ["b1", "b2", "b3", "c"],
            "relations": {"b1^2": "a2^2+a3^2", "b2^2": "a1^2+a3^2", "b3^2": "a1^2+a2^2", "c^2": "a1^2+a2^2+a3^2"},
            "full_sign_norm_degree": 16,
            "factorization_field": "Q(i)",
            "boundary_only_criterion": "ALL_IRREDUCIBLE_NORM_FACTORS_ARE_COORDINATE_A1_A2_A3",
        },
        "novel_20_exact_factorization": {
            "carrier_count": len(novel_rows),
            "all_are_pi_D_only": all(r["appears_in_pi_D"] and not r["appears_in_f_D"] for r in novel_rows),
            "boundary_only_count": len(novel_boundary),
            "off_boundary_count": len(novel_off),
            "noncoordinate_factor_pattern_histogram": pattern_hist,
            "carrier_rows": novel_rows,
        },
        "unified_27_classification": {
            "carrier_count": len(unified),
            "reused_retained_count": 7,
            "newly_factorized_count": 20,
            "boundary_only_count": len(boundary),
            "off_boundary_count": len(off),
            "pi_D_boundary_only_count": sum(r["appears_in_pi_D"] and r["boundary_only"] for r in unified),
            "pi_D_off_boundary_count": sum(r["appears_in_pi_D"] and not r["boundary_only"] for r in unified),
            "f_D_boundary_only_count": sum(r["appears_in_f_D"] and r["boundary_only"] for r in unified),
            "f_D_off_boundary_count": sum(r["appears_in_f_D"] and not r["boundary_only"] for r in unified),
            "off_boundary_carrier_ids": [r["carrier_id"] for r in off],
            "boundary_only_carrier_ids": [r["carrier_id"] for r in boundary],
            "carrier_rows": unified,
            "all_27_carriers_classified_boundary_vs_offboundary": len(unified) == 27 and len(boundary)+len(off) == 27,
        },
        "construction_status": {
            "all_20_novel_pi_D_carrier_full_sign_norms_factorized_exactly_over_Qi": True,
            "all_27_carriers_classified_boundary_vs_offboundary": True,
            "all_offboundary_carrier_hyperplane_sections_prime_decomposed_on_resolved_surface": False,
            "combined_tame_residue_squareclasses_audited": False,
            "offboundary_codimension_one_residue_cancellation_verified": False,
            "single_global_a2_02_kummer_or_brauer_representative_materialized": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "equivalent_unimodular_cech_glue_materialized": False,
            "same_representative_swap23_transport_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
        },
        "exact_consequence": {
            "the_possible_nonboundary_residue_support_is_now_restricted_to_the_explicit_offboundary_subset_of_the_27_carriers": True,
            "boundary_only_carriers_require_no_new_nonboundary_prime_decomposition": True,
            "the_next_task_is_prime_decomposition_only_for_the_offboundary_hyperplane_sections_then_combined_tame_residue_squareclasses": True,
            "classification_alone_does_not_prove_unramifiedness_or_global_lift": True,
        },
        "next_missing_object": "RESOLVED_SURFACE_PRIME_DECOMPOSITION_OF_ONLY_THE_OFFBOUNDARY_CARRIERS_IN_THE_UNIFIED_27_CLASSIFICATION_AND_EXACT_COMBINED_TAME_RESIDUE_SQUARECLASS_ON_EACH_RESULTING_PRIME",
        "next_exact_leaf": "V91C1X_R5B3B3C_PRIME_DECOMPOSE_OFFBOUNDARY_CARRIERS_AND_COMPUTE_COMBINED_TAME_RESIDUES",
        "credit_firewall": {
            "authority_promotion": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "mask20_credit": False,
            "source_bound_dim5_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "hostile_audit_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build_certificate()
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    n = cert["novel_20_exact_factorization"]
    u = cert["unified_27_classification"]
    print(json.dumps({
        "success": True,
        "candidate": cert["candidate"],
        "canonical_sha256": cert["canonical_sha256"],
        "novel_boundary_only_count": n["boundary_only_count"],
        "novel_off_boundary_count": n["off_boundary_count"],
        "unified_boundary_only_count": u["boundary_only_count"],
        "unified_off_boundary_count": u["off_boundary_count"],
        "pi_D_off_boundary_count": u["pi_D_off_boundary_count"],
        "f_D_off_boundary_count": u["f_D_off_boundary_count"],
        "stage33_progress": "6/11",
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
