#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
C4A = HERE / "e3-v91c1x-r5b3b3c4a-tame-residue-parity-and-cross-carrier-preflight.json"
C4B1 = HERE / "e3-v91c1x-r5b3b3c4b1-exceptional-p1-targeted-residue-field-squareclass.json"
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1a-exceptional-nonsquare-obstruction-census-and-correction-preflight.json"

C4A_SHA = "fab3f7b1235370a3916b99b6909cd6c6363193ff271ee6b51cb9494b0668e525"
C4B1_SHA = "f14d9ca73ad0f0cbcf052c4512603bcc0942fb9263f97535023e8050ffcdced4"
B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"

ZERO = "SQUARE_TRIVIAL_BY_C4A_ZERO_FORMAL_LINEAR_FACTOR_PARITY"
SQUARE = "SQUARE_TRIVIAL_AFTER_EXACT_EXCEPTIONAL_P1_RESIDUE_FIELD_REDUCTION"
NONSQUARE = "NONSQUARE_AFTER_EXACT_EXCEPTIONAL_P1_RESIDUE_FIELD_REDUCTION"


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(
            f"canonical source lock moved: {path.name}: "
            f"claimed={claimed} actual={actual} expected={expected}"
        )
    return obj


def grouped_rows(items: list[dict], key: str) -> list[dict]:
    groups: dict[str, list[str]] = defaultdict(list)
    for row in items:
        groups[row[key]].append(row["exceptional_id"])
    return [
        {
            "signature_sha256": sig,
            "exceptional_count": len(eids),
            "exceptional_ids": sorted(eids),
        }
        for sig, eids in sorted(groups.items())
    ]


