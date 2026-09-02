#!/usr/bin/env python3
from __future__ import annotations

# Merge-audit replay trigger after V10 provenance-chain repair; no mathematical change.

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
AUDIT = HERE / "v10-hostile-audit-pass-receipt.json"
GAP = HERE / "j2-named-order4-actual-s3-source-lock-gap-v10.json"

LOCKS = {
    "bridge": (STAGE / "33-07/marked-picard-basis-bridge-certified.json", "039e3792e950ac5bf94adf6538c229640da231000a5e1b159a80e2323a812a92"),
    "receipt": (HERE / "qpic-bridge-local-recertification-receipt.json", "c6e9466c509699b1ef2c037ad248915673d391f00115032782970667f44e7dd0"),
    "swap": (HERE / "j2-actual-swap-mixed-discriminant-descent.json", "93dc99201a04fdec7c8ad8369409e7cb593ae7f8fba44b772df1b2cc1d29cfa3"),
    "old_gap": (HERE / "j2-marked-order4-lift-label-gap.json", "4ca10da7ea214258dd57d1e42c2dc7ea7b66ae29c8cfd5b75ecd6a3eb0fd0101"),
    "orientation": (HERE / "j2-cv-d2-semantic-orientation.json", "0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e"),
    "order4": (HERE / "j2-order4-brauer-lift-reduction.json", "a524121930e1c712bd8d8220415ef1836b11cd6eb11f2bb44f70dc844f6d85b0"),
}
EXPECTED_AUDIT = "5bef940bf55dd480acb8fc3a75415470d28ee9eaa1473c3476d8bd6463ca89e1"
EXPECTED_GAP = "92502f0cb5d04cac6ed6b95270d9b844870a239dd5aaa2a3eeb535a74bac3f2e"


def csha(x: dict) -> str:
    y = dict(x)
    got = y.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(y, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == calc
    return got


def load_locked(path: Path, expected: str) -> dict:
    x = json.loads(path.read_text())
    assert csha(x) == expected, path
    return x


audit = load_locked(AUDIT, EXPECTED_AUDIT)
gap = load_locked(GAP, EXPECTED_GAP)
locked = {k: load_locked(p, h) for k, (p, h) in LOCKS.items()}

assert audit["status"] == "PASS_HOSTILE_AUDIT"
assert audit["audited_pr"] == 1476
assert audit["audited_head_sha"] == "088a0e5e3b0baefc0be016a9ba70a00b31c7aedc"
assert audit["audit_review_id"] == 5083583438
assert audit["merge_commit_sha"] == "9b97f0795d297e8afdbea56e3bf6ff3608c78639"
assert audit["pass_boundary"]["unique_joint_s3_fixed_candidate_retained10_mask_decimal"] == 6
assert audit["pass_boundary"]["named_j2_source_label_selected"] is False

assert gap["status"] == "PASS_EXACT_V10_POST_AUDIT_SOURCE_LOCK_GAP_REFINED_NO_LABEL_INFERENCE"
assert gap["audit_receipt_sha256"] == EXPECTED_AUDIT
assert gap["authoritative_v10_facts"]["residual_order4_candidate_masks_retained10"] == [4, 5, 6, 7]
assert gap["authoritative_v10_facts"]["unique_joint_s3_fixed_candidate_retained10_mask_decimal"] == 6
assert gap["authoritative_v10_facts"]["named_j2_order4_lift_selected"] is False
assert gap["targeted_source_audit"]["exact_name_matches_for_Magma_interface_m"] == []
assert gap["targeted_source_audit"]["exact_name_matches_for_load_Qtriv_m"] == []
assert gap["no_inference"]["unique_joint_s3_fixed_candidate_implies_named_j2_mask6"] is False
assert gap["promotion_firewall"]["matrix_standard_columns_materialized"] == 0
assert gap["promotion_firewall"]["stage33_12_closed_exact"] is False

swap = locked["swap"]
assert swap["residual_order4_affine_candidate_S3_action"]["unique_joint_fixed_retained10_mask_decimal"] == 6
assert swap["exact_consequence"]["historical_mask6_reused_as_named_J2_source"] is False

print(json.dumps({
    "success": True,
    "audit_receipt_sha256": EXPECTED_AUDIT,
    "gap_sha256": EXPECTED_GAP,
    "named_j2_source_label_selected": False,
    "unique_joint_s3_fixed_candidate_retained10_mask_decimal": 6,
}, sort_keys=True))
