#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09T" / "simultaneous-two-quotient-qi-rankjump-preflight.json"
NOTE = ROOT / "stages" / "stage36" / "36-09T" / "qi-twist-rankjump-proof-note.md"
M = ROOT / "stages" / "stage36" / "36-09M" / "universal-order4-2isogeny-physical-family-preflight.json"
N = ROOT / "stages" / "stage36" / "36-09N" / "relative-2isogeny-kummer-image-rank1-preflight.json"
O = ROOT / "stages" / "stage36" / "36-09O" / "physical-square-lift-v4-quotient-preflight.json"
S = ROOT / "stages" / "stage36" / "36-09S" / "esigmatau-torsion-growth-exclusion-preflight.json"
MAZUR = ROOT / "stages" / "stage36" / "36-09S" / "torsion-growth-lmfdb-mazur-source-lock.md"
W03 = ROOT / "docs" / "arsenal" / "cards" / "formal" / "S34-W03.md"
W02 = ROOT / "docs" / "arsenal" / "cards" / "formal" / "S34-W02.md"
CYCLE = ROOT / "docs" / "research-os" / "policies" / "cycle-exploration-safety-protocol.md"

BASE = "7a608ee2511192af8e293d88f8a7117aa5ad19d9"
V52_BLOB = "dfe27e24af76c0cfbd494c686287fd1faa9fd1c8"
CERT_BLOB = "1191de3e0176aac4ad10bd7b346830279ce12805"
NOTE_BLOB = "9d8d7e397aa71a38fa9daf6ebce0d8aa599e2691"
M_BLOB = "470e87d3e48c857b99793bd8ac0d01eff75eb727"
N_BLOB = "02a14439d94d7f6e5ac2f65e995e8acfb6845788"
O_BLOB = "6a2678ebedba40e13277100441361039ee47ca28"
S_BLOB = "3af506b590c5e4d7499c203651c0bf4ef31ec767"
MAZUR_BLOB = "3549b92406ead4ff846153c5444559ddeac245a7"
W03_BLOB = "1d5275321f42768a6414d4610ac912c63be43f96"
W02_BLOB = "13d41be776fcd2edcd258f11bd28c5a6596de45b"
CYCLE_BLOB = "4e911c4fc7e4ea7a2b5f96733a90b986ef8d9a37"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def trim(a: tuple[int, ...]) -> tuple[int, ...]:
    a = tuple(a)
    while len(a) > 1 and a[-1] == 0:
        a = a[:-1]
    return a


def add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    n = max(len(a), len(b))
    return trim(tuple((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)))


def scale(a: tuple[int, ...], c: int) -> tuple[int, ...]:
    return trim(tuple(c*x for x in a))


