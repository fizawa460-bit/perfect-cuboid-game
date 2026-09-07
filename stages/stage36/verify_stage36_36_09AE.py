#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages" / "stage36" / "36-09AE" / "six-reservoir-squareclass-conic-coupling-preflight.json"
AD_CERT = ROOT / "stages" / "stage36" / "36-09AD" / "coupled-six-reservoir-factor-squareclass-parity-preflight.json"
V_CERT = ROOT / "stages" / "stage36" / "36-09V" / "gaussian-directional-prime-support-preflight.json"
S34 = ROOT / "docs" / "arsenal" / "cards" / "formal" / "S34-W01.md"
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"

BASE = "07a465cb5025e7c0188fb63610bb40e4b54e7a84"
AD_HEAD = "ebb280e5f1c56372fa3494799506d2242ff2ec31"
AD_CI = "34066782657/101576826714"
CERT_BLOB = "ddae37dd35cd0e732cebadf9c17f3f3fa57930df"
AD_CERT_BLOB = "9d0388845955efee71d1a761ae4ee943d8b565d5"
AD_VERIFIER_BLOB = "c018ed5e0ec0918e388363ce260cdf3ba703b92f"
V_CERT_BLOB = "9fdec16f920104cc6c1961fb092185a0371258d5"
S34_BLOB = "01a8e90e34b4aa46edbfa825803d488e5230e9d0"
SURVIVOR_SHA = "b2c4eceb909cdefd18e3075d5223a95af6fcd029b623eeae557fe92f83e90721"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def rank_f2(rows: list[list[int]]) -> int:
    a = [r[:] for r in rows]
    if not a:
        return 0
    nr, nc = len(a), len(a[0])
    rank = 0
    for c in range(nc):
        pivot = next((i for i in range(rank, nr) if a[i][c] & 1), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for i in range(nr):
            if i != rank and (a[i][c] & 1):
                a[i] = [(x ^ y) for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def mt(n: int) -> tuple[int,int]:
    assert n in (1,3,5,7)
    return ((n-1)//2) & 1, ((n*n-1)//8) & 1


# Equation order is the eight aggregate Jacobi rows from the certificate.
# Pair-symbol columns are pAB,pAC,pAD,pBC,pBD,pCD after quadratic reciprocity.
COEFF = [
    [1,1,0,0,0,0],
    [1,0,1,0,0,0],
    [1,0,0,1,0,0],
    [1,0,0,0,1,0],
    [0,1,0,1,0,0],
    [0,1,0,0,0,1],
    [0,0,1,0,1,0],
    [0,0,1,0,0,1],
]
LEFT_NULL_BASIS = [
    [0,0,1,1,1,1,1,1],
    [0,1,0,1,0,0,1,0],
    [1,0,0,1,0,1,1,1],
]


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
    c = constants(A,B,C,D,e,f,h)
    return all(sum(y[i]*c[i] for i in range(8)) % 2 == 0 for y in LEFT_NULL_BASIS)


def uv_two_adic_allowed(A:int,B:int,e:int,f:int) -> bool:
    # Opposite parity U,V always supplies e=f=0.  If both are odd, AD gives
    # U=A*u^2, V=B*v^2 with odd u,v and A,B in {1,7} mod 8.
    if (e,f) == (0,0):
        return True
    if A == B:
        return f == 1  # U+V == +/-2 mod 8, hence v2(U+V)=1.
    return e == 1      # U-V == +/-2 mod 8, hence v2(U-V)=1.


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(AD_CERT) == AD_CERT_BLOB
    assert blob(V_CERT) == V_CERT_BLOB
    assert blob(S34) == S34_BLOB
    subprocess.check_call(["git","merge-base","--is-ancestor",BASE,"HEAD"],cwd=ROOT)
    subprocess.check_call(["git","merge-base","--is-ancestor",AD_HEAD,"HEAD"],cwd=ROOT)
    assert git("rev-parse", f"{AD_HEAD}:stages/stage36/36-09AD/coupled-six-reservoir-factor-squareclass-parity-preflight.json") == AD_CERT_BLOB
    assert git("rev-parse", f"{AD_HEAD}:stages/stage36/verify_stage36_36_09AD.py") == AD_VERIFIER_BLOB

    c=json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AE_SIX_RESERVOIR_SQUARECLASS_CONIC_COUPLING_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    assert c["batch_parent"]["36_09AD_exact_head"] == AD_HEAD
    assert c["batch_parent"]["36_09AD_exact_head_ci"] == AD_CI

    # The eight selected-prime rows reduce to six oriented pair-symbol variables.
    assert rank_f2(COEFF) == 5
    assert len(LEFT_NULL_BASIS) == 3
    for y in LEFT_NULL_BASIS:
        for col in range(6):
            assert sum(y[i]*COEFF[i][col] for i in range(8)) % 2 == 0
    assert rank_f2(LEFT_NULL_BASIS) == 3
    lin=c["reciprocity_linearization"]
    assert lin["eight_by_six_coefficient_rank"] == 5
    assert lin["left_nullity"] == 3
    assert lin["left_nullspace_basis_rows_over_eight_jacobi_equations"] == LEFT_NULL_BASIS

    # 36-09V alpha support gives (2/A)=(2/B)=+1, hence A,B = 1 or 7 mod 8.
    assert c["alpha_two_residue_input"]["consequence"][2] == "A mod 8 is in {1,7}"
    assert c["alpha_two_residue_input"]["consequence"][3] == "B mod 8 is in {1,7}"

    # Enumerate the exact finite mod-8/sign/2-adic skeleton.
    survivors=[]
    for A,B in itertools.product((1,7), repeat=2):
        for C,D in itertools.product((1,3,5,7), repeat=2):
            for e,f,h in itertools.product((0,1), repeat=3):
                if reciprocity_consistent(A,B,C,D,e,f,h) and uv_two_adic_allowed(A,B,e,f):
                    survivors.append((A,B,C,D,e,f,h))
    assert len(survivors) == 128
    text = "\n".join(",".join(map(str,x)) for x in sorted(survivors)) + "\n"
    assert hashlib.sha256(text.encode()).hexdigest() == SURVIVOR_SHA
    sk=c["finite_mod8_skeleton"]
    assert sk["naive_after_alpha_two_residue_count"] == 512
    assert sk["survivor_count_after_reciprocity_and_UV_2adic_compatibility"] == 128
    assert sk["eliminated_count"] == 384
    assert sk["survivor_sha256"] == SURVIVOR_SHA
    assert sum(1 for x in survivors if x[-1]==0) == 64
    assert sum(1 for x in survivors if x[-1]==1) == 64
    for A,B in itertools.product((1,7), repeat=2):
        assert sum(1 for x in survivors if x[0]==A and x[1]==B) == 32

    # Check the AD-derived U/V 2-adic compatibility rule explicitly.
    for A,B in itertools.product((1,7), repeat=2):
        if A == B:
            assert not uv_two_adic_allowed(A,B,1,0)
            assert uv_two_adic_allowed(A,B,0,0)
            assert uv_two_adic_allowed(A,B,0,1)
            assert uv_two_adic_allowed(A,B,1,1)
        else:
            assert not uv_two_adic_allowed(A,B,0,1)
            assert uv_two_adic_allowed(A,B,0,0)
            assert uv_two_adic_allowed(A,B,1,0)
            assert uv_two_adic_allowed(A,B,1,1)

    interp=c["interpretation"]
    assert interp["fixed_finite_S_recovered"] is False
    assert interp["finite_exhaustive_Q_squareclass_family"] is False
    s34=c["S34_W01_progress"]
    assert s34["quadratic_reciprocity_consistency"] is True
    assert s34["finite_mod8_branch_skeleton"] is True
    assert s34["finite_exhaustive_Q_squareclass_branch_family"] is False
    assert s34["full_S34_W01_output"] is False

    st=json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V66_36_09AE_CANDIDATE"
    assert st["base_main_sha"] == BASE
    ae=st["authority_frontier"]["36-09AE"]
    assert ae["MOD8_SKELETON_NAIVE"] == 512
    assert ae["MOD8_SKELETON_SURVIVORS"] == 128
    assert ae["BRANCH_RESIDUE_SKELETON_SHRUNK"] is True
    assert ae["PAIR_SYMBOL_REALIZABILITY_PROVED"] is False
    assert ae["FINITE_Q_SQUARECLASS_FAMILY"] is False
    assert ae["CANDIDATE_PARAMETER_SET_SHRUNK"] is False
    assert st["current"]["unit"] == "36-09AF"
    assert st["current"]["36_09AF_entry_allowed"] is True
    assert st["promotion_gates"]["36_09AE_hostile_audit_passed"] is False
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09AE reciprocity coupling verified: 8 Jacobi rows -> rank-5 pair-symbol system with 3 consistency relations; alpha (2/q)=1 plus U/V 2-adics prune 512 mod-8 patterns to 128; no actual Q-squareclass family or parameter shrink; 36-09AF unlocked")


if __name__ == "__main__":
    main()
