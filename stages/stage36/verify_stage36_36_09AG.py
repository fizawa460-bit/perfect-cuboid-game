#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage36/36-09AG/individual-conic-hasse-solubility-preflight.json"
SRC = ROOT / "stages/stage36/36-09AG/conic-hasse-source-lock.md"
AF = ROOT / "stages/stage36/36-09AF/variable-prime-jacobi-matrix-realizability-preflight.json"
AE = ROOT / "stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json"
AD = ROOT / "stages/stage36/36-09AD/coupled-six-reservoir-factor-squareclass-parity-preflight.json"
W_SRC = ROOT / "stages/stage36/36-09W/hilbert-reciprocity-source-lock.md"
S34 = ROOT / "docs/arsenal/cards/formal/S34-W01.md"
STATE = ROOT / "stages/stage36/MAIN-STATE.json"

BASE = "9306238c7ada55e31311245019d6b7e474ad837f"
AUDITED_HEAD = "f2922c992ab1e056fa03932ba017d0dfdae845cb"
AUDIT_REVIEW = 5127056767
AUDIT_CI = "34067480463/101578693605"
CERT_BLOB = "b40a525e739d6021c07d364a243c0d7653350abe"
SRC_BLOB = "68fb5ef625f9d81e8c9b9388f9be519c2ddd4ea8"
AF_BLOB = "be5a65e3fcfb182998ccb02ec42f8114b50b0a7d"
AE_BLOB = "ddae37dd35cd0e732cebadf9c17f3f3fa57930df"
AD_BLOB = "9d0388845955efee71d1a761ae4ee943d8b565d5"
W_SRC_BLOB = "52952e2afd1db636a236c6bd254acadc779fe09f"
S34_BLOB = "01a8e90e34b4aa46edbfa825803d488e5230e9d0"
SURVIVOR_SHA = "b2c4eceb909cdefd18e3075d5223a95af6fcd029b623eeae557fe92f83e90721"

