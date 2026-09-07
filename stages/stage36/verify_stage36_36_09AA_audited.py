#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
AA_CERT = ROOT / "stages" / "stage36" / "36-09AA" / "receiver-coupled-same-x-twist-intersection-preflight.json"
AA_VERIFIER = ROOT / "stages" / "stage36" / "verify_stage36_36_09AA.py"

BASE = "a6e8c96a4d115e47a9fbcebbb0fe505c58cc07a2"
AUDITED_HEAD = "25229e7b0dfbbc5524266ce49e8edaf217841701"
PASS_REVIEW = 5125551980
MERGED_STATE_BLOB = "f54b99361d8994287167b332d9d73996565cf1d9"
AA_CERT_BLOB = "be447726a97158849c67ed6d57d6d3c35d6ba20f"
AA_VERIFIER_BLOB = "9fb36b8c72e36bdc6a3c9b29fabcc31f30e7b7b3"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def main() -> None:
    s = json.loads(STATE.read_text())
    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V62_36_09AA_AUDITED"
    assert s["status"] == "ACTIVE"
    assert s["base_main_sha"] == BASE
    subprocess.check_call(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT)
    assert git("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == MERGED_STATE_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09AA/receiver-coupled-same-x-twist-intersection-preflight.json") == AA_CERT_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/verify_stage36_36_09AA.py") == AA_VERIFIER_BLOB
    assert blob(AA_CERT) == AA_CERT_BLOB
    assert blob(AA_VERIFIER) == AA_VERIFIER_BLOB

    p = s["audited_batch_promotion"]
    assert p["candidate_pr"] == 1664
    assert p["audited_head"] == AUDITED_HEAD
    assert p["hostile_audit_review"] == PASS_REVIEW
    assert p["exact_head_ci"] == "34037594565/101498394669"
    assert p["merged_main_sha"] == BASE
    assert p["merged_state_blob_sha"] == MERGED_STATE_BLOB

    for unit in ("36-09U", "36-09V", "36-09W", "36-09X", "36-09Y", "36-09Z", "36-09AA"):
        assert s["authority_frontier"][unit]["status"].startswith("AUDITED_")

    aa = s["authority_frontier"]["36-09AA"]
    assert aa["SAME_X_RECEIVER_EQUIVALENCE"] is True
    assert aa["RECEIVER_REQUIRES_E_PLUS_AND_E_MINUS_SAME_X"] is True
    assert aa["EXPLICIT_Z_POINTS_RECEIVER_INCOMPATIBLE"] is True
    assert aa["S34_W03_EXACT_JOINT_ADAPTER_READY"] is True
    assert aa["S34_W03_INTERSECTION_EXCLUSION_EXECUTED"] is False
    assert aa["RECEIVER_RANKJUMP_INTERSECTION_EMPTY"] is False
    assert aa["RECEIVER_CLOSED"] is False

    g = s["promotion_gates"]
    assert g["36_09AA_hostile_audit_passed"] is True
    assert g["36_09AA_promoted"] is True
    assert g["Qi_rankjump_locus_nonempty_audited"] is True
    assert g["same_x_receiver_equivalence_audited"] is True
    assert g["receiver_emptiness_proved"] is False
    assert g["R29_CAMP2_closed"] is False
    assert g["Q11_CAMPEDELLI_closed"] is False
    assert g["endpoint_closed"] is False

    assert s["current"]["unit"] == "36-09AB"
    assert s["current"]["36_09AB_entry_allowed"] is True
    assert s["claims"]["candidate_parameter_set_shrunk"] is False
    assert s["claims"]["perfect_cuboid_nonexistence_claim"] is False
    print("hostile-audited 36-09U through 36-09AA authority promoted; 36-09AB unlocked; receiver and endpoint firewalls remain closed")


if __name__ == "__main__":
    main()
