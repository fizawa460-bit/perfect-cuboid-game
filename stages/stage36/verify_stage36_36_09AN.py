#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage36/36-09AN/tunnell-filter-residue-noncompression-preflight.json"
AM = ROOT / "stages/stage36/36-09AM/uniform-congruent-covering-mw-sha-classifier-preflight.json"
AMSRC = ROOT / "stages/stage36/36-09AM/tunnell-uniform-branch-filter-source-lock.md"
AF = ROOT / "stages/stage36/36-09AF/variable-prime-jacobi-matrix-realizability-preflight.json"
STATE = ROOT / "stages/stage36/MAIN-STATE.json"

BASE = "24215fa27a631cd3cb370c0dfd76866dd2e916f1"
AM_HEAD = "73ab4ac138593af9712b735df9e543404bf7ab4c"
AM_CI = "34076651441/101603969844"
CERT_BLOB = "7bc094390cd4d82d9dee6959eb934185c8c4c492"
AM_BLOB = "cc9f74ed60680883e6b21ea555b3dfbd9dc3978c"
AM_VERIFIER_BLOB = "33a037e91a21e72f7ee6120aafcff168689a2b1b"
AMSRC_BLOB = "80cc32fb32417db74740152192df4fffc8be69c6"
AF_BLOB = "be5a65e3fcfb182998ccb02ec42f8114b50b0a7d"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def counts(n: int) -> tuple[int, int]:
    a = 1 if n & 1 else 2
    m = n // a
    even = odd = 0
    xmax = math.isqrt(m // (2 * a)) if m >= 2 * a else 0
    zmax = math.isqrt(m // 8)
    for x in range(-xmax, xmax + 1):
        r1 = m - 2 * a * x * x
        if r1 < 0:
            continue
        for z in range(-zmax, zmax + 1):
            r = r1 - 8 * z * z
            if r < 0:
                continue
            y = math.isqrt(r)
            if y * y == r:
                mult = 1 if y == 0 else 2
                if z & 1:
                    odd += mult
                else:
                    even += mult
    return even, odd


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(AM) == AM_BLOB
    assert blob(AMSRC) == AMSRC_BLOB
    assert blob(AF) == AF_BLOB
    subprocess.check_call(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT)
    subprocess.check_call(["git", "merge-base", "--is-ancestor", AM_HEAD, "HEAD"], cwd=ROOT)
    assert git("rev-parse", f"{AM_HEAD}:stages/stage36/36-09AM/uniform-congruent-covering-mw-sha-classifier-preflight.json") == AM_BLOB
    assert git("rev-parse", f"{AM_HEAD}:stages/stage36/verify_stage36_36_09AM.py") == AM_VERIFIER_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AN_TUNNELL_FILTER_RESIDUE_NONCOMPRESSION_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    bp = c["batch_parent"]
    assert bp["pr"] == 1680
    assert bp["36_09AM_exact_head"] == AM_HEAD
    assert bp["36_09AM_exact_head_ci"] == AM_CI

    p = c["same_parameter"]
    assert (p["a"], p["b"], p["M"], p["P"], p["D0"]) == (2, 11, -161, -73, -2574)
    assert -161 == -7 * 23
    assert -2574 == -2 * 3 * 3 * 11 * 13

    s = c["shared_coarse_data"]
    assert (s["A"], s["C"], s["D"]) == (73, 11, 13)
    assert (s["A_mod8"], s["B_mod8"], s["C_mod8"], s["D_mod8"]) == (1, 7, 3, 5)
    assert (s["e"], s["f"], s["h"], s["eta"]) == (1, 1, 1, -1)
    assert s["AE_128_skeleton_member"] is True

    b7 = c["B7"]
    b23 = c["B23"]
    n7 = 73 * 7 * 11 * 13
    n23 = 73 * 23 * 11 * 13
    assert (n7, n23) == (73073, 240097)
    assert b7["n"] == n7 and b23["n"] == n23
    assert n7 % 8 == n23 % 8 == 1
    assert b7["B"] % 8 == b23["B"] % 8 == 7

    e7, o7 = counts(n7)
    e23, o23 = counts(n23)
    assert (e7, o7) == (480, 416)
    assert (e23, o23) == (384, 384)
    assert [b7["Tunnell_N_even"], b7["Tunnell_N_odd"]] == [e7, o7]
    assert [b23["Tunnell_N_even"], b23["Tunnell_N_odd"]] == [e23, o23]
    assert b7["Tunnell_equality"] is False
    assert b23["Tunnell_equality"] is True

    af = json.loads(AF.read_text())
    assert af["exact_separation"]["same_parameter"] is True
    assert af["exact_separation"]["same_A_B_C_D_mod8_skeleton"] is True
    assert af["choice_B7"]["all_eight_rows_pass"] is True
    assert af["choice_B23"]["all_eight_rows_pass"] is False
    assert b7["AF_selected_prime_rows_pass"] is True
    assert b23["AF_selected_prime_rows_pass"] is False
    assert b23["local_or_receiver_survivor_claimed"] is False
    assert b23["positive_rank_claimed"] is False
    assert b23["congruent_number_claimed"] is False

    sep = c["exact_separation"]
    assert all(sep[k] is True for k in [
        "same_parameter", "same_A_C_D", "same_B_mod8", "same_e_f_h_eta",
        "same_A_B_C_D_mod8_skeleton", "same_B_reservoir", "same_n_mod8",
        "different_actual_B_prime_identity", "different_Tunnell_equality_outcome"
    ])
    out = c["conclusion"]
    assert out["mod8_skeleton_determines_Tunnell_filter"] is False
    assert out["reservoir_labels_plus_mod8_determine_Tunnell_filter"] is False
    assert out["n_mod8_determines_Tunnell_filter"] is False
    assert out["actual_prime_identity_load_bearing_for_Tunnell"] is True
    assert out["candidate_parameter_set_shrunk"] is False
    assert out["receiver_closed"] is False

    rr = c["route_result"]
    assert rr["route_status"] == "BLOCKED_NEW_PATTERN_ISOLATED"
    assert rr["next_leaf"] == "36-09AO_MONSKY_MATRIX_STAGE36_FULL2_CLASS_ADAPTER_PREFLIGHT"

    st = json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V76_36_09AN_CANDIDATE"
    an = st["authority_frontier"]["36-09AN"]
    assert an["RESIDUE_ONLY_TUNNELL_PRECOMPUTATION"] is False
    assert an["ACTUAL_PRIME_IDENTITY_LOAD_BEARING"] is True
    assert st["current"]["unit"] == "36-09AO"
    assert st["current"]["36_09AO_entry_allowed"] is True
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False

    print("36-09AN verified: same p=2/11 and same AE mod-8/reservoir skeleton give Tunnell failure for B=7 but equality for B=23; residue-only Tunnell precomputation is impossible; actual prime identity remains load-bearing; B23 is not promoted as local/congruent; AO Monsky adapter unlocked")


if __name__ == "__main__":
    main()
