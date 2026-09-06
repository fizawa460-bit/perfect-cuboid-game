#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09R" / "etau-rankjump-receiver-esigmatau-growth-preflight.json"
O_CERT = ROOT / "stages" / "stage36" / "36-09O" / "physical-square-lift-v4-quotient-preflight.json"
P_CERT = ROOT / "stages" / "stage36" / "36-09P" / "etau-generic-mw-zero-exceptional-growth-preflight.json"
Q_CERT = ROOT / "stages" / "stage36" / "36-09Q" / "etau-torsion-growth-stage14-second-basechange-preflight.json"
SOURCE = ROOT / "stages" / "stage36" / "36-09N" / "relative-2isogeny-specialization-source-lock.md"
W03 = ROOT / "docs" / "arsenal" / "cards" / "formal" / "S34-W03.md"

BASE = "69ac6635fb7a7808bca7aad72c5b7e61bcb5cbb6"
V47_BLOB = "0340f31e0378138830df9e02f77a69ec54446c1f"
CERT_BLOB = "265edaa03a4fac77de4206f2a31d0b8e439451bd"
O_BLOB = "6a2678ebedba40e13277100441361039ee47ca28"
P_BLOB = "a611b698fccfbd29a971ccede5c77b6832101c77"
Q_BLOB = "36b24b1a42231ccfec9364df6a8d52af13ceb6de"
SOURCE_BLOB = "a562d7053a6f04deff4473067777b7cfd538ea8a"
W03_BLOB = "1d5275321f42768a6414d4610ac912c63be43f96"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def is_square_int(n: int) -> bool:
    if n < 0:
        return False
    r = math.isqrt(n)
    return r*r == n


def is_square_fraction(q: Fraction) -> bool:
    return q >= 0 and is_square_int(q.numerator) and is_square_int(q.denominator)


def local_quartic_has_point(d: int, a: int, b2: int, prime: int) -> bool:
    squares = {y*y % prime for y in range(prime)}
    for M in range(prime):
        for e in range(prime):
            if M == 0 and e == 0:
                continue
            rhs = (d*pow(M,4,prime) + a*(M*M % prime)*(e*e % prime) + b2*pow(e,4,prime)) % prime
            if rhs in squares:
                return True
    return False


def point_count(prime: int) -> int:
    square_count = [0]*prime
    for y in range(prime):
        square_count[y*y % prime] += 1
    total = 1
    for x in range(prime):
        rhs = x*(x-49)*(x-289) % prime
        total += square_count[rhs]
    return total


def adapter_identities() -> None:
    for p0 in [-6,-5,-4,-3,-2,2,3,4,5,6]:
        p = Fraction(p0)
        h = p - 1/p
        r = p + 1/p
        D = p*(p*p-1)
        Nm = p*p-2*p-1
        Np = p*p+2*p-1
        a = r*r
        b = 4*r*r/(h*h)
        B = 2*r*r/h
        L = D/(p*p+1)
        assert B*B == a*b
        assert L*r*(h-2)/h == Nm
        assert L*r*(h+2)/h == Np
        assert Np*Np-Nm*Nm == 8*D
        for z in [Fraction(2), Fraction(3,2), Fraction(-2), Fraction(5,3)]:
            S2 = (2*B*z+a+b)/(z*z-1)
            X = 2*B*z
            U = X+a+b
            w2 = S2*(z*z-1)**2
            Y2 = (2*B)**2*w2
            assert Y2 == U*(U-(r-2*r/h)**2)*(U-(r+2*r/h)**2)
            xx = L*L*U
            yy2 = L**6*Y2
            assert yy2 == xx*(xx-Nm*Nm)*(xx-Np*Np)


def receiver_stage14_identity() -> None:
    for t in [Fraction(2,3), Fraction(-3,5), Fraction(5,7)]:
        for X in [Fraction(2), Fraction(3,2), Fraction(-1), Fraction(7,3)]:
            if X + t*t == 0:
                continue
            R2 = 4*X*(X-1)/(X+t*t)
            assert R2-4 == 4*(X*X-2*X-t*t)/(X+t*t)
            assert (X-1)**2-(1+t*t) == X*X-2*X-t*t


def specialization_injectivity_check() -> None:
    p = Fraction(3,2)
    basic = [p, p-1, p+1]
    seen=[]
    for k in range(1,4):
        for inds in combinations(range(3), k):
            q=Fraction(1)
            for i in inds:
                q *= basic[i]
            assert not is_square_fraction(q)
            seen.append(q)
    expected = {Fraction(3,2), Fraction(1,2), Fraction(5,2), Fraction(3,4), Fraction(15,4), Fraction(5,4), Fraction(15,8)}
    assert set(seen) == expected


