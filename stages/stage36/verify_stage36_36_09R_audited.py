#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09R" / "etau-rankjump-receiver-esigmatau-growth-preflight.json"
VERIFIER = ROOT / "stages" / "stage36" / "verify_stage36_36_09R.py"
SOURCE = ROOT / "stages" / "stage36" / "36-09N" / "relative-2isogeny-specialization-source-lock.md"
W03 = ROOT / "docs" / "arsenal" / "cards" / "formal" / "S34-W03.md"

BASE = "7aa230172497311267daa0451189377fbf8eba30"
V49_BLOB = "268ba43f3264e729ac627465c3d998b58027f960"
AUDITED_HEAD = "f48184e2ab7fabe6fd07b553aa1cda507874569d"
PASS_REVIEW = 5124114645
CERT_BLOB = "b55d042ede01032ff8c8b0d872510a53cb857969"
VERIFIER_BLOB = "62707dc5126e9ea6caad5fd41834cab488b29945"
SOURCE_BLOB = "a562d7053a6f04deff4473067777b7cfd538ea8a"
W03_BLOB = "1d5275321f42768a6414d4610ac912c63be43f96"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def main() -> None:
    s=json.loads(STATE.read_text())
    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V50_THIN_36_09R_AUDITED"
    assert s["status"] == "ACTIVE"
    assert s["base_main_sha"] == BASE
    assert git("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == V49_BLOB
    assert git("rev-parse", f"{BASE}^") == "69ac6635fb7a7808bca7aad72c5b7e61bcb5cbb6"

    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09R/etau-rankjump-receiver-esigmatau-growth-preflight.json") == CERT_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/verify_stage36_36_09R.py") == VERIFIER_BLOB
    assert blob(CERT) == CERT_BLOB
    assert blob(VERIFIER) == VERIFIER_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(W03) == W03_BLOB

    r=s["authority_frontier"]["36-09R"]
    assert r["status"] == "AUDITED_REPAIRED_COMPLETE_SPECIALIZATION_AND_E_SIGMA_TAU_GENERIC_MW"
    assert r["pr"] == 1655
    assert r["hostile_reaudit_review"] == PASS_REVIEW
    assert r["audited_head"] == AUDITED_HEAD
    assert r["exact_head_ci"] == "34011159813/101427124415"
    assert r["merged_main_sha"] == BASE
    assert r["certificate_blob_sha"] == CERT_BLOB
    assert r["verifier_blob_sha"] == VERIFIER_BLOB
    assert r["SPECIALIZATION_P0"] == "2/3"
    assert r["COMPLETE_GUSIC_TADIC_DIVISOR_CRITERION"] is True
    assert r["E_SIGMA_TAU_GENERIC_RANK"] == 0
    assert r["E_SIGMA_TAU_GENERIC_TORSION"] == "Z/2 x Z/2"
    assert r["RECEIVER_FORCES_E_SIGMA_TAU_MW_GROWTH"] is True
    assert r["INDEPENDENCE_CLAIMED"] is False
    assert r["CANDIDATE_SET_SHRUNK_BY_DERIVED_GROWTH"] is False
    assert r["E_SIGMA_TAU_RANK_JUMPS_EXCLUDED"] is False
    assert r["E_SIGMA_TAU_TORSION_GROWTH_EXCLUDED"] is False
    assert r["RECEIVER_CLOSED"] is False

    assert s["current"]["unit"] == "36-09S"
    assert s["current"]["36_09S_entry_allowed"] is True
    g=s["promotion_gates"]
    assert g["E_sigma_tau_complete_specialization_criterion_promoted"] is True
    assert g["E_sigma_tau_generic_MW_promoted"] is True
    assert g["E_sigma_tau_exceptional_growth_reduction_promoted"] is True
    assert g["E_sigma_tau_rank_jumps_excluded"] is False
    assert g["E_sigma_tau_torsion_growth_excluded"] is False
    assert g["simultaneous_growth_locus_empty"] is False
    assert g["receiver_emptiness_proved"] is False
    assert g["R29_CAMP2_closed"] is False
    assert g["endpoint_closed"] is False

    print("36-09R hostile-reaudited repaired authority promoted; generic E_sigma_tau MW=Z/2xZ/2; 36-09S unlocked")


if __name__ == "__main__":
    main()
