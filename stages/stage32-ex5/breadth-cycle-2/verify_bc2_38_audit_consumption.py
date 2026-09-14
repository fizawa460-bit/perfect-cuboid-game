#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CHECKPOINT = HERE / "bc2-38-fresh-unknown34-replay-checkpoint.json"
RUNKEY = ROOT / "runkeys/bc2-38-fresh-unknown34-replay.json"
RETAINED_VERIFIER = HERE / "verify_bc2_38_targeted_replay_checkpoint.py"
STATE = ROOT / "MAIN-STATE.json"
SYNC = ROOT / "LIVE-MAIN-COORDINATION-SYNC-20260914.json"

CP_BLOB = "91eca02054cd2dbf702dd4a7635398ef76ee832f"
CP_CANON = "88b41680df6bb78f8b7f8ca00cde121d909a39e7b3c29eef765edb77b2c022ba"
RUNKEY_BLOB = "87855350c6240cd524069490f85858b11099da60"
RETAINED_VERIFIER_BLOB = "934f19363549d652c18b02934c1f963a19204664"
SYNC_BLOB = "c9a3a878413df5afc634f99b94707534412b5d84"
SYNC_CANON = "fd5c7c6d025286a5677b7dcab5113f066dff83574c4647d772d89c7799b8be6c"
AUDIT_HEAD = "5e1d07e4c92fbecff9bfa89b0bfb65cdaf564a71"
AUDIT_REVIEW = 5190676180
UNKNOWN_SHA = "d60d873c4fc66ebb6cda0530d4137e5fd195fe1b601b0a21e91f873c1df28fb7"
V31 = "STAGE32EX5_MAIN_COMPACT_STATE_V31_BC2_38_AUDIT_CONSUMED_BC2_39_EXECUTION"
V32 = "STAGE32EX5_MAIN_COMPACT_STATE_V32_BC2_39_TARGETED_REPLAY_AUDIT_BOUNDARY"
V33 = "STAGE32EX5_MAIN_COMPACT_STATE_V33_BC2_39_AUDIT_CONSUMED_BC2_40_PREFLIGHT"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def canon(obj: dict) -> str:
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(q, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    req(blob(CHECKPOINT) == CP_BLOB, "BC2-38 checkpoint blob")
    cp = json.loads(CHECKPOINT.read_text())
    req(cp["canonical_sha256_without_this_field"] == CP_CANON and canon(cp) == CP_CANON, "BC2-38 checkpoint canonical")
    r = cp["replay"]
    req((r["parents_checked"], r["unsat_count"], r["unknown_count"], r["sat_count"]) == (34,4,30,0), "BC2-38 result partition")
    req(r["unknown_parent_indices_sha256"] == UNKNOWN_SHA, "BC2-38 unknown30 hash")
    req(cp["credit"]["known_parent_unsat_count_lower_bound"] == 7306, "BC2-38 candidate lower bound")
    req(blob(RUNKEY) == RUNKEY_BLOB, "BC2-38 consumed runkey")
    rk = json.loads(RUNKEY.read_text())
    req(rk["armed"] is False and rk["generation"] == 1, "BC2-38 runkey state")
    cr = rk["consumed_run"]
    req(cr["accepted_for_hostile_audit"] is True and cr["exact_head"] == "d26a27e8564458f3d575ec58601b2226fc23944f" and cr["workflow_run_id"] == 34742297972 and cr["artifact_id"] == 10313851431, "BC2-38 execution receipt")
    req(cr["checkpoint_git_blob_sha"] == CP_BLOB and cr["checkpoint_canonical"] == CP_CANON and cr["remaining_unknown_parent_indices_sha256"] == UNKNOWN_SHA and cr["known_parent_unsat_count_lower_bound"] == 7306, "BC2-38 receipt result identity")
    req(blob(RETAINED_VERIFIER) == RETAINED_VERIFIER_BLOB, "hostile-audited retained verifier identity")

    req(blob(SYNC) == SYNC_BLOB, "live coordination sync blob")
    sync = json.loads(SYNC.read_text())
    req(sync["canonical_sha256_without_this_field"] == SYNC_CANON and canon(sync) == SYNC_CANON, "live coordination sync canonical")
    req(sync["live_cross_lane_registry"]["open_ex5_producer_demand_count"] == 0, "OPEN EX5 producer demand")
    req(sync["live_main_state"]["mainbatch_stop_gate"] == "NONE", "MAIN stop gate")

    state = json.loads(STATE.read_text())
    schema = state["schema"]
    req(schema in {V31, V32, V33}, "BC2-38 consumed live state schema")
    pa = state["prior_audited_authority"]["bc2_38_pr_1776"]
    req(pa["hostile_audit_status"] == "PASS" and pa["audit_checkpoint_exact_head"] == AUDIT_HEAD and pa["hostile_audit_review_id"] == AUDIT_REVIEW, "BC2-38 hostile-audit receipt")
    f = state["frontier"]
    a = state["intermediate_audit_boundary"]
    if schema == V31:
        req(f["e8_bc2_38_audited"] is True and f["e8_known_parent_unsat_count_lower_bound"] == 7306 and f["e8_bc2_38_remaining_unknown_count"] == 30 and f["e8_bc2_38_remaining_unknown_parent_indices_sha256"] == UNKNOWN_SHA, "BC2-38 consumed frontier")
        req(f["e8_bc2_39_executed"] is False and f["e8_bc2_39_target_unknown_count"] == 30 and f["e8_bc2_39_target_unknown_parent_indices_sha256"] == UNKNOWN_SHA, "BC2-39 target frontier")
        req(a["last_hostile_audit_status"] == "PASS" and a["last_hostile_audit_exact_head"] == AUDIT_HEAD and a["last_hostile_audit_review_id"] == AUDIT_REVIEW and a["bc2_39_execution_authorized"] is True and a["freeze_active"] is False and a["new_audit_boundary_exists"] is False, "V31 audit consumption state")
    elif schema == V32:
        req(f["e8_bc2_38_audited"] is True and f["e8_known_parent_unsat_count_lower_bound"] == 7306 and f["e8_bc2_38_remaining_unknown_count"] == 30 and f["e8_bc2_38_remaining_unknown_parent_indices_sha256"] == UNKNOWN_SHA, "BC2-38 consumed frontier")
        req(f["e8_bc2_39_executed"] is True and f["e8_bc2_39_audited"] is False and f["e8_bc2_39_new_parent_unsat_count"] == 7 and f["e8_bc2_39_remaining_unknown_count"] == 23 and f["e8_bc2_39_sat_count"] == 0 and f["e8_bc2_39_candidate_known_parent_unsat_count_lower_bound"] == 7313, "V32 BC2-39 quarantined frontier")
        req(a["last_hostile_audit_status"] == "PASS" and a["last_hostile_audit_exact_head"] == AUDIT_HEAD and a["last_hostile_audit_review_id"] == AUDIT_REVIEW and a["bc2_39_execution_authorized"] is False and a["freeze_active"] is True and a["new_audit_boundary_exists"] is True and a["re_audit_required"] is True, "V32 audit freeze")
    else:
        req(f["e8_bc2_38_audited"] is True and f["e8_bc2_38_known_parent_unsat_count_lower_bound"] == 7306 and f["e8_known_parent_unsat_count_lower_bound"] == 7313, "BC2-38 V33 retained authority")
        pa39 = state["prior_audited_authority"]["bc2_39_pr_1776"]
        req(pa39["hostile_audit_status"] == "PASS" and pa39["audit_checkpoint_exact_head"] == "4b974550d9ad030973fec99e19a090f6785f8aa8" and pa39["hostile_audit_review_id"] == 5193423203, "BC2-39 hostile-audit receipt")
        req(f["e8_bc2_39_audited"] is True and f["e8_bc2_39_remaining_unknown_count"] == 23 and f["e8_bc2_40_preflight_ready"] is True and f["e8_bc2_40_execution_authorized"] is False, "V33 BC2-40 preflight frontier")
        req(a["last_hostile_audit_status"] == "PASS" and a["last_hostile_audit_exact_head"] == "4b974550d9ad030973fec99e19a090f6785f8aa8" and a["last_hostile_audit_review_id"] == 5193423203 and a["bc2_40_execution_authorized"] is False and a["freeze_active"] is False and a["new_audit_boundary_exists"] is False and a["re_audit_required"] is False, "V33 audit consumption state")

    print("PASS: BC2-38 hostile-audit PASS remains consumed into EX5 local authority")
    print("audited_lower_bound=7306 bc2_39_audited_lower_bound=7313 main_credit=NO merge=NO")


if __name__ == "__main__":
    main()
