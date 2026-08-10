#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def require(path: str, token: str) -> None:
    text = (ROOT / path).read_text()
    assert token in text, (path, token)


require("stages/stage14/14-X12/result.md", "STAGE14_X12=COMPLETE_LOST_CORE_FOURTH_ROOT_COLUMN_COFACTOR_COUPLING_AND_71_128_PROMOTION")
require("stages/stage14/14-X12/result.md", "LOST_CORE_FOURTH_ROOT_DIVISOR_DIVIDES_COLUMN_COFACTOR_PRODUCT=true")
require("stages/stage14/14-X12/result.md", "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=71/128")
require("stages/stage14/14-s7-37/result.md", "PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16")
require("stages/stage14/14-4cv/result.md", "STAGE14_4CV=COMPLETE_JOINT_CORE_ROW_COLUMN_COFACTOR_RECONSTRUCTION_AND_SEVEN_TWELFTHS_PROMOTION")
require("stages/stage14/14-4cr/result.md", "CAYLEY_GOOD_CORE_SIGN_ALLOCATION_PROVED=true")


def crt2(a: int, m: int, b: int, n: int) -> int:
    assert gcd(m, n) == 1
    return (a + m * (((b - a) * pow(m, -1, n)) % n)) % (m * n)


def check_nested_crt() -> None:
    Cmm, Cmp, Cpm, Cpp = 5, 13, 17, 29
    Cminus = Cmm * Cmp
    Cplus = Cpm * Cpp
    Cy = Cminus * Cplus
    J = Cmm * Cmp * Cpm
    assert Cy % J == 0 and Cy > J
    JLminus = Cmm * Cpm
    JLplus = Cmp
    Lminus = JLminus * 3
    Lplus = JLplus * 7
    assert Lminus % JLminus == 0 and Lplus % JLplus == 0
    M = 123457
    N0 = crt2(M % Cminus, Cminus, (-M) % Cplus, Cplus)
    assert (N0 - M) % Cminus == 0
    assert (N0 + M) % Cplus == 0
    assert 0 <= N0 < Cy


check_nested_crt()

# Equality ledger.
theta = F(61, 224)
phi = F(1, 4)
chi = 2 * theta + 2 * phi - F(3, 4)
d = chi - F(1, 4)
a = F(3, 112)
b = F(0)
rho = 2 * a
j = chi - 4 * a - 2 * b
cy = chi - 2 * a - 2 * b
lost = chi - j
raw_col = F(1, 4) - j
forced_root = lost / 4
eff_col = raw_col - forced_root
row = F(1, 4) - cy
EH = 3 * phi - F(1, 8) - 3 * a - 3 * b
EFR4 = 2 * phi + eff_col + row

assert chi == F(33, 112)
assert d == F(5, 112)
assert rho == F(3, 56)
assert j == F(3, 16)
assert cy == F(27, 112)
assert lost == F(3, 28)
assert raw_col == F(1, 16)
assert forced_root == F(3, 112) == a
assert eff_col == F(1, 28)
assert row == F(1, 112)
assert EH == EFR4 == F(61, 112)
assert F(71, 128) - F(61, 112) == F(9, 896)
assert F(19, 34) - F(61, 112) == F(27, 1904)
assert F(61, 112) - F(1, 2) == F(5, 112)
assert F(7, 16) < F(61, 112)


def strip_ok(t: F, p: F) -> bool:
    return F(3,16)<=t<=F(5,16) and F(1,8)<=p<=F(1,4) and 0<=t-p<=F(1,8) and t+p>=F(3,8)


def Es(t: F) -> F:
    return max(2*t, 1-2*t)


def Ek(t: F) -> F:
    return 3*t-F(1,4)


def caseA(t: F, p: F) -> F:
    return F(3,2)*p-t+F(7,16)


def caseB(t: F, p: F) -> F:
    return F(9,8)*p-F(3,2)*t+F(43,64)


D = 2240
TARGET = F(61,112)
bestA = (F(-1), None)
bestB = (F(-1), None)
for nt in range(3*D//16, 5*D//16+1):
    t = F(nt,D)
    for np in range(D//8, D//4+1):
        p = F(np,D)
        if not strip_ok(t,p):
            continue
        EA = min(Es(t), Ek(t), caseA(t,p))
        EB = min(Es(t), Ek(t), caseB(t,p))
        if EA > bestA[0]: bestA = (EA,(t,p))
        if EB > bestB[0]: bestB = (EB,(t,p))

assert bestA[0] < TARGET, bestA
assert bestB == (TARGET, (F(61,224),F(1,4))), bestB

out = (ROOT / "stages/stage14/14-4cw/result.md").read_text()
for token in (
    "STAGE14_4CW=COMPLETE_FULL_CAYLEY_ROW_LOST_CORE_FOURTH_ROOT_AND_61_112_PROMOTION",
    "MERGED_X12_IMPORTED=true",
    "LOST_CORE_FOURTH_ROOT_COLUMN_SAVING_IMPORTED=true",
    "FULL_CAYLEY_ROW_AFTER_X12_COLUMN_PROVED=true",
    "FULL_CAYLEY_ROW_AFTER_X12_COLUMN_DOUBLE_CHARGE=false",
    "NONPROPORTIONAL_CASE_A_WEIGHTED_COMBINATION=1:1",
    "NONPROPORTIONAL_CASE_B_WEIGHTED_COMBINATION=5:3",
    "NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=61/112",
    "PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/112",
    "IMPROVEMENT_OVER_MERGED_X12_71_128=9/896",
    "CURRENT_GAP_TO_SQRT=5/112",
    "SIXTYONE_112_SATURATION_THETA=61/224",
    "SIXTYONE_112_FORCED_FOURTH_ROOT_EXPONENT=3/112",
    "SIXTYONE_112_EFFECTIVE_COLUMN_SUPPORT_EXPONENT=1/28",
    "SIXTYONE_112_FULL_ROW_LIFT_EXPONENT=1/112",
    "REMAINING_RECEIVER=SixtyOneOneHundredTwelfthsFullCayleyRowFourthRootColumnShortLiftIncidence",
    "MAINLINE_H_NEEDED=false",
    "NEXT=Stage14-4cx",
):
    assert token in out, token

print("Stage14-4cw full-row + fourth-root audit: PASS")
print("best Case A envelope:", bestA)
print("best Case B envelope:", bestB)
print("equality ledger:", theta, phi, chi, a, j, cy, eff_col, row)
print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/112")
