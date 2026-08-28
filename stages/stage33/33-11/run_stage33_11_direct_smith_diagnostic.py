#!/usr/bin/env python3
"""Cheap preflight plus live stack diagnostics for the Stage33-11 direct scout.

This does not change the mathematical computation.  It measures the exact
64x64 Picard Gram before the expensive path and asks faulthandler to emit the
current Python stack every two minutes while the direct certificate runs.  A
timeout therefore identifies the active phase instead of producing a blind
cancel.
"""
from __future__ import annotations

import faulthandler
import json
import runpy
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEGACY = HERE.parent / "33-07"
DIRECT = HERE / "certify_stage33_11_direct_smith_naturality.py"
OUT = HERE / "stage33-11-direct-smith-preflight.json"

old = runpy.run_path(str(LEGACY / "picard_base_rows_retained.py"))["load"]()
raw = old["picard_gram_64x64"]
rows = len(raw)
cols = len(raw[0]) if raw else 0
entries = [int(x) for row in raw for x in row]
nonzero = sum(x != 0 for x in entries)
max_abs = max((abs(x) for x in entries), default=0)
max_bits = max_abs.bit_length()
row_nnz = [sum(int(x) != 0 for x in row) for row in raw]
preflight = {
    "status": "PREFLIGHT_ONLY_NOT_A_MATHEMATICAL_RESULT",
    "picard_gram_rows": rows,
    "picard_gram_cols": cols,
    "picard_gram_nonzero_entries": nonzero,
    "picard_gram_density": nonzero / (rows * cols),
    "picard_gram_max_abs_entry": max_abs,
    "picard_gram_max_entry_bits": max_bits,
    "picard_gram_max_row_nnz": max(row_nnz, default=0),
    "picard_gram_source_sha256": old.get("canonical_sha256"),
    "expensive_candidate": "fresh_exact_integer_smith_normal_decomposition_64x64",
    "heartbeat_seconds": 120,
}
OUT.write_text(json.dumps(preflight, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("STAGE33_11_PREFLIGHT=" + json.dumps(preflight, sort_keys=True), flush=True)

if rows != 64 or cols != 64:
    raise SystemExit("preflight Picard Gram shape moved")

faulthandler.enable(file=sys.stderr, all_threads=True)
faulthandler.dump_traceback_later(120, repeat=True, file=sys.stderr)
t0 = time.perf_counter()
print("STAGE33_11_DIRECT_SCOUT_START", flush=True)
try:
    runpy.run_path(str(DIRECT), run_name="__main__")
finally:
    faulthandler.cancel_dump_traceback_later()
    print(f"STAGE33_11_DIRECT_SCOUT_ELAPSED_SECONDS={time.perf_counter() - t0:.3f}", flush=True)
