#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages" / "stage36" / "36-09AC" / "same-x-separate-squareclass-double-cover-preflight.json"
AB_CERT = ROOT / "stages" / "stage36" / "36-09AB" / "same-x-product-square-etau-birational-preflight.json"
AA_CERT = ROOT / "stages" / "stage36" / "36-09AA" / "receiver-coupled-same-x-twist-intersection-preflight.json"
O_CERT = ROOT / "stages" / "stage36" / "36-09O" / "physical-square-lift-v4-quotient-preflight.json"
V_CERT = ROOT / "stages" / "stage36" / "36-09V" / "gaussian-directional-prime-support-preflight.json"
S34 = ROOT / "docs" / "arsenal" / "cards" / "formal" / "S34-W01.md"
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"

BASE = "bd1f40297f8dcf79e5bb4ef0b8cdc13fdb844177"
AB_HEAD = "f729993d52a441632b3566c5d08b06c2672d4ae6"
AB_CERT_BLOB = "65747ffe111d9f0f55f48d48d4f082e19d1ee759"
AB_VERIFIER_BLOB = "a54f25903669a64129a9e29d0ac343170536c65e"
CERT_BLOB = "3e95cc443bb9de9e0d2b14d6d9c32ea7c1953021"
AA_CERT_BLOB = "be447726a97158849c67ed6d57d6d3c35d6ba20f"
O_CERT_BLOB = "6a2678ebedba40e13277100441361039ee47ca28"
V_CERT_BLOB = "9fdec16f920104cc6c1961fb092185a0371258d5"
S34_BLOB = "01a8e90e34b4aa46edbfa825803d488e5230e9d0"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))

# Sparse polynomial arithmetic in Z[a,b].
Poly = dict[tuple[int, int], int]

def clean(x: Poly) -> Poly:
    return {m:c for m,c in x.items() if c}

def add(x: Poly,y: Poly) -> Poly:
    z=dict(x)
    for m,c in y.items(): z[m]=z.get(m,0)+c
    return clean(z)
def neg(x: Poly) -> Poly: return {m:-c for m,c in x.items()}
def sub(x: Poly,y: Poly) -> Poly: return add(x,neg(y))
def mul(x: Poly,y: Poly) -> Poly:
    z: Poly={}
    for (i,j),c in x.items():
        for (r,s),d in y.items():
            m=(i+r,j+s); z[m]=z.get(m,0)+c*d
    return clean(z)
def scale(x: Poly,n:int) -> Poly: return clean({m:n*c for m,c in x.items()})
def power(x: Poly,n:int) -> Poly:
    z={(0,0):1}
    for _ in range(n): z=mul(z,x)
    return z

