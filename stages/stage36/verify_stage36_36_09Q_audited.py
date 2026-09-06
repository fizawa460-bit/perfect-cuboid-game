#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09Q" / "etau-torsion-growth-stage14-second-basechange-preflight.json"
VERIFIER = ROOT / "stages" / "stage36" / "verify_stage36_36_09Q.py"
SOURCE = ROOT / "stages" / "stage36" / "36-09Q" / "stage14-pythagorean-basechange-source-lock.md"
STAGE14 = ROOT / "stages" / "stage14" / "archive" / "stage14-4af-specialization-triple.md"
W03 = ROOT / "docs" / "arsenal" / "cards" / "formal" / "S34-W03.md"
POLICY = ROOT / "docs" / "research-os" / "policies" / "research-credit-and-promotion-firewalls.md"

BASE = "aabe5d9d01f74ed2d68d27edaee7635af7c89ecf"
V46_BLOB = "dcdba98f4a7f103c2f409e1d5b3ee2885bbdf290"
AUDIT_BASE = "43f3f3b135a2f5664cb8cc736d6db0b37d7b79da"
MERGE_PARENT = "43f3f3b135a2f5664cb8cc736d6db0b37d7b79da"
AUDITED_HEAD = "fa93c23842a272251a88066d9d31d321f28db288"
PASS_REVIEW = 5123710654
CERT_BLOB = "36b24b1a42231ccfec9364df6a8d52af13ceb6de"
VERIFIER_BLOB = "d56f1b83663165952dfdb4dc240f916fb6e33558"
SOURCE_BLOB = "cb231b7d1351a9787c3da2e187c4bd0e67adf7c9"
STAGE14_BLOB = "f14d6840d10aaa36df63b2d4a70a07d509b596ce"
W03_BLOB = "1d5275321f42768a6414d4610ac912c63be43f96"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def main() -> None:
    s = json.loads(STATE.read_text())
    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V47_THIN_36_09Q_AUDITED"
    assert s["status"] == "ACTIVE"
    assert s["base_main_sha"] == BASE
    assert git("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == V46_BLOB
    assert git("rev-parse", f"{BASE}^") == MERGE_PARENT
    assert AUDIT_BASE == MERGE_PARENT
    assert git("diff", "--name-only", f"{AUDIT_BASE}..{MERGE_PARENT}") == ""

    # Audited 36-09Q payload and imported authority remain byte-identical.
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09Q/etau-torsion-growth-stage14-second-basechange-preflight.json") == CERT_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/verify_stage36_36_09Q.py") == VERIFIER_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09Q/stage14-pythagorean-basechange-source-lock.md") == SOURCE_BLOB
    assert blob(CERT) == CERT_BLOB
    assert blob(VERIFIER) == VERIFIER_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(STAGE14) == STAGE14_BLOB
    assert blob(W03) == W03_BLOB
    assert POLICY.exists()

    q = s["authority_frontier"]["36-09Q"]
    assert q["status"] == "AUDITED_EXACT_TORSION_GROWTH_EXCLUDED_AND_RANKJUMP_SECOND_BASECHANGE_REDUCTION"
    assert q["pr"] == 1652
    assert q["hostile_audit_review"] == PASS_REVIEW
    assert q["audited_head"] == AUDITED_HEAD
    assert q["exact_head_ci"] == "34003813914/101407291515"
    assert q["merged_main_sha"] == BASE
    assert q["certificate_blob_sha"] == CERT_BLOB
    assert q["verifier_blob_sha"] == VERIFIER_BLOB
    assert q["source_lock_blob_sha"] == SOURCE_BLOB
    assert q["STAGE14_SOURCE_BLOB"] == STAGE14_BLOB
    assert q["E_TAU_STAGE14_SIGNED_FAMILY_ISOMORPHISM"] is True
    assert q["STAGE14_U14"] == "(p^2-2p-1)/(p^2+2p-1)"
    assert q["SECOND_BASECHANGE_CONDITION"] == "2*(1+u14^2) is a rational square"
    assert q["E_TAU_TORSION_GROWTH_EXCLUDED"] is True
    assert q["ONLY_REMAINING_MW_GROWTH_SPECIES"] == "positive rank jump"
    assert q["POSITIVE_RANK_JUMPS_EXCLUDED"] is False
    assert q["S34_W03_INTERSECTION_EXECUTED"] is False
    assert q["RECEIVER_CLOSED"] is False

    assert s["freshness"]["audit_pr_base"] == AUDIT_BASE
    assert s["freshness"]["audit_merge_parent"] == MERGE_PARENT
    assert s["freshness"]["merged_stage36_main"] == BASE
    assert s["cycle_ledger"]["B3_TORSION_GROWTH_SUBROUTE"].startswith("CLOSED_AUDITED")
    assert s["cycle_ledger"]["B3_POSITIVE_RANK_JUMP_SUBROUTE"].startswith("LIVE")
    assert s["cycle_ledger"]["counts"] == {"live":1,"untested":3,"blocked":6,"dominated":2}

    assert s["current"]["unit"] == "36-09R"
    assert s["current"]["36_09R_entry_allowed"] is True
    g = s["promotion_gates"]
    assert g["E_tau_torsion_growth_exclusion_promoted"] is True
    assert g["E_tau_stage14_second_basechange_adapter_promoted"] is True
    assert g["specialization_rank_jumps_excluded"] is False
    assert g["S34_W03_receiver_intersection_executed"] is False
    assert g["receiver_emptiness_proved"] is False
    assert g["R29_CAMP2_closed"] is False
    assert g["Q11_CAMPEDELLI_closed"] is False
    assert g["endpoint_closed"] is False
    assert g["perfect_cuboid_nonexistence_claim"] is False

    print("36-09Q hostile-audited authority promoted; torsion growth closed; 36-09R rank-jump/receiver intersection unlocked")


if __name__ == "__main__":
    main()
