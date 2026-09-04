#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "stages/stage36/MAIN-STATE.json"
CERT_PATH = ROOT / "stages/stage36/36-03/physical-open-boundary.json"

AUDITED_CERT_BLOB = "fc1947b2de08f7d8a104bdc91902b20e88635349"
AUDITED_HEAD = "5fd7af75ede4cd2eceb70f9f21bd2b98ec5453a6"
AUDIT_REVIEW = 5113890803
AUDIT_CI_RUN = 33880359998
AUDIT_CI_JOB = 101047238497
AUDITED_MERGE = "45f290a443cf71b1fc62f031994122c3fa58f0e9"


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def main() -> None:
    # S30-WF02: freeze the hostile-audited 36-03 mathematical certificate byte-for-byte.
    require(blob_sha(CERT_PATH) == AUDITED_CERT_BLOB, "36-03 audited certificate blob drift")
    cert = json.loads(CERT_PATH.read_text())
    require(cert.get("schema") == "STAGE36_36_03_PHYSICAL_OPEN_PUSH_BOUNDARY_V1", "36-03 audited schema moved")
    require(cert.get("status") == "EXACT_PHYSICAL_OPEN_PUSH_BOUNDARY_PENDING_HOSTILE_AUDIT", "36-03 historical status moved")
    require(cert.get("pass_condition") == {"ENDPOINT_TO_EACH_Q_REPRESENTATIVE_PUSH_EXACT": True, "CONVERSE_LIFT_CLAIM": False}, "36-03 pass condition moved")
    require(cert.get("scheme_vs_rational_firewall", {}).get("U_H_Q_equals_q_H_of_U_Q_claimed") is False, "36-03 lift firewall moved")
    require(cert.get("restricted_receiver_preparation", {}).get("receiver_intersection_exclusion_executed") is False, "36-03 S34-W03 execution drift")
    require(all(v is False for v in cert.get("claims", {}).values()), "36-03 audited certificate leaked higher credit")

    state = json.loads(STATE_PATH.read_text())
    require(state.get("schema") == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V7_36_03_AUDITED", "36-03 audited successor schema moved")
    require(state.get("status") == "ACTIVE", "36-03 audited successor not ACTIVE")
    require(state.get("base_main_sha") == AUDITED_MERGE, "36-03 promotion base moved")

    auth = state.get("stage36_36_03_authority", {})
    require(auth == {
        "pr": 1553,
        "hostile_audit_review": AUDIT_REVIEW,
        "audited_head": AUDITED_HEAD,
        "merged_main_sha": AUDITED_MERGE,
        "exact_head_ci_run": AUDIT_CI_RUN,
        "exact_head_ci_job": AUDIT_CI_JOB,
        "certificate_blob_sha": AUDITED_CERT_BLOB,
        "verdict": "PASS",
    }, "36-03 authority block moved")

    unit = state.get("completed_units", {}).get("36-03", {})
    require(unit.get("status") == "AUDITED_PASS", "36-03 unit not audited PASS")
    require(unit.get("promotion_status") == "AUDITED", "36-03 promotion status moved")
    require(unit.get("hostile_audit_review") == AUDIT_REVIEW, "36-03 review moved")
    require(unit.get("audited_head") == AUDITED_HEAD, "36-03 audited head moved")
    require(unit.get("exact_head_ci_run") == AUDIT_CI_RUN and unit.get("exact_head_ci_job") == AUDIT_CI_JOB, "36-03 CI identity moved")
    require(unit.get("merged_main_sha") == AUDITED_MERGE and unit.get("certificate_blob_sha") == AUDITED_CERT_BLOB, "36-03 immutable authority moved")
    require(unit.get("ENDPOINT_TO_EACH_Q_REPRESENTATIVE_PUSH_EXACT") is True, "36-03 exact push credit lost")
    require(unit.get("CONVERSE_LIFT_CLAIM") is False and unit.get("NEW_THEOREM_CREDIT") is False, "36-03 credit firewall moved")

    gates = state.get("promotion_gates", {})
    require(gates.get("source_authority_lock_complete") is True, "36-01 gate lost")
    require(gates.get("three_Q_representatives_exact") is True, "36-02 gate lost")
    require(gates.get("physical_open_push_and_boundary_complete") is True, "36-03 gate not promoted")
    for key, value in gates.items():
        if key not in {"source_authority_lock_complete", "three_Q_representatives_exact", "physical_open_push_and_boundary_complete"}:
            require(value is False, f"later gate prematurely promoted: {key}")

    current = state.get("current", {})
    require(current.get("unit") == "36-04", "current unit is not 36-04")
    require(current.get("next_exact_leaf") == "36-04_EXPLICIT_H_TORSOR_AND_LIFT_CLASS", "36-04 successor moved")
    require("36-04" not in state.get("completed_units", {}), "36-04 started inside 36-03 promotion")
    require(all(v is False for v in state.get("claims", {}).values()), "Stage36 higher claim leaked")

    print("PASS STAGE36_36_03_AUDITED_SUCCESSOR_REPLAY")
    print(f"hostile_audit_review={AUDIT_REVIEW}; audited_head={AUDITED_HEAD}")
    print(f"audited_certificate_blob={AUDITED_CERT_BLOB}")
    print("physical_open_push_and_boundary_complete=true; 36-04 ready but not started")
    print("no finite-twist/receiver/endpoint/perfect-cuboid credit")


if __name__ == "__main__":
    main()
