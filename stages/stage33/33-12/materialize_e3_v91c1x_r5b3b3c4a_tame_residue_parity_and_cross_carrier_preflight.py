#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

import materialize_e3_v91c1x_r5b3b1_a2_02_317_1757_boundary_uniformizers as b3b1

HERE = Path(__file__).resolve().parent
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
C3 = HERE / "e3-v91c1x-r5b3b3c3-c1-factor-to-strict-prime-and-exceptional-attachment.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4a-tame-residue-parity-and-cross-carrier-preflight.json"

B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
C3_SHA = "d65be2f66b16c14ac230746ca0e832a627da611ceb7533b4766e1b13df23ae71"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical source lock moved: {path.name}: {claimed}")
    return obj


def build_member_exponents(carrier_rows: list[dict], components: list[str]):
    pi = {d: defaultdict(int) for d in components}
    ff = {d: defaultdict(int) for d in components}
    for row in carrier_rows:
        cid = row["carrier_id"]
        for app in row["appearances"]:
            d = app["symbol_component"]
            if d not in pi:
                raise SystemExit(f"unexpected symbol component in carrier inventory: {d}")
            target = pi if app["member"] == "pi_D" else ff if app["member"] == "f_D" else None
            if target is None:
                raise SystemExit(f"unexpected symbol member: {app['member']}")
            target[d][cid] += int(app["exponent"])
    return pi, ff


def residue_parity_for_valuation_vector(
    carrier_ids: list[str],
    components: list[str],
    pi: dict,
    ff: dict,
    valuation: dict[str, int],
) -> tuple[list[str], int, dict[str, int], dict[str, int]]:
    # For [pi_D,f_D]_2, tame residue has unit-factor exponent
    #   v_D(f_D)*ord(L in pi_D) - v_D(pi_D)*ord(L in f_D).
    # Mod 2 the sign (-1)^(v(pi_D)v(f_D)) is harmless over Q(i), since -1=i^2.
    odd = defaultdict(int)
    vpi_by_component: dict[str, int] = {}
    vf_by_component: dict[str, int] = {}
    sign_parity = 0
    for d in components:
        vpi = sum(int(pi[d].get(cid, 0)) * int(valuation.get(cid, 0)) for cid in carrier_ids)
        vf = sum(int(ff[d].get(cid, 0)) * int(valuation.get(cid, 0)) for cid in carrier_ids)
        vpi_by_component[d] = vpi
        vf_by_component[d] = vf
        sign_parity ^= (vpi * vf) & 1
        for cid in carrier_ids:
            e = int(pi[d].get(cid, 0)) * vf - int(ff[d].get(cid, 0)) * vpi
            odd[cid] ^= e & 1
    return sorted(cid for cid in carrier_ids if odd[cid]), sign_parity, vpi_by_component, vf_by_component


