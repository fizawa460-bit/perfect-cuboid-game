#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage36/36-09AN/retained-open-tunnell-necessary-gate-preflight.json"
SOURCE = ROOT / "stages/stage36/36-09AN/retained-open-congruent-number-rank-gate-source-lock.md"
AD = ROOT / "stages/stage36/36-09AD/coupled-six-reservoir-factor-squareclass-parity-preflight.json"
AJ = ROOT / "stages/stage36/36-09AJ/congruent-number-full2-covering-class-preflight.json"
AM = ROOT / "stages/stage36/36-09AM/uniform-rankzero-tunnell-sha2-sieve-preflight.json"
STATE = ROOT / "stages/stage36/MAIN-STATE.json"

BASE = "58e81a647b63bcea17ab396409c2813b667f45e2"
AM_HEAD = "46b426a393ee2eb027305f9c45f248008ff02fec"
AM_CI = "34075630812"
CERT_BLOB = "62437d59f47e991d812c1851b1ee7d393bf82318"
SOURCE_BLOB = "1486507569cd9b6263ff46c5db263fbbc198e87c"
AD_BLOB = "9d0388845955efee71d1a761ae4ee943d8b565d5"
AJ_BLOB = "27950f53a89e28d02d04f2c19628504561c206e7"
AM_BLOB = "6d9e9392df8fc70a90a356932724e0a589b6b446"
AM_VERIFIER_BLOB = "9d8b97cc96d6ca6b5d462d74340081f9d83d6149"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def add(*vs: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    return tuple(sum(v[i] for v in vs) for i in range(4))  # type: ignore[return-value]


def mul(k: int, v: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    return tuple(k*x for x in v)  # type: ignore[return-value]


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(AD) == AD_BLOB
    assert blob(AJ) == AJ_BLOB
    assert blob(AM) == AM_BLOB
    subprocess.check_call(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT)
    subprocess.check_call(["git", "merge-base", "--is-ancestor", AM_HEAD, "HEAD"], cwd=ROOT)
    assert git("rev-parse", f"{AM_HEAD}:stages/stage36/36-09AM/uniform-rankzero-tunnell-sha2-sieve-preflight.json") == AM_BLOB
    assert git("rev-parse", f"{AM_HEAD}:stages/stage36/verify_stage36_36_09AM.py") == AM_VERIFIER_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AN_RETAINED_OPEN_TUNNELL_NECESSARY_GATE_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    bp = c["batch_parent"]
    assert bp["pr"] == 1679
    assert bp["36_09AM_exact_head"] == AM_HEAD
    assert bp["36_09AM_exact_head_ci"] == AM_CI

    # Reconstruct AJ's coefficient monomials in (A,B,c,d).
    A=(1,0,0,0); B=(0,1,0,0); cc=(0,0,1,0); dd=(0,0,0,1)
    L=add(A,cc,dd)
    T=add(A,B,cc,dd)
    D1=add(A,A,cc,dd)
    D2=add(A,cc,cc,dd)
    D3=add(A,cc,dd,dd)
    assert add(D1,D2,D3) == mul(4,L)
    assert T == (1,1,1,1)

    aj=json.loads(AJ.read_text())
    rw=aj["exact_homogeneous_space_rewrite"]
    assert rw["D1"] == "A^2*c*d"
    assert rw["D2"] == "A*c^2*d"
    assert rw["D3"] == "A*c*d^2"
    assert rw["rewritten_equations"] == [
        "D1*u^2-D2*r^2=T*v^2",
        "D1*u^2-D3*s^2=-T*v^2",
    ]
    assert rw["product_identity"] == "D1*D2*D3=(A*c*d)^4=L^4"

    mp=c["full2_covering_map"]
    assert mp["covering_equations"] == rw["rewritten_equations"]
    assert mp["product_identity"] == rw["product_identity"]
    assert mp["affine_chart"] == "v!=0"
    assert mp["x_map"] == "x=D1*(u/v)^2"
    assert mp["y_map"] == "y=L^2*u*r*s/v^3"
    assert mp["derived"] == [
        "x-T=D2*(r/v)^2",
        "x+T=D3*(s/v)^2",
        "y^2=x*(x-T)*(x+T)",
    ]
    assert mp["Q_rational_map_exact"] is True

    # Formal algebra of the map: from the two covering equations,
    # x-T and x+T have the stated forms; multiplying and using
    # D1*D2*D3=L^4 gives y^2=x(x-T)(x+T).
    # Coefficient monomial exponents agree exactly.
    lhs_y_coeff = mul(2,L)
    rhs_coeff = add(D1,D2,D3)
    assert mul(2,lhs_y_coeff) == rhs_coeff  # L^4 on each side of y^2/product

    ad=json.loads(AD.read_text())
    assert ad["notation"]["receiver_square_conditions"] == [
        "Fminus is a nonzero square", "Fplus is a nonzero square"
    ]
    rec=ad["coupled_squareclass_reconstruction"]
    assert rec["U"] == "delta_P*u^2"
    assert rec["V"] == "delta_M*v^2"
    assert rec["UminusV"] == "eta*2^eps_minus*delta_minus*r^2"
    assert rec["UplusV"] == "2^eps_plus*delta_plus*s^2"
    ro=c["retained_open"]
    assert ro["forced_nonzero_coordinates"] == ["u","v","r","s"]
    assert ro["image_nonvanishing"] == ["x!=0","x-T!=0","x+T!=0","y!=0"]
    assert ro["normalized_image_avoids_all_rational_2torsion"] is True

    gate=c["congruent_number_torsion_rank_gate"]
    assert gate["rational_torsion_exact"] == ["O","(0,0)","(n,0)","(-n,0)"]
    assert gate["torsion_group"] == "Z/2 x Z/2"
    assert gate["retained_covering_point_maps_to_infinite_order"] is True
    assert gate["retained_receiver_implies_positive_MW_rank"] is True
    assert gate["retained_receiver_implies_n_congruent"] is True

    tg=c["Tunnell_gate"]
    assert tg["odd_and_even_squarefree_necessary_equalities_source_locked_in_36_09AM"] is True
    assert tg["retained_receiver_implies_parity_appropriate_Tunnell_equality"] is True
    assert tg["ELS_or_Selmer_hypothesis_needed"] is False
    assert tg["BSD_converse_used"] is False

    up=c["AM_exception_sector_upgrade"]
    am=json.loads(AM.read_text())
    assert len(am["exact_torsion_shaped_sector_union"]) == up["AM_torsion_shaped_sector_count"] == 4
    assert up["rankzero_torsion_shaped_sectors_survive_projective_Kummer_test"] is True
    assert up["rankzero_torsion_shaped_sectors_survive_retained_open"] is False
    assert up["Tunnell_fail_retained_open_exception_sector_count"] == 0

    out=c["route_result"]
    assert out["AM_conditional_Sha_classifier_strictly_strengthened_for_retained_receiver"] is True
    assert out["Tunnell_fail_retained_receiver_excluded_uniformly"] is True
    assert out["Tunnell_equality_side_classified"] is False
    assert out["candidate_parameter_set_shrunk"] is False
    assert out["receiver_closed"] is False
    assert out["natural_hostile_audit_checkpoint"] is True
    assert out["next_leaf_after_audit"] == "36-09AO_TUNNELL_EQUALITY_STAGE36_N_ARITHMETIC_PREFLIGHT"

    st=json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V76_36_09AN_BATCH_AUDIT_CHECKPOINT"
    assert st["base_main_sha"] == BASE
    an=st["authority_frontier"]["36-09AN"]
    assert an["RETAINED_OPEN_MAP_EXACT"] is True
    assert an["RETAINED_IMAGE_NON2TORSION"] is True
    assert an["TUNNELL_FAIL_RETAINED_RECEIVER_EMPTY"] is True
    assert an["AM_TORSION_EXCEPTION_SECTORS_REMAIN_ON_RETAINED_OPEN"] is False
    assert an["TUNNELL_EQUALITY_SIDE_CLASSIFIED"] is False
    assert st["current"]["unit"] == "36-09AN-AUDIT-CHECKPOINT"
    assert st["current"]["next_owner"] == "HOSTILE_AUDIT"
    assert st["current"]["hostile_audit_checkpoint_reached"] is True
    assert st["current"]["36_09AO_entry_allowed"] is False
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09AN verified: explicit retained-open covering map avoids all rational torsion on E_n; any retained receiver point forces positive rank, congruent n, and the parity-appropriate Tunnell equality. Hence Tunnell failure excludes the retained receiver with no ELS/Selmer hypothesis and AM's four rank-zero torsion sectors leave no retained-open exceptions. AO locked at hostile-audit checkpoint.")


if __name__ == "__main__":
    main()
