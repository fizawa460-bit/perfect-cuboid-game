#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
B2 = HERE / "breadth-cycle-2"
MODE = "FULL178_AND_FINAL_MILESTONE_CHAIN"
CURRENT_LEAF = "BC2_17_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT"
MAIN_HEAD = "c2c1041298ae34a593fcb48d04c0e0a20dc9c37a"
N353_HEAD = "0f8cee995e5c982cdb7ceceae14d69f91e65588d"
N354_RESULT = "9f9976bfcf6142e44042ef393b0c5668f4d84a743dfd243ef086eb1a79cee1c4"
N354_HANDOFF = "350afe8c3fbda418a888feff4e8c8233acc44b6472e825cf9d758c22d69065f6"
BC2_15 = "f88ebe53c4300c01fc0a4870cc0dca75a0a091b60c95c8da7e00926bcee43182"
BC2_16_EVIDENCE = "47278e00902f049e354227f02fe891b199025129a8fd3387a0249ad3b5c5ac9c"
BC2_16_CHECKPOINT = "8cfe535fbd486b32e21c9e2cbb7c2289f2880420e5aa4cf3fc98db5f7d310a20"
BC2_16_SYNC = "ddb8841a798ee491fd6322fcb5a25ac7ff64cc33fa1b82d7d5e717e13e3ea4fd"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit(f"FAIL: {msg}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_without(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def checked(path: Path, expected: str, label: str) -> dict:
    obj = load(path)
    req(obj.get("canonical_sha256_without_this_field") == expected, f"{label} canonical field drift")
    req(canonical_without(obj) == expected, f"{label} canonical replay drift")
    return obj


def main() -> None:
    s = load(HERE / "MAIN-STATE.json")
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V4_FULL178_FINAL_CHAIN_SYNC", "state schema drift")
    req(s["bootstrap"]["active_work_pr"] == 1765 and s["bootstrap"]["merge_authorized"] is False, "working surface drift")

    a = s["stage32_main_authority"]
    req(a["authority_pr"] == 1753 and a["authority_head_observed"] == MAIN_HEAD, "MAIN head drift")
    req(a["control_mode"] == MODE and a["primary_incomplete_id"] == "32-01", "MAIN route drift")
    req(a["latest_retained_checkpoint_observed"] == "N354_TWO_SIDED_SCALAR_HURWITZ_AUDIT_GATE", "N354 gate drift")
    req(a["latest_retained_checkpoint_result_canonical_observed"] == N354_RESULT, "N354 result drift")
    req(a["latest_retained_checkpoint_credit_status"] == "N353_AUDITED_CUT_CONSUMED_N354_AUDIT_REQUIRED_NO_MAIN_PRUNING_CREDIT", "audit boundary drift")
    req(a["n353_hostile_audit_status"] == "PASS" and a["n353_hostile_audit_review_id"] == 5163144778, "N353 audit status drift")
    req(a["n353_hostile_audit_exact_head"] == N353_HEAD and a["n353_audit_credit_consumed"] is True, "N353 audit consumption drift")
    req(a["n354_status"] == "AUDIT_REQUIRED" and a["n354_audit_candidate_exact_head"] == "ab0ce28876dbba306985343c104b02b69cec89fb", "N354 audit candidate drift")
    req(a["n354_audit_handoff_canonical_observed"] == N354_HANDOFF, "N354 handoff drift")
    req(a["freshness_freeze_active"] is False and a["freshness_last_hostile_audited_head"] == N353_HEAD, "freshness reset drift")
    req(a["freshness_commits_ahead_observed"] == 9 and a["freshness_commits_behind_observed"] == 0, "freshness distance drift")
    for k in ("V6_is_current_attack_target", "O210_is_current_attack_target", "Q602_is_current_attack_target"):
        req(a[k] is False, f"historical target reactivated: {k}")
    req(a["historical_formal_q602_residues"] == [73,97,235] and a["historical_formal_q602_residues_are_current_survivors"] is False, "Q602 provenance drift")

    cur = s["current"]
    req(cur["status"] == "BC2_16_EXACT_UNSAT_PASS_BC2_17_ACTIVE", "EX5 status drift")
    req(cur["leaf"] == CURRENT_LEAF and cur["next_route"] == CURRENT_LEAF, "BC2-17 route drift")

    iface = s["full178_interface"]
    req(iface["latest_stage32_attack_checkpoint_observed"] == "N354_TWO_SIDED_SCALAR_HURWITZ_AUDIT_GATE", "N354 interface projection drift")
    req(iface["latest_stage32_attack_checkpoint_result_canonical_observed"] == N354_RESULT, "N354 interface canonical drift")
    req(iface["latest_stage32_attack_checkpoint_status"] == "AUDIT_REQUIRED_NO_MAIN_PRUNING_CREDIT", "N354 interface status drift")
    req(iface["n350_registered_producer_count_observed"] == 0, "N350 producer drift")
    req(iface["ex5_retained_exact_unsat_progress_through_rank"] == 797, "EX5 exact prefix drift")
    req(iface["newer_ex5_progress_auto_promoted_to_main"] is False, "EX5 self-promotion drift")

    f = s["frontier"]
    req(f["closed_local_terminal_rank_prefix"] == [0,797], "closed prefix drift")
    req(f["closed_local_terminal_blocks"] == [[0,132],[133,265],[266,398],[399,531],[532,664],[665,797]], "closed blocks drift")
    req(f["whole_g1_d008_e4_stratum_closed"] is False and f["FULL178_complete"] is False, "local result promoted globally")

    c15 = checked(B2 / "bc2-15-next-exceptional-terminal-block-preflight-checkpoint.json", BC2_15, "BC2-15")
    e16 = checked(B2 / "bc2-16-outer-rank5-parent-preflight-evidence.json", BC2_16_EVIDENCE, "BC2-16 evidence")
    c16 = checked(B2 / "bc2-16-outer-rank5-exact-unsat-checkpoint.json", BC2_16_CHECKPOINT, "BC2-16 checkpoint")
    sync = checked(B2 / "bc2-16-claim-sync-receipt.json", BC2_16_SYNC, "BC2-16 claim sync")
    req(c15["next_block"]["outer_exceptional_rank"] == 5, "BC2-15 outer rank drift")
    p = e16["adaptive_exceptional_partition"]
    req(p["fixed_exceptional_mass"] == 4 and p["residual_exceptional_mass"] == 0 and p["parent_branch_count"] == 1, "BC2-16 partition drift")
    pr = e16["parent_result"]
    req(pr["aggregate_result"] == "UNSAT" and pr["exact_unsat_parent_branches"] == 1 and pr["unknown_parent_branches"] == 0, "BC2-16 result drift")
    req(c16["scope"]["local_exact_unsat_prefix"] == [0,797] and c16["next_exact_unit"]["id"] == CURRENT_LEAF, "BC2-16 checkpoint route drift")
    req(sync["result"] == "NO_ACTIVE_FRONTIER_REMAP_NO_MAIN_PROMOTION" and sync["claim_dag"]["main_credit_granted"] is False, "claim sync promotion drift")

    for section in (s["credit"], s["historical_credit_firewall"], s["firewalls"]):
        for key, value in section.items():
            if key != "level":
                req(value is False, f"unauthorized credit/firewall: {key}")

    docs = {
        "README": (HERE / "README.md").read_text(encoding="utf-8"),
        "START": (HERE / "MAIN-START-HERE.md").read_text(encoding="utf-8"),
        "ROADMAP": (HERE / "CURRENT-ROADMAP.md").read_text(encoding="utf-8"),
        "AUDIT": (HERE / "CURRENT-AUDIT-CONTRACT.md").read_text(encoding="utf-8"),
    }
    for name, text in docs.items():
        req(MODE in text and "0..797" in text and "N353" in text and "N354" in text and "N350" in text, f"{name} routing text drift")
        req(N353_HEAD in text and N354_RESULT in text, f"{name} MAIN source lock drift")
    req(CURRENT_LEAF in docs["README"] and CURRENT_LEAF in docs["ROADMAP"], "BC2-17 docs route missing")
    req("not the current Stage32 survivor population" in docs["README"], "Q602 survivor firewall lost")
    req("not current attack targets" in docs["ROADMAP"], "historical targets reactivated")
    req("historical-credit firewall" in docs["AUDIT"], "historical credit wording lost")
    req("historical Cycle1 source-locked roadmap" in docs["ROADMAP"], "historical roadmap protection lost")
    req("historical Cycle1 source-locked contract" in docs["AUDIT"], "historical audit protection lost")

    print("PASS: Stage32EX5 synced to N353 audited / N354 audit gate; BC2-17 routed")
    print("local_exact_unsat_prefix=0..797")
    print("stage32_main=N353_AUDITED_N354_AUDIT_REQUIRED")
    print("freshness=9_AHEAD_0_BEHIND_NO_FREEZE")
    print("stage32_main_credit=NO_FROM_EX5")
    print("merge=SEPARATE_USER_ACTION")


if __name__ == "__main__":
    main()
