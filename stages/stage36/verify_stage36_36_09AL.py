#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage36/36-09AL/b7-selmer-class-nontrivial-sha2-preflight.json"
SOURCE = ROOT / "stages/stage36/36-09AL/tunnell-mw-sha-source-lock.md"
AK = ROOT / "stages/stage36/36-09AK/b7-everywhere-local-full2-covering-preflight.json"
AJ = ROOT / "stages/stage36/36-09AJ/congruent-number-full2-covering-class-preflight.json"
STATE = ROOT / "stages/stage36/MAIN-STATE.json"

BASE = "4e6708cb807cc37bea6509245447a5817965256f"
AK_HEAD = "df566ff40260dad7a11067782841e521d33cf4cd"
AK_CI = "34073718579"
CERT_BLOB = "10962f8d2471a8236d66a602c0f4952ce497e56c"
SOURCE_BLOB = "f6ed54e24fce21722aeb89ffe6fa8368ce2b4dee"
AK_BLOB = "05bf95344372b362be47d11df7f930e72fa8ee18"
AK_VERIFIER_BLOB = "d60a58e64d7f91f96cae47f677b6aac9aa64ac79"
AJ_BLOB = "27950f53a89e28d02d04f2c19628504561c206e7"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def squarefree_rep(n: int) -> int:
    if n == 0:
        raise ValueError("squareclass representative must be nonzero")
    sign = -1 if n < 0 else 1
    n = abs(n)
    out = 1
    p = 2
    while p * p <= n:
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            out *= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out *= n
    return sign * out


