#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, pathlib

M = 140
MAGIC = b"S32D16C1"
SCHEMA = "STAGE32_18E_D16_EXACT_SYMMETRY_SHARDED_TRAVERSAL_CERT_V1"
EXEC_KEYS = [
    "nodes", "coordinate_trials", "exact_prune_checks", "exact_constraint_prunes",
    "exact_symmetry_prune_checks", "exact_symmetry_prunes", "exact_norm_leaves",
    "leaf_cap_survivors_after_branch_symmetry", "precanonical_survivors",
    "canonical_rejects"
]


def read_records(path: pathlib.Path):
    raw = path.read_bytes()
    if raw[:8] != MAGIC:
        raise RuntimeError(f"bad dump magic: {path}")
    body = raw[8:]
    size = M + 1
    if len(body) % size:
        raise RuntimeError(f"truncated dump: {path}")
    return [body[i:i + size] for i in range(0, len(body), size)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=pathlib.Path, required=True)
    ap.add_argument("--output-dump", type=pathlib.Path, required=True)
    ap.add_argument("--certificate", type=pathlib.Path, required=True)
    args = ap.parse_args()

    parent_count, parent_id = 256, 26
    rescue_count = 1024
    rescue_ids = [26, 282, 538, 794]
    expected = sorted(r for r in range(rescue_count) if r % parent_count == parent_id)
    if rescue_ids != expected:
        raise RuntimeError((rescue_ids, expected))

    records = []
    hist = {}
    exec_totals = {k: 0 for k in EXEC_KEYS}
    owned_prefixes = 0
    split_seen_values = []
    lock = None

    for sid in rescue_ids:
        jp = args.input / f"d16-b12-exact-subshard-{sid}-of1024.json"
        bp = args.input / f"d16-b12-exact-subshard-{sid}-of1024.bin"
        if not jp.exists() or not bp.exists():
            raise RuntimeError(f"missing rescue child {sid}")
        d = json.loads(jp.read_text())
        if d.get("schema") != SCHEMA or d.get("status") != "COMPLETE" or d.get("bound") != 12:
            raise RuntimeError(f"bad status/schema {sid}")
        if d.get("shard_id") != sid or d.get("shard_count") != rescue_count:
            raise RuntimeError(f"bad shard metadata {sid}")
        if d.get("split_coordinate") != 54 or d.get("dfs_symmetry_breaker_count") != 256:
            raise RuntimeError(f"bad split/breaker metadata {sid}")
        if d.get("aut_group_order") != 1536:
            raise RuntimeError(f"bad Aut order {sid}")
        if d.get("TRAVERSAL_COMPLETENESS_CERTIFICATE") is not True:
            raise RuntimeError(f"missing traversal certificate {sid}")
        if d.get("all_symmetry_branch_rejections_exact_rational_cauchy_schwarz") is not True:
            raise RuntimeError(f"missing exact symmetry certificate {sid}")
        here = (
            d.get("stable_aut_content_sha256"),
            d.get("prepared_input_sha256"),
            d.get("canonical_bundle_sha256"),
        )
        if lock is None:
            lock = here
        if here != lock:
            raise RuntimeError(f"source lock mismatch {sid}")

        split_seen_values.append(int(d.get("split_prefixes_seen", -1)))
        owned_prefixes += int(d.get("owned_prefixes", 0))
        for k in EXEC_KEYS:
            exec_totals[k] += int(d.get(k, 0))
        for k, v in d.get("canonical_norm_histogram", {}).items():
            hist[str(k)] = hist.get(str(k), 0) + int(v)

        rs = read_records(bp)
        if len(rs) != int(d.get("canonical_survivors_including_zero", -1)):
            raise RuntimeError(f"record count mismatch {sid}")
        records.extend(rs)

    if len(set(split_seen_values)) != 1:
        raise RuntimeError(f"pre-split traversal mismatch: {split_seen_values}")
    if len(records) != len(set(records)):
        raise RuntimeError("duplicate canonical records across deep-rescue children")
    records = sorted(records)
    record_hist = {}
    for r in records:
        record_hist[str(r[0])] = record_hist.get(str(r[0]), 0) + 1
    if record_hist != hist:
        raise RuntimeError((record_hist, hist))

    args.output_dump.parent.mkdir(parents=True, exist_ok=True)
    args.output_dump.write_bytes(MAGIC + b"".join(records))
    dump_sha = hashlib.sha256(args.output_dump.read_bytes()).hexdigest()
    stable_aut, prepared_input, bundle_sha = lock
    cert = {
        "schema": "STAGE32_18G_D16_B12_DEEP_RESCUE_CERTIFICATE_V1",
        "verdict": "PASS_EXACT_DEEP_RESCUE_26_OF256_PENDING_PARENT_SYNTHESIS_AND_HOSTILE_AUDIT",
        "bound": 12,
        "logical_parent_shard_count": parent_count,
        "logical_parent_shard_id": parent_id,
        "rescue_shard_count": rescue_count,
        "rescue_subshard_ids": rescue_ids,
        "residue_partition_exact": True,
        "residue_equivalence": "h%256==26 iff h%1024 in [26,282,538,794]",
        "stable_aut_content_sha256": stable_aut,
        "prepared_input_sha256": prepared_input,
        "canonical_bundle_sha256": bundle_sha,
        "aut_group_order": 1536,
        "dfs_symmetry_breaker_count": 256,
        "split_coordinate": 54,
        "logical_parent_split_prefixes_seen": split_seen_values[0],
        "logical_parent_owned_prefixes": owned_prefixes,
        "canonical_survivors_including_zero": len(records),
        "canonical_nonzero_survivors": len(records) - hist.get("0", 0),
        "canonical_norm_histogram": hist,
        "canonical_dump_sha256": dump_sha,
        "TRAVERSAL_COMPLETENESS_CERTIFICATE": True,
        "all_symmetry_branch_rejections_exact_rational_cauchy_schwarz": True,
        "telemetry_semantics": "rescue_execution_totals sum four real 1024-way runs and therefore repeat all work above split coordinate 54; they are execution-work counters, not reconstructed 256-way parent counters",
        "rescue_execution_totals": exec_totals,
        "GLOBAL_B12_AGGREGATION_COMPLETE": False,
        "D16_B12_NUMERICAL_CREDIT": False,
        "AUDIT_STATUS": "PENDING",
        "FULL_D16_G0_ROW_COMPLETE": False,
        "THEOREM_CREDIT": False,
        "RECEIVER_CREDIT": False
    }
    args.certificate.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(json.dumps(cert, sort_keys=True))


if __name__ == "__main__":
    main()
