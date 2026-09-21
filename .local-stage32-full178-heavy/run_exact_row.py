#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ctypes
import importlib.util
import json
import os
import platform
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCAL = ROOT / ".local-stage32-full178-heavy"
EXEC_ROOT = LOCAL / "exec-repo"
WORKER_PATH = EXEC_ROOT / "stages/stage32/management/grf04-hpadj22-joint/run_grf04_hpadj22_full178_parent.py"
WORKER_BLOB = "c9fbf71242581f096718ebf0dbc9ac88878c91f1"
SOURCE_ROOT = LOCAL / "source-lf"


def load_worker():
    spec = importlib.util.spec_from_file_location("full178_local_row_worker", WORKER_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.req(module.blob(WORKER_PATH) == WORKER_BLOB, "production worker blob drift")
    return module


def atomic_json(path: Path, doc: dict) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def current_rss_bytes() -> int:
    class ProcessMemoryCounters(ctypes.Structure):
        _fields_ = [("cb", ctypes.c_ulong), ("PageFaultCount", ctypes.c_ulong),
                    ("PeakWorkingSetSize", ctypes.c_size_t), ("WorkingSetSize", ctypes.c_size_t),
                    ("QuotaPeakPagedPoolUsage", ctypes.c_size_t), ("QuotaPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t), ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                    ("PagefileUsage", ctypes.c_size_t), ("PeakPagefileUsage", ctypes.c_size_t)]
    counters = ProcessMemoryCounters()
    counters.cb = ctypes.sizeof(counters)
    handle = ctypes.windll.kernel32.GetCurrentProcess()
    ok = ctypes.windll.psapi.GetProcessMemoryInfo(handle, ctypes.byref(counters), counters.cb)
    return int(counters.WorkingSetSize) if ok else 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--band", type=int, required=True)
    parser.add_argument("--chunk", type=int, required=True)
    parser.add_argument("--window", type=int, required=True)
    parser.add_argument("--row", type=int, required=True)
    args = parser.parse_args()

    worker = load_worker()
    b0, b1 = worker.chunks_for_band(args.band)[args.chunk]
    outdir = LOCAL / "rows" / f"b{args.band}-c{args.chunk}-w{args.window}" / f"row-{args.row:03d}"
    outdir.mkdir(parents=True, exist_ok=True)
    cert_path = outdir / f"row-{args.row:03d}.json"
    profile_path = outdir / "profile.json"

    hd = worker.load_helper()
    direct = hd.load(hd.DIRECT, hd.DIRECT_BLOB, "v46_full178_direct")
    proj = hd.load(hd.PROJECTION, hd.PROJECTION_BLOB, "v46_full178_projection")
    hd._full178_projection = proj
    worker.req(hd.E_VERIFY.is_file() and worker.blob(hd.E_VERIFY) == hd.E_VERIFY_BLOB,
               "e-independence verifier drift")
    old = direct.load_old(SOURCE_ROOT)
    ctx = old.source_context()
    rows = ctx[8]
    row_id, g0, d0 = rows[args.row]
    r0, r1 = ((0, 59), (60, 119), (120, 177))[args.window]
    worker.req(r0 <= args.row <= r1, "row/window mismatch")
    worker.req(int(d0) // 2 >= b0, "row is implicit zero for spatial chunk")

    if cert_path.exists():
        accepted = worker.validate_carry(
            cert_path, worker_blob=WORKER_BLOB, band=args.band, chunk=args.chunk,
            b0=b0, b1=b1, row_index=args.row, row_id=str(row_id), g=int(g0), d=int(d0))
        if accepted is not None:
            print(json.dumps({"status": "VALID_EXISTING_SKIP", "certificate": str(cert_path),
                              "canonical": accepted["canonical_sha256_without_this_field"]}, sort_keys=True))
            return
        raise SystemExit("FAIL: existing certificate rejected by production validate_carry")

    peak_rss = current_rss_bytes()
    stop = threading.Event()

    def monitor() -> None:
        nonlocal peak_rss
        while not stop.wait(1.0):
            peak_rss = max(peak_rss, current_rss_bytes())

    monitor_thread = threading.Thread(target=monitor, daemon=True)
    monitor_thread.start()
    cpu0 = time.process_time()
    wall0 = time.perf_counter()
    try:
        joint0 = time.perf_counter()
        joint = ctx[0].build_joint_bc_shard(old.HMAX, b0, b1)
        joint_seconds = time.perf_counter() - joint0
        interval0 = time.perf_counter()
        shared_intervals = {}
        for b in range(b0, b1 + 1):
            for c in range(old.HMAX + 1):
                qkeys = set()
                jbc = joint[b][c]
                for sbc in range(8):
                    for parity in (0, 1):
                        hist = jbc[sbc][parity]
                        if hist:
                            qkeys.update(int(q) for q, value in hist.items() if int(value))
                shared_intervals[(b, c)] = hd.interval_table(proj, b, c, qkeys) if qkeys else {}
        interval_seconds = time.perf_counter() - interval0
        cert = worker.compute_row(
            hd, old, ctx, joint, shared_intervals, worker_blob=WORKER_BLOB,
            band=args.band, chunk=args.chunk, b0=b0, b1=b1, row_index=args.row)
        atomic_json(cert_path, cert)
        accepted = worker.validate_carry(
            cert_path, worker_blob=WORKER_BLOB, band=args.band, chunk=args.chunk,
            b0=b0, b1=b1, row_index=args.row, row_id=str(row_id), g=int(g0), d=int(d0))
        worker.req(accepted is not None, "production validate_carry rejected generated certificate")
    finally:
        stop.set()
        monitor_thread.join(timeout=2)

    wall_seconds = time.perf_counter() - wall0
    cpu_seconds = time.process_time() - cpu0
    profile = {
        "schema": "STAGE32_MAIN_V46_GRF04_HPADJ22_FULL178_LOCAL_ROW_RUN_V1",
        "status": "EXACT_ROW_CHUNK_COMPLETE_ZERO_CREDIT",
        "target": {"band_position": args.band, "chunk_position": args.chunk,
                   "row_window_position": args.window, "b_chunk": [b0, b1],
                   "row_index": args.row, "row_id": str(row_id), "g": int(g0), "d": int(d0)},
        "source_locks": {"production_worker_blob_sha1": WORKER_BLOB,
                         "hpadj22_source_head": worker.SOURCE_HEAD},
        "result": {"certificate_path": str(cert_path.relative_to(ROOT)),
                   "canonical_sha256": cert["canonical_sha256_without_this_field"],
                   "production_validate_carry": "PASS"},
        "timing_seconds": {"wall": round(wall_seconds, 6), "cpu": round(cpu_seconds, 6),
                           "joint_bc_build": round(joint_seconds, 6),
                           "shared_integer_interval_build": round(interval_seconds, 6),
                           "compute_row_reported": cert["timing_seconds"]["row_total"]},
        "resources": {"max_rss_bytes": peak_rss, "max_rss_mib": round(peak_rss / 1048576, 3),
                      "logical_cpu_count": os.cpu_count(), "python": platform.python_version()},
        "firewalls": {"main_pruning_credit": False, "full178_complete": False,
                      "theorem_credit": False, "effectivity_credit": False,
                      "receiver_credit": False, "route_credit": False,
                      "endpoint_credit": False, "merge_authorized": False},
    }
    atomic_json(profile_path, profile)
    print(json.dumps(profile, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
