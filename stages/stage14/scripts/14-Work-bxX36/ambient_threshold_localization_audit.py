from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

RESULT = ROOT / "stages/stage14/14-Work-bxX36/result.md"
MATRIX = ROOT / "docs/stage14-toolbox/work-bxX36-receiver-matrix.md"
MAIN = ROOT / "stages/stage14/14-4fy/result.md"
S = ROOT / "stages/stage14/14-s7-107/result.md"
TH32 = ROOT / "stages/stage14/14-tH32/result.md"
T143 = ROOT / "stages/stage14/14-t143/result.md"
WORK35 = ROOT / "stages/stage14/14-Work-bwX35/result.md"


def text(path: Path) -> str:
    assert path.exists(), path
    return path.read_text(encoding="utf-8")


r = text(RESULT)
m = text(MATRIX)
main = text(MAIN)
s = text(S)
th32 = text(TH32)
t143 = text(T143)
w35 = text(WORK35)

# Gate and global locks.
for needle in [
    "STAGE14_WORK_TOOLBOX_X=RUN",
    "AMBIENT_CAPACITY_THRESHOLD_LOCALIZATION_LEMMA_PROVED=true",
    "COMMON_AMBIENT_THRESHOLD_LOCALIZATION_LANGUAGE_PROVED=true",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "COMMON_ADAPTER_PROVED=false",
    "SAVING_CROSS_PROMOTABLE=false",
    "NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
]:
    assert needle in r, needle

# X35 dependency is actually merged and encoded.
assert "COMMON_ABSOLUTE_CAPACITY_FIRST_PRINCIPLE_PROVED=true" in w35
assert "merged_tH32_result" in w35

# Main rectangular-product source locks.
for needle in [
    "FixedComplementaryDilationTwoSidedPrincipalRectangularDistinctProductCapacityVersusConditionalPhysicalLiftDeficit",
    "Q15_MOVING_INTERVAL_NORMALIZATION_REMAINS=false",
]:
    assert needle in main, needle
for needle in [
    "Q15_MOVING_INTERVAL_NORMALIZATION_REMAINS=false",
    "FIXED_E_TWO_SIDED_RECTANGULAR_PRODUCT_COORDINATE_PROVED=true",
    "FIXED_E_SUBPRINCIPAL_RECTANGLES_DISCHARGED=true",
    "FIXED_E_DISTINCT_PRODUCT_CAPACITY_REMAINS=true",
]:
    assert needle in r, needle

# s-route ordinary upper-envelope source locks.
for needle in [
    "PolynomialComplementaryDilationPolynomialPrimitiveProductMovingOrdinaryDivisorOuterPairAbsoluteCapacityVersusConditionalPhysicalCompletionDeficit",
    "S_ROUTE_H_NEEDED=false",
]:
    assert needle in s, needle
for needle in [
    "S_FIXED_E_MAIN_RECTANGLE_SAME_PACKET=true",
    "S_POLYNOMIAL_PAIR_ORDINARY_UPPER_ENVELOPE_PROVED=true",
    "S_POLYNOMIAL_PAIR_RECTANGULAR_STRAIGHTENING_PROVED=false",
]:
    assert needle in r, needle

# tH32/t143 theorem-threshold locks.
for needle in [
    "B^(1/4",
    "B^(1/2)",
    "7/20",
]:
    assert needle in th32, needle
for needle in [
    "SafeMitsuiModulusIntermediateShortEndpointFixedGaussianResiduePrimeOccupancy",
    "TH33_NEEDED=false",
]:
    assert needle in t143, needle
for needle in [
    "TH32_COMPLETE_CONSUMED=true",
    "TH32_QUARTER_SCALE_DIRECT_THEOREM_APPLICABLE=false",
    "TH32_SAFE_NEAR_FULL_SUBRANGE_DISCHARGED=true",
    "FIXED_U_SAFE_ENDPOINT_THEOREM_GAP_INTERVAL_LOCALIZED=true",
    "TH33_NEEDED=false",
]:
    assert needle in r, needle

# Matrix must mirror the integrated boundary.
for needle in [
    "AMBIENT_CAPACITY_THRESHOLD_LOCALIZATION_LEMMA_PROVED=true",
    "COMMON_AMBIENT_THRESHOLD_LOCALIZATION_LANGUAGE_PROVED=true",
    "COMMON_MULTIPLICATION_TO_GAUSSIAN_PRIME_THRESHOLD_ADAPTER_PROVED=false",
    "COMMON_ADAPTER_PROVED=false",
    "NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
    "TH32_COMPLETE_CONSUMED=true",
    "TH33_NEEDED=false",
]:
    assert needle in m, needle

# Charged-once/no-cross-promotion sanity checks.
assert "fixed-E straightening may not be charged on the polynomial-E outer-pair branch" in r
assert "tH32's near-full Gaussian-prime theorem may not be charged on rectangular product sets" in r
assert "COMMON_MULTIPLICATION_TO_GAUSSIAN_PRIME_THRESHOLD_ADAPTER_PROVED=false" in r

print("Stage14-Work-bxX36 ambient-threshold localization audit: PASS")
