#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
REPAIRED = ROOT / "stages" / "stage36" / "verify_stage36_36_09M.py"
CERT = ROOT / "stages" / "stage36" / "36-09M" / "universal-order4-2isogeny-physical-family-preflight.json"
SOURCE = ROOT / "stages" / "stage36" / "36-09M" / "lmfdb-32a3-source-lock.md"

CURRENT_BASE = "cf5389b857ee52225ed44543ff7ac8d05387583a"
MERGED_V38 = "8607da00e76f9f0ff1759c04b983ba329cca5de6"
V38_BLOB = "6fa174d77f2b5e1d131fae289af79cf522885b15"
CERT_BLOB = "470e87d3e48c857b99793bd8ac0d01eff75eb727"
REPAIRED_BLOB = "5fa2b4c0d57ac50c14dfdb05fc03f2b848967d25"
SOURCE_BLOB = "e820cc4e73af3be46f60f92aede8c076a92504df"
AUDIT_BASE = "dd0fab674db9a10d6494590c1987333aa338a37e"
MERGE_PARENT = "6fa39f76be24b55153f118812b1bd7f41c43e399"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def main() -> None:
    s = json.loads(STATE.read_text())
    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V39_36_09M_USER_PASS_PROMOTED"
    assert s["status"] == "ACTIVE"
    assert s["base_main_sha"] == CURRENT_BASE
    assert git("rev-parse", f"{MERGED_V38}:stages/stage36/MAIN-STATE.json") == V38_BLOB
    assert blob(CERT) == CERT_BLOB
    assert blob(REPAIRED) == REPAIRED_BLOB
    assert blob(SOURCE) == SOURCE_BLOB

    changed = [x for x in git("diff", "--name-only", f"{AUDIT_BASE}..{MERGE_PARENT}").splitlines() if x]
    assert changed
    for path in changed:
        assert path.startswith("stages/stage35-ex/") or path == ".github/workflows/stage35-35-01-to-09-audit.yml"

    sync_changed = [x for x in git("diff", "--name-only", f"{MERGED_V38}..{CURRENT_BASE}").splitlines() if x]
    assert sync_changed
    for path in sync_changed:
        assert path.startswith("stages/stage33/") or path == ".github/workflows/stage33-v41-e3-source.yml"

    m = s["authority_frontier"]["36-09M"]
    assert m["status"] == "USER_PASS_PROMOTED_AFTER_HOSTILE_MATH_PASS_AND_VERIFIER_REPAIR"
    assert m["hostile_audit_outcome"] == "FAIL_VERIFIER_COVERAGE_ONLY_MATHEMATICS_PASS"
    assert m["user_pass_override"] is True
    assert m["certificate_blob_sha"] == CERT_BLOB
    assert m["repaired_verifier_blob_sha"] == REPAIRED_BLOB
    assert m["source_lock_blob_sha"] == SOURCE_BLOB
    assert m["C8_RATIONAL_POINTS_EXHAUSTED"] is True
    assert m["PHYSICAL_K_AND_MINUS_K_NONSQUARE"] is True
    assert m["E_K_2PRIMARY_TORSION"] == "Z/4 x Z/2"
    assert m["E_K_PRIME_2PRIMARY_TORSION"] == "(Z/2)^2"
    assert m["FULL_TORSION_SUBGROUP_PROVED"] is False
    assert m["B3_RELATIVE_2_ISOGENY_ROUTE"] == "LIVE"

    assert s["cycle_ledger"]["counts"] == {"live":1,"untested":3,"blocked":6,"dominated":2}
    assert s["current"]["unit"] == "36-09N"
    assert s["current"]["36_09N_entry_allowed"] is True
    assert s["promotion_gates"]["verifier_coverage_repaired"] is True
    assert s["promotion_gates"]["two_primary_torsion_control_promoted"] is True
    assert s["promotion_gates"]["full_torsion_subgroup_proved"] is False
    assert s["promotion_gates"]["isogeny_Selmer_groups_computed"] is False
    assert s["promotion_gates"]["uniform_Mordell_Weil_group_proved"] is False
    assert s["promotion_gates"]["receiver_emptiness_proved"] is False
    assert s["promotion_gates"]["R29_CAMP2_closed"] is False

    print("36-09M user-pass promotion verified after exact verifier repair and current-main sync; 36-09N unlocked without higher credit")


if __name__ == "__main__":
    main()
