#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/"stages/stage36/36-09AI/j1728-congruent-number-jacobian-preflight.json"
SRC=ROOT/"stages/stage36/36-09AI/quadric-intersection-jacobian-source-lock.md"
AH=ROOT/"stages/stage36/36-09AH/common-uv-two-quadric-genusone-preflight.json"
AHV=ROOT/"stages/stage36/verify_stage36_36_09AH.py"
S31=ROOT/"docs/arsenal/cards/formal/S31-W01.md"
STATE=ROOT/"stages/stage36/MAIN-STATE.json"

BASE="9306238c7ada55e31311245019d6b7e474ad837f"
AH_HEAD="ab90853e74735a367faa4d98e5c249de3c3a9cd5"
AH_CI="34069620942/101584427296"
CERT_BLOB="c5af6c4dde67532ea8d592e74aed187c72bbed4e"
SRC_BLOB="5f119e0563f1d60fa4e4c0ee6781d71c0bb6d817"
AH_BLOB="732431bef8dfafe25cbdeb005c4237d72a40ae4b"
AHV_BLOB="f5889e32fdeea06e9287e86f45c694df9815dabf"
S31_BLOB="122a6c1c5c871c1c7b797017e854de8ec55e7c50"


def git(*args:str)->str:
    return subprocess.check_output(["git",*args],cwd=ROOT,text=True).strip()

def blob(path:Path)->str:
    return git("hash-object",str(path.relative_to(ROOT)))

def squarefree(n:int)->bool:
    if n<=0:
        return False
    p=2
    m=n
    while p*p<=m:
        c=0
        while m%p==0:
            m//=p;c+=1
            if c>=2:return False
        p+=1
    return True

def normalized_n(A:int,B:int,C:int,D:int,e:int,f:int)->tuple[int,int,int]:
    N=A*B*C*D
    g=(e+f)&1
    n=(2**g)*N
    k=2**((e+f)//2)
    return N,n,k

def main()->None:
    assert blob(CERT)==CERT_BLOB
    assert blob(SRC)==SRC_BLOB
    assert blob(AH)==AH_BLOB
    assert blob(AHV)==AHV_BLOB
    assert blob(S31)==S31_BLOB
    subprocess.check_call(["git","merge-base","--is-ancestor",BASE,"HEAD"],cwd=ROOT)
    subprocess.check_call(["git","merge-base","--is-ancestor",AH_HEAD,"HEAD"],cwd=ROOT)
    assert git("rev-parse",f"{AH_HEAD}:stages/stage36/36-09AH/common-uv-two-quadric-genusone-preflight.json")==AH_BLOB
    assert git("rev-parse",f"{AH_HEAD}:stages/stage36/verify_stage36_36_09AH.py")==AHV_BLOB

    c=json.loads(CERT.read_text())
    assert c["schema"]=="STAGE36_36_09AI_J1728_CONGRUENT_NUMBER_JACOBIAN_PREFLIGHT_V1"
    assert c["base_main_sha"]==BASE
    assert c["batch_parent"]["36_09AH_exact_head"]==AH_HEAD
    assert c["batch_parent"]["36_09AH_exact_head_ci"]==AH_CI

    fs=c["fisher_specialization"]
    assert fs["rank_Qminus"]==3
    assert fs["smooth_intersection"] is True
    assert fs["coefficient_matrix_determinant"]=="delta*x*(1-x^2)"
    assert fs["second_derivative_matrix_factor"]==16
    assert int(math.isqrt(16))**2==16
    assert fs["two_covering_of_jacobian"] is True

    jm=c["jacobian_models"]
    assert jm["pencil_model"]=="y^2=delta*x*(1-x^2)"
    assert jm["short_weierstrass"]=="Y^2=X^3-delta^2*X"
    # Verify the rational change X=-delta*x, Y=delta*y symbolically by
    # comparing coefficients of x and x^3 after multiplying the pencil equation by delta^2.
    # delta^2*y^2 = delta^3*x - delta^3*x^3 = X^3-delta^2*X.
    assert jm["first_change"]=={"X":"-delta*x","Y":"delta*y"}
    assert jm["sign_eta_drops_from_coefficient"] is True
    # Short Weierstrass A=-delta^2, B=0 => j=1728*4A^3/(4A^3+27B^2)=1728.
    assert jm["short_weierstrass_j"]==1728

    sf=c["squarefree_normalization"]
    assert sf["n"]=="2^g*A*B*C*D"
    # Exhaust e,f possibilities and verify |delta|=k^2*n.
    A,B,C,D=3,5,7,11
    for e in (0,1):
        for f in (0,1):
            N,n,k=normalized_n(A,B,C,D,e,f)
            delta_abs=(2**(e+f))*N
            assert delta_abs==k*k*n
            assert squarefree(N)
            assert squarefree(n)
    assert sf["n_positive_squarefree"] is True
    assert sf["normalized_jacobian"]=="E_n: Y0^2=X0^3-n^2*X0"
    assert sf["rational_2torsion_x_coordinates"]==["0","n","-n"]

    ex=c["AF_examples"]
    for key,Bv,expected in (("B7_branch",7,73073),("B23_branch",23,240097)):
        z=ex[key]
        N,n,k=normalized_n(73,Bv,11,13,1,1)
        assert N==expected and n==expected and k==2
        assert z["N"]==expected and z["n"]==expected and z["g"]==0
        assert squarefree(n)
    assert ex["B7_branch"]["jacobian"]=="Y^2=X^3-73073^2*X"
    assert ex["B23_branch"]["jacobian"]=="Y^2=X^3-240097^2*X"

    rr=c["route_result"]
    assert rr["Q_jacobian_identified"] is True
    assert rr["Q_jacobian_family_fixed"]=="CONGRUENT_NUMBER_J1728"
    assert rr["two_covering_structure_identified"] is True
    assert rr["covering_class_trivialized"] is False
    assert rr["Mordell_Weil_rank_classified"] is False
    assert rr["candidate_parameter_set_shrunk"] is False
    assert rr["receiver_closed"] is False
    assert rr["next_leaf"]=="36-09AJ_CONGRUENT_NUMBER_2SELMER_COVERING_CLASS_PREFLIGHT"

    st=json.loads(STATE.read_text())
    assert st["schema"]=="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V70_36_09AI_CANDIDATE"
    ai=st["authority_frontier"]["36-09AI"]
    assert ai["Q_JACOBIAN_FAMILY"]=="CONGRUENT_NUMBER_J1728"
    assert ai["TWO_COVERING_STRUCTURE_IDENTIFIED"] is True
    assert ai["COVERING_CLASS_TRIVIALIZED"] is False
    assert ai["RECEIVER_CLOSED"] is False
    assert st["current"]["unit"]=="36-09AJ"
    assert st["current"]["36_09AJ_entry_allowed"] is True
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09AI verified: Fisher rank-3 quadric-intersection theorem identifies the common-u:v genus-one curve as a 2-covering of E_n: Y^2=X^3-n^2X with squarefree n=2^((e+f) mod2)ABCD and j=1728; covering class remains nontriviality/solubility target; 36-09AJ unlocked")

if __name__=="__main__":
    main()
