#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

PACKET_BLOB = "f57a138e24ee5a17eb23ce186b23a468ef717c73"
EXPECTED_CURRENT = 179119009547804181594
EXPECTED_IMPROVEMENT = 1312541087830960386
EXPECTED_CANDIDATE = 177806468459973221208


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_locked_json(path: Path, blob: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}: {path}")
    req(git_blob(path) == blob, f"{label} blob drift")
    return json.loads(path.read_text())


def check_blob(path: Path, blob: str, label: str) -> None:
    req(path.is_file(), f"missing {label}: {path}")
    req(git_blob(path) == blob, f"{label} blob drift")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-root", type=Path, required=True)
    args = ap.parse_args()

    here = Path(__file__).resolve().parent
    packet_path = here / "HPADJ21-KNOWN-STRICT-PROMOTION-PACKET.json"
    packet = load_locked_json(packet_path, PACKET_BLOB, "promotion packet")

    req(packet["schema"] == "STAGE32_MAIN_HPADJ21_KNOWN_STRICT_PROMOTION_PACKET_V1", "packet schema")
    req(packet["status"] == "AUDIT_READY_ZERO_MAIN_CREDIT", "packet status")

    chain = packet["main_chain_blobs"]
    local = {
        "v41_audit_sync_record_blob_sha1": here / "GRF04-V41-HPADJ20-FULL178-AUDIT-SYNC.json",
        "v41_audit_sync_verifier_blob_sha1": here / "verify_grf04_v41_hpadj20_full178_audit_sync.py",
        "known_strict_preflight_record_blob_sha1": here / "HPADJ21-KNOWN-STRICT-SUBSET-MAIN-PREFLIGHT.json",
        "known_strict_preflight_verifier_blob_sha1": here / "verify_hpadj21_known_strict_subset_main_preflight.py",
        "structural_refinement_verifier_blob_sha1": here / "verify_hpadj21_structural_refinement.py",
        "event_compiler_verifier_blob_sha1": here / "verify_hpadj21_event_compiled_capacity_preflight.py",
        "known_strict_independent_replay_blob_sha1": here / "verify_hpadj21_known_strict_independent_replay.py",
    }
    for key, path in local.items():
        check_blob(path, chain[key], key)

    sync = load_locked_json(
        here / "GRF04-V41-HPADJ20-FULL178-AUDIT-SYNC.json",
        chain["v41_audit_sync_record_blob_sha1"],
        "V41 audit sync",
    )
    req(sync["hostile_audit"]["status"] == "PASS", "V40 hostile-audit PASS not retained")
    req(sync["hostile_audit"]["audited_exact_head"] == packet["current_authority"]["hostile_audited_v40_head"],
        "V40 audited head mismatch")
    req(int(sync["sync"]["authoritative_remaining_strata"]) == int(packet["current_authority"]["remaining_strata"]),
        "remaining strata mismatch")
    req(int(sync["sync"]["authoritative_remaining_terminals"]) == EXPECTED_CURRENT, "V41 authority mismatch")
    req(int(packet["current_authority"]["authoritative_remaining_terminals"]) == EXPECTED_CURRENT,
        "packet authority mismatch")

    preflight = load_locked_json(
        here / "HPADJ21-KNOWN-STRICT-SUBSET-MAIN-PREFLIGHT.json",
        chain["known_strict_preflight_record_blob_sha1"],
        "known-strict preflight",
    )
    measured = preflight["measured_strict_subset"]
    low = measured["bounded_low_d_cells"]
    req(len(low) == 6, "low-d measured-cell count")
    low_ids = [str(x["row_id"]) for x in low]
    req(len(set(low_ids)) == 6, "duplicate low-d measured row")
    near_id = str(measured["near_max_row"]["row_id"])
    req(near_id not in set(low_ids), "near-max row overlaps low-d measured rows")
    low_sum = sum(int(x["floor_improvement"]) for x in low)
    near_sum = int(measured["near_max_row"]["floor_improvement_vs_hpadj20"])
    combined = low_sum + near_sum
    req(low_sum == int(packet["measured_replacement"]["bounded_low_d_six_cell_improvement"]), "low-d sum mismatch")
    req(near_sum == int(packet["measured_replacement"]["g1_d190_row_improvement"]), "near-max sum mismatch")
    req(combined == EXPECTED_IMPROVEMENT, "combined measured improvement mismatch")
    req(int(packet["measured_replacement"]["known_measured_improvement_sum"]) == EXPECTED_IMPROVEMENT,
        "packet improvement mismatch")
    req(EXPECTED_CURRENT - EXPECTED_IMPROVEMENT == EXPECTED_CANDIDATE, "candidate arithmetic")
    req(int(packet["measured_replacement"]["candidate_upper_bound"]) == EXPECTED_CANDIDATE, "packet candidate mismatch")
    req(int(preflight["candidate"]["candidate_upper_bound"]) == EXPECTED_CANDIDATE, "preflight candidate mismatch")

    source = packet["retained_hpadj21_source"]
    root = args.source_root.resolve()
    req(root.is_dir(), "missing retained HPADJ21 source root")
    source_paths = {
        "row_worker_blob_sha1": root / "stages/stage32-ex5/hpadj-21_ex5/run_full_hist_row.py",
        "bounded_pilot_blob_sha1": root / "stages/stage32-ex5/hpadj-21_ex5/strictness_pilot_bounded_exact.py",
        "hpadj20_parent_blob_sha1": root / "stages/stage32-ex5/hpadj-20_ex5/derive_two_tier_qa_predomain_picard_lp_bound.py",
    }
    for key, path in source_paths.items():
        check_blob(path, source[key], "retained source " + key)

    semantics = packet["replacement_semantics"]
    req(semantics["same_population"] is True, "same-population firewall")
    req(semantics["same_cell_partition"] is True, "same-cell partition firewall")
    req(semantics["strict_measurements_are_distinct_cells_or_rows"] is True, "distinct replacement firewall")
    req(semantics["cross_route_additive_subtraction"] is False, "cross-route additive subtraction forbidden")
    req(semantics["transition_rule_after_hostile_audit"] == "min(current_authority, candidate_upper_bound)",
        "transition rule")
    req(semantics["exact_rejected_identity_set_claimed"] is False, "exact rejected identity set forbidden")

    for key, value in packet["firewalls"].items():
        req(value is False, f"firewall unexpectedly true: {key}")

    print("PASS: HPADJ21 known-strict promotion packet is source-locked and audit-ready")
    print(f"current_authority={EXPECTED_CURRENT}")
    print(f"known_measured_improvement={EXPECTED_IMPROVEMENT}")
    print(f"zero_credit_candidate={EXPECTED_CANDIDATE}")
    print("replacement_semantics=same_population_same_partition_no_cross_route_additive_subtraction")
    print("ZERO_MAIN_CREDIT")


if __name__ == "__main__":
    main()
