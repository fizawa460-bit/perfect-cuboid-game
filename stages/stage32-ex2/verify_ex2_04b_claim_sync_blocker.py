#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ART = HERE / "EX2-04/ex2-04b-claim-sync-blocker.json"
EX2_04B = HERE / "EX2-04/third-section-valuation-separation.json"
SYNC = ROOT / "stages/stage32/proof/CLAIM-SYNC-CONTRACT.md"
EXPECTED_CANON = "efdef1983868b1490fa6d76deddfb44be358c51f27a0db12fb98d7d1795f62ab"


def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], cwd=ROOT, text=True).strip()


def canon(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    d = json.loads(ART.read_text())
    b = json.loads(EX2_04B.read_text())
    assert d["schema"] == "STAGE32EX2_EX2_04B_CLAIM_SYNC_BLOCKER_V1"
    assert d["status"] == "BLOCKED_INHERITED_CURRENT_MAIN_CLAIM_DAG_SOURCE_LOCK_DRIFT"
    assert d["canonical_sha256_without_this_field"] == EXPECTED_CANON
    assert canon(d) == EXPECTED_CANON
    assert d["freshness"]["current_main_sha"] == "70265586b3f97be21c7621af73f443311f1f3fa3"
    assert blob(EX2_04B) == d["retained_ex2_result"]["artifact_blob_sha1"] == "5e9cf16ece57162db995cb1b7014a9d583453202"
    assert blob(SYNC) == d["freshness"]["claim_sync_contract_blob_sha1"] == "bbab1b565afbd2e767fc6cc4325c5167d42919b4"
    assert b["reconstruction"]["certified_section_subspace_dimension"] == 3
    assert b["reconstruction"]["complete_H0"] is False
    assert d["retained_ex2_result"]["authority_status"] == "SCRATCH_PENDING_CLAIM_SYNC"
    assert d["retained_ex2_result"]["stage32_main_credit"] is False
    assert d["diagnostic_evidence"]["main_baseline_source_lock_mismatch_count"] == 4
    assert d["diagnostic_evidence"]["main_baseline_failure_preexists_ex2_overlay"] is True
    assert d["diagnostic_evidence"]["main_baseline_failed_phase"] == "source-locks"
    assert d["claim_sync_contract_interpretation"]["core_change_requires_new_versioned_claim_id"] is True
    assert d["claim_sync_contract_interpretation"]["audited_status_requires_exact_hostile_audit_pass_for_same_claim_core_evidence_boundary"] is True
    assert d["decision"]["claim_dag_sync_complete"] is False
    assert d["decision"]["advance_to_ex2_04c_before_sync"] is False
    assert d["decision"]["merge_authorized"] is False
    for value in d["firewalls"].values():
        assert value is False
    print("PASS Stage32EX2 EX2-04B claim-sync blocker checkpoint")
    print("retained_math=3D_divisor_theoretic_subspace authority=SCRATCH_PENDING_CLAIM_SYNC")
    print("blocker=inherited_current_main_source_lock_drift main_mismatch_count=4")
    print("advance_to_EX2_04C=false stage32_main_credit=false")


if __name__ == "__main__":
    main()
