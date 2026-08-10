#!/usr/bin/env python3
"""Validate Stage14-t62 frozen boundary."""

from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
GOT = ROOT / "stages/stage14/data/14-t62/matched_rectangle_frame.json"
FROZEN = ROOT / "stages/stage14/data/14-t62/matched_rectangle_frame_frozen.json"


def main() -> None:
    got = json.loads(GOT.read_text())
    frozen = json.loads(FROZEN.read_text())
    assert got["stage"] == frozen["stage"]
    for key, value in frozen["totals"].items():
        assert got["totals"][key] == value, (key, got["totals"][key], value)
    for key, value in frozen["decision"].items():
        assert got["decision"][key] == value, (key, got["decision"][key], value)

    assert got["totals"]["sum_family_masses"] == got["totals"]["invisible_states"]
    assert got["totals"]["sum_selector_hs2"] == got["totals"]["sum_family_masses"]
    assert all(
        f["hs_orthonormal"] and f["selector_exact_svd"] and f["block_projection_bessel"]
        for p in got["packets"] for f in p["family_rows"]
    )
    print("Stage14-t62 frozen boundary verified")


if __name__ == "__main__":
    main()
