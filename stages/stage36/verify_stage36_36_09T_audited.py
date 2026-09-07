#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09T" / "simultaneous-two-quotient-qi-rankjump-preflight.json"
VERIFIER = ROOT / "stages" / "stage36" / "verify_stage36_36_09T.py"
NOTE = ROOT / "stages" / "stage36" / "36-09T" / "qi-twist-rankjump-proof-note.md"

BASE = "f6b1d047dfd238de80ed8f5c267609d01ea1a3bb"
MERGED_V53 = "266f1b24bea60744bc688afc40482090f7026ce0"
V53_BLOB = "704692dbe0900da949cde35636716f0f74ab1897"
AUDITED_HEAD = "1515be28ce81aca49adb18cd3532f0597a55e69f"
PASS_REVIEW = 5124828133
CERT_BLOB = "1191de3e0176aac4ad10bd7b346830279ce12805"
VERIFIER_BLOB = "c71d643031a01e6b67f91235d724deca82e79eb1"
NOTE_BLOB = "9d8d7e397aa71a38fa9daf6ebce0d8aa599e2691"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def main() -> None:
    s = json.loads(STATE.read_text())
    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V54_THIN_36_09T_AUDITED"
    assert s["status"] == "ACTIVE"
    assert s["base_main_sha"] == BASE
    assert git("rev-parse", f"{MERGED_V53}:stages/stage36/MAIN-STATE.json") == V53_BLOB
    subprocess.check_call(["git", "merge-base", "--is-ancestor", MERGED_V53, BASE], cwd=ROOT)

    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09T/simultaneous-two-quotient-qi-rankjump-preflight.json") == CERT_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/verify_stage36_36_09T.py") == VERIFIER_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09T/qi-twist-rankjump-proof-note.md") == NOTE_BLOB
    assert blob(CERT) == CERT_BLOB
    assert blob(VERIFIER) == VERIFIER_BLOB
    assert blob(NOTE) == NOTE_BLOB

    t = s["authority_frontier"]["36-09T"]
    assert t["status"] == "AUDITED_QI_TWIST_EIGENSPACE_RANKJUMP_REDUCTION"
    assert t["pr"] == 1660
    assert t["hostile_audit_review"] == PASS_REVIEW
    assert t["audited_head"] == AUDITED_HEAD
    assert t["exact_head_ci"] == "34023508761/101460296380"
    assert t["merged_main_sha"] == MERGED_V53
    assert t["certificate_blob_sha"] == CERT_BLOB
    assert t["verifier_blob_sha"] == VERIFIER_BLOB
    assert t["proof_note_blob_sha"] == NOTE_BLOB
    assert t["E_SIGMA_RETAINED_TORSION"] == "Z/4 x Z/2"
    assert t["E_SIGMA_FIBERWISE_NONTORSION_SECTION"] is True
    assert t["E_SIGMA_FIBERWISE_RANK_AT_LEAST"] == 1
    assert t["GENERIC_E_SIGMA_QI_RANK"] == 1
    assert t["RECEIVER_FORCES_E_SIGMA_QI_RANK_AT_LEAST"] == 2
    assert t["RECEIVER_FORCES_QI_RANK_JUMP"] is True
    assert t["QI_INVARIANT_ANTIINVARIANT_POINT_INDEPENDENCE"] is True
    assert t["TWO_QUOTIENT_RANK_OBLIGATIONS_INDEPENDENT"] is False
    assert t["CANDIDATE_SET_SHRUNK"] is False
    assert t["QI_RANKJUMP_LOCUS_EMPTY"] is False
    assert t["RECEIVER_CLOSED"] is False

    assert s["freshness"]["merged_stage36_main"] == MERGED_V53
    assert s["freshness"]["promotion_base_main"] == BASE
    assert s["freshness"]["stage36_drift_after_36_09T_merge"] is False

    assert s["current"]["unit"] == "36-09U"
    assert s["current"]["next_exact_leaf"] == "36-09U_QI_ANTIINVARIANT_RANKJUMP_DESCENT_PREFLIGHT"
    assert s["current"]["next_owner"] == "STAGE36_MAIN"
    assert s["current"]["36_09U_entry_allowed"] is True

    g = s["promotion_gates"]
    assert g["E_sigma_fiberwise_nontorsion_section_promoted"] is True
    assert g["Qi_rankjump_gate_promoted"] is True
    assert g["Qi_rankjump_locus_empty"] is False
    assert g["simultaneous_positive_rank_locus_empty"] is False
    assert g["S34_W03_receiver_intersection_executed"] is False
    assert g["receiver_emptiness_proved"] is False
    assert g["R29_CAMP2_closed"] is False
    assert g["Q11_CAMPEDELLI_closed"] is False
    assert g["endpoint_closed"] is False

    assert s["claims"]["receiver_forces_Qi_rankjump_promoted"] is True
    assert s["claims"]["candidate_set_shrunk"] is False
    assert s["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09T hostile-audited Q(i) rankjump gate promoted; 36-09U unlocked; no receiver or endpoint closure credit")


if __name__ == "__main__":
    main()
