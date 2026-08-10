#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def require(path: str, token: str) -> None:
    text = (ROOT / path).read_text()
    assert token in text, (path, token)


# Canonical predecessor locks.
require(
    "stages/stage14/14-4cx/result.md",
    "STAGE14_4CX=COMPLETE_CAYLEY_ANNULUS_COLLAPSE_FULL_LOST_CORE_COLUMN_DIVISOR_AND_23_44_PROMOTION",
)
require(
    "stages/stage14/14-4cx/result.md",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44",
)
require(
    "stages/stage14/14-4cx/result.md",
    "CAYLEY_GOOD_CORE_COPRIME_TO_CROSS_ROOT_GCD=true",
)
require(
    "stages/stage14/14-s7-39/result.md",
    "CAYLEY_GOOD_CORE_COPRIME_TO_COMMON_ROOT_GCD=true",
)
require(
    "stages/stage14/14-s7-39/result.md",
    "JOINT_CORE_EQUALS_CAYLEY_GOOD_CORE_AT_FIXED_POWER=true",
)
require(
    "stages/stage14/14-s7-31/result.md",
    "OPPOSITE_SIGNED_QUOTIENT_PAIR_EXPONENT=max(0,nu-chi)",
)


# Exact cancellation regression: if H is a unit modulo a Cayley factor, then
# C | H^2*(A) iff C | A.  Test both row signs on many small packets.
def check_row_square_cancellation() -> None:
    for H in range(1, 18, 2):
        H2 = H * H
        for cm in range(1, 18, 2):
            if gcd(cm, H) != 1:
                continue
            for cp in range(1, 18, 2):
                if gcd(cp, H) != 1 or gcd(cm, cp) != 1:
                    continue
                for MH in range(1, 12):
                    for NH in range(1, 12):
                        M = H2 * MH
                        N = H2 * NH
                        assert ((M - N) % cm == 0) == ((MH - NH) % cm == 0)
                        assert ((M + N) % cp == 0) == ((MH + NH) % cp == 0)


check_row_square_cancellation()


# Column regression: the same H divides each post-J column cofactor when J is
# coprime to H, hence H^2 is removable from the cofactor product.
def check_column_square_removal() -> None:
    for H in range(1, 18, 2):
        for jm in range(1, 14, 2):
            if gcd(jm, H) != 1:
                continue
            for jp in range(1, 14, 2):
                if gcd(jp, H) != 1 or gcd(jm, jp) != 1:
                    continue
                for hm0 in range(1, 8):
                    for hp0 in range(1, 8):
                        Lm = jm * H * hm0
                        Lp = jp * H * hp0
                        hm = Lm // jm
                        hp = Lp // jp
                        assert hm % H == 0 and hp % H == 0
                        assert (hm * hp) // (H * H) == hm0 * hp0


check_column_square_removal()


def strip_ok(theta: F, phi: F) -> bool:
    return (
        F(3, 16) <= theta <= F(5, 16)
        and F(1, 8) <= phi <= F(1, 4)
        and 0 <= theta - phi <= F(1, 8)
        and theta + phi >= F(3, 8)
    )


def E_s(theta: F) -> F:
    return max(2 * theta, 1 - 2 * theta)


def E_k(theta: F) -> F:
    return 3 * theta - F(1, 4)


def E_H0(phi: F) -> F:
    # s=0 upper envelope.  Positive s is strictly better.
    return 3 * phi - F(1, 8)


def E_R2(theta: F, phi: F) -> F:
    chi = 2 * theta + 2 * phi - F(3, 4)
    assert chi <= F(1, 4)
    return 2 * phi + 2 * (F(1, 4) - chi)


# Exact equality arithmetic.
theta = F(23, 88)
phi = F(19, 88)
chi = 2 * theta + 2 * phi - F(3, 4)
mu = 2 * theta - 2 * phi
nu = F(1, 4) + 2 * phi - 2 * theta
short = F(1, 4) - chi

assert chi == F(9, 44)
assert mu == F(1, 11)
assert nu == F(7, 44)
assert nu - chi == -F(1, 22)
assert short == F(1, 22)
assert 2 * phi == F(19, 44)
assert E_s(theta) == F(23, 44)
assert E_H0(phi) == F(23, 44)
assert E_R2(theta, phi) == F(23, 44)
assert F(23, 44) - F(1, 2) == F(1, 44)


# Exact rational whole-strip audit.  1408 is divisible by 88 and 16.
D = 1408
best = (F(-1), None)
points_at_best = []
for nt in range(3 * D // 16, 5 * D // 16 + 1):
    t = F(nt, D)
    for np in range(D // 8, D // 4 + 1):
        p = F(np, D)
        if not strip_ok(t, p):
            continue
        c = 2 * t + 2 * p - F(3, 4)
        if c > F(1, 4):
            # 4cx proves the fixed-power high-core nonproportional branch empty.
            continue
        e = min(E_s(t), E_k(t), E_H0(p), E_R2(t, p))
        if e > best[0]:
            best = (e, (t, p))
            points_at_best = [(t, p)]
        elif e == best[0]:
            points_at_best.append((t, p))

assert best == (F(23, 44), (F(23, 88), F(19, 88))), best
assert points_at_best == [(F(23, 88), F(19, 88))], points_at_best


# A positive cross-root exponent makes E_H strictly smaller at the unique
# theta/phi point, so equality forces s=0.
for ns in range(1, 20):
    s = F(ns, 1408)
    assert 3 * phi - F(1, 8) - 3 * s < F(23, 44)


out = (ROOT / "stages/stage14/14-4cy/result.md").read_text()
for token in (
    "STAGE14_4CY=COMPLETE_CROSS_ROOT_SQUARE_ROW_REDUCTION_AND_UNIQUE_23_44_SATURATION",
    "CROSS_ROOT_SQUARE_DIVIDES_CAYLEY_NUMERATOR=true",
    "CROSS_ROOT_SQUARE_DIVIDES_SIGNED_QUOTIENT_PRODUCT=true",
    "CAYLEY_ROW_DESCENDS_AFTER_CROSS_ROOT_SQUARE_DIVISION=true",
    "CROSS_ROOT_SQUARE_REMOVED_FROM_COLUMN_SUPPORT=true",
    "CROSS_ROOT_SQUARE_REMOVED_FROM_ROW_SUPPORT=true",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44",
    "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
    "TWENTYTHREE_44_SATURATION_SEGMENT_COLLAPSED_TO_POINT=true",
    "TWENTYTHREE_44_UNIQUE_SATURATION_THETA=23/88",
    "TWENTYTHREE_44_UNIQUE_SATURATION_PHI=19/88",
    "TWENTYTHREE_44_TOTAL_CROSS_ROOT_EXPONENT=0",
    "TWENTYTHREE_44_COLUMN_RESIDUAL_EXPONENT=1/22",
    "TWENTYTHREE_44_REDUCED_ROW_LIFT_EXPONENT=1/22",
    "TWENTYTHREE_44_OPPOSITE_SIGNED_QUOTIENT_PAIR_EXPONENT=0",
    "REMAINING_RECEIVER=TwentyThreeFortyFourthsCrossRootFreeEqualCoreTwinOneTwentySecondLiftIncidence",
    "MAINLINE_H_NEEDED=false",
    "NEXT=Stage14-4cz",
):
    assert token in out, token

print("Stage14-4cy cross-root-square row reduction audit: PASS")
print("whole-strip maximum:", best)
print("unique equality: theta=23/88 phi=19/88 chi=9/44 s=0")
print("remaining short supports: column=1/22 row=1/22")
print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44")
