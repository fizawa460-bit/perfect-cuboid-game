#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09K" / "genus-one-quartic-elliptic-adapter.json"
VERIFY = ROOT / "stages" / "stage36" / "verify_stage36_36_09K.py"
AUDITED_HEAD = "e10530918619cea1fc1720a6074ea0ca0499f904"
AUDIT_BASE = "0bc325f9b9db817193bc271121d19cb04970c5b9"
MERGE_PARENT = "12f0adb9a70e387f0a3ad6c37d6f22a3fb78cda6"
MERGED_MAIN = "40cd38c5f5d2679874ce3be882cc67d17d4c7558"
CURRENT_BASE = "40cd38c5f5d2679874ce3be882cc67d17d4c7558"
AUDIT_REVIEW = 5123183075
CI = "33994269460/101381855654"
CERT_BLOB = "1a838c473343eb0eac0a0a871c95fdf207475d53"
VERIFY_BLOB = "fdf02d8fcf4c095661e4ad0a35f1f94e46b70f9c"
V34_BLOB = "f644da4012991b4887290ec5ad0008e8fa946062"
S31_W01_BLOB = "122a6c1c5c871c1c7b797017e854de8ec55e7c50"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def main() -> None:
    s = json.loads(STATE.read_text())
    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V35_THIN_36_09K_AUDITED"
    assert s["status"] == "ACTIVE"
    assert s["base_main_sha"] == CURRENT_BASE

    k = s["authority_frontier"]["36-09K"]
    assert k["status"] == "AUDITED_EXACT_GENUS_ONE_QUARTIC_ELLIPTIC_ADAPTER"
    assert k["pr"] == 1628 and k["hostile_audit_review"] == AUDIT_REVIEW
    assert k["audited_head"] == AUDITED_HEAD and k["exact_head_ci"] == CI
    assert k["certificate_blob_sha"] == CERT_BLOB and k["verifier_blob_sha"] == VERIFY_BLOB
    assert k["merged_main_sha"] == MERGED_MAIN
    assert k["FORWARD_INVERSE_RATIONAL_MAPS_CERTIFIED"] is True
    assert k["PROJECTIVE_EXCEPTIONAL_LOCUS_COMPLETE"] is True
    assert k["INVERSE_DENOMINATOR_PHYSICAL_COLLISIONS"] == 0
    assert k["PHYSICAL_FULL_RATIONAL_2_TORSION"] is True
    assert k["S31_W01_ADAPTER_CERTIFICATE_COMPLETE"] is True
    assert k["S31_W01_PROMOTED_TRIGGER"] is True

    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09K/genus-one-quartic-elliptic-adapter.json") == CERT_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/verify_stage36_36_09K.py") == VERIFY_BLOB
    assert git("rev-parse", f"{MERGED_MAIN}:stages/stage36/36-09K/genus-one-quartic-elliptic-adapter.json") == CERT_BLOB
    assert git("rev-parse", f"{MERGED_MAIN}:stages/stage36/verify_stage36_36_09K.py") == VERIFY_BLOB
    assert git("rev-parse", f"{MERGED_MAIN}:stages/stage36/MAIN-STATE.json") == V34_BLOB
    assert git("rev-parse", f"{MERGED_MAIN}:docs/arsenal/cards/formal/S31-W01.md") == S31_W01_BLOB
    assert git("rev-parse", f"{MERGED_MAIN}^") == MERGE_PARENT

    drift = set(git("diff", "--name-only", AUDIT_BASE, MERGE_PARENT).splitlines())
    assert drift == {
        ".github/workflows/stage35-35-01-to-09-audit.yml",
        "stages/stage35-ex/35ex-35/goal4c-mod7-private-gcd-support-receiver.json",
        "stages/stage35-ex/MAIN-STATE.json",
        "stages/stage35-ex/verify_stage35_ex_35_goal4c.py",
        "stages/stage35-ex/verify_stage35_ex_v40_legacy_replay.py",
    }

    assert blob(CERT) == CERT_BLOB and blob(VERIFY) == VERIFY_BLOB
    assert s["cycle_ledger"]["counts"] == {"live": 1, "untested": 3, "blocked": 6, "dominated": 2}
    assert s["current"]["unit"] == "36-09L"
    assert s["current"]["36_09L_entry_allowed"] is True
    assert s["current"]["next_exact_leaf"] == "36-09L_PHYSICAL_BASE_FULL_2_TORSION_DESCENT_PREFLIGHT"
    assert s["promotion_gates"]["genus_one_quartic_adapter_triggered"] is True
    assert s["promotion_gates"]["physical_full_rational_2_torsion_certified"] is True
    assert s["promotion_gates"]["uniform_Mordell_Weil_group_proved"] is False
    assert s["promotion_gates"]["quartic_rational_points_exhausted"] is False
    assert s["promotion_gates"]["receiver_emptiness_proved"] is False
    assert s["promotion_gates"]["R29_CAMP2_closed"] is False
    assert s["claims"]["genus_one_quartic_adapter_promoted"] is True
    for key, value in s["claims"].items():
        if key != "genus_one_quartic_adapter_promoted":
            assert value is False, key
    print("36-09K hostile audit promoted; exact elliptic adapter/full rational 2-torsion audited; 36-09L unlocked")


if __name__ == "__main__":
    main()
