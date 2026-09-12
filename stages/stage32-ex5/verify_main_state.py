#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
B2 = HERE / "breadth-cycle-2"
ROOT = HERE.parents[0]
STAGE32_MAIN = ROOT / "stage32" / "MAIN-STATE.json"
TMP_WORKFLOW = ROOT.parent / ".github/workflows/stage32-ex5-bc2-31-fresh-replay.yml"
FULL178_GOAL_CLAIM = "S32.FULL178.NUMERICAL_CENSUS.V1"
STAGE32_MAIN_BLOB = "9981889309c833a1834eaadddce73e52c0aa0176"
BC2_30_AUDIT_HEAD = "38b60be7d0390ad5fa89ddb4dcd9511cfe36c57f"
BC2_30_AUDIT_REVIEW = 5184226057
BC2_31_CP_CANON = "f2aec1d923ff43393d24364864be36e223d43674149e6655a920d3b3d5de3ae4"
BC2_31_CP_BLOB = "188601efcb99d33fe00fc60dc3c2f40f51e65b20"
BC2_31_SOURCE_BLOB = "0433c448acfe55d17aa27f3ffd6c0e6e0a13d6f4"
BC2_31_PREFLIGHT_BLOB = "2b2e568da2cf643ffe7a72a07071f40c00780f1f"
BC2_31_PREFLIGHT_CANON = "a856d1eaedea9f71e7c33c96d84a0b6fc7310028896ebaa652a87c1298fbe1d0"
BC2_31_RUN = 34665881779
BC2_31_JOB = 103477565567
BC2_31_ART = 10288804651
UNKNOWN_SHA = "df7db2159df41d93ce64b7d2ccf230b9363711bbdf769280e1df0560cfbae1ae"
PC_KEYS = {"perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim"}


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(f"FAIL: {msg}")


