#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
SOURCE = ROOT / "stages" / "stage36" / "36-09N" / "relative-2isogeny-specialization-source-lock.md"
CERT = ROOT / "stages" / "stage36" / "36-09N" / "relative-2isogeny-kummer-image-rank1-preflight.json"
VERIFIER = ROOT / "stages" / "stage36" / "verify_stage36_36_09N.py"

BASE = "2b0516975cda83df31a0a6b247a7d2b81ba550fe"
V40_BLOB = "ab619d48917321194676ec7544d4abad05e42011"
AUDITED_HEAD = "8ca23e42a057af260c7051c20dd8f608067efefd"
AUDIT_BASE = "824355f591f8f951fda9f2a7c1f4e3e66d4e1e9a"
MERGE_PARENT = "dbcff26c0267416caa4fdd0515293396d0f86887"
CERT_BLOB = "02a14439d94d7f6e5ac2f65e995e8acfb6845788"
VERIFIER_BLOB = "e7effbe9ee6106505db013f326ec653627885054"
AUDITED_SOURCE_BLOB = "e7c98981fbb1d523fd7db54478dc09aa87b547e8"
CORRECTED_SOURCE_BLOB = "a562d7053a6f04deff4473067777b7cfd538ea8a"
PASS_REVIEW = 5123389934


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def main() -> None:
    s = json.loads(STATE.read_text())
    src = SOURCE.read_text()

    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V41_THIN_36_09N_AUDITED"
    assert s["status"] == "ACTIVE"
    assert s["base_main_sha"] == BASE
    assert git("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == V40_BLOB

    # Exact audited mathematical payload is immutable.
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09N/relative-2isogeny-kummer-image-rank1-preflight.json") == CERT_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/verify_stage36_36_09N.py") == VERIFIER_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09N/relative-2isogeny-specialization-source-lock.md") == AUDITED_SOURCE_BLOB
    assert blob(CERT) == CERT_BLOB
    assert blob(VERIFIER) == VERIFIER_BLOB

    # Post-audit change is wording-only source attribution; mathematical source facts remain.
    assert blob(SOURCE) == CORRECTED_SOURCE_BLOB
    for needle in [
        "No theorem number is asserted here.",
        "stronger unique-prime-style sufficient condition",
        "changes no Stage36 mathematical conclusion",
        "2^r = |Im(alpha)|*|Im(beta)|/4",
    ]:
        assert needle in src

    # Freshness: exactly one Stage33-only commit intervened before #1640 merge.
    changed = [x for x in git("diff", "--name-only", f"{AUDIT_BASE}..{MERGE_PARENT}").splitlines() if x]
    assert changed
    for path in changed:
        assert path.startswith("stages/stage33/") or path == ".github/workflows/stage33-v41-e3-source.yml"

    n = s["authority_frontier"]["36-09N"]
    assert n["status"] == "AUDITED_EXACT_RELATIVE_KUMMER_AND_GENERIC_RANK1"
    assert n["pr"] == 1640
    assert n["hostile_audit_review"] == PASS_REVIEW
    assert n["audited_head"] == AUDITED_HEAD
    assert n["exact_head_ci"] == "33998632868/101393423222"
    assert n["certificate_blob_sha"] == CERT_BLOB
    assert n["verifier_blob_sha"] == VERIFIER_BLOB
    assert n["audited_source_lock_blob_sha"] == AUDITED_SOURCE_BLOB
    assert n["corrected_source_lock_blob_sha"] == CORRECTED_SOURCE_BLOB
    assert n["SOURCE_ATTRIBUTION_CORRECTED_POST_AUDIT"] is True
    assert n["GENERIC_FUNCTION_FIELD_MW_RANK"] == 1
    assert n["EXACT_ALPHA_IMAGE"] == ["[1]", "[-1]", "[C]", "[-C]"]
    assert n["EXACT_BETA_IMAGE"] == ["[1]", "[2]"]
    assert n["FIBERWISE_RANK_ONE_FOR_EVERY_RATIONAL_Q_PROVED"] is False
    assert n["SPECIALIZATION_RANK_JUMPS_EXCLUDED"] is False

    assert s["cycle_ledger"]["counts"] == {"live":1,"untested":3,"blocked":6,"dominated":2}
    assert s["current"]["unit"] == "36-09O"
    assert s["current"]["36_09O_entry_allowed"] is True
    assert s["promotion_gates"]["generic_function_field_rank1_promoted"] is True
    assert s["promotion_gates"]["exact_generic_kummer_images_promoted"] is True
    assert s["promotion_gates"]["fiberwise_rank_one_for_every_rational_q_proved"] is False
    assert s["promotion_gates"]["uniform_Mordell_Weil_group_proved"] is False
    assert s["promotion_gates"]["receiver_emptiness_proved"] is False
    assert s["promotion_gates"]["R29_CAMP2_closed"] is False

    print("36-09N hostile-audited authority promoted; source attribution clarified; 36-09O unlocked without fiberwise-rank credit")


if __name__ == "__main__":
    main()