def count_signed_ternary(n: int, zcoef: int) -> int:
    # Counts all signed integer triples satisfying n=2*x^2+y^2+zcoef*z^2.
    total = 0
    xmax = math.isqrt(n // 2)
    zmax = math.isqrt(n // zcoef)
    for x in range(-xmax, xmax + 1):
        remx = n - 2 * x * x
        if remx < 0:
            continue
        for z in range(-zmax, zmax + 1):
            rem = remx - zcoef * z * z
            if rem < 0:
                continue
            y = math.isqrt(rem)
            if y * y == rem:
                total += 1 if y == 0 else 2
    return total


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(AK) == AK_BLOB
    assert blob(AJ) == AJ_BLOB
    subprocess.check_call(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT)
    subprocess.check_call(["git", "merge-base", "--is-ancestor", AK_HEAD, "HEAD"], cwd=ROOT)
    assert git("rev-parse", f"{AK_HEAD}:stages/stage36/36-09AK/b7-everywhere-local-full2-covering-preflight.json") == AK_BLOB
    assert git("rev-parse", f"{AK_HEAD}:stages/stage36/verify_stage36_36_09AK.py") == AK_VERIFIER_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AL_B7_SELMER_CLASS_NONTRIVIAL_SHA2_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    bp = c["batch_parent"]
    assert bp["pr"] == 1677
    assert bp["36_09AK_exact_head"] == AK_HEAD
    assert bp["36_09AK_exact_head_ci"] == AK_CI

    b = c["branch"]
    n = b["n"]
    assert n == 73073 == 7 * 11 * 13 * 73
    assert b["factorization"] == [7, 11, 13, 73]
    assert all(n % (p * p) != 0 for p in b["factorization"])
    assert n & 1

    # Tunnell counts are recomputed exhaustively from the defining ternary forms.
    a32 = count_signed_ternary(n, 32)
    a8 = count_signed_ternary(n, 8)
    assert (a32, a8) == (480, 896)
    te = c["tunnell_exact_enumeration"]
    assert te["A32_signed_integer_triple_count"] == a32
    assert te["A8_signed_integer_triple_count"] == a8
    assert te["lhs_2A32"] == 2 * a32 == 960
    assert te["rhs_A8"] == a8 == 896
    assert 2 * a32 != a8
    assert te["necessary_equality_fails"] is True
    assert te["Mordell_Weil_rank_E73073"] == 0
    assert te["BSD_converse_used"] is False

    # AK supplies actual everywhere-local solubility/Selmer membership.
    ak = json.loads(AK.read_text())
    assert ak["global_local_conclusion"]["covering_everywhere_locally_soluble"] is True
    assert ak["global_local_conclusion"]["AJ_H1_class_lies_in_2Selmer_of_E73073"] is True
    assert b["AK_covering_everywhere_locally_soluble"] is True
    assert b["AK_class_in_Sel2"] is True

    # AJ raw ordering (0,T,-T), T=-4n, scales to (0,-n,+n); standard
    # normalized order (0,+n,-n) therefore swaps components 2 and 3.
    aj = json.loads(AJ.read_text())
    raw = aj["AF_same_skeleton_examples"]["shared_squareclass_triple_representatives"]
    assert raw == [-143, 1898, -1606]
    order = c["normalized_full2_ordering"]
    assert order["B7_T"] == -4 * n == -292292
    normalized_triple = [raw[0], raw[2], raw[1]]
    normalized_pair = normalized_triple[:2]
    assert normalized_triple == [-143, -1606, 1898]
    assert normalized_pair == [-143, -1606]
    assert order["normalized_triple_representatives"] == normalized_triple
    assert order["normalized_pair_representative"] == normalized_pair
    assert squarefree_rep(normalized_triple[0] * normalized_triple[1] * normalized_triple[2]) == 1

    # Kummer image of E(Q)/2E(Q). Tunnell gives rank zero. The three
    # nonzero 2-torsion images below are nontrivial, so none is divisible
    # by 2 and there is no rational 4-torsion. Odd torsion is 2-divisible,
    # hence contributes nothing mod 2. Thus these four classes exhaust.
    mw_pairs = [
        [1, 1],
        [-1, -n],
        [n, 2],
        [-n, -2 * n],
    ]
    assert all([squarefree_rep(x), squarefree_rep(y)] == [x, y] for x, y in mw_pairs)
    assert mw_pairs[1] != [1, 1] and mw_pairs[2] != [1, 1] and mw_pairs[3] != [1, 1]
    assert normalized_pair not in mw_pairs
    km = c["Mordell_Weil_mod2_Kummer_image"]
    assert km["pair_classes"] == mw_pairs
    assert km["covering_pair"] == normalized_pair
    assert km["rank_zero"] is True
    assert km["nonzero_2torsion_not_divisible_by_2"] is True
    assert km["rational_4torsion_absent"] is True
    assert km["E_Q_mod_2E_exhausted_by_four_2torsion_classes"] is True
    assert km["covering_pair_in_MW_Kummer_image"] is False

    sh = c["Selmer_to_Sha_conclusion"]
    assert sh["covering_class_in_Sel2"] is True
    assert sh["covering_class_in_MW_Kummer_image"] is False
    assert sh["covering_class_maps_to_nonzero_Sha2"] is True
    assert sh["Sha_E73073_2_nontrivial"] is True
    assert sh["covering_has_Q_point"] is False
    assert sh["B7_branch_receiver_point_exists"] is False

    out = c["route_result"]
    assert out["B7_MW_vs_Sha_dichotomy_resolved"] == "NONTRIVIAL_SHA2"
    assert out["explicit_branch_globally_excluded"] is True
    assert out["uniform_branch_family_classified"] is False
    assert out["candidate_parameter_set_shrunk"] is False
    assert out["receiver_closed"] is False
    assert out["natural_hostile_audit_checkpoint"] is True

    st = json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V74_36_09AL_BATCH_AUDIT_CHECKPOINT"
    assert st["base_main_sha"] == BASE
    al = st["authority_frontier"]["36-09AL"]
    assert al["B7_TUNNELL_NONCONGRUENT"] is True
    assert al["B7_MW_RANK"] == 0
    assert al["B7_CLASS_IN_2SELMER"] is True
    assert al["B7_CLASS_IN_MW_KUMMER_IMAGE"] is False
    assert al["B7_SHA2_NONTRIVIAL"] is True
    assert al["B7_COVERING_Q_POINT_EXISTS"] is False
    assert st["current"]["unit"] == "36-09AL-AUDIT-CHECKPOINT"
    assert st["current"]["next_owner"] == "HOSTILE_AUDIT"
    assert st["current"]["hostile_audit_checkpoint_reached"] is True
    assert st["current"]["36_09AM_entry_allowed"] is False
    assert st["claims"]["B7_class_nontrivial_in_Sha2_provisional"] is True
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09AL verified: Tunnell counts 480/896 violate the odd congruent necessary equality; rank E_73073(Q)=0; normalized covering class (-143,-1606) is outside the four MW mod-2 Kummer classes while AK puts it in Sel^2; hence it gives a nonzero Sha(E_73073)[2] class and the explicit B7 covering has no Q-point; AM locked at hostile-audit checkpoint")


if __name__ == "__main__":
    main()
