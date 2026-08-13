from pathlib import Path
from fractions import Fraction

repo = Path(__file__).resolve().parents[3]
paths = {
    "t74": repo / "stages/stage14/14-t74/result.md",
    "t122": repo / "stages/stage14/14-t122/result.md",
    "t123": repo / "stages/stage14/14-t123/result.md",
    "bpx28": repo / "stages/stage14/14-Work-bpX28/result.md",
    "t124": repo / "stages/stage14/14-t124/result.md",
}
for name, path in paths.items():
    assert path.exists(), (name, path)
texts = {name: path.read_text() for name, path in paths.items()}

assert "0<r<t" in texts["t74"]
assert "SIGN_CANONICAL_FAILURE_IMPLIES_D4_BOUNDARY=true" in texts["t122"]
assert "FINITE_D4_BOUNDARY_GENERIC_NORM_COUNT_LE_2=true" in texts["t123"]
assert "FIXED_U_FINITE_BOUNDARY_ATOMIC_WEIGHT_DEFICIT_PROVED=false" in texts["bpx28"]

for token in [
    "D4_BOUNDARY_ATOMS_CONTRIBUTE_TO_ACTUAL_PHYSICAL_COUNT=false",
    "BOUNDARY_HEAVY_PACKET_CORE_SAVING_CLOSED=true",
    "BOUNDARY_LIGHT_TARGET_RETAINS_FIXED_POSITIVE_POWER=true",
    "FINITE_BOUNDARY_ATOMIC_CONCENTRATION_AS_SEPARATE_RECEIVER_SUPERSEDED=true",
    "SELECTED_CLASS_NEAR_TOTAL_DEPLETION_IS_ONLY_LIVE_FIXED_U_MECHANISM=true",
    "RECEIVER_MATERIALLY_CHANGED=true",
    "T_ROUTE_H_NEEDED=false",
    "NEXT=Stage14-t125",
]:
    assert token in texts["t124"], token

# D4 boundary and strict physical chamber are disjoint.
for p in range(-4, 5):
    for q in range(-4, 5):
        r, t = q - p, q + p
        physical_chamber = 0 < r < t
        d4_boundary = (p == 0 or q == 0 or p * p == q * q)
        if physical_chamber:
            assert q > p > 0
            assert not d4_boundary

# Baseline conversion: if H_nb > B^{-theta} H and T <= B^{-delta} H,
# then T/H_nb < B^{-(delta-theta)}.  Use rational toy powers.
# B=16, delta=1/2, theta=1/4.
B_delta = Fraction(1, 4)       # 16^{-1/2}
B_theta = Fraction(1, 2)       # 16^{-1/4}
B_delta_minus_theta = Fraction(1, 2)
for H in range(1, 100):
    for Hnb in range(1, H + 1):
        if Fraction(Hnb, H) <= B_theta:
            continue
        T_max = B_delta * H
        assert T_max / Hnb < B_delta_minus_theta

assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2" in texts["t124"]
assert "STRICT_SUBSQRT_POWER_SAVING_PROVED=false" in texts["t124"]

print("Stage14-t-batch t124 audit: OK")
