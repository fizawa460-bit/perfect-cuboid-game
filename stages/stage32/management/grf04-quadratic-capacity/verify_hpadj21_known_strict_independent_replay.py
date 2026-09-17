#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

EVENT_VERIFIER_BLOB = "eda1baab64ffeaf41f03dbf810c2b24beb31bced"
PREFLIGHT_RECORD_BLOB = "c3949f06501debcd062dca2d8fc3962f725e337e"
ORIGINAL_LOW_D_CANONICAL = "ddd139f47889ad1a32f4f0604a399a5b97757da9844ca34d5d22ba7c2b57e81e"
ORIGINAL_NEAR_MAX_CANONICAL = "7da39b4427f1f164c8b484216ec67b32287ecd8215006f36d24421eac5962c7a"


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-root", type=Path, required=True)
    args = ap.parse_args()

    here = Path(__file__).resolve().parent
    event_path = here / "verify_hpadj21_event_compiled_capacity_preflight.py"
    record_path = here / "HPADJ21-KNOWN-STRICT-SUBSET-MAIN-PREFLIGHT.json"

    # Lock the MAIN-side independent compiler and the frozen measurement record
    # before importing or interpreting either one.
    req(event_path.is_file() and git_blob(event_path) == EVENT_VERIFIER_BLOB,
        "MAIN event-compiler verifier blob drift")
    req(record_path.is_file() and git_blob(record_path) == PREFLIGHT_RECORD_BLOB,
        "known-strict preflight record blob drift")
    record = json.loads(record_path.read_text())
    event = load_module(event_path, "main_hpadj21_event_compiler_for_independent_replay")

    root = args.source_root.resolve()
    row_worker = root / "stages/stage32-ex5/hpadj-21_ex5/run_full_hist_row.py"
    pilot = root / "stages/stage32-ex5/hpadj-21_ex5/strictness_pilot_bounded_exact.py"
    hpadj20 = root / "stages/stage32-ex5/hpadj-20_ex5/derive_two_tier_qa_predomain_picard_lp_bound.py"

    # Fail closed before importing retained specialist code.  The replay uses
    # the fixed later HPADJ21 boundary, not the old diagnostic checkout, and
    # reconstructs e-capacities by interval events instead of direct e loops.
    req(row_worker.is_file() and git_blob(row_worker) == event.ROW_WORKER_BLOB,
        "retained HPADJ21 row-worker drift")
    req(pilot.is_file() and git_blob(pilot) == event.PILOT_BLOB,
        "retained HPADJ21 pilot drift")
    req(hpadj20.is_file() and git_blob(hpadj20) == event.HPADJ20_BLOB,
        "retained HPADJ20 parent drift")
    worker = event.load_module(row_worker, "main_hpadj21_row_worker_for_known_strict_replay")

    p = worker.load_pilot()
    h20 = p.load_parent(); h19 = h20.load_parent(); h18 = h19.load_parent(); h17 = h18.load_parent(); h16 = h17.load_parent()
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "hpadj15_locked_for_known_strict_replay")
    p14 = p15.load_parent(); counter = p14.load_counter()
    manifest = counter.load_locked_json(
        p14.MANIFEST,
        p14.LOCKS["manifest_blob"],
        p14.LOCKS["manifest_canonical"],
        "FULL178 manifest",
    )
    rows = counter.manifest_rows(manifest)
    req(len(rows) == 178, "FULL178 row coverage")
    index_by_id = {str(row_id): i for i, (row_id, _g, _d) in enumerate(rows)}
    req(tuple(p15.PLANNED[0]) == (0, 11), "first b-interval drift")

    measured = record["measured_strict_subset"]
    low_expected = measured["bounded_low_d_cells"]
    low_results = []
    low_sum = 0
    for expected in low_expected:
        row_id = str(expected["row_id"])
        req(row_id in index_by_id, f"missing low-d row {row_id}")
        replay = event.compiled_row(worker, index_by_id[row_id])
        strict = [r for r in replay["cell_records"] if r["strict"]]
        req(len(strict) == 1, f"unexpected strict-cell count on {row_id}")
        cell = strict[0]
        req(int(cell["interval_position"]) == 0, f"strict low-d cell moved off [0,11] on {row_id}")
        req(int(cell["hpadj20_floor"]) == int(expected["hpadj20_floor"]), f"HPADJ20 floor mismatch {row_id}")
        req(int(cell["hpadj21_floor"]) == int(expected["full_hist_floor"]), f"HPADJ21 floor mismatch {row_id}")
        improvement = int(cell["hpadj20_floor"]) - int(cell["hpadj21_floor"])
        req(improvement == int(expected["floor_improvement"]), f"floor improvement mismatch {row_id}")
        low_sum += improvement
        low_results.append({
            "row_id": row_id,
            "row_index": index_by_id[row_id],
            "hpadj20_floor": int(cell["hpadj20_floor"]),
            "hpadj21_floor": int(cell["hpadj21_floor"]),
            "floor_improvement": improvement,
        })

    req(low_sum == int(measured["bounded_low_d_floor_improvement_sum"]),
        "bounded low-d improvement sum mismatch")

    near_expected = measured["near_max_row"]
    near_id = str(near_expected["row_id"])
    req(near_id in index_by_id, "near-max row missing")
    near = event.compiled_row(worker, index_by_id[near_id])
    req(int(near["row"]["index"]) == int(near_expected["row_index"]), "near-max row index drift")
    req(int(near["row"]["d"]) == 190, "near-max d drift")
    req(int(near["totals"]["strict_cell_count"]) == int(near_expected["strict_cells"]),
        "near-max strict-cell count mismatch")
    near_improvement = int(near["totals"]["floor_improvement"])
    req(near_improvement == int(near_expected["floor_improvement_vs_hpadj20"]),
        "near-max floor improvement mismatch")

    combined = low_sum + near_improvement
    req(combined == int(measured["known_measured_floor_improvement_sum"]),
        "known measured improvement sum mismatch")
    current = int(record["current_authority"]["authoritative_remaining_terminals"])
    candidate = current - combined
    req(candidate == int(record["candidate"]["candidate_upper_bound"]),
        "candidate upper bound arithmetic mismatch")

    out = {
        "schema": "STAGE32_MAIN_HPADJ21_KNOWN_STRICT_INDEPENDENT_EVENT_REPLAY_V1",
        "status": "INDEPENDENT_EVENT_COMPILED_REPLAY_PASS__ZERO_MAIN_CREDIT",
        "source_boundary": {
            "hpadj21_exact_head": event.HPADJ21_HEAD,
            "row_worker_blob_sha1": event.ROW_WORKER_BLOB,
            "bounded_pilot_blob_sha1": event.PILOT_BLOB,
            "hpadj20_parent_blob_sha1": event.HPADJ20_BLOB,
            "main_event_compiler_blob_sha1": EVENT_VERIFIER_BLOB,
            "main_preflight_record_blob_sha1": PREFLIGHT_RECORD_BLOB,
        },
        "original_measurement_provenance": {
            "bounded_low_d_canonical_sha256": ORIGINAL_LOW_D_CANONICAL,
            "near_max_row_canonical_sha256": ORIGINAL_NEAR_MAX_CANONICAL,
        },
        "bounded_low_d": {
            "replayed_cells": low_results,
            "floor_improvement_sum": low_sum,
        },
        "near_max_row": {
            "row_id": near_id,
            "row_index": int(near["row"]["index"]),
            "strict_cell_count": int(near["totals"]["strict_cell_count"]),
            "floor_improvement": near_improvement,
            "compiler_accounting": near["compiler_accounting"],
        },
        "known_measured_floor_improvement_sum": combined,
        "zero_credit_candidate_upper_bound": candidate,
        "independence_semantics": {
            "original_direct_e_expansion_reused": False,
            "event_compiled_capacity_assembly_used": True,
            "shared_exact_lp_kernel_is_source_locked": True,
            "same_population_same_cell_replacement_only": True,
            "additive_independence_assumed": False,
        },
        "firewalls": {
            "stage32_main_pruning_credit": False,
            "current_main_incremental_credit": False,
            "full178_complete": False,
            "theorem_credit": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_credit": False,
            "merge_authorized": False,
        },
    }
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
