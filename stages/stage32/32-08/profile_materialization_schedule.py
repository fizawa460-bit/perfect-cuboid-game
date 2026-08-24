#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import pathlib
import sys
from typing import Any

HERE = pathlib.Path(__file__).resolve().parent
S32 = HERE.parent
S32_05 = S32 / "32-05"
S32_07 = S32 / "32-07"
sys.path.insert(0, str(S32_05))


def load_module(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


pilot = load_module("stage32_07_profile", S32_07 / "run_d8_bounded_signature_cells.py")
from cap_certificate import load_and_verify

SCHEMA = "STAGE32_D8_MATERIALIZATION_SCHEDULE_PROFILE_V1"
EXPECTED_CAP_SHA = "75224aee543dcd4a56e814503765d1e1e69514b237fb900688243546ea6b4d03"
THRESHOLDS = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--core", type=pathlib.Path, required=True)
    ap.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--exceptional-mass", type=int, required=True)
    ap.add_argument("--curve-group-mass", type=int, required=True)
    args = ap.parse_args()

    core, _, cap_summary = load_and_verify(args.core, args.cap_certificate)
    assert cap_summary["certificate_canonical_sha256"] == EXPECTED_CAP_SHA
    transform = pilot.base.build_transform(core)
    quotient = pilot.base.quotient_data(transform["inv"])
    aggregate = pilot.base.aggregate_structure(transform["pair"], transform["h"])
    cells, inventory = pilot.build_signature_cells(
        quotient["K"], aggregate["types"], args.exceptional_mass, args.curve_group_mass
    )
    qhead_counts = {int(k): int(v) for k, v in inventory["qhead_assignment_count_by_total"].items()}

    rows: list[dict[str, Any]] = []
    total_branches = 0
    for index, cell in enumerate(cells):
        exceptional = int(cell["left_assignment_count"]) * int(cell["right_assignment_count"])
        t = int(cell["aggregate"][3])
        qhead = qhead_counts[t]
        branches = exceptional * qhead
        total_branches += branches
        rows.append({
            "cell_index": index,
            "cell_id": cell["cell_id"],
            "aggregate": cell["aggregate"],
            "left_assignment_count": int(cell["left_assignment_count"]),
            "right_assignment_count": int(cell["right_assignment_count"]),
            "exceptional_assignment_count": exceptional,
            "qhead_total": t,
            "qhead_assignment_count": qhead,
            "materialized_branch_count": branches,
        })
    rows.sort(key=lambda r: (r["materialized_branch_count"], r["cell_id"]))

    cumulative = []
    for threshold in THRESHOLDS:
        selected = [r for r in rows if r["materialized_branch_count"] <= threshold]
        cumulative.append({
            "branch_threshold": threshold,
            "covered_cell_count": len(selected),
            "covered_cell_fraction": len(selected) / len(rows) if rows else 0.0,
            "covered_exceptional_assignment_count": sum(r["exceptional_assignment_count"] for r in selected),
            "scheduled_materialized_branch_count": sum(r["materialized_branch_count"] for r in selected),
        })

    counts = [r["materialized_branch_count"] for r in rows]
    report = {
        "schema": SCHEMA,
        "degree": pilot.DEGREE,
        "genus": 0,
        "exceptional_mass": args.exceptional_mass,
        "curve_group_mass": args.curve_group_mass,
        "signature_cell_count": len(rows),
        "exceptional_assignment_count_after_qtail_quotient": inventory["exceptional_assignment_count_after_qtail_quotient"],
        "total_materialized_branch_count": total_branches,
        "min_materialized_branch_count": min(counts) if counts else 0,
        "max_materialized_branch_count": max(counts) if counts else 0,
        "branch_count_cumulative_profile": cumulative,
        "cells_sorted_by_branch_count": rows,
        "profile_only": True,
        "theorem_credit": False,
        "receiver_credit": False,
        "FULL_D8_G0_ROW_COMPLETE": False,
        "FULL_D176_D192_NUMERICAL_ORBIT_CENSUS": False,
        "R29_LG2_NUMERICAL_COMPONENT_COMPLETE": False,
        "R29_LG2": "NOT_DISCHARGED",
        "R29_LG2_EFF": "NOT_DISCHARGED",
        "R29_LG2_MB": "NOT_DISCHARGED",
        "G10_LOWGENUS_PICARD": "AMBER",
    }
    report["canonical_sha256_without_this_field"] = pilot.canonical_sha256(report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "e": args.exceptional_mass,
        "a": args.curve_group_mass,
        "cells": len(rows),
        "exceptional_assignments": inventory["exceptional_assignment_count_after_qtail_quotient"],
        "total_branches": total_branches,
        "min": min(counts) if counts else 0,
        "max": max(counts) if counts else 0,
        "thresholds": cumulative,
        "smallest": rows[:10],
        "canonical_sha256": report["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
