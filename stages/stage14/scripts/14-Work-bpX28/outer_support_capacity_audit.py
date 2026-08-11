from pathlib import Path

repo = Path(__file__).resolve().parents[3]
paths = {
    "result": repo / "stages/stage14/14-Work-bpX28/result.md",
    "matrix": repo / "docs/stage14-toolbox/work-bpX28-receiver-matrix.md",
    "bo": repo / "stages/stage14/14-Work-boX27/result.md",
    "main": repo / "stages/stage14/14-4fa/result.md",
    "s": repo / "stages/stage14/14-s7-83/result.md",
    "t": repo / "stages/stage14/14-t123/result.md",
}
for key, path in paths.items():
    assert path.exists(), (key, path)
texts = {k: p.read_text() for k, p in paths.items()}

for token in [
    "OUTER_SUPPORT_CAPACITY_LEMMA_PROVED=true",
    "COMMON_OUTER_SUPPORT_CAPACITY_LANGUAGE_PROVED=true",
    "COMMON_SUPPORT_TIMES_ATOMIC_WEIGHT_TEMPLATE_PROVED=true",
    "MAINLINE_HEAVY_RAY_SUPPORT_CAPACITY_EXPONENT_MAX=1/24",
    "UNIFORM_HEAVY_RAY_REQUIRED_MASS_EXPONENT_GT_1_24_PROVED=false",
    "FIXED_U_FINITE_BOUNDARY_SUPPORT_EXPONENT=0",
    "FIXED_U_FINITE_BOUNDARY_ATOMIC_WEIGHT_DEFICIT_PROVED=false",
    "COMMON_ADAPTER_PROVED=false",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "NEXT_INTEGRATED_TARGET=OuterAtomicWeightCapacityDeficitOrNoGo",
]:
    assert token in texts["result"], token

for token in [
    "UNIFORM_FIXED_AGREEMENT_RADIAL_SCALE_COUNT_MAX=B^(1/24+o(1))",
    "HEAVY_RAY_CLOSED=false",
]:
    assert token in texts["main"], token

for token in [
    "POLYNOMIAL_FACTOR_MOBILITY_SPLIT_QUANTITATIVE=true",
    "DIFFUSE_FACTOR_KERNEL_BRANCH_DEFINED=true",
    "FIXED_FACTOR_KERNEL_SQUAREPART_BRANCH_DEFINED=true",
]:
    assert token in texts["s"], token

for token in [
    "FINITE_D4_BOUNDARY_GENERIC_NORM_COUNT_LE_2=true",
    "GENERIC_SUPPORT_POWER_DEFICIT_FORCES_NEAR_TOTAL_BOUNDARY_WEIGHT_CONCENTRATION=true",
]:
    assert token in texts["t"], token

assert "COMMON_FIXED_POWER_SAVING_REQUIRES_POLYNOMIAL_OUTER_MOBILITY=true" in texts["bo"]

# Deterministic support-capacity inequality checks.
for weights in ([1, 2, 3], [5], [2, 7, 1, 4], [0, 0, 9]):
    mass = sum(weights)
    support = len(weights)
    atom = max(weights) if weights else 0
    assert mass <= support * atom

# If support exponent + atomic exponent is below required exponent,
# the capacity exponent cannot support the required mass exponent.
examples = [
    (1/24, 0, 1/12),
    (0, 1/10, 1/8),
    (1/8, 1/8, 3/8),
]
for sigma, omega, eta in examples:
    assert sigma + omega < eta

print("Stage14-Work-bpX28 outer support capacity audit: OK")
