#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4cs/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/five_eighths_boundary_split_summary.json"


def oddpart(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    while n % 2 == 0:
        n //= 2
    return n


def divisors(n: int):
    out = []
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


# 1. Exact rational ledger on a 1/192 mesh containing every named endpoint.
max_e = F(0)
saturation = []
for ti in range(0, 193):
    theta = F(ti, 192)
    if not (F(3, 16) <= theta <= F(5, 16)):
        continue
    for pi in range(0, 193):
        phi = F(pi, 192)
        if not (F(1, 8) <= phi <= F(1, 4)):
            continue
        if not (F(0) <= theta - phi <= F(1, 8)):
            continue
        if theta + phi < F(3, 8):
            continue
        e = max(2 * theta, 1 - 2 * theta)
        if e > max_e:
            max_e = e
            saturation = [(theta, phi)]
        elif e == max_e:
            saturation.append((theta, phi))

assert max_e == F(5, 8), max_e
for theta, phi in saturation:
    assert (
        (theta == F(5, 16) and F(3, 16) <= phi <= F(1, 4))
        or (theta == phi == F(3, 16))
    ), (theta, phi)
assert (F(3, 16), F(3, 16)) in saturation
assert (F(5, 16), F(3, 16)) in saturation
assert (F(5, 16), F(1, 4)) in saturation

# 2. Upper-edge exponent identities.
for pi in range(36, 49):
    phi = F(pi, 192)
    theta = F(5, 16)
    chi = 2 * theta + 2 * phi - F(3, 4)
    mu = 2 * theta - 2 * phi
    nu = F(1, 4) + 2 * phi - 2 * theta
    assert chi == 2 * phi - F(1, 8)
    assert mu == F(5, 8) - 2 * phi
    assert nu == 2 * phi - F(3, 8)
    assert 2 * phi - chi == F(1, 8)
    assert nu - chi == -F(1, 4)
    assert chi + mu + F(1, 8) == F(5, 8)
    assert max(F(0), chi - F(1, 4)) == max(F(0), 2 * phi - F(3, 8))

# 3. Lower-corner exponent identities.
theta = phi = F(3, 16)
chi = 2 * theta + 2 * phi - F(3, 4)
mu = 2 * theta - 2 * phi
nu = F(1, 4) + 2 * phi - 2 * theta
assert chi == 0
assert mu == 0
assert nu == F(1, 4)
assert 2 * phi - chi == F(3, 8)
assert F(3, 8) + F(1, 4) == F(5, 8)

# 4. Synthetic root-gcd identity under the reducedness consequences
# gcd(R,J)=gcd(R,Y)=gcd(J,X)=1 and same-state root coprimality.
root_checks = 0
for x1 in range(1, 8):
    for y1 in range(1, 8):
        if gcd(x1, y1) != 1:
            continue
        for x2 in range(1, 8):
            for y2 in range(1, 8):
                if gcd(x2, y2) != 1:
                    continue
                X = x1 * x2
                Y = y1 * y2
                for R in (1, 3, 5, 7, 11):
                    for J in (1, 3, 5, 7, 11):
                        if gcd(R, J) != 1:
                            continue
                        if gcd(R, Y) != 1 or gcd(J, X) != 1:
                            continue
                        P = R * X
                        Q = J * Y
                        assert oddpart(gcd(P, Q)) == oddpart(gcd(X, Y))
                        root_checks += 1
assert root_checks > 1000

# 5. Synthetic signed-quotient gcd identity.
quotient_checks = 0
for P in range(1, 60):
    for Q in range(P + 1, 70):
        plus = Q + P
        minus = Q - P
        for p in divisors(plus):
            for q in divisors(minus):
                if gcd(p, q) != 1:
                    continue
                if gcd(p * q, P * Q) != 1:
                    continue
                c = plus // p
                d = minus // q
                assert oddpart(gcd(c, d)) == oddpart(gcd(P, Q)), (P, Q, p, q, c, d)
                quotient_checks += 1
assert quotient_checks > 1000

# 6. Sequential Cayley bad-core peel always divides g_A^2*g_P^2.
peel_checks = 0
for C in range(1, 200, 2):
    for gA in range(1, 20):
        for gP in range(1, 20):
            a = gcd(C, gA * gA)
            C1 = C // a
            b = gcd(C1, gP * gP)
            Cstar = C1 // b
            Cbad = C // Cstar
            assert (gA * gA * gP * gP) % Cbad == 0
            peel_checks += 1
assert peel_checks > 10000

# 7. Frozen theorem-boundary tokens and JSON consistency.
text = RESULT.read_text()
required = [
    "STAGE14_4CS=COMPLETE_FIVE_EIGHTHS_PROMOTION_COMMON_GCD_ROOT_GCD_IDENTIFICATION_AND_TWO_BOUNDARY_SPLIT",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8",
    "IMPROVEMENT_OVER_PREVIOUS_2_3=1/24",
    "ODDPART_QUOTIENT_GCD_EQUALS_PQ_GCD=true",
    "ODDPART_PQ_GCD_EQUALS_XY_GCD=true",
    "H_SQUARED_DIVIDES_C_URES=true",
    "H_SQUARED_DIVIDES_X_TIMES_Y=true",
    "C_BAD_EXPONENT_MAX=1/4",
    "UPPER_RECEIVER=UpperFiveEighthsCayleyGaussianOuterSupportPrimitiveRootLineIncidence",
    "LOWER_RECEIVER=LowerFiveEighthsCoprimeRootProductTwoPrimitiveReciprocalFactorizationIncidence",
    "MAINLINE_H_NEEDED=false",
    "NEXT=Stage14-4ct",
]
for token in required:
    assert token in text, token

summary = json.loads(SUMMARY.read_text())
assert summary["current_physical_upper_bound_exponent"] == "5/8"
assert summary["improvement_over_previous_2_3"] == "1/24"
assert summary["five_eighths_saturation_components"] == 2
assert summary["mainline_H_needed"] is False
assert summary["next"] == "Stage14-4ct"

print("Stage14-4cs audit: PASS")
print(f"root_gcd_checks={root_checks}")
print(f"signed_quotient_checks={quotient_checks}")
print(f"bad_core_peel_checks={peel_checks}")
print("max_exponent=5/8")
