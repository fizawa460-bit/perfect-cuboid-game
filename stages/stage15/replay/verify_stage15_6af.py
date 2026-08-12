#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_6af_cross_resultant import witness_report  # noqa: E402


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing frozen statement: {needle}")


def main() -> None:
    rows = witness_report()
    assert len(rows) >= 3
    assert any(r["L_plus"] != 0 and r["L_minus"] != 0 for r in rows)

    evidence = json.loads((ROOT / "evidence/stage15_6af_cross_resultant.json").read_text())
    assert evidence["shared_prime_transfer"] is True
    assert evidence["arsenal"]["AR-017"] == "EXACT_STAGE15_CROSS_RESULTANT_ADAPTER_PROVED_ENERGY_COUNT_OPEN"
    assert evidence["nonclaims"]["pair_energy_bound_proved"] is False

    result = (ROOT / "15-6af/result.md").read_text()
    require(result, "STAGE15_6AF_TWO_POINT_CROSS_RESULTANT=true")
    require(result, "STAGE15_6AF_AR017_EXACT_STAGE15_CROSS_RESULTANT_ADAPTER=true")
    require(result, "STAGE15_6AF_PAIR_ENERGY_BOUND_PROVED=false")
    require(result, "STAGE15_6AF_EXIT=GENUINE_TWO_POINT_CROSS_RESULTANT_RECEIVER_READY")

    predecessor = (ROOT / "15-6ae/result.md").read_text()
    require(predecessor, "STAGE15_6AE_EXIT=ONE_PAIR_ANISOTROPIC_GAUSSIAN_SQUARE_RECEIVER_READY")

    print("STAGE15_6AF_VERIFY=PASS")
    print("CROSS_RESULTANT=true")
    print("PAIR_ENERGY_BOUND_PROVED=false")


if __name__ == "__main__":
    main()
