#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b3b1_a2_02_317_1757_boundary_uniformizers as b3b1
import materialize_e3_v91c1x_r5b3b3b_classify_20_novel_carriers_and_unify_27 as b3b3b

HERE = Path(__file__).resolve().parent
B3B1 = HERE / "e3-v91c1x-r5b3b1-a2-02-317-1757-boundary-uniformizers.json"
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
C1 = HERE / "e3-v91c1x-r5b3b3c1-offboundary-norm-factorization.json"
C2A = HERE / "e3-v91c1x-r5b3b3c2a-reused-prime-refinement-partition.json"
C2C = HERE / "e3-v91c1x-r5b3b3c2c-orbit-representative-strict-prime-decomposition-and-transport.json"
OUT = HERE / "e3-v91c1x-r5b3b3c3-c1-factor-to-strict-prime-and-exceptional-attachment.json"

B3B1_SHA = "8a5dcb751b312a846a06fac88298166efe8c1fd91ed0988b3cb04a408cfc2654"
B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
C1_SHA = "5c092fcec6720d0097d6e7509ce37b1506d7a099015a1a6a004250513d0f29f3"
C2A_SHA = "8eb0f382998f934ec712b79af0900df1f3da401e1a9770b770091577d0bc1c44"
C2C_SHA = "01fc321272106a1ce7c382783c4dcb128c164d21ee4deedf4060137ef9ed971a"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
A1_FACTOR_SHA = "44afff33ba591a11904229fe7936cb41caa700bd759cda0a5106218250561491"
SPECIAL = {"LIN_008", "LIN_015", "LIN_020", "LIN_025"}


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if csha(body) != claimed:
        raise SystemExit(f"canonical mismatch: {path.name}")
    if claimed != expected:
        raise SystemExit(f"source lock moved: {path.name}: {claimed}")
    return obj


def local_prime_id(kind: str, carrier_id: str, payload: object) -> str:
    return csha({"kind": kind, "carrier_id": carrier_id, "payload": payload})


def canonical_direct_support(expr: sp.Expr) -> str:
    poly = sp.Poly(expr, *b3b3b.BASE, extension=sp.I)
    terms = poly.terms()
    if not terms:
        raise SystemExit("zero direct support")
    normalized = sp.expand(expr / terms[0][1])
    return str(normalized).replace("**", "^").replace("I", "i")


def lin024_direct_factor_adapter(c1_row: dict, reused_row: dict) -> dict[str, dict]:
    a1, _a2, a3 = b3b3b.BASE
    exprs = [a1 + sp.I * a3, a1 - sp.I * a3]
    frozen_carrier = reused_row["projective_linear_form_Qi_sha256"]
    exact_prime_ids = {r["prime_id"] for r in reused_row["strict_height_one_prime_refinement"]}
    out: dict[str, dict] = {}
    calculated_prime_ids = set()
    for expr in exprs:
        support = canonical_direct_support(expr)
        factor_sha = csha(b3b3b.normalize_norm(sp.Poly(expr, *b3b3b.BASE, extension=sp.I)))
        prime_id = csha({"audited_direct_carrier": frozen_carrier, "support": support})
        calculated_prime_ids.add(prime_id)
        out[factor_sha] = {
            "strict_prime_ids": [prime_id],
            "adapter_basis": "HOSTILE_AUDITED_33_11D_DIRECT_LINEAR_BRANCH_AND_33_11E_CANONICAL_PRIME_ID_RULE",
            "direct_support_Qi": support,
            "prime_identifier_kind": "AUDITED_33_11D_DIRECT_PRIME_SUPPORT",
        }
    c1_hashes = {f["normalized_factor_sha256"] for f in c1_row["factors"]}
    if set(out) != c1_hashes:
        raise SystemExit(f"LIN_024 C1 direct-factor hashes moved: {set(out)} != {c1_hashes}")
    if calculated_prime_ids != exact_prime_ids:
        raise SystemExit(f"LIN_024 direct prime ids moved: {calculated_prime_ids} != {exact_prime_ids}")
    return out


def exceptional_orders(encoded: list, metas: dict[str, dict]) -> tuple[dict[str, int], int]:
    orders: dict[str, int] = {}
    checks = 0
    for eid, meta in metas.items():
        chart_orders = []
        for cp in range(6):
            _desc, order = b3b1.linear_factor_rees_pullback(encoded, meta, cp)
            chart_orders.append(int(order))
            checks += 1
        if len(set(chart_orders)) != 1:
            raise SystemExit(f"carrier exceptional order depends on Rees chart: {eid}/{chart_orders}")
        if chart_orders[0] not in (0, 1):
            raise SystemExit(f"unexpected linear carrier exceptional order: {eid}/{chart_orders[0]}")
        orders[eid] = chart_orders[0]
    return orders, checks


