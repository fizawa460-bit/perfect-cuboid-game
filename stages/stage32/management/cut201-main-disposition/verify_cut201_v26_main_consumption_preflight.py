#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
PREFLIGHT = HERE / "CUT201-V26-MAIN-CONSUMPTION-PREFLIGHT.json"
MAIN = ROOT / "stages/stage32/MAIN-STATE.json"
EXPECTED_CANON = "1c65420fbd2ff79c466630f221edcd1ceb3d58a36e65bbdf28461f24b2da3bf6"
EXPECTED_MAIN_BLOB = "9242ffc2d44d68b7c6e3a3946fa26f18288fe51b"
DEMAND_ID = "S32.DEMAND.CUT201.CUT.MAIN.V26_CURRENT_AUTHORITY_ADAPTER.V1"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], cwd=ROOT, text=True).strip()


def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def main() -> None:
    req(PREFLIGHT.is_file() and MAIN.is_file(), "missing preflight or MAIN state")
    req(blob(MAIN) == EXPECTED_MAIN_BLOB, "MAIN authority projection drift")
    p = json.loads(PREFLIGHT.read_text())
    m = json.loads(MAIN.read_text())
    req(p["schema"] == "STAGE32_MAIN_CUT201_V26_CONSUMPTION_PREFLIGHT_V1", "schema")
    req(p["canonical_sha256_without_this_field"] == EXPECTED_CANON and canon(p) == EXPECTED_CANON, "canonical")
    req(p["status"] == "HOLD_EXACT_ADAPTER_HOSTILE_AUDIT_RECEIPT_NOT_REPOSITORY_BOUND", "hold status")

    s = p["source_locks"]
    req(s["producer_pr"] == 1806, "producer PR")
    req(s["producer_live_head"] == "9b485b4e643b7ed041629547fdb4a867e31c00cd", "producer live head")
    req(s["bounded_cut_audited_exact_head"] == "8eed1449b325c3b990f90b61471bf7ecec0d89bc", "bounded CUT audited head")
    req(s["bounded_cut_hostile_audit_review_id"] == 5204865930, "bounded CUT audit receipt")
    req(s["main_state_blob_sha1"] == EXPECTED_MAIN_BLOB, "preflight MAIN blob lock")

    c = p["candidate"]
    req(c["source_candidate_terminals"] == 25538, "source candidate count")
    req(c["certlift03_exact_overlap_terminals"] == 6780 and c["certlift03_exact_overlap_blocks"] == 60, "CERTLIFT03 overlap")
    req(c["exact_incremental_terminals"] == 18758 and c["exact_incremental_blocks"] == 166, "exact incremental set")
    req(c["double_charge"] is False and c["other_consumed_route_overlap_terminals"] == 0, "no-double-charge firewall")

    g = p["audit_gate"]
    req(g["bounded_cut_result_hostile_audited"] is True, "bounded CUT audit lost")
    req(g["current_v26_adapter_exact_ci_observed_green"] is True, "adapter CI observation")
    req(g["repository_bound_exact_adapter_hostile_audit_receipt"] is None, "adapter audit receipt fabricated")
    req(g["claim_sync_contract_requires_exact_pass_receipt_before_audited_consumption"] is True, "claim-sync gate weakened")
    req(g["demand_id"] == DEMAND_ID and g["demand_may_be_marked_satisfied_now"] is False, "demand prematurely satisfied")
    req(g["main_consumption_authorized"] is False, "MAIN consumption prematurely authorized")

    f = p["authority_firewall"]
    mf = m["current_exact_frontier"]
    req(f["authoritative_remaining_strata_before"] == mf["authoritative_remaining_strata"] == 17128, "MAIN strata drift")
    req(f["authoritative_remaining_terminals_before"] == mf["authoritative_remaining_terminals"] == 26876434389242951083886, "MAIN terminal authority drift")
    req(f["credited_incremental_rejected_terminals_now"] == 0, "premature pruning credit")
    req(f["main_authority_mutated"] is False, "premature MAIN authority mutation")
    req(f["hypothetical_remaining_terminals_if_future_exact_adapter_audit_passes_and_main_consumes_once"] == 26876434389242951065128, "future arithmetic")
    for k in ("full178_complete", "effectivity_credit", "receiver_credit", "theorem_credit", "endpoint_credit", "stage32_closed", "merge_authorized"):
        req(f[k] is False, f"firewall {k}")

    print("PASS: CUT201 V26 MAIN consumption remains fail-closed at exact 18,758-terminal candidate pending a repository-bound exact adapter hostile-audit PASS receipt")


if __name__ == "__main__":
    main()
