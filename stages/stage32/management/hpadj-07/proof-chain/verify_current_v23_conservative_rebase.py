#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
RESULT = HERE / "CURRENT-V23-CONSERVATIVE-REBASE.json"
CORRECTED = HERE / "GENERAL-TYPE-ADJUNCTION-CORRECTION.json"
MAIN = ROOT / "stages/stage32/MAIN-STATE.json"

EXPECTED_RESULT_CANON = "9ae15dd70a3ba84fe83d2d11dfa8e1081c44a8b06e68b78dda4f871aa0f00e01"
EXPECTED_CORRECTED_CANON = "87e9ee4ea791d894f5f1ba093d5ad295ad2ebb3d569f2f50fa9a1b1d4c1858aa"
EXPECTED_MAIN_BLOB = "bead809db3a008dd35d664a8923f06fecb7de5bb"
V22 = 47589703313957134804198
V23 = 47589703313957134649501
CORRECTED_V22 = 20713268924714183714810
EXPECTED_V23_LB = 20713268924714183560113


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def main() -> None:
    req(git_blob(MAIN) == EXPECTED_MAIN_BLOB, "current MAIN-STATE blob drift")
    main = json.loads(MAIN.read_text(encoding="utf-8"))
    frontier = main["current_exact_frontier"]
    req(frontier["authoritative_remaining_terminals"] == V23, "V23 terminal authority drift")
    req(frontier["authoritative_remaining_strata"] == 17128, "V23 stratum authority drift")
    req(frontier["certlift03_incremental_rejected_terminals"] == V22 - V23 == 154697,
        "V22->V23 removal identity drift")

    corrected = json.loads(CORRECTED.read_text(encoding="utf-8"))
    req(corrected.get("canonical_sha256_without_this_field") == EXPECTED_CORRECTED_CANON, "corrected stored canonical")
    req(canon(corrected) == EXPECTED_CORRECTED_CANON, "corrected canonical")
    req(corrected["corrected_v22_conservative_replay"]["candidate_rejected_terminals_lower_bound"] == CORRECTED_V22,
        "corrected V22 lower bound drift")

    result = json.loads(RESULT.read_text(encoding="utf-8"))
    req(result.get("canonical_sha256_without_this_field") == EXPECTED_RESULT_CANON, "rebase stored canonical")
    req(canon(result) == EXPECTED_RESULT_CANON, "rebase canonical")
    removal = V22 - V23
    lower = CORRECTED_V22 - removal
    req(lower == EXPECTED_V23_LB, "V23 worst-case lower-bound arithmetic")
    req(result["set_theoretic_rebase"]["therefore_current_v23_hpadj_rejected_lower_bound"] == lower,
        "retained V23 lower bound drift")
    req(result["set_theoretic_rebase"]["candidate_remaining_upper_bound_if_corrected_hpadj_promoted"] == V23 - lower,
        "retained V23 remaining upper bound drift")
    req(result["set_theoretic_rebase"]["requires_exact_overlap_for_exact_increment"] is False,
        "conservative set bound must not require exact overlap")
    req(result["firewalls"]["main_pruning_credit"] is False, "premature MAIN pruning credit")
    req(result["firewalls"]["merge_authorized"] is False, "merge authorization drift")

    print(json.dumps({
        "verdict": "PASS_HPADJ07_CURRENT_V23_CONSERVATIVE_REBASE_CANDIDATE",
        "v22_to_v23_removed": removal,
        "corrected_v22_hpadj_lower_bound": CORRECTED_V22,
        "current_v23_hpadj_lower_bound": lower,
        "current_v23_remaining_upper_bound_if_promoted": V23 - lower,
        "main_pruning_credit": False,
        "hostile_audit_required": True,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
