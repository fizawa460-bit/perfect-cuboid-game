#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
B2 = HERE / "breadth-cycle-2"
MAIN = "b41ce34172870fb541498e62d041e940b66d85be"
BC2_25 = "fc4e4541a4f349e6c249f7dadd85f91edfd1c0dc1cb56d92b18bbf13054a4518"
FAILED_AUDIT_HEAD = "9bbc491cfde0f8a7f48d9742dad8ff368e4837b2"
FAILED_AUDIT_REVIEW = 5176133548


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(f"FAIL: {msg}")


def main() -> None:
    s = json.loads((HERE / "MAIN-STATE.json").read_text(encoding="utf-8"))
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V6_BC2_25_AUDIT_BOUNDARY", "state schema drift")

    b = s["bootstrap"]
    req(b["current_main_sha_observed"] == MAIN, "current-main observation drift")
    req(b["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch" and b["active_work_pr"] == 1776, "active work surface drift")
    req(b["latest_merged_pr"] == 1765 and b["latest_merge_commit"] == "98c5710dad4ca9a006e93b273ecf5259733e03aa", "BC2-24 merge provenance drift")
    req(b["merge_authorized"] is False and b["merge_priority_requested"] is False, "merge authorization leak")

    a = s["stage32_main_authority"]
    req(a["control_mode"] == "FULL178_AND_FINAL_MILESTONE_CHAIN" and a["primary_incomplete_id"] == "32-01", "Stage32 route drift")
    req(a["n356_status"] == "AUDIT_REQUIRED" and a["n356_audit_credit_consumed"] is False and a["n356_main_pruning_credit"] is False, "N356 credit leak")
    for k in ("V6_is_current_attack_target","O210_is_current_attack_target","Q602_is_current_attack_target"):
        req(a[k] is False, f"historical target reactivated: {k}")

    cur = s["current"]
    req(cur["status"] == "BC2_25_RETAINED_HOSTILE_AUDIT_REPAIR_REQUIRED", "BC2-25 status drift")
    req(cur["leaf"] == "BC2_25_BOUNDARY33_PARTITION_RETAINED", "BC2-25 leaf drift")
    req(cur["next_route"] == "HOSTILE_AUDIT_BC2_25_RECHECK", "audit-first route drift")
    req(cur["stop_semantics"] == "BC2_26_BLOCKED_UNTIL_BC2_25_HOSTILE_AUDIT_PASS", "BC2-26 stop firewall drift")

    f = s["frontier"]
    req((f["e8_bc2_25_new_parent_unsat_count"],f["e8_bc2_25_retained_unknown_count"],f["e8_bc2_25_parent_sat_count"]) == (3,16,0), "BC2-25 parent accounting drift")
    req((f["e8_bc2_25_branch_unsat_count"],f["e8_bc2_25_branch_unknown_count"],f["e8_bc2_25_branch_sat_count"]) == (24,36,0), "BC2-25 branch accounting drift")
    req((f["e8_bc2_25_subbranch_unsat_count"],f["e8_bc2_25_subbranch_unknown_count"],f["e8_bc2_25_subbranch_sat_count"]) == (128,38,0), "BC2-25 subbranch accounting drift")
    req(f["e8_known_parent_unsat_count_lower_bound"] == 7148 and f["e8_bc2_25_unretained_unknown_identity_count"] == 172, "BC2-25 residual accounting drift")
    req(f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False, "local BC2-25 result promoted")

    rp = s["retained_exact_progress"]
    req(rp["bc2_25_checkpoint_canonical"] == BC2_25, "BC2-25 checkpoint state lock drift")
    req(rp["bc2_25_workflow_run_id"] == 34574409241 and rp["bc2_25_exact_compute_head"] == "01e6e23ce90b24efda37303d81df3820a948061a", "BC2-25 compute provenance drift")
    req(rp["bc2_25_hperp_integral_adapter_git_blob_sha"] == "fb1eb380ca786e42a6b00c5ef454b0e79fdba771", "hperp state lock drift")
    req(rp["bc2_25_pairing_prefix_engine_git_blob_sha"] == "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b", "pairing state lock drift")

    audit = s["intermediate_audit_boundary"]
    req(audit["candidate_pr"] == 1776 and audit["candidate_checkpoint_canonical"] == BC2_25, "active audit checkpoint drift")
    req(audit["last_hostile_audit_status"] == "FAIL" and audit["last_hostile_audit_exact_head"] == FAILED_AUDIT_HEAD and audit["last_hostile_audit_review_id"] == FAILED_AUDIT_REVIEW, "failed audit receipt drift")
    req(audit["new_audit_boundary_exists"] is True and audit["historical_boundary_only"] is False, "new audit boundary not registered")
    req(audit["repair_required_before_merge"] is True and audit["re_audit_required"] is True and audit["freeze_active"] is True, "audit repair freeze drift")
    req(audit["merged"] is False and audit["bc2_26_execution_authorized"] is False, "merge/BC2-26 authorization leak")

    ns = s["next_step"]
    req(ns["id"] == "BC2_25_HOSTILE_AUDIT_RECHECK" and ns["bc2_26_blocked_until_audit_pass"] is True, "next-step audit gate drift")
    for k in ("heavy_scaleout_authorized","main_promotion_authorized","n350_registration_authorized","merge_authorized"):
        req(ns[k] is False, f"next-step authorization leak: {k}")

    for section_name in ("credit","historical_credit_firewall","firewalls"):
        for key, value in s[section_name].items():
            if key != "level":
                req(value is False, f"credit/firewall leak: {section_name}.{key}")

    checkpoint = json.loads((B2 / "bc2-25-boundary33-partition-checkpoint.json").read_text(encoding="utf-8"))
    req(checkpoint["canonical_sha256_without_this_field"] == BC2_25, "BC2-25 checkpoint canonical field drift")

    subprocess.run([sys.executable, str(B2 / "verify_bc2_25_boundary33_partition_checkpoint.py")], check=True)

    docs = {
        "README": (HERE / "README.md").read_text(encoding="utf-8"),
        "START": (HERE / "MAIN-START-HERE.md").read_text(encoding="utf-8"),
        "ROADMAP": (HERE / "CURRENT-ROADMAP.md").read_text(encoding="utf-8"),
        "AUDIT": (HERE / "CURRENT-AUDIT-CONTRACT.md").read_text(encoding="utf-8"),
        "OPS": (HERE / "MAINBATCH-OPERATIONS.md").read_text(encoding="utf-8"),
    }
    for name, text in docs.items():
        for token in ("BC2-25", "7148", "16", "172", "#1776"):
            req(token in text, f"{name} missing BC2-25 audit-boundary token: {token}")
    req("5176133548" in docs["AUDIT"] and FAILED_AUDIT_HEAD in docs["AUDIT"], "audit contract missing FAIL receipt")
    for name, text in docs.items():
        req("BC2-26" in text and ("blocked" in text.lower() or "禁止" in text), f"{name} does not block BC2-26 before audit PASS")

    print("PASS: Stage32EX5 BC2-25 active hostile-audit boundary is coherent")
    print("bc2_25=3_NEW_UNSAT_16_RETAINED_UNKNOWN_0_SAT;172_OTHER_IDENTITIES_UNINFERRED")
    print("known_parent_unsat_lower_bound=7148")
    print("stage32_main_credit=NO_FROM_EX5")
    print("next=HOSTILE_AUDIT_BC2_25_RECHECK;BC2_26_BLOCKED")


if __name__ == "__main__":
    main()
