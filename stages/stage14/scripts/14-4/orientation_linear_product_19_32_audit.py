#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def require(path: str, token: str) -> None:
    assert token in (ROOT / path).read_text(), (path, token)


# Merged predecessor locks, including latest-main X10 compatibility.
require("stages/stage14/14-4ct/result.md", "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8")
require("stages/stage14/14-s7-32/result.md", "UNIQUE_FIVE_EIGHTHS_SATURATION=(theta,phi)=(5/16,1/4)")
require("stages/stage14/14-4cs/result.md", "ODDPART_H_EQUALS_ODDPART_GCD_XY=true")
require("stages/stage14/14-4cr/result.md", "CAYLEY_SIGN_ALLOCATION_EQUALS_GAUSSIAN_RELATIVE_ORIENTATION=true")
require("stages/stage14/14-X10/result.md", "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8")

# Cross-root gcd split and matched raw-host square divisibility.
root_packets = 0
for x1 in range(1, 11):
    for y1 in range(1, 11):
        if gcd(x1, y1) != 1:
            continue
        for x2 in range(1, 11):
            for y2 in range(1, 11):
                if gcd(x2, y2) != 1:
                    continue
                H = oddpart(gcd(x1 * x2, y1 * y2))
                HS = oddpart(gcd(x2, y1))
                HT = oddpart(gcd(x1, y2))
                assert H == HS * HT
                assert gcd(HS, HT) == 1
                R, J, om1, om2 = 7, 11, 3, 5
                AS, BS = R * x2 * x2 * om1, J * y1 * y1 * om2
                AT, BT = J * y2 * y2 * om1, R * x1 * x1 * om2
                assert gcd(AS, BS) % (HS * HS) == 0
                assert gcd(AT, BT) % (HT * HT) == 0
                root_packets += 1

# Exact determinant identities producing L-/L+ on S and T hosts.
linear_checks = 0
for x1 in range(1, 7):
    for y1 in range(1, 7):
        if gcd(x1, y1) != 1:
            continue
        for x2 in range(1, 7):
            for y2 in range(1, 7):
                if gcd(x2, y2) != 1:
                    continue
                for g1 in (1, 2):
                    for g2 in (1, 2):
                        z1 = 2 * x1 * y1 // g1
                        z2 = 2 * x2 * y2 // g2
                        r1, s1, r2, s2 = 1, 3, 5, 7
                        om1, om2 = g1 * r1 * s1, g2 * r2 * s2
                        R, J = 11, 13
                        P, Q = R * x1 * x2, J * y1 * y2
                        Lm = z1 * r2 * s2 - z2 * r1 * s1
                        Lp = z1 * r2 * s2 + z2 * r1 * s1

                        AT, BT = J * y2 * y2 * om1, R * x1 * x1 * om2
                        assert 2 * (BT * Q - AT * P) == R * J * x1 * y2 * g1 * g2 * Lm
                        assert 2 * (BT * Q + AT * P) == R * J * x1 * y2 * g1 * g2 * Lp

                        AS, BS = R * x2 * x2 * om1, J * y1 * y1 * om2
                        assert 2 * (BS * P - AS * Q) == R * J * x2 * y1 * g1 * g2 * Lm
                        assert 2 * (BS * P + AS * Q) == R * J * x2 * y1 * g1 * g2 * Lp
                        linear_checks += 1

# Primitive sqrt(-1) roots have only same/opposite relative orientation.
rootline_checks = 0
for q in (5, 13, 17, 25, 29):
    for A in range(1, q):
        if gcd(A, q) != 1:
            continue
        for B in range(1, q):
            if gcd(B, q) != 1 or (A * A + B * B) % q:
                continue
            for Q in range(1, q):
                if gcd(Q, q) != 1:
                    continue
                for P in range(1, q):
                    if gcd(P, q) != 1 or (P * P + Q * Q) % q:
                        continue
                    assert ((B * Q - A * P) * (B * Q + A * P)) % q == 0
                    rootline_checks += 1

# Proportional equality gives a large full common coordinate divisor.
prop_checks = 0
for a, b in ((1, 1), (1, 3), (3, 5), (5, 7)):
    if gcd(a, b) != 1:
        continue
    for t in (3, 8, 25, 64):
        z1, z2 = a * t, b * t
        assert z1 * b == z2 * a
        A = 11 * b * b * z1
        B = 13 * a * a * z2
        assert gcd(A, B) % t == 0
        prop_checks += 1

# Exact rational minimax.  Denominator 384 contains 19/64 and all strip endpoints.
D = 384
max_nonprop = (F(-1), None)
for nt in range(3 * D // 16, 5 * D // 16 + 1):
    theta = F(nt, D)
    for np in range(D // 8, D // 4 + 1):
        phi = F(np, D)
        if theta < phi or theta - phi > F(1, 8) or theta + phi < F(3, 8):
            continue
        Es = max(2 * theta, 1 - 2 * theta)
        Ek = 3 * theta - F(1, 4)
        Ex = 3 * phi - F(1, 8)
        chi = 2 * theta + 2 * phi - F(3, 4)
        if theta + phi > F(1, 2):
            Ex -= (chi - F(1, 4)) / 3
        E = min(Es, Ek, Ex)
        if E > max_nonprop[0]:
            max_nonprop = (E, (theta, phi, chi))

assert max_nonprop == (F(19, 32), (F(19, 64), F(1, 4), F(11, 32))), max_nonprop
rho = (F(11, 32) - F(1, 4)) / 3
assert rho == F(1, 32)
assert F(11, 32) - 3 * rho == F(1, 4)
assert F(5, 8) - F(19, 32) == F(1, 32)
assert 3 * F(5, 16) - F(3, 8) == F(9, 16)
assert F(9, 16) < F(19, 32)

# Freeze new theorem boundary.
result = (ROOT / "stages/stage14/14-4cu/result.md").read_text()
for token in (
    "STAGE14_4CU=COMPLETE_RESIDUAL_CAYLEY_ORIENTATION_LINEAR_PRODUCT_TRANSFER_AND_19_32_PROMOTION",
    "MERGED_X10_COMPATIBILITY_CHECKED=true",
    "JOINT_CORE_DIVIDES_ENDPOINT_LINEAR_PRODUCT=true",
    "THREE_GAUSSIAN_ROOT_ORIENTATION_ENTROPY_RANK=2",
    "NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/32",
    "PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/32",
    "IMPROVEMENT_OVER_PREVIOUS_5_8=1/32",
    "NINETEEN_THIRTYSECONDS_SATURATION_THETA=19/64",
    "NINETEEN_THIRTYSECONDS_SATURATION_PHI=1/4",
    "REMAINING_RECEIVER=NineteenThirtySecondsJointCoreCayleyResidualLinearProductIncidence",
    "MAINLINE_H_NEEDED=false",
    "NEXT=Stage14-4cv",
):
    assert token in result, token

print("Stage14-4cu audit: PASS")
print("cross-root packets:", root_packets)
print("linear identities:", linear_checks)
print("root-line checks:", rootline_checks)
print("proportional checks:", prop_checks)
print("max nonproportional:", max_nonprop)
