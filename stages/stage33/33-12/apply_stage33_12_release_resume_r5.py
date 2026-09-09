#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
STATE = STAGE33 / "MAIN-STATE.json"
SYNC = STAGE33 / "sync_main_state.py"
DECISION = HERE / "stage33-12-release-resume-r5-decision.json"

OLD_STATE_SHA = "279e19062296234c52276db5993c25a9a68f846897467ecf3f088de4bc5864d0"
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
SOURCE_HEAD = "19287284bd006e43029783139e628b82931f0390"
SOURCE_REVIEW = 5155040445
H_CERT_SHA = "5c37431587bf30ccd11f3212db1ef6ecc2f4bd134b439303386fce1bc6089ae6"
R5_LEAF = "V91C1X_R5_FIND_OR_CONSTRUCT_SOURCE_BOUND_A2_02_FINITE_COVER_LOCAL_EQUATION_UNIFORMIZER_OVERLAP_GLUE_PACKAGE"
R5_SUBSTEP = "E3_V91C1X_R5_SOURCE_BOUND_COVER_GLUE_PACKAGE_ACTIVE"

NEW_CHECKPOINT = {
    "authority": "OPERATIONAL_ONLY_NOT_PROOF",
    "consumed_c4b2b2f_hostile_reaudit_exact_head": "29f3dab7936b79f3f761af004dbedb10797802f3",
    "consumed_c4b2b2f_hostile_reaudit_review": 5150755582,
    "consumed_c4b2b2g_hostile_audit_exact_head": "8edfc08159cca1b95815278317873488075657f1",
    "consumed_c4b2b2g_hostile_audit_review": 5151676010,
    "consumed_c4b2b2h_hostile_audit_exact_head": "0e6af14e8b806eb857b8a8844f206a118008a15f",
    "consumed_c4b2b2h_hostile_audit_review": 5152927668,
    "consumed_post_h_freshness_exact_head": SOURCE_HEAD,
    "consumed_post_h_freshness_review": SOURCE_REVIEW,
    "failure_category": "R5_SOURCE_BOUND_A2_02_COVER_GLUE_PACKAGE_NOT_YET_MATERIALIZED",
    "frontier": "V91C1X_R5B3B3C4B2B2H_REPAIRED_STAGE33_11G_EXACT_EXIT",
    "frontier_certificate_sha256": H_CERT_SHA,
    "historical_stage33_11f_26_column_closure_reuse_allowed": False,
    "historical_stage33_11g_44_prime_exact_exit_reuse_allowed": False,
    "next_leaf": R5_LEAF,
    "pr": 1722,
    "repaired_stage33_11f_26_column_closure_audited": True,
    "repaired_stage33_11f_26_column_closure_materialized": True,
    "repaired_stage33_11f_exact_audited_connecting_columns": "26/26",
    "repaired_stage33_11g_exact_exit_audited": True,
    "repaired_stage33_11g_exact_exit_condition_satisfied": True,
    "repaired_stage33_11g_exact_exit_materialized": True,
    "stage33_11_closed_exact": True,
    "stage33_12_released_for_existing_repair_scope": True,
    "stage33_12_closed_exact": False,
    "status": "STAGE33_12_RELEASED_RESUME_EXISTING_R5_SOURCE_BOUND_COVER_GLUE",
}


def csha(obj: dict) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if csha(body) != claimed:
        raise SystemExit(f"canonical mismatch: {path}")
    return obj, claimed


def sync_sha(text: str) -> str:
    m = re.search(r"^STATE_SHA='([0-9a-f]{64})'$", text, flags=re.M)
    if not m:
        raise SystemExit("sync_main_state STATE_SHA not found")
    return m.group(1)