def descent_check() -> None:
    a=-338; b=14161
    assert b == 119**2
    for d in [-1,-7,-17,-119]:
        assert d < 0 and a < 0 and b//d < 0
    assert not local_quartic_has_point(7,a,b//7,5)
    assert not local_quartic_has_point(17,a,b//17,3)
    assert not local_quartic_has_point(119,a,b//119,3)

    ap=676; bp=57600
    assert bp == 240**2
    realized={1:(0,1,240), -1:(10,1,0), 15:(4,1,136), -15:(4,1,56)}
    for d,(M,e,N) in realized.items():
        assert N*N == d*M**4 + ap*M*M*e*e + (bp//d)*e**4
    for d in [3,-3,5,-5,6,-6,10,-10]:
        assert not local_quartic_has_point(d,ap,bp//d,17)

    for M in [1,3]:
        for e in range(4):
            rhs=(2*M**4 + ap*M*M*e*e + (bp//2)*e**4) % 4
            assert rhs == 2 and rhs not in {0,1}
    for m in [1,3,5,7]:
        for e in [1,3,5,7]:
            rhs=(2*m**4 + 169*m*m*e*e + 1800*e**4) % 8
            assert rhs == 3
    squares8={0,1,4}
    for m1 in range(8):
        for e in [1,3,5,7]:
            rhs=(8*m1**4 + 169*m1*m1*e*e + 450*e**4) % 8
            assert rhs == (m1*m1+2) % 8
            assert rhs not in squares8
    assert 1*4//4 == 1


def torsion_check() -> None:
    assert point_count(11) == 8
    assert point_count(13) == 8
    assert math.gcd(11, 2*3*5*7*17) == 1
    assert math.gcd(13, 2*3*5*7*17) == 1
    assert not is_square_fraction(Fraction(-49))
    assert not is_square_fraction(Fraction(-289))
    assert is_square_fraction(Fraction(49))
    assert not is_square_fraction(Fraction(-240))
    assert is_square_fraction(Fraction(289))
    assert not is_square_fraction(Fraction(240))


def source_and_state_check(c: dict) -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(O_CERT) == O_BLOB
    assert blob(P_CERT) == P_BLOB
    assert blob(Q_CERT) == Q_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(W03) == W03_BLOB
    assert git("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == V47_BLOB
    assert "2^r = |Im(alpha)|*|Im(beta)|/4" in SOURCE.read_text()
    assert "square-free divisor" in SOURCE.read_text()
    assert "RECEIVER_RESTRICTED_INTERSECTION_EXCLUSION" in W03.read_text()

    s=json.loads(STATE.read_text())
    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V48_36_09R_PENDING_HOSTILE_AUDIT"
    assert s["status"] == "ACTIVE_PENDING_HOSTILE_AUDIT"
    r=s["authority_frontier"]["36-09R"]
    assert r["certificate_blob_sha"] == CERT_BLOB
    assert r["E_TAU_RANKJUMP_PLUS_K_REDUNDANT"] is True
    assert r["E_SIGMA_TAU_GENERIC_RANK"] == 0
    assert r["E_SIGMA_TAU_GENERIC_TORSION"] == "Z/2 x Z/2"
    assert r["RECEIVER_FORCES_E_SIGMA_TAU_MW_GROWTH"] is True
    assert r["CANDIDATE_SET_SHRUNK_BY_DERIVED_GROWTH"] is False
    assert r["INDEPENDENCE_CLAIMED"] is False
    assert r["SIMULTANEOUS_GROWTH_LOCUS_EMPTY"] is False
    assert r["S34_W03_INTERSECTION_EXECUTED"] is False
    assert r["RECEIVER_CLOSED"] is False
    assert s["current"]["36_09S_entry_allowed"] is False
    assert s["promotion_gates"]["E_sigma_tau_generic_MW_certificate_complete"] is True
    assert s["promotion_gates"]["E_sigma_tau_generic_MW_promoted"] is False
    assert s["promotion_gates"]["receiver_emptiness_proved"] is False
    assert s["promotion_gates"]["R29_CAMP2_closed"] is False


def main() -> None:
    c=json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09R_E_TAU_RANKJUMP_RECEIVER_E_SIGMA_TAU_GROWTH_PREFLIGHT_V1"
    assert c["status"] == "EXACT_E_TAU_RANKJUMP_REDUNDANCY_AND_E_SIGMA_TAU_GENERIC_MW_GROWTH_REDUCTION_PENDING_HOSTILE_AUDIT"
    assert c["base_main_sha"] == BASE
    adapter_identities()
    receiver_stage14_identity()
    specialization_injectivity_check()
    descent_check()
    torsion_check()
    assert c["generic_E_sigma_tau_MW"]["generic_rank"] == 0
    assert c["generic_E_sigma_tau_MW"]["exact_generic_MW_group"] == "Z/2 x Z/2"
    assert c["generic_quartic_point_inventory"]["count"] == 4
    sim=c["simultaneous_exceptional_growth_reduction"]
    assert sim["adds_distinct_quotient_growth_obligation"] is True
    assert sim["candidate_set_shrunk_by_adding_derived_E_sigma_tau_growth"] is False
    assert sim["independence_claimed"] is False
    assert sim["simultaneous_growth_locus_empty_proved"] is False
    assert sim["E_sigma_tau_rank_jumps_excluded"] is False
    assert sim["E_sigma_tau_torsion_growth_excluded"] is False
    assert sim["S34_W03_intersection_exclusion_executed"] is False
    source_and_state_check(c)
    print("36-09R exact: E_tau rankjump+K redundancy exposed; E_sigma_tau generic MW=Z/2xZ/2; receiver forces a distinct quotient-growth obligation with no independence or candidate-set-shrink claim")


if __name__ == "__main__":
    main()
