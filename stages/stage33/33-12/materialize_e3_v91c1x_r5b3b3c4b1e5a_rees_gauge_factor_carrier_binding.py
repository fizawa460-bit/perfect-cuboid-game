#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as atlas

HERE = Path(__file__).resolve().parent
E4 = HERE / "e3-v91c1x-r5b3b3c4b1e4-rees-cartier-rational-gauge-lift.json"
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
EXC = HERE.parent / "33-07" / "exceptional-p1-tangent-coordinates.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1e5a-rees-gauge-factor-carrier-binding.json"

E4_SHA = "6a31839c0ef50439d6a0e5a7b4d6b452ae8caf2f68d0419aa1dbc4d339c27d07"
B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
EXC_SHA = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
I = sp.I


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(
            f"canonical source lock moved {path.name}: claimed={claimed} actual={actual} expected={expected}"
        )
    return obj


def clean(x: sp.Expr) -> sp.Expr:
    return atlas.clean(x)


def normalize_projective_coefficients(coeffs: list[sp.Expr]) -> tuple[tuple[int, int, int, int], ...]:
    vals = [clean(x) for x in coeffs]
    pivot = next((x for x in vals if x != 0), None)
    if pivot is None:
        raise SystemExit("zero projective linear form")
    vals = [clean(x / pivot) for x in vals]
    return tuple(tuple(int(y) for y in atlas.encode_element(x)) for x in vals)


def normalized_poly(poly: sp.Expr, variables: list[sp.Symbol]) -> sp.Expr:
    P = sp.Poly(sp.expand(poly), *variables, extension=I)
    if P.is_zero:
        raise SystemExit("zero polynomial factor")
    return clean(P.monic().as_expr())


def affine_direction_linear_to_ambient_signature(
    factor: sp.Expr,
    H: list[sp.Symbol],
    meta: dict,
) -> tuple[tuple[int, int, int, int], ...]:
    f = clean(factor)
    P = sp.Poly(sp.expand(f), *H, extension=I)
    if int(P.total_degree()) != 1:
        raise SystemExit("nonlinear factor passed to ambient linear carrier conversion")
    zero = {h: 0 for h in H}
    if clean(f.subs(zero, simultaneous=True)) != 0:
        raise SystemExit("Rees-direction linear factor acquired constant term")
    c = [clean(sp.diff(f, h)) for h in H]
    if all(x == 0 for x in c):
        raise SystemExit("zero Rees-direction linear coefficients")

    ambient = [sp.Integer(0)] * 7
    p = meta["point"]
    pivot = int(meta["pivot"])
    pp = clean(p[pivot])
    if pp == 0:
        raise SystemExit("zero affine pivot")
    q = [clean(x / pp) for x in p]
    nonpivot = [int(x) for x in meta["nonpivot"]]
    if len(nonpivot) != 6:
        raise SystemExit("unexpected affine nonpivot count")
    for j, cj in zip(nonpivot, c):
        ambient[j] = clean(cj)
    ambient[pivot] = clean(-sum(cj * q[j] for j, cj in zip(nonpivot, c)))
    if clean(sum(ambient[j] * p[j] for j in range(7))) != 0:
        raise SystemExit("lifted ambient hyperplane does not pass through source node")
    return normalize_projective_coefficients(ambient)


def encode_signature(sig: tuple[tuple[int, int, int, int], ...]) -> list[list[int]]:
    return [list(z) for z in sig]


