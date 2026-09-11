#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
B2 = HERE / "breadth-cycle-2"
STAGE32_MAIN = HERE.parent / "stage32" / "MAIN-STATE.json"
EX5_WORKFLOW = ROOT / ".github" / "workflows" / "stage32-ex5-main.yml"
TEMP_BC2_28_WORKFLOW = ROOT / ".github" / "workflows" / "stage32-ex5-bc2-28.yml"
MAIN = "c31684fb5f63d8a025eb298c91861d4c979b0e28"
STAGE32_MAIN_BLOB = "9981889309c833a1834eaadddce73e52c0aa0176"
FULL178_GOAL_CLAIM = "S32.FULL178.NUMERICAL_CENSUS.V1"
BC2_27_AUDIT_HEAD = "b70bc51909f5ed78641ee3b727a2258382ef950c"
BC2_27_AUDIT_REVIEW = 5179488973
BC2_28_CHECKPOINT = "52138e7c417d69814d5007479420b56fcc27031679bf88f432916e6c89c77ec4"
BC2_28_CHECKPOINT_BLOB = "bec4b7c06de727339b8eaf42f5158b7f28ba0376"
BC2_28_PRIOR_MALFORMED_CHECKPOINT_BLOB = "a4ea686f58d51ab451f9dbac420bfc97ca41d6ed"
BC2_28_RAW = "f77cad8d03035514e43e992ccdee25c1d4f6a386789fac33e488e198c35a998d"
BC2_28_RAW_SHA256 = "768c4209d2162cd85a2c93a3bfcb3a71e8ea9a600e62b1323b8f7b372139f843"
PERFECT_CUBOID_FIREWALL_KEYS = {"perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim"}


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(f"FAIL: {msg}")


