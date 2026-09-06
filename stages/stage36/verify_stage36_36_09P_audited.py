#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09P" / "etau-generic-mw-zero-exceptional-growth-preflight.json"
VERIFIER = ROOT / "stages" / "stage36" / "verify_stage36_36_09P.py"
SOURCE = ROOT / "stages" / "stage36" / "36-09N" / "relative-2isogeny-specialization-source-lock.md"
W03 = ROOT / "docs" / "arsenal" / "cards" / "formal" / "S34-W03.md"
POLICY = ROOT / "docs" / "research-os" / "policies" / "research-credit-and-promotion-firewalls.md"

BASE = "54610c016ef6a27977e382998734982c98d6a191"
V44_BLOB = "2774e95d5da015e9686bdeb1f177f1cb6b410a96"
AUDIT_BASE = "749e06f82a3ffa1e9cb4e831760244e9237f34a4"
MERGE_PARENT = "f1635f67c2a93c85fbb02c3231c554759d45797e"
AUDITED_HEAD = "5a349a03f0b825f4bb557c08754e271715a4810a"
PASS_REVIEW = 5123601403
CERT_BLOB = "a611b698fccfbd29a971ccede5c77b6832101c77"
VERIFIER_BLOB = "5c82e4462b76f58c9eb892435060826a99eaf803"
SOURCE_BLOB = "a562d7053a6f04deff4473067777b7cfd538ea8a"
W03_BLOB = "1d5275321f42768a6414d4610ac912c63be43f96"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def main() -> None:
    s = json.loads(STATE.read_text())
    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V45_THIN_36_09P_AUDITED"
    assert s["status"] == "ACTIVE"
    assert s["base_main_sha"] == BASE
    assert git("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == V44_BLOB
    assert git("rev-parse", f"{BASE}^") == MERGE_PARENT

    # Audit-base -> merge-parent drift must be Stage35-EX only.
    changed = [x for x in git("diff", "--name-only", f"{AUDIT_BASE}..{MERGE_PARENT}").splitlines() if x]
    assert changed
    for path in changed:
        assert path.startswith("stages/stage35-ex/") or path == ".github/workflows/stage35-35-01-to-09-audit.yml", path
        assert not path.startswith("stages/stage36/")
        assert path != "docs/arsenal/cards/formal/S34-W03.md"
        assert path != "stages/stage36/36-09N/relative-2isogeny-specialization-source-lock.md"
        assert path != "docs/research-os/policies/research-credit-and-promotion-firewalls.md"

    # Audited 36-09P payload remains byte-identical.
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09P/etau-generic-mw-zero-exceptional-growth-preflight.json") == CERT_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/verify_stage36_36_09P.py") == VERIFIER_BLOB
    assert blob(CERT) == CERT_BLOB
    assert blob(VERIFIER) == VERIFIER_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(W03) == W03_BLOB
    assert POLICY.exists()

    p = s["authority_frontier"]["36-09P"]
    assert p["status"] == "AUDITED_EXACT_E_TAU_GENERIC_MW_ZERO_AND_EXCEPTIONAL_GROWTH_REDUCTION"
    assert p["pr"] == 1647
    assert p["hostile_audit_review"] == PASS_REVIEW
    assert p["audited_head"] == AUDITED_HEAD
    assert p["exact_head_ci"] == "34002056730/101402561271"
    assert p["merged_main_sha"] == BASE
    assert p["certificate_blob_sha"] == CERT_BLOB
    assert p["verifier_blob_sha"] == VERIFIER_BLOB
    assert p["source_lock_blob_sha"] == SOURCE_BLOB
    assert p["E_TAU_GENERIC_RANK"] == 0
    assert p["E_TAU_GENERIC_TORSION"] == "Z/4 x Z/2"
    assert p["E_TAU_GENERIC_MW_GROUP"] == "Z/4 x Z/2"
    assert p["E_TAU_GENERIC_RECEIVER_COMPATIBLE_POINTS"] == 0
    assert p["SPECIALIZED_RECEIVER_POINT_REQUIRES_MW_GROWTH"] is True
    assert p["MW_GROWTH_SPECIES"] == ["positive rank jump", "torsion growth"]
    assert p["RANK_JUMPS_EXCLUDED"] is False
    assert p["TORSION_GROWTH_EXCLUDED"] is False
    assert p["S34_W03_INTERSECTION_EXECUTED"] is False
    assert p["RECEIVER_CLOSED"] is False
    assert p["E_SIGMA_TAU_GENERIC_RANK_COMPUTED"] is False

    assert s["freshness"]["audit_pr_base"] == AUDIT_BASE
    assert s["freshness"]["audit_merge_parent"] == MERGE_PARENT
    assert s["freshness"]["merged_stage36_main"] == BASE
    assert s["cycle_ledger"]["counts"] == {"live":1,"untested":3,"blocked":6,"dominated":2}

    assert s["current"]["unit"] == "36-09Q"
    assert s["current"]["36_09Q_entry_allowed"] is True
    g = s["promotion_gates"]
    assert g["E_tau_generic_rank0_promoted"] is True
    assert g["E_tau_generic_torsion_promoted"] is True
    assert g["E_tau_generic_receiver_points_excluded_promoted"] is True
    assert g["E_tau_exceptional_MW_growth_reduction_promoted"] is True
    assert g["specialization_rank_jumps_excluded"] is False
    assert g["specialization_torsion_growth_excluded"] is False
    assert g["S34_W03_receiver_intersection_executed"] is False
    assert g["receiver_emptiness_proved"] is False
    assert g["R29_CAMP2_closed"] is False
    assert g["Q11_CAMPEDELLI_closed"] is False
    assert g["endpoint_closed"] is False
    assert g["perfect_cuboid_nonexistence_claim"] is False

    print("36-09P hostile-audited authority promoted; E_tau generic MW frozen; 36-09Q unlocked")


if __name__ == "__main__":
    main()
