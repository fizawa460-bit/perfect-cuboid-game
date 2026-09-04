#!/usr/bin/env python3
import json
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage35-ex/35ex-10/split-prime-certificate.json"
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"


def v2(n: int) -> int:
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def factor(n: int):
    n = abs(n)
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def legendre(a: int, ell: int) -> int:
    a %= ell
    assert a != 0
    z = pow(a, (ell - 1) // 2, ell)
    return 1 if z == 1 else -1


cert = json.loads(CERT.read_text())
state = json.loads(STATE.read_text())

assert cert["status"] == "PROVISIONAL_EXACT_CONDITIONAL_REDUCTION_NO_PROMOTION"
assert cert["audited_parent_head"] == "3642810596eb1aa6e58a59fd6805e872b2ac8bc1"
assert cert["bridge_descent_test"]["bridge_is_genuine_primitive_euclid_triple"] is True
assert cert["bridge_descent_test"]["both_obligations_inherited_from_parent_system"] is False
assert cert["bridge_descent_test"]["new_successor_gcd_adapter_proved"] is False
assert cert["bridge_descent_test"]["uniform_height_decrease_proved"] is False
assert cert["bridge_descent_test"]["infinite_descent_proved"] is False
assert cert["split_prime_obstruction"]["source_only_kill_predicate_proved"] is True
assert cert["split_prime_obstruction"]["universal_bad_split_prime_existence_proved"] is False
assert cert["split_prime_obstruction"]["global_E1_proved"] is False

for key in (
    "new_theorem_credit",
    "R29_PESCH_E1_closed",
    "R29_FIB2_closed",
    "J12_PARAMETRIC_closed",
    "stage35_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
):
    assert cert["credit"][key] is False

# Genuine Master-Hit regression panel inherited from the Stage35-EX aggregate.
# The general Legendre-symbol proof is in split-prime-obstruction.md; this panel
# only guards the source-only implementation and is not global theorem evidence.
panel = [
    (4, 3, 16, 5),
    (5, 2, 8, 3),
    (6, 5, 8, 5),
    (9, 8, 6, 5),
    (11, 2, 8, 5),
    (13, 2, 17, 8),
]

hits = []
for a, b, m, n in panel:
    U1, V1, W1 = a*a-b*b, 2*a*b, a*a+b*b
    U2, V2, W2 = m*m-n*n, 2*m*n, m*m+n*n
    assert gcd(a, b) == gcd(m, n) == 1
    assert (a-b) % 2 == (m-n) % 2 == 1

    c = gcd(U1, U2)
    p = gcd(W1, V2)
    q = gcd(V1, V2)
    D = U1 // c
    T = U2 // c
    K = (W1 // p) * (V1 // q)
    k1, k2 = v2(V1), v2(V2)
    assert k1 != k2

    if k1 < k2:
        cross = D * V2 // (2 * p * q)
        for ell in factor(cross):
            if ell % 4 == 1:
                assert K % ell != 0
                if legendre(K, ell) == -1:
                    hits.append(((a,b,m,n), "L", "t", ell))
        for ell in factor(T):
            if ell % 4 == 1:
                assert (p*q) % ell != 0
                if legendre(p*q, ell) == -1:
                    hits.append(((a,b,m,n), "L", "T", ell))
    else:
        cross = D * V2 // (p * q)
        for ell in factor(cross):
            if ell % 4 == 1:
                assert (2*K) % ell != 0
                if legendre(2*K, ell) == -1:
                    hits.append(((a,b,m,n), "R", "j", ell))
        for ell in factor(T):
            if ell % 4 == 1:
                assert (2*p*q) % ell != 0
                if legendre(2*p*q, ell) == -1:
                    hits.append(((a,b,m,n), "R", "T", ell))

assert ((6,5,8,5), "L", "T", 13) in hits
assert ((13,2,17,8), "L", "t", 17) in hits
assert len(hits) == 2

# Local finite-field regression of the split-prime sign argument. For ell=1 mod4,
# +/-1 is a square, so the orientation sign cannot rescue a nonresidue coefficient.
for ell in (5, 13, 17, 29, 37):
    assert ell % 4 == 1
    assert legendre(-1, ell) == 1

assert state["stage"] == "35-EX"
assert state["stage35_main_firewall"]["stage35_ex_reopens_stage35_main"] is False

print("PASS STAGE35_EX_10_SPLIT_PRIME_OBSTRUCTION_V1")
