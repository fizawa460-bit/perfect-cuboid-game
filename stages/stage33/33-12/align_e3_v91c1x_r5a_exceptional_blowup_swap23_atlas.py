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

OLD_STATE_SHA = "c98172b7d84ecfef88be2c6318274f213839952fe3d86354027a2bf01fd01717"
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
CANDIDATE = "V91C1X_R5A_A2_02_EXCEPTIONAL_STANDARD_BLOWUP_CHARTS_AND_SWAP23_REFINEMENT_SKELETON"
AUDIT_LEAF = CANDIDATE + "_HOSTILE_AUDIT"


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


def assert_cert():
    cert, claimed = load_locked(CERT)
    if cert.get("candidate") != CANDIDATE:
        raise SystemExit("R5A candidate moved")
    if cert["entry"] != {"authority": AUTH, "stage33_progress": "6/11", "pr": 1722}:
        raise SystemExit("R5A authority/progress/PR moved")
    s = cert["summary"]
    if s["exceptional_support_components"] != 4 or s["standard_blowup_charts_materialized"] != 12:
        raise SystemExit("R5A exceptional atlas incomplete")
    if not s["exceptional_standard_chart_cover_exact"] or not s["exceptional_overlap_units_materialized"]:
        raise SystemExit("R5A exceptional atlas exact checks incomplete")
    if not s["swap23_common_refinement_skeleton_materialized"]:
        raise SystemExit("R5A swap23 refinement skeleton missing")
    if s["side_isolation_opens_materialized"] != 0 or s["full_eight_component_finite_cover_materialized"]:
        raise SystemExit("R5A partial-cover boundary moved")
    if s["literal_mu2_2_cocycle_materialized"] or s["source_bound_full_surface_h2_representative_materialized"]:
        raise SystemExit("R5A H2/Cech credit boundary moved")
    xc = cert["exact_consequence"]
    if xc["next_exact_leaf"] != AUDIT_LEAF or xc["stage33_12_closed_exact"]:
        raise SystemExit("R5A next leaf/Stage33-12 closure boundary moved")
    if not xc["authority_unchanged"] or not xc["stage33_progress_unchanged"]:
        raise SystemExit("R5A authority/progress firewall moved")
    if any(cert["credit_firewall"].values()):
        raise SystemExit("R5A downstream credit firewall moved")
    return claimed


def build_checkpoint(old, cert_sha):
    new = dict(old)
    new.update({
        "authority": "OPERATIONAL_ONLY_NOT_PROOF",
        "status": "V91C1X_R5A_EXCEPTIONAL_BLOWUP_SWAP23_ATLAS_MAIN_COMPLETE_PENDING_HOSTILE_AUDIT",
        "frontier": CANDIDATE,
        "frontier_certificate_sha256": cert_sha,
        "failure_category": "HOSTILE_AUDIT_REQUIRED_BEFORE_R5A_EXCEPTIONAL_ATLAS_CREDIT_OR_R5B_CONTINUATION",
        "next_leaf": AUDIT_LEAF,
        "r5a_exceptional_blowup_swap23_atlas_materialized": True,
        "r5a_exceptional_blowup_swap23_atlas_audited": False,
        "r5a_exceptional_standard_blowup_charts": "12/12",
        "r5a_exceptional_overlap_transitions": "24/24_ORDERED",
        "r5a_side_isolation_opens_materialized": "0/4",
        "r5a_full_eight_component_finite_cover_materialized": False,
        "r5a_literal_mu2_2_cocycle_materialized": False,
        "r5a_source_bound_full_surface_h2_representative_materialized": False,
        "stage33_12_released_for_existing_repair_scope": True,
        "stage33_12_closed_exact": False,
        "pr": 1722,
    })
    return new


def assert_state_invariants(state):
    if state["authority_sync"]["frontier_authority"] != AUTH or state["stage33_progress"] != "6/11":
        raise SystemExit("proof authority/progress moved")
    cur = state["current"]
    if cur["unit"] != "33-12" or cur["substep"] != "E3_V91C1X_R5_SOURCE_BOUND_COVER_GLUE_PACKAGE_ACTIVE":
        raise SystemExit("Stage33-12 R5 route moved")
    if cur["next_exact_leaf"] != "V91C1X_R5_FIND_OR_CONSTRUCT_SOURCE_BOUND_A2_02_FINITE_COVER_LOCAL_EQUATION_UNIFORMIZER_OVERLAP_GLUE_PACKAGE":
        raise SystemExit("R5 parent leaf moved")
    fw = state["firewalls"]
    for key in ["stage33_07_reclosed", "stage33_08_released", "stage33_12_closed_exact", "stage33_13_released", "theorem_credit", "receiver_credit", "endpoint_credit", "merge_allowed"]:
        if fw.get(key) is not False:
            raise SystemExit(f"downstream firewall moved: {key}")


