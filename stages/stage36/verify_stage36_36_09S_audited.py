#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09S" / "esigmatau-torsion-growth-exclusion-preflight.json"
VERIFIER = ROOT / "stages" / "stage36" / "verify_stage36_36_09S.py"
SOURCE = ROOT / "stages" / "stage36" / "36-09S" / "torsion-growth-lmfdb-mazur-source-lock.md"
W03 = ROOT / "docs" / "arsenal" / "cards" / "formal" / "S34-W03.md"

BASE = "87a1c4e6268f76c642964dbcb5d0cd4be4e7c425"
MERGED_V51 = "bf7399e69c36cadf9d52684821332a235b3e6237"
V51_BLOB = "d403689921bff2a9679e459ce3bd7ba9db249e58"
AUDITED_HEAD = "27d5479fd10627076f5cf2c5f952f4759b1ec6da"
PASS_REVIEW = 5124402673
CERT_BLOB = "3af506b590c5e4d7499c203651c0bf4ef31ec767"
VERIFIER_BLOB = "ef3faf907fceb6d31aa1e1f4299f0dcbb62f9e46"
SOURCE_BLOB = "3549b92406ead4ff846153c5444559ddeac245a7"
W03_BLOB = "1d5275321f42768a6414d4610ac912c63be43f96"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def main() -> None:
    s = json.loads(STATE.read_text())
    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V52_THIN_36_09S_AUDITED"
    assert s["status"] == "ACTIVE"
    assert s["base_main_sha"] == BASE
    assert git("rev-parse", f"{MERGED_V51}:stages/stage36/MAIN-STATE.json") == V51_BLOB
    subprocess.check_call(["git", "merge-base", "--is-ancestor", MERGED_V51, BASE], cwd=ROOT)

    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09S/esigmatau-torsion-growth-exclusion-preflight.json") == CERT_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/verify_stage36_36_09S.py") == VERIFIER_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09S/torsion-growth-lmfdb-mazur-source-lock.md") == SOURCE_BLOB
    assert blob(CERT) == CERT_BLOB
    assert blob(VERIFIER) == VERIFIER_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(W03) == W03_BLOB

    r = s["authority_frontier"]["36-09S"]
    assert r["status"] == "AUDITED_E_SIGMA_TAU_TORSION_GROWTH_EXCLUSION_AND_POSITIVE_RANK_REDUCTION"
    assert r["pr"] == 1657
    assert r["hostile_audit_review"] == PASS_REVIEW
    assert r["audited_head"] == AUDITED_HEAD
    assert r["exact_head_ci"] == "34012855886/101431530393"
    assert r["merged_main_sha"] == MERGED_V51
    assert r["certificate_blob_sha"] == CERT_BLOB
    assert r["verifier_blob_sha"] == VERIFIER_BLOB
    assert r["external_source_lock_blob_sha"] == SOURCE_BLOB
    assert r["ORDER4_GATE_RANK"] == 0
    assert r["ORDER4_GATE_TORSION"] == "Z/2 x Z/2"
    assert r["RETAINED_ORDER4_EXISTS"] is False
    assert r["ORDER3_GATE_RANK"] == 0
    assert r["ORDER3_GATE_TORSION"] == "Z/2 x Z/4"
    assert r["RETAINED_ORDER3_EXISTS"] is False
    assert r["E_SIGMA_TAU_TORSION_GROWTH_EXCLUDED"] is True
    assert r["E_SIGMA_TAU_RETAINED_TORSION"] == "Z/2 x Z/2"
    assert r["ONLY_REMAINING_E_SIGMA_TAU_MW_GROWTH_SPECIES"] == "positive rank jump"
    assert r["RECEIVER_FORCES_E_SIGMA_TAU_POSITIVE_RANK_JUMP"] is True
    assert r["RECEIVER_FORCES_E_TAU_POSITIVE_RANK_JUMP"] is True
    assert r["INDEPENDENCE_CLAIMED"] is False
    assert r["CANDIDATE_SET_SHRUNK"] is False
    assert r["SIMULTANEOUS_POSITIVE_RANK_LOCUS_EMPTY"] is False
    assert r["S34_W03_INTERSECTION_EXECUTED"] is False
    assert r["RECEIVER_CLOSED"] is False

    assert s["freshness"]["merged_stage36_main"] == MERGED_V51
    assert s["freshness"]["promotion_base_main"] == BASE
    assert s["freshness"]["stage36_drift_after_36_09S_merge"] is False

    assert s["current"]["unit"] == "36-09T"
    assert s["current"]["next_owner"] == "STAGE36_MAIN"
    assert s["current"]["36_09T_entry_allowed"] is True
    g = s["promotion_gates"]
    assert g["E_sigma_tau_torsion_growth_exclusion_promoted"] is True
    assert g["E_sigma_tau_positive_rank_jumps_excluded"] is False
    assert g["E_tau_positive_rank_jumps_excluded"] is False
    assert g["simultaneous_positive_rank_locus_empty"] is False
    assert g["S34_W03_receiver_intersection_executed"] is False
    assert g["receiver_emptiness_proved"] is False
    assert g["R29_CAMP2_closed"] is False
    assert g["endpoint_closed"] is False

    assert s["claims"]["independence_claimed"] is False
    assert s["claims"]["candidate_set_shrunk"] is False
    assert s["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09S hostile-audited torsion-growth exclusion promoted; both quotient obligations are positive-rank jumps; 36-09T unlocked")


if __name__ == "__main__":
    main()
