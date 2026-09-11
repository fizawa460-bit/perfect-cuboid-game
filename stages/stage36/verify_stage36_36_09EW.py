#!/usr/bin/env python3
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def blob(rel):
    return subprocess.check_output(["git", "hash-object", str(ROOT / rel)], text=True).strip()


def load(rel):
    return json.loads((ROOT / rel).read_text())


def is_prime(n):
    if n < 2:
        return False
    small = (2,3,5,7,11,13,17,19,23,29,31,37)
    for p in small:
        if n == p:
            return True
        if n % p == 0:
            return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n-1):
            continue
        for _ in range(s-1):
            x = (x*x) % n
            if x == n-1:
                break
        else:
            return False
    return True


def legendre(a, p):
    a %= p
    assert a != 0
    x = pow(a, (p-1)//2, p)
    assert x in (1, p-1)
    return 1 if x == 1 else -1


def bit(x):
    assert x in (-1,1)
    return 0 if x == 1 else 1


def rank_f2(M):
    A = [row[:] for row in M]
    r = 0
    for c in range(len(A[0])):
        pivot = next((i for i in range(r, len(A)) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        for i in range(len(A)):
            if i != r and A[i][c]:
                A[i] = [x ^ y for x,y in zip(A[i], A[r])]
        r += 1
    return r


def psi3_coeffs(a, b):
    N = a*a - b*b
    M = a*a + b*b
    d = a*b
    return [
        -64*N*N*d*d*(M**4 + 4*N*N*d*d),
        -192*N*N*d*d*M*M,
        -96*N*N*d*d,
        4*M*M,
        3,
    ]


def has_root_mod(coeffs, q):
    for x in range(q):
        y = 0
        for c in reversed(coeffs):
            y = (y*x + c) % q
        if y == 0:
            return True
    return False

EU = "stages/stage36/36-09EU/rho-t6-profile-legendre-rigidity-preflight.json"
EV = "stages/stage36/36-09EV/rho-t6-profile-rank3-realization-preflight.json"
EH = "stages/stage36/36-09EH/rho-fixed-p-rankzero-torsion-criterion-preflight.json"
EK = "stages/stage36/36-09EK/rho-sel2-literal-orbit-closure-preflight.json"
SOURCE = "stages/stage36/36-09EW/rho-t6-profile-parametric-realization-source-lock.md"
CERT = "stages/stage36/36-09EW/rho-t6-profile-parametric-realization-preflight.json"

expected = {
    EU: "0507f5a19cc3baf44553e7b9bdd0e689bd5ec5d7",
    EV: "c5067f43b6217d7faebc23c9921895d5f53e3dbf",
    EH: "d95bf71f3cbed1d3fd12eaa0d235d2aa83539d37",
    EK: "f6af11a0f7fd8a303531b2a587b7446c382a84c5",
    SOURCE: "b92ef93224cdb22a47dd8cdda001e306e57b291f",
    CERT: "dce14a68463c8c95d33c3397a79fd120a8b064dd",
}
for path, sha in expected.items():
    assert blob(path) == sha, (path, blob(path), sha)

cert = load(CERT)
eu = load(EU)
eh = load(EH)
ek = load(EK)

assert cert["entry_authority"]["v278_exact_head"] == "4d24772fbb03edcc1ac7e45d39dc7cd437914b66"
assert cert["entry_authority"]["v278_exact_head_ci"] == "34408388995/102656758007"
assert eu["pfaffian_rank_theorem"]["sel2_dimension_2_iff_B_rank_3"] is True
assert eh["rational_4torsion_test"]["order4_iff"] == "8h in Q^2 or -8h in Q^2"
assert ek["literal_orbit_theorem"]["positive_literal_orbit_complete"] is True

K = 729
MOD = 11480
REP = 6147
assert REP % 8 == 3
assert REP % 7 == 1
assert REP % 41 == 38
assert REP % 5 == 2
assert MOD == 8*5*7*41
assert (8*(REP % 7)**2 - (K % 7)**2) % 7 == 0
assert (8*(REP % 41)**2 + 8*(K % 41)*(REP % 41) + (K % 41)**2) % 41 == 0

r7 = REP % 7
r41 = REP % 41
fixed_B = [
    [bit(-legendre(7,3)), bit(legendre(41,3)), bit(-legendre(41,3))],
    [bit(legendre(r7,7)), bit(legendre(r41,41)), bit(legendre(r41,41))],
    [bit(-legendre((4*r7+K)%7,7)), bit(legendre((4*r41+K)%41,41)), bit(-legendre((4*r41+K)%41,41))],
    [bit(-legendre((2*r7+K)%7,7)), bit(legendre((2*r41+K)%41,41)), bit(-legendre((2*r41+K)%41,41))],
]
assert fixed_B == [[1,1,0],[0,1,1],[0,0,1],[0,1,0]], fixed_B
assert rank_f2(fixed_B) == 3
assert cert["forced_legendre_rank"]["B"] == fixed_B
assert cert["forced_legendre_rank"]["rank_F2"] == 3
assert cert["forced_legendre_rank"]["EU_implied_sel2_dimension"] == 2

a5 = (2*(REP % 5)) % 5
b5 = (2*(REP % 5) + K) % 5
assert (a5,b5) == (4,3)
coeff5 = [c % 5 for c in psi3_coeffs(a5,b5)]
assert coeff5 == [4,0,4,0,3], coeff5
assert not has_root_mod(coeff5,5)
assert [sum(c*pow(x,i,5) for i,c in enumerate(coeff5)) % 5 for x in range(5)] == [4,1,3,3,1]

def hit(u):
    if u <= 258 or u % MOD != REP:
        return False
    vals = [u, 2*u+K, 4*u+K]
    if not all(is_prime(x) for x in vals):
        return False
    P = 8*u*u-K*K
    Qabs = 8*u*u+8*K*u+K*K
    if P % 7 or Qabs % 41:
        return False
    s = P//7
    t = Qabs//41
    return is_prime(s) and is_prime(t)

hits = [u for u in range(REP, 1601867+1, MOD) if hit(u)]
assert len(range(REP, 1601867+1, MOD)) == 140
assert hits == [1601867], hits

u = hits[0]
a = 2*u
b = 2*u+K
q = 4*u+K
P = 8*u*u-K*K
Qabs = 8*u*u+8*K*u+K*K
s = P//7
t = Qabs//41
assert math.gcd(a,b) == 1
assert all(is_prime(x) for x in (u,b,q,s,t))
assert (u%8,b%8,q%8,s%8,7%8,41%8,t%8) == (3,7,5,1,7,1,1)
assert P == 7*s
assert Qabs == 41*t
N = a*a-b*b
d = a*b
D = 8*N*d
assert N == -K*q
assert d == 2*u*b
assert D == -(2**4)*(3**6)*u*b*q
assert D == -383676395401189735185168

Drows = [3,u,q,b]
cols = [s,41,t]
direct_B = [[bit(legendre(c,p)) for c in cols] for p in Drows]
assert direct_B == fixed_B
assert rank_f2(direct_B) == 3

absD = abs(D)
r = math.isqrt(absD)
assert r*r != absD
coeffs = psi3_coeffs(a,b)
assert [c%5 for c in coeffs] == [4,0,4,0,3]
assert not has_root_mod(coeffs,5)

orbit = [Fraction(a,b), Fraction(b,a), Fraction(K,q), Fraction(q,K)]
assert [f"{x.numerator}/{x.denominator}" for x in orbit] == cert["new_exact_realization"]["literal_orbit"]
assert len(set(orbit)) == 4

real = cert["new_exact_realization"]
assert real["u"] == u
assert real["a"] == a and real["b"] == b
assert real["P"] == P and real["Q"] == -Qabs and real["D"] == D
assert real["direct_B"] == direct_B and real["direct_B_rank"] == 3
assert real["plus_minus_8Nd_both_nonsquare"] is True
assert real["psi3_witness_prime"] == 5

impact = cert["registry_impact"]
assert impact["previous_exact_fixed_parameter_count"] == 40
assert impact["new_exact_orbit_parameter_count"] == 4
assert impact["provisional_expanded_registry_count"] == 44

assert cert["conditional_prime_tuple"]["infinitely_many_hits_proved"] is False
assert cert["route_result"]["next_leaf"] == "36-09EX_RHO_T6_CONTROLLED_RADICAL_RELAXATION_PREFLIGHT"
assert cert["route_result"]["next_leaf_entry_allowed"] is False
for key,val in cert["scope_firewalls"].items():
    assert val is False, (key,val)

print("36-09EW verified: CRT family fixes the T6 profile/rank-3 B and EH screens conditional on five prime values; bounded progression replay finds u=1601867, giving one new four-point orbit provisionally. No infinitude/parent receiver/endpoint credit.")
