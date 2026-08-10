#!/usr/bin/env python3
"""Validate Stage14-t60 frozen boundary against the deterministic audit output."""

from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
GOT = ROOT / "stages/stage14/data/14-t60/polar_kummer_fourth_moment.json"
FROZEN = ROOT / "stages/stage14/data/14-t60/polar_kummer_fourth_moment_frozen.json"


def main() -> None:
    got = json.loads(GOT.read_text())
    frozen = json.loads(FROZEN.read_text())

    assert got["stage"] == frozen["stage"]
    assert got["split_primes"] == frozen["split_primes"]
    for key, value in frozen["totals"].items():
        assert got["totals"][key] == value, (key, got["totals"][key], value)
    for key, value in frozen["decision"].items():
        assert got["decision"][key] == value, (key, got["decision"][key], value)

    # Numeric diagnostics must also satisfy the theorem-side constant bounds.
    assert got["totals"]["max_aggregated_matrix_hs2"] <= 2 + 1e-6
    assert got["totals"]["max_two_prime_tensor_hs2"] <= 4 + 1e-6
    assert all(r["reconstruction_max_error"] < 2e-8 for r in got["prime_rows"])

    print("Stage14-t60 frozen boundary verified")


if __name__ == "__main__":
    main()
