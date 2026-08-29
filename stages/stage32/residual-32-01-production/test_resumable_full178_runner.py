#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OLD = HERE / "run_full178_prefix_work_unit.py"
NEW = HERE / "run_full178_resumable_work_unit.py"
RETAINED = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"


def run(script: pathlib.Path, unit: dict, output: pathlib.Path) -> dict:
    subprocess.run(
        [
            sys.executable,
            str(script),
            "--retained",
            str(RETAINED),
            "--marking",
            str(MARKING),
            "--work-unit-json",
            json.dumps(unit, separators=(",", ":")),
            "--node-limit",
            "50000",
            "--output",
            str(output),
        ],
        check=True,
    )
    return json.loads(output.read_text())


def main() -> None:
    source = {"kind": "ROW_TAIL", "row_id": "g0-d008", "e_start": 8}
    with tempfile.TemporaryDirectory() as td:
        root = pathlib.Path(td)
        old = run(OLD, source, root / "old.json")
        new = run(NEW, source, root / "new.json")

        assert old["nodes_used"] == new["nodes_used"] == 50000
        assert old["unknown_count"] == 3  # split current e into two + remaining row tail
        assert new["unknown_count"] == 1  # one exact continuation contains both obligations
        assert new["max_unresolved_children_per_input"] == 1
        assert new["reproduction_factor_structural_upper_bound"] == 1.0

        old_t = old["telemetry"][0]
        new_t = new["telemetry"][0]
        for key in (
            "nodes",
            "membership_prunes",
            "symmetry_prunes",
            "terminal_count",
            "terminal_stream_sha256",
            "complete",
        ):
            assert old_t[key] == new_t[key], (key, old_t[key], new_t[key])

        child = new["unresolved_exact_child_work_units"][0]
        resumed = run(NEW, child, root / "resumed.json")
        assert resumed["unknown_count"] <= 1
        assert resumed["max_unresolved_children_per_input"] == 1
        assert resumed["unknown_is_unsat"] is False
        assert resumed["numerical_row_complete"] is False

        print(json.dumps({
            "verdict": "PASS_REAL_ROW_TAIL_BRANCHING_COLLAPSE",
            "old_children_after_50k": old["unknown_count"],
            "resumable_children_after_50k": new["unknown_count"],
            "resumed_children_after_next_50k": resumed["unknown_count"],
        }, sort_keys=True))


if __name__ == "__main__":
    main()
