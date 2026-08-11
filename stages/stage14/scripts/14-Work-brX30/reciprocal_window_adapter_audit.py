#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
paths = {
    "result": ROOT / "stages/stage14/14-Work-brX30/result.md",
    "matrix": ROOT / "docs/stage14-toolbox/work-brX30-receiver-matrix.md",
    "bq": ROOT / "stages/stage14/14-Work-bqX29/result.md",
    "main": ROOT / "stages/stage14/14-4fg/result.md",
    "s": ROOT / "stages/stage14/14-s7-89/result.md",
    "t": ROOT / "stages/stage14/14-t128/result.md",
}
for key, path in paths.items():
    assert path.exists(), (key, path)
texts = {k: p.read_text() for k, p in paths.items()}

for token in [
    "GLOBAL_S_RECIPROCAL_DIVISOR_WINDOW_COORDINATE_IDENTIFIED=true",
    "COMMON_RECIPROCAL_WINDOW_GEOMETRY_LANGUAGE_PROVED=true",
    "DIRECT_RADIAL_DIVISOR_TO_PROJECTIVE_PRIME_ADAPTER_NOGO_AT_CURRENT_LEVEL=true",
    "COMMON_ARITHMETIC_RECIPROCAL_WINDOW_ADAPTER_PROVED=false",
    "COMMON_ADAPTER_PROVED=false",
    "SAVING_CROSS_PROMOTABLE=false",
    "TH29_COMPLETE_CONSUMED=true",
    "TH30_NEEDED=false",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "NEXT_INTEGRATED_TARGET=ReciprocalWindowEndpointInteriorPhysicalWeightIntersectionOrNoGo",
]:
    assert token in texts["result"], token

for token in [
    "ROOT_PAIR_SINGLE_L_COORDINATE_PROVED=true",
    "RADIAL_THINNING_REDUCED_TO_PHYSICAL_DIVISOR_WINDOW_OCCUPANCY=true",
    "FIXED_N_L_CANDIDATE_COUNT=Bo1",
]:
    assert token in texts["main"], token

for token in [
    "PEELED_ROOT_PAIR_NORMAL_FORM=true",
    "SHARED_SQUAREFREE_FACTOR_CANCELS_FROM_ROOT_RATIO=true",
    "ROOT_PROJECTIVE_RATIO_IS_FIXED_COEFFICIENT_RATIONAL_SQUARE=true",
]:
    assert token in texts["s"], token

for token in [
    "PROJECTIVE_DEPLETION_HEADROOM_SPLIT_EXACT=true",
    "LONG_BRANCH_PRINCIPAL_SCALE_CHARACTER_PIGEONHOLE=true",
    "TH29_DIRECT_THEOREM_APPLICABLE=false",
    "TH30_NEEDED=false",
]:
    assert token in texts["t"], token

assert "GLOBAL_S_COMMON_RADIAL_OUTER_COORDINATE_PROVED=true" in texts["bq"]

# Exact algebraic identification of the s7-89 coordinate with one reciprocal divisor.
for J in [1, 2, 3, 5, 6, 10]:
    for a in [1, 2, 3, 4]:
        for b in [1, 2, 5]:
            n = J * a * b
            L = J * a * a
            assert n * n == L * (J * b * b)
            assert n * n // L == J * b * b

# The structural resemblance to fixed-U is only reciprocal monotonicity, not a map.
# Toy check: increasing first coordinate lowers the reciprocal ceiling.
X = 10_000
prev = None
for n in range(1, 101):
    ceiling = X / n
    if prev is not None:
        assert ceiling <= prev
    prev = ceiling

for token in [
    "GLOBAL_S_RECIPROCAL_DIVISOR_WINDOW_COORDINATE_IDENTIFIED=true",
    "COMMON_ARITHMETIC_RECIPROCAL_WINDOW_ADAPTER_PROVED=false",
    "NEXT_REVISIT_CONDITION=4fj+s7-92+t131",
]:
    assert token in texts["matrix"], token

print("Stage14-Work-brX30 reciprocal window adapter audit: OK")
