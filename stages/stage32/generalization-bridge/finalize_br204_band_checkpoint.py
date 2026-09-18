#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def load_combiner(path: str):
    spec = importlib.util.spec_from_file_location("br204_combiner", path)
    req(spec is not None and spec.loader is not None, "cannot load combiner")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--combiner", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--b", type=int, required=True)
    ap.add_argument("--band-lo", type=int, required=True)
    ap.add_argument("--band-hi", type=int, required=True)
    ap.add_argument("--worker-blob", required=True)
    a = ap.parse_args()

    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    status_path = out / "STATUS.json"
    final = out / f"br204-u-b{a.b}-d{a.band_lo}-{a.band_hi}.tsv.gz"
    partial = out / f"br204-partial-b{a.b}-d{a.band_lo}-{a.band_hi}.tsv.gz"

    if status_path.exists():
        s = json.loads(status_path.read_text())
    else:
        if final.exists():
            s = {
                "schema": "STAGE32_BR204_RESUMABLE_BAND_STATUS_V3_DURABLE_LOCAL_ROLLUP",
                "b": a.b,
                "band": [a.band_lo, a.band_hi],
                "complete": True,
                "stop_reason": "INTERRUPTED_AFTER_COMPLETE_ROLLUP",
                "failed_d": None,
                "rollup_payload": final.name,
                "rollup_payload_gzip_bytes": final.stat().st_size,
                "checkpoint_after_each_completed_d": True,
            }
        else:
            cmd = [
                sys.executable, a.combiner, "inspect-partial",
                "--input-dir", str(out),
                "--b", str(a.b), "--band-lo", str(a.band_lo), "--band-hi", str(a.band_hi),
                "--worker-blob", a.worker_blob,
            ]
            cp = subprocess.run(cmd, text=True, capture_output=True)
            req(cp.returncode == 0, cp.stderr.strip())
            info = json.loads(cp.stdout.strip().splitlines()[-1])
            if info.get("found"):
                st = info["state"]
                req(partial.exists(), "validated partial state missing local payload")
                s = {
                    "schema": "STAGE32_BR204_RESUMABLE_BAND_STATUS_V3_DURABLE_LOCAL_ROLLUP",
                    "b": a.b,
                    "band": [a.band_lo, a.band_hi],
                    "expected_d": sorted(list(map(int, st["completed_d"])) + list(map(int, st["missing_d"]))),
                    "recovered_d": [],
                    "completed_d": list(map(int, st["completed_d"])),
                    "missing_d": list(map(int, st["missing_d"])),
                    "complete": False,
                    "stop_reason": "INTERRUPTED_AFTER_LAST_D_CHECKPOINT",
                    "failed_d": None,
                    "worker_blob": a.worker_blob,
                    "rollup_payload": partial.name,
                    "rollup_payload_gzip_bytes": partial.stat().st_size,
                    "checkpoint_after_each_completed_d": True,
                }
            else:
                s = {
                    "schema": "STAGE32_BR204_RESUMABLE_BAND_STATUS_V3_DURABLE_LOCAL_ROLLUP",
                    "b": a.b,
                    "band": [a.band_lo, a.band_hi],
                    "completed_d": [],
                    "complete": False,
                    "stop_reason": "INTERRUPTED_WITHOUT_DURABLE_D_CHECKPOINT",
                    "failed_d": None,
                    "worker_blob": a.worker_blob,
                    "rollup_payload": None,
                    "rollup_payload_gzip_bytes": 0,
                    "checkpoint_after_each_completed_d": True,
                }
        status_path.write_text(json.dumps(s, sort_keys=True, indent=2) + "\n")

    req(s.get("b") == a.b and s.get("band") == [a.band_lo, a.band_hi], "status identity drift")
    req(s.get("checkpoint_after_each_completed_d") is True, "checkpoint contract drift")

    # Revalidate the actual persisted payload before declaring it upload-eligible.
    combiner = load_combiner(a.combiner)
    complete = bool(s.get("complete"))
    if complete:
        req(final.exists(), "complete status missing final payload")
        parsed = combiner.parse_payload(final, a.worker_blob)
        req(
            parsed["b"] == a.b and parsed["d_lo"] == a.band_lo and parsed["d_hi"] == a.band_hi,
            "complete payload identity drift",
        )
        req(not partial.exists(), "complete checkpoint retains partial payload")
    else:
        if partial.exists():
            cmd = [
                sys.executable, a.combiner, "inspect-partial",
                "--input-dir", str(out),
                "--b", str(a.b), "--band-lo", str(a.band_lo), "--band-hi", str(a.band_hi),
                "--worker-blob", a.worker_blob,
            ]
            cp = subprocess.run(cmd, text=True, capture_output=True)
            req(cp.returncode == 0, cp.stderr.strip())
            info = json.loads(cp.stdout.strip().splitlines()[-1])
            req(info.get("found") is True, "partial payload failed validation")
            st = info["state"]
            if "completed_d" in s:
                req(list(map(int, s["completed_d"])) == list(map(int, st["completed_d"])), "status/partial completed_d drift")
            if "missing_d" in s:
                req(list(map(int, s["missing_d"])) == list(map(int, st["missing_d"])), "status/partial missing_d drift")
        else:
            req(int(s.get("rollup_payload_gzip_bytes", 0)) == 0, "status claims missing partial payload")

    payload_bytes = partial.stat().st_size if partial.exists() else 0
    final_bytes = final.stat().st_size if final.exists() else 0
    req(payload_bytes <= 900000, "recovery slot too large")
    req(final_bytes <= 900000, "final band gzip too large")

    # Only complete payloads or a validated nonempty partial are recovery-upload safe.
    upload_safe = complete or partial.exists()
    result = {
        "complete": complete,
        "upload_safe": upload_safe,
        "stop_reason": s.get("stop_reason"),
        "payload_bytes": payload_bytes,
        "final_bytes": final_bytes,
        "has_partial": partial.exists(),
        "status": str(status_path),
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
