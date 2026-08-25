#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, pathlib

M = 140
MAGIC = b"S32D16C1"
STD_SCHEMA = "STAGE32_18E_D16_EXACT_SYMMETRY_SHARDED_TRAVERSAL_CERT_V1"
LOGICAL_SCHEMA = "STAGE32_18I_D16_EXACT_LOGICAL_PARENT_26_OF1024_V1"
EXPECTED_AUT = "7aa6c9be4a91a25549950e1e45c2349146c6ea4cd035ff9133b41e9de3032bc3"
EXPECTED_HPERP = "7cd24466752b21a30b4f523c04892215d5ad0f33d1cc61bc09fa8f6dc815edd3"
EXPECTED_B10_DUMP_SHA = "186085d4824e8752f11fa81c5f538e54fe724268defe288e5c2e004613bb474a"
EXPECTED_B10_COUNT = 1430
EXPECTED_B10_HIST = {"0":1,"2":1,"4":7,"6":28,"8":223,"10":1170}

def read_records(path: pathlib.Path):
    raw = path.read_bytes()
    if raw[:8] != MAGIC:
        raise RuntimeError(f"bad dump magic {path}")
    body = raw[8:]
    size = M + 1
    if len(body) % size:
        raise RuntimeError(f"truncated dump {path}")
    return [body[i:i+size] for i in range(0, len(body), size)]

def validate_std(d: dict, sid: int, count: int):
    if d.get("schema") != STD_SCHEMA or d.get("status") != "COMPLETE" or d.get("bound") != 12:
        raise RuntimeError(f"bad standard shard schema/status {sid}/{count}")
    if (d.get("shard_id"), d.get("shard_count"), d.get("split_coordinate")) != (sid, count, 54):
        raise RuntimeError(f"bad standard shard metadata {sid}/{count}")
    if d.get("stable_aut_content_sha256") != EXPECTED_AUT or d.get("prepared_input_sha256") != EXPECTED_HPERP:
        raise RuntimeError(f"source lock mismatch {sid}/{count}")
    if d.get("aut_group_order") != 1536 or d.get("dfs_symmetry_breaker_count") != 256:
        raise RuntimeError(f"group/breaker mismatch {sid}/{count}")
    if d.get("TRAVERSAL_COMPLETENESS_CERTIFICATE") is not True:
        raise RuntimeError(f"missing traversal certificate {sid}/{count}")
    if d.get("all_symmetry_branch_rejections_exact_rational_cauchy_schwarz") is not True:
        raise RuntimeError(f"missing exact symmetry certificate {sid}/{count}")

def load_std(root: pathlib.Path, sid: int, count: int):
    if count == 64:
        jp = root / f"d16-b12-exact-shard-{sid}.json"
        bp = root / f"d16-b12-exact-shard-{sid}.bin"
    else:
        jp = root / f"d16-b12-exact-subshard-{sid}-of{count}.json"
        bp = root / f"d16-b12-exact-subshard-{sid}-of{count}.bin"
    if not jp.exists() or not bp.exists():
        raise RuntimeError(f"missing standard shard files {sid}/{count}")
    d = json.loads(jp.read_text())
    validate_std(d, sid, count)
    rs = read_records(bp)
    if len(rs) != int(d.get("canonical_survivors_including_zero", -1)):
        raise RuntimeError(f"record count mismatch {sid}/{count}")
    return d, rs