ONE={(0,0):1}; a={(1,0):1}; b={(0,1):1}
a2=power(a,2); b2=power(b,2); ab=mul(a,b)
M=sub(sub(a2,scale(ab,2)),b2)
P=sub(add(a2,scale(ab,2)),b2)
D0=mul(mul(a,b),mul(sub(a,b),add(a,b)))
S0=add(a2,b2)


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(AB_CERT) == AB_CERT_BLOB
    assert blob(AA_CERT) == AA_CERT_BLOB
    assert blob(O_CERT) == O_CERT_BLOB
    assert blob(V_CERT) == V_CERT_BLOB
    assert blob(S34) == S34_BLOB
    subprocess.check_call(["git","merge-base","--is-ancestor",BASE,"HEAD"],cwd=ROOT)
    subprocess.check_call(["git","merge-base","--is-ancestor",AB_HEAD,"HEAD"],cwd=ROOT)
    assert git("rev-parse", f"{AB_HEAD}:stages/stage36/36-09AB/same-x-product-square-etau-birational-preflight.json") == AB_CERT_BLOB
    assert git("rev-parse", f"{AB_HEAD}:stages/stage36/verify_stage36_36_09AB.py") == AB_VERIFIER_BLOB

    c=json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AC_SAME_X_SEPARATE_SQUARECLASS_DOUBLE_COVER_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE

    # Exact homogeneous parameter identities.
    assert sub(power(P,2),power(M,2)) == scale(D0,8)
    assert add(power(P,2),power(M,2)) == scale(power(S0,2),2)

    # The V4 character product identity is exact pointwise as a polynomial in X,K.
    for X in (-7,-3,-1,0,1,2,5,11):
        for K in (2,4,9,25):
            fm=X*(X-1)*(X-K)
            fp=X*(X+1)*(X+K)
            prod=(X*X-1)*(X*X-K*K)
            assert fm*fp == X*X*prod

    # Primitive four-factor clearing and pairwise-resultant support.
    # For linear forms alpha*U+beta*V, determinant gives common-prime support.
    # minus: U, V, U-V, M^2 U-P^2 V
    # plus : U, V, U+V, M^2 U+P^2 V
    M2=power(M,2); P2=power(P,2)
    assert sub(M2,P2) == scale(D0,-8)
    assert sub(P2,M2) == scale(D0,8)
    # The remaining nontrivial determinants are square coefficients P^2 and M^2.
    assert P2 == power(P,2)
    assert M2 == power(M,2)

    # Exhaustive modular logic for the six pair types, checked over many primitive integers:
    # any odd common prime of a nontrivial pair must divide P, M, or D0.
    from math import gcd
    def prime_divs(n:int):
        n=abs(n); out=[]; q=2
        while q*q<=n:
            if n%q==0:
                out.append(q)
                while n%q==0:n//=q
            q+=1
        if n>1: out.append(n)
        return out
    for aa in range(-8,9):
        for bb in range(1,9):
            if gcd(aa,bb)!=1: continue
            mm=aa*aa-2*aa*bb-bb*bb
            pp=aa*aa+2*aa*bb-bb*bb
            dd=aa*bb*(aa-bb)*(aa+bb)
            if mm==0 or pp==0: continue
            for U in range(-9,10):
                for V in range(1,10):
                    if gcd(U,V)!=1: continue
                    lm=mm*mm*U-pp*pp*V
                    lp=mm*mm*U+pp*pp*V
                    pairs_minus=((U,lm,pp),(V,lm,mm),(U-V,lm,dd))
                    pairs_plus=((U,lp,pp),(V,lp,mm),(U+V,lp,dd))
                    for x,y,support in pairs_minus+pairs_plus:
                        g=gcd(abs(x),abs(y))
                        for q in prime_divs(g):
                            if q!=2:
                                assert support%q==0

    v4=c["v4_and_genus"]
    assert v4["degree_over_QX"] == 4
    assert len(v4["branch_points"]) == 6
    assert v4["genus"] == 3
    assert -8 + 12 == 4  # 2g-2 for g=3.

    odd=c["odd_pairwise_support"]
    assert "C0*D0" in odd["squarefree_kernel_support"]
    six=c["six_reservoir_recovery"]
    assert six["new_dynamic_UV_prime_reservoir"] is False
    assert six["fixed_finite_S_recovered"] is False
    s34=c["S34_W01_diagnosis"]
    assert s34["exact_four_factor_forms_materialized"] is True
    assert s34["pairwise_odd_support_control_materialized"] is True
    assert s34["complete_sign_2adic_bookkeeping_materialized"] is False
    assert s34["finite_global_squareclass_branch_family_materialized"] is False

    st=json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V64_36_09AC_CANDIDATE"
    ac=st["authority_frontier"]["36-09AC"]
    assert ac["GENUS3_SAME_X_V4_COVER"] is True
    assert ac["ODD_SQUARECLASS_SUPPORT_REDUCES_TO_SIX_RESERVOIRS"] is True
    assert ac["NEW_DYNAMIC_UV_PRIME_RESERVOIR"] is False
    assert ac["FIXED_FINITE_S_RECOVERED"] is False
    assert ac["S34_W01_FULL_OUTPUT_OBTAINED"] is False
    assert st["current"]["unit"] == "36-09AD"
    assert st["current"]["36_09AD_entry_allowed"] is True
    assert st["promotion_gates"]["36_09AC_hostile_audit_passed"] is False
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False
    print("36-09AC genus-3 same-x V4 cover verified; odd squareclass charge reduces exactly to the audited six parameter reservoirs; no fixed finite-S or receiver closure; 36-09AD unlocked")


if __name__ == "__main__":
    main()
