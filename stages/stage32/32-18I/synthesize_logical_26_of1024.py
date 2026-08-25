#!/usr/bin/env python3
from __future__ import annotations
import argparse
import hashlib
import json
import pathlib

M = 140
MAGIC = b"S32D16C1"
SCHEMA = "STAGE32_18I_D16_EXACT_TWO_STAGE_SHARDED_TRAVERSAL_CERT_V1"
EXEC_KEYS = [
    "nodes", "coordinate_trials", "exact_prune_checks", "exact_constraint_prunes",
    "exact_symmetry_prune_checks", "exact_symmetry_prunes", "exact_norm_leaves",
    "leaf_cap_survivors_after_branch_symmetry", "precanonical_survivors",
    "canonical_rejects", "owned_prefixes",
]


def read_records(path: pathlib.Path):
    raw = path.read_bytes()
    if raw[:8] != MAGIC:
        raise RuntimeError(f"bad dump magic {path}")
    body = raw[8:]
    size = M + 1
    if len(body) % size:
        raise RuntimeError(f"truncated dump {path}")
    return [body[i:i + size] for i in range(0, len(body), size)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=pathlib.Path, required=True)
    ap.add_argument("--output-json", type=pathlib.Path, required=True)
    ap.add_argument("--output-dump", type=pathlib.Path, required=True)
    ap.add_argument("--certificate", type=pathlib.Path, required=True)
    args = ap.parse_args()

    docs = []
    records = []
    hist = {}
    execution = {k: 0 for k in EXEC_KEYS}
    lock = None
    split_seen = set()
    canonical_total = 0
    canonical_nonzero = 0

    for sid in range(32):
        jp = args.input / f"d16-b12-exact-secondary-{sid}-of32.json"
        bp = args.input / f"d16-b12-exact-secondary-{sid}-of32.bin"
        if not jp.exists() or not bp.exists():
            raise RuntimeError(f"missing secondary shard {sid}")
        d = json.loads(jp.read_text())
        if d.get("schema") != SCHEMA or d.get("status") != "COMPLETE" or d.get("bound") != 12:
            raise RuntimeError(f"bad secondary status/schema {sid}")
        if d.get("two_stage_partition") is not True:
            raise RuntimeError(f"missing two-stage flag {sid}")
        if (d.get("primary_split_coordinate"), d.get("primary_shard_id"), d.get("primary_shard_count")) != (54, 26, 1024):
            raise RuntimeError(f"bad primary gate {sid}")
        if (d.get("secondary_split_coordinate"), d.get("secondary_shard_id"), d.get("secondary_shard_count")) != (45, sid, 32):
            raise RuntimeError(f"bad secondary gate {sid}")
        if d.get("aut_group_order") != 1536 or d.get("dfs_symmetry_breaker_count") != 256:
            raise RuntimeError(f"bad group/breakers {sid}")
        if d.get("TRAVERSAL_COMPLETENESS_CERTIFICATE") is not True:
            raise RuntimeError(f"missing traversal certificate {sid}")
        if d.get("all_symmetry_branch_rejections_exact_rational_cauchy_schwarz") is not True:
            raise RuntimeError(f"missing exact symmetry certificate {sid}")
        here = (d.get("stable_aut_content_sha256"), d.get("prepared_input_sha256"), d.get("canonical_bundle_sha256"))
        if lock is None:
            lock = here
        if here != lock:
            raise RuntimeError(f"source lock mismatch {sid}")
        rs = read_records(bp)
        if len(rs) != int(d.get("canonical_survivors_including_zero", 0)):
            raise RuntimeError(f"record count mismatch {sid}")
        docs.append(d)
        records.extend(rs)
        canonical_total += int(d.get("canonical_survivors_including_zero", 0))
        canonical_nonzero += int(d.get("canonical_nonzero_survivors", 0))
        split_seen.add(int(d.get("split_prefixes_seen", -1)))
        for k in EXEC_KEYS:
            execution[k] += int(d.get(k, 0))
        for k, v in d.get("canonical_norm_histogram", {}).items():
            hist[str(k)] = hist.get(str(k), 0) + int(v)

    if len(split_seen) != 1:
        raise RuntimeError(f"secondary split-prefix scan differs across runs: {sorted(split_seen)}")
    if execution["owned_prefixes"] != next(iter(split_seen)):
        raise RuntimeError("secondary owned-prefix union does not cover the common split-prefix scan")
    if len(records) != canonical_total or len(records) != len(set(records)):
        raise RuntimeError("duplicate or missing canonical records across secondary shards")
    record_hist = {}
    for r in records:
        record_hist[str(r[0])] = record_hist.get(str(r[0]), 0) + 1
    if record_hist != hist:
        raise RuntimeError(f"histogram mismatch {record_hist} != {hist}")

    records = sorted(records)
    args.output_dump.parent.mkdir(parents=True, exist_ok=True)
    args.output_dump.write_bytes(MAGIC + b"".join(records))
    dump_sha = hashlib.sha256(args.output_dump.read_bytes()).hexdigest()
    stable_aut, prepared_input, bundle_sha = lock
    logical = {
        "schema": "STAGE32_18I_D16_EXACT_LOGICAL_PARENT_26_OF1024_V1",
        "status": "COMPLETE", "bound": 12, "aut_group_order": 1536,
        "stable_aut_content_sha256": stable_aut,
        "prepared_input_sha256": prepared_input,
        "canonical_bundle_sha256": bundle_sha,
        "dfs_symmetry_breaker_count": 256,
        "shard_id": 26, "shard_count": 1024, "split_coordinate": 54,
        "two_stage_partition_certificate": True,
        "primary_residue": "h54%1024==26",
        "secondary_split_coordinate": 45, "secondary_shard_count": 32,
        "secondary_partition_complete": True,
        "secondary_split_prefixes_seen_per_run": next(iter(split_seen)),
        "canonical_survivors_including_zero": canonical_total,
        "canonical_nonzero_survivors": canonical_nonzero,
        "canonical_norm_histogram": hist,
        "canonical_dump_sha256": dump_sha,
        "TRAVERSAL_COMPLETENESS_CERTIFICATE": True,
        "all_symmetry_branch_rejections_exact_rational_cauchy_schwarz": True,
        "execution_work_counters_not_parent_equivalent": True,
        "secondary_32_run_execution_work_totals": execution,
        "D16_B12_NUMERICAL_CREDIT": False,
        "AUDIT_STATUS": "PENDING", "FULL_D16_G0_ROW_COMPLETE": False,
        "THEOREM_CREDIT": False, "RECEIVER_CREDIT": False,
    }
    args.output_json.write_text(json.dumps(logical, indent=2, sort_keys=True) + "\n")
    cert = {
        "schema": "STAGE32_18I_D16_B12_TWO_STAGE_RESCUE_CERTIFICATE_V1",
        "verdict": "PASS_EXACT_TWO_STAGE_RESCUE_LOGICAL_26_OF1024_PENDING_GLOBAL_INTEGRATION_AND_HOSTILE_AUDIT",
        "primary_residue": "h54%1024==26",
        "secondary_partition": "32 exact FNV64 shards at coordinate 45",
        "canonical_survivors_including_zero": canonical_total,
        "canonical_norm_histogram": hist,
        "canonical_dump_sha256": dump_sha,
        "secondary_partition_complete": True,
        "execution_work_counters_not_parent_equivalent": True,
        "D16_B12_NUMERICAL_CREDIT": False,
        "GLOBAL_B12_AGGREGATION_COMPLETE": False,
        "AUDIT_STATUS": "PENDING", "THEOREM_CREDIT": False, "RECEIVER_CREDIT": False,
    }
    args.certificate.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(json.dumps(cert, sort_keys=True))


if __name__ == "__main__":
    main()
