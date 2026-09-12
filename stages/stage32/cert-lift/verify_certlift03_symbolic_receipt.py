#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import g3_mass7_symbolic_parity_lemma as lemma

RECEIPT = HERE / "CERTLIFT-03-G3-MASS7-SYMBOLIC-RECEIPT.json"
EXPECTED_CANONICAL = "2d1fcfe51420ab01f81d353e0d19a2b1eef467a51e321da953b5cf18aa88e764"
EXPECTED_REPLAY = "a48db497fc3a7e4b2ace3edcc03714f3c956724a7b6aad6bcd36f8e806bb9a9b"
EXPECTED_FIBRE = "aa3d9b6b16738fc0594daa0b2cfcfbf8043afc1ac0e3e651e1be5153f3d8ab1c"
EXPECTED_PROFILE = "ce8fd6bf083a08f0e59f7617aaf3e4157a51aa01278ebc4d0fd3f7815840525d"


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def main() -> None:
    r = json.loads(RECEIPT.read_text())
    req(r["status"] == "SYMBOLIC_CANDIDATE_PASS_PENDING_HOSTILE_AUDIT", "receipt status drift")
    req(r["symbolic_lemma"]["canonical"] == EXPECTED_CANONICAL, "symbolic canonical drift")
    req(r["finite_replay"]["canonical"] == EXPECTED_REPLAY, "finite replay canonical drift")
    req(r["pre_picard_replay"]["canonical"] == EXPECTED_FIBRE, "pre-Picard replay canonical drift")
    req(r["failure_profile"]["canonical"] == EXPECTED_PROFILE, "failure profile canonical drift")
    req(r["finite_replay"]["targeted_blocks"] == 1852 and r["finite_replay"]["closed_blocks"] == 1852, "finite replay count drift")
    req(r["finite_replay"]["survivors"] == 0, "finite replay survivor regression")
    req(r["pre_picard_replay"]["post_fibre_configurations"] == 0, "post-fibre configuration regression")
    req(r["failure_profile"]["exact_exceptional_completions"] == 23608, "completion-count drift")
    req(r["failure_profile"]["fibre_feasible_completions"] == 0, "fibre-feasible completion regression")
    req(r["source_locked_geometry"]["free_exceptional_labels_with_g3_cell_pair_4_5"] == [], "residual g3-pair escape drift")
    req(r["audit"]["hostile_audited"] is False, "unaudited receipt upgraded unexpectedly")
    req(not any(r["credit"].values()), "credit firewall regression")

    live = lemma.run()
    req(live["status"] == "PASS_SYMBOLIC_MASS7_G3_FIBRE_PARITY_LEMMA_D8_E8", "live symbolic lemma failed")
    req(live["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL, "live symbolic canonical mismatch")
    req(live["source_locked_geometry"]["free_labels_with_g3_cell_pair_4_5"] == [], "live source geometry residual escape")

    print(json.dumps({
        "status": "PASS_CERTLIFT03_SYMBOLIC_RECEIPT_REPLAY",
        "receipt_status": r["status"],
        "symbolic_canonical": EXPECTED_CANONICAL,
        "finite_replay_closed": r["finite_replay"]["closed_blocks"],
        "exact_exceptional_completions": r["failure_profile"]["exact_exceptional_completions"],
        "hostile_audited": r["audit"]["hostile_audited"],
        "main_credit": r["credit"]["stage32_main_pruning_credit"],
        "merge_authorized": r["credit"]["merge_authorized"]
    }, sort_keys=True))


if __name__ == "__main__":
    main()
