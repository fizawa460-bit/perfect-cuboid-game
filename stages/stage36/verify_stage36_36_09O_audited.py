#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09O" / "physical-square-lift-v4-quotient-preflight.json"
VERIFIER = ROOT / "stages" / "stage36" / "verify_stage36_36_09O.py"
SOURCE = ROOT / "stages" / "stage36" / "36-09O" / "kani-rosen-v4-jacobian-source-lock.md"
W03 = ROOT / "docs" / "arsenal" / "cards" / "formal" / "S34-W03.md"

BASE = "b97673ec1c058e4e39bad24b68c036e721a97462"
V42_BLOB = "6973beebc15fc945e4f9f2eb6489dccf964781c0"
AUDITED_HEAD = "be979251c6e3d7a2431fb56537520afd2596c7d9"
PASS_REVIEW = 5123512777
CERT_BLOB = "6a2678ebedba40e13277100441361039ee47ca28"
VERIFIER_BLOB = "ed0ae786505e3443226eaed6e61b7c78ee389191"
SOURCE_BLOB = "5b5957843933b487bb9cae3acd22bb7737f37392"
W03_BLOB = "1d5275321f42768a6414d4610ac912c63be43f96"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def main() -> None:
    s = json.loads(STATE.read_text())
    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V43_THIN_36_09O_AUDITED"
    assert s["status"] == "ACTIVE"
    assert s["base_main_sha"] == BASE
    assert git("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == V42_BLOB

    # Audited 36-09O mathematical payload remains byte-identical.
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09O/physical-square-lift-v4-quotient-preflight.json") == CERT_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/verify_stage36_36_09O.py") == VERIFIER_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09O/kani-rosen-v4-jacobian-source-lock.md") == SOURCE_BLOB
    assert blob(CERT) == CERT_BLOB
    assert blob(VERIFIER) == VERIFIER_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(W03) == W03_BLOB

    o = s["authority_frontier"]["36-09O"]
    assert o["status"] == "AUDITED_EXACT_PHYSICAL_SQUARE_LIFT_AND_V4_JACOBIAN_DECOMPOSITION"
    assert o["pr"] == 1642
    assert o["hostile_audit_review"] == PASS_REVIEW
    assert o["audited_head"] == AUDITED_HEAD
    assert o["exact_head_ci"] == "34000052247/101397173180"
    assert o["merged_main_sha"] == BASE
    assert o["certificate_blob_sha"] == CERT_BLOB
    assert o["verifier_blob_sha"] == VERIFIER_BLOB
    assert o["source_lock_blob_sha"] == SOURCE_BLOB
    assert o["PHYSICAL_SQUARE_LIFT_FORMULA"] == "(V+rho*U)/(V-rho*U) is a nonzero rational square"
    assert o["GENERIC_RANK1_SECTION_IS_BOUNDARY"] is True
    assert o["FIRST_2P_LIFT_LOCUS_GENUS"] == 7
    assert o["TOP_GENUS3_V4_ACTION"] is True
    assert o["TOP_GENUS3_JACOBIAN_PRODUCT_ISOGENY"] is True
    assert o["RANK_JUMP_ONLY_ROUTE"] == "DOMINATED_INCOMPLETE"
    assert o["S34_W03_ADAPTER"] == "READY_NOT_EXECUTED"
    assert o["NEW_TWO_QUOTIENT_GENERIC_RANKS_COMPUTED"] is False
    assert o["RECEIVER_CLOSED"] is False

    assert s["cycle_ledger"]["counts"] == {"live":1,"untested":3,"blocked":6,"dominated":2}
    assert s["cycle_ledger"]["B7_STANDARD_CAMPEDELLI_MODEL_ARITHMETIC_TRANSFER"].startswith("UNTESTED")
    assert s["cycle_ledger"]["C2_GAUSSIAN_NORM_COMPRESSION"].startswith("UNTESTED_DISTINCT")
    assert s["cycle_ledger"]["B11_DIRECT_MULTIPLACE_ADELIC_RECIPROCITY"].startswith("UNTESTED")

    assert s["current"]["unit"] == "36-09P"
    assert s["current"]["36_09P_entry_allowed"] is True
    g=s["promotion_gates"]
    assert g["physical_square_lift_adapter_promoted"] is True
    assert g["top_genus3_v4_action_promoted"] is True
    assert g["top_genus3_jacobian_product_isogeny_promoted"] is True
    assert g["S34_W03_receiver_intersection_executed"] is False
    assert g["new_two_quotient_generic_ranks_computed"] is False
    assert g["specialization_rank_jumps_excluded"] is False
    assert g["top_genus3_rational_points_exhausted"] is False
    assert g["receiver_emptiness_proved"] is False
    assert g["R29_CAMP2_closed"] is False
    assert g["Q11_CAMPEDELLI_closed"] is False
    assert g["endpoint_closed"] is False
    assert g["perfect_cuboid_nonexistence_claim"] is False

    print("36-09O hostile-audited authority promoted; V4 Jacobian/physical-lift adapter frozen; 36-09P unlocked")


if __name__ == "__main__":
    main()