def build_certificate() -> dict:
    b3b2 = load(B3B2, B3B2_SHA)
    c3 = load(C3, C3_SHA)

    formal = b3b2["formal_tame_symbol_sum"]
    if formal["term_count"] != 8 or formal["formal_symbol_sum_materialized"] is not True:
        raise SystemExit("R5B3B2 eight-term formal symbol prefix moved")
    components = list(formal["component_ids_in_source_order"])
    carrier_rows = b3b2["finite_linear_carrier_inventory"]["carrier_rows"]
    carrier_ids = [r["carrier_id"] for r in carrier_rows]
    if len(carrier_ids) != len(set(carrier_ids)):
        raise SystemExit("duplicate carrier id")
    inv = {r["carrier_id"]: r for r in carrier_rows}
    pi, ff = build_member_exponents(carrier_rows, components)

    adapter = c3["c1_factor_to_strict_prime_adapter"]
    if adapter["all_21_unique_c1_factors_covered"] is not True or adapter["all_23_carriers_covered"] is not True:
        raise SystemExit("C3 strict-prime adapter coverage moved")
    adapter_rows = list(adapter["rows"])
    off_ids = sorted({r["carrier_id"] for r in adapter_rows})
    if len(off_ids) != 23 or any(cid not in inv for cid in off_ids):
        raise SystemExit("C3 off-boundary carrier coverage moved")

    factor_groups: dict[str, list[dict]] = defaultdict(list)
    for row in adapter_rows:
        factor_groups[row["c1_normalized_factor_sha256"]].append(row)
    if len(factor_groups) != 21:
        raise SystemExit(f"C3 unique C1 factor count moved: {len(factor_groups)}")

    repeated_groups = []
    repeated_factor_shas = set()
    for fsha, rows in sorted(factor_groups.items()):
        carriers = sorted({r["carrier_id"] for r in rows})
        if len(rows) > 1:
            repeated_factor_shas.add(fsha)
            repeated_groups.append({
                "c1_normalized_factor_sha256": fsha,
                "carrier_ids": carriers,
                "carrier_factor_incidence_count": len(rows),
                "strict_prime_ids_by_carrier": {
                    r["carrier_id"]: list(r["strict_prime_ids"]) for r in rows
                },
                "local_prime_id_equality_alone_is_not_used_as_geometric_distinctness_proof": True,
            })

    strict_rows = []
    unique_factor_rows = 0
    unique_factor_zero_parity_rows = 0
    unresolved_repeated_rows = 0
    for row in adapter_rows:
        cid = row["carrier_id"]
        fsha = row["c1_normalized_factor_sha256"]
        repeated = fsha in repeated_factor_shas
        # This valuation vector is exact only after establishing that the target prime
        # is not simultaneously contained in another distinct carrier hyperplane.
        valuation = {x: 0 for x in carrier_ids}
        valuation[cid] = 1
        odd, sign, vpi, vf = residue_parity_for_valuation_vector(carrier_ids, components, pi, ff, valuation)
        if repeated:
            unresolved_repeated_rows += 1
        else:
            unique_factor_rows += 1
            if not odd:
                unique_factor_zero_parity_rows += 1
        strict_rows.append({
            "carrier_id": cid,
            "c1_normalized_factor_sha256": fsha,
            "strict_prime_ids": list(row["strict_prime_ids"]),
            "c1_factor_repeated_across_carrier_contexts": repeated,
            "single_carrier_valuation_candidate": {cid: 1},
            "combined_tame_residue_odd_linear_carrier_ids_under_single_carrier_valuation": odd,
            "combined_tame_residue_carrier_parity_zero_under_single_carrier_valuation": not odd,
            "tame_sign_parity": sign,
            "minus_one_is_square_in_Qi_so_tame_sign_does_not_obstruct_squaretriviality": True,
            "v_pi_by_symbol_component": vpi,
            "v_f_by_symbol_component": vf,
            "squareclass_conclusion_on_this_strict_prime": (
                "SQUARE_TRIVIAL_BY_EVEN_LINEAR_FACTOR_PARITY" if (not repeated and not odd)
                else "OPEN_REPEATED_FACTOR_CROSS_CARRIER_INCIDENCE" if repeated
                else "OPEN_NONZERO_FORMAL_LINEAR_FACTOR_PARITY"
            ),
        })

    # Exact exceptional valuation vectors for all formal-symbol carriers, not only the 23 C3 off-boundary rows.
    exc = b3b1.atlas.load_locked(b3b1.atlas.EXC, b3b1.atlas.EXC_SHA)
    models = exc["exceptional_models"]
    expected_eids = [f"EXC_{i:03d}" for i in range(1, 49)]
    if [r["exceptional_id"] for r in models] != expected_eids:
        raise SystemExit("frozen 48-node inventory moved")
    metas = {r["exceptional_id"]: b3b1.atlas.node_meta(r) for r in models}
    order_by_eid: dict[str, dict[str, int]] = {eid: {} for eid in expected_eids}
    rees_checks = 0
    for cid in carrier_ids:
        coeffs = inv[cid]["normalized_coefficients_Qi"]
        for eid in expected_eids:
            orders = []
            for cp in range(6):
                _desc, order = b3b1.linear_factor_rees_pullback(coeffs, metas[eid], cp)
                orders.append(int(order))
                rees_checks += 1
            if len(set(orders)) != 1 or orders[0] not in (0, 1):
                raise SystemExit(f"carrier Rees order moved: {cid}/{eid}/{orders}")
            order_by_eid[eid][cid] = orders[0]

    c3_exc = {r["carrier_id"]: r for r in c3["exceptional_total_transform_attachment"]["rows"]}
    if set(c3_exc) != set(off_ids):
        raise SystemExit("C3 exceptional attachment off-boundary carrier set moved")
    for cid in off_ids:
        support = [eid for eid in expected_eids if order_by_eid[eid][cid] == 1]
        if support != c3_exc[cid]["nonzero_exceptional_ids"]:
            raise SystemExit(f"C3 exceptional support replay mismatch: {cid}")

    exceptional_rows = []
    exceptional_zero_parity_count = 0
    for eid in expected_eids:
        valuation = order_by_eid[eid]
        odd, sign, vpi, vf = residue_parity_for_valuation_vector(carrier_ids, components, pi, ff, valuation)
        if not odd:
            exceptional_zero_parity_count += 1
        exceptional_rows.append({
            "exceptional_id": eid,
            "nonzero_carrier_valuation_ids": sorted(cid for cid, v in valuation.items() if v),
            "combined_tame_residue_odd_linear_carrier_ids": odd,
            "combined_tame_residue_carrier_parity_zero": not odd,
            "tame_sign_parity": sign,
            "minus_one_is_square_in_Qi_so_tame_sign_does_not_obstruct_squaretriviality": True,
            "v_pi_by_symbol_component": vpi,
            "v_f_by_symbol_component": vf,
            "squareclass_conclusion": (
                "SQUARE_TRIVIAL_BY_EVEN_LINEAR_FACTOR_PARITY" if not odd
                else "OPEN_NONZERO_FORMAL_LINEAR_FACTOR_PARITY_REQUIRES_EXCEPTIONAL_RESIDUE_FIELD_RELATIONS"
            ),
        })

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4a.tame_residue_parity_and_cross_carrier_preflight.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4A_TAME_RESIDUE_PARITY_AND_CROSS_CARRIER_PREFLIGHT",
        "role": "EXACT_NONCREDIT_C4_PREFLIGHT_SPLITTING_CERTIFIED_FACTOR_PARITY_FROM_REPEATED_FACTOR_CROSS_CARRIER_INCIDENCE_AND_EXCEPTIONAL_RESIDUE_FIELD_GAPS",
        "entry": {"pr": 1695, "authority": AUTHORITY, "stage33_progress": "6/11"},
        "source_locks": {
            "r5b3b2_formal_symbol_carrier_inventory_sha256": B3B2_SHA,
            "r5b3b3c3_factor_prime_exceptional_attachment_sha256": C3_SHA,
            "frozen_exceptional_source_sha256": b3b1.atlas.EXC_SHA,
        },
        "formal_symbol_input": {
            "symbol_component_count": len(components),
            "component_ids_in_source_order": components,
            "projective_linear_carrier_count": len(carrier_ids),
            "carrier_ids": carrier_ids,
            "tame_residue_formula_mod_square": "(-1)^(v(pi)*v(f))*pi^v(f)/f^v(pi)",
            "linear_factor_parity_zero_is_a_sufficient_squaretriviality_certificate_after_any_residue_specialization": True,
            "the_converse_is_not_claimed": True,
        },
        "strict_prime_preflight": {
            "carrier_factor_incidence_row_count": len(adapter_rows),
            "unique_c1_factor_count": len(factor_groups),
            "repeated_c1_factor_group_count": len(repeated_groups),
            "repeated_factor_groups": repeated_groups,
            "unique_factor_context_row_count": unique_factor_rows,
            "unique_factor_context_zero_formal_parity_row_count": unique_factor_zero_parity_rows,
            "repeated_factor_context_row_count_requiring_cross_carrier_geometric_incidence": unresolved_repeated_rows,
            "rows": strict_rows,
            "no_false_inference_from_context_local_prime_id_inequality": True,
        },
        "exceptional_prime_preflight": {
            "frozen_exceptional_prime_count": len(expected_eids),
            "all_formal_symbol_carriers_rees_replayed": True,
            "standard_rees_charts_per_node": 6,
            "exact_linear_factor_rees_order_checks": rees_checks,
            "c3_offboundary_23_carrier_exceptional_support_replayed_exact": True,
            "zero_formal_linear_factor_parity_exceptional_prime_count": exceptional_zero_parity_count,
            "rows": exceptional_rows,
        },
        "construction_status": {
            "combined_tame_residue_factor_parity_preflight_materialized": True,
            "repeated_factor_cross_carrier_geometric_prime_incidence_materialized": False,
            "residue_field_squareclass_relations_for_nonzero_formal_parity_rows_materialized": False,
            "combined_tame_residue_squareclasses_audited_on_every_strict_and_exceptional_prime": False,
            "offboundary_codimension_one_residue_cancellation_verified": False,
            "unramifiedness_verified": False,
        },
        "exact_consequence": {
            "strict_prime_work_is_partitioned_into_unique_factor_contexts_and_repeated_factor_cross_carrier_contexts": True,
            "exceptional_prime_formal_factor_parity_is_computed_from_all_formal_symbol_carriers_on_all_48_frozen_nodes": True,
            "zero_linear_factor_parity_rows_are_exact_squaretriviality_certificates_over_Qi": True,
            "nonzero_parity_rows_are_not_declared_nontrivial_because_residue_field_relations_may_still_make_them_squares": True,
        },
        "next_missing_object": "EXACT_CROSS_CARRIER_INCIDENCE_FOR_REPEATED_C1_FACTOR_GROUPS_THEN_RESIDUE_FIELD_SQUARECLASS_REDUCTION_ONLY_ON_THE_REMAINING_NONZERO_FORMAL_PARITY_STRICT_OR_EXCEPTIONAL_ROWS",
        "next_exact_leaf": "V91C1X_R5B3B3C4B_REPEATED_FACTOR_CROSS_CARRIER_INCIDENCE_AND_TARGETED_RESIDUE_FIELD_SQUARECLASS_REDUCTION",
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


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build_certificate()
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    else:
        current = json.loads(OUT.read_text(encoding="utf-8"))
        if current != cert:
            raise SystemExit("materialized C4A artifact is stale")
    print(json.dumps({
        "success": True,
        "marker": "V91C1X_R5B3B3C4A_TAME_RESIDUE_PARITY_PREFLIGHT_EXACT",
        "canonical_sha256": cert["canonical_sha256"],
        "unique_factor_zero_parity": cert["strict_prime_preflight"]["unique_factor_context_zero_formal_parity_row_count"],
        "unique_factor_rows": cert["strict_prime_preflight"]["unique_factor_context_row_count"],
        "repeated_factor_groups": cert["strict_prime_preflight"]["repeated_c1_factor_group_count"],
        "exceptional_zero_parity": cert["exceptional_prime_preflight"]["zero_formal_linear_factor_parity_exceptional_prime_count"],
        "exceptional_total": 48,
        "next_exact_leaf": cert["next_exact_leaf"],
        "stage33_progress": "6/11",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
