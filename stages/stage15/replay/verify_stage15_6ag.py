#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_6ag_pair_energy import synthetic_report  # noqa: E402


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing frozen statement: {needle}")


def main() -> None:
    row = synthetic_report()
    assert row["shared_prime_receiver_lines"] == 2

    evidence = json.loads((ROOT / "evidence/stage15_6ag_pair_energy.json").read_text())
    assert evidence["large_shared_prime_energy_proved"] is True
    assert evidence["extra_good_overlap_forced"] is False
    assert evidence["global_pair_energy_saving_proved"] is False

    result = (ROOT / "15-6ag/result.md").read_text()
    require(result, "STAGE15_6AG_DEGENERATE_PAIR_COUNT=O(N)")
    require(result, "STAGE15_6AG_LARGE_SHARED_PRIME_ENERGY_BOUND=true")
    require(result, "STAGE15_6AG_EXTRA_GOOD_OVERLAP_FORCED=false")
    require(result, "STAGE15_6AG_SMALL_OR_ZERO_OVERLAP_OPEN=true")
    require(result, "STAGE15_6AG_GLOBAL_PAIR_ENERGY_SAVING_PROVED=false")
    require(result, "STAGE15_6AG_EXIT=LARGE_OVERLAP_ENERGY_CONTROLLED_SMALL_OR_ZERO_OVERLAP_OPEN")
    print("STAGE15_6AG_REPLAY=PASS")


if __name__ == "__main__":
    main()
