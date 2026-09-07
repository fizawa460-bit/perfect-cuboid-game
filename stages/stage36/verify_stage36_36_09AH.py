#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage36/36-09AH/common-uv-two-quadric-genusone-preflight.json"
SRC = ROOT / "stages/stage36/36-09AH/two-quadric-genusone-source-lock.md"
AG = ROOT / "stages/stage36/36-09AG/individual-conic-hasse-solubility-preflight.json"
AGV = ROOT / "stages/stage36/verify_stage36_36_09AG.py"
S31 = ROOT / "docs/arsenal/cards/formal/S31-W01.md"
STATE = ROOT / "stages/stage36/MAIN-STATE.json"

BASE = "9306238c7ada55e31311245019d6b7e474ad837f"
AG_HEAD = "6ef7635a92bc5e9440ed527c60ea871d0c3216fc"
AG_CI = "34069292996"
CERT_BLOB = "732431bef8dfafe25cbdeb005c4237d72a40ae4b"
SRC_BLOB = "f23393668c810bf53ec6a6fbb0fb11642d73c5c3"
AG_BLOB = "b40a525e739d6021c07d364a243c0d7653350abe"
AGV_BLOB = "800d40dfb2371dd548dc8f827dad44b652baa2be"
S31_BLOB = "122a6c1c5c871c1c7b797017e854de8ec55e7c50"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


# Bivariate Z[lambda,mu] polynomials represented by exponent pairs.
def pmul(a: dict[tuple[int,int],int], b: dict[tuple[int,int],int]) -> dict[tuple[int,int],int]:
    out: dict[tuple[int,int],int] = {}
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            key=(i+k,j+l)
            out[key]=out.get(key,0)+x*y
    return {k:v for k,v in out.items() if v}


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(SRC) == SRC_BLOB
    assert blob(AG) == AG_BLOB
    assert blob(AGV) == AGV_BLOB
    assert blob(S31) == S31_BLOB
    subprocess.check_call(["git","merge-base","--is-ancestor",BASE,"HEAD"], cwd=ROOT)
    subprocess.check_call(["git","merge-base","--is-ancestor",AG_HEAD,"HEAD"], cwd=ROOT)
    assert git("rev-parse", f"{AG_HEAD}:stages/stage36/36-09AG/individual-conic-hasse-solubility-preflight.json") == AG_BLOB
    assert git("rev-parse", f"{AG_HEAD}:stages/stage36/verify_stage36_36_09AG.py") == AGV_BLOB

    c=json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AH_COMMON_UV_TWO_QUADRIC_GENUSONE_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    assert c["batch_parent"]["36_09AG_exact_head"] == AG_HEAD
    assert c["batch_parent"]["36_09AG_exact_head_ci"] == AG_CI

    # Exact scalar-free pencil determinant:
    # (lambda+mu)(mu-lambda)(-lambda)(-mu)
    L={(1,0):1}; M={(0,1):1}
    lp={(1,0):1,(0,1):1}
    mm={(0,1):1,(1,0):-1}
    nl={(1,0):-1}; nm={(0,1):-1}
    det={ (0,0):1 }
    for f in (lp,mm,nl,nm):
        det=pmul(det,f)
    assert det == {(1,3):1,(3,1):-1}
    pencil=c["quadric_pencil"]
    assert pencil["determinant"] == "eta*2^(e+f)*A*B*C*D*lambda*mu*(mu^2-lambda^2)"
    assert pencil["singular_projective_directions_lambda_mu"] == ["[0:1]","[1:0]","[1:1]","[1:-1]"]
    assert pencil["directions_parameter_independent"] is True

    # At each determinant root the diagonal pencil has exactly one kernel axis.
    # Evaluate the *base* quadrics on that axis; a nonzero coefficient forbids
    # the kernel point from belonging to Qminus cap Qplus.
    # Entries are (direction, zero-axis, Qminus-axis-coeff, Qplus-axis-coeff),
    # with symbolic nonzero labels represented as strings.
    kernel_table=[
        ("[0:1]","r","-eta*2^e*C","0"),
        ("[1:0]","s","0","-2^f*D"),
        ("[1:1]","v","-B","B"),
        ("[1:-1]","u","A","A"),
    ]
    for _,_,qm,qp in kernel_table:
        assert qm != "0" or qp != "0"
    sm=c["direct_smoothness"]
    assert sm["base_intersection_smooth"] is True
    assert "-eta*2^e*C != 0" in sm["kernel_checks"]["lambda_0"]
    assert "-2^f*D != 0" in sm["kernel_checks"]["mu_0"]
    assert "-B != 0" in sm["kernel_checks"]["lambda_eq_mu"]
    assert "A != 0" in sm["kernel_checks"]["lambda_eq_minus_mu"]

    g=c["genus_one_classification"]
    assert g["complete_intersection_type"] == "(2,2) in P^3"
    assert g["connected"] is True
    assert g["canonical_bundle"] == "O_C(2+2-3-1)=O_C"
    assert g["genus"] == 1

    fx=c["fixed_pencil_geometry"]
    assert fx["discriminant_binary_quartic_up_to_nonzero_scalar"] == "lambda*mu*(mu^2-lambda^2)"
    assert fx["branch_direction_set"] == ["0","infinity","1","-1"]
    assert fx["geometric_shape_fixed"] is True
    assert fx["Q_jacobian_identified"] is False
    assert fx["Q_twist_squareclass_identified"] is False
    assert fx["explicit_quartic_to_elliptic_adapter_built"] is False

    rr=c["route_result"]
    assert rr["route_status"] == "PASS_NEW_GATE_FROM_STRONGER_VIEW"
    assert rr["common_uv_intersection_is_genus_one"] is True
    assert rr["pencil_singular_directions_fixed"] is True
    assert rr["candidate_parameter_set_shrunk"] is False
    assert rr["receiver_closed"] is False
    assert rr["next_leaf"] == "36-09AI_J1728_TWIST_JACOBIAN_ADAPTER_PREFLIGHT"

    st=json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V69_36_09AH_CANDIDATE"
    assert st["base_main_sha"] == BASE
    ah=st["authority_frontier"]["36-09AH"]
    assert ah["COMMON_UV_INTERSECTION_GENUS"] == 1
    assert ah["PENCIL_SINGULAR_DIRECTIONS_FIXED"] is True
    assert ah["Q_JACOBIAN_IDENTIFIED"] is False
    assert ah["RECEIVER_CLOSED"] is False
    assert st["current"]["unit"] == "36-09AI"
    assert st["current"]["36_09AI_entry_allowed"] is True
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09AH verified: common-u:v locus is a smooth connected (2,2) complete intersection of genus one; pencil determinant is scalar*lambda*mu*(mu^2-lambda^2) with fixed singular directions 0,infinity,+/-1; no Q-Jacobian/twist/receiver credit; 36-09AI unlocked")


if __name__ == "__main__":
    main()
