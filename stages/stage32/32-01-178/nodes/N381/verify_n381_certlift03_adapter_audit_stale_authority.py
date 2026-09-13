#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]

EXPECTED_N380_BLOB = "4464d6106d71758bf3e920c3d2963db128e48cf9"
EXPECTED_N380_CANONICAL = "bb6b8c48550c60cc090bf1226ae3ee50c5a66c862398df75edc5505001d3a7de"
EXPECTED_N381_CANONICAL = "e9c8efa33cce2251fe0ac6f35b9b1664af74fe46ccc2fde32ff5cf394030a276"
EXPECTED_PRODUCER_STATE_BLOB = "7622229037045b1e43e9c25864354ac2c1ed77f7"
EXPECTED_SYMBOLIC_AUDIT_BLOB = "5a8083c6dfcf67b052966dbbfdf5c29c1767448f"
EXPECTED_ADAPTER_RECEIPT_BLOB = "994d518394e39e857adaace8cb79989f44a87301"
EXPECTED_V15_MAIN_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
EXPECTED_V22_MAIN_BLOB = "80fb35c79854bfdf775dc5b94c331f5f8a535ced"


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def canonical(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    hdr = f"blob {len(data)}\0".encode()
    return hashlib.sha1(hdr + data).hexdigest()


def check_blob(path: Path, expected: str, label: str) -> None:
    req(path.is_file(), f"missing {label}: {path}")
    req(git_blob_sha1(path) == expected, f"{label} blob drift")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--certlift-root", required=True)
    ap.add_argument("--source-main-v15-root", required=True)
    ap.add_argument("--current-main-v22-root", required=True)
    args = ap.parse_args()

    cert = Path(args.certlift_root)
    v15 = Path(args.source_main_v15_root)
    v22 = Path(args.current_main_v22_root)

    n380_path = HERE.parent / "N380" / "STATE.json"
    n381_path = HERE / "STATE.json"
    check_blob(n380_path, EXPECTED_N380_BLOB, "N380 state")
    n380 = load(n380_path)
    req(canonical(n380) == EXPECTED_N380_CANONICAL, "N380 canonical drift")

    n381 = load(n381_path)
    req(canonical(n381) == EXPECTED_N381_CANONICAL, "N381 canonical drift")
    req(n381["canonical_sha256_without_this_field"] == EXPECTED_N381_CANONICAL, "N381 retained canonical mismatch")
    req(n381["status"] == "CERTLIFT03_ADAPTER_HOSTILE_AUDIT_PASS_BUT_V15_SNAPSHOT_STALE_VS_V22_NO_CREDIT", "N381 status drift")

    producer_state_path = cert / "stages/stage32/cut-cert-lift/STATE.json"
    symbolic_audit_path = cert / "stages/stage32/cert-lift/CERTLIFT-03-HOSTILE-AUDIT-PASS.json"
    adapter_receipt_path = cert / "stages/stage32/cert-lift/CERTLIFT-03-MAIN-CONSUMPTION-ADAPTER-RECEIPT.json"
    check_blob(producer_state_path, EXPECTED_PRODUCER_STATE_BLOB, "producer state")
    check_blob(symbolic_audit_path, EXPECTED_SYMBOLIC_AUDIT_BLOB, "symbolic audit pass")
    check_blob(adapter_receipt_path, EXPECTED_ADAPTER_RECEIPT_BLOB, "adapter receipt")

    ps = load(producer_state_path)
    sa = load(symbolic_audit_path)
    ar = load(adapter_receipt_path)
    req(ps["active_node"] == "CERTLIFT-03_MAIN_CONSUMPTION_ADAPTER_CANDIDATE_PENDING_HOSTILE_AUDIT", "producer active node drift")
    req(ps["certlift_03"]["hostile_audited"] is True, "symbolic hostile audit lost")
    req(ps["certlift_03"]["hostile_audit_review_id"] == 5188640528, "symbolic review drift")
    req(ps["consumption_adapter"]["adapter_hostile_audited"] is False, "reviewed producer state unexpectedly postdates adapter audit")
    req(ps["consumption_adapter"]["candidate_incremental_blocks"] == 1615, "producer candidate block drift")
    req(ps["consumption_adapter"]["candidate_incremental_terminals"] == 182495, "producer candidate terminal drift")

    req(sa["status"] == "HOSTILE_AUDIT_PASS", "symbolic audit artifact drift")
    req(sa["review_id"] == 5188640528, "symbolic audit review id drift")
    req(sa["symbolic_canonical_sha256"] == "2d1fcfe51420ab01f81d353e0d19a2b1eef467a51e321da953b5cf18aa88e764", "symbolic canonical drift")

    req(ar["adapter_exact_head"] == "9215d4f365ee6400c7de9ba169fe670ddde1d067", "adapter evidence head drift")
    req(ar["adapter_blob_sha1"] == "97ece748a7cd30bd718ea87a64405ab592548aa9", "adapter blob drift")
    req(ar["adapter_canonical_sha256"] == "ba5079e4370db0467a40c80646bce90fae5e907993a3614c928fae1a73cb5ebb", "adapter canonical drift")
    req(ar["source_locks"]["current_main_exact_head"] == "4c51b4ea90a84f9a22a90f194c6d8ecadd9f0d1c", "adapter source MAIN drift")
    req(ar["candidate_increment"]["incremental_blocks"] == 1615, "adapter receipt block drift")
    req(ar["candidate_increment"]["incremental_terminals"] == 182495, "adapter receipt terminal drift")
    req(ar["credit"]["adapter_hostile_audited"] is False, "frozen receipt unexpectedly upgraded")
    req(ar["credit"]["main_pruning"] is False and ar["credit"]["main_authority_mutated"] is False, "adapter receipt credit regression")

    v15_state_path = v15 / "stages/stage32/MAIN-STATE.json"
    v22_state_path = v22 / "stages/stage32/MAIN-STATE.json"
    check_blob(v15_state_path, EXPECTED_V15_MAIN_BLOB, "V15 MAIN state")
    check_blob(v22_state_path, EXPECTED_V22_MAIN_BLOB, "V22 MAIN state")
    m15 = load(v15_state_path)
    m22 = load(v22_state_path)

    req(m15["schema"] == "STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED", "V15 schema drift")
    req(m15["canonical_sha256_without_this_field"] == "d61dd73ecf0c0fa6fc1a96ea37f284dac4d5beb65c88bff59d5cc25b87939193", "V15 canonical drift")
    req(m15["current_exact_frontier"]["authoritative_remaining_terminals"] == 47598978285064933757427, "V15 authority drift")

    req(m22["schema"] == "STAGE32_MAIN_COMPACT_STATE_V22_BATCH_CUT193_CUT197_CUT198_CONSUMED", "V22 schema drift")
    req(m22["canonical_sha256_without_this_field"] == "82ca200d81b0ce844b1756dc0c3205eec388a20cae312af5e0f3c55d959d491c", "V22 canonical drift")
    req(m22["current_exact_frontier"]["authoritative_remaining_strata"] == 17128, "V22 strata drift")
    req(m22["current_exact_frontier"]["authoritative_remaining_terminals"] == 47589703313957134804198, "V22 authority drift")
    req(m22["current_exact_frontier"]["full178_numerical_census_complete"] is False, "V22 FULL178 unexpectedly complete")
    for cut in ("cut193", "cut196", "cut197", "cut198"):
        req(m22["current_exact_frontier"][f"{cut}_main_pruning_credit"] is True, f"V22 {cut} consumption drift")
    req(m22["current_exact_frontier"]["n358_main_pruning_credit"] is True, "V22 N358 consumption drift")

    b = n381["consumption_boundary"]
    req(n381["producer"]["adapter_external_review_pass_observed"] is True, "adapter hostile audit observation lost")
    req(n381["producer"]["adapter_hostile_audit_review_id"] == 5188753236, "adapter hostile audit review id drift")
    req(n381["producer"]["adapter_pass_not_yet_promoted_in_reviewed_state"] is True, "producer review/state ordering drift")
    req(n381["current_audited_main"]["source_snapshot_equals_current_audited_authority"] is False, "stale authority guard lost")
    req(n381["current_audited_main"]["source_minus_current_authority_terminals"] == 47598978285064933757427 - 47589703313957134804198, "authority delta arithmetic drift")
    req(b["adapter_increment_consumable_on_v22_now"] is False, "stale adapter accidentally consumable")
    req(b["v22_incremental_overlap_with_post_v15_consumed_sets_proved"] is False, "missing overlap proof upgraded")
    req(b["v22_incremental_candidate_blocks"] is None and b["v22_incremental_candidate_terminals"] is None, "V22 increment invented")
    req(b["main_authority_mutation_allowed"] is False, "MAIN mutation incorrectly authorized")

    req(n381["n101_contract"]["remains_stopped"] is True, "N101 stop lost")
    req(not any(n381["credit"].values()), "N381 credit firewall regression")
    req(not any(n381["anti_loop"].values()), "N381 anti-loop regression")

    print(json.dumps({
        "adapter_hostile_audit_review_id": n381["producer"]["adapter_hostile_audit_review_id"],
        "adapter_source_main": n381["adapter_snapshot"]["source_main_exact_head"],
        "candidate_blocks_on_source_snapshot": n381["adapter_snapshot"]["candidate_incremental_blocks_on_source_snapshot"],
        "candidate_terminals_on_source_snapshot": n381["adapter_snapshot"]["candidate_incremental_terminals_on_source_snapshot"],
        "current_audited_main": n381["current_audited_main"]["exact_head"],
        "current_audited_main_version": n381["current_audited_main"]["version"],
        "full178_complete": n381["credit"]["full178_complete"],
        "main_pruning_credit": n381["credit"]["main_pruning_credit"],
        "n101_reopened_credit": n381["credit"]["n101_reopened_credit"],
        "next_gate": n381["next_gate"],
        "v22_consumable_now": b["adapter_increment_consumable_on_v22_now"],
        "verdict": "PASS_N381_CERTLIFT03_ADAPTER_AUDIT_PASS_STALE_AUTHORITY_REBASE_WAIT_BOUNDARY"
    }, sort_keys=True))


if __name__ == "__main__":
    main()