def check():
    cert_sha = assert_cert()
    state, claimed = load_locked(STATE)
    assert_state_invariants(state)
    old = dict(state["work_checkpoint"])
    expected = build_checkpoint(old, cert_sha)
    # A previously aligned state is recognized by its R5A status; rebuild from a
    # stripped predecessor to avoid self-extension changing the expected object.
    if old.get("status") == "V91C1X_R5A_EXCEPTIONAL_BLOWUP_SWAP23_ATLAS_MAIN_COMPLETE_PENDING_HOSTILE_AUDIT":
        for k in [
            "r5a_exceptional_blowup_swap23_atlas_materialized",
            "r5a_exceptional_blowup_swap23_atlas_audited",
            "r5a_exceptional_standard_blowup_charts",
            "r5a_exceptional_overlap_transitions",
            "r5a_side_isolation_opens_materialized",
            "r5a_full_eight_component_finite_cover_materialized",
            "r5a_literal_mu2_2_cocycle_materialized",
            "r5a_source_bound_full_surface_h2_representative_materialized",
        ]:
            old.pop(k, None)
        expected = build_checkpoint(old, cert_sha)
    if state["work_checkpoint"] != expected:
        raise SystemExit("R5A work_checkpoint not aligned")
    text = SYNC.read_text(encoding="utf-8")
    if sync_sha(text) != claimed:
        raise SystemExit("sync_main_state STATE_SHA not aligned")
    print(json.dumps({"status":"PASS","main_state_sha":claimed,"frontier":CANDIDATE,"frontier_certificate_sha256":cert_sha,"next_leaf":AUDIT_LEAF,"stage33_progress":"6/11"}, sort_keys=True))


def write():
    cert_sha = assert_cert()
    state, claimed = load_locked(STATE)
    assert_state_invariants(state)
    text = SYNC.read_text(encoding="utf-8")
    old = state["work_checkpoint"]
    if old.get("status") == "V91C1X_R5A_EXCEPTIONAL_BLOWUP_SWAP23_ATLAS_MAIN_COMPLETE_PENDING_HOSTILE_AUDIT":
        check()
        return
    if claimed != OLD_STATE_SHA:
        raise SystemExit(f"unexpected pre-R5A MAIN-STATE lock: {claimed}")
    if old.get("status") != "STAGE33_12_RELEASED_RESUME_EXISTING_R5_SOURCE_BOUND_COVER_GLUE":
        raise SystemExit("pre-R5A release checkpoint moved")
    if old.get("stage33_11_closed_exact") is not True or old.get("stage33_12_released_for_existing_repair_scope") is not True:
        raise SystemExit("Stage33-11/12 prerequisite moved")
    if sync_sha(text) != claimed:
        raise SystemExit("pre-R5A sync STATE_SHA mismatch")

    proof_before = {k:v for k,v in state.items() if k not in {"canonical_sha256", "work_checkpoint"}}
    state["work_checkpoint"] = build_checkpoint(old, cert_sha)
    proof_after = {k:v for k,v in state.items() if k not in {"canonical_sha256", "work_checkpoint"}}
    if proof_before != proof_after:
        raise SystemExit("proof-relevant MAIN-STATE changed during R5A alignment")

    body = dict(state)
    body.pop("canonical_sha256", None)
    new_sha = csha(body)
    state["canonical_sha256"] = new_sha
    STATE.write_text(json.dumps(state, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    text2, n = re.subn(r"^STATE_SHA='[0-9a-f]{64}'$", f"STATE_SHA='{new_sha}'", text, count=1, flags=re.M)
    if n != 1:
        raise SystemExit("failed to patch sync_main_state STATE_SHA")
    SYNC.write_text(text2, encoding="utf-8")
    print(json.dumps({"status":"WROTE","old_main_state_sha":claimed,"new_main_state_sha":new_sha,"frontier_certificate_sha256":cert_sha}, sort_keys=True))


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--write", action="store_true")
    g.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if args.write:
        write()
    check()


if __name__ == "__main__":
    main()
