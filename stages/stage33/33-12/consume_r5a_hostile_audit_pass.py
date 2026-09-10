#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
STATE = S33 / "MAIN-STATE.json"
SYNC = S33 / "sync_main_state.py"
CERT = HERE / "e3-v91c1x-r5a-a2-02-exceptional-blowup-swap23-atlas.json"
RECEIPT = HERE / "r5a-hostile-audit-pass-consumption.json"

OLD_STATE_SHA = "3aa765e4e458362551aa848bc1eb7ae2314e1f6035a509451641c4a406c0a280"
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
CANDIDATE = "V91C1X_R5A_A2_02_EXCEPTIONAL_STANDARD_BLOWUP_CHARTS_AND_SWAP23_REFINEMENT_SKELETON"
CERT_SHA = "4d8c7fbf517dba8968d3ecdd871f9f80544859bd05563a7c4c8dd123c43555d1"
AUDITED_HEAD = "f2ef0692fb9c186680d58693d2569aae84188827"
AUDIT_REVIEW_NODE = "PRR_kwDOTr52Y88AAAABM6R4BQ"
AUDIT_AT = "2026-09-10T00:34:00Z"
NEXT_LEAF = "V91C1X_R5B_A2_02_SIDE_COMPONENT_ISOLATION_AND_LOCAL_EQUATIONS_CONSTRUCTION"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if csha(body) != claimed:
        raise SystemExit(f"canonical mismatch: {path}")
    return obj, claimed


def sync_sha(text: str):
    m = re.search(r"^STATE_SHA='([0-9a-f]{64})'$", text, flags=re.M)
    if not m:
        raise SystemExit("sync_main_state STATE_SHA not found")
    return m.group(1)


def assert_cert_and_receipt():
    cert, claimed = load_locked(CERT)
    if claimed != CERT_SHA or cert.get("candidate") != CANDIDATE:
        raise SystemExit("R5A certificate identity/hash moved")
    if cert.get("entry") != {"authority": AUTH, "stage33_progress": "6/11", "pr": 1722}:
        raise SystemExit("R5A authority/progress/PR moved")
    s = cert["summary"]
    if s["exceptional_support_components"] != 4 or s["standard_blowup_charts_materialized"] != 12:
        raise SystemExit("R5A exceptional atlas incomplete")
    if not s["exceptional_standard_chart_cover_exact"] or not s["exceptional_overlap_units_materialized"]:
        raise SystemExit("R5A exceptional atlas exact boundary moved")
    if s["side_isolation_opens_materialized"] != 0 or s["full_eight_component_finite_cover_materialized"]:
        raise SystemExit("R5A partial-cover boundary moved")
    if s["literal_mu2_2_cocycle_materialized"] or s["source_bound_full_surface_h2_representative_materialized"]:
        raise SystemExit("R5A H2/Cech firewall moved")
    if any(cert["credit_firewall"].values()):
        raise SystemExit("R5A downstream credit firewall moved")

    r = json.loads(RECEIPT.read_text(encoding="utf-8"))
    expected = {
        "schema": "STAGE33_R5A_EXCEPTIONAL_BLOWUP_SWAP23_HOSTILE_AUDIT_PASS_CONSUMPTION_V1",
        "pr": 1722,
        "audited_exact_head": AUDITED_HEAD,
        "hostile_audit_review_node": AUDIT_REVIEW_NODE,
        "hostile_audit_submitted_at": AUDIT_AT,
        "hostile_audit_verdict": "PASS",
        "r5a_certificate_sha256": CERT_SHA,
    }
    for key, value in expected.items():
        if r.get(key) != value:
            raise SystemExit(f"R5A receipt field moved: {key}")
    b = r["consumption_boundary"]
    for key in ["mathematical_authority_unchanged", "stage33_progress_unchanged", "r5a_exceptional_blowup_swap23_atlas_audited"]:
        if b.get(key) is not True:
            raise SystemExit(f"R5A positive receipt boundary moved: {key}")
    for key in ["r5a_full_eight_component_finite_cover_materialized", "r5a_literal_mu2_2_cocycle_materialized", "r5a_source_bound_full_surface_h2_representative_materialized", "stage33_12_closed_exact", "stage33_13_released", "theorem_credit", "receiver_credit", "endpoint_credit", "perfect_cuboid_credit", "merge_allowed"]:
        if b.get(key) is not False:
            raise SystemExit(f"R5A receipt firewall moved: {key}")
    if b.get("next_action") != NEXT_LEAF:
        raise SystemExit("R5A receipt next action moved")


def assert_state_firewalls(state):
    if state["authority_sync"]["frontier_authority"] != AUTH or state["stage33_progress"] != "6/11":
        raise SystemExit("proof authority/progress moved")
    fw = state["firewalls"]
    for key in ["stage33_07_reclosed", "stage33_08_released", "stage33_12_closed_exact", "stage33_13_released", "theorem_credit", "receiver_credit", "endpoint_credit", "merge_allowed"]:
        if fw.get(key) is not False:
            raise SystemExit(f"downstream firewall moved: {key}")


