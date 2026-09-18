#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORKER = HERE / "run_full_bband.py"
WORKER_BLOB = "2c998a190baaf5f29b33a91fd9efedbb036cef46"
EXPECTED_HPADJ21 = 157570677819451133507
EXPECTED_HPADJ08_REJECTED = 40886299509963924857401
EXPECTED_ROWS = 178
EXPECTED_BANDS = 8
EXPECTED_CELLS = EXPECTED_ROWS * EXPECTED_BANDS


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_worker():
    req(WORKER.is_file() and git_blob(WORKER) == WORKER_BLOB, "band worker blob drift")
    spec = importlib.util.spec_from_file_location("hpadj22_band_locked_for_aggregate", WORKER)
    req(spec is not None and spec.loader is not None, "cannot load band worker")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def aggregate(root: Path) -> dict:
    w = load_worker()
    ctx = w.source_context()
    dirs = {}
    for marker in sorted(root.rglob("BAND-COMPLETE.json")):
        raw = json.loads(marker.read_text())
        pos = int(raw.get("band_position", -1))
        req(0 <= pos < EXPECTED_BANDS, f"band position out of range {pos}")
        req(pos not in dirs, f"duplicate band artifact {pos}")
        dirs[pos] = marker.parent
    req(set(dirs) == set(range(EXPECTED_BANDS)), f"band coverage drift: {sorted(dirs)}")

    band_markers = {}
    all_rows = {}
    for pos in range(EXPECTED_BANDS):
        marker, rows_data = w.validate_complete_dir(dirs[pos], pos, ctx)
        band_markers[pos] = marker
        all_rows[pos] = rows_data

    pre = reject = post = h21 = h22 = strict = 0
    cell_stream = hashlib.sha256()
    row_stream = hashlib.sha256()
    row_summaries = []
    for idx in range(EXPECTED_ROWS):
        row_h21 = row_h22 = row_reject = row_pre = row_post = row_strict = 0
        row_id = None
        for pos in range(EXPECTED_BANDS):
            d = all_rows[pos][idx]
            t = d["totals"]
            row_id = d["row"]["row_id"] if row_id is None else row_id
            req(d["row"]["row_id"] == row_id, f"row identity mismatch {idx}")
            pre += int(t["pre_mass"]); reject += int(t["rejected_mass"]); post += int(t["post_mass"])
            h21 += int(t["hpadj21_floor"]); h22 += int(t["hpadj22_exact_survivors"])
            strict += int(bool(t["strict"]))
            row_pre += int(t["pre_mass"]); row_reject += int(t["rejected_mass"]); row_post += int(t["post_mass"])
            row_h21 += int(t["hpadj21_floor"]); row_h22 += int(t["hpadj22_exact_survivors"])
            row_strict += int(bool(t["strict"]))
            compact = {
                "band_position": pos,
                "row_index": idx,
                "row_id": row_id,
                "canonical": d["canonical_sha256_without_this_field"],
                "hpadj21_floor": int(t["hpadj21_floor"]),
                "hpadj22_exact": int(t["hpadj22_exact_survivors"]),
                "improvement": int(t["improvement"]),
            }
            cell_stream.update(json.dumps(compact, sort_keys=True, separators=(",", ":")).encode() + b"\n")
        req(row_pre - row_reject == row_post, f"row mass conservation {idx}")
        req(row_h22 <= row_h21, f"row HPADJ22 weakening {idx}")
        summary = {
            "row_index": idx,
            "row_id": row_id,
            "pre_mass": row_pre,
            "rejected_mass": row_reject,
            "post_mass": row_post,
            "hpadj21_floor": row_h21,
            "hpadj22_exact": row_h22,
            "improvement": row_h21 - row_h22,
            "strict_cells": row_strict,
        }
        row_summaries.append(summary)
        row_stream.update(json.dumps(summary, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    req(pre - reject == post, "global mass conservation")
    req(h21 == EXPECTED_HPADJ21, f"audited HPADJ21 FULL178 replay drift {h21}")
    req(reject == EXPECTED_HPADJ08_REJECTED, f"audited HPADJ08 FULL178 rejection replay drift {reject}")
    req(h22 <= h21, "HPADJ22 aggregate weakened HPADJ21")
    req(h22 < h21 and strict > 0, "HPADJ22 FULL178 lacks strict gain")

    band_summaries = []
    for pos in range(EXPECTED_BANDS):
        m = band_markers[pos]
        band_summaries.append({
            "band_position": pos,
            "b_interval": m["b_interval"],
            "canonical": m["canonical_sha256_without_this_field"],
            "row_stream_sha256": m["row_stream_sha256"],
            "hpadj21": int(m["totals"]["hpadj21_cellwise_floor_sum"]),
            "hpadj22": int(m["totals"]["hpadj22_exact_survivor_sum"]),
            "improvement": int(m["totals"]["improvement"]),
        })

    out = {
        "schema": "STAGE32EX5_HPADJ22_FULL178_AGGREGATE_V1",
        "route_id": "HPADJ-22_ex5",
        "status": "EXACT_FULL178_DELETION_CORRELATION_CANDIDATE_HOSTILE_AUDIT_REQUIRED",
        "coverage": {
            "expected_rows": EXPECTED_ROWS,
            "received_rows": EXPECTED_ROWS,
            "expected_bands": EXPECTED_BANDS,
            "received_bands": EXPECTED_BANDS,
            "expected_cells": EXPECTED_CELLS,
            "received_cells": EXPECTED_CELLS,
            "row_gaps": 0,
            "band_gaps": 0,
            "overlaps": 0,
            "cell_certificate_stream_sha256": cell_stream.hexdigest(),
            "row_summary_stream_sha256": row_stream.hexdigest(),
        },
        "source_locks": {
            "band_worker_git_blob": WORKER_BLOB,
            "audited_hpadj21_full178_upper_bound": EXPECTED_HPADJ21,
            "audited_hpadj08_exact_square_rejected_terminals": EXPECTED_HPADJ08_REJECTED,
        },
        "totals": {
            "pre_mass": pre,
            "rejected_mass": reject,
            "post_mass": post,
            "hpadj21_cellwise_floor_sum": h21,
            "hpadj22_exact_survivor_sum": h22,
            "strict_cell_count": strict,
            "improvement_vs_hpadj21": h21 - h22,
        },
        "composition": {
            "rule": "DIRECT_SAME_POPULATION_REFINEMENT__EXACT_HPADJ08_DELETION_CORRELATION__NO_ADDITIVE_SUBTRACTION",
            "same_pre_domain_population_as_hpadj21": True,
            "audited_hpadj21_full178_reproduced_exactly": True,
            "audited_hpadj08_rejected_mass_reproduced_exactly": True,
            "exact_joint_qA_qBC_picard_parity_used": True,
            "statistical_independence_assumed": False,
            "main_consumption_performed": False,
        },
        "bands": band_summaries,
        "rows": row_summaries,
        "firewalls": {
            "hostile_audit_required": True,
            "stage32_main_pruning_credit": False,
            "current_main_incremental_credit": False,
            "full178_producer_candidate_only": True,
            "effectivity_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_credit": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canonical(out)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bands-root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    out = aggregate(args.bands_root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n")
    print(json.dumps({
        "bands": out["coverage"]["received_bands"],
        "rows": out["coverage"]["received_rows"],
        "cells": out["coverage"]["received_cells"],
        "hpadj21": out["totals"]["hpadj21_cellwise_floor_sum"],
        "hpadj22": out["totals"]["hpadj22_exact_survivor_sum"],
        "improvement": out["totals"]["improvement_vs_hpadj21"],
        "strict_cells": out["totals"]["strict_cell_count"],
        "canonical": out["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
