#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "stages/stage36/MAIN-STATE.json"
CERT_PATH = ROOT / "stages/stage36/36-01/source-authority-certificate.json"
CERT_BASE = "5ed32fa53bdecb735f461d7c27e85851d9ad8c21"
AUDITED_MERGE = "8c59c81bcf0bcd442705cfb7a3db297253b34679"
SOURCES = {
    "stage29_active_kernel_ledger": ("stages/stage29/29-16/active-kernel-ledger.json", "5d6d4c7709b57064aea5dc0ece672c5170c39550"),
    "stage29_endpoint_hub_graph": ("stages/stage29/29-06/endpoint-hub-graph.json", "7ea59474767f81fbaa4837c8cbc94b535560617b"),
    "stage29_campedelli_route_contract": ("stages/stage29/29-02hb/route-contract.json", "75045d8f15786836e8a7383fc07ef95161fa86e7"),
    "stage29_campedelli_arithmetic_routing": ("stages/stage29/29-02hb/arithmetic-routing.md", "ff83f652e2c9e95b0670c0964b9c8cf0fbccd696"),
    "stage29_campedelli_quotient_adapter": ("stages/stage29/29-02hb/campedelli-quotient-adapter.md", "5f959d60106243bb31df06a3961ab04182d78fc7"),
    "stage29_campedelli_source_lock": ("stages/stage29/29-02hb/source-lock.md", "713f22bb1347b8c6d5f8b32bfc2a24b3ce8b2e5d"),
}
ARSENAL = {
    "router": ("docs/arsenal/index.json", "aa45d19c2f1d8970c7f142bf744c5c17e75abe5a"),
    "S30-WF02": ("docs/arsenal/cards/workflows/S30-WF02.md", "38e4625155eb079bbe3d50d663c6256559319886"),
    "S30-WF03": ("docs/arsenal/cards/workflows/S30-WF03.md", "12740198aba19ade18302819f8e890dbda4eb701"),
}


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def main() -> None:
    state = json.loads(STATE_PATH.read_text())
    cert = json.loads(CERT_PATH.read_text())

    expected = {k: {"path": p, "blob_sha": s} for k, (p, s) in SOURCES.items()}
    require(cert.get("immutable_stage29_sources") == expected, "36-01 certificate source locks moved")
    require(state.get("source_locks") == expected, "MAIN-STATE source locks moved")
    for key, (rel, sha) in SOURCES.items():
        require(blob_sha(ROOT / rel) == sha, f"36-01 source blob drift: {key}")

    aw = cert.get("arsenal_workflow_locks", {})
    for key, (rel, sha) in ARSENAL.items():
        require(aw.get(key, {}).get("path") == rel, f"36-01 Arsenal path moved: {key}")
        require(aw.get(key, {}).get("blob_sha") == sha, f"36-01 Arsenal lock moved: {key}")
        require(blob_sha(ROOT / rel) == sha, f"36-01 Arsenal blob drift: {key}")

    require(cert.get("schema") == "STAGE36_36_01_SOURCE_AUTHORITY_LOCK_V1", "36-01 certificate schema moved")
    require(cert.get("base_main_sha") == CERT_BASE, "36-01 certificate historical base moved")
    require(cert.get("pass_condition") == {"STAGE36_SOURCE_FRONTIER_LOCKED": True, "NEW_THEOREM_CREDIT": False}, "36-01 pass condition moved")
    require(all(v is False for v in cert.get("claims", {}).values()), "36-01 certificate leaked higher credit")

    unit = state.get("completed_units", {}).get("36-01", {})
    require(unit.get("status") == "AUDITED_PASS", "36-01 not promoted as audited")
    require(unit.get("promotion_status") == "AUDITED", "36-01 promotion status moved")
    require(unit.get("hostile_audit_review") == 5112705173, "36-01 hostile audit review moved")
    require(unit.get("audited_head") == "e2f6c5a2f34d76c1f17f90983a4e7fea62816621", "36-01 audited head moved")
    require(unit.get("exact_head_ci_run") == 33866017108, "36-01 CI run moved")
    require(unit.get("exact_head_ci_job") == 101000945515, "36-01 CI job moved")
    require(unit.get("merged_main_sha") == AUDITED_MERGE, "36-01 merged authority moved")
    require(unit.get("STAGE36_SOURCE_FRONTIER_LOCKED") is True, "36-01 source frontier credit lost")
    require(unit.get("NEW_THEOREM_CREDIT") is False, "36-01 theorem credit leaked")
    require(state.get("promotion_gates", {}).get("source_authority_lock_complete") is True, "36-01 promotion gate lost")
    require(all(v is False for v in state.get("claims", {}).values()), "Stage36 higher claim leaked after 36-01")

    print("PASS STAGE36_36_01_AUDITED_SUCCESSOR_REPLAY")
    print("hostile_audit_review=5112705173; audited_head=e2f6c5a2f34d76c1f17f90983a4e7fea62816621")
    print("source_authority_lock_complete=true; no theorem/receiver/endpoint credit")


if __name__ == "__main__":
    main()