def new_checkpoint(old):
    new = dict(old)
    new.update({
        "authority": "OPERATIONAL_ONLY_NOT_PROOF",
        "status": "V91C1X_R5A_HOSTILE_AUDIT_PASS_CONSUMED_R5B_SIDE_COMPONENT_ISOLATION_ACTIVE",
        "frontier": CANDIDATE,
        "frontier_certificate_sha256": CERT_SHA,
        "consumed_r5a_hostile_audit_exact_head": AUDITED_HEAD,
        "consumed_r5a_hostile_audit_review_node": AUDIT_REVIEW_NODE,
        "r5a_exceptional_blowup_swap23_atlas_materialized": True,
        "r5a_exceptional_blowup_swap23_atlas_audited": True,
        "r5a_exceptional_standard_blowup_charts": "12/12",
        "r5a_exceptional_overlap_transitions": "24/24_ORDERED",
        "r5a_side_isolation_opens_materialized": "0/4",
        "r5a_full_eight_component_finite_cover_materialized": False,
        "r5a_literal_mu2_2_cocycle_materialized": False,
        "r5a_source_bound_full_surface_h2_representative_materialized": False,
        "failure_category": "R5B_SIDE_COMPONENT_ISOLATION_AND_LOCAL_EQUATIONS_STILL_MISSING",
        "next_leaf": NEXT_LEAF,
        "stage33_12_released_for_existing_repair_scope": True,
        "stage33_12_closed_exact": False,
        "pr": 1722,
    })
    return new


def check():
    assert_cert_and_receipt()
    state, claimed = load_locked(STATE)
    assert_state_firewalls(state)
    cp = state["work_checkpoint"]
    if cp.get("status") != "V91C1X_R5A_HOSTILE_AUDIT_PASS_CONSUMED_R5B_SIDE_COMPONENT_ISOLATION_ACTIVE":
        raise SystemExit("R5A hostile PASS not consumed")
    if cp != new_checkpoint(cp):
        raise SystemExit("R5A consumed checkpoint fields moved")
    text = SYNC.read_text(encoding="utf-8")
    if sync_sha(text) != claimed:
        raise SystemExit("sync_main_state STATE_SHA not aligned")
    print(json.dumps({"status":"PASS","main_state_sha":claimed,"audited_head":AUDITED_HEAD,"audit_review_node":AUDIT_REVIEW_NODE,"r5a_audited":True,"next_leaf":NEXT_LEAF,"stage33_progress":"6/11"}, sort_keys=True))


def write():
    assert_cert_and_receipt()
    state, claimed = load_locked(STATE)
    assert_state_firewalls(state)
    text = SYNC.read_text(encoding="utf-8")
    cp = state["work_checkpoint"]
    if cp.get("status") == "V91C1X_R5A_HOSTILE_AUDIT_PASS_CONSUMED_R5B_SIDE_COMPONENT_ISOLATION_ACTIVE":
        check()
        return
    if claimed != OLD_STATE_SHA:
        raise SystemExit(f"unexpected pre-consumption MAIN-STATE lock: {claimed}")
    if cp.get("status") != "V91C1X_R5A_EXCEPTIONAL_BLOWUP_SWAP23_ATLAS_MAIN_COMPLETE_PENDING_HOSTILE_AUDIT":
        raise SystemExit("unexpected pre-consumption R5A checkpoint")
    if cp.get("frontier") != CANDIDATE or cp.get("frontier_certificate_sha256") != CERT_SHA:
        raise SystemExit("R5A frontier lock moved")
    if cp.get("r5a_exceptional_blowup_swap23_atlas_materialized") is not True or cp.get("r5a_exceptional_blowup_swap23_atlas_audited") is not False:
        raise SystemExit("R5A audit gate state moved")
    if cp.get("r5a_side_isolation_opens_materialized") != "0/4":
        raise SystemExit("R5A side-isolation boundary moved")
    if sync_sha(text) != claimed:
        raise SystemExit("pre-consumption sync STATE_SHA mismatch")

    proof_before = {k: v for k, v in state.items() if k not in {"canonical_sha256", "work_checkpoint"}}
    state["work_checkpoint"] = new_checkpoint(cp)
    proof_after = {k: v for k, v in state.items() if k not in {"canonical_sha256", "work_checkpoint"}}
    if proof_before != proof_after:
        raise SystemExit("proof-relevant MAIN-STATE changed during R5A audit consumption")

    body = dict(state)
    body.pop("canonical_sha256", None)
    new_sha = csha(body)
    state["canonical_sha256"] = new_sha
    STATE.write_text(json.dumps(state, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    text2, n = re.subn(r"^STATE_SHA='[0-9a-f]{64}'$", f"STATE_SHA='{new_sha}'", text, count=1, flags=re.M)
    if n != 1:
        raise SystemExit("failed to patch sync_main_state STATE_SHA")
    SYNC.write_text(text2, encoding="utf-8")
    print(json.dumps({"status":"WROTE","old_main_state_sha":claimed,"new_main_state_sha":new_sha,"next_leaf":NEXT_LEAF}, sort_keys=True))


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
