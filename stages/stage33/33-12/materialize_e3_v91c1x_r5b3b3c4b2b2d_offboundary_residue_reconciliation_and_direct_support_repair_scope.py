#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

B1 = HERE / "e3-v91c1x-r5b3b3c4b2b1-explicit-a1-boundary-residue-field-squareclass.json"
B2 = HERE / "e3-v91c1x-r5b3b3c4b2b2-remaining24-strict-prime-squareclass-partition.json"
F4 = HERE / "e3-v91c1x-r5b3b3c4b2b2a-f4-pair-multiquadratic-residue-norm-witness.json"
F14 = HERE / "e3-v91c1x-r5b3b3c4b2b2b-f14-four-residual-prime-residue-norm-witness.json"
D16 = HERE / "e3-v91c1x-r5b3b3c4b2b2c-unique-degree16-residue-norm-sweep.json"
C1 = HERE / "e3-v91c1x-r5b3b3c4b2b2c1-inherited-direct-support-primality-recheck.json"
C2 = HERE / "e3-v91c1x-r5b3b3c4b2b2c2-lin024-actual-four-component-prime-incidence.json"
C3 = HERE / "e3-v91c1x-r5b3b3c4b2b2c3-lin024-four-component-biquadratic-residue-norm.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b2b2d-offboundary-residue-reconciliation-and-direct-support-repair-scope.json"

B1_SHA = "bc13cb417addcfbd05616c9cff1f8ae73ba286071b2f6ebbda9144ec0eeb9de3"
B2_SHA = "c35b8737bd310935c844b170975617e69f2745b60a932349b3c297dd6909fb27"
F4_SHA = "0defae3bd0bd809bcee4ab22fadf159b168a43c987c903b734d14f7b01478769"
F14_SHA = "6949358e0bd577a9538bc09e662682240c571f7909b0b9feb02eea6efa0c7e08"
D16_SHA = "92fdf2bc96ff0f00c2200cef63a1270b96e6962a6022e0cd5fb2ed361ba8bb3a"
C1_SHA = "64e25e200f4f0188731a6c85e1e69e6eae85a759403ac0d984309b3dca881b39"
C2_SHA = "68d1be09543e79e210dc3e1e13d9f3e9cee3eb08d1b576238b5889e2a995e59f"
C3_SHA = "0d2a5dd5312f1754d1e13a012848cea2d1ef973bfafe9409f801c5bdc9084d50"
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"canonical source lock moved {path.name}: claimed={claimed} actual={actual} expected={expected}")
    return obj


