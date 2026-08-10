#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def require(path: str, token: str) -> None:
    text = (ROOT / path).read_text()
    assert token in text, (path, token)


# Canonical merged predecessor locks.
require(
    "stages/stage14/14-X12/result.md",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=71/128",
)
require(
    "stages/stage14/14-X12/result.md",
    "LOST_CORE_FOURTH_ROOT_DIVISOR_DIVIDES_COLUMN_COFACTOR_PRODUCT=true",
)
require(
    "stages/stage14/14-s7-37/result.md",
    "PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16",
)
require(
    "stages/stage14/14-4cv/result.md",
    "STAGE14_4CV=COMPLETE_JOINT_CORE_ROW_COLUMN_COFACTOR_RECONSTRUCTION_AND_SEVEN_TWELFTHS_PROMOTION",
)
require(
    "stages/stage14/14-4cr/result.md",
    "CAYLEY_GOOD_CORE_SIGN_ALLOCATION_PROVED=true",
)
require(
    "stages/stage14/14-4cu/result.md",
    "JOINT_CORE_DIVIDES_ENDPOINT_LINEAR_PRODUCT=true",
)


def crt2(a: int, m: int, b: int, n: int) -> int:
    assert gcd(m, n) == 1
    return (a + m * (((b - a) * pow(m, -1, n)) % n)) % (m * n)


# Synthetic nested-core regression: the column uses J while the Cayley row
# continues on the larger C_y after M is known. No product J*C_y is charged.
def check_nested_core_crt() -> None:
    Cmm, Cmp, Cpm, Cpp = 5, 13, 17, 29
    extra_m, extra_p = 37, 41
    vals = (Cmm, Cmp, Cpm, Cpp, extra_m, extra_p)
    for i in range(len(vals)):
        for k in range(i):
            assert gcd(vals[i], vals[k]) == 1

    Jminus = Cmm * Cmp
    Jplus = Cpm * Cpp
    J = Jminus * Jplus
    Cminus = Jminus * extra_m
    Cplus = Jplus * extra_p
    Cy = Cminus * Cplus
    assert Cy % J == 0 and Cy > J

    M = 123457
    NJ = crt2(M % Jminus, Jminus, (-M) % Jplus, Jplus)
    NC = crt2(M % Cminus, Cminus, (-M) % Cplus, Cplus)
    assert (NC - M) % Cminus == 0
    assert (NC + M) % Cplus == 0
    assert (NC - NJ) % J == 0
    assert 0 <= NC < Cy


check_nested_core_crt()


def strip_ok(theta: F, phi: F) -> bool:
    return (
        F(3, 16) <= theta <= F(5, 16)
        and F(1, 8) <= phi <= F(1, 4)
        and 0 <= theta - phi <= F(1, 8)
        and theta + phi >= F(3, 8)
    )


def case_zero(theta: F, phi: F) -> F:
    return 2 * phi


def case_A(theta: F, phi: F) -> F:
    return (3 * phi - 2 * theta + F(7, 8)) / 2


def case_B(theta: F, phi: F) -> F:
    return (9 * phi - 12 * theta + F(43, 8)) / 8


def base_s(theta: F) -> F:
    return max(2 * theta, 1 - 2 * theta)


def base_k(theta: F) -> F:
    return 3 * theta - F(1, 4)


# Exact algebra at the claimed equality point.
theta = F(61, 224)
phi = F(1, 4)
chi = 2 * theta + 2 * phi - F(3, 4)
d = chi - F(1, 4)
a = F(3, 112)
b = F(0)
rho = 2 * a
j = chi - 4 * a - 2 * b
cy = chi - 2 * a - 2 * b
raw_col = F(1, 4) - j
forced_r4 = (chi - j) / 4
effective_col = raw_col - forced_r4
row = F(1, 4) - cy
EH = 3 * phi - F(1, 8) - 3 * a - 3 * b
EFR = 2 * phi + effective_col + row

assert chi == F(33, 112)
assert d == F(5, 112)
assert rho == F(3, 56)
assert j == F(3, 16)
assert cy == F(27, 112)
assert chi - j == F(3, 28)
assert raw_col == F(1, 16)
assert forced_r4 == F(3, 112)
assert effective_col == F(1, 28)
assert row == F(1, 112)
assert EH == EFR == F(61, 112)
assert case_B(theta, phi) == F(61, 112)
assert case_A(theta, phi) == F(121, 224) < F(61, 112)
assert case_zero(theta, phi) == F(1, 2) < F(61, 112)
assert F(71, 128) - F(61, 112) == F(9, 896)
assert F(19, 34) - F(61, 112) == F(27, 1904)
assert F(61, 112) - F(1, 2) == F(5, 112)
assert F(7, 16) < F(61, 112)


# Whole-strip exact rational envelope audit. Each physical packet belongs to
# exactly one of the three short-support cases, so max(case0,A,B) is a valid
# uniform case envelope before intersecting with the complete s/k counts.
D = 3584  # divisible by 224 and 16.
best = (F(-1), None)
for nt in range(3 * D // 16, 5 * D // 16 + 1):
    t = F(nt, D)
    for np in range(D // 8, D // 4 + 1):
        p = F(np, D)
        if not strip_ok(t, p):
            continue
        Ecase = max(case_zero(t, p), case_A(t, p), case_B(t, p))
        E = min(base_s(t), base_k(t), Ecase)
        if E > best[0]:
            best = (E, (t, p))

assert best == (F(61, 112), (F(61, 224), F(1, 4))), best


out = (ROOT / "stages/stage14/14-4cw/result.md").read_text()
for token in (
    "STAGE14_4CW=COMPLETE_LOST_CORE_FOURTH_ROOT_FULL_CAYLEY_ROW_AND_61_112_PROMOTION",
    "MERGED_X12_IMPORTED=true",
    "X12_LOST_CORE_FOURTH_ROOT_COLUMN_SAVING_IMPORTED=true",
    "FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_PROVED=true",
    "FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_DOUBLE_CHARGE=false",
    "NONPROPORTIONAL_CASE_ZERO_BOUND_EXPONENT=1/2",
    "NONPROPORTIONAL_CASE_A_WEIGHTED_COMBINATION=1:1",
    "NONPROPORTIONAL_CASE_B_WEIGHTED_COMBINATION=5:3",
    "NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=61/112",
    "PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/112",
    "IMPROVEMENT_OVER_MERGED_X12_71_128=9/896",
    "CURRENT_GAP_TO_SQRT=5/112",
    "SIXTYONE_112_SATURATION_THETA=61/224",
    "SIXTYONE_112_JOINT_CORE_EXPONENT=3/16",
    "SIXTYONE_112_CAYLEY_GOOD_CORE_EXPONENT=27/112",
    "SIXTYONE_112_FORCED_FOURTH_ROOT_EXPONENT=3/112",
    "SIXTYONE_112_EFFECTIVE_COLUMN_SUPPORT_EXPONENT=1/28",
    "SIXTYONE_112_FULL_ROW_LIFT_EXPONENT=1/112",
    "REMAINING_RECEIVER=SixtyOneOneHundredTwelfthsLostCoreFourthRootFullCayleyRowAsymmetricShortLiftIncidence",
    "MAINLINE_H_NEEDED=false",
    "NEXT=Stage14-4cx",
):
    assert token in out, token

print("Stage14-4cw X12 + full Cayley-row audit: PASS")
print("best whole-strip envelope:", best)
print("equality: theta=61/224 phi=1/4 a=3/112 b=0")
print("effective column=1/28 full-row lift=1/112")
print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/112")
