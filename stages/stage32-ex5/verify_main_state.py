#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
B2 = HERE / "breadth-cycle-2"
ROOT = HERE.parents[0]
STAGE32_MAIN = ROOT / "stage32" / "MAIN-STATE.json"
BC29_TEMP_WORKFLOW = ROOT.parent / ".github/workflows/stage32-ex5-bc2-29.yml"
MAIN = "c31684fb5f63d8a025eb298c91861d4c979b0e28"
STAGE32_MAIN_BLOB = "9981889309c833a1834eaadddce73e52c0aa0176"
FULL178_GOAL_CLAIM = "S32.FULL178.NUMERICAL_CENSUS.V1"
BC2_28_AUDIT_HEAD = "4221d7f9816590e808976da37ba479880f35dc22"
BC2_28_AUDIT_REVIEW = 5183082213
BC2_29_CHECKPOINT = "e02b94819d44d0d74e5ce393746efcc4b069075f98c4c00ad2895246e941fe1d"
BC2_29_RAW = "e3284337761fd966a26a4c8b720b132de7e6a481746343403454707eff28a77b"
PERFECT_CUBOID_FIREWALL_KEYS = {"perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim"}


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(f"FAIL: {msg}")


def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def main() -> None:
    s = json.loads((HERE / "MAIN-STATE.json").read_text(encoding="utf-8"))
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V12_BC2_29_RETAINED_AUDIT_BOUNDARY", "state schema drift")
    b = s["bootstrap"]
    req(b["current_main_sha_observed"] == MAIN, "current-main observation drift")
    req(b["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch" and b["active_work_pr"] == 1776, "active work surface drift")
    req(b["merge_authorized"] is False, "merge authorization leak")

    a = s["stage32_main_authority"]
    req(a["routing_source"] == "stages/stage32/MAIN-STATE.json" and a["routing_source_blob_sha"] == STAGE32_MAIN_BLOB, "Stage32 authority projection drift")
    req(a["full178_goal_claim_id_observed"] == FULL178_GOAL_CLAIM, "FULL178 projection drift")
    req(git_blob(STAGE32_MAIN) == STAGE32_MAIN_BLOB, "Stage32 MAIN authority blob drift")
    ma = json.loads(STAGE32_MAIN.read_text(encoding="utf-8"))
    req(ma["current_exact_frontier"]["full178_goal_claim_id"] == FULL178_GOAL_CLAIM, "authoritative FULL178 claim-id drift")
    req(a["n356_status"] == "AUDIT_REQUIRED" and a["n356_audit_credit_consumed"] is False and a["n356_main_pruning_credit"] is False, "N356 credit leak")

    p28 = s["prior_audited_authority"]["bc2_28_pr_1776"]
    req(p28["hostile_audit_status"] == "PASS" and p28["audit_checkpoint_exact_head"] == BC2_28_AUDIT_HEAD and p28["hostile_audit_review_id"] == BC2_28_AUDIT_REVIEW, "BC2-28 PASS authority drift")

    cur = s["current"]
    req(cur["status"] == "BC2_29_RESULT_RETAINED_HOSTILE_AUDIT_REQUIRED", "BC2-29 status drift")
    req(cur["leaf"] == "BC2_29_BOUNDARY39_PARTITION_RETAINED_AUDIT_BOUNDARY", "BC2-29 leaf drift")
    req(cur["next_route"] == "HOSTILE_AUDIT_BC2_29", "BC2-29 audit route drift")
    req(cur["stop_semantics"] == "NO_BC2_30_OR_BROAD_PROMOTION_BEFORE_BC2_29_HOSTILE_AUDIT_PASS", "BC2-30 stop firewall drift")

    f = s["frontier"]
    req(f["e8_bc2_28_audited"] is True, "BC2-28 audit PASS not consumed")
    req(f["e8_bc2_29_executed"] is True and f["e8_bc2_29_audited"] is False, "BC2-29 execution/audit marker drift")
    req((f["e8_bc2_29_new_parent_unsat_count"],f["e8_bc2_29_retained_unknown_count"],f["e8_bc2_29_parent_sat_count"]) == (3,1,0), "BC2-29 parent accounting drift")
    req((f["e8_bc2_29_p39_leaf_unsat_count"],f["e8_bc2_29_p39_leaf_unknown_count"]) == (15,1), "BC2-29 p39 accounting drift")
    req(f["e8_known_parent_unsat_count_lower_bound"] == 7163 and f["e8_bc2_29_unretained_unknown_identity_count"] == 172, "BC2-29 lower-bound/firewall drift")
    req(f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False, "local result promoted")

    rp = s["retained_exact_progress"]
    req(rp["bc2_28_hostile_audit_exact_head"] == BC2_28_AUDIT_HEAD and rp["bc2_28_hostile_audit_review_id"] == BC2_28_AUDIT_REVIEW, "BC2-28 audit receipt drift")
    req(rp["bc2_29_checkpoint_canonical"] == BC2_29_CHECKPOINT and rp["bc2_29_checkpoint_git_blob_sha"] == "2200e596c1e8077f024859370c57ee263b5227a1", "BC2-29 checkpoint drift")
    req(rp["bc2_29_raw_result_canonical"] == BC2_29_RAW and rp["bc2_29_raw_json_sha256"] == "cf2ff678247cd46efcb9558a1890dd27b1f799831a1b2073ec545d7dea97c50d", "BC2-29 raw receipt drift")
    req(rp["bc2_29_workflow_run_id"] == 34644942182 and rp["bc2_29_compute_job_id"] == 103413402930 and rp["bc2_29_artifact_id"] == 10281797941, "BC2-29 execution receipt drift")
    req(rp["bc2_29_retained_unknown_parent_indices"] == [1064] and rp["bc2_29_known_parent_unsat_count_lower_bound"] == 7163, "BC2-29 residual receipt drift")
    req(rp["bc2_29_residual_unknown_p38_leaf"] == {"parent_index":1064,"n1":2,"n2":6,"p33":1,"p34":3,"p35":3,"p38":1,"p39":3}, "BC2-29 final timeout leaf drift")

    runkey = json.loads((HERE / "runkeys/bc2-29-boundary39-partition.json").read_text(encoding="utf-8"))
    req(runkey["schema"] == "STAGE32EX5_BC2_29_BOUNDARY39_PARTITION_RUNKEY_V1" and runkey["generation"] == 1 and runkey["armed"] is False, "BC2-29 runkey not consumed/disarmed")
    consumed = runkey["consumed_run"]
    req(consumed["checkpoint_canonical"] == BC2_29_CHECKPOINT and consumed["checkpoint_git_blob_sha"] == "2200e596c1e8077f024859370c57ee263b5227a1", "BC2-29 consumed checkpoint drift")
    req((consumed["new_parent_unsat_count"],consumed["retained_unknown_parent_count"],consumed["parent_sat_count"]) == (3,1,0), "BC2-29 consumed parent accounting drift")
    req((consumed["p39_leaf_unsat_count"],consumed["p39_leaf_unknown_count"]) == (15,1), "BC2-29 consumed p39 accounting drift")
    req(consumed["known_parent_unsat_count_lower_bound"] == 7163, "BC2-29 consumed lower-bound drift")

    claim = s["claim_sync"]
    req(claim["existing_active_goal"] == FULL178_GOAL_CLAIM and claim["lane_role"] == "ATTACKS", "claim-sync drift")
    req(claim["active_frontier_remapped"] is False and claim["main_promotion"] is False, "claim-sync promotion leak")

    audit = s["intermediate_audit_boundary"]
    req(audit["last_hostile_audit_status"] == "PASS" and audit["last_hostile_audit_exact_head"] == BC2_28_AUDIT_HEAD and audit["last_hostile_audit_review_id"] == BC2_28_AUDIT_REVIEW, "BC2-28 audit consumption drift")
    req(audit["new_audit_boundary_exists"] is True and audit["freeze_active"] is True and audit["re_audit_required"] is True, "BC2-29 audit boundary not frozen")
    req(audit["bc2_29_execution_authorized"] is False and audit["bc2_30_execution_authorized"] is False, "BC2-29/30 authorization leak")
    req(audit["merged"] is False, "merge state leak")

    ns = s["next_step"]
    req(ns["id"] == "HOSTILE_AUDIT_BC2_29_RETAINED_BOUNDARY" and ns["bc2_30_blocked_until_bc2_29_hostile_audit_pass"] is True, "BC2-29 next-step drift")
    for k in ("heavy_scaleout_authorized","main_promotion_authorized","n350_registration_authorized","merge_authorized"):
        req(ns[k] is False, f"authorization leak: {k}")

    fw = s["firewalls"]
    observed_pc_keys = {k for k in fw if "cuboid" in k or "curboid" in k}
    req(observed_pc_keys == PERFECT_CUBOID_FIREWALL_KEYS, "Perfect Cuboid firewall key-set drift")
    for section in ("credit","historical_credit_firewall","firewalls"):
        for key, value in s[section].items():
            if key != "level":
                req(value is False, f"credit/firewall leak: {section}.{key}")

    req(not BC29_TEMP_WORKFLOW.exists(), "temporary BC2-29 executor must be removed after retention")
    main_workflow = (ROOT.parent / ".github/workflows/stage32-ex5-main.yml").read_text(encoding="utf-8")
    req("bc2-29-boundary39-bounded:" not in main_workflow and "authorize-bc2-29:" not in main_workflow, "duplicate BC2-29 heavy execution path leaked into main workflow")

    for verifier in (
        "verify_bc2_25_boundary33_partition_checkpoint.py",
        "verify_bc2_26_boundary34_partition_checkpoint.py",
        "verify_bc2_27_boundary35_partition_checkpoint.py",
        "verify_bc2_28_boundary38_partition_checkpoint.py",
        "verify_bc2_29_boundary39_partition_checkpoint.py",
    ):
        subprocess.run([sys.executable, str(B2 / verifier)], check=True)

    docs = {name:(HERE/name).read_text(encoding="utf-8") for name in ["README.md","MAIN-START-HERE.md","CURRENT-ROADMAP.md","CURRENT-AUDIT-CONTRACT.md","MAINBATCH-OPERATIONS.md"]}
    for name,text in docs.items():
        for token in ("BC2-29","boundary39","7163","1064","172","#1776",str(BC2_28_AUDIT_REVIEW)):
            req(token in text, f"{name} missing BC2-29 retained-boundary token: {token}")
        req("BC2-30" in text and ("blocked" in text.lower() or "禁止" in text), f"{name} does not block BC2-30")
        req("audit" in text.lower(), f"{name} does not identify audit boundary")

    print("PASS: Stage32EX5 BC2-29 retained boundary is coherent and frozen for hostile audit")
    print("bc2_29=3_NEW_UNSAT_1_RETAINED_UNKNOWN_0_SAT;15_P39_UNSAT_1_P39_UNKNOWN;known_parent_unsat_lower_bound=7163")
    print("stage32_main_credit=NO;full178_complete=NO;merge_authorized=NO")
    print("next=HOSTILE_AUDIT_BC2_29;BC2_30_BLOCKED")


if __name__ == "__main__":
    main()