def build() -> dict:
    b1 = load(B1, B1_SHA)
    b2 = load(B2, B2_SHA)
    f4 = load(F4, F4_SHA)
    f14 = load(F14, F14_SHA)
    d16 = load(D16, D16_SHA)
    c1 = load(C1, C1_SHA)
    c2 = load(C2, C2_SHA)
    c3 = load(C3, C3_SHA)

    if not b1["exact_consequence"]["all_four_are_nonsquare"]:
        raise SystemExit("C4B2B1 four-boundary negative checkpoint moved")
    if b1["method"]["target_prime_count"] != 4:
        raise SystemExit("C4B2B1 boundary target count moved")
    if b2["remaining24_partition"]["bucket_sizes"] != {
        "F14_RESIDUAL_REPEATED_FACTOR_STRICT_PRIMES": 4,
        "F4_REPEATED_FACTOR_PAIR_STRICT_PRIMES": 2,
        "UNIQUE_C1_FACTOR_STRICT_PRIMES": 18,
    }:
        raise SystemExit("C4B2B2 old remaining24 partition moved")
    if b2["exact_consequence"]["remaining_strict_prime_squareclass_debt_count"] != 24:
        raise SystemExit("C4B2B2 old debt count moved")
    if f4["exact_consequence"]["F4_pair_residue_nonsquare_certified_count"] != 2:
        raise SystemExit("F4 result moved")
    if f14["exact_consequence"]["F14_four_residue_nonsquare_certified_count"] != 4:
        raise SystemExit("F14 result moved")
    if d16["degree16_sweep"]["nonsquare_by_norm_count"] != 16 or d16["degree16_sweep"]["inconclusive_count"] != 0:
        raise SystemExit("degree16 sweep moved")
    if d16["exact_consequence"]["remaining_strict_prime_squareclass_debt_count"] != 2:
        raise SystemExit("pre-repair LIN024 two-label debt marker moved")
    recheck = c1["inherited_direct_recheck"]
    if recheck["direct_carrier_count"] != 6 or recheck["recorded_support_pseudo_prime_count"] != 9:
        raise SystemExit("33-11D inherited direct-support recheck inventory moved")
    if not recheck["all_nine_recorded_support_quotients_non_domains"]:
        raise SystemExit("33-11D support primality diagnosis moved")
    if c2["component_refinement"]["actual_height_one_prime_count"] != 4 or not c2["component_refinement"]["all_four_actual_component_ideals_prime"]:
        raise SystemExit("LIN024 actual four-prime refinement moved")
    if c2["incidence_summary"]["components_with_extra_formal_carrier_incidence"] != 0:
        raise SystemExit("LIN024 formal-carrier incidence moved")
    if c3["componentwise_result"]["actual_prime_count"] != 4 or c3["componentwise_result"]["nonsquare_certified_count"] != 4 or c3["componentwise_result"]["inconclusive_count"] != 0:
        raise SystemExit("LIN024 four-prime squareclass result moved")
    if not c3["exact_consequence"]["lin024_old_two_support_label_squareclass_debt_retired"]:
        raise SystemExit("LIN024 old support debt was not retired")

    old_total_slots = 4 + 24
    corrected_remaining_actual_prime_slots = 2 + 4 + 16 + 4
    corrected_total_actual_prime_test_slots = 4 + corrected_remaining_actual_prime_slots
    if old_total_slots != 28 or corrected_remaining_actual_prime_slots != 26 or corrected_total_actual_prime_test_slots != 30:
        raise SystemExit("corrected C4B2B slot arithmetic regression")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b2b2d.offboundary_residue_reconciliation_and_direct_support_repair_scope.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B2B2D_OFFBOUNDARY_RESIDUE_CLASSIFICATION_RECONCILIATION_AND_DIRECT_SUPPORT_REPAIR_SCOPE",
        "role": "EXACT_NONCREDIT_RECONCILIATION_OF_THE_C4B2B_RESIDUE_LEDGER_AFTER_REPLACING_TWO_NONPRIME_LIN024_SUPPORT_LABELS_BY_FOUR_ACTUAL_HEIGHT_ONE_PRIMES_AND_ISOLATING_THE_SEPARATE_STAGE33_11E_DIRECT_SUPPORT_REPAIR_DEBT",
        "entry": {"authority": AUTH, "stage33_progress": "6/11", "successor_pr": 1722},
        "source_locks": {
            "c4b2b1_explicit_boundary_sha256": B1_SHA,
            "c4b2b2_old_remaining24_partition_sha256": B2_SHA,
            "c4b2b2a_f4_sha256": F4_SHA,
            "c4b2b2b_f14_sha256": F14_SHA,
            "c4b2b2c_degree16_sha256": D16_SHA,
            "c4b2b2c1_direct_support_primality_recheck_sha256": C1_SHA,
            "c4b2b2c2_lin024_actual_prime_incidence_sha256": C2_SHA,
            "c4b2b2c3_lin024_actual_prime_squareclass_sha256": C3_SHA,
        },
        "old_support_level_ledger": {
            "reported_total_target_slots": old_total_slots,
            "explicit_a1_boundary_actual_prime_slots": 4,
            "reported_remaining_slots": 24,
            "reported_remaining_bucket_sizes": {
                "F4": 2,
                "F14": 4,
                "UNIQUE_DEGREE16": 16,
                "LIN024_DIRECT_SUPPORT_LABELS": 2,
            },
            "prime_exact": False,
            "defect": "the two LIN024 direct-support labels were not domains and therefore were not actual residue-field prime targets",
        },
        "corrected_actual_prime_test_ledger": {
            "explicit_a1_boundary_actual_prime_slots": 4,
            "F4_actual_prime_slots": 2,
            "F14_actual_prime_slots": 4,
            "unique_degree16_actual_prime_slots": 16,
            "LIN024_actual_component_prime_slots": 4,
            "corrected_remaining_actual_prime_test_slots": corrected_remaining_actual_prime_slots,
            "corrected_total_actual_prime_test_slots": corrected_total_actual_prime_test_slots,
            "nonsquare_certified_slots": corrected_total_actual_prime_test_slots,
            "inconclusive_slots": 0,
            "all_corrected_tested_actual_prime_slots_have_nontrivial_tame_residue_squareclass": True,
            "cross_bucket_prime_id_distinctness_reproved_in_this_reconciliation": False,
            "count_semantics": "test slots inherited from disjoint construction buckets; this reconciliation does not add a new global prime-id deduplication proof",
        },
        "current_literal_candidate_consequence": {
            "already_ramified_before_this_reconciliation": True,
            "current_literal_eight_symbol_candidate_cannot_be_unramified": True,
            "this_negative_result_is_about_the_current_literal_formal_symbol_representative": True,
            "this_does_not_negate_other_representatives_or_the_stage33_endpoint": True,
            "offboundary_codimension_one_residue_cancellation_verified": False,
            "unramifiedness_verified": False,
        },
        "stage33_11e_direct_support_repair_scope": {
            "historical_inherited_direct_carrier_count": 6,
            "historical_support_labels_consumed_as_prime_ids": 9,
            "all_nine_support_label_quotients_non_domains": True,
            "LIN024_support_labels_with_actual_component_refinement_now_materialized": 2,
            "LIN024_actual_component_primes_materialized": 4,
            "support_labels_still_without_actual_component_refinement": 7,
            "historical_stage33_11e_prime_level_transport_certificate_requires_replay_after_all_direct_supports_are_refined": True,
            "historical_stage33_11f_26_column_closure_should_not_be_reused_as_prime_exact_repair_evidence_without_that_replay": True,
            "current_V91C1V_authority_demotion_claimed_here": False,
            "repair_is_separate_from_the_corrected_C4B2B_squareclass_ledger": True,
        },
        "checkpoint_policy": {
            "same_successor_pr": 1722,
            "retained_accumulation_should_stop_before_another_large_chain": True,
            "reason": "successor PR is near the bounded retained-surface limit and now contains a structural upstream direct-support primality diagnosis; perform the intended audit/repair checkpoint before broad continuation",
            "merge_allowed": False,
        },
        "exact_consequence": {
            "C4B2B_old_28_target_accounting_replaced_by_corrected_prime_exactness_aware_ledger": True,
            "old_LIN024_two_support_squareclass_debt_retired": True,
            "corrected_LIN024_four_actual_prime_residues_all_nonsquare": True,
            "F4_F14_degree16_results_retained": True,
            "stage33_11e_direct_support_repair_debt_explicitly_separated": True,
            "authority_unchanged": True,
            "stage33_progress_unchanged": True,
        },
        "next_exact_leaf": "V91C1X_R5_DIRECT_SUPPORT_PRIME_REPAIR_CHECKPOINT_REFINE_REMAINING_SEVEN_SUPPORT_LABELS_THEN_REPLAY_STAGE33_11E_PRIME_TRANSPORT_BEFORE_FURTHER_LARGE_ACCUMULATION",
        "credit_firewall": {
            "authority_promotion": False,
            "authority_demotion_claim": False,
            "hostile_audit_credit": False,
            "marked_brauer_image_credit": False,
            "offboundary_cancellation_credit": False,
            "unramifiedness_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
        print(json.dumps({
            "success": True,
            "marker": cert["candidate"],
            "corrected_total_actual_prime_test_slots": cert["corrected_actual_prime_test_ledger"]["corrected_total_actual_prime_test_slots"],
            "nonsquare_certified_slots": cert["corrected_actual_prime_test_ledger"]["nonsquare_certified_slots"],
            "remaining_unrefined_direct_support_labels": cert["stage33_11e_direct_support_repair_scope"]["support_labels_still_without_actual_component_refinement"],
            "next_exact_leaf": cert["next_exact_leaf"],
            "certificate_sha256": cert["canonical_sha256"],
        }, sort_keys=True))
        return
    if not OUT.exists():
        raise SystemExit(f"missing materialized certificate: {OUT}")
    if json.loads(OUT.read_text(encoding="utf-8")) != cert:
        raise SystemExit("materialized C4B2B2D certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
