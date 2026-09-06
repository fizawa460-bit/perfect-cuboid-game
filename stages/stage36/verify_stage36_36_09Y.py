#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages" / "stage36" / "36-09Y" / "kummer-complement-prime-2adic-hilbert-preflight.json"
X_CERT = ROOT / "stages" / "stage36" / "36-09X" / "kummer-class-coupled-hilbert-local-solvability-preflight.json"
X_VERIFIER = ROOT / "stages" / "stage36" / "verify_stage36_36_09X.py"
Q2_CARD = ROOT / "docs" / "stage14-toolbox" / "cards" / "TB-FORMULA-q2-hilbert-symbol.md"
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"

BASE = "f8522bd1a38fa551186ad370f51d17c73c7927e2"
X_HEAD = "fbb418d7cc2a5a58cf79391d90ff71a4017f72cd"
CERT_BLOB = "20c6d782e59bff820392731ec81653d15b2d1921"
X_CERT_BLOB = "3eb6e42b563ee2b5042917467a62e7606f27a869"
X_VERIFIER_BLOB = "a511b1830f6a3fa91cdae180dddee81c1c360bea"
Q2_CARD_BLOB = "f19870f56c2c8f608b53991672cfe9a6ecf09644"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def vals(a: int, b: int) -> tuple[int, int, int]:
    S = a * a + b * b
    C = a**4 - 6 * a * a * b * b + b**4
    D = a * b * (a - b) * (a + b)
    return S, C, D


def legendre(x: int, q: int) -> int:
    x %= q
    if x == 0:
        return 0
    r = pow(x, (q - 1) // 2, q)
    return 1 if r == 1 else -1


def v2(n: int) -> int:
    n = abs(n)
    assert n
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(X_CERT) == X_CERT_BLOB
    assert blob(X_VERIFIER) == X_VERIFIER_BLOB
    assert blob(Q2_CARD) == Q2_CARD_BLOB
    assert git("merge-base", "--is-ancestor", BASE, "HEAD") == ""
    assert git("rev-parse", f"{X_HEAD}:stages/stage36/36-09X/kummer-class-coupled-hilbert-local-solvability-preflight.json") == X_CERT_BLOB
    assert git("rev-parse", f"{X_HEAD}:stages/stage36/verify_stage36_36_09X.py") == X_VERIFIER_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09Y_KUMMER_COMPLEMENT_PRIME_2ADIC_HILBERT_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    assert c["batch_parent"]["36_09X_exact_head"] == X_HEAD
    assert c["source_locks"]["stage14_q2_hilbert_formula"]["blob_sha"] == Q2_CARD_BLOB

    # Exact polynomial identities behind all cross-sector reductions.
    for a in range(-8, 9):
        for b in range(-8, 9):
            if not a or not b or math.gcd(a, b) != 1 or a == b or a == -b:
                continue
            S, C, D = vals(a, b)
            assert S**4 == C**2 + 16 * D**2
            # These are the two completed-square identities used modulo D and C.
            for d in (1, 3, 5, 7):
                z = 2
                lhs_a_num = d * (d * z**4 - 2 * S**2 * z**2) + C**2
                rhs_a = (d * z**2 - S**2) ** 2 - 16 * D**2
                assert lhs_a_num == rhs_a
            for e in (1, 3, 5, 7):
                z = 2
                lhs_b_num = e * (e * z**4 + 4 * S**2 * z**2) + 64 * D**2
                rhs_b = (e * z**2 + 2 * S**2) ** 2 - 4 * C**2
                assert lhs_b_num == rhs_b

    olm = c["odd_local_matrix"]
    assert olm["alpha_cross_D0_prime"]["exact_result"] == "Q_r-soluble iff (d/r)=+1"
    assert olm["beta_cross_C0_prime"]["exact_result"] == "Q_r-soluble iff (e/r)=+1"
    assert olm["alpha_unselected_C0_prime"]["result"] == "automatic Q_q-solubility"
    assert olm["beta_unselected_D0_prime"]["result"] == "automatic Q_q-solubility"

    # Alpha 2-adic valuation lock when 2 is selected: for odd a,b, v2(S)=1 and v2(C)=2.
    for a in range(1, 16, 2):
        for b in range(1, 16, 2):
            if math.gcd(a, b) != 1 or a == b:
                continue
            S, C, _ = vals(a, b)
            assert v2(S) == 1
            assert v2(C) == 2
    a2 = c["alpha_two_adic_and_real_classification"]
    assert a2["two_selected_case"]["result"].startswith("no Q2-point")
    assert "d=1 mod 8" in a2["two_unselected_case"]["consequence"]

    # Exact alpha bad-place witness.
    S, C, D = vals(14, 13)
    assert (S, C, D) == (365, -131767, 4914)
    assert C == -(17 * 23 * 337)
    assert D == 2 * 3**3 * 7 * 13
    assert 337 % 8 == 1
    assert [legendre(337, q) for q in (3, 7, 13)] == [1, 1, 1]

    # Exact nonbaseline beta bad-place witness and Q2 square criterion.
    S, C, D = vals(5, 2)
    assert (S, C, D) == (29, 41, 210)
    e, z = 5, 1
    rhs = e * z**4 + 4 * S**2 * z**2 + 64 * D**2 // e
    assert rhs == 567849
    assert rhs % 8 == 1
    assert legendre(e, 41) == 1
    # Rational beta baseline is {1,-1, +/-2D}; squarefree kernel of 2D=420 is 105.
    assert 420 == 4 * 105
    assert e not in (1, -1, 105, -105)

    rb = c["reciprocity_route_boundary"]
    assert rb["class_coupled_odd_rows_derived"] is True
    assert rb["alpha_Q2_infinity_boundary_derived"] is True
    assert rb["beta_complete_Q2_image_classified"] is False
    assert rb["support_place_local_conditions_uniformly_exclude_nontrivial_alpha_classes"] is False
    assert rb["support_place_local_conditions_uniformly_exclude_nonbaseline_beta_classes"] is False
    assert rb["multiplace_reciprocity_obstruction_proved"] is False

    assert c["next_leaf"] == "36-09Z_2ISOGENY_SELMER_TO_MW_CASSELS_PAIRING_PREFLIGHT"

    st = json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V59_36_09Y_BATCHED"
    assert st["base_main_sha"] == BASE
    y = st["authority_frontier"]["36-09Y"]
    assert y["certificate_blob_sha"] == CERT_BLOB
    assert y["COMPLETE_ODD_LOCAL_MATRIX"] is True
    assert y["ALPHA_Q2_INFINITY_CLASSIFIED"] is True
    assert y["B11_LOCAL_SOLVABILITY_ONLY_UNIFORM_CLOSURE_BLOCKED"] is True
    assert y["GLOBAL_SELMER_TO_MW_DISTINCTION_LIVE"] is True
    assert y["MULTIPLACE_RECIPROCITY_OBSTRUCTION_PROVED"] is False
    assert st["current"]["unit"] == "36-09Z"
    assert st["current"]["36_09Z_entry_allowed"] is True
    assert st["promotion_gates"]["36_09Y_hostile_audit_passed"] is False
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09Y odd cross-sector local matrix and alpha Q2/infinity boundary verified; pure local B11 closure blocked; Selmer-to-MW/Cassels route unlocked")


if __name__ == "__main__":
    main()
