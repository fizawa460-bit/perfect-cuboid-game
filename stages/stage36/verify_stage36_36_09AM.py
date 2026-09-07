#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage36/36-09AM/uniform-congruent-covering-mw-sha-classifier-preflight.json"
SOURCE = ROOT / "stages/stage36/36-09AM/tunnell-uniform-branch-filter-source-lock.md"
AL = ROOT / "stages/stage36/36-09AL/b7-selmer-class-nontrivial-sha2-preflight.json"
AF = ROOT / "stages/stage36/36-09AF/variable-prime-jacobi-matrix-realizability-preflight.json"
STATE = ROOT / "stages/stage36/MAIN-STATE.json"

BASE = "24215fa27a631cd3cb370c0dfd76866dd2e916f1"
AUDITED_MERGE = "58e81a647b63bcea17ab396409c2813b667f45e2"
AUDITED_HEAD = "56f815b9bc25ca91a2ba6e0c0291664bfeac733d"
AUDIT_REVIEW = 5127436589
AUDIT_CI = "34074355295/101597480228"
CERT_BLOB = "cc9f74ed60680883e6b21ea555b3dfbd9dc3978c"
SOURCE_BLOB = "80cc32fb32417db74740152192df4fffc8be69c6"
AL_BLOB = "10962f8d2471a8236d66a602c0f4952ce497e56c"
AL_VERIFIER_BLOB = "b4b5215bf5f06ed451f7cd99fef708de5069b087"
AF_BLOB = "be5a65e3fcfb182998ccb02ec42f8114b50b0a7d"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def tunnell_parity_counts(n: int) -> tuple[int, int]:
    assert n > 0
    # Unified statement: a=1 for odd n, a=2 for even n,
    # n/a = 2*a*x^2 + y^2 + 8*z^2.
    a = 1 if n % 2 else 2
    assert n % a == 0
    m = n // a
    even = odd = 0
    xmax = math.isqrt(m // (2 * a)) if m >= 2 * a else 0
    zmax = math.isqrt(m // 8)
    for x in range(-xmax, xmax + 1):
        remx = m - 2 * a * x * x
        if remx < 0:
            continue
        for z in range(-zmax, zmax + 1):
            rem = remx - 8 * z * z
            if rem < 0:
                continue
            y = math.isqrt(rem)
            if y * y == rem:
                mult = 1 if y == 0 else 2
                if z % 2 == 0:
                    even += mult
                else:
                    odd += mult
    return even, odd


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(AL) == AL_BLOB
    assert blob(AF) == AF_BLOB
    subprocess.check_call(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT)
    subprocess.check_call(["git", "merge-base", "--is-ancestor", AUDITED_MERGE, "HEAD"], cwd=ROOT)
    # Squash-merged audited head is provenance metadata rather than an ancestor;
    # fail-close on the audited payload as materialized in the merge/current main.
    assert git("rev-parse", f"{AUDITED_MERGE}:stages/stage36/36-09AL/b7-selmer-class-nontrivial-sha2-preflight.json") == AL_BLOB
    assert git("rev-parse", f"{AUDITED_MERGE}:stages/stage36/verify_stage36_36_09AL.py") == AL_VERIFIER_BLOB
    assert git("rev-parse", f"{BASE}:stages/stage36/36-09AL/b7-selmer-class-nontrivial-sha2-preflight.json") == AL_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AM_UNIFORM_CONGRUENT_COVERING_MW_SHA_CLASSIFIER_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    ap = c["audited_parent"]
    assert ap["pr"] == 1677
    assert ap["hostile_audit_review"] == AUDIT_REVIEW
    assert ap["audited_exact_head"] == AUDITED_HEAD
    assert ap["exact_head_ci"] == AUDIT_CI
    assert ap["merged_main_sha"] == AUDITED_MERGE
    assert c["freshness"]["current_main"] == BASE
    assert c["freshness"]["stage36_source_drift"] is False

    tf = c["unified_tunnell_filter"]
    assert tf["necessary_condition_for_congruent_n"] == "N_even=N_odd"
    assert tf["equality_conclusion_unconditional"] == "NO_RANK_OR_MW_CONCLUSION"
    assert tf["BSD_converse_used"] is False

    # Audited B=7 branch: exact parity counts recover AL's 480 / total 896.
    e7, o7 = tunnell_parity_counts(73073)
    assert (e7, o7, e7 + o7) == (480, 416, 896)
    b7 = c["audited_B7_replay"]
    assert [b7["N_even"], b7["N_odd"], b7["N_total"]] == [e7, o7, e7 + o7]
    assert b7["tunnell_equality"] is False
    al = json.loads(AL.read_text())
    assert al["Selmer_to_Sha_conclusion"]["covering_class_maps_to_nonzero_Sha2"] is True
    assert al["Selmer_to_Sha_conclusion"]["covering_has_Q_point"] is False
    assert b7["nontrivial_Sha2"] is True
    assert b7["covering_Q_point"] is False

    # Same AF coarse skeleton, different actual B-prime identity.  Tunnell
    # outcome changes even though both n are 1 mod 8.
    e23, o23 = tunnell_parity_counts(240097)
    assert (e23, o23, e23 + o23) == (384, 384, 768)
    assert 73073 % 8 == 240097 % 8 == 1
    af = json.loads(AF.read_text())
    assert af["shared_branch_skeleton"]["B_mod8"] == 7
    assert af["choice_B7"]["all_eight_rows_pass"] is True
    assert af["choice_B23"]["all_eight_rows_pass"] is False

    ub = c["uniformity_boundary"]
    assert ub["Tunnell_filter_is_branchwise_effective"] is True
    assert ub["Tunnell_filter_alone_closes_all_branches"] is False
    assert ub["Tunnell_equality_is_not_positive_rank_credit"] is True
    assert ub["fixed_fiber_MW_certification_still_needed_after_Tunnell_failure"] is True
    assert ub["actual_prime_identity_remains_load_bearing"] is True
    assert ub["candidate_parameter_set_shrunk"] is False
    assert ub["receiver_closed"] is False

    out = c["route_result"]
    assert out["route_status"] == "PASS_NEW_GATE_FROM_STRONGER_VIEW"
    assert out["next_leaf"] == "36-09AN_TUNNELL_FILTER_RESIDUE_NONCOMPRESSION_PREFLIGHT"

    st = json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V75_36_09AM_CANDIDATE"
    assert st["base_main_sha"] == BASE
    assert st["promotion_gates"]["36_09AL_hostile_audit_passed"] is True
    am = st["authority_frontier"]["36-09AM"]
    assert am["UNCONDITIONAL_TUNNELL_BRANCH_FILTER"] is True
    assert am["BSD_CONVERSE_USED"] is False
    assert am["UNIFORM_BRANCH_FAMILY_CLASSIFIED"] is False
    assert st["current"]["unit"] == "36-09AN"
    assert st["current"]["36_09AN_entry_allowed"] is True
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09AM verified: audited AJ-AL promoted; unified Tunnell necessary filter is exact and BSD-free; B7 fails (480 vs 416) while same coarse AF skeleton B23 has equality (384=384); equality gives no positive-rank credit; uniform receiver remains open; AN unlocked")


if __name__ == "__main__":
    main()