def build_certificate() -> dict:
    c4a = load_locked(C4A, C4A_SHA)
    c4b1 = load_locked(C4B1, C4B1_SHA)
    b3b2 = load_locked(B3B2, B3B2_SHA)

    summary = c4b1["exceptional_squareclass_reduction"]
    rows = list(summary["rows"])
    if len(rows) != 48:
        raise SystemExit("C4B1 exceptional row count moved")
    if summary["c4a_zero_formal_parity_count"] != 7:
        raise SystemExit("C4B1 zero-parity count moved")
    if summary["targeted_nonzero_formal_parity_count"] != 41:
        raise SystemExit("C4B1 targeted count moved")
    if summary["targeted_square_trivial_count"] != 10:
        raise SystemExit("C4B1 targeted-square count moved")
    if summary["targeted_nonsquare_count"] != 31:
        raise SystemExit("C4B1 targeted-nonsquare count moved")

    classes = defaultdict(list)
    for row in rows:
        classes[row["classification"]].append(row)
    if set(classes) != {ZERO, SQUARE, NONSQUARE}:
        raise SystemExit(f"C4B1 classification vocabulary moved: {sorted(classes)}")
    if [len(classes[ZERO]), len(classes[SQUARE]), len(classes[NONSQUARE])] != [7, 10, 31]:
        raise SystemExit("C4B1 7+10+31 partition moved")

    c4a_rows = c4a["exceptional_prime_preflight"]["rows"]
    c4a_by_eid = {row["exceptional_id"]: row for row in c4a_rows}
    if len(c4a_by_eid) != 48:
        raise SystemExit("C4A exceptional inventory moved")

    obstruction_rows = []
    for row in sorted(classes[NONSQUARE], key=lambda x: x["exceptional_id"]):
        eid = row["exceptional_id"]
        arow = c4a_by_eid[eid]
        if arow["combined_tame_residue_carrier_parity_zero"] is not False:
            raise SystemExit(f"nonsquare row became C4A parity-zero: {eid}")
        if row["square_trivial_in_Qi_exceptional_function_field"] is not False:
            raise SystemExit(f"nonsquare row became square-trivial: {eid}")

        sq = row["combined_residue_squareclass"]
        factors = sorted(
            [
                {
                    "degree": int(f["degree"]),
                    "projective_factor_sha256": f["projective_factor_sha256"],
                }
                for f in sq["odd_irreducible_factors"]
            ],
            key=lambda x: (x["degree"], x["projective_factor_sha256"]),
        )
        if len(factors) != int(sq["odd_irreducible_factor_count"]):
            raise SystemExit(f"odd-factor count mismatch: {eid}")
        if bool(sq["square_trivial"]):
            raise SystemExit(f"nonsquare row has square_trivial=true: {eid}")

        odd_support = sorted(row["c4a_odd_carrier_ids"])
        order_one = sorted(row["odd_carrier_exceptional_order_one_ids"])
        order_zero = sorted(row["odd_carrier_exceptional_order_zero_ids"])
        if sorted(order_one + order_zero) != odd_support:
            raise SystemExit(f"order support does not partition odd support: {eid}")

        exact_local_presentation = {
            "factorization_coefficient_Qi": sq["factorization_coefficient_Qi"],
            "coefficient_is_square_in_Qi": bool(sq["coefficient_is_square_in_Qi"]),
            "odd_irreducible_factors": factors,
        }
        factor_parity_pattern = {
            "coefficient_is_square_in_Qi": bool(sq["coefficient_is_square_in_Qi"]),
            "odd_irreducible_factors": factors,
        }
        obstruction_rows.append({
            "exceptional_id": eid,
            "combined_residue_representative_Qi_t_sha256": row["combined_residue_representative_Qi_t_sha256"],
            "frozen_tangent_model_sha256": row["frozen_tangent_model_sha256"],
            "deterministic_p1_parametrization_sha256": row["deterministic_p1_parametrization_sha256"],
            "c4a_odd_carrier_ids": odd_support,
            "odd_carrier_exceptional_order_one_ids": order_one,
            "odd_carrier_exceptional_order_zero_ids": order_zero,
            "combined_residue_squareclass": exact_local_presentation,
            "exact_local_presentation_sha256": csha(exact_local_presentation),
            "factor_parity_pattern_sha256": csha(factor_parity_pattern),
            "odd_carrier_support_sha256": csha(odd_support),
            "order_one_support_sha256": csha(order_one),
        })

    if len(obstruction_rows) != 31:
        raise SystemExit("obstruction census lost a C4B1 nonsquare row")

    bstatus = b3b2["construction_status"]
    correction_prerequisites = [
        "single_global_a2_02_kummer_or_brauer_representative_materialized",
        "line_bundle_gm_1_cocycle_ell_ij_materialized",
        "square_root_1_cochain_r_ij_materialized",
        "literal_mu2_2_cocycle_materialized",
        "equivalent_unimodular_cech_glue_materialized",
        "same_representative_swap23_transport_materialized",
        "triple_overlap_action_difference_identity_verified",
    ]
    prereq_state = {key: bool(bstatus[key]) for key in correction_prerequisites}
    if any(prereq_state.values()):
        raise SystemExit("B3B2 correction-space prerequisite unexpectedly became materialized")

    exact_groups = grouped_rows(obstruction_rows, "exact_local_presentation_sha256")
    parity_groups = grouped_rows(obstruction_rows, "factor_parity_pattern_sha256")
    support_groups = grouped_rows(obstruction_rows, "odd_carrier_support_sha256")
    order_one_groups = grouped_rows(obstruction_rows, "order_one_support_sha256")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1a.exceptional_nonsquare_obstruction_census_and_correction_preflight.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1A_EXCEPTIONAL_NONSQUARE_OBSTRUCTION_CENSUS_AND_CORRECTION_PREFLIGHT",
        "role": "EXACT_NONCREDIT_CENSUS_OF_C4B1_EXCEPTIONAL_RAMIFICATION_AND_SOURCE_BOUND_CORRECTION_SPACE_PREFLIGHT",
        "entry": {
            "pr": 1695,
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
        },
        "source_locks": {
            "r5b3b3c4a_tame_residue_parity_preflight_sha256": C4A_SHA,
            "r5b3b3c4b1_exceptional_p1_squareclass_sha256": C4B1_SHA,
            "r5b3b2_formal_symbol_carrier_inventory_sha256": B3B2_SHA,
        },
        "exceptional_obstruction_census": {
            "frozen_exceptional_prime_count": 48,
            "c4a_zero_formal_parity_count": 7,
            "targeted_square_trivial_count": 10,
            "targeted_nonsquare_obstruction_count": 31,
            "current_candidate_square_or_trivial_exceptional_count": 17,
            "current_candidate_ramified_exceptional_count": 31,
            "nonsquare_obstruction_rows": obstruction_rows,
            "exact_local_presentation_group_count": len(exact_groups),
            "exact_local_presentation_groups": exact_groups,
            "factor_parity_pattern_group_count": len(parity_groups),
            "factor_parity_pattern_groups": parity_groups,
            "odd_carrier_support_group_count": len(support_groups),
            "odd_carrier_support_groups": support_groups,
            "order_one_support_group_count": len(order_one_groups),
            "order_one_support_groups": order_one_groups,
        },
        "interpretation_firewall": {
            "equal_local_presentation_hashes_across_distinct_exceptional_p1_parameterizations_are_not_claimed_to_be_identical_global_geometric_squareclasses": True,
            "carrier_surface_actions_are_not_promoted_here_to_a_certified_permutation_action_on_the_48_exceptional_ids": True,
            "this_leaf_does_not_claim_an_exceptional_orbit_reduction_without_a_source_locked_exceptional_prime_action_adapter": True,
            "the_31_rows_are_an_obstruction_to_the_current_formal_symbol_candidate_not_a_nonexistence_proof_for_all_corrected_candidates": True,
        },
        "correction_preflight": {
            "b3b2_correction_prerequisite_state": prereq_state,
            "source_bound_correction_space_materialized": False,
            "auditable_allowed_correction_cochain_materialized": False,
            "existence_of_a_permitted_correction_killing_all_31_exceptional_classes_determined": False,
            "arbitrary_free_correction_variables_may_not_be_invented_from_the_31_local_rows": True,
            "reason": "B3B2 does not yet materialize a single global representative or the Cech/Kummer cochain data needed to define the allowed source-bound correction space.",
        },
        "construction_status": {
            "all_31_c4b1_nonsquare_exceptional_rows_censused_exactly": True,
            "local_presentation_and_carrier_support_fingerprints_materialized": True,
            "certified_exceptional_prime_action_adapter_materialized": False,
            "source_bound_correction_space_materialized": False,
            "corrected_formal_symbol_candidate_materialized": False,
            "exceptional_residue_cancellation_verified": False,
            "strict_prime_repeated_factor_cross_carrier_incidence_materialized": False,
            "strict_prime_residue_field_squareclasses_materialized": False,
            "all_codimension_one_residue_cancellation_verified": False,
            "unramifiedness_verified": False,
        },
        "exact_consequence": {
            "current_formal_symbol_candidate_has_31_exact_nonsquare_exceptional_residues": True,
            "current_formal_symbol_candidate_is_not_unramified": True,
            "no_source_bound_correction_can_yet_be_audited_because_the_allowed_correction_space_is_not_materialized": True,
            "c4b2_strict_prime_work_remains_separately_outstanding": True,
        },
        "next_missing_object": "SOURCE_BOUND_A2_02_CECH_KUMMER_CORRECTION_SPACE_OR_ALLOWED_CORRECTION_COCHAIN_MATERIALIZATION_THEN_EXCEPTIONAL_RESIDUE_REPLAY",
        "parallel_outstanding_leaf": "V91C1X_R5B3B3C4B2_STRICT_PRIME_CROSS_CARRIER_INCIDENCE_AND_RESIDUE_FIELD_SQUARECLASS_REDUCTION",
        "next_exact_leaf": "V91C1X_R5B3B3C4B1B_SOURCE_BOUND_CORRECTION_SPACE_PREFLIGHT",
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
        if not OUT.exists():
            raise SystemExit("materialized C4B1A artifact is missing")
        current = json.loads(OUT.read_text(encoding="utf-8"))
        if current != cert:
            raise SystemExit("materialized C4B1A artifact is stale")
    census = cert["exceptional_obstruction_census"]
    print(json.dumps({
        "success": True,
        "marker": "V91C1X_R5B3B3C4B1A_EXCEPTIONAL_OBSTRUCTION_CENSUS_EXACT",
        "canonical_sha256": cert["canonical_sha256"],
        "nonsquare_obstruction_count": census["targeted_nonsquare_obstruction_count"],
        "exact_local_presentation_group_count": census["exact_local_presentation_group_count"],
        "factor_parity_pattern_group_count": census["factor_parity_pattern_group_count"],
        "odd_carrier_support_group_count": census["odd_carrier_support_group_count"],
        "order_one_support_group_count": census["order_one_support_group_count"],
        "source_bound_correction_space_materialized": False,
        "next_exact_leaf": cert["next_exact_leaf"],
        "stage33_progress": "6/11",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
