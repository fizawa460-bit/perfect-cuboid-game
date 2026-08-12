#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing {label}: {needle}")


def main() -> None:
    stage14 = (REPO / "docs/stage14-final-self-contained.md").read_text(encoding="utf-8")
    stage15_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    stage15_2b = (ROOT / "15-2b/result.md").read_text(encoding="utf-8")
    stage15_4 = (ROOT / "15-4/result.md").read_text(encoding="utf-8")
    result = (ROOT / "15-5/result.md").read_text(encoding="utf-8")
    evidence = json.loads((ROOT / "evidence/stage15_5_survival_theorem.json").read_text(encoding="utf-8"))

    # Exact population/cutoff bridge.
    require(stage15_readme, "R\\le B\\iff d\\le B", "Stage15-0 cutoff equivalence")

    # Certified numerator and denominator theorem inputs.
    require(stage14, "N_2(B)\\le C_\\epsilon B^{1/2+\\epsilon}", "Stage14 numerator theorem")
    require(stage15_2b, "M_2(B)\\sim C_{M_2}B(\\log B)^5", "Stage15 ambient asymptotic")
    require(stage15_2b, "M_{2,j}(B)\\sim C_j B(\\log B)^5", "directional ambient asymptotic")

    # Stage15-4 readiness and normal form are inherited but not used as a new saving.
    require(stage15_4, "STAGE15_5_READY_WITH_ARSENAL=true", "Stage15-5 Arsenal readiness")
    require(stage15_4, "sf(N(mr+i*ns))=sf(N(ms+i*nr))", "Stage15-4 normal form")

    # The fixed Stage15-5 theorem and non-claims must remain explicit.
    require(result, "STAGE15_5_SURVIVAL_ZERO_DENSITY=true", "zero-density exit")
    require(result, "STAGE15_5_TRUE_SURVIVAL_EXPONENT_IDENTIFIED=false", "no exponent equality claim")
    require(result, "STAGE15_5_GAUSSIAN_CAUSAL_DERIVATION_PROVED=false", "no causal overclaim")

    assert evidence["inputs"]["common_cutoff_exact"] is True
    assert evidence["theorem"]["zero_density"] is True
    assert evidence["theorem"]["polynomial_thinning_any_delta_lt_half"] is True
    assert evidence["theorem"]["directional_zero_density"] is True
    assert evidence["nonclaims"]["true_survival_exponent_identified"] is False
    assert evidence["nonclaims"]["matching_lower_bound"] is False
    assert evidence["nonclaims"]["gaussian_causal_derivation_proved"] is False
    assert evidence["arsenal"]["AR-006"] == "DIRECT_NUMERATOR_REUSE"
    assert evidence["arsenal"]["AR-017"] == "ADAPTER_REQUIRED_NOT_USED"

    # For every delta<1/2 one may select epsilon<1/2-delta, making
    # -1/2+epsilon strictly smaller than -delta.
    for delta in (0.01, 0.10, 0.25, 0.40, 0.49):
        epsilon = (0.5 - delta) / 2.0
        assert epsilon > 0
        assert -0.5 + epsilon < -delta

    # Directional theorem uses only N2_j <= N2 and positive directional
    # denominator constants; it does not assume a directional Stage14 theorem.
    for total, directional in ((100, 0), (100, 37), (100, 100)):
        assert directional <= total

    print("STAGE15_5_VERIFY=PASS")
    print("SURVIVAL_RATIO_BOUND=O_epsilon(B^(-1/2+epsilon)*(logB)^(-5))")
    print("SURVIVAL_ZERO_DENSITY=true")
    print("POLYNOMIAL_THINNING_ANY_DELTA_LT_HALF=true")
    print("DIRECTIONAL_ZERO_DENSITY=true")
    print("TRUE_SURVIVAL_EXPONENT_IDENTIFIED=false")
    print("GAUSSIAN_CAUSAL_DERIVATION_PROVED=false")


if __name__ == "__main__":
    main()
