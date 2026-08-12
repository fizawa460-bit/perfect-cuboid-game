#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_6ac_high_low_core import witness_report  # noqa: E402


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing frozen statement: {needle}")


def main() -> None:
    report = witness_report()
    assert len(report["high"]) == 2
    assert len(report["low"]) == 3

    high_expected = {
        (13, 1, 9, 1): (5, 8),
        (9, 1, 27, 14): (205, 128),
    }
    for row in report["high"]:
        params = tuple(row["params"])
        assert params in high_expected
        assert (row["q"], row["V"]) == high_expected[params]
        assert row["q"] * row["q"] >= row["V"]
        assert row["bound"] is not None

    low_expected = {
        (5, 3, 7, 4): (1, 1, 16),
        (31, 7, 31, 23): (2, 1, 256),
        (11, 1, 29, 22): (5, 5, 256),
    }
    for row in report["low"]:
        params = tuple(row["params"])
        assert params in low_expected
        k, q, V = low_expected[params]
        assert (row["k"], row["q"], row["V"]) == (k, q, V)
        assert q * q < V
        assert row["Pi_alpha"][0] ** 2 + row["Pi_alpha"][1] ** 2 == k
        assert row["Pi_beta"][0] ** 2 + row["Pi_beta"][1] ** 2 == k

    evidence = json.loads(
        (ROOT / "evidence/stage15_6ac_high_low_core.json").read_text(encoding="utf-8")
    )
    assert evidence["classification"] == "HIGH_CORE_ROOT_SPACING_LOW_CORE_GAUSSIAN_SQUARE_RECEIVER"
    assert evidence["high_core"]["fiberwise_sqrt_collapse"] is True
    assert evidence["low_core"]["global_count_proved"] is False
    assert evidence["nonclaims"]["causal_thinning_exponent_derived"] is False

    result = (ROOT / "15-6ac/result.md").read_text(encoding="utf-8")
    require(result, "STAGE15_6AC_HIGH_CORE_FIBERWISE_SQRT_COLLAPSE=true")
    require(result, "STAGE15_6AC_LOW_CORE_GAUSSIAN_SQUARE_RECEIVER=true")
    require(result, "STAGE15_6AC_LOW_CORE_GLOBAL_COUNT_PROVED=false")
    require(result, "STAGE15_6AC_CAUSAL_THINNING_EXPONENT_DERIVED=false")
    require(result, "STAGE15_6AC_AR012_TRIGGERED=false")

    stage6ab = (ROOT / "15-6ab/result.md").read_text(encoding="utf-8")
    require(stage6ab, "STAGE15_6AB_AR009_FIBERWISE_GLOBALIZATION_LEGAL=true")
    require(stage6ab, "STAGE15_6AB_LOW_CORE_NEGLIGIBLE_PROVED=false")

    arsenal = (REPO / "docs/stage14-arsenal.md").read_text(encoding="utf-8")
    require(arsenal, "### AR-009 — Primitive Gaussian root-line lattice count")
    require(arsenal, "### AR-010 — Primitive-ratio rigidity and one-pair reconstruction")
    require(arsenal, "### AR-017 — Gaussian quotient and cross-resultant dictionary")
    require(arsenal, "### AR-023 — Scalar fixed-E versus `(E,m)` pair-measure separation")
    require(arsenal, "### AR-024 — Conditioned-kernel measure firewall")

    print("STAGE15_6AC_VERIFY=PASS")
    print("HIGH_CORE_FIBERWISE_SQRT_COLLAPSE=true")
    print("LOW_CORE_GAUSSIAN_SQUARE_RECEIVER=true")
    print("LOW_CORE_GLOBAL_COUNT_PROVED=false")
    print("CAUSAL_THINNING_EXPONENT_DERIVED=false")


if __name__ == "__main__":
    main()
