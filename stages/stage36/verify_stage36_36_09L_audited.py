#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09L" / "physical-base-full2-descent-preflight.json"
VERIFY = ROOT / "stages" / "stage36" / "verify_stage36_36_09L.py"

AUDITED_HEAD = "98d057a47fc37a897fb14e904cdf9d52913f082b"
AUDIT_BASE = "f91c045796cba859ec1dd172cf7871fcac5f6d8a"
MERGE_PARENT = "e2103a2de367a0a6d0826b044b6bb83d24ad6f6f"
MERGED_MAIN = "b6b538b4c8838e24ddf99eb05fc022fe50056af4"
CURRENT_BASE = MERGED_MAIN
AUDIT_REVIEW = 5123231006
CI = "33995276496/101384623587"
CERT_BLOB = "56fd432a3ae6046bc4643b56bf562660af49fe89"
VERIFY_BLOB = "d59215520dd5c5ef265672b60681df65ef7b0292"
V36_BLOB = "85239c06bf81dc934bfdd5193b4b0236baaa5d22"
ARSENAL_INDEX_BLOB = "aa45d19c2f1d8970c7f142bf744c5c17e75abe5a"

EXPECTED_DRIFT = {
    ".github/workflows/stage33-v41-e3-source.yml",
    ".github/workflows/stage35-35-01-to-09-audit.yml",
    "stages/stage33/33-12/e3-v91c1b-a2-02-resolved-valuation-carrier-preflight.json",
    "stages/stage33/33-12/e3-v91c1c-a2-02-strict-transform-prime-refinement.json",
    "stages/stage33/33-12/verify_e3_v91c1b_a2_02_resolved_valuation_carrier_preflight.py",
    "stages/stage33/33-12/verify_e3_v91c1c_a2_02_strict_transform_prime_refinement.py",
    "stages/stage33/33-12/verify_stage33_v91c1c_candidate_current_startup_v95.py",
    "stages/stage33/MAIN-STATE.json",
    "stages/stage33/sync_main_state.py",
    "stages/stage35-ex/35ex-35/goal4d-full-q7-valuation-crossface-closure.json",
    "stages/stage35-ex/MAIN-STATE.json",
    "stages/stage35-ex/verify_stage35_ex_35_goal4d.py",
    "stages/stage35-ex/verify_stage35_ex_v41_legacy_replay.py",
}


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def main() -> None:
    s = json.loads(STATE.read_text())
    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V37_THIN_36_09L_AUDITED"
    assert s["status"] == "ACTIVE"
    assert s["base_main_sha"] == CURRENT_BASE

    L = s["authority_frontier"]["36-09L"]
    assert L["status"] == "AUDITED_PHYSICAL_BASE_FULL2_DESCENT_PREFLIGHT"
    assert L["pr"] == 1632 and L["hostile_audit_review"] == AUDIT_REVIEW
    assert L["audited_head"] == AUDITED_HEAD and L["exact_head_ci"] == CI
    assert L["certificate_blob_sha"] == CERT_BLOB and L["verifier_blob_sha"] == VERIFY_BLOB
    assert L["merged_main_sha"] == MERGED_MAIN
    assert L["ROOT_DIFFERENCE_SQUARECLASSES"] == ["1", "1", "[2*h]"]
    assert L["UNIVERSAL_RATIONAL_ORDER4_POINT"] is True
    assert L["CERTIFIED_TORSION_SUBGROUP"] == "Z/4 x Z/2"
    assert L["FULL_TORSION_SUBGROUP_PROVED"] is False
    assert L["EXACT_2_ISOGENY_FAMILY_ADAPTER"] is True
    assert L["FIXED_S_UNIFORM_FULL2_DESCENT"] == "BLOCKED"
    assert L["B3_TORSION_ENHANCED_2_ISOGENY_FAMILY"] == "LIVE"

    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09L/physical-base-full2-descent-preflight.json") == CERT_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/verify_stage36_36_09L.py") == VERIFY_BLOB
    assert git("rev-parse", f"{MERGED_MAIN}:stages/stage36/36-09L/physical-base-full2-descent-preflight.json") == CERT_BLOB
    assert git("rev-parse", f"{MERGED_MAIN}:stages/stage36/verify_stage36_36_09L.py") == VERIFY_BLOB
    assert git("rev-parse", f"{MERGED_MAIN}:stages/stage36/MAIN-STATE.json") == V36_BLOB
    assert git("rev-parse", f"{MERGED_MAIN}^") == MERGE_PARENT

    drift = set(git("diff", "--name-only", AUDIT_BASE, MERGE_PARENT).splitlines())
    assert drift == EXPECTED_DRIFT
    assert not any(p.startswith("stages/stage36/") or p.startswith("docs/arsenal/") or p.startswith("docs/research-os/") for p in drift)

    assert blob(CERT) == CERT_BLOB and blob(VERIFY) == VERIFY_BLOB
    assert git("rev-parse", "HEAD:docs/arsenal/index.json") == ARSENAL_INDEX_BLOB

    assert s["cycle_ledger"]["counts"] == {"live": 1, "untested": 3, "blocked": 6, "dominated": 2}
    assert s["cycle_ledger"]["B3_FINITE_CURVE_OR_COVER_DECOMPOSITION"].startswith("LIVE_")
    assert s["current"]["unit"] == "36-09M"
    assert s["current"]["36_09M_entry_allowed"] is True
    assert s["promotion_gates"]["universal_order4_promoted"] is True
    assert s["promotion_gates"]["exact_2_isogeny_family_adapter_promoted"] is True
    assert s["promotion_gates"]["fixed_S_uniform_full2_descent_blocked"] is True
    assert s["promotion_gates"]["full_2_Selmer_group_computed"] is False
    assert s["promotion_gates"]["full_torsion_subgroup_proved"] is False
    assert s["promotion_gates"]["uniform_Mordell_Weil_group_proved"] is False
    assert s["promotion_gates"]["receiver_emptiness_proved"] is False
    assert s["promotion_gates"]["R29_CAMP2_closed"] is False

    print("36-09L hostile PASS promoted; universal order4 and exact 2-isogeny adapter audited; fixed-S subroute blocked; 36-09M unlocked")


if __name__ == "__main__":
    main()
