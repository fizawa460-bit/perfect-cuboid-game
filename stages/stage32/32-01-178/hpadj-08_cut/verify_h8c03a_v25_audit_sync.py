#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
SNAPSHOT = ROOT / "stages/stage32/proof/historical-routing-blobs/e0c256916815220746b3d53a81044889d8444749.json"
RECEIPT = HERE / "H8C-03A-V25-HOSTILE-AUDIT-PASS-SYNC.json"
CLAIM = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
LANES = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

AUDITED_HEAD = "f7b7b0377800bea569f00b415123e047a66dd109"
AUDIT_REVIEW = 5208685885
SNAPSHOT_BLOB = "e0c256916815220746b3d53a81044889d8444749"
SNAPSHOT_CANON = "a818ff8294ec5f2e1b7674b12cd86049b0c41a34dabc9d220d318bb0786aeb74"
STATE_BLOB = "0f8aa75df6246064afbd4977775097a5bb807612"
STATE_CANON = "833f765544279c65e85fac8ff2cf57262f9bb71cdc208378216cb31826831c11"
RECEIPT_BLOB = "65ebf7d5e9e99eea2b20325533e0ce79d8f804c0"
RECEIPT_CANON = "b12265cb0a425e9b57572cfa45c8f1f0952b678e8a0b2eb230c676c414e3fced"
CLAIM_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
LANES_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"
AUTH = 16747313051409592067289
STRATA = 17128


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def locked(path: Path, b: str, c: str | None = None) -> dict:
    req(path.is_file(), f"missing {path}")
    req(blob(path) == b, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    if c is not None:
        req(obj.get("canonical_sha256_without_this_field") == c,
            f"stored canonical drift {path}")
        req(canon(obj) == c, f"canonical drift {path}")
    return obj


def main() -> None:
    old = locked(SNAPSHOT, SNAPSHOT_BLOB, SNAPSHOT_CANON)
    of = old["current_exact_frontier"]
    req(old["schema"] == "STAGE32_MAIN_COMPACT_STATE_V25_H8C03A_CONSUMED", "pre-sync schema")
    req(old["current"]["mainbatch_stop_gate"] == "REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED",
        "pre-sync stop gate")
    req(old["firewalls"]["replacement_head_hostile_reaudit_required"] is True,
        "pre-sync re-audit firewall")
    req(of["authoritative_remaining_strata"] == STRATA, "pre-sync strata")
    req(of["authoritative_remaining_terminals"] == AUTH, "pre-sync authority")
    req(of["h8c03a_main_pruning_credit"] is True and of["h8c03a_double_charge"] is False,
        "pre-sync H8C03A accounting")
    req(of["full178_numerical_census_complete"] is False and of["stage32_closed"] is False,
        "pre-sync closure overclaim")

    r = locked(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON)
    req(r["schema"] == "STAGE32_MAIN_H8C03A_V25_HOSTILE_AUDIT_PASS_SYNC_V1", "receipt schema")
    req(r["status"] == "HOSTILE_AUDIT_PASS_CONSUMED_ROUTING_RESUMED_NO_NEW_MATHEMATICAL_CREDIT",
        "receipt status")
    b = r["audited_boundary"]
    req(b["status"] == "PASS" and b["exact_head"] == AUDITED_HEAD and
        b["review_id"] == AUDIT_REVIEW, "audited boundary")
    req(b["main_state_blob_sha1"] == SNAPSHOT_BLOB and
        b["main_state_canonical_sha256"] == SNAPSHOT_CANON, "audited state identity")
    req(b["authoritative_remaining_strata"] == STRATA and
        b["authoritative_remaining_terminals_upper_bound"] == AUTH, "audited authority")
    a = r["authority_accounting"]
    req(a["additional_pruning_credit_consumed"] == 0 and a["double_charge"] is False,
        "sync accounting")
    req(a["pre_sync_remaining_terminals_upper_bound"] == AUTH and
        a["post_sync_remaining_terminals_upper_bound"] == AUTH, "sync authority drift")
    req(a["stratum_count_change_claimed"] is False, "sync stratum overclaim")
    req(r["claim_sync"]["immutable_claim_core_mutation_required"] is False,
        "claim-core mutation")
    req(r["claim_sync"]["full178_frontier_status_remains"] == "ACTIVE_INCOMPLETE" and
        r["claim_sync"]["full178_audit_receipt_remains"] == "NOT_AUDITED_GOAL",
        "FULL178 promotion")
    req(r["exact_head_ci"]["all_success"] is True, "exact-head CI")
    req(r["exact_head_ci"]["stage32_claim_frontier_integrity"] == 34955122364 and
        r["exact_head_ci"]["stage32_main_startup_authority"] == 34955122389 and
        r["exact_head_ci"]["stage32_stale_run_sweeper"] == 34955122551 and
        r["exact_head_ci"]["stage32ex5_main_integrity"] == 34955122398, "CI run identity")
    req(r["routing_after_sync"]["heavy_compute_authorized"] is False and
        r["routing_after_sync"]["mainbatch_stop_gate"] == "NONE", "routing firewall")
    req(all(v is False for v in r["firewalls"].values()), "receipt broad-credit firewall")

    locked(CLAIM, CLAIM_BLOB)
    locked(FRONTIER, FRONTIER_BLOB)
    locked(LANES, LANES_BLOB)
    req(r["claim_sync"]["claim_registry_blob_sha1"] == CLAIM_BLOB and
        r["claim_sync"]["active_frontier_blob_sha1"] == FRONTIER_BLOB and
        r["claim_sync"]["lane_adapters_blob_sha1"] == LANES_BLOB, "claim source locks")

    cur = locked(STATE, STATE_BLOB, STATE_CANON)
    f = cur["current_exact_frontier"]
    req(cur["schema"] == "STAGE32_MAIN_COMPACT_STATE_V25_H8C03A_AUDIT_SYNCED", "synced schema")
    req(f["authoritative_remaining_strata"] == STRATA and
        f["authoritative_remaining_terminals"] == AUTH, "synced authority")
    req(f["authoritative_remaining_terminals_semantics"] ==
        "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "synced semantics")
    req(f["h8c03a_v25_hostile_audited"] is True and
        f["h8c03a_v25_audited_exact_head"] == AUDITED_HEAD and
        f["h8c03a_v25_hostile_audit_review_id"] == AUDIT_REVIEW, "synced audit identity")
    req(cur["authority_sync"]["h8c03a_v25_hostile_audit_status"] == "PASS" and
        cur["authority_sync"]["h8c03a_v25_exact_head"] == AUDITED_HEAD and
        cur["authority_sync"]["h8c03a_v25_hostile_audit_review_id"] == AUDIT_REVIEW,
        "synced authority audit identity")
    req(cur["current"]["mainbatch_stop_gate"] == "NONE" and
        cur["current"]["next_exact_route"] ==
        "FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS", "synced routing")
    req(cur["firewalls"]["replacement_head_hostile_reaudit_required"] is False,
        "stale re-audit firewall")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,
        "synced closure overclaim")
    for key in ("effectivity_released", "endpoint_credit", "full178_complete", "merge_authorized",
                "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
                "receiver_credit", "route_credit", "stage32_closed", "theorem_credit"):
        req(cur["firewalls"][key] is False, f"firewall unexpectedly true: {key}")

    lock = cur["source_locks"]["h8c03a_v25_audit_sync"]
    req(lock["reviewed_exact_head"] == AUDITED_HEAD and
        lock["reviewed_main_state_blob_sha1"] == SNAPSHOT_BLOB and
        lock["reviewed_main_state_canonical_sha256"] == SNAPSHOT_CANON, "state reviewed lock")
    req(lock["hostile_audit_review_id"] == AUDIT_REVIEW and
        lock["hostile_audit_status"] == "PASS", "state audit lock")
    req(lock["audit_sync_receipt_blob_sha1"] == RECEIPT_BLOB and
        lock["audit_sync_receipt_canonical_sha256"] == RECEIPT_CANON, "state receipt lock")
    req(lock["claim_registry_blob_sha1"] == CLAIM_BLOB and
        lock["active_frontier_blob_sha1"] == FRONTIER_BLOB and
        lock["lane_adapters_blob_sha1"] == LANES_BLOB, "state claim locks")

    print(json.dumps({
        "verdict": "PASS_V25_H8C03A_HOSTILE_AUDIT_SYNC",
        "audited_exact_head": AUDITED_HEAD,
        "review_id": AUDIT_REVIEW,
        "remaining_strata": STRATA,
        "remaining_terminals_upper_bound": AUTH,
        "additional_pruning_credit": 0,
        "full178_status": "ACTIVE_INCOMPLETE",
        "next_route": "FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS",
        "heavy_compute_authorized": False,
        "merge_authorized": False
    }, sort_keys=True))


if __name__ == "__main__":
    main()