def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def main() -> None:
    s = json.loads((HERE / "MAIN-STATE.json").read_text(encoding="utf-8"))
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V11_BC2_28_RETAINED_AUDIT_BOUNDARY", "state schema drift")

    b = s["bootstrap"]
    req(b["current_main_sha_observed"] == MAIN, "current-main observation drift")
    req(b["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch" and b["active_work_pr"] == 1776, "active work surface drift")
    req(b["merge_authorized"] is False, "merge authorization leak")

    a = s["stage32_main_authority"]
    req(a["routing_source"] == "stages/stage32/MAIN-STATE.json", "Stage32 routing source drift")
    req(a["routing_source_blob_sha"] == STAGE32_MAIN_BLOB, "Stage32 authority blob lock drift")
    req(a["full178_goal_claim_id_observed"] == FULL178_GOAL_CLAIM, "FULL178 projection drift")
    req(git_blob(STAGE32_MAIN) == STAGE32_MAIN_BLOB, "Stage32 MAIN authority blob drift")
    ma = json.loads(STAGE32_MAIN.read_text(encoding="utf-8"))
    req(ma["current_exact_frontier"]["full178_goal_claim_id"] == FULL178_GOAL_CLAIM, "authoritative FULL178 claim-id drift")
    req(a["n356_status"] == "AUDIT_REQUIRED" and a["n356_audit_credit_consumed"] is False and a["n356_main_pruning_credit"] is False, "N356 credit leak")

    prior = s["prior_audited_authority"]["bc2_27_pr_1776"]
    req(prior["hostile_audit_status"] == "PASS" and prior["audit_checkpoint_exact_head"] == BC2_27_AUDIT_HEAD and prior["hostile_audit_review_id"] == BC2_27_AUDIT_REVIEW, "BC2-27 PASS authority drift")

    cur = s["current"]
    req(cur["status"] == "BC2_28_RESULT_RETAINED_HOSTILE_AUDIT_REQUIRED", "BC2-28 retained status drift")
    req(cur["leaf"] == "BC2_28_BOUNDARY38_PARTITION_RETAINED_AUDIT_BOUNDARY", "BC2-28 retained leaf drift")
    req(cur["next_route"] == "HOSTILE_AUDIT_BC2_28", "BC2-28 audit route drift")
    req(cur["stop_semantics"] == "NO_BC2_29_OR_BROAD_PROMOTION_BEFORE_BC2_28_HOSTILE_AUDIT_PASS", "BC2-29 stop firewall drift")

    raw_mirror = "stages/stage32-ex5/breadth-cycle-2/bc2-28-boundary38-partition-raw.json"
    req(raw_mirror not in s["current_leaf_working_set"], "malformed raw mirror leaked into current working set")
    req(not (B2 / "bc2-28-boundary38-partition-raw.json").exists(), "non-authoritative raw mirror must remain absent")

    f = s["frontier"]
    req(f["e8_bc2_28_executed"] is True and f["e8_bc2_28_audited"] is False, "BC2-28 execution/audit marker drift")
    req((f["e8_bc2_28_new_parent_unsat_count"], f["e8_bc2_28_retained_unknown_count"], f["e8_bc2_28_parent_sat_count"]) == (5, 4, 0), "BC2-28 parent accounting drift")
    req((f["e8_bc2_28_branch_unknown_count"], f["e8_bc2_28_p33_subbranch_unknown_count"], f["e8_bc2_28_p34_target_unknown_count"], f["e8_bc2_28_p35_leaf_unknown_count"]) == (4,4,4,4), "BC2-28 residual hierarchy drift")
    req((f["e8_bc2_28_p38_leaf_unsat_count"], f["e8_bc2_28_p38_leaf_unknown_count"]) == (38,4), "BC2-28 p38 accounting drift")
    req(f["e8_known_parent_unsat_count_lower_bound"] == 7160 and f["e8_bc2_28_unretained_unknown_identity_count"] == 172, "BC2-28 lower-bound/firewall drift")
    req(f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False, "local result promoted")

    rp = s["retained_exact_progress"]
    req(rp["bc2_28_checkpoint_canonical"] == BC2_28_CHECKPOINT, "BC2-28 checkpoint canonical drift")
    req(rp["bc2_28_checkpoint_git_blob_sha"] == BC2_28_CHECKPOINT_BLOB, "BC2-28 checkpoint blob receipt drift")
    req(rp["bc2_28_prior_malformed_checkpoint_git_blob_sha"] == BC2_28_PRIOR_MALFORMED_CHECKPOINT_BLOB, "BC2-28 checkpoint repair provenance drift")
    req(git_blob(B2 / "bc2-28-boundary38-partition-checkpoint.json") == BC2_28_CHECKPOINT_BLOB, "BC2-28 checkpoint blob drift")
    req(rp["bc2_28_raw_result_canonical"] == BC2_28_RAW and rp["bc2_28_raw_json_sha256"] == BC2_28_RAW_SHA256, "BC2-28 artifact raw identity drift")
    req(rp["bc2_28_raw_repository_mirror_retained"] is False, "BC2-28 raw mirror authority leak")
    req(rp["bc2_28_raw_artifact_receipt_authoritative"] is True, "BC2-28 artifact receipt authority missing")
    req("bc2_28_raw_result_git_blob_sha" not in rp, "stale raw mirror blob receipt leaked into state")
    req(rp["bc2_28_workflow_run_id"] == 34609454583 and rp["bc2_28_compute_job_id"] == 103296259426, "BC2-28 workflow/job receipt drift")
    req(rp["bc2_28_artifact_id"] == 10268117064 and rp["bc2_28_known_parent_unsat_count_lower_bound"] == 7160, "BC2-28 artifact/lower-bound receipt drift")
    req(rp["bc2_28_retained_unknown_parent_indices"] == [1048,1050,1064,1103], "BC2-28 residual parent receipt drift")

    runkey = json.loads((HERE / "runkeys/bc2-28-boundary38-partition.json").read_text(encoding="utf-8"))
    req(runkey["schema"] == "STAGE32EX5_BC2_28_BOUNDARY38_PARTITION_RUNKEY_V1" and runkey["generation"] == 1 and runkey["armed"] is False, "BC2-28 runkey not consumed/disarmed")
    consumed = runkey["consumed_run"]
    req(consumed["checkpoint_canonical"] == BC2_28_CHECKPOINT and consumed["checkpoint_git_blob_sha"] == BC2_28_CHECKPOINT_BLOB, "BC2-28 consumed checkpoint evidence drift")
    req(consumed["prior_malformed_checkpoint_git_blob_sha"] == BC2_28_PRIOR_MALFORMED_CHECKPOINT_BLOB, "BC2-28 consumed repair provenance drift")
    req(consumed["raw_result_canonical"] == BC2_28_RAW and consumed["raw_json_sha256"] == BC2_28_RAW_SHA256, "BC2-28 consumed raw digest drift")
    req(consumed["raw_repository_mirror_authoritative"] is False, "BC2-28 consumed raw mirror authority leak")
    req((consumed["new_parent_unsat_count"], consumed["retained_unknown_parent_count"], consumed["parent_sat_count"]) == (5,4,0), "BC2-28 consumed parent accounting drift")
    req((consumed["p38_leaf_unsat_count"], consumed["p38_leaf_unknown_count"]) == (38,4), "BC2-28 consumed p38 accounting drift")
    req(consumed["known_parent_unsat_count_lower_bound"] == 7160, "BC2-28 consumed lower-bound drift")

    workflow_text = EX5_WORKFLOW.read_text(encoding="utf-8")
    req("authorize-bc2-28:" not in workflow_text, "duplicate BC2-28 authorization path reintroduced")
    req("bc2-28-boundary38-bounded:" not in workflow_text, "duplicate BC2-28 heavy executor reintroduced")
    req("Verify retained BC2-28 boundary38 checkpoint and artifact receipt" in workflow_text, "BC2-28 exact-head verifier step missing")
    req(not TEMP_BC2_28_WORKFLOW.exists(), "temporary BC2-28 auto workflow must remain removed")

    claim = s["claim_sync"]
    req(claim["existing_active_goal"] == FULL178_GOAL_CLAIM and claim["lane_role"] == "ATTACKS", "claim-sync drift")
    req(claim["active_frontier_remapped"] is False and claim["main_promotion"] is False, "claim-sync promotion leak")

    audit = s["intermediate_audit_boundary"]
    req(audit["new_audit_boundary_exists"] is True and audit["freeze_active"] is True and audit["re_audit_required"] is True, "BC2-28 audit boundary not frozen")
    req(audit["bc2_28_execution_authorized"] is False and audit["bc2_29_execution_authorized"] is False, "BC2-28/29 authorization leak")
    req(audit["merged"] is False, "merge state leak")

    ns = s["next_step"]
    req(ns["id"] == "HOSTILE_AUDIT_BC2_28_RETAINED_BOUNDARY" and ns["bc2_29_blocked_until_bc2_28_hostile_audit_pass"] is True, "BC2-28 next-step drift")
    for k in ("heavy_scaleout_authorized", "main_promotion_authorized", "n350_registration_authorized", "merge_authorized"):
        req(ns[k] is False, f"authorization leak: {k}")

    fw = s["firewalls"]
    observed_pc_keys = {k for k in fw if "cuboid" in k or "curboid" in k}
    req(observed_pc_keys == PERFECT_CUBOID_FIREWALL_KEYS, "Perfect Cuboid firewall key-set drift")
    for section in ("credit", "historical_credit_firewall", "firewalls"):
        for key, value in s[section].items():
            if key != "level":
                req(value is False, f"credit/firewall leak: {section}.{key}")

    subprocess.run([sys.executable, str(B2 / "verify_bc2_25_boundary33_partition_checkpoint.py")], check=True)
    subprocess.run([sys.executable, str(B2 / "verify_bc2_26_boundary34_partition_checkpoint.py")], check=True)
    subprocess.run([sys.executable, str(B2 / "verify_bc2_27_boundary35_partition_checkpoint.py")], check=True)
    subprocess.run([sys.executable, str(B2 / "verify_bc2_28_boundary38_partition_checkpoint.py")], check=True)

    docs = {name: (HERE / name).read_text(encoding="utf-8") for name in ["README.md","MAIN-START-HERE.md","CURRENT-ROADMAP.md","CURRENT-AUDIT-CONTRACT.md","MAINBATCH-OPERATIONS.md"]}
    for name, text in docs.items():
        for token in ("BC2-28", "boundary38", "7160", "172", "#1776", str(BC2_27_AUDIT_REVIEW)):
            req(token in text, f"{name} missing BC2-28 retained-boundary token: {token}")
        req("BC2-29" in text and ("blocked" in text.lower() or "禁止" in text), f"{name} does not block BC2-29")
        req("audit" in text.lower(), f"{name} does not identify audit boundary")

    print("PASS: Stage32EX5 BC2-28 retained boundary is coherent, non-rerunnable, and frozen for hostile audit")
    print("bc2_28=5_NEW_UNSAT_4_RETAINED_UNKNOWN_0_SAT;38_P38_UNSAT_4_P38_UNKNOWN;known_parent_unsat_lower_bound=7160")
    print("raw_authority=ARTIFACT_RECEIPT_ONLY;duplicate_bc2_28_heavy_path=ABSENT")
    print("stage32_main_credit=NO;full178_complete=NO;merge_authorized=NO")
    print("next=HOSTILE_AUDIT_BC2_28;BC2_29_BLOCKED")


if __name__ == "__main__":
    main()
