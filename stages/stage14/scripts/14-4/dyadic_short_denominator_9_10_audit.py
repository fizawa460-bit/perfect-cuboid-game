from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4ca/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/dyadic_short_denominator_9_10_summary.json"
PREV = ROOT / "stages/stage14/14-s7-12/result.md"


def sf_squarepart(n: int):
    """Return (squarefree coefficient b, maximal squarepart root y) with n=b*y^2."""
    m = n
    p = 2
    b = 1
    y = 1
    while p * p <= m:
        e = 0
        while m % p == 0:
            m //= p
            e += 1
        if e:
            y *= p ** (e // 2)
            if e % 2:
                b *= p
        p += 1 if p == 2 else 2
    if m > 1:
        b *= m
    return b, y


def is_squarefree(n: int) -> bool:
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p += 1
    return True


# 1. Predecessor/current-bound lock.
prev = PREV.read_text()
assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=10/11" in prev
assert "SHORT_DENOMINATOR_ARCHITECTURE_BARRIER=10/11" in prev

# 2. Canonical decomposition finite regression.
for n in range(1, 5000):
    b, y = sf_squarepart(n)
    assert n == b * y * y
    assert is_squarefree(b)

# 3. Exact critical dyad.
q = Fraction(1, 2)
t = Fraction(1, 10)
support = 2 * q - t
cell = 1 - (q - 2 * t) / 3
coeff = q - 2 * t
assert support == Fraction(9, 10)
assert cell == Fraction(9, 10)
assert coeff == Fraction(3, 10)

# 4. Exact crossing identity and domain check.
for q_num in range(0, 101):
    q = Fraction(q_num, 200)  # q in [0,1/2]
    if q >= Fraction(3, 7):
        t0 = (7 * q - 3) / 5
        assert t0 >= 0
        assert t0 <= q / 2
        assert 2 * q - t0 == 1 - (q - 2 * t0) / 3
        assert 2 * q - t0 == 3 * (q + 1) / 5

# 5. Rational grid: every legal dyad is <= 9/10.
worst = Fraction(0, 1)
worst_pair = None
for q_num in range(0, 201):
    q = Fraction(q_num, 400)  # 0..1/2
    for t_num in range(0, q_num + 1):
        # t grid 0..q/2 with common denominator 800
        t = Fraction(t_num, 800)
        if t > q / 2:
            continue
        e1 = 2 * q - t
        e2 = 1 - (q - 2 * t) / 3
        e = min(e1, e2)
        assert e <= Fraction(9, 10)
        if e > worst:
            worst = e
            worst_pair = (q, t)
assert worst == Fraction(9, 10)
assert worst_pair == (Fraction(1, 2), Fraction(1, 10))

# 6. Finite support-count regression.
# Weighted reduced-coordinate support is <= unrestricted support, so audit the latter.
for D in [32, 64, 128, 256, 512]:
    for T in [1, 2, 4, 8, 16]:
        if T * T > 2 * D:
            continue
        total = 0
        for Q in range(D, 2 * D):
            b, y = sf_squarepart(Q)
            if T <= y < 2 * T:
                total += Q
        # Dyadic theorem is O(D^2/T); generous absolute finite constant.
        assert total <= 8 * D * D / T

# 7. Exact exponent ledger.
assert Fraction(10, 11) - Fraction(9, 10) == Fraction(1, 110)
assert Fraction(13, 14) - Fraction(9, 10) == Fraction(1, 35)
assert Fraction(41, 42) - Fraction(9, 10) == Fraction(8, 105)
assert Fraction(9, 10) - Fraction(1, 2) == Fraction(2, 5)

# 8. Frozen summary/result agreement.
summary = json.loads(SUMMARY.read_text())
assert summary["current_physical_upper_bound_exponent"] == "9/10"
assert summary["critical_short_denominator_exponent"] == "1/2"
assert summary["critical_squarepart_exponent"] == "1/10"
assert summary["critical_denominator_coefficient_exponent"] == "3/10"
assert summary["receiver_combination"] == "min"
assert summary["receiver_savings_multiplied"] is False
assert summary["new_whole_family_power_saving_proved"] is True
assert summary["sqrt_B_upper_bound_proved"] is False

text = RESULT.read_text()
for token in [
    "STAGE14_4CA=DYADIC_SHORT_DENOMINATOR_SUPPORT_TWO_CELL_MIN_RECEIVER_AND_9_10_BOUND",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=9/10",
    "DYADIC_RECEIVER_COMBINATION=min",
    "DYADIC_RECEIVER_SAVINGS_MULTIPLIED=false",
    "CRITICAL_SQUAREPART_EXPONENT=1/10",
    "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true",
    "SQRT_B_UPPER_BOUND_PROVED=false",
]:
    assert token in text

print("Stage14-4ca audit: SUCCESS")
print(f"worst dyad={worst_pair}, exponent={worst}")
