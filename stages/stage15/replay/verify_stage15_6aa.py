#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_6aa_core_adapter import (  # noqa: E402
    classify_core,
    physical_exact_two,
    scan_small_survivors,
    witness_report,
)


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing frozen statement: {needle}")


def main() -> None:
    expected = [
        ((13, 1, 9, 1), 10, 5, 1),
        ((13, 4, 13, 1), 17, 1, 17),
        ((9, 1, 27, 14), 205, 41, 5),
    ]
    for params, k, k_s, k_o in expected:
        split = classify_core(*params)
        assert (split.k, split.k_S, split.k_O) == (k, k_s, k_o)
        assert physical_exact_two(*params)

    rows = witness_report()
    assert len(rows) == 3

    stats = scan_small_survivors(18)
    assert stats == {
        "survivors": 12,
        "physical_exact_two_survivors": 12,
        "mixed": 0,
        "S_only": 2,
        "O_only": 2,
    }

    evidence = json.loads(
        (ROOT / "evidence/stage15_6aa_core_adapter.json").read_text(encoding="utf-8")
    )
    assert evidence["classification"] == "TWO_CHANNEL_GAUSSIAN_DETERMINANT_LOCK"
    assert evidence["arsenal"]["AR-009"] == "EXACT_LOCAL_ADAPTER_PROVED_GLOBAL_CHARGE_OPEN"
    assert evidence["nonclaims"]["global_core_charge_proved"] is False
    assert evidence["nonclaims"]["causal_thinning_exponent_derived"] is False

    result = (ROOT / "15-6aa/result.md").read_text(encoding="utf-8")
    require(result, "STAGE15_6AA_TWO_CHANNEL_SPLIT=true")
    require(result, "STAGE15_6AA_AR009_LOCAL_ADAPTER=true")
    require(result, "STAGE15_6AA_GLOBAL_CORE_CHARGE_PROVED=false")
    require(result, "STAGE15_6AA_CAUSAL_THINNING_EXPONENT_DERIVED=false")

    stage15_4 = (ROOT / "15-4/result.md").read_text(encoding="utf-8")
    require(stage15_4, "sf(N(mr+i*ns))=sf(N(ms+i*nr))")

    arsenal = (REPO / "docs/stage14-arsenal.md").read_text(encoding="utf-8")
    require(arsenal, "### AR-009 — Primitive Gaussian root-line lattice count")
    require(arsenal, "### AR-017 — Gaussian quotient and cross-resultant dictionary")
    require(arsenal, "### AR-018 — Cayley/Gaussian squareclass orientation split")

    print("STAGE15_6AA_VERIFY=PASS")
    print("CAUSAL_CANDIDATE=TWO_CHANNEL_GAUSSIAN_DETERMINANT_LOCK")
    print("AR009_LOCAL_ADAPTER=true")
    print("AR017_LOCAL_DIVISOR_LIFT=true")
    print("GLOBAL_CORE_CHARGE_PROVED=false")
    print("CAUSAL_THINNING_EXPONENT_DERIVED=false")


if __name__ == "__main__":
    main()