def build_certificate() -> dict:
    e4 = load_locked(E4, E4_SHA)
    b3b2 = load_locked(B3B2, B3B2_SHA)
    exc = load_locked(EXC, EXC_SHA)

    er_by_eid = {row["exceptional_id"]: row for row in exc["exceptional_models"]}
    carrier_rows = b3b2["finite_linear_carrier_inventory"]["carrier_rows"]
    old_by_sig = {
        tuple(tuple(int(y) for y in z) for z in row["normalized_coefficients_Qi"]): row["carrier_id"]
        for row in carrier_rows
    }
    if len(old_by_sig) != len(carrier_rows):
        raise SystemExit("B3B2 carrier normalized signatures are not unique")

    H = list(sp.symbols("H0:6"))
    factor_rows = []
    linear_signatures: dict[tuple[tuple[int, int, int, int], ...], dict] = {}
    nonlinear_factor_count = 0
    total_factor_occurrences = 0

    gauges = e4["rees_rational_gauge_lifts"]["rows"]
    if len(gauges) != 4:
        raise SystemExit("expected four E4 gauge rows")

    for grow in gauges:
        eid = grow["source_exceptional_id"]
        if eid not in er_by_eid:
            raise SystemExit(f"missing exceptional source row {eid}")
        meta = atlas.node_meta(er_by_eid[eid])
        for kind, field in (
            ("zero", "homogeneous_q_numerator_Qi_H"),
            ("pole", "homogeneous_q_denominator_Qi_H"),
        ):
            poly = atlas.decode_poly(grow[field], H)
            if poly == 0:
                raise SystemExit(f"zero E4 homogeneous {kind} polynomial for {eid}")
            scalar, factors = sp.factor_list(sp.expand(poly), *H, extension=I)
            rebuild = sp.sympify(scalar)
            for fac, exponent in factors:
                rebuild *= sp.expand(fac) ** int(exponent)
            if clean(poly - rebuild) != 0:
                raise SystemExit(f"factorization rebuild failed for {eid}/{kind}")
            if not factors:
                raise SystemExit(f"constant E4 homogeneous {kind} polynomial for {eid}")

            for fac, exponent in factors:
                fac = clean(fac)
                exponent = int(exponent)
                degree = int(sp.Poly(sp.expand(fac), *H, extension=I).total_degree())
                total_factor_occurrences += exponent
                row = {
                    "source_exceptional_id": eid,
                    "equation_kind": kind,
                    "factor_exponent": exponent,
                    "factor_total_degree": degree,
                    "normalized_factor_Qi_H": atlas.encode_poly(normalized_poly(fac, H), H),
                }
                if degree == 1:
                    sig = affine_direction_linear_to_ambient_signature(fac, H, meta)
                    old_id = old_by_sig.get(sig)
                    row.update({
                        "factor_is_linear_rees_direction_hyperplane": True,
                        "ambient_projective_hyperplane_through_source_node_normalized_coefficients_Qi": encode_signature(sig),
                        "ambient_projective_hyperplane_signature_sha256": csha(encode_signature(sig)),
                        "matches_existing_b3b2_linear_carrier": old_id is not None,
                        "matching_b3b2_carrier_id": old_id,
                    })
                    entry = linear_signatures.setdefault(sig, {
                        "matching_b3b2_carrier_id": old_id,
                        "occurrences": [],
                    })
                    if entry["matching_b3b2_carrier_id"] != old_id:
                        raise SystemExit("carrier match instability for repeated signature")
                    entry["occurrences"].append({
                        "source_exceptional_id": eid,
                        "equation_kind": kind,
                        "factor_exponent": exponent,
                    })
                else:
                    nonlinear_factor_count += 1
                    row.update({
                        "factor_is_linear_rees_direction_hyperplane": False,
                        "matches_existing_b3b2_linear_carrier": False,
                        "matching_b3b2_carrier_id": None,
                    })
                factor_rows.append(row)

    inventory_rows = []
    existing_match_count = 0
    for sig, data in sorted(linear_signatures.items(), key=lambda kv: csha(encode_signature(kv[0]))):
        old_id = data["matching_b3b2_carrier_id"]
        if old_id is not None:
            existing_match_count += 1
        inventory_rows.append({
            "ambient_projective_hyperplane_normalized_coefficients_Qi": encode_signature(sig),
            "ambient_projective_hyperplane_signature_sha256": csha(encode_signature(sig)),
            "matching_b3b2_carrier_id": old_id,
            "matches_existing_b3b2_linear_carrier": old_id is not None,
            "occurrences": sorted(data["occurrences"], key=lambda x: (x["source_exceptional_id"], x["equation_kind"])),
        })

    distinct_linear = len(inventory_rows)
    all_linear = nonlinear_factor_count == 0
    all_existing = all_linear and existing_match_count == distinct_linear

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1e5a.rees_gauge_factor_carrier_binding.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1E5A_REES_GAUGE_FACTOR_TO_B3B2_CARRIER_BINDING",
        "role": "EXACT_NONCREDIT_BOUNDED_FACTORIZATION_OF_THE_E4_HOMOGENEOUS_GAUGE_NUMERATOR_AND_DENOMINATOR_AND_SOURCE_BOUND_BINDING_OF_LINEAR_DIRECTION_FACTORS_TO_AMBIENT_PROJECTIVE_HYPERPLANES",
        "entry": {
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
            "successor_pr": 1722,
            "merged_parent_pr": 1695,
            "replaces_timeout_heavy_e5_as_the_next_bounded_diagnostic": True,
        },
        "source_locks": {
            "c4b1e4_rees_cartier_rational_gauge_lift_sha256": E4_SHA,
            "b3b2_hidden_linear_carrier_inventory_sha256": B3B2_SHA,
            "exceptional_p1_tangent_coordinates_sha256": EXC_SHA,
        },
        "factorization": {
            "gauge_row_count": len(gauges),
            "zero_pole_polynomial_count": 2 * len(gauges),
            "factor_occurrence_count_with_multiplicity": total_factor_occurrences,
            "nonlinear_distinct_factor_row_count": nonlinear_factor_count,
            "all_e4_homogeneous_zero_and_pole_factors_linear_over_Qi": all_linear,
            "rows": sorted(factor_rows, key=lambda x: (x["source_exceptional_id"], x["equation_kind"], x["ambient_projective_hyperplane_signature_sha256"] if x.get("ambient_projective_hyperplane_signature_sha256") else csha(x["normalized_factor_Qi_H"]))),
        },
        "ambient_linear_carrier_binding": {
            "distinct_e4_ambient_linear_hyperplane_count": distinct_linear,
            "existing_b3b2_match_count": existing_match_count,
            "all_e4_linear_hyperplanes_already_present_in_b3b2_inventory": all_existing,
            "rows": inventory_rows,
        },
        "exact_consequence": {
            "e4_offfiber_support_candidates_are_factored_before_any_prime_level_claim": True,
            "all_e4_direction_linear_factors_are_lifted_to_source_bound_projective_hyperplanes_through_the_corresponding_frozen_node": all(row["factor_is_linear_rees_direction_hyperplane"] for row in factor_rows) if factor_rows else False,
            "no_new_ambient_linear_carrier_beyond_b3b2_inventory": all_existing,
            "e5_cartier_nonzerodivisor_saturation_completed": False,
            "off_exceptional_height_one_prime_inventory_complete": False,
            "same_representative_full_surface_gauge_correction_verified": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
            "h2_fixedness_verified": False,
        },
        "diagnostic_boundary": {
            "what_this_can_close_if_all_existing": "the E4 rational extension introduces no previously unseen ambient linear hyperplane carrier; prime-level support still inherits the existing B3B2 carrier-refinement debt rather than disappearing",
            "what_this_does_not_prove": "factor-level carrier matching is not a height-one prime decomposition, is not a nonzerodivisor proof on every strict-transform chart, and is not a full-surface Hilbert90 correction",
        },
        "next_exact_step": "if every E4 factor is linear and bound to B3B2, restrict the next computation to the matched finite carrier subset and reuse the Stage33-11 prime-refinement/orbit-reduction protocol to compute the induced residue change prime by prime; otherwise isolate only the residual new or nonlinear factors",
        "parallel_outstanding_leaf": "V91C1X_R5B3B3C4B2_STRICT_PRIME_CROSS_CARRIER_INCIDENCE_AND_RESIDUE_FIELD_SQUARECLASS_REDUCTION",
        "credit_firewall": {
            "authority_promotion": False,
            "hostile_audit_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
            "exceptional_cancellation_credit": False,
            "unramifiedness_credit": False,
            "source_bound_dim5_credit": False,
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
        print(f"wrote {OUT}")
        print(cert["canonical_sha256"])
        return
    if not OUT.exists():
        raise SystemExit(f"missing materialized certificate: {OUT}")
    current = json.loads(OUT.read_text(encoding="utf-8"))
    if current != cert:
        raise SystemExit("materialized C4B1E5A certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
