#!/usr/bin/env python3
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
STATE = ROOT / "stages/stage32/final-chain/32-03-multibranch/STATE.json"
HANDOFF = Path(__file__).with_name("MB104-COMPACT-AUDIT-RESTART-20260920.md")
RUNKEY = Path(__file__).with_name("runkeys") / "000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"
WORKFLOW = ROOT / ".github/workflows/stage32-mb104-isotropic-shell-pilot.yml"

EXPECTED = {
    "base_main": "659ba93b9eba657b49a728f549c6bb6028398e08",
    "predecessor_pr": 1825,
    "predecessor_boundary": "d13afbb1a693a5547bebd31ec6fbcc04a7648f05",
    "substantive_freeze_boundary": "37e70e06635892ff29970e58f26efec0f498432b",
    "audit_release_head": "70c2fe772df63362d82df537ea889658eb03f58f",
    "audit_review_id": 5257816963,
    "pair_map": {
        "restriction_certificate_blob": "7b65e7845e0a5028f61afbd85777c541d9eff305",
        "restriction_note_blob": "186173988d6d3d99839d39b7c6b07863e31ba894",
        "discriminant_certificate_blob": "3ee982baf491ecce19b1e49707e66e1edacf812f",
        "discriminant_note_blob": "0e1f7d60276c4e8aa23d1a3236149454cecec7b0",
        "verifier_blob": "6238d8f6c1977dbe88ff78ade09cb5bc5f4b019b",
    },
    "r4": {
        "note_blob": "7fbe74fbab2a0b4c848a1c5c1910b603f72b0adf",
        "certificate_blob": "024ac0e4f1b1caed527e01becd60cea41c27409b",
        "verifier_blob": "df5355623736f188059d0f1c04ce718eef0ef3f6",
    },
    "isotropic": {
        "note_blob": "c65e9daa8f29a4ba525742116c9995cdc9cc504d",
        "certificate_blob": "67e897bd2d46b3382282449b301235af2497109b",
        "cold_runkey_blob": "9dcd460c5d7a73a87e4ed24569c742cac42ea511",
    },
    "runner_locks": {
        "runner_git_blob": "1ad6c42b41a2c044933bd04c0495b40814f22b9e",
        "parent_verifier_git_blob": "5b1d120b6cd2dcd6d23ebcaa889448b897a479db",
        "workunit_runner_git_blob": "671fa6cbc2ea171a4abebacf44e8122189e8397f",
        "workunit_verifier_git_blob": "2a067db553a45f2f8e70783ec6b95495fc976360",
        "stage33_stoll_helper_blob": "010db3767b8f932c71ac5722b50ccb64a8c79f9d",
        "stage33_picard_marking_blob": "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7",
    },
}

def req(ok, msg):
    if not ok:
        raise SystemExit("FAIL: " + msg)

def git_blob(path):
    return subprocess.check_output(["git","hash-object",str(path.relative_to(ROOT))], cwd=ROOT, text=True).strip()

