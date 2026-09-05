#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stage36" / "36-09J" / "reciprocal-involution-two-linear-cover-preflight.json"
VERIFY = ROOT / "stage36" / "verify_stage36_36_09J.py"
AUDITED_HEAD = "6ede28751914a881a5ddaca7691538a8a3e4780c"
AUDIT_BASE = "d761baa2d2d5e69479ef191041c5e2f017a50283"
MERGE_PARENT = "ab01a77fbedf2efba21a7744ccc798201c0cc672"
MERGED_MAIN = "8ff10455b27a789a6ba71c354042be0f79a2b3a6"
CURRENT_BASE = "cc27e6d6146e93e1928b467cda3464845350b7c1"
AUDIT_REVIEW = 5123112446
CI = "33971092160/101319624484"
CERT_BLOB = "72e9ca86f726f2ff286c983138d9381acdd97e62"
VERIFY_BLOB = "b5357a344ffab51118f4f1ec92904367c79c6541"
V32_BLOB = "936b0282a6e0f37c6ac8b81683a00cdaeecdce2e"

def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT.parent, text=True).strip()

def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT.parent)))

def main() -> None:
    s = json.loads(STATE.read_text())
    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V33_THIN_36_09J_AUDITED"
    assert s["status"] == "ACTIVE"
    assert s["base_main_sha"] == CURRENT_BASE
    a = s["authority_frontier"]["36-09J"]
    assert a["status"] == "AUDITED_RECIPROCAL_PHYSICAL_FIBER_TOWER_GENUS_3_1_0"
    assert a["pr"] == 1624 and a["hostile_audit_review"] == AUDIT_REVIEW
    assert a["audited_head"] == AUDITED_HEAD and a["exact_head_ci"] == CI
    assert a["certificate_blob_sha"] == CERT_BLOB and a["verifier_blob_sha"] == VERIFY_BLOB
    assert a["merged_main_sha"] == MERGED_MAIN
    assert a["PHYSICAL_FIBER_GENUS_SEQUENCE"] == [3, 1, 0]
    assert a["S31_W01_TYPE_MATCH"] is True and a["S31_W01_TRIGGERED"] is False
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09J/reciprocal-involution-two-linear-cover-preflight.json") == CERT_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/verify_stage36_36_09J.py") == VERIFY_BLOB
    assert git("rev-parse", f"{MERGED_MAIN}:stages/stage36/36-09J/reciprocal-involution-two-linear-cover-preflight.json") == CERT_BLOB
    assert git("rev-parse", f"{MERGED_MAIN}:stages/stage36/verify_stage36_36_09J.py") == VERIFY_BLOB
    assert git("rev-parse", f"{MERGED_MAIN}:stages/stage36/MAIN-STATE.json") == V32_BLOB
    assert git("rev-parse", f"{MERGED_MAIN}^") == MERGE_PARENT
    drift = set(git("diff", "--name-only", AUDIT_BASE, MERGE_PARENT).splitlines())
    assert drift == {"stages/stage32/MAIN-STATE.json", "stages/stage32/verify_main_startup.py"}
    post = set(git("diff", "--name-only", MERGED_MAIN, CURRENT_BASE).splitlines())
    assert post == {".github/workflows/stage35-35-01-to-09-audit.yml", "stages/stage35-ex/35ex-35/goal4b-mod7-local-restriction.json", "stages/stage35-ex/MAIN-STATE.json", "stages/stage35-ex/verify_stage35_ex_35_goal4b.py", "stages/stage35-ex/verify_stage35_ex_v38_legacy_replay.py"}
    assert blob(CERT) == CERT_BLOB and blob(VERIFY) == VERIFY_BLOB
    assert s["cycle_ledger"]["counts"] == {"live": 1, "untested": 3, "blocked": 6, "dominated": 2}
    assert s["current"]["unit"] == "36-09K"
    assert s["current"]["36_09K_entry_allowed"] is True
    assert s["current"]["next_exact_leaf"] == "36-09K_GENUS_ONE_QUARTIC_ELLIPTIC_ADAPTER_PREFLIGHT"
    assert s["promotion_gates"]["generic_cover_genera_classified"] is True
    assert s["promotion_gates"]["genus_one_quartic_adapter_triggered"] is False
    assert s["promotion_gates"]["receiver_emptiness_proved"] is False
    assert s["promotion_gates"]["R29_CAMP2_closed"] is False
    assert all(v is False for v in s["claims"].values())
    print("36-09J hostile audit promoted; genus 3->1->0 tower audited; 36-09K unlocked")

if __name__ == "__main__":
    main()