LEFT_NULL_BASIS = [
    [0,0,1,1,1,1,1,1],
    [0,1,0,1,0,0,1,0],
    [1,0,0,1,0,1,1,1],
]


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def mt(n: int) -> tuple[int,int]:
    assert n in (1,3,5,7)
    return ((n-1)//2) & 1, ((n*n-1)//8) & 1


def constants(A:int,B:int,C:int,D:int,e:int,f:int,h:int) -> list[int]:
    mA,tA=mt(A); mB,tB=mt(B); mC,tC=mt(C); mD,tD=mt(D)
    return [
        ((1+h)*mA + e*tA + mA*mB + mA*mC) & 1,
        (f*tA + mA*mB + mA*mD) & 1,
        (h*mB + e*tB + mB*mC) & 1,
        (f*tB + mB*mD) & 1,
        0,
        ((1-f)*tC + mC*mD) & 1,
        mD & 1,
        (h*mD + (1-e)*tD) & 1,
    ]


def reciprocity_consistent(A:int,B:int,C:int,D:int,e:int,f:int,h:int) -> bool:
    c=constants(A,B,C,D,e,f,h)
    return all(sum(y[i]*c[i] for i in range(8)) % 2 == 0 for y in LEFT_NULL_BASIS)


def uv_two_adic_allowed(A:int,B:int,e:int,f:int) -> bool:
    if (e,f)==(0,0):
        return True
    if A==B:
        return f==1
    return e==1


def eps_odd(u: int) -> int:
    u %= 8
    assert u & 1
    return ((u-1)//2) & 1


def omega_odd(u: int) -> int:
    u %= 8
    assert u & 1
    return ((u*u-1)//8) & 1


def hilbert2(alpha:int,u:int,beta:int,v:int) -> int:
    # (2^alpha*u, 2^beta*v)_2 for odd u,v.
    exponent = eps_odd(u)*eps_odd(v) + alpha*omega_odd(v) + beta*omega_odd(u)
    return -1 if exponent & 1 else 1


def hminus2(A:int,B:int,C:int,e:int,h:int) -> int:
    eta = -1 if h else 1
    return hilbert2(0, A*B, e, eta*A*C)


def hplus2(A:int,B:int,D:int,f:int) -> int:
    return hilbert2(0, -A*B, f, A*D)


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(SRC) == SRC_BLOB
    assert blob(AF) == AF_BLOB
    assert blob(AE) == AE_BLOB
    assert blob(AD) == AD_BLOB
    assert blob(W_SRC) == W_SRC_BLOB
    assert blob(S34) == S34_BLOB
    subprocess.check_call(["git","merge-base","--is-ancestor",BASE,"HEAD"], cwd=ROOT)
    assert git("rev-parse", f"{BASE}:stages/stage36/36-09AF/variable-prime-jacobi-matrix-realizability-preflight.json") == AF_BLOB
    assert git("rev-parse", f"{BASE}:stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json") == AE_BLOB

    c=json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AG_INDIVIDUAL_CONIC_HASSE_SOLUBILITY_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    ap=c["audited_parent"]
    assert ap["pr"] == 1670
    assert ap["hostile_audit_review"] == AUDIT_REVIEW
    assert ap["audited_exact_head"] == AUDITED_HEAD
    assert ap["exact_head_ci"] == AUDIT_CI
    assert ap["merged_main_sha"] == BASE

    rows=c["exact_odd_bad_place_rows"]
    assert rows["minus"]["required_row_indices_one_based"] == [1,3,5]
    assert rows["plus"]["required_row_indices_one_based"] == [2,4,7]
    assert "not needed" in rows["rows_6_and_8"]
    assert c["hilbert_norm_models"]["minus"]["pair"] == ["A*B", "eta*2^e*A*C"]
    assert c["hilbert_norm_models"]["plus"]["pair"] == ["-A*B", "2^f*A*D"]

    # Reconstruct the exact audited AE finite residue skeleton and independently
    # verify the two Q_2 Hilbert symbols on every survivor.
    survivors=[]
    for A,B in itertools.product((1,7), repeat=2):
        for C,D in itertools.product((1,3,5,7), repeat=2):
            for e,f,h in itertools.product((0,1), repeat=3):
                if reciprocity_consistent(A,B,C,D,e,f,h) and uv_two_adic_allowed(A,B,e,f):
                    survivors.append((A,B,C,D,e,f,h))
    assert len(survivors) == 128
    text="\n".join(",".join(map(str,x)) for x in sorted(survivors))+"\n"
    assert hashlib.sha256(text.encode()).hexdigest() == SURVIVOR_SHA
    for A,B,C,D,e,f,h in survivors:
        assert hminus2(A,B,C,e,h) == 1
        assert hplus2(A,B,D,f) == 1

    # Exact AF B=7 separate-conic witnesses.  Their u:v ratios deliberately differ.
    A,B,C,D,eta,e,f = 73,7,11,13,-1,1,1
    um,vm,rm = 5,17,3
    up,vp,sp = 1,7,4
    assert A*um*um-B*vm*vm == eta*(2**e)*C*rm*rm == -198
    assert A*up*up+B*vp*vp == (2**f)*D*sp*sp == 416
    assert um*vp != up*vm
    w=c["AF_B7_exact_witness"]
    assert w["projective_u_v_ratios_differ"] is True

    g=c["global_conclusion"]
    assert g["minus_rows_1_3_5_pass_implies_minus_conic_Q_point"] is True
    assert g["plus_rows_2_4_7_pass_implies_plus_conic_Q_point"] is True
    assert g["all_eight_AE_rows_pass_implies_both_conics_individually_Q_solvable"] is True
    assert g["common_u_v_ratio_obtained"] is False
    assert g["coupled_intersection_point_obtained"] is False

    st=json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V68_36_09AG_CANDIDATE"
    assert st["base_main_sha"] == BASE
    assert st["audited_batch_promotion"]["candidate_pr"] == 1670
    assert st["audited_batch_promotion"]["hostile_audit_review"] == AUDIT_REVIEW
    assert st["audited_batch_promotion"]["merged_main_sha"] == BASE
    for leaf in ("36-09AB","36-09AC","36-09AD","36-09AE","36-09AF"):
        assert st["promotion_gates"][leaf.replace("-", "_") + "_hostile_audit_passed"] is True
    ag=st["authority_frontier"]["36-09AG"]
    assert ag["INDIVIDUAL_CONIC_Q_SOLUBILITY_CLASSIFIED"] is True
    assert ag["COMMON_UV_RATIO_OBTAINED"] is False
    assert ag["RECEIVER_CLOSED"] is False
    assert st["current"]["unit"] == "36-09AH"
    assert st["current"]["36_09AH_entry_allowed"] is True
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09AG verified: AE rows 1/3/5 and 2/4/7 are exact odd bad-place Hilbert conditions for the two diagonal conics; reciprocity discharges Q2, Hasse-Minkowski gives each conic a Q-point separately; all 128 AE residue survivors pass both Q2 symbols; common u:v remains the live obstruction and 36-09AH is unlocked")


if __name__ == "__main__":
    main()
