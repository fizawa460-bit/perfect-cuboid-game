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
MAIN_WORKFLOW = ROOT.parent / ".github/workflows/stage32-ex5-main.yml"
FULL178_GOAL_CLAIM = "S32.FULL178.NUMERICAL_CENSUS.V1"
STAGE32_MAIN_BLOB = "9981889309c833a1834eaadddce73e52c0aa0176"
BC2_31_AUDIT_HEAD = "72118efafdd25ca3b08d408463db46e2800e22df"
BC2_31_AUDIT_REVIEW = 5184996992
BC2_31_CP_CANON = "f2aec1d923ff43393d24364864be36e223d43674149e6655a920d3b3d5de3ae4"
BC2_31_CP_BLOB = "188601efcb99d33fe00fc60dc3c2f40f51e65b20"
UNKNOWN_SHA = "df7db2159df41d93ce64b7d2ccf230b9363711bbdf769280e1df0560cfbae1ae"
BC2_32_SOURCE_BLOB = "7cfe8450cb9b9ab7f04da797d487655505598b93"
BC2_32_PREFLIGHT_BLOB = "45f2bb716266898a33ad49ea79ef1136907c8a09"
BC2_32_PREFLIGHT_CANON = "2fba662ed105bd3a2b8e8b0989483364b62a6feb6b04f5ce909c462d8ca93cb9"
PC_KEYS = {"perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim"}


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(f"FAIL: {msg}")


def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def checked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text())
    got = obj.get("canonical_sha256_without_this_field")
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    req(got == expected and csha(q) == expected, f"canonical drift: {path.name}")
    return obj


