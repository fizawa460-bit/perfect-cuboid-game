#!/usr/bin/env python3
"""Validate Stage14-t61 frozen theorem boundary."""

from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
GOT = ROOT / "stages/stage14/data/14-t61/polar_schatten_obstruction.json"
FROZEN = ROOT / "stages/stage14/data/14-t61/polar_schatten_obstruction_frozen.json"


def main() -> None:
    got = json.loads(GOT.read_text())
    frozen = json.loads(FROZEN.read_text())

    assert got["stage"] == frozen["stage"]
    assert got["split_primes"] == frozen["split_primes"]
    for key, value in frozen["totals"].items():
        assert got["totals"][key] == value, (key, got["totals"][key], value)
    for key, value in frozen["decision"].items():
        assert got["decision"][key] == value, (key, got["decision"][key], value)

    assert got["totals"]["min_polar_leverage_over_p_quarter"] > 0
    assert got["totals"]["min_two_prime_squared_loss_over_sqrt_pq"] > 0
    assert all(r["min_nonzero_row_entries"] >= r["n"] - 4 for r in got["prime_rows"])
    assert all(r["max_resonant_rows_per_t"] <= 4 for r in got["prime_rows"])
    assert all(r["max_nonresonant_correlation"] <= r["weil_safe_envelope"] + 1e-9 for r in got["prime_rows"])

    print("Stage14-t61 frozen boundary verified")


if __name__ == "__main__":
    main()
