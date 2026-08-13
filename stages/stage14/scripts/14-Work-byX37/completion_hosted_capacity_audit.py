from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

RESULT = ROOT / "stages/stage14/14-Work-byX37/result.md"
MATRIX = ROOT / "docs/stage14-toolbox/work-byX37-receiver-matrix.md"
WORK36 = ROOT / "stages/stage14/14-Work-bxX36/result.md"
MAIN = ROOT / "stages/stage14/14-4gb/result.md"
S = ROOT / "stages/stage14/14-s7-110/result.md"
T = ROOT / "stages/stage14/14-t146/result.md"
Q16 = ROOT / "stages/stage14/archive/docs/q-research/stage14-q16-summary.md"


def text(path: Path) -> str:
    assert path.exists(), path
    return path.read_text(encoding="utf-8")


def tau(n: int) -> int:
    n = abs(n)
    assert n >= 1
    ans = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            ans += 1 if d * d == n else 2
        d += 1
    return ans


r = text(RESULT)
m = text(MATRIX)
w36 = text(WORK36)
main = text(MAIN)
s = text(S)
t = text(T)
q16 = text(Q16)

# Gate / global boundary.
for needle in [
    "STAGE14_WORK_TOOLBOX_X=RUN",
    "FIBERED_BOUNDED_MULTIPLICITY_MULTIPLICATION_LEMMA_PROVED=true",
    "GLOBAL_S_AMBIENT_MULTIPLICATIVE_COMPRESSION_AS_FINAL_OBSTRUCTION_SUPERSEDED=true",
    "GLOBAL_S_HEAVY_RECEIVERS_ALL_REDUCED_TO_CONDITIONAL_PHYSICAL_COMPLETION_OR_LIFT=true",
    "FIXED_U_SELECTOR_MODULUS_HOSTED_NOT_INDEPENDENT_ENTROPY=true",
    "COMMON_ADAPTER_PROVED=false",
    "SAVING_CROSS_PROMOTABLE=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
]:
    assert needle in r, needle

# X36 dependency and early-trigger boundary.
assert "AMBIENT_CAPACITY_THRESHOLD_LOCALIZATION_LEMMA_PROVED=true" in w36
assert "merged_4gc" in w36

# Merged mainline source: fixed-E product compression and unitary recovery are exhausted.
for needle in [
    "FixedComplementaryDilationTwoSidedPrincipalRectangularConditionalCanonicalReversePhysicalCompletionDeficitWithCapacityHeadroomKappaMinusMu",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
]:
    assert needle in main, needle

# Merged s source: E remains an outer coordinate and the fibered product receiver is live at s7-110.
for needle in [
    "PolynomialComplementaryDilationPolynomialPrimitiveProductPrincipalFiberedDistinctProductOuterPairCapacityVersusConditionalPhysicalLiftDeficit",
    "S_ROUTE_H_NEEDED=false",
]:
    assert needle in s, needle

# Merged t source: hosted modulus / host-normalized endpoint capacity.
for needle in [
    "SafeMitsuiModulusHostNormalizedIntermediateEndpointFixedGaussianResiduePrimeOccupancy",
    "BeyondMitsuiHostedSelectorHostNormalizedEndpointFixedGaussianResiduePrimeOccupancyBias",
    "TH33_NEEDED=false",
]:
    assert needle in t, needle

# q16 is consumed only on fixed-E ambient product capacity.
for needle in [
    "FIXED_E_DISTINCT_PRODUCT_CAPACITY_FULL_EXPONENT_PROVED=true",
    "FIXED_E_CONDITIONAL_PHYSICAL_LIFT_REMAINS=true",
]:
    assert needle in q16, needle
assert "Q16_CROSS_PROMOTED_TO_POLYNOMIAL_E_S=false" in r

# Deterministic finite audit of Phi(e,d,v)=(e,dv): output multiplicity is bounded by tau(m).
triples = []
for e in range(1, 5):
    for d in range(2, 13):
        for v in range(3, 16):
            if (e + d + v) % 3 != 0:
                triples.append((e, d, v))

counts = Counter((e, d * v) for e, d, v in triples)
for (e, prod), multiplicity in counts.items():
    assert multiplicity <= tau(prod), (e, prod, multiplicity, tau(prod))

# Image cardinality is incidence cardinality divided by at most the maximum divisor fiber.
max_tau = max(tau(d * v) for _, d, v in triples)
assert len(counts) * max_tau >= len(triples)
assert len(counts) <= len(triples)

# Matrix mirrors the integrated boundary.
for needle in [
    "FIBERED_BOUNDED_MULTIPLICITY_MULTIPLICATION_LEMMA_PROVED=true",
    "S_FIBERED_ORDINARY_PRODUCT_FULL_EXPONENT_PROVED=true",
    "FIXED_U_HOST_NORMALIZED_ENDPOINT_CAPACITY_PROVED=true",
    "COMMON_HOSTED_AUXILIARY_NONENTROPY_LANGUAGE_PROVED=true",
    "COMMON_COMPLETION_TO_GAUSSIAN_PRIME_OCCUPANCY_ADAPTER_PROVED=false",
    "COMMON_ADAPTER_PROVED=false",
    "NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
    "TH33_NEEDED=false",
]:
    assert needle in m, needle

# No-recharge / theorem-boundary locks.
for needle in [
    "Q16_RESULT_RECHARGED=false",
    "S_UNITARY_OR_PHYSICAL_LIFT_FULL_DENSITY_PROVED=false",
    "SUBPOLYNOMIAL_HOSTED_AUXILIARY_RECHARGE_FORBIDDEN=true",
    "TH32_COMPLETE_CONSUMED=true",
]:
    assert needle in r, needle

print("Stage14-Work-byX37 completion/hosted-capacity audit: PASS")
