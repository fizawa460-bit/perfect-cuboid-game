from fractions import Fraction
from pathlib import Path

repo = Path(__file__).resolve().parents[3]
paths = {
    "t112": repo / "stages/stage14/14-t112/result.md",
    "t113": repo / "stages/stage14/14-t113/result.md",
    "t114": repo / "stages/stage14/14-t114/result.md",
    "batch": repo / "stages/stage14/14-t-batch-t112-114/result.md",
}
for name, path in paths.items():
    assert path.exists(), (name, path)

texts = {name: path.read_text() for name, path in paths.items()}

for token in [
    "SELECTED_CLASS_PRINCIPAL_CENTERED_DECOMPOSITION_EXACT=true",
    "CLASS_DISCREPANCY_HAS_ZERO_CLASS_MEAN=true",
    "PROJECTIVE_PRINCIPAL_FACTOR_FIXED_POWER_SAVING=false",
    "NEXT=Stage14-t113",
]:
    assert token in texts["t112"], token

for token in [
    "ORDINARY_PROJECTIVE_EQUIDISTRIBUTION_FIXED_POWER_SOURCE=false",
    "PROJECTIVE_SAVING_REQUIRES_PRINCIPAL_SCALE_NEGATIVE_DISCREPANCY=true",
    "NEXT=Stage14-t114",
]:
    assert token in texts["t113"], token

for token in [
    "WEIGHTED_PHYSICAL_COFACTOR_CORE_DENSITY_DEFINED=true",
    "FIXED_POWER_SAVING_DICHOTOMY_EXACT=true",
    "COFACTOR_CORE_POWER_DEFICIT_BRANCH_EXPOSED=true",
    "SELECTED_CLASS_NEAR_TOTAL_DEPLETION_BRANCH_EXPOSED=true",
    "RECEIVER_MATERIALLY_CHANGED=true",
    "NEXT=Stage14-t115",
]:
    assert token in texts["t114"], token

for text in (texts["t112"], texts["t113"], texts["t114"], texts["batch"]):
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2" in text
    assert "STRICT_SUBSQRT_POWER_SAVING_PROVED=false" in text

# Exact principal/centered identity on sample projective class histograms.
for counts in ([7, 5, 4, 8], [0, 3, 1], [11, 11, 11, 11, 11]):
    g = len(counts)
    total = sum(counts)
    A = Fraction(total, g)
    deltas = [Fraction(k) - A for k in counts]
    assert sum(deltas) == 0
    for k, delta in zip(counts, deltas):
        assert Fraction(k) == A + delta

# t114 dichotomy algebra: x=B^{-delta}; sqrt_x=B^{-delta/2}.
x = Fraction(1, 16)
sqrt_x = Fraction(1, 4)
for H in range(1, 65):
    for M in range(0, H + 1):
        mu = Fraction(M, H)
        for T in range(0, H + 1):
            if Fraction(T, H) > x:
                continue
            if mu <= sqrt_x:
                assert Fraction(M, H) <= sqrt_x
            else:
                D = T - M
                assert Fraction(D, 1) <= -(1 - sqrt_x) * M

assert "BATCH_SUBSTANTIVE_STAGE_COUNT=3" in texts["batch"]
assert "BATCH_STOP_REASON=receiver_change" in texts["batch"]
assert "T_ROUTE_H_NEEDED=false" in texts["batch"]
assert "NEXT=Stage14-t115" in texts["batch"]

print("Stage14-t-batch t112-t114 audit: OK")
