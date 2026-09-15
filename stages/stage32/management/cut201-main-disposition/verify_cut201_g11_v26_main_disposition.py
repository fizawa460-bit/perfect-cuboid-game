#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
DISP = HERE / "CUT201-G11-V26-MAIN-DISPOSITION.json"
MAIN = ROOT / "stages/stage32/MAIN-STATE.json"
EXPECTED_CANON = "946ec777f824eaae75aa14d9c3ab5f348bfea38da020e72ede9750c914f86381"
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
    req(DISP.is_file() and MAIN.is_file(), "missing disposition or MAIN state")
    req(blob(MAIN) == EXPECTED_MAIN_BLOB, "MAIN authority projection drift")
    d = json.loads(DISP.read_text())
    m = json.loads(MAIN.read_text())
    req(d["schema"] == "STAGE32_MAIN_CUT201_G11_V26_DISPOSITION_V1", "schema")
    req(d["canonical_sha256_without_this_field"] == EXPECTED_CANON and canon(d) == EXPECTED_CANON, "canonical")
    p = d["producer"]
    req(p["pr"] == 1806 and p["audited_exact_head"] == "8eed1449b325c3b990f90b61471bf7ecec0d89bc", "CUT201 audited source")
    req(p["hostile_audit_review_id"] == 5204865930 and p["audit_status"] == "PASS", "CUT201 audit receipt")
    req(p["result_blob_sha1"] == "ebdf1f741365f7403050f22b478eeea5a7a1d653", "CUT201 result blob")
    req(p["result_canonical_sha256"] == "8f9ccc51046b9559d15ee5d64ef72be35f798a740a78a85df92d865286dbd467", "CUT201 result canonical")
    req(p["verifier_blob_sha1"] == "1aad3b1ffb54b1d3be8e4095091904826fbdfa43", "CUT201 verifier blob")
    c = d["candidate"]
    req(c["target_block_count"] == 255 and c["target_terminal_count"] == 28815, "CUT201 target size")
    req(c["candidate_closed_block_count"] == 226 and c["candidate_pruned_terminals"] == 25538, "CUT201 candidate counts")
    req(c["remaining_nonclosed_block_count"] == 29, "CUT201 residual count")
    s = d["source_authority"]
    req(s["cut_result_main_baseline"] == "V12" and s["main_v12_exact_head"] == "6d63d798adb50dd4efc5f0d5abc553b3dfa23060", "CUT201 V12 baseline")
    req(s["current_main_projection_schema"] == m["schema"], "V26 schema lock")
    f = m["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "MAIN strata drift")
    req(f["authoritative_remaining_terminals"] == 26876434389242951083886, "MAIN terminal authority drift")
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "MAIN semantics drift")
    md = d["main_disposition"]
    req(md["current_v26_subset_identity_proved"] is False, "subset identity promoted")
    req(md["current_v26_post_v12_overlap_accounting_proved"] is False, "overlap accounting promoted")
    req(md["exact_current_v26_incremental_rejected_terminal_count"] is None, "unproved exact increment fabricated")
    req(md["credited_current_v26_incremental_rejected_terminal_count"] == 0, "premature MAIN credit")
    req(md["main_subtraction_performed"] is False and md["main_authority_mutated"] is False, "premature MAIN mutation")
    req(md["cross_lane_demand_id"] == DEMAND_ID, "demand id")
    req(all(v is False for v in d["firewalls"].values()), "credit firewall")
    print("PASS: CUT201 G11 hostile-audited evidence is dispositioned at MAIN with zero current-V26 credit pending an exact subset/no-double-charge adapter")


if __name__ == "__main__":
    main()
