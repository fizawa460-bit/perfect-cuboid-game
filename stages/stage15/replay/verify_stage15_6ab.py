#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_6ab_core_charge import (  # noqa: E402
    actual_outer_charge,
    candidate_core_count,
    mixed_root_line_report,
    physical_parameter_bound_report,
    scan_small_outer_pairs,
    witness_report,
)


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing frozen statement: {needle}")


def main() -> None:
    expected = [
        ((13, 1, 9, 1), 925, 5, 1, 5, 4, 4),
        ((13, 4, 13, 1), 697, 1, 17, 17, 13, 8),
        ((9, 1, 27, 14), 3485, 41, 5, 205, 163, 4),
    ]
    for params, B, k_s, k_o, q, rho, candidates in expected:
        charge = actual_outer_charge(*params)
        assert (charge.actual_k_S, charge.actual_k_O, charge.q) == (k_s, k_o, q)
        assert charge.candidate_count == candidates
        assert candidate_core_count(params[0], params[1]) == candidates

        bounds = physical_parameter_bound_report(*params)
        assert bounds["B"] == B
        assert all(
            bounds[key]
            for key in ("m_le_2B", "n_le_B", "r_le_2B", "s_le_B")
        )

        root = mixed_root_line_report(*params)
        assert root["rho"] == rho
        assert root["q"] == q

    rows = witness_report()
    assert len(rows) == 3
    scan = scan_small_outer_pairs(40)
    assert scan["primitive_outer_pairs"] > 0
    assert scan["max_candidate_core_count"] >= 1

    evidence = json.loads(
        (ROOT / "evidence/stage15_6ab_core_charge.json").read_text(encoding="utf-8")
    )
    assert evidence["classification"] == "MEASURE_PRESERVING_OUTER_PAIR_CORE_CHARGE"
    assert evidence["proved"]["global_core_charge_proved"] is True
    assert evidence["proved"]["physical_measure_adapter_proved"] is True
    assert evidence["proved"]["AR009_fiberwise_globalization_legal"] is True
    assert evidence["nonclaims"]["causal_thinning_exponent_derived"] is False
    assert evidence["nonclaims"]["low_core_negligible_proved"] is False

    result = (ROOT / "15-6ab/result.md").read_text(encoding="utf-8")
    require(result, "STAGE15_6AB_GLOBAL_CORE_CHARGE_PROVED=true")
    require(result, "STAGE15_6AB_PHYSICAL_MEASURE_DISINTEGRATION_PROVED=true")
    require(result, "STAGE15_6AB_AR009_FIBERWISE_GLOBALIZATION_LEGAL=true")
    require(result, "STAGE15_6AB_LOW_CORE_NEGLIGIBLE_PROVED=false")
    require(result, "STAGE15_6AB_CAUSAL_THINNING_EXPONENT_DERIVED=false")

    previous = (ROOT / "15-6aa/result.md").read_text(encoding="utf-8")
    require(previous, "STAGE15_6AA_GLOBAL_CORE_CHARGE_PROVED=false")
    require(previous, "k_S\\mid m^2+n^2")
    require(previous, "k_O\\mid m^2-n^2")

    arsenal = (REPO / "docs/stage14-arsenal.md").read_text(encoding="utf-8")
    require(arsenal, "### AR-009 — Primitive Gaussian root-line lattice count")
    require(arsenal, "### AR-016 — Polynomially bounded divisor/finite-fiber adapter")
    require(arsenal, "### AR-017 — Gaussian quotient and cross-resultant dictionary")
    require(arsenal, "### AR-023 — Scalar fixed-E versus `(E,m)` pair-measure separation")
    require(arsenal, "### AR-024 — Conditioned-kernel measure firewall")

    print("STAGE15_6AB_VERIFY=PASS")
    print("GLOBAL_CORE_CHARGE_PROVED=true")
    print("PHYSICAL_MEASURE_ADAPTER_PROVED=true")
    print("AR009_FIBERWISE_GLOBALIZATION_LEGAL=true")
    print("LOW_CORE_NEGLIGIBLE_PROVED=false")
    print("CAUSAL_THINNING_EXPONENT_DERIVED=false")


if __name__ == "__main__":
    main()
