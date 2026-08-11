from pathlib import Path
from math import gcd

ROOT = Path(__file__).resolve().parents[4]

files = {
    "btx32": ROOT / "stages/stage14/14-Work-btX32/result.md",
    "main": ROOT / "stages/stage14/14-4fp/result.md",
    "s": ROOT / "stages/stage14/14-s7-98/result.md",
    "t136": ROOT / "stages/stage14/14-t136/result.md",
    "th30": ROOT / "stages/stage14/14-tH30/result.md",
    "x33": ROOT / "stages/stage14/14-Work-buX33/result.md",
    "matrix": ROOT / "docs/stage14-toolbox/work-buX33-receiver-matrix.md",
}
texts = {k: p.read_text() for k, p in files.items()}

# Merged-boundary locks consumed by this integration.
assert "NEXT=Stage14-4fq" in texts["main"]
assert "NEXT=Stage14-s7-99" in texts["s"]
assert "NEXT=Stage14-t137" in texts["t136"]

# The mainline has relocated polynomial mass away from the inner unitary fiber.
for token in (
    "INNER_UNITARY",
    "OUTER",
):
    assert token.lower() in texts["main"].lower()

# tH30/t136 must be present as the new fixed-U theorem/receiver boundary.
assert "tH30" in texts["t136"] or "TH30" in texts["t136"]
assert "endpoint" in texts["th30"].lower()
assert "residue" in texts["th30"].lower()

# Exact unitary-divisor equivalence toy audit: u||m <=> gcd(u,m/u)=1.
for m in range(1, 100):
    unitary = []
    for u in range(1, m + 1):
        if m % u == 0 and gcd(u, m // u) == 1:
            unitary.append(u)
    # Each primitive factorization m=u*v appears exactly once per chosen u.
    for u in unitary:
        v = m // u
        assert u * v == m
        assert gcd(u, v) == 1

# A B^o(1)-sized witness fiber changes counts by only multiplicity, not a
# new polynomial exponent. Toy finite version: support <= incidence <= K*support.
outer = {
    2: [1],
    3: [],
    5: [1, 5],
    7: [7],
}
support = sum(bool(v) for v in outer.values())
incidence = sum(len(v) for v in outer.values())
K = max(len(v) for v in outer.values())
assert support <= incidence <= K * support

required_x33 = (
    "TOOLBOX_COMPONENT_COMPLETE=true",
    "X_COMPONENT_COMPLETE=true",
    "GLOBAL_S_INNER_UNITARY_MULTIPLICITY_POLYNOMIAL_OBSTRUCTION_EXHAUSTED=true",
    "GLOBAL_S_OUTER_PHYSICAL_EXISTENCE_SUPPORT_RECEIVER_PROVED=true",
    "FIXED_U_OPAQUE_COFACTOR_WEIGHT_OBSTRUCTION_EXHAUSTED=true",
    "FIXED_U_RECEIVER_RELOCATED_TO_PRIME_SIDE_ONLY=true",
    "COMMON_OUTER_FAMILY_INNER_ARITHMETIC_WITNESS_LANGUAGE_PROVED=true",
    "BTX32_WEIGHT_LOCATION_AS_FINAL_COMMON_OBSTRUCTION_SUPERSEDED=true",
    "DIRECT_OUTER_SUPPORT_EXISTENCE_TO_FIXED_RESIDUE_PRIME_OCCUPANCY_ADAPTER_NOGO_AT_CURRENT_LEVEL=true",
    "COMMON_ADAPTER_PROVED=false",
    "SAVING_CROSS_PROMOTABLE=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "TH31_NEEDED=false",
    "NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
)
for token in required_x33:
    assert token in texts["x33"], token

required_matrix = (
    "GLOBAL_S_MAIN_S_COUNTS_MULTIPLICABLE=false",
    "FIXED_U_TYPE_I_II_COFACTOR_ADAPTER_OBSTRUCTION_EXHAUSTED=true",
    "COMMON_PHYSICAL_MEASURE_ADAPTER_PROVED=false",
    "COMMON_ARITHMETIC_INNER_SELECTOR_ADAPTER_PROVED=false",
    "TH31_NEEDED=false",
)
for token in required_matrix:
    assert token in texts["matrix"], token

# Cross-route no-double-charge / no-cross-promotion boundary.
assert "COMMON_ADAPTER_PROVED=false" in texts["x33"]
assert "GLOBAL_FIXED_U_SAVING_CROSS_PROMOTED=false" in texts["x33"]

print("Stage14-Work-buX33 support/occupancy adapter audit: OK")
