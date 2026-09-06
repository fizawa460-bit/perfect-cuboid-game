#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages" / "stage36" / "36-09AF" / "variable-prime-jacobi-matrix-realizability-preflight.json"
AE_CERT = ROOT / "stages" / "stage36" / "36-09AE" / "six-reservoir-squareclass-conic-coupling-preflight.json"
AD_CERT = ROOT / "stages" / "stage36" / "36-09AD" / "coupled-six-reservoir-factor-squareclass-parity-preflight.json"
V_CERT = ROOT / "stages" / "stage36" / "36-09V" / "gaussian-directional-prime-support-preflight.json"
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"

BASE = "07a465cb5025e7c0188fb63610bb40e4b54e7a84"
AE_HEAD = "205042c4c09917c319f1a596f67bf6a55d8c3d65"
AE_CI = "34067030924/101577492048"
CERT_BLOB = "25bb2807ad8693da8dc700d3dfb2cdd9e34b37a9"
AE_CERT_BLOB = "ddae37dd35cd0e732cebadf9c17f3f3fa57930df"
AE_VERIFIER_BLOB = "4c2e672572984399a507ddddf296b3861a80edd5"
AD_CERT_BLOB = "9d0388845955efee71d1a761ae4ee943d8b565d5"
V_CERT_BLOB = "9fdec16f920104cc6c1961fb092185a0371258d5"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def leg(a: int, q: int) -> int:
    a %= q
    assert a != 0 and q > 2
    return 1 if pow(a, (q-1)//2, q) == 1 else -1


def rows(A:int,B:int,C:int,D:int,e:int,f:int,h:int) -> list[int]:
    eta = -1 if h else 1
    return [
        leg(-eta*(2**e)*B*C, A),
        leg((2**f)*B*D, A),
        leg(eta*(2**e)*A*C, B),
        leg((2**f)*A*D, B),
        leg(A*B, C),
        leg((2**(1-f))*A*D, C),
        leg(-A*B, D),
        leg(eta*(2**(1-e))*A*C, D),
    ]


def pair_symbols(A:int,B:int,C:int,D:int) -> list[int]:
    return [leg(A,B),leg(A,C),leg(A,D),leg(B,C),leg(B,D),leg(C,D)]


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(AE_CERT) == AE_CERT_BLOB
    assert blob(AD_CERT) == AD_CERT_BLOB
    assert blob(V_CERT) == V_CERT_BLOB
    subprocess.check_call(["git","merge-base","--is-ancestor",BASE,"HEAD"],cwd=ROOT)
    subprocess.check_call(["git","merge-base","--is-ancestor",AE_HEAD,"HEAD"],cwd=ROOT)
    assert git("rev-parse", f"{AE_HEAD}:stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json") == AE_CERT_BLOB
    assert git("rev-parse", f"{AE_HEAD}:stages/stage36/verify_stage36_36_09AE.py") == AE_VERIFIER_BLOB

    c=json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AF_VARIABLE_PRIME_JACOBI_MATRIX_REALIZABILITY_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    assert c["batch_parent"]["36_09AE_exact_head"] == AE_HEAD
    assert c["batch_parent"]["36_09AE_exact_head_ci"] == AE_CI

    # Exact same-fiber arithmetic.
    a,b=2,11
    M=a*a-2*a*b-b*b
    P=a*a+2*a*b-b*b
    D0=a*b*(a-b)*(a+b)
    assert (M,P,D0) == (-161,-73,-2574)
    assert M == -7*23
    assert P == -73
    assert D0 == -2*3*3*11*13
    assert a != 0 and a != b and a != -b and M != 0 and P != 0

    A,C,D=73,11,13
    B7,B23=7,23
    e=f=h=1
    assert abs(P)%A == 0
    assert abs(M)%B7 == 0 and abs(M)%B23 == 0
    assert b%C == 0 and (a+b)%D == 0
    assert (A%8,B7%8,C%8,D%8,e,f,h) == (1,7,3,5,1,1,1)
    assert (A%8,B23%8,C%8,D%8,e,f,h) == (1,7,3,5,1,1,1)

    ps7=pair_symbols(A,B7,C,D)
    ps23=pair_symbols(A,B23,C,D)
    assert ps7 == [-1,-1,1,-1,1,-1]
    assert ps23 == [1,-1,1,1,-1,-1]
    assert ps7 != ps23

    r7=rows(A,B7,C,D,e,f,h)
    r23=rows(A,B23,C,D,e,f,h)
    assert r7 == [1,1,1,1,1,1,1,1]
    assert r23 == [-1,-1,1,1,-1,1,-1,1]
    assert all(x==1 for x in r7)
    assert [i+1 for i,x in enumerate(r23) if x==-1] == [1,2,5,7]

    sh=c["shared_branch_skeleton"]
    assert sh["A_mod8"] == 1 and sh["B_mod8"] == 7 and sh["C_mod8"] == 3 and sh["D_mod8"] == 5
    assert sh["e"] == sh["f"] == sh["h"] == 1
    assert sh["AE_128_skeleton_member"] is True
    assert c["choice_B7"]["pair_symbols"] == ps7
    assert c["choice_B7"]["eight_selected_prime_jacobi_rows"] == r7
    assert c["choice_B23"]["pair_symbols"] == ps23
    assert c["choice_B23"]["eight_selected_prime_jacobi_rows"] == r23

    sep=c["exact_separation"]
    assert sep["same_parameter"] is True
    assert sep["same_A_B_C_D_mod8_skeleton"] is True
    assert sep["different_actual_B_prime_identity_inside_same_M_reservoir"] is True
    assert sep["different_pair_symbol_matrix"] is True
    assert sep["different_selected_prime_row_outcome"] is True

    out=c["conclusion"]
    assert out["mod8_skeleton_sufficient_for_selected_prime_rows"] is False
    assert out["reservoir_labels_plus_mod8_sufficient_for_selected_prime_rows"] is False
    assert out["actual_variable_prime_identity_load_bearing"] is True
    assert out["actual_pairwise_jacobi_matrix_load_bearing"] is True
    assert out["residue_only_compression_status"] == "BLOCKED_NEW_PATTERN_ISOLATED"
    assert out["full_variable_prime_jacobi_route_status"] == "LIVE"
    assert out["candidate_parameter_set_shrunk"] is False
    assert out["receiver_closed"] is False
    firewall=c["interpretation_firewall"]
    assert firewall["B7_choice_proves_conic_point"] is False
    assert firewall["B7_choice_proves_receiver_point"] is False

    st=json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V67_36_09AF_BATCH_AUDIT_CHECKPOINT"
    assert st["status"] == "ACTIVE_BATCH_HOSTILE_AUDIT_CHECKPOINT"
    af=st["authority_frontier"]["36-09AF"]
    assert af["SAME_FIBER_SAME_MOD8_PRIME_IDENTITY_SEPARATION"] is True
    assert af["MOD8_RESERVOIR_COMPRESSION_SUFFICIENT"] is False
    assert af["ACTUAL_PRIME_IDENTITY_LOAD_BEARING"] is True
    assert af["FULL_VARIABLE_PRIME_JACOBI_ROUTE_LIVE"] is True
    assert af["RECEIVER_CLOSED"] is False
    assert st["current"]["unit"] == "36-09AF-AUDIT-CHECKPOINT"
    assert st["current"]["next_owner"] == "HOSTILE_AUDIT"
    assert st["current"]["hostile_audit_checkpoint_reached"] is True
    assert st["current"]["36_09AG_entry_allowed"] is False
    assert st["promotion_gates"]["36_09AF_hostile_audit_passed"] is False
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09AF exact counterexample verified: same p=2/11, same mod-8/reservoir skeleton, B=7 vs 23 inside the same M reservoir changes the Jacobi matrix and selected-prime row outcome; residue-only compression blocked, actual variable-prime matrix remains live; AB-AF hostile-audit checkpoint reached")


if __name__ == "__main__":
    main()
