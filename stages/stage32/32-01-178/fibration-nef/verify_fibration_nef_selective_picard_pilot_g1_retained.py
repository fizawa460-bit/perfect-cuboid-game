#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECKPOINT = HERE / "SELECTIVE-PICARD-PILOT-G1-RETAINED.json"
RECEIPT = HERE / "SELECTIVE-PICARD-PILOT-G1-U0000-RECEIPT.json"
WORKER = HERE / "run_fibration_nef_selective_picard_workunit.py"
WORKUNIT = HERE / "verify_fibration_nef_selective_picard_workunit_preflight.py"
PLAN = HERE / "verify_fibration_nef_selective_workunit_plan_certificate.py"
SELECTIVE = HERE / "verify_fibration_nef_selective_weighted_survivor_preflight.py"

EXPECTED_BLOBS = {
    WORKER: "3bbc4ba84f7ba5bf7188929d56c4a273ca0532f5",
    WORKUNIT: "0ee1c21df1b765e91937587903e873f83ec06729",
    PLAN: "37745be7877f32a1804a350d8ebbeedc893d4a5b",
    SELECTIVE: "9e5b662d1e26a20afdf8621b131ffbac60b31b07",
}
EXPECTED_RECEIPT_SHA256 = "ddd6e644f1ec9acf0e467d7f678b7fb0a6325cf7cd0c6040169e0b21b86dd328"


def req(value, message):
    if not value:
        raise SystemExit("FAIL: " + message)


def git_blob(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def stream_sha(records):
    digest = hashlib.sha256()
    for record in records:
        digest.update(json.dumps(record, sort_keys=True, separators=(",", ":")).encode())
        digest.update(b"\n")
    return digest.hexdigest()


def main():
    for path, expected in EXPECTED_BLOBS.items():
        req(path.is_file() and git_blob(path) == expected, f"source drift: {path.name}")

    raw = RECEIPT.read_bytes()
    req(hashlib.sha256(raw).hexdigest() == EXPECTED_RECEIPT_SHA256, "receipt file digest drift")
    receipt = json.loads(raw)
    req(receipt["schema"] == "STAGE32_32_01_178_SELECTIVE_PICARD_WORKUNIT_RECEIPT_V1", "receipt schema")
    req(receipt["role"] == "COMPLETE_EXACT_WORKUNIT_RECEIPT__NO_MAIN_CREDIT", "receipt role")

    identity = receipt["workunit_identity"]
    req(identity == {
        "start_index": 0,
        "static_key_count": 256,
        "static_key_stream_sha256": "5f6dd5f2196ed46f853d6459b868d91d14ce93bb42f3c16de8726e3633ea027c",
        "stop_index_exclusive": 256,
        "workunit_id": "g1-d192-e032-x4-0000-u0000",
        "x4": 0,
    }, "workunit identity")

    locks = receipt["source_locks"]
    req(locks["worker_blob_sha1"] == EXPECTED_BLOBS[WORKER], "worker lock")
    req(locks["workunit_preflight_blob_sha1"] == EXPECTED_BLOBS[WORKUNIT], "workunit lock")
    req(locks["workunit_plan_certificate_producer_blob_sha1"] == EXPECTED_BLOBS[PLAN], "plan lock")
    req(locks["selective_weighted_survivor_blob_sha1"] == EXPECTED_BLOBS[SELECTIVE], "selective lock")

    semantics = receipt["execution_semantics"]
    req(semantics["completed_key_count"] == 256 and semantics["unknown_count"] == 0, "completion semantics")
    req(semantics["atomic_receipt_written_only_after_complete_unit"] is True, "atomic receipt flag")
    rows = receipt["result"]["key_evidence_rows"]
    req(len(rows) == 256, "evidence row coverage")
    req(stream_sha(rows) == receipt["result"]["key_evidence_stream_sha256"], "evidence stream digest")
    envelope = sum(int(row["depth2_envelope_weighted_mass"]) for row in rows)
    exact = sum(int(row["exact_picard_weighted_mass"]) for row in rows)
    req(all(int(row["exact_picard_weighted_mass"]) <= int(row["depth2_envelope_weighted_mass"]) for row in rows), "per-key mass monotonicity")
    result = receipt["result"]
    req(str(envelope) == result["depth2_envelope_weighted_mass"] == "3007", "envelope aggregate")
    req(str(exact) == result["exact_picard_weighted_mass"] == "3007", "exact aggregate")
    req(str(envelope - exact) == result["exact_picard_tightening"] == "0", "tightening aggregate")

    claimed = receipt["canonical_sha256_without_this_field"]
    body = dict(receipt)
    body.pop("canonical_sha256_without_this_field")
    req(csha(body) == claimed == "5da442edd1eeeeb4a580923934739d364bc370c4f630026414e1f7b84afcd8da", "receipt canonical digest")
    firewalls = receipt["firewalls"]
    req(firewalls["main_credit_changed"] is False, "MAIN credit firewall")
    req(firewalls["theorem_credit_changed"] is False, "theorem credit firewall")
    req(firewalls["endpoint_credit_changed"] is False, "endpoint credit firewall")

    checkpoint = json.loads(CHECKPOINT.read_text())
    checkpoint_claimed = checkpoint["canonical_sha256_without_this_field"]
    checkpoint_body = dict(checkpoint)
    checkpoint_body.pop("canonical_sha256_without_this_field")
    req(csha(checkpoint_body) == checkpoint_claimed, "checkpoint canonical digest")
    req(checkpoint["receipt"]["canonical_sha256_without_this_field"] == claimed, "checkpoint receipt canonical")
    req(checkpoint["verification"]["result"] == "PASS", "retained resume verification")
    req(checkpoint["verification"]["rejected_receipt_count"] == 0, "rejected receipt count")
    req(checkpoint["authorization"]["production_wave_armed"] is False, "production wave unexpectedly armed")
    req(checkpoint["firewalls"]["mathematical_credit_granted"] is False, "mathematical credit firewall")

    print("PASS: selective Picard generation-1 pilot receipt is exact and complete for 256/256 static keys")
    print("PASS: depth2 envelope mass=3007 exact Picard mass=3007 tightening=0 UNKNOWN=0")
    print("PASS: source locks, evidence stream, receipt/checkpoint canonicals, and zero-credit firewalls")
    print("PASS: production wave remains unarmed; hostile audit is required before any credit")


if __name__ == "__main__":
    main()
