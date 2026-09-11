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
BC2_26_AUDIT_HEAD = "34d6b030095b97c738f6faf6b9045f366622592c"
BC2_26_AUDIT_REVIEW = 5177919212
BC2_27 = "0f9278799809fd1a48c187f9a9668631422ab3136478cb3f9f64fd423df71462"
BC2_27_RAW = "6537cdece0d03e80fb704e9ee8b95de240ec7dc043e872004ca78d4199a08fbd"
BC2_27_RUN = 34593864110
BC2_27_INTEGRITY_JOB = 103245034147
BC2_27_JOB = 103245141239
BC2_27_HEAD = "21828bcf36ea33d1e6c26465eea74c646ba26901"
BC2_27_ARTIFACT = 10262350002

def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(f"FAIL: {msg}")

def main() -> None:
    s=json.loads((HERE/"MAIN-STATE.json").read_text())
    req(s["schema"]=="STAGE32EX5_MAIN_COMPACT_STATE_V9_BC2_27_AUDIT_BOUNDARY","state schema drift")
    b=s["bootstrap"]
    req(b["current_main_sha_observed"]==MAIN,"current-main observation drift")
    req(b["work_branch"]=="stage32ex5-bc2-25-boundary33-mainbatch" and b["active_work_pr"]==1776,"active work surface drift")
    req(b["merge_authorized"] is False,"merge authorization leak")
    a=s["stage32_main_authority"]
    req(a["control_mode"]=="FULL178_AND_FINAL_MILESTONE_CHAIN" and a["primary_incomplete_id"]=="32-01","Stage32 route drift")
    req(a["n356_status"]=="AUDIT_REQUIRED" and a["n356_audit_credit_consumed"] is False and a["n356_main_pruning_credit"] is False,"N356 credit leak")
    cur=s["current"]
    req(cur["status"]=="BC2_27_RETAINED_HOSTILE_AUDIT_REQUIRED","BC2-27 status drift")
    req(cur["leaf"]=="BC2_27_BOUNDARY35_PARTITION_RETAINED","BC2-27 leaf drift")
    req(cur["next_route"]=="HOSTILE_AUDIT_BC2_27_RECHECK","audit-first route drift")
    req(cur["stop_semantics"]=="BC2_28_BLOCKED_UNTIL_BC2_27_HOSTILE_AUDIT_PASS","BC2-28 stop firewall drift")
    f=s["frontier"]
    req((f["e8_bc2_27_new_parent_unsat_count"],f["e8_bc2_27_retained_unknown_count"],f["e8_bc2_27_parent_sat_count"])==(3,9,0),"BC2-27 parent accounting drift")
    req((f["e8_bc2_27_branch_unsat_count"],f["e8_bc2_27_branch_unknown_count"],f["e8_bc2_27_branch_sat_count"])==(7,13,0),"BC2-27 branch accounting drift")
    req((f["e8_bc2_27_p33_subbranch_unsat_count"],f["e8_bc2_27_p33_subbranch_unknown_count"],f["e8_bc2_27_p33_subbranch_sat_count"])==(7,13,0),"BC2-27 p33 accounting drift")
    req((f["e8_bc2_27_p34_target_unsat_count"],f["e8_bc2_27_p34_target_unknown_count"],f["e8_bc2_27_p34_target_sat_count"])==(10,13,0),"BC2-27 p34 accounting drift")
    req((f["e8_bc2_27_p35_leaf_unsat_count"],f["e8_bc2_27_p35_leaf_unknown_count"],f["e8_bc2_27_p35_leaf_sat_count"])==(57,13,0),"BC2-27 p35 accounting drift")
    req(f["e8_known_parent_unsat_count_lower_bound"]==7155 and f["e8_bc2_27_unretained_unknown_identity_count"]==172,"BC2-27 lower-bound/firewall drift")
    req(f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False,"local result promoted")
    rp=s["retained_exact_progress"]
    req(rp["bc2_25_checkpoint_canonical"]==BC2_25 and rp["bc2_25_hostile_audit_exact_head"]==BC2_25_AUDIT_HEAD and rp["bc2_25_hostile_audit_review_id"]==BC2_25_AUDIT_REVIEW,"BC2-25 receipt drift")
    req(rp["bc2_26_checkpoint_canonical"]==BC2_26 and rp["bc2_26_hostile_audit_exact_head"]==BC2_26_AUDIT_HEAD and rp["bc2_26_hostile_audit_review_id"]==BC2_26_AUDIT_REVIEW,"BC2-26 PASS receipt drift")
    req(rp["bc2_27_checkpoint_canonical"]==BC2_27 and rp["bc2_27_raw_result_canonical"]==BC2_27_RAW,"BC2-27 checkpoint/raw lock drift")
    req(rp["bc2_27_workflow_run_id"]==BC2_27_RUN and rp["bc2_27_integrity_job_id"]==BC2_27_INTEGRITY_JOB and rp["bc2_27_compute_job_id"]==BC2_27_JOB and rp["bc2_27_exact_compute_head"]==BC2_27_HEAD,"BC2-27 run provenance drift")
    req(rp["bc2_27_artifact_id"]==BC2_27_ARTIFACT,"BC2-27 artifact drift")
    audit=s["intermediate_audit_boundary"]
    req(audit["candidate_pr"]==1776 and audit["candidate_checkpoint_canonical"]==BC2_27,"BC2-27 audit checkpoint drift")
    req(audit["predecessor_hostile_audit_status"]=="PASS" and audit["predecessor_hostile_audit_exact_head"]==BC2_26_AUDIT_HEAD and audit["predecessor_hostile_audit_review_id"]==BC2_26_AUDIT_REVIEW,"BC2-26 predecessor audit receipt drift")
    req(audit["last_hostile_audit_status"]=="PENDING" and audit["re_audit_required"] is True and audit["freeze_active"] is True,"BC2-27 boundary not frozen")
    req(audit["bc2_28_execution_authorized"] is False and audit["merged"] is False,"BC2-28/merge authorization leak")
    ns=s["next_step"]
    req(ns["id"]=="BC2_27_HOSTILE_AUDIT_RECHECK" and ns["bc2_28_blocked_until_audit_pass"] is True,"next-step audit gate drift")
    for k in ("heavy_scaleout_authorized","main_promotion_authorized","n350_registration_authorized","merge_authorized"):
        req(ns[k] is False,f"authorization leak: {k}")
    for section in ("credit","historical_credit_firewall","firewalls"):
        for key,value in s[section].items():
            if key!="level": req(value is False,f"credit/firewall leak: {section}.{key}")
    runkey=json.loads((HERE/"runkeys/bc2-27-boundary35-partition.json").read_text())
    req(runkey["armed"] is False,"BC2-27 runkey must stay disarmed")
    req(runkey["consumed_run"]["checkpoint_canonical"]==BC2_27 and runkey["consumed_run"]["retained_checkpoint_committed"] is True,"BC2-27 consumed checkpoint drift")
    subprocess.run([sys.executable,str(B2/"verify_bc2_25_boundary33_partition_checkpoint.py")],check=True)
    subprocess.run([sys.executable,str(B2/"verify_bc2_26_boundary34_partition_checkpoint.py")],check=True)
    subprocess.run([sys.executable,str(B2/"verify_bc2_27_boundary35_partition_checkpoint.py")],check=True)
    docs={name:(HERE/name).read_text() for name in ["README.md","MAIN-START-HERE.md","CURRENT-ROADMAP.md","CURRENT-AUDIT-CONTRACT.md","MAINBATCH-OPERATIONS.md"]}
    for name,text in docs.items():
        for token in ("BC2-27","7155","9","13","172","#1776"):
            req(token in text,f"{name} missing BC2-27 boundary token: {token}")
        req("BC2-28" in text and ("blocked" in text.lower() or "禁止" in text),f"{name} does not block BC2-28 before audit PASS")
    req(BC2_27 in docs["CURRENT-AUDIT-CONTRACT.md"] and str(BC2_27_RUN) in docs["CURRENT-AUDIT-CONTRACT.md"],"audit contract missing BC2-27 receipt")
    print("PASS: Stage32EX5 BC2-27 retained hostile-audit boundary is coherent")
    print("bc2_27=3_NEW_UNSAT_9_RETAINED_UNKNOWN_0_SAT;13_BRANCH_UNKNOWN;13_P33_UNKNOWN;13_P34_UNKNOWN;13_P35_TIMEOUT_UNKNOWN;172_OTHER_IDENTITIES_UNINFERRED")
    print("known_parent_unsat_lower_bound=7155")
    print("stage32_main_credit=NO;merge_authorized=NO")
    print("next=HOSTILE_AUDIT_BC2_27_RECHECK;BC2_28_BLOCKED")

if __name__=="__main__": main()
