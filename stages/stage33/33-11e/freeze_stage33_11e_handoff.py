#!/usr/bin/env python3
"""Freeze the audited 33-11d handoff plus #1449 generator carrier vectors."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
D11 = HERE.parent / "33-11d"
OUT = HERE / "stage33-11e-source-lock.json"
CARRIER_NAME = "stage33-11-all-generator-strict-transform-carriers.json"
CARRIER_CANONICAL = "950e8c51025e171819fb38f2a1939bce7a35395856232f12abcb01a7ec30673b"
D11_CERT = "b45da57ac9b04b744dbdc44a69b80cc3acca42c30e62db6351903d6be3aafc4d"
D11_SOURCE = "a7989a2e0bd58371f7eb4692a5f905c55007606d01b6b364f25558823ca52852"


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_checked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical lock mismatch: {path}")
    return obj


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("artifact_directory", type=Path)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    carrier_path = args.artifact_directory / CARRIER_NAME
    carrier = load_checked(carrier_path, CARRIER_CANONICAL)
    d11 = load_checked(D11 / "stage33-11d-prime-refinement-certificate.json", D11_CERT)
    load_checked(D11 / "stage33-11d-source-lock.json", D11_SOURCE)
    if d11["summary"]["actual_height_one_prime_refinement_coverage"] != "30/30":
        raise SystemExit("33-11d prime coverage moved")
    if d11["summary"]["remaining_unresolved_original_carriers"] != 0:
        raise SystemExit("33-11d unresolved set reopened")
    if len(carrier["records"]) != 14 or len(carrier["global_carrier_inventory"]) != 30:
        raise SystemExit("#1449 generator/carrier inventory moved")

    lock = {
        "schema": "STAGE33_11E_AUDITED_HANDOFF_V1",
        "stage": "33-11e",
        "audited_stage33_11d": {
            "pr": 1455,
            "merged_commit": "cd034173",
            "audited_head": "1e5612d92586f157acbd334506e99d2642a409f7",
            "hostile_audit_verdict": "PASS_STAGE33_11D_CARRIER_PRIME_REFINEMENT",
            "repair_required": False,
            "advance_to_33_11e": True,
            "certificate_sha256": D11_CERT,
            "source_lock_sha256": D11_SOURCE,
            "workflow_run": 33216280553,
        },
        "frozen_pr1449_carrier_evidence": {
            "pr": 1449,
            "run": 33213248650,
            "head": "532d6047780e89f97813980a43458b1dd3f9b251",
            "certificate_sha256": CARRIER_CANONICAL,
            "file_sha256": hashlib.sha256(carrier_path.read_bytes()).hexdigest(),
        },
        "coordinate_order": ["a1", "a2", "a3", "b1", "b2", "b3", "c"],
        "carrier_inventory": carrier["global_carrier_inventory"],
        "generator_records": carrier["records"],
        "summary": {
            "working_generators": carrier["generators"],
            "working_generator_count": 14,
            "carrier_count": 30,
            "prime_refinement_coverage": "30/30",
            "exact_connecting_progress_at_entry": "0/26",
        },
        "firewalls": {
            "stage33_11_exact_connecting_columns": 0,
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
    elif not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
        raise SystemExit("recorded 33-11e source lock differs")
    print("STAGE33_11E_AUDITED_SOURCE_LOCK=PASS")
    print("SOURCE_LOCK_SHA256=" + lock["canonical_sha256"])


if __name__ == "__main__":
    main()
