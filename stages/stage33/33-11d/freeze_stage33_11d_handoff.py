#!/usr/bin/env python3
"""Freeze the compact #1449 run-92 carrier handoff used by 33-11d.

This is a one-time import tool.  It accepts only the named frozen artifact and
refuses any carrier/orbit certificate whose canonical digest differs from the
controller locks merged from #1449.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "stage33-11d-source-lock.json"
CARRIER_FILE = "stage33-11-all-generator-strict-transform-carriers.json"
SCOUT_FILE = "stage33-11-carrier-prime-refinement-scout.json"
ORBIT_FILE = "stage33-11-carrier-geometric-orbit-reduction.json"
EXPECTED = {
    CARRIER_FILE: "950e8c51025e171819fb38f2a1939bce7a35395856232f12abcb01a7ec30673b",
    SCOUT_FILE: "b2af551da0817436b2d7ddc299cb0e52f4e27ae491d92813688b43ff451ff4bb",
    ORBIT_FILE: "9666df780b098959665a1607926da5e6d34878f4631e2e7f03539732b5457201",
}


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def file_sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_checked(root, name):
    path = root / name
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if csha(body) != claimed or claimed != EXPECTED[name]:
        raise SystemExit(f"frozen canonical lock mismatch: {name}")
    return obj, file_sha(path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("artifact_directory", type=Path)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    carrier, carrier_file_sha = load_checked(args.artifact_directory, CARRIER_FILE)
    scout, scout_file_sha = load_checked(args.artifact_directory, SCOUT_FILE)
    orbit, orbit_file_sha = load_checked(args.artifact_directory, ORBIT_FILE)

    if carrier["summary"]["working_generator_coverage"] != "14/14":
        raise SystemExit("working-generator coverage moved")
    if len(carrier["global_carrier_inventory"]) != 30:
        raise SystemExit("carrier inventory moved")
    if scout["summary"]["forced_refinement_carrier_count"] != 6:
        raise SystemExit("direct-refinement count moved")
    if orbit["summary"]["unresolved_geometric_orbit_count"] != 8:
        raise SystemExit("geometric representative count moved")

    files = {
        CARRIER_FILE: {
            "canonical_sha256": EXPECTED[CARRIER_FILE],
            "file_sha256": carrier_file_sha,
        },
        SCOUT_FILE: {
            "canonical_sha256": EXPECTED[SCOUT_FILE],
            "file_sha256": scout_file_sha,
        },
        ORBIT_FILE: {
            "canonical_sha256": EXPECTED[ORBIT_FILE],
            "file_sha256": orbit_file_sha,
        },
    }
    direct_records = [
        row for row in scout["records"]
        if row["refinement_scout"]["status"] == "FORCED_BY_FROZEN_QUADRICS"
    ]
    lock = {
        "schema": "STAGE33_11D_FROZEN_PR1449_HANDOFF_V1",
        "stage": "33-11d",
        "source_pr": 1449,
        "source_pr_role": "FROZEN_MAIN_EVIDENCE_HANDOFF_FOR_AUDIT",
        "authoritative_workflow_run": {
            "run_number": 92,
            "run_id": 33213248650,
            "conclusion": "success",
            "head_sha": "532d6047780e89f97813980a43458b1dd3f9b251",
        },
        "artifact": {
            "id": 9702500748,
            "name": "stage33-11-localization-working-evidence",
            "archive_digest": "sha256:8b04640e784c2c4d52b9fbe130635f658affd4461e3bbb1178877738a782cd5b",
            "files": files,
        },
        "surface_model": {
            "base_field": "Q(i)",
            "coordinate_order": ["a1", "a2", "a3", "b1", "b2", "b3", "c"],
            "equations": [
                "a1^2+a2^2-b3^2",
                "a2^2+a3^2-b1^2",
                "a1^2+a3^2-b2^2",
                "a1^2+a2^2+a3^2-c^2",
            ],
        },
        "certified_actions": {
            "cc": "complex conjugation on Q(i) coefficients",
            "swap12": [1, 0, 2, 4, 3, 5, 6],
            "swap13": [2, 1, 0, 5, 4, 3, 6],
        },
        "carrier_inventory": carrier["global_carrier_inventory"],
        "direct_refinement_records": direct_records,
        "geometric_orbits": orbit["orbits"],
        "handoff_summary": {
            "working_generator_coverage": "14/14",
            "carrier_count": 30,
            "direct_refinement_carrier_count": 6,
            "unresolved_original_carrier_count": 24,
            "geometric_orbit_count": 10,
            "unresolved_geometric_representative_count": 8,
            "unresolved_geometric_representative_hashes": orbit["summary"]["prime_refinement_representatives"],
            "exact_connecting_progress": "0/26",
            "hostile_audit_state": "FAIL_REPAIR_REQUIRED",
            "remaining_exact_debt": "FINITE_CARRIER_PRIME_REFINEMENT_ONLY",
        },
        "firewalls": {
            "exact_connecting_columns_promoted": 0,
            "stage33_11_closed_exact": False,
            "stage33_12_released": False,
            "stage33_08_released": False,
            "stage33_07_closed": False,
            "theorem_credit": False,
            "endpoint_credit": False,
        },
    }
    lock["canonical_sha256"] = csha(lock)
    text = json.dumps(lock, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
    else:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            raise SystemExit("source lock differs; rerun with --write only from frozen artifact")
    print("STAGE33_11D_SOURCE_LOCK=PASS")
    print("SOURCE_LOCK_SHA256=" + lock["canonical_sha256"])


if __name__ == "__main__":
    main()
