#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages" / "stage36" / "36-09AJ" / "congruent-number-full2-covering-class-preflight.json"
SOURCE = ROOT / "stages" / "stage36" / "36-09AJ" / "full2-homogeneous-space-source-lock.md"
AI = ROOT / "stages" / "stage36" / "36-09AI" / "j1728-congruent-number-jacobian-preflight.json"
AH = ROOT / "stages" / "stage36" / "36-09AH" / "common-uv-two-quadric-genusone-preflight.json"
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"

BASE = "652cbd51cd6b546f2a178597f7f2d3474c92b1c6"
AUDITED_HEAD = "4bfec87e1ce85608f87fc57e884fc026b5a715b8"
AUDIT_REVIEW = 5127180987
AUDIT_CI = "34070010830/101585489611"
CERT_BLOB = "cad74b5be80d877b2b804cce8aa218360b259af6"
SOURCE_BLOB = "cc16ef3a9ed5ca5d8924ddb9fd531197d68c2f0d"
AI_BLOB = "c5af6c4dde67532ea8d592e74aed187c72bbed4e"
AH_BLOB = "732431bef8dfafe25cbdeb005c4237d72a40ae4b"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def sf(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    p = 2
    out = 1
    while p * p <= n:
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            out *= p
        p += 1 if p == 2 else 2
    if n > 1:
        out *= n
    return sign * out


def add_exp(*vectors: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    return tuple(sum(v[i] for v in vectors) for i in range(4))  # type: ignore[return-value]


def mod2(v: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    return tuple(x & 1 for x in v)  # type: ignore[return-value]


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(AI) == AI_BLOB
    assert blob(AH) == AH_BLOB
    subprocess.check_call(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT)
    # PR #1674 was squash-merged.  Preserve hostile-audit provenance by
    # checking that the merged authority contains the exact audited math blobs,
    # rather than incorrectly requiring the pre-merge PR head to be an ancestor.
    assert git("rev-parse", f"{BASE}:stages/stage36/36-09AI/j1728-congruent-number-jacobian-preflight.json") == AI_BLOB
    assert git("rev-parse", f"{BASE}:stages/stage36/36-09AH/common-uv-two-quadric-genusone-preflight.json") == AH_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AJ_CONGRUENT_NUMBER_FULL2_COVERING_CLASS_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    ap = c["audited_parent"]
    assert ap["pr"] == 1674
    assert ap["hostile_audit_review"] == AUDIT_REVIEW
    assert ap["audited_exact_head"] == AUDITED_HEAD
    assert ap["exact_head_ci"] == AUDIT_CI
    assert ap["merged_main_sha"] == BASE

    # Exact monomial bookkeeping in variables (A,B,c,d).
    A = (1, 0, 0, 0)
    B = (0, 1, 0, 0)
    cc = (0, 0, 1, 0)
    dd = (0, 0, 0, 1)
    L = add_exp(A, cc, dd)
    T = add_exp(A, B, cc, dd)
    D1 = add_exp(A, A, cc, dd)
    D2 = add_exp(A, cc, cc, dd)
    D3 = add_exp(A, cc, dd, dd)
    assert add_exp(D1, D2, D3) == tuple(4 * x for x in L)
    assert mod2(D1) == mod2(add_exp(cc, dd))
    assert mod2(D2) == mod2(add_exp(A, dd))
    assert mod2(D3) == mod2(add_exp(A, cc))
    assert mod2(add_exp(D1, D2, D3)) == (0, 0, 0, 0)
    assert T == (1, 1, 1, 1)

    rewrite = c["exact_homogeneous_space_rewrite"]
    assert rewrite["common_multiplier"] == "L=A*c*d"
    assert rewrite["D1"] == "A^2*c*d"
    assert rewrite["D2"] == "A*c^2*d"
    assert rewrite["D3"] == "A*c*d^2"
    assert rewrite["rewritten_equations"] == [
        "D1*u^2-D2*r^2=T*v^2",
        "D1*u^2-D3*s^2=-T*v^2",
    ]
    assert rewrite["product_identity"] == "D1*D2*D3=(A*c*d)^4=L^4"

    cls = c["full2_squareclass"]
    assert cls["ordered_triple_raw_ET"] == ["[c*d]", "[A*d]", "[A*c]"]
    assert cls["expanded"] == [
        "[eta*2^(e+f)*C*D]",
        "[2^f*A*D]",
        "[eta*2^e*A*C]",
    ]
    assert cls["product_trivial_in_Qstar_mod_squares"] is True
    assert cls["unordered_class_transport_exact"] is True

    A0, C0, D0, eta, e, f = 73, 11, 13, -1, 1, 1
    c0 = eta * (2**e) * C0
    d0 = (2**f) * D0
    triple = [sf(c0 * d0), sf(A0 * d0), sf(A0 * c0)]
    assert triple == [-143, 1898, -1606]
    ex = c["AF_same_skeleton_examples"]
    assert ex["shared_squareclass_triple_representatives"] == triple
    for key, B0, T0, n0 in (
        ("B7", 7, -292292, 73073),
        ("B23", 23, -960388, 240097),
    ):
        Tcalc = A0 * B0 * c0 * d0
        assert Tcalc == T0
        assert sf(Tcalc) == -n0
        assert ex[key]["B"] == B0
        assert ex[key]["T"] == T0
        assert ex[key]["normalized_n"] == n0

    support = c["support_structure"]
    assert support["B_occurs_in_class_components"] is False
    assert support["new_dynamic_UV_prime_support"] is False
    assert support["fixed_finite_S_recovered"] is False

    out = c["route_result"]
    assert out["H1_full2_class_identified"] is True
    assert out["Selmer_membership_proved"] is False
    assert out["covering_locally_solvable_everywhere_proved"] is False
    assert out["covering_class_trivialized"] is False
    assert out["receiver_closed"] is False
    assert out["next_leaf"] == "36-09AK_FULL2_COVERING_LOCAL_SOLVABILITY_PREFLIGHT"

    st = json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V72_36_09AJ_CANDIDATE"
    assert st["base_main_sha"] == BASE
    assert st["audited_batch_promotion"]["candidate_pr"] == 1674
    assert st["audited_batch_promotion"]["hostile_audit_review"] == AUDIT_REVIEW
    assert st["promotion_gates"]["36_09AI_hostile_audit_passed"] is True
    aj = st["authority_frontier"]["36-09AJ"]
    assert aj["H1_FULL2_CLASS_IDENTIFIED"] is True
    assert aj["SELMER_MEMBERSHIP_PROVED"] is False
    assert aj["COVERING_CLASS_TRIVIALIZED"] is False
    assert st["current"]["unit"] == "36-09AK"
    assert st["current"]["36_09AK_entry_allowed"] is True
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09AJ exact full-2 class verified: multiply by L=A*c*d to obtain the standard E_T homogeneous space; class=([c*d],[A*d],[A*c]) with trivial product; Selmer/MW/receiver credit remains false; 36-09AK unlocked")


if __name__ == "__main__":
    main()