def build_certificate() -> dict:
    b3b1_cert = load(B3B1, B3B1_SHA)
    b3b2 = load(B3B2, B3B2_SHA)
    c1 = load(C1, C1_SHA)
    c2a = load(C2A, C2A_SHA)
    c2c = load(C2C, C2C_SHA)

    if b3b1_cert["cover_indexed_materialization"]["exceptional_order_standard_chart_invariance_check_count"] != 384:
        raise SystemExit("R5B3B1 exceptional replay prefix moved")
    if c2a["exact_partition"]["off_boundary_carrier_count"] != 23:
        raise SystemExit("C2A off-boundary count moved")
    if c2c["transported_novel20_strict_prime_decompositions"]["novel20_carrier_count"] != 20:
        raise SystemExit("C2C novel20 count moved")

    inv_rows = {r["carrier_id"]: r for r in b3b2["finite_linear_carrier_inventory"]["carrier_rows"]}
    c1_rows = {r["carrier_id"]: r for r in c1["exact_factorization"]["carrier_rows"]}
    off_ids = [r["carrier_id"] for r in c1["exact_factorization"]["carrier_rows"]]
    if len(off_ids) != 23 or len(set(off_ids)) != 23:
        raise SystemExit("C1 off-boundary carrier inventory moved")
    if any(cid not in inv_rows for cid in off_ids):
        raise SystemExit("C1 carrier escaped B3B2 inventory")

    reused_rows = {r["carrier_id"]: r for r in c2a["exact_partition"]["reused_carrier_rows"]}
    novel_rows = {r["carrier_id"]: r for r in c2c["transported_novel20_strict_prime_decompositions"]["rows"]}
    rep_rows = {r["carrier_id"]: r for r in c2c["representative_strict_prime_decompositions"]["rows"]}
    if set(reused_rows) | set(novel_rows) != set(off_ids) or set(reused_rows) & set(novel_rows):
        raise SystemExit("C2A/C2C do not partition C1 off-boundary carriers")

    exc = b3b1.atlas.load_locked(b3b1.atlas.EXC, b3b1.atlas.EXC_SHA)
    models = exc["exceptional_models"]
    expected_eids = [f"EXC_{i:03d}" for i in range(1, 49)]
    if [r["exceptional_id"] for r in models] != expected_eids:
        raise SystemExit("frozen exceptional inventory moved")
    metas = {r["exceptional_id"]: b3b1.atlas.node_meta(r) for r in models}

    adapter_rows = []
    exceptional_rows = []
    unique_factor_hashes = set()
    total_exceptional_rees_checks = 0

    for cid in off_ids:
        c1row = c1_rows[cid]
        factors = c1row["factors"]
        factor_hashes = {f["normalized_factor_sha256"] for f in factors}
        unique_factor_hashes.update(factor_hashes)
        per_factor: dict[str, dict] = {}

        if cid in reused_rows:
            reused = reused_rows[cid]
            strict_ids = [r["prime_id"] for r in reused["strict_height_one_prime_refinement"]]
            if cid == "LIN_024":
                per_factor = lin024_direct_factor_adapter(c1row, reused)
            else:
                if len(factors) != 1 or len(strict_ids) != 1:
                    raise SystemExit(f"unexpected reused singleton pattern: {cid}")
                per_factor[factors[0]["normalized_factor_sha256"]] = {
                    "strict_prime_ids": strict_ids,
                    "adapter_basis": "C2A_REUSED_FROZEN_33_11E_UNIQUE_STRICT_PRIME_REFINEMENT",
                    "prime_identifier_kind": reused["strict_height_one_prime_refinement"][0]["prime_record_kind"],
                }
        else:
            transported = novel_rows[cid]
            if transported["strict_prime_count"] == 1:
                if len(factors) != 1:
                    raise SystemExit(f"C2C singleton carrier has non-single C1 factors: {cid}")
                pid = local_prime_id(
                    "C2C_UNIQUE_REDUCED_STRICT_PRIME_OF_LINEAR_SECTION",
                    cid,
                    inv_rows[cid]["projective_linear_form_Qi_sha256"],
                )
                per_factor[factors[0]["normalized_factor_sha256"]] = {
                    "strict_prime_ids": [pid],
                    "adapter_basis": "C2C_UNIQUE_REDUCED_STRICT_PRIME_PLUS_C1_UNIQUE_BASE_FACTOR",
                    "prime_identifier_kind": "CERTIFICATE_LOCAL_UNIQUE_STRICT_PRIME_KEY",
                }
            elif transported["strict_prime_count"] == 2:
                if cid not in SPECIAL or cid not in rep_rows:
                    raise SystemExit(f"unexpected C2C two-prime carrier: {cid}")
                rep = rep_rows[cid]["special_reducible_norm_prime_decomposition_certificate"]
                if len(factors) != 2 or A1_FACTOR_SHA not in factor_hashes:
                    raise SystemExit(f"special C1 factor pattern moved: {cid}")
                boundary = rep["boundary_prime"]
                boundary_pid = local_prime_id(
                    "C2C_EXPLICIT_A1_BOUNDARY_PRIME",
                    cid,
                    boundary["ideal_generators_on_singular_surface"],
                )
                per_factor[A1_FACTOR_SHA] = {
                    "strict_prime_ids": [boundary_pid],
                    "adapter_basis": "C2C_EXPLICIT_BOUNDARY_PRIME_EXHAUSTS_A1_DETERMINANT_LENGTH",
                    "prime_identifier_kind": "CERTIFICATE_LOCAL_EXPLICIT_BOUNDARY_PRIME_KEY",
                    "ideal_generators_on_singular_surface": boundary["ideal_generators_on_singular_surface"],
                }
                residual = [f for f in factors if f["normalized_factor_sha256"] != A1_FACTOR_SHA]
                if len(residual) != 1 or rep["residual_prime"]["unique_minimal_prime_above_factor"] is not True:
                    raise SystemExit(f"special residual uniqueness moved: {cid}")
                residual_sha = residual[0]["normalized_factor_sha256"]
                residual_pid = local_prime_id("C2C_UNIQUE_RESIDUAL_PRIME_OVER_C1_FACTOR", cid, residual_sha)
                per_factor[residual_sha] = {
                    "strict_prime_ids": [residual_pid],
                    "adapter_basis": "C2C_UNIQUE_MINIMAL_RESIDUAL_PRIME_OVER_C1_F14_FACTOR",
                    "prime_identifier_kind": "CERTIFICATE_LOCAL_UNIQUE_RESIDUAL_PRIME_KEY",
                }
            else:
                raise SystemExit(f"unexpected novel strict-prime count: {cid}")

        if set(per_factor) != factor_hashes:
            raise SystemExit(f"factor adapter incomplete: {cid}")
        for fac in factors:
            sha = fac["normalized_factor_sha256"]
            rec = per_factor[sha]
            adapter_rows.append({
                "carrier_id": cid,
                "projective_linear_form_Qi_sha256": inv_rows[cid]["projective_linear_form_Qi_sha256"],
                "c1_normalized_factor_sha256": sha,
                "c1_factor_total_degree": fac["factor_total_degree"],
                "c1_determinant_multiplicity": fac["multiplicity"],
                "strict_prime_count_for_this_carrier_factor": len(rec["strict_prime_ids"]),
                **rec,
            })

        node_orders, checks = exceptional_orders(inv_rows[cid]["normalized_coefficients_Qi"], metas)
        total_exceptional_rees_checks += checks
        support = [eid for eid in expected_eids if node_orders[eid] == 1]
        exceptional_rows.append({
            "carrier_id": cid,
            "all_48_frozen_nodes_checked": True,
            "all_six_standard_rees_charts_agree_at_each_node": True,
            "nonzero_exceptional_total_transform_order": 1 if support else 0,
            "nonzero_exceptional_ids": support,
            "nonzero_exceptional_count": len(support),
            "full_48_order_vector_sha256": csha(node_orders),
        })

    if len(unique_factor_hashes) != c1["exact_factorization"]["unique_irreducible_factor_sha256_count"]:
        raise SystemExit("C1 unique factor count mismatch")
    if len(unique_factor_hashes) != 21:
        raise SystemExit(f"expected 21 unique C1 factors, got {len(unique_factor_hashes)}")
    if total_exceptional_rees_checks != 23 * 48 * 6:
        raise SystemExit("exceptional carrier Rees replay count moved")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c3.c1_factor_to_strict_prime_and_exceptional_attachment.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C3_C1_FACTOR_TO_STRICT_PRIME_MATCH_AND_EXCEPTIONAL_ATTACHMENT",
        "role": "EXACT_NONCREDIT_CONTEXTUAL_ADAPTER_FROM_ALL_C1_OFFBOUNDARY_BASE_FACTORS_TO_C2A_C2C_STRICT_PRIMES_PLUS_EXACT_48_NODE_EXCEPTIONAL_TOTAL_TRANSFORM_ORDERS_FOR_ALL_23_CARRIERS",
        "entry": {"pr": 1695, "authority": AUTHORITY, "stage33_progress": "6/11"},
        "source_locks": {
            "r5b3b1_boundary_uniformizers_sha256": B3B1_SHA,
            "r5b3b2_formal_symbol_carrier_inventory_sha256": B3B2_SHA,
            "r5b3b3c1_offboundary_norm_factorization_sha256": C1_SHA,
            "r5b3b3c2a_reused_prime_refinement_partition_sha256": C2A_SHA,
            "r5b3b3c2c_strict_prime_decomposition_sha256": C2C_SHA,
            "exceptional_p1_tangent_coordinates_sha256": b3b1.atlas.EXC_SHA,
        },
        "c1_factor_to_strict_prime_adapter": {
            "offboundary_carrier_count": 23,
            "unique_c1_factor_sha256_count": len(unique_factor_hashes),
            "carrier_factor_incidence_row_count": len(adapter_rows),
            "all_23_carriers_covered": {r["carrier_id"] for r in adapter_rows} == set(off_ids),
            "all_21_unique_c1_factors_covered": {r["c1_normalized_factor_sha256"] for r in adapter_rows} == unique_factor_hashes,
            "adapter_is_contextual_in_carrier_section_not_a_false_global_one_factor_one_prime_identification": True,
            "base_norm_determinant_multiplicity_kept_separate_from_scheme_multiplicity_of_strict_prime": True,
            "rows": adapter_rows,
        },
        "exceptional_total_transform_attachment": {
            "frozen_exceptional_node_count": 48,
            "offboundary_carrier_count": 23,
            "standard_rees_charts_per_node": 6,
            "exact_linear_factor_rees_pullback_checks": total_exceptional_rees_checks,
            "orders_are_carrier_total_transform_orders_not_claimed_as_additional_strict_prime_components": True,
            "rows": exceptional_rows,
        },
        "construction_status": {
            "c1_base_factor_to_strict_prime_adapter_materialized_for_all_21_unique_factors": True,
            "exceptional_total_transform_orders_materialized_for_all_23_offboundary_carriers_at_all_48_nodes": True,
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
            "the_C1_base_factor_versus_resolved_strict_prime_gap_is_closed_contextually_for_each_of_the_23_carrier_sections": True,
            "the_exceptional_total_transform_order_of_every_offboundary_linear_carrier_is_now_exact_on_all_48_frozen_exceptional_divisors": True,
            "LIN_024_two_linear_base_factors_are_matched_to_the_two_audited_33_11d_direct_prime_supports": True,
            "no_combined_residue_squareclass_or_unramifiedness_credit_follows_yet": True,
        },
        "next_missing_object": "COMPUTE_THE_COMBINED_EIGHT_TERM_TAME_RESIDUE_SQUARECLASS_ON_EVERY_STRICT_AND_EXCEPTIONAL_CODIMENSION_ONE_PRIME_USING_THE_B3B2_SIGNED_CARRIER_APPEARANCES_THE_C3_ADAPTER_AND_THE_EXACT_BOUNDARY_UNIFORMIZER_RESIDUE_FUNCTION_PAIRS",
        "next_exact_leaf": "V91C1X_R5B3B3C4_COMBINED_TAME_RESIDUE_SQUARECLASS_AUDIT",
        "credit_firewall": {
            "authority_promotion": False,
            "hostile_audit_credit": False,
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
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "candidate": cert["candidate"],
        "canonical_sha256": cert["canonical_sha256"],
        "unique_c1_factors": cert["c1_factor_to_strict_prime_adapter"]["unique_c1_factor_sha256_count"],
        "carrier_factor_rows": cert["c1_factor_to_strict_prime_adapter"]["carrier_factor_incidence_row_count"],
        "exceptional_rees_checks": cert["exceptional_total_transform_attachment"]["exact_linear_factor_rees_pullback_checks"],
        "stage33_progress": "6/11",
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
