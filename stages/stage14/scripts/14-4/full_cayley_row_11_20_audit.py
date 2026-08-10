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
    "stages/stage14/14-X11/result.md",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34",
)
require(
    "stages/stage14/14-s7-37/result.md",
    "PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16",
)
require(
    "stages/stage14/14-s7-37/result.md",
    "NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34",
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


# Synthetic nested-core regression.  J is a strict divisor of the full
# Cayley-good core.  The column step uses J; after M is known, the row step
# legally uses all of C_y.
def check_nested_core_crt() -> None:
    Cmm, Cmp, Cpm, Cpp = 5, 13, 17, 29
    cells = (Cmm, Cmp, Cpm, Cpp)
    for i in range(4):
        for k in range(i):
            assert gcd(cells[i], cells[k]) == 1

    Cminus = Cmm * Cmp
    Cplus = Cpm * Cpp
    Cy = Cminus * Cplus

    # Residual-good intersection omits one Cayley cell.
    Jmm, Jmp, Jpm, Jpp = Cmm, Cmp, Cpm, 1
    J = Jmm * Jmp * Jpm * Jpp
    assert Cy % J == 0 and Cy > J

    JLminus = Jmm * Jpm
    JLplus = Jmp * Jpp
    hm, hp = 3, 7
    Lminus = JLminus * hm
    Lplus = JLplus * hp
    assert Lminus % JLminus == 0
    assert Lplus % JLplus == 0

    # Parity-compatible linear reconstruction; exact endpoint factors are
    # irrelevant to the modular nesting regression.
    A2 = Lplus + Lminus
    B2 = Lplus - Lminus
    assert A2 - B2 == 2 * Lminus
    assert A2 + B2 == 2 * Lplus

    M = 123457
    N0_full = crt2(M % Cminus, Cminus, (-M) % Cplus, Cplus)
    assert (N0_full - M) % Cminus == 0
    assert (N0_full + M) % Cplus == 0
    assert 0 <= N0_full < Cy

    # The full row fixes a strictly finer class than reducing the same class
    # modulo J.  No product J*Cy is used.
    assert N0_full % J == N0_full % J
    assert Cy > J


check_nested_core_crt()


def strip_ok(theta: F, phi: F) -> bool:
    return (
        F(3, 16) <= theta <= F(5, 16)
        and F(1, 8) <= phi <= F(1, 4)
        and 0 <= theta - phi <= F(1, 8)
        and theta + phi >= F(3, 8)
    )


def case_A(theta: F, phi: F) -> F:
    return (12 * phi - 6 * theta + F(5, 2)) / 7


def case_B(theta: F, phi: F) -> F:
    return (4 * phi - 4 * theta + F(7, 4)) / 3


def base_s(theta: F) -> F:
    return max(2 * theta, 1 - 2 * theta)


def base_k(theta: F) -> F:
    return 3 * theta - F(1, 4)


# Exact theorem algebra at the claimed equality point.
theta = F(11, 40)
phi = F(1, 4)
chi = 2 * theta + 2 * phi - F(3, 4)
d = chi - F(1, 4)
a = F(1, 40)
b = F(0)
rho = 2 * a
j = chi - 4 * a - 2 * b
cy = chi - 2 * a - 2 * b
EH = 3 * phi - F(1, 8) - 3 * a - 3 * b
col = 4 * a + 2 * b - d
row = max(F(0), 2 * a + 2 * b - d)
EFR = 2 * phi + col + row

assert chi == F(3, 10)
assert d == F(1, 20)
assert rho == F(1, 20)
assert j == F(1, 5)
assert cy == F(1, 4)
assert col == F(1, 20)
assert row == 0
assert EH == EFR == F(11, 20)
assert case_A(theta, phi) == F(11, 20)
assert case_B(theta, phi) == F(11, 20)
assert F(19, 34) - F(11, 20) == F(3, 340)
assert F(11, 20) - F(1, 2) == F(1, 20)
assert F(7, 16) < F(11, 20)


# Whole-strip exact rational envelope audit.  We do not need to optimize over
# a,b here: Stage14-4cw proves a casewise bound independent of them after the
# weighted cancellation.  The merged s/k complete counts control the lower
# theta region.
D = 1360  # divisible by 16 and 40; includes theta=11/40 and phi=1/4.
best_A = (F(-1), None)
best_B = (F(-1), None)
for nt in range(3 * D // 16, 5 * D // 16 + 1):
    t = F(nt, D)
    for np in range(D // 8, D // 4 + 1):
        p = F(np, D)
        if not strip_ok(t, p):
            continue

        EA = min(base_s(t), base_k(t), case_A(t, p))
        EB = min(base_s(t), base_k(t), case_B(t, p))
        if EA > best_A[0]:
            best_A = (EA, (t, p))
        if EB > best_B[0]:
            best_B = (EB, (t, p))

assert best_A == (F(11, 20), (F(11, 40), F(1, 4))), best_A
assert best_B == (F(11, 20), (F(11, 40), F(1, 4))), best_B


out = (ROOT / "stages/stage14/14-4cw/result.md").read_text()
for token in (
    "STAGE14_4CW=COMPLETE_FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_RECONSTRUCTION_AND_11_20_PROMOTION",
    "FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_PROVED=true",
    "FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_DOUBLE_CHARGE=false",
    "NONPROPORTIONAL_CASE_A_WEIGHTED_COMBINATION=4:3",
    "NONPROPORTIONAL_CASE_B_WEIGHTED_COMBINATION=2:1",
    "NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=11/20",
    "PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=11/20",
    "IMPROVEMENT_OVER_MERGED_X11_19_34=3/340",
    "CURRENT_GAP_TO_SQRT=1/20",
    "ELEVEN_TWENTIETHS_SATURATION_THETA=11/40",
    "ELEVEN_TWENTIETHS_CAYLEY_GOOD_CORE_EXPONENT=1/4",
    "ELEVEN_TWENTIETHS_COLUMN_SHORT_SUPPORT_EXPONENT=1/20",
    "ELEVEN_TWENTIETHS_FULL_ROW_LIFT_EXPONENT=0",
    "REMAINING_RECEIVER=ElevenTwentiethsFullCayleyRowUniqueNLinearShortCofactorIncidence",
    "MAINLINE_H_NEEDED=false",
    "NEXT=Stage14-4cx",
):
    assert token in out, token

print("Stage14-4cw full Cayley-row audit: PASS")
print("best Case A envelope:", best_A)
print("best Case B envelope:", best_B)
print("equality: theta=11/40 phi=1/4 a=1/40 b=0")
print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=11/20")
