#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import resource
import sys
import tempfile
import time
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHARD = HERE / "build_exact_t_joint_histogram_shard.py"
SHARD_BLOB = "25284ea56c0746912318ce3c0d0e75d50cf60458"

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def load_shard():
    req(SHARD.is_file() and blob(SHARD) == SHARD_BLOB, "shard builder blob drift")
    spec = importlib.util.spec_from_file_location("hpadj23_shard_locked_for_measurement", SHARD)
    req(spec is not None and spec.loader is not None, "cannot load shard builder")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--H", type=int, required=True)
    ap.add_argument("--b-start", type=int, required=True)
    ap.add_argument("--b-stop", type=int, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--raw-output", type=Path)
    ap.add_argument("--exact-head", default=os.environ.get("GITHUB_SHA"))
    args = ap.parse_args()

    req(args.H == 32 and args.b_start == 0 and args.b_stop == 11,
        "measurement target must remain H=32,b=0..11")
    if args.exact_head is not None:
        req(len(args.exact_head) == 40 and all(ch in "0123456789abcdef" for ch in args.exact_head),
            "exact-head format drift")

    shard = load_shard()
    raw_path = args.raw_output
    temp = None
    if raw_path is None:
        temp = tempfile.TemporaryDirectory()
        raw_path = Path(temp.name) / "hpadj23-measurement.jsonl"
    raw_path.parent.mkdir(parents=True, exist_ok=True)

    wall0 = time.perf_counter()
    cpu0 = time.process_time()
    hist = shard.build_joint_bc_t_shard(args.H, args.b_start, args.b_stop)
    build_wall = time.perf_counter() - wall0
    build_cpu = time.process_time() - cpu0

    ser_wall0 = time.perf_counter()
    metrics = shard.stream_metrics(hist, raw_path)
    ser_wall = time.perf_counter() - ser_wall0
    raw = raw_path.read_bytes()
    compressed = zlib.compress(raw, level=9)

    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    out = {
        "schema": "STAGE32EX5_HPADJ23_SCALEOUT_MEASUREMENT_RESULT_V1",
        "route_id": "HPADJ-23_ex5",
        "status": "REPRESENTATIVE_SHARD_MEASUREMENT_ONLY_ZERO_MATHEMATICAL_CREDIT",
        "exact_head": args.exact_head,
        "target": {"H": args.H, "b_start": args.b_start, "b_stop": args.b_stop},
        "source_locks": {"shard_builder_blob_sha1": SHARD_BLOB},
        "metrics": {
            **metrics,
            "zlib_level9_bytes": len(compressed),
            "build_wall_seconds": build_wall,
            "build_cpu_seconds": build_cpu,
            "serialization_wall_seconds": ser_wall,
            "peak_rss_kib": int(rss),
        },
        "semantics": {
            "representative_measurement_only": True,
            "not_a_full178_production_result": True,
            "not_a_consumer_numeric_replay": True,
            "storage_runtime_concurrency_planning_only": True,
        },
        "credit": {
            "stage32_main_credit": False,
            "full178_producer_complete": False,
            "effectivity_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canonical(out)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n")
    print(json.dumps(out, sort_keys=True))
    if temp is not None:
        temp.cleanup()

if __name__ == "__main__":
    main()
