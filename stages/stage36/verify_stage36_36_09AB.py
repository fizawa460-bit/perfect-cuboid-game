#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages" / "stage36" / "36-09AB" / "same-x-product-square-etau-birational-preflight.json"
AA_CERT = ROOT / "stages" / "stage36" / "36-09AA" / "receiver-coupled-same-x-twist-intersection-preflight.json"
R_CERT = ROOT / "stages" / "stage36" / "36-09R" / "etau-rankjump-receiver-esigmatau-growth-preflight.json"
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"

BASE = "bd1f40297f8dcf79e5bb4ef0b8cdc13fdb844177"
PROMOTION_HEAD = "d5c212d9be970dc31a28d50db926f4cfac34c561"
CERT_BLOB = "65747ffe111d9f0f55f48d48d4f082e19d1ee759"
AA_CERT_BLOB = "be447726a97158849c67ed6d57d6d3c35d6ba20f"
R_CERT_BLOB = "b55d042ede01032ff8c8b0d872510a53cb857969"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))

Poly = dict[tuple[int, int], int]
def pclean(a: Poly) -> Poly: return {m:c for m,c in a.items() if c}
def padd(a: Poly, b: Poly) -> Poly:
    out=dict(a)
    for m,c in b.items(): out[m]=out.get(m,0)+c
    return pclean(out)
def pneg(a: Poly) -> Poly: return {m:-c for m,c in a.items()}
def psub(a: Poly,b: Poly) -> Poly: return padd(a,pneg(b))
def pmul(a: Poly,b: Poly) -> Poly:
    out: Poly={}
    for (i,j),c in a.items():
        for (r,s),d in b.items():
            m=(i+r,j+s); out[m]=out.get(m,0)+c*d
    return pclean(out)
def pscale(a: Poly,n:int) -> Poly: return {m:n*c for m,c in a.items() if n*c}
def ppow(a: Poly,n:int) -> Poly:
    out={(0,0):1}
    for _ in range(n): out=pmul(out,a)
    return out
ONE={(0,0):1}; K={(1,0):1}; X={(0,1):1}


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(AA_CERT) == AA_CERT_BLOB
    assert blob(R_CERT) == R_CERT_BLOB
    subprocess.check_call(["git","merge-base","--is-ancestor",BASE,"HEAD"],cwd=ROOT)
    subprocess.check_call(["git","merge-base","--is-ancestor",PROMOTION_HEAD,"HEAD"],cwd=ROOT)

    c=json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AB_SAME_X_PRODUCT_SQUARE_ETAU_BIRATIONAL_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    assert c["freshness"]["stage36_source_drift"] is False
    assert c["route_diagnosis"]["product_square_quotient_equals_existing_E_tau_route_birationally"] is True
    assert c["route_diagnosis"]["candidate_parameter_set_shrunk_by_product_quotient"] is False
    assert c["route_diagnosis"]["S34_W03_intersection_exclusion_executed"] is False
    assert c["required_stronger_interface"]["next_leaf"] == "36-09AC_SAME_X_SEPARATE_SQUARECLASS_DOUBLE_COVER_PREFLIGHT"

    for p in (Fraction(2,3), Fraction(5,2), Fraction(14,13), Fraction(7,4)):
        nm=p*p-2*p-1; np=p*p+2*p-1
        k=np/nm; C=nm*np; D=p*(p*p-1)
        assert k*k-1 == 8*D/(nm*nm)
        assert 2*k/(k*k-1) == C/(4*D)

    km1=psub(K,ONE); kp1=padd(K,ONE); xp1=padd(X,ONE)
    num_u=pscale(psub(K,X),2)
    num_um1=pmul(kp1,psub(ONE,X))
    num_upt=pscale(pmul(kp1,padd(K,X)),2)
    lhs=pmul(pmul(pmul(num_u,num_um1),num_upt),xp1)
    quart=pmul(pmul(psub(ppow(X,2),ONE), psub(ppow(X,2),ppow(K,2))), pscale(ppow(kp1,2),4))
    assert lhs == quart

    for Kq,Xq in ((Fraction(9,4),Fraction(2)),(Fraction(25,9),Fraction(7,3)),(Fraction(49,16),Fraction(5,2))):
        u=2*(Kq-Xq)/((Kq-1)*(Xq+1))
        Xback=(2*Kq-u*(Kq-1))/(2+u*(Kq-1))
        assert Xback == Xq
        t2=4*Kq/(Kq-1)**2
        quartq=(Xq*Xq-1)*(Xq*Xq-Kq*Kq)
        ratio=4*(Kq+1)**2/((Kq-1)**4*(Xq+1)**4)
        assert u*(u-1)*(u+t2) == ratio*quartq

    st=json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V63_36_09AB_CANDIDATE"
    assert st["base_main_sha"] == BASE
    ab=st["authority_frontier"]["36-09AB"]
    assert ab["certificate_blob_sha"] == CERT_BLOB
    assert ab["PRODUCT_QUOTIENT_BIRATIONAL_TO_E_TAU"] is True
    assert ab["PRODUCT_QUOTIENT_CANDIDATE_SHRINK"] is False
    assert ab["SAME_X_SEPARATE_SQUARE_DATA_PRESERVED_BY_PRODUCT"] is False
    assert st["current"]["unit"] == "36-09AC"
    assert st["current"]["36_09AC_entry_allowed"] is True
    assert st["promotion_gates"]["36_09AB_hostile_audit_passed"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False
    print("36-09AB product-square quotient is exactly birational to audited E_tau; product-only route dominated; separate-squareclass double cover 36-09AC unlocked")


if __name__ == "__main__":
    main()