def main() -> None:
    s = json.loads((HERE / "MAIN-STATE.json").read_text())
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V17_BC2_31_AUDIT_CONSUMED_BC2_32_EXECUTION", "state schema drift")
    b = s["bootstrap"]
    req(b["current_main_sha_observed"] == "c31684fb5f63d8a025eb298c91861d4c979b0e28", "current MAIN observation drift")
    req(b["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch" and b["active_work_pr"] == 1776, "work surface drift")
    req(b["merge_authorized"] is False, "merge authorization leak")

    req(git_blob(STAGE32_MAIN) == STAGE32_MAIN_BLOB, "Stage32 MAIN blob drift")
    ma = json.loads(STAGE32_MAIN.read_text())
    req(ma["current_exact_frontier"]["full178_goal_claim_id"] == FULL178_GOAL_CLAIM, "FULL178 claim drift")

    p31 = s["prior_audited_authority"]["bc2_31_pr_1776"]
    req(p31["hostile_audit_status"] == "PASS", "BC2-31 PASS not consumed")
    req(p31["audit_checkpoint_exact_head"] == BC2_31_AUDIT_HEAD and p31["hostile_audit_review_id"] == BC2_31_AUDIT_REVIEW, "BC2-31 audit receipt drift")

    cp_path = B2 / "bc2-31-fresh-all7336-replay-checkpoint.json"
    cp = checked(cp_path, BC2_31_CP_CANON)
    req(git_blob(cp_path) == BC2_31_CP_BLOB, "BC2-31 checkpoint blob drift")
    fr = cp["fresh_replay"]
    req((fr["parents_checked"], fr["unsat_count"], fr["unknown_count"]) == (7336, 7166, 170), "BC2-31 counts drift")
    req(fr["sat_found"] is False and fr["all_unknown_identities_explicitly_retained"] is True, "BC2-31 target scope drift")
    req(fr["unknown_parent_indices_all_sha256"] == UNKNOWN_SHA and len(fr["unknown_parent_indices_all"]) == 170, "BC2-31 UNKNOWN list drift")

    src = B2 / "bc2_32_replay_explicit_fresh_unknown170.py"
    pf_path = B2 / "bc2-32-fresh-unknown170-replay-preflight.json"
    req(git_blob(src) == BC2_32_SOURCE_BLOB, "BC2-32 source blob drift")
    req(git_blob(pf_path) == BC2_32_PREFLIGHT_BLOB, "BC2-32 preflight blob drift")
    pf = checked(pf_path, BC2_32_PREFLIGHT_CANON)
    req(pf["audit_consumption"]["bc2_31_hostile_audit_review_id"] == BC2_31_AUDIT_REVIEW, "preflight audit receipt drift")
    req(pf["target"]["audited_fresh_unknown_parent_count"] == 170, "preflight target count drift")
    req(pf["target"]["audited_fresh_unknown_parent_indices_sha256"] == UNKNOWN_SHA, "preflight target identity drift")
    req(pf["execution"]["per_parent_timeout_ms"] == 20000 and pf["execution"]["effective_heavy_concurrency"] == 1, "preflight execution drift")
    req(pf["execution"]["heavy_scaleout_authorized"] is False, "preflight heavy scaleout leak")

    rk = json.loads((HERE / "runkeys/bc2-32-fresh-unknown170-replay.json").read_text())
    req(rk["schema"] == "STAGE32EX5_BC2_32_FRESH_UNKNOWN170_REPLAY_RUNKEY_V1", "runkey schema drift")
    req(rk["source_git_blob_sha"] == BC2_32_SOURCE_BLOB and rk["preflight_git_blob_sha"] == BC2_32_PREFLIGHT_BLOB, "runkey source lock drift")
    req(rk["preflight_canonical"] == BC2_32_PREFLIGHT_CANON, "runkey preflight canonical drift")
    req(rk["audit_consumption"]["bc2_31_hostile_audit_exact_head"] == BC2_31_AUDIT_HEAD and rk["audit_consumption"]["bc2_31_hostile_audit_review_id"] == BC2_31_AUDIT_REVIEW, "runkey audit receipt drift")
    req(rk["target"]["fresh_unknown_parent_count"] == 170 and rk["target"]["fresh_unknown_parent_indices_sha256"] == UNKNOWN_SHA, "runkey target drift")
    req(rk["execution"]["per_parent_timeout_ms"] == 20000 and rk["execution"]["effective_heavy_concurrency"] == 1 and rk["execution"]["heavy_scaleout_authorized"] is False, "runkey execution drift")
    req(rk["generation"] in (0, 1), "unexpected runkey generation")
    if rk["generation"] == 0:
        req(rk["armed"] is False and rk["consumed_run"] is None, "cold runkey drift")
    else:
        req(rk["armed"] is True and rk["consumed_run"] is None, "armed runkey drift")

    cur = s["current"]
    req(cur["status"] == "BC2_32_EXPLICIT_FRESH_UNKNOWN170_REPLAY_EXECUTION_AUTHORIZED", "current status drift")
    req(cur["leaf"] == "BC2_32_REPLAY_EXPLICIT_FRESH_UNKNOWN_SET" and cur["next_route"] == "BC2_32_REPLAY_EXPLICIT_FRESH_UNKNOWN_SET", "current route drift")
    req("NO_BC2_33" in cur["stop_semantics"] and "NO_MAIN_PROMOTION" in cur["stop_semantics"], "BC2-32 stop firewall drift")

    f = s["frontier"]
    req(f["e8_bc2_31_audited"] is True and f["e8_bc2_31_fresh_unknown_count"] == 170, "BC2-31 audited frontier drift")
    req(f["e8_bc2_32_target_unknown_count"] == 170 and f["e8_bc2_32_executed"] is False, "BC2-32 execution state drift")
    req(f["e8_known_parent_unsat_count_lower_bound"] == 7166, "pre-execution lower-bound drift")
    req(f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False, "local result promoted")

    a = s["intermediate_audit_boundary"]
    req(a["last_hostile_audit_status"] == "PASS" and a["last_hostile_audit_exact_head"] == BC2_31_AUDIT_HEAD and a["last_hostile_audit_review_id"] == BC2_31_AUDIT_REVIEW, "BC2-31 audit consumption drift")
    req(a["freeze_active"] is False and a["new_audit_boundary_exists"] is False and a["re_audit_required"] is False, "execution state incorrectly frozen")
    req(a["bc2_32_execution_authorized"] is True and a["bc2_31_execution_authorized"] is False, "BC2-32 authorization drift")

    ns = s["next_step"]
    req(ns["id"] == "BC2_32_REPLAY_EXPLICIT_FRESH_UNKNOWN_SET" and ns["bc2_32_execution_authorized"] is True, "next step drift")
    req(ns["bc2_33_blocked_until_bc2_32_hostile_audit_pass"] is True, "BC2-33 firewall drift")
    for k in ("heavy_scaleout_authorized", "main_promotion_authorized", "n350_registration_authorized", "merge_authorized"):
        req(ns[k] is False, f"authorization leak: {k}")

    observed = {k for k in s["firewalls"] if "cuboid" in k or "curboid" in k}
    req(observed == PC_KEYS, "Perfect Cuboid firewall key set drift")
    for section in ("historical_credit_firewall", "firewalls"):
        for key, value in s[section].items():
            req(value is False, f"firewall leak: {section}.{key}")
    for key, value in s["credit"].items():
        if key != "level":
            req(value is False, f"credit leak: credit.{key}")

    wf = MAIN_WORKFLOW.read_text()
    for token in (
        "authorize-bc2-32-fresh-unknown170:",
        "bc2-32-fresh-unknown170:",
        "bc2-32-fresh-unknown170-replay.json",
        BC2_32_SOURCE_BLOB,
        str(BC2_31_AUDIT_REVIEW),
    ):
        req(token in wf, f"main workflow missing BC2-32 token: {token}")
    req("authorize-bc2-31-recovery:" not in wf, "retired BC2-31 recovery auto job still present")

    for verifier in (
        "verify_bc2_25_boundary33_partition_checkpoint.py",
        "verify_bc2_26_boundary34_partition_checkpoint.py",
        "verify_bc2_27_boundary35_partition_checkpoint.py",
        "verify_bc2_28_boundary38_partition_checkpoint.py",
        "verify_bc2_29_boundary39_partition_checkpoint.py",
        "verify_bc2_30_boundary42_partition_checkpoint.py",
    ):
        subprocess.run([sys.executable, str(B2 / verifier)], check=True)

    print("PASS: Stage32EX5 BC2-31 hostile audit consumed; BC2-32 targeted fresh UNKNOWN replay narrowly authorized")
    print("target=170 audited UNKNOWN parents; timeout=20000ms; concurrency=1; heavy_scaleout=NO")
    print("known_parent_unsat_lower_bound=7166 pre-execution; Stage32_MAIN_credit=NO; merge=NO")
    print("next=arm BC2-32 generation1 only after exact-head integrity PASS")


if __name__ == "__main__":
    main()
