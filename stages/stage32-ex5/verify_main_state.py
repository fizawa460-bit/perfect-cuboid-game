#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
B2 = HERE / "breadth-cycle-2"
MAIN = "c31684fb5f63d8a025eb298c91861d4c979b0e28"
BC2_25 = "fc4e4541a4f349e6c249f7dadd85f91edfd1c0dc1cb56d92b18bbf13054a4518"
BC2_25_AUDIT_HEAD = "1d2e04486e170336ce02af144aabb08e4a80a31d"
BC2_25_AUDIT_REVIEW = 5177354131
BC2_26 = "b97d61c0d20cec1742831a07595429024cb9bb272d383cfb98d968278d8d330a"
BC2_26_RAW = "f61f60804829c63b2090b42e142824411120f4d1a80d04ea323e04127e94e831"
BC2_26_RUN = 34588771756
BC2_26_JOB = 103229111936
BC2_26_HEAD = "7d5c35057b480ebe6bf3b0cdf047c0d7bdfde18f"
BC2_26_ARTIFACT = 10194988584


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(f"FAIL: {msg}")


def main() -> None:
    s = json.loads((HERE / "MAIN-STATE.json").read_text(encoding="utf-8"))
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V8_BC2_26_AUDIT_BOUNDARY", "state schema drift")

    b = s["bootstrap"]
    req(b["current_main_sha_observed"] == MAIN, "current-main observation drift")
    req(b["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch" and b["active_work_pr"] == 1776, "active work surface drift")
    req(b["latest_merged_pr"] == 1765 and b["merge_authorized"] is False, "merge provenance/authorization drift")

    a = s["stage32_main_authority"]
    req(a["control_mode"] == "FULL178_AND_FINAL_MILESTONE_CHAIN" and a["primary_incomplete_id"] == "32-01", "Stage32 route drift")
    req(a["n356_status"] == "AUDIT_REQUIRED" and a["n356_audit_credit_consumed"] is False and a["n356_main_pruning_credit"] is False, "N356 credit leak")
    for k in ("V6_is_current_attack_target", "O210_is_current_attack_target", "Q602_is_current_attack_target"):
        req(a[k] is False, f"historical target reactivated: {k}")

    cur = s["current"]
    req(cur["status"] == "BC2_26_RETAINED_HOSTILE_AUDIT_REQUIRED", "BC2-26 status drift")
    req(cur["leaf"] == "BC2_26_BOUNDARY34_PARTITION_RETAINED", "BC2-26 leaf drift")
    req(cur["next_route"] == "HOSTILE_AUDIT_BC2_26_RECHECK", "audit-first route drift")
    req(cur["stop_semantics"] == "BC2_27_BLOCKED_UNTIL_BC2_26_HOSTILE_AUDIT_PASS", "BC2-27 stop firewall drift")

    f = s["frontier"]
    req((f["e8_bc2_26_new_parent_unsat_count"], f["e8_bc2_26_retained_unknown_count"], f["e8_bc2_26_parent_sat_count"]) == (4, 12, 0), "BC2-26 parent accounting drift")
    req((f["e8_bc2_26_branch_unsat_count"], f["e8_bc2_26_branch_unknown_count"], f["e8_bc2_26_branch_sat_count"]) == (16, 20, 0), "BC2-26 branch accounting drift")
    req((f["e8_bc2_26_p33_subbranch_unsat_count"], f["e8_bc2_26_p33_subbranch_unknown_count"], f["e8_bc2_26_p33_subbranch_sat_count"]) == (18, 20, 0), "BC2-26 p33 accounting drift")
    req((f["e8_bc2_26_p34_leaf_unsat_count"], f["e8_bc2_26_p34_leaf_unknown_count"], f["e8_bc2_26_p34_leaf_sat_count"]) == (87, 23, 0), "BC2-26 p34 accounting drift")
    req(f["e8_known_parent_unsat_count_lower_bound"] == 7152 and f["e8_bc2_26_unretained_unknown_identity_count"] == 172, "BC2-26 lower-bound/firewall drift")
    req(f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False, "local BC2-26 result promoted")

    rp = s["retained_exact_progress"]
    req(rp["bc2_25_checkpoint_canonical"] == BC2_25, "BC2-25 checkpoint lock drift")
    req(rp["bc2_25_hostile_audit_exact_head"] == BC2_25_AUDIT_HEAD and rp["bc2_25_hostile_audit_review_id"] == BC2_25_AUDIT_REVIEW, "BC2-25 PASS receipt drift")
    req(rp["bc2_26_checkpoint_canonical"] == BC2_26 and rp["bc2_26_raw_result_canonical"] == BC2_26_RAW, "BC2-26 checkpoint/raw lock drift")
    req(rp["bc2_26_workflow_run_id"] == BC2_26_RUN and rp["bc2_26_compute_job_id"] == BC2_26_JOB and rp["bc2_26_exact_compute_head"] == BC2_26_HEAD, "BC2-26 run provenance drift")
    req(rp["bc2_26_artifact_id"] == BC2_26_ARTIFACT, "BC2-26 artifact drift")

    audit = s["intermediate_audit_boundary"]
    req(audit["candidate_pr"] == 1776 and audit["candidate_checkpoint_canonical"] == BC2_26, "BC2-26 audit checkpoint drift")
    req(audit["predecessor_hostile_audit_status"] == "PASS" and audit["predecessor_hostile_audit_review_id"] == BC2_25_AUDIT_REVIEW, "BC2-25 predecessor audit receipt drift")
    req(audit["last_hostile_audit_status"] == "PENDING", "BC2-26 audit status must be pending")
    req(audit["new_audit_boundary_exists"] is True and audit["re_audit_required"] is True and audit["freeze_active"] is True, "BC2-26 audit boundary not frozen")
    req(audit["bc2_27_execution_authorized"] is False and audit["merged"] is False, "BC2-27/merge authorization leak")

    ns = s["next_step"]
    req(ns["id"] == "BC2_26_HOSTILE_AUDIT_RECHECK" and ns["bc2_27_blocked_until_audit_pass"] is True, "next-step audit gate drift")
    for k in ("heavy_scaleout_authorized", "main_promotion_authorized", "n350_registration_authorized", "merge_authorized"):
        req(ns[k] is False, f"authorization leak: {k}")

    for section_name in ("credit", "historical_credit_firewall", "firewalls"):
        for key, value in s[section_name].items():
            if key != "level":
                req(value is False, f"credit/firewall leak: {section_name}.{key}")

    runkey = json.loads((HERE / "runkeys/bc2-26-boundary34-partition.json").read_text(encoding="utf-8"))
    req(runkey["armed"] is False, "BC2-26 runkey must stay disarmed after retained execution")
    req(runkey["consumed_run"]["checkpoint_canonical"] == BC2_26, "BC2-26 consumed checkpoint drift")

    subprocess.run([sys.executable, str(B2 / "verify_bc2_25_boundary33_partition_checkpoint.py")], check=True)
    subprocess.run([sys.executable, str(B2 / "verify_bc2_26_boundary34_partition_checkpoint.py")], check=True)

    docs = {name: (HERE / name).read_text(encoding="utf-8") for name in ["README.md", "MAIN-START-HERE.md", "CURRENT-ROADMAP.md", "CURRENT-AUDIT-CONTRACT.md", "MAINBATCH-OPERATIONS.md"]}
    for name, text in docs.items():
        for token in ("BC2-26", "7152", "12", "20", "23", "172", "#1776"):
            req(token in text, f"{name} missing BC2-26 audit-boundary token: {token}")
        req("BC2-27" in text and ("blocked" in text.lower() or "禁止" in text), f"{name} does not block BC2-27 before audit PASS")
    req(BC2_26 in docs["CURRENT-AUDIT-CONTRACT.md"] and str(BC2_26_RUN) in docs["CURRENT-AUDIT-CONTRACT.md"], "audit contract missing BC2-26 receipt")

    print("PASS: Stage32EX5 BC2-26 retained hostile-audit boundary is coherent")
    print("bc2_26=4_NEW_UNSAT_12_RETAINED_UNKNOWN_0_SAT;20_BRANCH_UNKNOWN;20_P33_UNKNOWN;23_P34_UNKNOWN;172_OTHER_IDENTITIES_UNINFERRED")
    print("known_parent_unsat_lower_bound=7152")
    print("stage32_main_credit=NO;merge_authorized=NO")
    print("next=HOSTILE_AUDIT_BC2_26_RECHECK;BC2_27_BLOCKED")


if __name__ == "__main__":
    main()
