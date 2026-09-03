#!/usr/bin/env python3
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"
CERT05 = ROOT / "stages/stage35-ex/35ex-05/reduction-certificate.json"
CERT06 = ROOT / "stages/stage35-ex/35ex-06/gcd-squareclass-certificate.json"
CERT07 = ROOT / "stages/stage35-ex/35ex-07/moving-squareclass-certificate.json"
CERT08 = ROOT / "stages/stage35-ex/35ex-08/hypotenuse-bridge-certificate.json"
CERT09 = ROOT / "stages/stage35-ex/35ex-09/bridge-squareclass-certificate.json"


def v2(n: int) -> int:
    n = abs(n)
    k = 0
    while n and n % 2 == 0:
        n //= 2
        k += 1
    return k


def oddpart(n: int) -> int:
    n = abs(n)
    return n >> v2(n) if n else 0


def square(n: int) -> bool:
    s = isqrt(n)
    return s * s == n


state = json.loads(STATE.read_text())
cert05 = json.loads(CERT05.read_text())
cert06 = json.loads(CERT06.read_text())
cert07 = json.loads(CERT07.read_text())
cert08 = json.loads(CERT08.read_text())
cert09 = json.loads(CERT09.read_text())

assert state["stage"] == "35-EX"
assert state["true_owner"]["kernel"] == "K16-C3-PESCH-EXPONENT-ONE"
assert state["true_owner"]["receiver"] == "R29-PESCH-E1"
assert state["stage35_main_firewall"]["stage35_ex_reopens_stage35_main"] is False

for cert in (cert05, cert06, cert07, cert08, cert09):
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
    Eraw_norm = (W1*U2)**2 + (U1*V2)**2
    assert square(M)
    assert Eraw_norm - M == (U1*U2)**2

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

structural_tuples = [(5, 2, 7, 4), (8, 3, 9, 2), (11, 4, 13, 6), (9, 2, 7, 4)]
for r, s, u, v in structural_tuples:
    assert gcd(r, s) == gcd(u, v) == 1
    assert (r - s) % 2 == (u - v) % 2 == 1
    w, H = r*r+s*s, u*u+v*v
    rs, uv = r*s, u*v

    L1, L2 = r*u+s*v, r*v-s*u
    L3, L4 = r*u-s*v, r*v+s*u
    Gplus = gcd(w, H)
    Gminus = gcd(r*r-s*s, u*u-v*v)
    C13 = gcd(r, v)*gcd(s, u)
    C24 = gcd(r, u)*gcd(s, v)
    assert Gplus % gcd(L1, L2) == 0
    assert Gplus % gcd(L3, L4) == 0
    assert Gminus % gcd(L1, L4) == 0
    assert Gminus % gcd(L2, L3) == 0
    assert oddpart(gcd(L1, L3)) == oddpart(C13)
    assert oddpart(gcd(L2, L4)) == oddpart(C24)
    assert L1*L4 == uv*w + rs*H
    assert L2*L3 == uv*w - rs*H

    t = gcd(rs, uv)
    T_L = gcd(r*r-s*s, u*u-v*v)
    assert C13*C24 == t
    assert gcd(C13, C24) == 1
    assert gcd(t, T_L) == 1
    assert gcd(Gplus, t*T_L) == 1

    x, y = u-v, u+v
    assert x % 2 == y % 2 == 1 and gcd(x, y) == 1
    R1, R2 = r*x-s*y, r*y+s*x
    R3, R4 = r*x+s*y, r*y-s*x
    Hplus = gcd(w, x*x+y*y)
    Hminus = gcd(r*r-s*s, x*x-y*y)
    D13 = gcd(r, y)*gcd(s, x)
    D24 = gcd(r, x)*gcd(s, y)
    assert all(z % 2 for z in (R1, R2, R3, R4))
    assert Hplus % gcd(R1, R2) == 0
    assert Hplus % gcd(R3, R4) == 0
    assert abs(Hminus) % gcd(R1, R4) == 0
    assert abs(Hminus) % gcd(R2, R3) == 0
    assert gcd(R1, R3) == D13
    assert gcd(R2, R4) == D24
    assert R1*R4 == (u*u-v*v)*w - 2*rs*H
    assert R2*R3 == (u*u-v*v)*w + 2*rs*H

    j = gcd(rs, x*y)
    T_R = gcd(r*r-s*s, u*v)
    assert D13*D24 == j
    assert gcd(D13, D24) == 1
    assert gcd(j, T_R) == 1
    assert gcd(Hplus, j*T_R) == 1
    assert Hminus == T_R

