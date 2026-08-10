#!/usr/bin/env python3
"""Validate the compact frozen Stage14-t58 summary against the audit output."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LIVE = ROOT / "stages/stage14/data/14-t58/physical_mask_radial_transfer.json"
FROZEN = ROOT / "stages/stage14/data/14-t58/physical_mask_radial_transfer_frozen.json"


def main() -> None:
    got = json.loads(LIVE.read_text())
    frozen = json.loads(FROZEN.read_text())

    assert got["stage"] == frozen["stage"]
    assert got["input"]["reciprocal_states"] == frozen["reciprocal_states"]
    assert got["input"]["invisible_states"] == frozen["invisible_states"]
    assert got["input"]["fixed_U_fibers"] == frozen["fixed_U_fibers"]

    radial = got["radial_cell_energy"]
    assert radial["cells"] == frozen["radial_cells"]
    assert radial["multiplicity_histogram"] == frozen["radial_cell_multiplicity_histogram"]
    assert radial["max_frozen_cell"] == frozen["max_frozen_radial_cell"]
    assert radial["frozen_energy"] == frozen["frozen_radial_cell_energy"]

    guard = got["non_cartesian_guard"]
    fw = frozen["rectangle_witness"]
    assert guard["U"] == fw["U"]
    assert guard["u1"] == fw["u1"]
    assert guard["u2"] == fw["u2"]
    assert guard["v1"] == fw["v1"]
    assert guard["v2"] == fw["v2"]
    assert guard["rectangle_membership"] == fw["membership"]

    for key, value in frozen["decision"].items():
        assert got["decision"][key] == value, (key, got["decision"][key], value)

    print("Stage14-t58 frozen summary verified")


if __name__ == "__main__":
    main()
