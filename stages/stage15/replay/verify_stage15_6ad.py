#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_6ad_low_core_reconstruction import witness_report  # noqa: E402


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing frozen statement: {needle}")


def main() -> None:
    rows = witness_report()
    assert len(rows) == 3
    expected = {
        (5, 3, 7, 4),
        (31, 7, 31, 23),
        (11, 1, 29, 22),
    }
    assert {tuple(row["params"]) for row in rows} == expected
    for row in rows:
        assert row["z_primitive"] is True
        assert row["w_root_fiber_upper_bound"] == 2

    evidence = json.loads(
        (ROOT / "evidence/stage15_6ad_reconstruction.json").read_text(encoding="utf-8")
    )
    assert evidence["classification"] == "LOW_CORE_ONE_SQUARE_ANTILINEAR_TRANSFER_RECONSTRUCTION"
    assert evidence["reconstruction"]["fixed_z_reconstructs_r_s"] is True
    assert evidence["reconstruction"]["fixed_z_reconstructs_w_squared"] is True
    assert evidence["reconstruction"]["second_gaussian_parameter_independent"] is False
    assert evidence["arsenal"]["AR-010"] == "RECONSTRUCTION_FIREWALL_TRIGGERED_STAGE15_EXACT_ADAPTER_PROVED"
    assert evidence["nonclaims"]["low_core_global_count_proved"] is False
    assert evidence["nonclaims"]["causal_thinning_exponent_derived"] is False

    result = (ROOT / "15-6ad/result.md").read_text(encoding="utf-8")
    require(result, "STAGE15_6AD_ONE_SQUARE_RECONSTRUCTION=true")
    require(result, "STAGE15_6AD_FIXED_Z_RECONSTRUCTS_W_SQUARED=true")
    require(result, "STAGE15_6AD_SECOND_GAUSSIAN_PARAMETER_INDEPENDENT=false")
    require(result, "STAGE15_6AD_ANTILINEAR_TRANSFER_IDENTITY=true")
    require(result, "STAGE15_6AD_AR010_EXACT_STAGE15_ADAPTER=true")
    require(result, "STAGE15_6AD_LOW_CORE_GLOBAL_COUNT_PROVED=false")

    arsenal = (REPO / "docs/stage14-arsenal.md").read_text(encoding="utf-8")
    require(arsenal, "### AR-010 — Primitive-ratio rigidity and one-pair reconstruction")
    require(arsenal, "### AR-016 — Polynomially bounded divisor/finite-fiber adapter")
    require(arsenal, "### AR-017 — Gaussian quotient and cross-resultant dictionary")

    print("STAGE15_6AD_VERIFY=PASS")
    print("ONE_SQUARE_RECONSTRUCTION=true")
    print("SECOND_GAUSSIAN_PARAMETER_INDEPENDENT=false")
    print("ANTILINEAR_TRANSFER_IDENTITY=true")
    print("AR010_EXACT_STAGE15_ADAPTER=true")
    print("LOW_CORE_GLOBAL_COUNT_PROVED=false")
    print("CAUSAL_THINNING_EXPONENT_DERIVED=false")


if __name__ == "__main__":
    main()
