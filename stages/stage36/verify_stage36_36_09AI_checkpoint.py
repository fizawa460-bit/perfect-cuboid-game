#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/"stages/stage36/MAIN-STATE.json"
AG=ROOT/"stages/stage36/36-09AG/individual-conic-hasse-solubility-preflight.json"
AH=ROOT/"stages/stage36/36-09AH/common-uv-two-quadric-genusone-preflight.json"
AI=ROOT/"stages/stage36/36-09AI/j1728-congruent-number-jacobian-preflight.json"
AIV=ROOT/"stages/stage36/verify_stage36_36_09AI.py"

BASE="9306238c7ada55e31311245019d6b7e474ad837f"
AI_HEAD="8c84ca4ea7676029d6580ae433b506eaa9cc067b"
AI_CI="34069843149/101585034485"
STATE_BLOB="62efff71453c1961ea4a13273b9d7abf07af20b8"
AG_BLOB="b40a525e739d6021c07d364a243c0d7653350abe"
AH_BLOB="732431bef8dfafe25cbdeb005c4237d72a40ae4b"
AI_BLOB="c5af6c4dde67532ea8d592e74aed187c72bbed4e"
AIV_BLOB="2300ca45ac37314829ee83cfb054e45e021c0bbe"


def git(*args:str)->str:
    return subprocess.check_output(["git",*args],cwd=ROOT,text=True).strip()

def blob(path:Path)->str:
    return git("hash-object",str(path.relative_to(ROOT)))

def main()->None:
    assert blob(STATE)==STATE_BLOB
    assert blob(AG)==AG_BLOB
    assert blob(AH)==AH_BLOB
    assert blob(AI)==AI_BLOB
    assert blob(AIV)==AIV_BLOB
    subprocess.check_call(["git","merge-base","--is-ancestor",BASE,"HEAD"],cwd=ROOT)
    subprocess.check_call(["git","merge-base","--is-ancestor",AI_HEAD,"HEAD"],cwd=ROOT)
    assert git("rev-parse",f"{AI_HEAD}:stages/stage36/36-09AI/j1728-congruent-number-jacobian-preflight.json")==AI_BLOB
    assert git("rev-parse",f"{AI_HEAD}:stages/stage36/verify_stage36_36_09AI.py")==AIV_BLOB

    s=json.loads(STATE.read_text())
    assert s["schema"]=="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V71_36_09AI_BATCH_AUDIT_CHECKPOINT"
    assert s["status"]=="ACTIVE_BATCH_HOSTILE_AUDIT_CHECKPOINT"
    assert s["base_main_sha"]==BASE
    ai=s["authority_frontier"]["36-09AI"]
    assert ai["exact_head"]==AI_HEAD
    assert ai["exact_head_ci"]==AI_CI
    assert ai["certificate_blob_sha"]==AI_BLOB
    assert ai["verifier_blob_sha"]==AIV_BLOB
    assert ai["Q_JACOBIAN_FAMILY"]=="CONGRUENT_NUMBER_J1728"
    assert ai["NORMALIZED_MODEL"]=="E_n: Y^2=X^3-n^2*X"
    assert ai["n_positive_squarefree"] is True
    assert ai["TWO_COVERING_STRUCTURE_IDENTIFIED"] is True
    assert ai["COVERING_CLASS_TRIVIALIZED"] is False
    assert ai["MORDELL_WEIL_RANK_CLASSIFIED"] is False
    assert ai["CANDIDATE_PARAMETER_SET_SHRUNK"] is False
    assert ai["RECEIVER_CLOSED"] is False
    assert s["current"]["unit"]=="36-09AI-AUDIT-CHECKPOINT"
    assert s["current"]["next_owner"]=="HOSTILE_AUDIT"
    assert s["current"]["hostile_audit_checkpoint_reached"] is True
    assert s["current"]["36_09AJ_entry_allowed"] is False
    assert s["promotion_gates"]["36_09AI_hostile_audit_passed"] is False
    assert s["claims"]["covering_class_trivialized"] is False
    assert s["claims"]["receiver_emptiness_proved"] is False
    assert s["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("Stage36 AG-AI checkpoint verified: individual conic Hasse solubility -> smooth common-u:v genus-one -> exact squarefree congruent-number Jacobian 2-covering; AJ locked pending hostile audit; receiver/endpoints remain closed")

if __name__=="__main__":
    main()