def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    s = json.loads((HERE / "MAIN-STATE.json").read_text())
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V16_BC2_31_FRESH_REPLAY_AUDIT_BOUNDARY", "state schema drift")
    req(s["bootstrap"]["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch", "work branch drift")
    req(s["bootstrap"]["active_work_pr"] == 1776 and s["bootstrap"]["merge_authorized"] is False, "PR/merge state drift")

    req(git_blob(STAGE32_MAIN) == STAGE32_MAIN_BLOB, "Stage32 MAIN blob drift")
    ma = json.loads(STAGE32_MAIN.read_text())
    req(ma["current_exact_frontier"]["full178_goal_claim_id"] == FULL178_GOAL_CLAIM, "FULL178 claim drift")

    p30 = s["prior_audited_authority"]["bc2_30_pr_1776"]
    req(p30["hostile_audit_status"] == "PASS" and p30["audit_checkpoint_exact_head"] == BC2_30_AUDIT_HEAD and p30["hostile_audit_review_id"] == BC2_30_AUDIT_REVIEW, "BC2-30 predecessor audit drift")

    old = json.loads((HERE / "runkeys/bc2-31-recover-remaining172.json").read_text())
    req(old["generation"] == 2 and old["armed"] is False, "old recovery runkey not disarmed")
    oc = old.get("consumed_run") or {}
    req(oc.get("workflow_run_id") == 34660585544 and oc.get("accepted") is False, "failed historical recovery receipt drift")
    req(oc.get("raw_canonical") == "f5ef75a81dcb3a952689a0bad14fcf8b122d2b321b4b63a469b3e761910d7f13", "failed recovery canonical drift")

    cp_path = B2 / "bc2-31-fresh-all7336-replay-checkpoint.json"
    cp = json.loads(cp_path.read_text())
    expected = cp.pop("canonical_sha256_without_this_field")
    req(expected == BC2_31_CP_CANON and csha(cp) == BC2_31_CP_CANON, "BC2-31 checkpoint canonical drift")
    req(git_blob(cp_path) == BC2_31_CP_BLOB, "BC2-31 checkpoint blob drift")
    fr = cp["fresh_replay"]
    req((fr["parents_checked"], fr["unsat_count"], fr["unknown_count"]) == (7336, 7166, 170), "BC2-31 fresh counts drift")
    req(fr["sat_found"] is False and fr["all_unknown_identities_explicitly_retained"] is True, "fresh replay scope drift")
    req(fr["unknown_parent_indices_all_sha256"] == UNKNOWN_SHA and len(fr["unknown_parent_indices_all"]) == 170, "UNKNOWN identity list drift")
    req(cp["interpretation"]["historical_remaining172_exact_identity_recovery_claim"] is False, "historical 172 inference leak")
    req(cp["credit"]["known_parent_unsat_count_lower_bound"] == 7166 and cp["credit"]["stage32_main_credit"] is False, "fresh credit drift")

    req(git_blob(B2 / "bc2_31_fresh_all7336_replay.py") == BC2_31_SOURCE_BLOB, "fresh producer blob drift")
    req(git_blob(B2 / "bc2-31-fresh-all7336-replay-preflight.json") == BC2_31_PREFLIGHT_BLOB, "fresh preflight blob drift")
    pf = json.loads((B2 / "bc2-31-fresh-all7336-replay-preflight.json").read_text())
    q = dict(pf); q.pop("canonical_sha256_without_this_field", None)
    req(pf["canonical_sha256_without_this_field"] == BC2_31_PREFLIGHT_CANON and csha(q) == BC2_31_PREFLIGHT_CANON, "fresh preflight canonical drift")

    rk = json.loads((HERE / "runkeys/bc2-31-fresh-all7336-replay.json").read_text())
    req(rk["generation"] == 1 and rk["armed"] is False, "fresh runkey not consumed/disarmed")
    rc = rk.get("consumed_run") or {}
    req((rc.get("workflow_run_id"), rc.get("compute_job_id"), rc.get("artifact_id")) == (BC2_31_RUN, BC2_31_JOB, BC2_31_ART), "fresh workflow receipt drift")
    req(rc.get("result_canonical") == BC2_31_CP_CANON and rc.get("unknown_parent_indices_all_sha256") == UNKNOWN_SHA, "fresh runkey result lock drift")
    req(rc.get("accepted_for_hostile_audit") is True, "fresh result not marked audit candidate")

    cur = s["current"]
    req(cur["status"] == "BC2_31_FRESH_ALL7336_REPLAY_EXECUTED_AUDIT_REQUIRED", "current status drift")
    req(cur["next_route"] == "HOSTILE_AUDIT_BC2_31_FRESH_ALL7336_REPLAY", "current route drift")
    req("NO_BC2_32" in cur["stop_semantics"] and "NO_HISTORICAL_172_IDENTITY_INFERENCE" in cur["stop_semantics"], "stop firewall drift")
    f = s["frontier"]
    req(f["e8_bc2_31_fresh_replay_executed"] is True and f["e8_bc2_31_fresh_unsat_count"] == 7166 and f["e8_bc2_31_fresh_unknown_count"] == 170, "frontier fresh replay drift")
    req(f["e8_bc2_31_exact_remaining172_recovered"] is False and f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False, "frontier overclaim")

    a = s["intermediate_audit_boundary"]
    req(a["last_hostile_audit_exact_head"] == BC2_30_AUDIT_HEAD and a["last_hostile_audit_review_id"] == BC2_30_AUDIT_REVIEW, "predecessor audit receipt drift")
    req(a["freeze_active"] is True and a["new_audit_boundary_exists"] is True and a["re_audit_required"] is True, "audit freeze drift")
    req(a["bc2_31_execution_authorized"] is False, "BC2-31 execution left authorized")
    req(s["next_step"]["id"] == "HOSTILE_AUDIT_BC2_31_FRESH_ALL7336_REPLAY" and s["next_step"]["bc2_32_blocked_until_bc2_31_hostile_audit_pass"] is True, "next-step drift")

    req(not TMP_WORKFLOW.exists(), "temporary BC2-31 executor still active")
    observed = {k for k in s["firewalls"] if "cuboid" in k or "curboid" in k}
    req(observed == PC_KEYS, "Perfect Cuboid firewall key set drift")
    for section in ("historical_credit_firewall", "firewalls"):
        for key, value in s[section].items(): req(value is False, f"firewall leak: {section}.{key}")
    for key, value in s["credit"].items():
        if key != "level": req(value is False, f"credit leak: credit.{key}")

    for verifier in (
        "verify_bc2_25_boundary33_partition_checkpoint.py",
        "verify_bc2_26_boundary34_partition_checkpoint.py",
        "verify_bc2_27_boundary35_partition_checkpoint.py",
        "verify_bc2_28_boundary38_partition_checkpoint.py",
        "verify_bc2_29_boundary39_partition_checkpoint.py",
        "verify_bc2_30_boundary42_partition_checkpoint.py",
    ):
        subprocess.run([sys.executable, str(B2 / verifier)], check=True)

    print("PASS: Stage32EX5 BC2-31 fresh all7336 replay retained and frozen for hostile audit")
    print("fresh=7166_UNSAT_170_UNKNOWN_0_SAT; unknown identities explicit; historical remaining172 recovery=REFUSED")
    print("whole_first_block_unsat=NO; FULL178_complete=NO; Stage32_MAIN_credit=NO; merge=NO")
    print("next=stage32ex5-audit")

if __name__ == "__main__":
    main()
