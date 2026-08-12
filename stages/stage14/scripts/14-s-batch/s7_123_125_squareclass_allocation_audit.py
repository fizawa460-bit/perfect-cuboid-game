from pathlib import Path
from math import gcd, isqrt

ROOT = Path(__file__).resolve().parents[4]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


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


def divisors(n: int):
    return [d for d in range(1, n + 1) if n % d == 0]


# Exact normalization audit on a finite family.
for C in range(1, 41):
    K = sqf(C)
    cC2 = C // K
    cC = isqrt(cC2)
    assert cC * cC == cC2
    for z in range(1, 16):
        W = C * z * z
        direct = set()
        normalized = set()

        for fm in divisors(W):
            fp = W // fm
            direct.add((fm, fp))
            g = gcd(fm, fp)
            r, s = fm // g, fp // g
            assert gcd(r, s) == 1
            A, B = sqf(r), sqf(s)
            assert A * B == K
            assert gcd(A, B) == 1
            x2, y2 = r // A, s // B
            x, y = isqrt(x2), isqrt(y2)
            assert x * x == x2 and y * y == y2
            assert g * x * y == cC * z
            normalized.add((g * A * x * x, g * B * y * y))

        assert direct == normalized

s123 = read("stages/stage14/14-s7-123/result.md")
s124 = read("stages/stage14/14-s7-124/result.md")
s125 = read("stages/stage14/14-s7-125/result.md")
report = read("stages/stage14/14-s-batch/s7-123-125-report.md")
prev = read("stages/stage14/14-s7-122/result.md")
work = read("stages/stage14/14-Work-cbX40/result.md")

for token in [
    "S_FIRST_REVERSE_SQUARECLASS_ALLOCATION_NORMAL_FORM_PROVED=true",
    "S_FIRST_REVERSE_EXACT_RELATION=g_times_x_times_y_eq_c_times_z",
    "S_FIRST_REVERSE_ALLOCATION_DENSITY_SAVING_RECHARGED=false",
]:
    assert token in s123

for token in [
    "S_FIRST_REVERSE_MULTIPLICATIVE_HOST_SET_DEFINED=true",
    "S_FIRST_MULTIPLICATIVE_FIXED_Z_FIBER_RECHARGED=false",
    "S_MULTIPLICATIVE_CHARGED_MEASURE_COMMON=false",
]:
    assert token in s124

for token in [
    "S_MULTIPLICATIVE_REVERSE_POSTMASK_THREE_DEFICIT_LEDGER_PROVED=true",
    "S_ONE_DIMENSIONAL_MULTIPLICATIVE_REVERSE_THEOREM_CONTRACT_FROZEN=true",
    "S_POLYNOMIAL_PAIR_MULTIPLICATIVE_REVERSE_THEOREM_CONTRACT_FROZEN=true",
    "RECEIVER_MATERIALLY_CHANGED=true",
    "NEXT=Stage14-s7-126",
]:
    assert token in s125

assert "Q18_THEOREM_TARGETS_NOW_STABLE=true" in prev
assert "S_ROUTE_H_NEEDED=false" in work
assert "BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3" in report
assert "BATCH_STOP_REASON=receiver_change" in report
assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2" in report
assert "STRICT_SUBSQRT_POWER_SAVING_PROVED=false" in report
assert "S_ROUTE_H_NEEDED=false" in report
assert "STAGE14_AUTOMATION_SAFE=true" in report
assert "STAGE14_ROUTE=s" in report

print("STAGE14_S_BATCH_S7_123_125_AUDIT=PASS")