for alpha, beta in [(2, 1), (4, 1), (5, 2), (8, 3), (9, 4)]:
    assert alpha > beta > 0
    assert gcd(alpha, beta) == 1
    assert (alpha-beta) % 2 == 1
    X = 2*alpha*beta
    Y = alpha*alpha-beta*beta
    Z = alpha*alpha+beta*beta
    assert X*X + Y*Y == Z*Z
    assert gcd(X, Y) == 1
    assert Z-X == (alpha-beta)**2
    assert Z+X == (alpha+beta)**2
    assert gcd(alpha-beta, alpha+beta) == 1

for r, s, u, v, e_u in [(8, 3, 6, 5, 1), (8, 3, 5, 2, 1)]:
    assert gcd(r, s) == gcd(u, v) == 1
    assert v2(r*s) > v2(u*v) == e_u
    L = (r*u+s*v, r*v-s*u, r*u-s*v, r*v+s*u)
    vals = [v2(z) for z in L]
    assert vals in ([0, e_u, 0, e_u], [e_u, 0, e_u, 0])
    assert sum(vals) == 2*e_u

for ell in (3, 5, 7, 11, 13):
    r, s, u, v = ell-1, 1, ell+1, 1
    assert gcd(r, s) == gcd(u, v) == 1
    assert (r-s) % 2 == (u-v) % 2 == 1
    L1, L4 = r*u+s*v, r*v+s*u
    assert L1 == ell*ell
    assert L4 == 2*ell
    assert gcd(L1, L4) == ell
    assert gcd(r*r-s*s, u*u-v*v) == ell

assert cert05["arsenal_assessment"]["factor_square_shape_matched"] is True
assert cert05["arsenal_assessment"]["finite_exhaustive_squareclass_family_proved"] is False

check = cert06["s34_w01_contract_check"]
assert check["factorization_hypothesis"] is True
assert check["pairwise_gcd_support_derived"] is True
assert check["sign_and_two_adic_bookkeeping"] is True
assert check["finite_shared_prime_support_proved"] is False
assert check["finite_exhaustive_squareclass_family_proved"] is False
assert check["direct_stage34_branch_transfer_allowed"] is False

arsenal07 = cert07["arsenal_decision"]
assert arsenal07["dynamic_reservoirs_collapsed"] is True
assert arsenal07["fixed_finite_squareclass_support_proved"] is False
assert arsenal07["finite_enumeration_authorized"] is False

bridge = cert08["primitive_bridge"]
assert cert08["bridge_identity"] == "(q*H)^2 + (U1*U2/c)^2 = (p*w)^2"
assert bridge["gcd_X_Y"] == 1
assert bridge["alpha_beta_coprime_opposite_parity"] is True
assert cert08["assessment"]["third_primitive_parameter_pair_forced"] is True
assert cert08["assessment"]["size_decreasing_counterexample_map_proved"] is False

assert cert09["branch_L"]["pairwise_coprime"] is True
assert cert09["branch_R"]["pairwise_coprime"] is True
assert cert09["common_hypotenuse_refinement"]["common_hypotenuse_primes_outside_e_individually_squareclass_neutral"] is True
assert cert09["arsenal_decision"]["S34_W01_factorwise_support_complete"] is True
assert cert09["arsenal_decision"]["fixed_finite_squareclass_family_proved"] is False
assert cert09["arsenal_decision"]["finite_enumeration_authorized"] is False
assert cert09["descent"]["size_decreasing_admissible_counterexample_map_proved"] is False
assert cert09["next_exact_leaf"] == "35EX-10_BRIDGE_DESCENT_MAP_OR_SPLIT_PRIME_OBSTRUCTION"

print("PASS STAGE35_EX_REDUCTION_V5_THREE_RESERVOIR_GRAPH")