def hist_of(records):
    out = {}
    for r in records:
        out[str(r[0])] = out.get(str(r[0]), 0) + 1
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ordinary", type=pathlib.Path, required=True)
    ap.add_argument("--rescue256", type=pathlib.Path, required=True)
    ap.add_argument("--deep1024", type=pathlib.Path, required=True)
    ap.add_argument("--logical26", type=pathlib.Path, required=True)
    ap.add_argument("--audited-b10-dump", type=pathlib.Path, required=True)
    ap.add_argument("--output-json", type=pathlib.Path, required=True)
    ap.add_argument("--output-dump", type=pathlib.Path, required=True)
    ap.add_argument("--certificate", type=pathlib.Path, required=True)
    args = ap.parse_args()

    bundle = None
    ordinary_records = []
    ordinary_ids = set(range(64)) - {26}
    for sid in sorted(ordinary_ids):
        d, rs = load_std(args.ordinary, sid, 64)
        if bundle is None:
            bundle = d.get("canonical_bundle_sha256")
        if d.get("canonical_bundle_sha256") != bundle:
            raise RuntimeError("ordinary canonical bundle mismatch")
        ordinary_records.extend(rs)
    if len(ordinary_records) != len(set(ordinary_records)):
        raise RuntimeError("duplicate canonical records across ordinary shards")

    rescue_records = []
    for sid in [90,154,218]:
        d, rs = load_std(args.rescue256, sid, 256)
        if d.get("canonical_bundle_sha256") != bundle:
            raise RuntimeError("18F canonical bundle mismatch")
        rescue_records.extend(rs)
    if len(rescue_records) != len(set(rescue_records)):
        raise RuntimeError("duplicate canonical records across 18F children")

    deep_records = []
    for sid in [282,538,794]:
        d, rs = load_std(args.deep1024, sid, 1024)
        if d.get("canonical_bundle_sha256") != bundle:
            raise RuntimeError("18G canonical bundle mismatch")
        deep_records.extend(rs)

    lj = args.logical26 / "d16-b12-exact-subshard-26-of1024.json"
    lb = args.logical26 / "d16-b12-exact-subshard-26-of1024.bin"
    if not lj.exists() or not lb.exists():
        raise RuntimeError("18K logical 26-of1024 files missing")
    ld = json.loads(lj.read_text())
    if ld.get("schema") != LOGICAL_SCHEMA or ld.get("status") != "COMPLETE" or ld.get("bound") != 12:
        raise RuntimeError("bad 18K logical schema/status")
    if (ld.get("shard_id"), ld.get("shard_count"), ld.get("split_coordinate")) != (26,1024,54):
        raise RuntimeError("bad 18K logical residue metadata")
    if ld.get("stable_aut_content_sha256") != EXPECTED_AUT or ld.get("prepared_input_sha256") != EXPECTED_HPERP:
        raise RuntimeError("18K source lock mismatch")
    if ld.get("canonical_bundle_sha256") != bundle:
        raise RuntimeError("18K canonical bundle mismatch")
    if ld.get("aut_group_order") != 1536 or ld.get("dfs_symmetry_breaker_count") != 256:
        raise RuntimeError("18K group/breaker mismatch")
    if ld.get("two_stage_partition_certificate") is not True or ld.get("secondary_partition_complete") is not True:
        raise RuntimeError("18K nested partition certificate missing")
    if ld.get("TRAVERSAL_COMPLETENESS_CERTIFICATE") is not True:
        raise RuntimeError("18K traversal certificate missing")
    if ld.get("all_symmetry_branch_rejections_exact_rational_cauchy_schwarz") is not True:
        raise RuntimeError("18K exact symmetry certificate missing")
    logical26 = read_records(lb)
    if len(logical26) != int(ld.get("canonical_survivors_including_zero", -1)):
        raise RuntimeError("18K logical record count mismatch")
    if hashlib.sha256(lb.read_bytes()).hexdigest() != ld.get("canonical_dump_sha256"):
        raise RuntimeError("18K logical dump SHA mismatch")

    deep_records.extend(logical26)
    if len(deep_records) != len(set(deep_records)):
        raise RuntimeError("duplicate canonical records inside logical 26-of256")
    if sorted(r for r in range(1024) if r % 256 == 26) != [26,282,538,794]:
        raise RuntimeError("256->1024 residue identity failed")
    logical_26_of256 = sorted(deep_records)

    parent26 = list(logical_26_of256) + rescue_records
    if len(parent26) != len(set(parent26)):
        raise RuntimeError("duplicate canonical records inside logical 26-of64")
    if sorted(r for r in range(256) if r % 64 == 26) != [26,90,154,218]:
        raise RuntimeError("64->256 residue identity failed")
    parent26 = sorted(parent26)

    records = ordinary_records + parent26
    if len(records) != len(set(records)):
        raise RuntimeError("duplicate canonical records in global aggregate")
    records = sorted(records)
    hist = hist_of(records)

    audited_raw = args.audited_b10_dump.read_bytes()
    if hashlib.sha256(audited_raw).hexdigest() != EXPECTED_B10_DUMP_SHA:
        raise RuntimeError("audited b10 dump SHA mismatch")
    audited = sorted(read_records(args.audited_b10_dump))
    if len(audited) != EXPECTED_B10_COUNT:
        raise RuntimeError("audited b10 record count mismatch")
    predecessor = sorted(r for r in records if r[0] <= 10)
    if predecessor != audited:
        raise RuntimeError("b12 <=10 predecessor set differs from hostile-audited b10")
    lower_hist = {k:v for k,v in hist.items() if int(k) <= 10}
    if lower_hist != EXPECTED_B10_HIST:
        raise RuntimeError(f"b10 predecessor histogram mismatch {lower_hist}")

    args.output_dump.parent.mkdir(parents=True, exist_ok=True)
    args.output_dump.write_bytes(MAGIC + b"".join(records))
    dump_sha = hashlib.sha256(args.output_dump.read_bytes()).hexdigest()
    zero = hist.get("0", 0)
    summary = {
        "schema": "STAGE32_18L_D16_B12_FINAL_RESCUE_AWARE_AGGREGATE_V1",
        "status": "COMPLETE", "bound": 12, "aut_group_order": 1536,
        "stable_aut_content_sha256": EXPECTED_AUT, "prepared_input_sha256": EXPECTED_HPERP,
        "canonical_bundle_sha256": bundle, "breaker_count": 256, "split_coordinate": 54,
        "canonical_survivors_including_zero": len(records), "canonical_nonzero_survivors": len(records)-zero,
        "canonical_norm_histogram": hist, "new_norm12_canonical_survivors": hist.get("12", 0),
        "canonical_dump_sha256": dump_sha, "ordinary_64way_shard_ids": sorted(ordinary_ids),
        "rescued_parent_64way_shard_id": 26, "rescue_256way_residues": [26,90,154,218],
        "deep_1024way_residues": [26,282,538,794],
        "deep_1024way_residue26_source": "Stage32-18K exact logical parent from 32 coordinate-45 secondaries",
        "deep_1024way_other_sources": "Stage32-18G completed exact children retained from cancelled superseded run",
        "nested_residue_partition_exact": True, "audited_b10_predecessor_set_identical": True,
        "TRAVERSAL_COMPLETENESS_CERTIFICATE": True,
        "telemetry_semantics": "No hypothetical single-run global nodes/trials total is claimed; Stage32-18K nested execution counters include repeated work above its deeper split.",
        "D16_B12_NUMERICAL_CREDIT": False, "D16_B12_NUMERICAL_CREDIT_PENDING_HOSTILE_AUDIT": True,
        "AUDIT_STATUS": "PENDING", "FULL_D16_G0_ROW_COMPLETE": False, "THEOREM_CREDIT": False,
        "RECEIVER_CREDIT": False, "CONTROLLER_MODIFIED": False,
    }
    args.output_json.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    cert = {
        "schema": "STAGE32_18L_D16_B12_FINAL_PRODUCTION_CERTIFICATE_V1",
        "verdict": "PASS_EXACT_FINAL_RESCUE_AWARE_D16_B12_PRODUCTION_PENDING_HOSTILE_AUDIT",
        "bound": 12, "canonical_survivors_including_zero": len(records),
        "canonical_nonzero_survivors": len(records)-zero, "canonical_norm_histogram": hist,
        "new_norm12_canonical_survivors": hist.get("12", 0), "canonical_dump_sha256": dump_sha,
        "nested_residue_partition_exact": True, "audited_b10_predecessor_set_identical": True,
        "TRAVERSAL_COMPLETENESS_CERTIFICATE": True, "D16_B12_NUMERICAL_CREDIT": False,
        "D16_B12_NUMERICAL_CREDIT_PENDING_HOSTILE_AUDIT": True, "AUDIT_STATUS": "PENDING",
        "FULL_D16_G0_ROW_COMPLETE": False, "THEOREM_CREDIT": False, "RECEIVER_CREDIT": False,
        "CONTROLLER_MODIFIED": False,
    }
    args.certificate.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(json.dumps(cert, sort_keys=True))

if __name__ == "__main__":
    main()
