#!/usr/bin/env python3

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SRC = ROOT / "stages/stage14/data/14-num-alpha11-diag8/extended_denominator_summary.json"

# Proved Stage13 limiting face vector, frozen in diag8.
P = (0.5347369332, 0.2453591778, 0.2199038889)


def close(a: float, b: float, tol: float = 5e-10) -> bool:
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)


def main() -> None:
    data = json.loads(SRC.read_text())
    rows = data["rows"]

    assert [row["B"] for row in rows] == data["checkpoints"]

    for row in rows:
        Aab, Aac, Abc = row["raw"]
        a, b, c = row["pair"]
        endpoint = (a + b, a + c, b + c)
        assert list(endpoint) == row["endpoint"]

        sab = endpoint[0] / Aab
        sac = endpoint[1] / Aac
        sbc = endpoint[2] / Abc
        rel = (sab / sbc, sac / sbc, 1.0)

        for got, frozen in zip(rel, row["survival_rel_bc"]):
            assert close(got, frozen)

        # The bridge signal is the persistent ordering only; no convergence claim.
        assert sab < sac < sbc

    # Conditional algebra: hypothetical pair law 2:2:1 -> endpoint law 4:3:3.
    C = (2.0, 2.0, 1.0)
    endpoint_law = (C[0] + C[1], C[0] + C[2], C[1] + C[2])
    assert endpoint_law == (4.0, 3.0, 3.0)

    target = (
        (endpoint_law[0] / P[0]) / (endpoint_law[2] / P[2]),
        (endpoint_law[1] / P[1]) / (endpoint_law[2] / P[2]),
        1.0,
    )
    frozen_target = data["required_relative_survival_if_stage13_limit_plus_hypothetical_221"]
    for got, frozen in zip(target, frozen_target):
        assert close(got, frozen, tol=2e-9)

    print("Stage14-bridge1 deterministic audit: PASS")
    print("checkpoints:", data["checkpoints"])
    print("persistent ordering: S_ab < S_ac < S_bc")
    print("conditional 2:2:1 target:", target)
    print("receiver: Stage14-4be chamber-resolved D_loc/A_W")


if __name__ == "__main__":
    main()