def main():
    d=json.loads(STATE.read_text())
    req(d["schema"]=="STAGE32_32_03_MULTIBRANCH_STATE_V1","state schema")
    req(d["mission_id"]=="stage32-32-03-multibranch","mission")
    req(d["current_node"]=="MB104","current node")
    req(d["completed_retained_nodes"]==["MB101","MB102","MB103"],"completed nodes")
    req(d["status"] in {"FROZEN_COMPACT_AUDIT_RESTART_NO_CREDIT","ACTIVE_POST_AUDIT_ZERO_CREDIT","FROZEN_POST_AUDIT_APPEND_REAUDIT_REQUIRED_NO_CREDIT"},"state mode")

    freeze=d["audit_freeze"]
    req(freeze["substantive_boundary_head"]==EXPECTED["substantive_freeze_boundary"],"substantive freeze boundary")
    req(freeze["boundary_semantics"]=="COMPACT_RESTART_SUBSTANTIVE_CONTENT_FROZEN","freeze semantics")

    rb=d["restart_boundary"]
    req(rb["base_main"]==EXPECTED["base_main"],"base main")
    req(rb["predecessor_pr"]==EXPECTED["predecessor_pr"],"predecessor PR")
    req(rb["predecessor_retained_boundary"]==EXPECTED["predecessor_boundary"],"predecessor boundary")
    req(rb["local_history_copied"] is False,"history must not be copied")

    pm=d["retained_frontier"]["pair_map"]
    req(pm["status"]=="ARCHIVED_PRE_AUDIT_ZERO_EXCLUSION_CREDIT","pair-map status")
    req(pm["support_mask"]=="000707000f0f","support mask")
    for k,v in EXPECTED["pair_map"].items():
        req(pm[k]==v,f"pair-map lock {k}")
    req("all r=1,2,3,4 remain OPEN" in pm["result"],"all restriction degrees open")
    req("no orbit excluded" in pm["result"],"no orbit exclusion")
    req("864" in pm["result"],"support count 864")
    req("Stein/common-vertical correction mandatory" in pm["result"],"Stein correction")

    r4=d["retained_frontier"]["r4"]
    req(r4["status"]=="ARCHIVED_PRE_AUDIT_NO_CREDIT","R4 status")
    for k,v in EXPECTED["r4"].items():
        req(r4[k]==v,f"R4 lock {k}")
    req("no finite window or credit" in r4["result"],"R4 zero credit")

    iso=d["retained_frontier"]["isotropic_shell_preflight"]
    req(iso["note_blob"]==EXPECTED["isotropic"]["note_blob"],"isotropic note lock")
    req(iso["certificate_blob"]==EXPECTED["isotropic"]["certificate_blob"],"isotropic certificate lock")
    old=iso.get("cold_preflight_runkey_blob",iso.get("runkey_blob"))
    req(old==EXPECTED["isotropic"]["cold_runkey_blob"],"cold isotropic runkey lock")
    req(iso["numerical_execution_completed"] is False,"isotropic execution must still be false in retained STATE")

    routing=d["routing"]
    if d["status"]=="FROZEN_COMPACT_AUDIT_RESTART_NO_CREDIT":
        req(d["next_obligation"]["active_leaf"]=="MB104-COMPACT-HOSTILE-REAUDIT-RESTART","audit leaf")
        req(routing["substantive_research_append_blocked_until_reaudit_pass"] is True,"research blocked")
        head=subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip()
        req(subprocess.run(["git","merge-base","--is-ancestor",EXPECTED["substantive_freeze_boundary"],head],cwd=ROOT).returncode==0,"freeze ancestor")
        allowed=set(freeze["allowed_post_boundary_paths"])
        changed={x for x in subprocess.check_output(["git","diff","--name-only",EXPECTED["substantive_freeze_boundary"]+".."+head],cwd=ROOT,text=True).splitlines() if x}
        req(changed<=allowed,"post-freeze substantive path detected: "+",".join(sorted(changed-allowed)))
        mode="FROZEN"
    elif d["status"]=="FROZEN_POST_AUDIT_APPEND_REAUDIT_REQUIRED_NO_CREDIT":
        ar=d["audit_release"]
        req(ar["hostile_audit_status"]=="PASS_AT_OLDER_EXACT_HEAD_ONLY","older-head audit status")
        req(ar["audited_exact_head"]==EXPECTED["audit_release_head"],"older audit head")
        req(ar["hostile_audit_review_id"]==EXPECTED["audit_review_id"],"older audit review")
        req(ar["current_head_inherits_pass"] is False,"current head must not inherit audit")
        req(routing["substantive_research_append_blocked_until_reaudit_pass"] is True,"reaudit research freeze")
        req(routing["isotropic_shell_pilot_authorized"] is False,"pilot must be blocked")
        req(routing["isotropic_shell_scaleout_authorized"] is False,"scaleout must be blocked")
        req(routing["current_head_reaudit_required"] is True,"current-head reaudit required")
        req(routing["latest_audited_exact_head"]==EXPECTED["audit_release_head"],"latest audited head")
        req(routing["active_pr_number"]==1827,"active PR")
        req(routing["active_branch"]=="stage32mb-audit-restart-20260920","active branch")
        req(d["active_surface"]["pr_number"]==1827,"active surface PR")
        req(d["active_surface"]["predecessor_archive_pr"]==1825,"archive predecessor")
        req(d["next_obligation"]["active_leaf"]=="MB104-POST-AUDIT-APPEND-REAUDIT-CHECKPOINT","reaudit leaf")
        req(iso["status"]=="POST_AUDIT_APPEND_FROZEN_FOR_REAUDIT_NO_NUMERICAL_CREDIT","isotropic reaudit freeze")
        req(iso["pilot_runkey_generation"]==3 and iso["pilot_shell_index"]==0,"cold pilot generation")
        req(iso["numerical_execution_completed"] is False,"no numerical execution")
        req(RUNKEY.is_file() and WORKFLOW.is_file(),"frozen pilot files")
        k=json.loads(RUNKEY.read_text())
        req(k["schema"]=="STAGE32_MB104_000707_FIBRATION_ISOTROPIC_SHELLS_RUNKEY_V1","runkey schema")
        req(k["generation"]==3 and k["mode"]=="COLD" and k["armed"] is False,"runkey cold")
        req(k["leaf"]=="MB104-POST-AUDIT-APPEND-REAUDIT-CHECKPOINT","runkey reaudit leaf")
        req(k["pilot"]["shell_index"]==0 and k["pilot"]["measured"] is False,"pilot remains unmeasured")
        req(k["execution_gate"]["workflow_class"]=="MANUAL","manual workflow class")
        req(k["execution_gate"]["automatic_execution_authorized"] is False,"automatic execution blocked")
        req(k["execution_gate"]["current_head_execution_blocked"] is True,"current-head execution blocked")
        req(k["execution_gate"]["scaleout_authorized"] is False,"scaleout blocked")
        req(k["execution_gate"]["shells_1_2_3_authorized"] is False,"remaining shells blocked")
        req(k["source_locks"]["current_state_git_blob"] is None,"cold runkey state lock must be null")
        req(k["source_locks"]["workflow_git_blob"] is None,"cold runkey workflow lock must be null")
        req(all(v is False for v in k["credit"].values()),"cold runkey credit firewall")
        w=WORKFLOW.read_text()
        req("workflow_dispatch:" in w,"manual workflow dispatch")
        req("pull_request:" not in w,"manual workflow must not auto-trigger on PR")
        mode="POST_AUDIT_APPEND_REAUDIT_FROZEN"
    else:
        ar=d["audit_release"]
        req(ar["hostile_audit_status"]=="PASS","audit release status")
        req(ar["audited_exact_head"]==EXPECTED["audit_release_head"],"audit release head")
        req(ar["hostile_audit_review_id"]==EXPECTED["audit_review_id"],"audit review")
        req(ar["current_main_at_audit"]==EXPECTED["base_main"],"audit current main")
        req(ar["merge_ready_freshness"]=="CLEAR","audit freshness")
        req(ar["grants"]=="ORDINARY_MB104_RESEARCH_RESUME_ONLY","audit grant scope")
        req(routing["substantive_research_append_blocked_until_reaudit_pass"] is False,"research release")
        req(routing["ordinary_mb104_research_released_by_review"]==EXPECTED["audit_review_id"],"release review")
        req(routing["isotropic_shell_pilot_authorized"] is True,"pilot authorization")
        req(routing["isotropic_shell_scaleout_authorized"] is False,"scaleout must remain blocked")
        req(routing["finite_picard_enumeration_released"] is False,"MB105 carrier enumeration remains blocked")
        req(d["next_obligation"]["active_leaf"]=="MB104-000707-FIBRATION-ISOTROPIC-SHELLS-PILOT","pilot leaf")
        req(iso["status"]=="AUDIT_RELEASED_PILOT_ARMED_NO_NUMERICAL_RESULT","isotropic pilot status")
        req(iso["pilot_runkey_generation"]==2 and iso["pilot_shell_index"]==0,"pilot state")
        req(RUNKEY.is_file() and WORKFLOW.is_file(),"pilot execution files")
        k=json.loads(RUNKEY.read_text())
        req(k["schema"]=="STAGE32_MB104_000707_FIBRATION_ISOTROPIC_SHELLS_RUNKEY_V1","runkey schema")
        req(k["generation"]==2 and k["mode"]=="PILOT" and k["armed"] is True,"runkey arm")
        req(k["leaf"]=="MB104-000707-FIBRATION-ISOTROPIC-SHELLS-PILOT","runkey leaf")
        req(k["pilot"]["shell_index"]==0 and k["pilot"]["measured"] is False,"pilot shell")
        req(k["execution_gate"]["pilot_only"] is True and k["execution_gate"]["scaleout_authorized"] is False,"pilot-only gate")
        req(k["execution_gate"]["hostile_audit_review_id"]==EXPECTED["audit_review_id"],"runkey audit review")
        req(k["source_locks"]["predecessor_boundary"]==EXPECTED["predecessor_boundary"],"runkey predecessor")
        for fld,val in EXPECTED["runner_locks"].items():
            req(k["source_locks"][fld]==val,f"runner lock {fld}")
        req(k["source_locks"]["current_state_git_blob"]==git_blob(STATE),"state source lock")
        req(k["source_locks"]["workflow_git_blob"]==git_blob(WORKFLOW),"workflow source lock")
        req(k["concurrency"]["planned_effective_heavy_concurrency"]==1,"pilot concurrency")
        req(k["concurrency"]["stage_heavy_cap"]==18,"heavy cap")
        req(k["storage"]["repository_operating_budget_mb"]==500,"storage budget")
        req(k["storage"]["raw_magma_stdout_persisted"] is False,"raw stdout retention")
        req(k["storage"]["retention_days_if_executed"]==1,"retention")
        req(all(v is False for v in k["credit"].values()),"runkey credit firewall")
        mode="POST_AUDIT_PILOT"

    req(all(v is False for v in d["credit_firewall"].values()),"credit firewall")
    h=HANDOFF.read_text()
    for needle in (
        EXPECTED["base_main"],
        EXPECTED["predecessor_boundary"],
        "all restriction degrees `r=1,2,3,4` remain OPEN",
        "remaining balanced support count is `48+48+768=864`",
        "No shell execution is consumed",
        "ZERO CREDIT",
    ):
        req(needle in h,f"handoff text: {needle}")
    for section in ("pair_map","r4","isotropic"):
        for v in EXPECTED[section].values():
            req(re.fullmatch(r"[0-9a-f]{40}",v) is not None,f"blob syntax {section}")

    print("PASS: MB104 compact restart controller",mode)
    print("base main",EXPECTED["base_main"])
    print("predecessor retained boundary",EXPECTED["predecessor_boundary"])
    print("pair-map: all r open, no excluded orbit, 864 supports")
    print("credit firewalls remain false")

if __name__=="__main__":
    main()
