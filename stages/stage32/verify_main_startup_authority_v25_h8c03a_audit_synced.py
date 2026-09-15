#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
SNAPSHOT = HERE / "proof/historical-routing-blobs/e0c256916815220746b3d53a81044889d8444749.json"
OLD_VERIFIER = HERE / "verify_main_startup_authority_v25_h8c03a_consumed.py"
SYNC_VERIFIER = HERE / "32-01-178/hpadj-08_cut/verify_h8c03a_v25_audit_sync.py"

STATE_BLOB = "0f8aa75df6246064afbd4977775097a5bb807612"
STATE_CANON = "833f765544279c65e85fac8ff2cf57262f9bb71cdc208378216cb31826831c11"
SNAPSHOT_BLOB = "e0c256916815220746b3d53a81044889d8444749"
OLD_VERIFIER_BLOB = "77a7c60a2134505c742af8571a23ba9244f27494"
AUDITED_HEAD = "f7b7b0377800bea569f00b415123e047a66dd109"
AUDIT_REVIEW = 5208685885
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


def main() -> None:
    req(STATE.is_file() and blob(STATE) == STATE_BLOB, "synced MAIN-STATE blob drift")
    req(SNAPSHOT.is_file() and blob(SNAPSHOT) == SNAPSHOT_BLOB, "pre-sync V25 snapshot drift")
    req(OLD_VERIFIER.is_file() and blob(OLD_VERIFIER) == OLD_VERIFIER_BLOB,
        "pre-sync V25 authority verifier drift")

    live = STATE.read_bytes()
    try:
        # Re-run the complete pre-sync V25 authority verifier against the exact
        # hostile-audited state bytes, then restore the synced state unconditionally.
        STATE.write_bytes(SNAPSHOT.read_bytes())
        runpy.run_path(str(OLD_VERIFIER), run_name="__main__")
    finally:
        STATE.write_bytes(live)
    req(STATE.read_bytes() == live, "synced MAIN-STATE restore failed")

    runpy.run_path(str(SYNC_VERIFIER), run_name="__main__")

    state = json.loads(STATE.read_text(encoding="utf-8"))
    req(state.get("canonical_sha256_without_this_field") == STATE_CANON,
        "synced MAIN-STATE stored canonical drift")
    req(canon(state) == STATE_CANON, "synced MAIN-STATE canonical drift")
    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V25_H8C03A_AUDIT_SYNCED", "schema")
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == STRATA, "strata authority")
    req(f["authoritative_remaining_terminals"] == AUTH, "terminal authority")
    req(f["authoritative_remaining_terminals_semantics"] ==
        "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "authority semantics")
    req(f["h8c03a_main_pruning_credit"] is True, "H8C03A consumed credit")
    req(f["h8c03a_current_authority_overlap_accounted"] is True, "H8C03A overlap")
    req(f["h8c03a_double_charge"] is False, "H8C03A double charge")
    req(f["h8c03a_v25_hostile_audited"] is True, "V25 audit status")
    req(f["h8c03a_v25_audited_exact_head"] == AUDITED_HEAD, "V25 audit head")
    req(f["h8c03a_v25_hostile_audit_review_id"] == AUDIT_REVIEW, "V25 audit review")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,
        "closure overclaim")
    req(state["current"]["mainbatch_stop_gate"] == "NONE", "stale stop gate")
    req(state["current"]["next_exact_route"] ==
        "FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS", "next route")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is False,
        "stale re-audit firewall")
    for key in ("effectivity_released", "endpoint_credit", "full178_complete", "merge_authorized",
                "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
                "receiver_credit", "route_credit", "stage32_closed", "theorem_credit"):
        req(state["firewalls"][key] is False, f"firewall unexpectedly true: {key}")

    expected = [
        "stages/stage32/32-01-178/hpadj-08_cut/H8C-03A-V25-HOSTILE-AUDIT-PASS-SYNC.json",
        "stages/stage32/32-01-178/hpadj-08_cut/verify_h8c03a_v25_audit_sync.py",
        "stages/stage32/verify_main_startup_authority_v25_h8c03a_audit_synced.py",
        "stages/stage32/proof/verify_cross_lane_demands.py",
    ]
    req(state["current_leaf_working_set"] == expected, "audit-sync working-set drift")

    print("PASS: Stage32 MAIN V25 H8C-03A audit-synced authority")
    print(f"remaining_strata={STRATA} remaining_terminals_upper_bound={AUTH}")
    print("FULL178=ACTIVE_INCOMPLETE stop_gate=NONE heavy_compute_authorized=false merge_authorized=false")


if __name__ == "__main__":
    main()