def sub(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return add(a, scale(b, -1))


def mul(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(tuple(out))


def main() -> None:
    c = json.loads(CERT.read_text())
    s = json.loads(STATE.read_text())
    m = json.loads(M.read_text())
    n = json.loads(N.read_text())
    o = json.loads(O.read_text())
    old_s = json.loads(S.read_text())

    assert c["schema"] == "STAGE36_36_09T_SIMULTANEOUS_TWO_QUOTIENT_QI_RANKJUMP_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    assert git("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == V52_BLOB
    assert blob(CERT) == CERT_BLOB
    assert blob(NOTE) == NOTE_BLOB
    assert blob(M) == M_BLOB
    assert blob(N) == N_BLOB
    assert blob(O) == O_BLOB
    assert blob(S) == S_BLOB
    assert blob(MAZUR) == MAZUR_BLOB
    assert blob(W03) == W03_BLOB
    assert blob(W02) == W02_BLOB
    assert blob(CYCLE) == CYCLE_BLOB

    nm = (-1, -2, 1)
    np = (-1, 2, 1)
    d = (0, -1, 0, 1)
    h = (1, 0, 2, 0, 1)
    cc = (1, 0, -6, 0, 1)
    assert sub(mul(np, np), mul(nm, nm)) == scale(d, 8)
    assert add(mul(np, np), mul(nm, nm)) == scale(h, 2)
    assert mul(nm, np) == cc
    assert scale(h, 4) == scale(add(mul(np, np), mul(nm, nm)), 2)

    assert m["two_primary_torsion_Ek"]["conclusion"] == "E_k(Q)[2^infinity] is exactly Z/4 x Z/2 on every retained physical fiber"
    assert set(m["two_primary_torsion_Ek"]["rational_2_torsion"]) == {"(0,0)", "(-1,0)", "(-k^2,0)"}
    assert m["two_primary_torsion_Ek"]["order4_above_T0"] == ["x=k", "x=-k"]
    assert n["function_field_index_argument"]["generic_rank"] == 1
    assert n["explicit_relative_sections_and_lower_kummer_classes"]["dual_E_section"] == [
        "x=Nplus^2", "y=-2*(q^2+1)*Nplus^2"
    ]
    assert old_s["family"]["audited_generic_MW"] == "Z/2 x Z/2"
    assert old_s["conclusion"]["receiver_forces_E_sigma_tau_positive_rank_jump"] is True

    mid = c["middle_E_sigma"]
    assert mid["retained_two_primary_torsion"] == "Z/4 x Z/2"
    assert mid["retained_full_torsion_from_Mazur"] == "Z/4 x Z/2"
    assert mid["section"] == "P_sigma=(k^2,-rho*k^2)"
    assert mid["section_fiberwise_nontorsion"] is True
    assert mid["retained_rank_lower_bound_over_Q"] == 1
    assert mid["generic_rank_over_Qp"] == 1

    tw = c["minus_one_twist"]
    assert tw["twist_relation"] == "E_sigma_tau is the quadratic twist of E_sigma by -1"
    assert tw["Qi_isomorphism"] == "phi(x,y)=(-x,i*y)"
    assert tw["generic_rank_E_sigma_tau_over_Qp"] == 0
    assert tw["generic_rank_E_sigma_over_Qi_p"] == 1

    rr = c["receiver_rankjump_consequence"]
    assert rr["receiver_forces_E_sigma_tau_nontorsion_point"] is True
    assert rr["receiver_twist_point_is_anti_invariant_over_Qi"] is True
    assert rr["P_sigma_is_invariant_over_Qi"] is True
    assert rr["invariant_and_anti_invariant_nontorsion_points_independent_mod_torsion"] is True
    assert rr["receiver_forces_E_sigma_rank_over_Qi_at_least"] == 2
    assert rr["generic_E_sigma_rank_over_Qi_p"] == 1
    assert rr["receiver_forces_genuine_Qi_rank_jump"] is True

    pair = c["compatible_pair_audit"]
    assert pair["compatibility"] == "R^2-S^2=4"
    assert pair["inverse"] == ["t=(R+S)/2", "1/t=(R-S)/2", "y=t^2*v"]
    assert pair["compatible_pair_fiber_product_equals_top_receiver_open"] is True
    assert pair["two_positive_rank_conditions_claimed_independent"] is False
    assert pair["candidate_set_shrunk_by_rank_intersection"] is False
    assert pair["S34_W03_rank_only_close_valid"] is False
    assert pair["S34_W03_intersection_executed"] is False

    ca = c["cycle_audit"]
    assert ca["CYCLE_ROUTE_STATUS"] == "PASS_NEW_GATE_FROM_STRONGER_VIEW"
    assert ca["CYCLE_EXHAUSTIVE_VIEW_AUDIT"] is True
    assert ca["CYCLE_BLIND_REDISCOVERY"] is True
    assert ca["CYCLE_SPLIT_TRIGGERED"] is False
    assert ca["candidate_ledger"]["Qi_twist_eigenspace_rankjump"] == "LIVE"
    assert ca["candidate_ledger"]["compatible_two_quotient_point_fiber_product"] == "EQUIVALENT"
    assert ca["candidate_ledger"]["rank_only_S34_W03_intersection"] == "BLOCKED"

    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V53_36_09T_PENDING_HOSTILE_AUDIT"
    assert s["status"] == "ACTIVE_PENDING_HOSTILE_AUDIT"
    assert s["base_main_sha"] == BASE
    t = s["authority_frontier"]["36-09T"]
    assert t["certificate_blob_sha"] == CERT_BLOB
    assert t["proof_note_blob_sha"] == NOTE_BLOB
    assert t["E_SIGMA_FIBERWISE_NONTORSION_SECTION"] is True
    assert t["RECEIVER_FORCES_E_SIGMA_QI_RANK_AT_LEAST"] == 2
    assert t["GENERIC_E_SIGMA_QI_RANK"] == 1
    assert t["RECEIVER_FORCES_QI_RANK_JUMP"] is True
    assert t["TWO_QUOTIENT_RANK_OBLIGATIONS_INDEPENDENT"] is False
    assert t["CANDIDATE_SET_SHRUNK"] is False
    assert t["S34_W03_INTERSECTION_EXECUTED"] is False
    assert t["RECEIVER_CLOSED"] is False
    assert s["current"]["36_09U_entry_allowed"] is False
    assert s["promotion_gates"]["Qi_rankjump_gate_promoted"] is False
    assert s["promotion_gates"]["receiver_emptiness_proved"] is False
    assert s["promotion_gates"]["R29_CAMP2_closed"] is False
    assert s["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09T exact Q(i) twist-eigenspace rankjump gate verified; compatible rank-only intersection gives no shrink; pending hostile audit")


if __name__ == "__main__":
    main()
