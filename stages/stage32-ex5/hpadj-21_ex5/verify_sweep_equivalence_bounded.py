#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DIRECT = HERE / "run_full_hist_row.py"
DIRECT_BLOB = "68a3edcf5be71bb75ed97959fcc5f56a2fcecbd7"
SWEEP = HERE / "run_full_hist_row_sweep.py"
TARGET_ROW_IDS = ("g0-d016", "g1-d016")


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, "cannot load " + name)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    req(DIRECT.is_file() and git_blob(DIRECT) == DIRECT_BLOB, "direct worker drift")
    req(SWEEP.is_file(), "missing sweep worker")
    direct = load(DIRECT, "hpadj21_direct_for_equivalence")
    sweep = load(SWEEP, "hpadj21_sweep_for_equivalence")

    p = direct.load_pilot()
    h20 = p.load_parent()
    h19 = h20.load_parent()
    h18 = h19.load_parent()
    h17 = h18.load_parent()
    h16 = h17.load_parent()
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "hpadj15_for_hpadj21_equivalence")
    p14 = p15.load_parent()
    counter = p14.load_counter()
    manifest = counter.load_locked_json(
        p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = counter.manifest_rows(manifest)
    index = {row_id: i for i, (row_id, _, _) in enumerate(rows)}
    req(all(row_id in index for row_id in TARGET_ROW_IDS), "equivalence target row missing")

    checks = []
    for row_id in TARGET_ROW_IDS:
        idx = index[row_id]
        a = direct.compute_row(idx)
        b = sweep.compute_row(idx)
        req(a["row"] == b["row"], f"row identity mismatch {row_id}")
        req(a["profile"] == b["profile"], f"profile mismatch {row_id}")
        req(a["totals"] == b["totals"], f"totals mismatch {row_id}")
        req(a["cell_records"] == b["cell_records"], f"cell record mismatch {row_id}")
        checks.append({
            "row_id": row_id,
            "row_index": idx,
            "d": a["row"]["d"],
            "strict_cells": a["totals"]["strict_cell_count"],
            "floor_improvement": a["totals"]["floor_improvement"],
            "direct_canonical": a["canonical_sha256_without_this_field"],
            "sweep_canonical": b["canonical_sha256_without_this_field"],
        })

    out = {
        "schema": "STAGE32EX5_HPADJ21_SWEEP_DIRECT_BOUNDED_EQUIVALENCE_V1",
        "status": "EXACT_BOUNDED_EQUIVALENCE_PASS",
        "direct_worker_git_blob": DIRECT_BLOB,
        "sweep_worker_git_blob": git_blob(SWEEP),
        "rows": checks,
        "credit": {
            "stage32_main_credit": False,
            "full178_completion_credit": False,
            "merge_authorized": False,
        },
    }
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
