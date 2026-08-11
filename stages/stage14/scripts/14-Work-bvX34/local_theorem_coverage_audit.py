#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def text(path: str) -> str:
    p = ROOT / path
    assert p.is_file(), f"missing file: {path}"
    return p.read_text(encoding="utf-8")


def require(haystack: str, *needles: str) -> None:
    for needle in needles:
        assert needle in haystack, f"missing lock: {needle}"


result = text("stages/stage14/14-Work-bvX34/result.md")
matrix = text("docs/stage14-toolbox/work-bvX34-receiver-matrix.md")
prev = text("stages/stage14/14-Work-buX33/result.md")
main = text("stages/stage14/14-4fs/result.md")
sroute = text("stages/stage14/14-s7-101/result.md")
th31 = text("stages/stage14/14-tH31/result.md")
t139 = text("stages/stage14/14-t139/result.md")

# Previous integrated boundary and normal revisit trigger.
require(
    prev,
    "PhysicalExistenceSupportVersusFixedResiduePrimeOccupancyTheoremIntersectionOrNoGo",
    "4fs + s7-101 + t139",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
)

# Main/s receiver opening.
require(
    main,
    "HEAVY_SURVIVAL_BUDGET=sigma_j_minus_delta_j_ge_mu",
    "BARE_SHADOW_SAVING_MECHANISM_SEPARATED=true",
    "CONDITIONAL_COMPLETION_SAVING_MECHANISM_SEPARATED=true",
    "CURRENT_HEAVY_RECEIVER=ComplementaryDilationBareShortUnitaryShadowExponentVersusConditionalCanonicalReverseCompletionDeficitBudget",
)
require(
    sroute,
    "FIXED_E_ENDPOINT_ONE_DIMENSIONAL_SUPPORT=true",
    "FIXED_E_TWO_SIDED_POLYNOMIAL_UNITARY_PARTITION_RETAINS=true",
    "WORK_BUX33_REVISIT_TRIGGER_S7_101_REACHED=true",
)

# Positive tH31 theorem and exact surviving fixed-U boundary.
require(
    th31,
    "MITSUI_SAFE_LONG_HEADROOM_THEOREM_APPLICABLE=true",
    "SAFE_BRANCH_FIXED_POWER_DEPLETION_RULED_OUT=true",
    "POSSIBLE_SIEGEL_ZERO_RETAINED=true",
    "ENDPOINT_SHORT_BRANCH_UNCHANGED=true",
    "LARGE_SUBPOLYNOMIAL_MODULUS_BRANCH_UNCHANGED=true",
)
require(
    t139,
    "MITSUI_SAFE_LONG_HEADROOM_BRANCH_DISCHARGED=true",
    "LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias",
    "TH32_NEEDED=false",
)

# Integrated X34 locks.
require(
    result,
    "STAGE14_WORK_TOOLBOX_X=RUN",
    "PRINCIPAL_SCALE_THEOREM_COVERAGE_COMPLETENESS_LEMMA_PROVED=true",
    "BRANCH_LOCAL_POSITIVE_THEOREM_DISCHARGE_PROVED=true",
    "MITSUI_SAFE_LONG_HEADROOM_BRANCH_DISCHARGED=true",
    "MERGED_DIRECT_COMMON_THEOREM_FOR_CURRENT_SURVIVORS=NONE",
    "TH31_SAFE_SAVING_CROSS_PROMOTABLE=false",
    "COMMON_ADAPTER_PROVED=false",
    "SAVING_CROSS_PROMOTABLE=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
    "TH32_NEEDED=false",
    "ResidualPrincipalScaleBranchCoverageOrNoGo",
)
require(
    matrix,
    "MITSUI_SAFE_LONG_HEADROOM_BRANCH_DISCHARGED=true",
    "PRINCIPAL_SCALE_THEOREM_COVERAGE_COMPLETENESS_LEMMA_PROVED=true",
    "MERGED_DIRECT_COMMON_THEOREM_FOR_CURRENT_SURVIVORS=NONE",
    "COMMON_ADAPTER_PROVED=false",
)

# No accidental promotion of the positive fixed-U subbranch theorem.
assert "TH31_SAFE_SAVING_CROSS_PROMOTABLE=true" not in result
assert "STRICT_SUBSQRT_POWER_SAVING_PROVED=true" not in result
assert "NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=true" not in result

print("Stage14-Work-bvX34 local theorem coverage audit: PASS")
