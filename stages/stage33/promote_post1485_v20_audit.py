#!/usr/bin/env python3
"""Verify the already-promoted #1485 v17-v20 Stage33 boundary.

The one-shot promotion is complete. This historical helper is deliberately
read-only and verifies only immutable #1485 evidence plus global no-release
firewalls. Later Stage33 leaf/schema changes must not make this replay stale.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

H = Path(__file__).resolve().parent
C_PATH = H / "controller.json"
R_PATH = H / "33-12/v20-hostile-audit-pass-receipt.json"

AUDIT_SCOPE = "STAGE33_12_V17_V20_ORDER4_TWO_BIT_GAP_HOSTILE_AUDIT"
AUDIT_HEAD = "2f3a511f945a22c1df58eaf68553cbb70d4a207c"
AUDIT_REVIEW = 5086169445
MERGE_COMMIT = "dc6b19ea5944c1c249f6d9534a095ffad9ae8f67"
RECEIPT_SHA = "2d65169174d636a93d68f7c2fe4dd1fef322dcd7598459253460631648dd9927"
NEXT = "SOURCE_LOCK_NAMED_J2_ORDER4_LIFT_ACTUAL_SWAP12_SWAP13_BEHAVIOR_OR_EQUIVALENT_TWO_BIT_VALUE_A_B; DO_NOT_SELECT_MASK6_WITHOUT_SOURCE"


def csha(x):
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def canonical(path: Path, expected: str):
    x = json.loads(path.read_text())
    body = dict(x)
    got = body.pop("canonical_sha256")
    assert got == expected == csha(body), path
    return x


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--continuation-pr", type=int, default=1488)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    assert a.continuation_pr == 1488

    canonical(
        H / "33-12/j2-order4-row20-row67-exact-source-lock-v17.json",
        "04b47064db73e02068aa51301c94ab0576d927c0b71b2d3df093012028f061d2",
    )
    canonical(
        H / "33-12/j2-order4-source-coordinate-v18.json",
        "a0378a7d7191d537347435d11002faa3692f91781dd15f53fe3063443e9d50d1",
    )
    canonical(
        H / "33-12/j2-order4-integral-correction-torsor-v19.json",
        "3ee11e0ecdc855083a4260c2ae4f24ef4c160a7e26a48fd3872369d117118576",
    )
    v20 = canonical(
        H / "33-12/j2-order4-named-functional-quotient-v20.json",
        "1b53db254c381721c0c648bab41c276ec79f69f6e1f81235993936df3e25232e",
    )
    receipt = canonical(R_PATH, RECEIPT_SHA)
    c = json.loads(C_PATH.read_text())
    s = c["stage33_12"]

    # Immutable #1485 hostile-audit receipt.
    assert receipt["status"] == "PASS_HOSTILE_AUDIT"
    assert receipt["audit_scope"] == AUDIT_SCOPE
    assert receipt["audit_review_id"] == AUDIT_REVIEW
    assert receipt["audited_head_sha"] == AUDIT_HEAD
    assert receipt["merge_commit_sha"] == MERGE_COMMIT
    assert receipt["next_exact_leaf"] == NEXT
    assert receipt["pass_boundary"]["named_j2_source_label_selected"] is False
    assert receipt["pass_boundary"]["named_75d_column_materialized"] is False
    assert receipt["pass_boundary"]["kummer_standard_columns_materialized"] == 0

    # Immutable v20 mathematical boundary. Later v21+ work may legitimately
    # select the named source, so this helper must not assert current leaf flags.
    assert v20["status"] == "PASS_EXACT_NAMED_COLUMN_GAP_REDUCED_TO_TWO_BITS"
    assert v20["actual_s3_action_on_two_bit_quotient"]["orbits"] == [[6], [4, 5, 7]]
    assert v20["actual_s3_action_on_two_bit_quotient"]["named_mask_selected"] is False

    # Current controller only has to retain the audited historical boundary and
    # the global no-release firewalls. Do not pin its evolving schema/next leaf.
    assert c["stage33_progress"] == "6/11"
    assert c["last_completed_audit_scope"] == AUDIT_SCOPE
    assert c["last_completed_audit_review_id"] == AUDIT_REVIEW
    assert c["last_completed_audit_head_sha"] == AUDIT_HEAD
    assert s["v20_hostile_audit_pass_receipt_sha256"] == RECEIPT_SHA

    assert c["merge_allowed"] is False
    assert c["release_gates"]["stage33_12_closed_exact"] is False
    assert c["release_gates"]["stage33_07_reclosed"] is False
    assert c["release_gates"]["stage33_08_released"] is False
    assert c["theorem_credit"] is False
    assert c["receiver_credit"] is False
    assert c["endpoint_credit"] is False
    assert c["perfect_cuboid_existence_claim"] is False
    assert c["perfect_cuboid_nonexistence_claim"] is False

    print(json.dumps({
        "success": True,
        "mode": "check" if a.check else "verify_noop",
        "promotion_already_complete": True,
        "receipt_sha256": RECEIPT_SHA,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