def assert_decision():
    d = json.loads(DECISION.read_text(encoding="utf-8"))
    if d.get("schema") != "STAGE33_12_RELEASE_RESUME_R5_DECISION_V1":
        raise SystemExit("release decision schema moved")
    if d.get("source_exact_head") != SOURCE_HEAD or d.get("source_hostile_audit_review") != SOURCE_REVIEW:
        raise SystemExit("release decision hostile-audit provenance moved")
    p = d["prerequisite"]
    if not p["repaired_stage33_11_closed_exact"] or not p["repaired_stage33_11g_exact_exit_audited"]:
        raise SystemExit("Stage33-11 prerequisite not exact/audited")
    if p["c4b2b2h_certificate_sha256"] != H_CERT_SHA:
        raise SystemExit("C4B2B2H source lock moved")
    dec = d["decision"]
    if not dec["stage33_12_released_for_existing_repair_scope"] or dec["stage33_12_closed_exact"]:
        raise SystemExit("Stage33-12 release/closure boundary moved")
    if dec["resume_existing_r5_leaf"] != R5_LEAF or dec["resume_existing_r5_substep"] != R5_SUBSTEP:
        raise SystemExit("R5 resume leaf moved")
    if not dec["mathematical_authority_unchanged"] or not dec["stage33_progress_unchanged"] or dec["stage33_progress"] != "6/11":
        raise SystemExit("authority/progress boundary moved")
    if any(d["firewalls"].values()):
        raise SystemExit("downstream firewall unexpectedly released")


def assert_state_invariants(state: dict):
    if state["authority_sync"]["frontier_authority"] != AUTH or state["stage33_progress"] != "6/11":
        raise SystemExit("proof authority/progress moved")
    cur = state["current"]
    if cur["unit"] != "33-12" or cur["substep"] != R5_SUBSTEP or cur["next_exact_leaf"] != R5_LEAF:
        raise SystemExit("existing Stage33-12 R5 current leaf moved")
    fw = state["firewalls"]
    for key in ["stage33_07_reclosed", "stage33_08_released", "stage33_12_closed_exact", "stage33_13_released", "theorem_credit", "receiver_credit", "endpoint_credit", "merge_allowed"]:
        if fw.get(key) is not False:
            raise SystemExit(f"downstream firewall moved: {key}")


def check():
    assert_decision()
    state, claimed = load_locked(STATE)
    assert_state_invariants(state)
    if state.get("work_checkpoint") != NEW_CHECKPOINT:
        raise SystemExit("Stage33-12 release/resume checkpoint not applied")
    text = SYNC.read_text(encoding="utf-8")
    if sync_sha(text) != claimed:
        raise SystemExit("sync_main_state STATE_SHA not aligned")
    print(json.dumps({"status":"PASS","main_state_sha":claimed,"stage33_12_released":True,"stage33_12_closed_exact":False,"next_leaf":R5_LEAF,"stage33_progress":"6/11"}, sort_keys=True))


def write():
    assert_decision()
    state, claimed = load_locked(STATE)
    assert_state_invariants(state)
    text = SYNC.read_text(encoding="utf-8")
    if state.get("work_checkpoint") == NEW_CHECKPOINT:
        if sync_sha(text) != claimed:
            raise SystemExit("already-released checkpoint has stale sync STATE_SHA")
        return
    if claimed != OLD_STATE_SHA:
        raise SystemExit(f"unexpected pre-release MAIN-STATE lock: {claimed}")
    old = state.get("work_checkpoint", {})
    if old.get("next_leaf") != "STAGE33_12_SEPARATE_RELEASE_SUMMARY_DECISION" or old.get("stage33_11_closed_exact") is not True:
        raise SystemExit("pre-release Stage33-11/12 boundary moved")
    if old.get("consumed_post_h_freshness_review") is not None:
        raise SystemExit("post-H freshness receipt unexpectedly pre-consumed")
    if sync_sha(text) != claimed:
        raise SystemExit("pre-release sync STATE_SHA mismatch")

    proof_before = {k: v for k, v in state.items() if k not in {"canonical_sha256", "work_checkpoint"}}
    state["work_checkpoint"] = NEW_CHECKPOINT
    proof_after = {k: v for k, v in state.items() if k not in {"canonical_sha256", "work_checkpoint"}}
    if proof_before != proof_after:
        raise SystemExit("proof-relevant MAIN-STATE changed during Stage33-12 release")

    body = dict(state)
    body.pop("canonical_sha256", None)
    new_sha = csha(body)
    state["canonical_sha256"] = new_sha
    STATE.write_text(json.dumps(state, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    text2, n = re.subn(r"^STATE_SHA='[0-9a-f]{64}'$", f"STATE_SHA='{new_sha}'", text, count=1, flags=re.M)
    if n != 1:
        raise SystemExit("failed to patch sync_main_state STATE_SHA")
    SYNC.write_text(text2, encoding="utf-8")
    print(json.dumps({"status":"WROTE","old_main_state_sha":claimed,"new_main_state_sha":new_sha}, sort_keys=True))


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if args.write:
        write()
    check()


if __name__ == "__main__":
    main()
