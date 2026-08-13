from math import gcd
from pathlib import Path

repo = Path(__file__).resolve().parents[3]
paths = {
    "t120": repo / "stages/stage14/14-t120/result.md",
    "t121": repo / "stages/stage14/14-t121/result.md",
    "t122": repo / "stages/stage14/14-t122/result.md",
    "t123": repo / "stages/stage14/14-t123/result.md",
    "contract": repo / "docs/stage14-t-batch-task-contract.md",
}
for name, path in paths.items():
    assert path.exists(), (name, path)
texts = {name: path.read_text() for name, path in paths.items()}

for token in [
    "GENERIC_NORM_SUPPORT_BOOLEAN_EQUALS_SIGN_CANONICAL_EXISTENCE=true",
    "GENERIC_GOOD_PRIME_UNNAMED_LOCAL_SELECTOR_REMAINS=false",
    "FINITE_GAUSSIAN_SYMMETRY_LABEL_COUNT=O1",
    "NEXT=Stage14-t122",
]:
    assert token in texts["t121"], token

for token in [
    "NONBOUNDARY_D4_ORBIT_HAS_CANONICAL_SIGN_REPRESENTATIVE=true",
    "PRIMITIVE_D4_BOUNDARY_NORM_SET={1,2}",
    "GENERIC_SIGN_SUPPORT_POINTWISE_FULL_FOR_K0_M_G_GT_2=true",
    "NEXT=Stage14-t123",
]:
    assert token in texts["t122"], token

for token in [
    "GENERIC_NORM_SUPPORT_COMPLEMENT_SUBSET_FINITE_D4_BOUNDARY=true",
    "FINITE_D4_BOUNDARY_GENERIC_NORM_COUNT_LE_2=true",
    "GENERIC_SUPPORT_POWER_DEFICIT_FORCES_NEAR_TOTAL_BOUNDARY_WEIGHT_CONCENTRATION=true",
    "RECEIVER_MATERIALLY_CHANGED=true",
    "NEXT=Stage14-t124",
]:
    assert token in texts["t123"], token

assert "NEXT=Stage14-t121" in texts["t120"]
assert "Integrated tH work unit and independence" in texts["contract"]

# Primitive lattice points on the D4 boundary p*q*(p^2-q^2)=0
# have norm exactly 1 or 2.
seen = set()
for p in range(-8, 9):
    for q in range(-8, 9):
        if p == 0 and q == 0:
            continue
        if gcd(abs(p), abs(q)) != 1:
            continue
        if p*q*(p*p-q*q) == 0:
            seen.add(p*p + q*q)
assert seen == {1, 2}, seen

# Weighted implication used at t123: if accepted support omits only B,
# M <= xH forces boundary weight >= (1-x)H.
for weights in ([3, 5, 7, 11], [1, 1, 20], [9, 4]):
    H = sum(weights)
    for boundary_mask in range(1 << len(weights)):
        B = sum(w for i, w in enumerate(weights) if boundary_mask >> i & 1)
        M = H - B
        for den in (2, 4, 8):
            x = 1 / den
            if M <= x * H + 1e-12:
                assert B + 1e-12 >= (1 - x) * H

for text in (texts["t121"], texts["t122"], texts["t123"]):
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2" in text
    assert "STRICT_SUBSQRT_POWER_SAVING_PROVED=false" in text

print("Stage14-t-batch t121-t123 audit: OK")
