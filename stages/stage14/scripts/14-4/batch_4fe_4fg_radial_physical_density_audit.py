from math import gcd, isqrt
from pathlib import Path

repo = Path(__file__).resolve().parents[4]
paths = {
    "4fd": repo / "stages/stage14/14-4fd/result.md",
    "s786": repo / "stages/stage14/14-s7-86/result.md",
    "work": repo / "stages/stage14/14-Work-bqX29/result.md",
    "4fe": repo / "stages/stage14/14-4fe/result.md",
    "4ff": repo / "stages/stage14/14-4ff/result.md",
    "4fg": repo / "stages/stage14/14-4fg/result.md",
    "report": repo / "stages/stage14/14-4-batch/4fe-4fg-report.md",
}
for name, path in paths.items():
    assert path.exists(), (name, path)
texts = {name: path.read_text() for name, path in paths.items()}

assert "SURVIVING_HEAVY_RAY_RADIAL_SUPPORT_LOWER_BOUND=B^(mu-o(1))" in texts["4fd"]
assert "ROOT_OVERLAP_SQUAREPART_RADIAL_EQUATION=d0_J_a_b_equals_c0_h" in texts["s786"]
assert "MAINLINE_HEAVY_MASS_FORCES_MATCHING_RADIAL_SUPPORT_EXPONENT=true" in texts["work"]

for token in [
    "RADIAL_DENOMINATOR_DIVIDES_EVERY_ACCEPTED_H=true",
    "BARE_NORMALIZED_RADIAL_EQUATION_ACCEPTS_EVERY_N=true",
    "FRESH_SQUARECLASS_FACTORIZATION_POWER_SAVING_AVAILABLE=false",
    "NEXT=Stage14-4ff",
]:
    assert token in texts["4fe"], token

for token in [
    "NORMALIZED_RADIAL_SUPPORT_CARDINALITY_EQUALS_H_SUPPORT=true",
    "FIXED_N_FULL_PHYSICAL_REVERSE_FIBER=Bo1",
    "HEAVY_MASS_RELOCATED_TO_NORMALIZED_RADIAL_ACCEPTANCE_SUPPORT=true",
    "NEXT=Stage14-4fg",
]:
    assert token in texts["4ff"], token

for token in [
    "ROOT_PAIR_SINGLE_L_COORDINATE_PROVED=true",
    "RADIAL_THINNING_REDUCED_TO_PHYSICAL_DIVISOR_WINDOW_OCCUPANCY=true",
    "RECEIVER_MATERIALLY_CHANGED=true",
    "NEXT=Stage14-4fh",
]:
    assert token in texts["4fg"], token

for token in [
    "BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3",
    "BATCH_STOP_REASON=receiver_change",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "NEXT=Stage14-4fh",
]:
    assert token in texts["report"], token

# 4fe: the denominator divisibility is exact, and the normalized bare equation
# has an explicit section (J,a,b)=(1,1,c0*n).
for c0 in range(1, 10):
    for d0 in range(1, 10):
        if gcd(c0, d0) != 1:
            continue
        for n in range(1, 30):
            h = d0 * n
            J, a, b = 1, 1, c0 * n
            assert d0 * J * a * b == c0 * h
            assert h % d0 == 0

# Multiples-of-d0 support count.
for H in range(1, 100):
    for d0 in range(1, 20):
        exact = sum(1 for h in range(1, H + 1) if h % d0 == 0)
        assert exact == H // d0

# 4fg: one L coordinate reconstructs both root factors and their product.
def sqf(n: int) -> int:
    out = 1
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e ^= 1
        if e:
            out *= p
        p += 1
    if n > 1:
        out *= n
    return out

for A, B in [(1, 1), (1, 3), (3, 5), (5, 7)]:
    KZ = A * B
    for c0 in range(1, 6):
        for n in range(1, 20):
            target = c0 * n
            for J in range(1, target + 1):
                if sqf(J) != J or gcd(J, KZ) != 1:
                    continue
                for a in range(1, target + 1):
                    if target % (J * a) != 0:
                        continue
                    b = target // (J * a)
                    L = J * a * a
                    X = A * L
                    num = B * c0 * c0 * n * n
                    assert num % L == 0
                    Y = num // L
                    assert X == J * A * a * a
                    assert Y == J * B * b * b
                    assert X * Y == A * B * c0 * c0 * n * n
                    assert sqf(L) == J
                    root = isqrt(sqf(L) * L)
                    assert root * root == sqf(L) * L
                    assert target % root == 0

print("Stage14-main-batch 4fe-4fg audit: OK")
