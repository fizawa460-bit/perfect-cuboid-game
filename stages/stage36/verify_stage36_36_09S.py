#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09S" / "esigmatau-torsion-growth-exclusion-preflight.json"
R_CERT = ROOT / "stages" / "stage36" / "36-09R" / "etau-rankjump-receiver-esigmatau-growth-preflight.json"
SOURCE = ROOT / "stages" / "stage36" / "36-09S" / "torsion-growth-lmfdb-mazur-source-lock.md"
W03 = ROOT / "docs" / "arsenal" / "cards" / "formal" / "S34-W03.md"

BASE = "a53cd347f83ae47687254430ee25c98d841dc52b"
V50_BLOB = "f34cd4df8cca7232fae5c307f398fb97ac310058"
CERT_BLOB = "3af506b590c5e4d7499c203651c0bf4ef31ec767"
R_BLOB = "b55d042ede01032ff8c8b0d872510a53cb857969"
SOURCE_BLOB = "3549b92406ead4ff846153c5444559ddeac245a7"
W03_BLOB = "1d5275321f42768a6414d4610ac912c63be43f96"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))

# polynomial coefficients in ascending order
def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:
        a.pop()
    return tuple(a)

def add(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i in range(n): c[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    return trim(c)
def neg(a): return tuple(-x for x in a)
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def scale(a,k): return trim([k*x for x in a])
def powp(a,n):
    out=(1,)
    for _ in range(n): out=mul(out,a)
    return out

P=(0,1)
ONE=(1,)
PM1=(-1,1)
PP1=(1,1)
NM=(-1,-2,1)
NP=(-1,2,1)
D=mul(P,mul(PM1,PP1))


def family_identities() -> None:
    assert sub(mul(NP,NP),mul(NM,NM)) == scale(D,8)
    # order-4 common target adapters after Y=2w, X=+/-2p
    # X^3-4X = +/- 8 p(p^2-1) = 4 w^2 for w^2=+/- 2D
    xpos=scale(P,2)
    xneg=scale(P,-2)
    assert sub(powp(xpos,3),scale(xpos,4)) == scale(D,8)
    assert sub(powp(xneg,3),scale(xneg,4)) == scale(D,-8)


def division_polynomial_identity() -> None:
    # psi3 quadratic in lambda has discriminant 16*x^3*(x-1)^3.
    # b=4x^3-6x^2, c=-3x^4+4x^3
    X=(0,1)
    b=add(scale(powp(X,3),4),scale(powp(X,2),-6))
    c=add(scale(powp(X,4),-3),scale(powp(X,3),4))
    disc=sub(mul(b,b),scale(c,4))
    rhs=scale(mul(powp(X,3),powp((-1,1),3)),16)
    assert disc == rhs

    # Substitute x=1/(1-m^2), lambda=(2m-1)/((m-1)^3(m+1)).
    M=(0,1)
    d=sub(ONE,powp(M,2))
    n=(-1,2)
    ell=mul(powp(PM1,3),PP1)
    # cleared numerator of lambda^2 +(4x^3-6x^2)lambda -3x^4+4x^3
    cleared=add(
        mul(powp(n,2),powp(d,4)),
        add(mul(mul(add(scale(d,4),scale(powp(d,2),-6)),n),ell),
            mul(add((-3,),scale(d,4)),powp(ell,2)))
    )
    assert trim(cleared) == (0,)

    # Squareclass reduction: n*ell = (m-1)^2*(2m-1)*(m^2-1).
    lhs=mul(n,ell)
    rhs2=mul(powp(PM1,2),mul(n,mul(PM1,PP1)))
    assert lhs == rhs2

    # Gate curve under X=2m,Y=2z.
    gate=scale(mul(n,mul(PM1,PP1)),4)
    x2=scale(M,2)
    cubic=add(add(powp(x2,3),scale(powp(x2,2),-1)),add(scale(x2,-4),(4,)))
    assert gate == cubic


def is_square_fraction(q: Fraction) -> bool:
    if q < 0: return False
    return math.isqrt(q.numerator)**2 == q.numerator and math.isqrt(q.denominator)**2 == q.denominator


def e3_point_inventory() -> None:
    pts=[(-2,0),(1,0),(2,0),(0,2),(0,-2),(4,6),(4,-6)]
    for x,y in pts:
        assert y*y == (x-2)*(x-1)*(x+2)
    assert len(set(pts)) == 7  # plus O gives 8, matching source-locked torsion order 8 and rank 0.

    # Relevant minus branch lambda at all finite non-boundary m values from the exhaustive list.
    def lam_minus(m: Fraction):
        den=(m-1)**3*(m+1)
        return None if den == 0 else (2*m-1)/den
    assert lam_minus(Fraction(1,2)) == 0
    assert lam_minus(Fraction(0)) == 1
    assert lam_minus(Fraction(2)) == 1
    assert lam_minus(Fraction(1)) is None
    assert lam_minus(Fraction(-1)) is None
    # plus branch is minus branch after m -> -m, so it has the same boundary-only outcome.


def source_and_state_check(c: dict) -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(R_CERT) == R_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(W03) == W03_BLOB
    assert git("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == V50_BLOB
    text=SOURCE.read_text()
    assert "64.a3" in text and "y^2 = x^3 - 4*x" in text and "Z/2 x Z/2" in text
    assert "24.a4" in text and "x^3 - x^2 - 4*x + 4" in text and "Z/2 x Z/4" in text
    assert "Z/2 x Z/(2n)" in text and "n=1,2,3,4" in text

    s=json.loads(STATE.read_text())
    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V51_36_09S_PENDING_HOSTILE_AUDIT"
    assert s["status"] == "ACTIVE_PENDING_HOSTILE_AUDIT"
    q=s["authority_frontier"]["36-09S"]
    assert q["certificate_blob_sha"] == CERT_BLOB
    assert q["E_SIGMA_TAU_TORSION_GROWTH_EXCLUDED"] is True
    assert q["E_SIGMA_TAU_RETAINED_TORSION"] == "Z/2 x Z/2"
    assert q["ONLY_REMAINING_E_SIGMA_TAU_MW_GROWTH_SPECIES"] == "positive rank jump"
    assert q["RECEIVER_FORCES_E_SIGMA_TAU_POSITIVE_RANK_JUMP"] is True
    assert q["INDEPENDENCE_CLAIMED"] is False
    assert q["SIMULTANEOUS_POSITIVE_RANK_LOCUS_EMPTY"] is False
    assert q["RECEIVER_CLOSED"] is False
    assert s["current"]["36_09T_entry_allowed"] is False
    assert s["promotion_gates"]["E_sigma_tau_torsion_growth_exclusion_promoted"] is False
    assert s["promotion_gates"]["receiver_emptiness_proved"] is False
    assert s["promotion_gates"]["R29_CAMP2_closed"] is False


def main() -> None:
    c=json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09S_E_SIGMA_TAU_TORSION_GROWTH_EXCLUSION_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    family_identities()
    division_polynomial_identity()
    e3_point_inventory()

    # retained lambda != 0,1: Nplus/Nminus has no rational zero/pole from its irreducible discriminant-8 quadratics;
    # lambda=1 forces Nplus=+/-Nminus, hence p=0 or p=+/-1.
    assert not is_square_fraction(Fraction(8))
    assert sub(NP,NM) == scale(P,4)
    assert add(NP,NM) == scale(mul(PM1,PP1),2)

    m=c["mazur_reduction"]
    assert m["full_rational_2torsion_already_present"] is True
    assert m["strict_torsion_growth_candidates"] == ["Z/2 x Z/4","Z/2 x Z/6","Z/2 x Z/8"]
    assert c["order4_exclusion"]["retained_order4_exists"] is False
    assert c["order3_exclusion"]["retained_order3_exists"] is False
    con=c["conclusion"]
    assert con["E_SIGMA_TAU_TORSION_GROWTH_EXCLUDED"] is True
    assert con["retained_fiber_torsion_exact"] == "Z/2 x Z/2"
    assert con["receiver_forces_E_sigma_tau_positive_rank_jump"] is True
    assert con["two_positive_rank_obligations_claimed_independent"] is False
    for k,v in c["scope_firewalls"].items():
        if k not in (): assert v is False
    source_and_state_check(c)
    print("36-09S exact: E_sigma_tau torsion growth excluded via order-4 64.a3 and order-3 24.a4 gates; receiver now forces positive rank jump; no simultaneous-rank/receiver closure credit")


if __name__ == "__main__":
    main()
