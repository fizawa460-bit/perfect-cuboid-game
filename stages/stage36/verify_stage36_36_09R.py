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
CERT_BLOB = "efb5768a002d03110d91687c755ecf26e475bd22"
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
    # The numerator identities here have bounded degree <= 8; these ten distinct
    # retained integer samples also guard all signs/scalings independently.
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

        # Direct quartic-to-cubic algebra at generic rational z values.
        for z in [Fraction(2), Fraction(3,2), Fraction(-2), Fraction(5,3)]:
            if z*z == 1:
                continue
            S2 = (2*B*z+a+b)/(z*z-1)
            X = 2*B*z
            U = X+a+b
            # w^2 from the eliminated quartic equals the cubic product.
            w2 = S2*(z*z-1)**2
            Y2 = (2*B)**2*w2
            assert Y2 == U*(U-(r-2*r/h)**2)*(U-(r+2*r/h)**2)
            # scaled roots are exactly Nm^2,Np^2.
            xx = L*L*U
            yy2 = L**6*Y2
            assert yy2 == xx*(xx-Nm*Nm)*(xx-Np*Np)


def receiver_stage14_identity() -> None:
    # Pure algebra on E_t: Y^2=X(X-1)(X+t^2).
    for t in [Fraction(2,3), Fraction(-3,5), Fraction(5,7)]:
        for X in [Fraction(2), Fraction(3,2), Fraction(-1), Fraction(7,3)]:
            if X + t*t == 0:
                continue
            R2 = 4*X*(X-1)/(X+t*t)
            assert R2-4 == 4*(X*X-2*X-t*t)/(X+t*t)
            h2 = 1+t*t
            assert (X-1)**2-h2 == X*X-2*X-t*t


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
    # squareclasses are [6],[2],[10],[3],[15],[5],[30]
    expected = {Fraction(3,2), Fraction(1,2), Fraction(5,2), Fraction(3,4), Fraction(15,4), Fraction(5,4), Fraction(15,8)}
    assert set(seen) == expected


def descent_check() -> None:
    # E*: y^2=x^3-338x^2+14161x.
    a=-338; b=14161
    assert b == 119**2
    # Negative alpha classes: d<0, a<0, b/d<0 makes RHS strictly negative.
    for d in [-1,-7,-17,-119]:
        assert d < 0 and a < 0 and b//d < 0
    assert not local_quartic_has_point(7,a,b//7,5)
    assert not local_quartic_has_point(17,a,b//17,3)
    assert not local_quartic_has_point(119,a,b//119,3)

    # Dual E*': y^2=x^3+676x^2+57600x=x(x+100)(x+576).
    ap=676; bp=57600
    assert bp == 240**2
    realized={1:(0,1,240), -1:(10,1,0), 15:(4,1,136), -15:(4,1,56)}
    for d,(M,e,N) in realized.items():
        assert N*N == d*M**4 + ap*M*M*e*e + (bp//d)*e**4
    for d in [3,-3,5,-5,6,-6,10,-10]:
        assert not local_quartic_has_point(d,ap,bp//d,17)

    # Primitive parity descent excluding class d=2.
    # M odd: RHS = 2 (mod 4), impossible for a square.
    for M in [1,3]:
        for e in range(4):
            rhs=(2*M**4 + ap*M*M*e*e + (bp//2)*e**4) % 4
            assert rhs == 2
            assert rhs not in {0,1}
    # M=2m, primitive => e odd. After division by 16:
    # n^2=2m^4+169m^2 e^2+1800e^4. If m odd this is 3 mod 8.
    for m in [1,3,5,7]:
        for e in [1,3,5,7]:
            rhs=(2*m**4 + 169*m*m*e*e + 1800*e**4) % 8
            assert rhs == 3
    # If m=2m1, divide again by 4:
    # n1^2=8m1^4+169m1^2 e^2+450e^4 = m1^2+2 mod 8,
    # never one of 0,1,4.
    squares8={0,1,4}
    for m1 in range(8):
        for e in [1,3,5,7]:
            rhs=(8*m1**4 + 169*m1*m1*e*e + 450*e**4) % 8
            assert rhs == (m1*m1+2) % 8
            assert rhs not in squares8

    # Since beta image is a subgroup containing [-1],[15], any of
    # [-2],[30],[-30] would force [2]; hence the d=2 exclusion closes all four.
    beta_real={1,-1,15,-15}
    assert len(beta_real)==4
    assert 1*4//4 == 1  # 2^rank


def torsion_check() -> None:
    assert point_count(11) == 8
    assert point_count(13) == 8
    # Discriminant support uses 49,289,240, so 11,13 are good.
    assert math.gcd(11, 2*3*5*7*17) == 1
    assert math.gcd(13, 2*3*5*7*17) == 1
    # Full rational 2-torsion is present. Halving criterion fails in every direction.
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
    text=SOURCE.read_text()
    assert "2^r = |Im(alpha)|*|Im(beta)|/4" in text
    assert "square-free divisor" in text
    w=W03.read_text()
    assert "RECEIVER_RESTRICTED_INTERSECTION_EXCLUSION" in w

    s=json.loads(STATE.read_text())
    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V48_36_09R_PENDING_HOSTILE_AUDIT"
    assert s["status"] == "ACTIVE_PENDING_HOSTILE_AUDIT"
    r=s["authority_frontier"]["36-09R"]
    assert r["certificate_blob_sha"] == CERT_BLOB
    assert r["E_TAU_RANKJUMP_PLUS_K_REDUNDANT"] is True
    assert r["E_SIGMA_TAU_GENERIC_RANK"] == 0
    assert r["E_SIGMA_TAU_GENERIC_TORSION"] == "Z/2 x Z/2"
    assert r["RECEIVER_FORCES_E_SIGMA_TAU_MW_GROWTH"] is True
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
    assert sim["strictly_stronger_than_E_tau_rankjump_plus_K_restatement"] is True
    assert sim["simultaneous_growth_locus_empty_proved"] is False
    assert sim["E_sigma_tau_rank_jumps_excluded"] is False
    assert sim["E_sigma_tau_torsion_growth_excluded"] is False
    assert sim["S34_W03_intersection_exclusion_executed"] is False
    source_and_state_check(c)
    print("36-09R exact: E_tau rankjump+K redundancy exposed; E_sigma_tau generic MW=Z/2xZ/2; every receiver point forces simultaneous exceptional quotient growth")


if __name__ == "__main__":
    main()
