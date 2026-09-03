#!/usr/bin/env python3
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"
CERT = ROOT / "stages/stage35-ex/35ex-05/reduction-certificate.json"


def v2(n: int) -> int:
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def square(n: int) -> bool:
    s = isqrt(n)
    return s * s == n


state = json.loads(STATE.read_text())
cert = json.loads(CERT.read_text())

assert state["stage"] == "35-EX"
assert state["true_owner"]["kernel"] == "K16-C3-PESCH-EXPONENT-ONE"
assert state["true_owner"]["receiver"] == "R29-PESCH-E1"
assert state["stage35_main_firewall"]["stage35_ex_reopens_stage35_main"] is False

credit = cert["credit"]
for key in (
    "new_theorem_credit",
    "R29_PESCH_E1_closed",
    "R29_FIB2_closed",
    "J12_PARAMETRIC_closed",
    "stage35_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
):
    assert credit[key] is False

# Small fixed regression panel of genuine Master-Hits. This is not theorem evidence;
# the proof is the exact argument in 35ex-02. The panel guards implementation drift.
panel = [
    (4, 3, 16, 5),
    (5, 2, 8, 3),
    (6, 5, 8, 5),
    (9, 8, 6, 5),
    (11, 2, 8, 5),
    (13, 2, 17, 8),
]
seen_L = seen_R = False
for a, b, m, n in panel:
    assert gcd(a, b) == gcd(m, n) == 1
    assert (a - b) % 2 == (m - n) % 2 == 1
    U1, V1, W1 = a*a-b*b, 2*a*b, a*a+b*b
    U2, V2, W2 = m*m-n*n, 2*m*n, m*m+n*n
    assert U1*U1 + V1*V1 == W1*W1
    assert U2*U2 + V2*V2 == W2*W2

    M = (V1*U2)**2 + (U1*V2)**2
    assert square(M)

    c = gcd(U1, U2)
    p = gcd(W1, V2)
    q = gcd(V1, V2)
    g0 = gcd(W1*U2, U1*V2)
    h = gcd(V1*U2, U1*V2)

    assert g0 == c*p
    assert h == c*q
    assert gcd(c, p) == gcd(c, q) == gcd(p, q) == 1
    assert c % 2 == p % 2 == 1

    k1, k2 = v2(V1), v2(V2)
    assert k1 != k2
    A = (V1*U2)//h
    B = (U1*V2)//h
    assert gcd(A, B) == 1
    assert square(A*A + B*B)
    if k1 < k2:
        seen_L = True
        assert A % 2 == 1 and B % 2 == 0
    else:
        seen_R = True
        assert A % 2 == 0 and B % 2 == 1

assert seen_L and seen_R

# Exact algebraic regression for the additive factorizations used in 35ex-05.
for r, s, u, v in [(5, 2, 7, 4), (8, 3, 9, 2), (11, 4, 13, 6)]:
    lhs_minus = u*v*(r*r-s*s) - r*s*(u*u-v*v)
    rhs_minus = (r*u+s*v)*(r*v-s*u)
    lhs_plus = u*v*(r*r-s*s) + r*s*(u*u-v*v)
    rhs_plus = (r*u-s*v)*(r*v+s*u)
    assert lhs_minus == rhs_minus
    assert lhs_plus == rhs_plus

    lhs_R_minus = (r*r-s*s)*(u*u-v*v) - 4*r*s*u*v
    rhs_R_minus = (r*(u-v)-s*(u+v))*(r*(u+v)+s*(u-v))
    lhs_R_plus = (r*r-s*s)*(u*u-v*v) + 4*r*s*u*v
    rhs_R_plus = (r*(u-v)+s*(u+v))*(r*(u+v)-s*(u-v))
    assert lhs_R_minus == rhs_R_minus
    assert lhs_R_plus == rhs_R_plus

assert cert["arsenal_assessment"]["factor_square_shape_matched"] is True
assert cert["arsenal_assessment"]["exact_pairwise_gcd_support_complete"] is False
assert cert["arsenal_assessment"]["finite_exhaustive_squareclass_family_proved"] is False

print("PASS STAGE35_EX_REDUCTION_V1")
