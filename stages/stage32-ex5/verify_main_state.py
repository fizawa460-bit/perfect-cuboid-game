#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
B2 = HERE / "breadth-cycle-2"
MAIN_SHA = "6bad01a45b3c57d8697df79c1790bd2f30af68de"
STAGE32_AUTH_HEAD = "b474801454dfc0ac2ee22e7daf9325d83f1fb237"
BC2_24 = "ac6f8afff29a4ac969b1fd32251499f299395261c1aa96a813502cfe2b22472f"
BC2_24_RAW = "8ce9b64586a0431a2695f5761d81f3e6e198e20cae63f3cf76ea6f38c6bbb758"
BC2_23 = "6da1c158da8f8171d446c39b517270c0f7bf524ac62df0cd8f9d099155cdb3a0"
BC2_24_SOURCE_BLOB = "fea28d97abd21c4ee1a8a4604e38785045f4c7f5"


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


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main() -> None:
    s = load(HERE / "MAIN-STATE.json")
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V4_FULL178_FINAL_CHAIN_SYNC", "state schema drift")
    b = s["bootstrap"]
    req(b["active_work_pr"] == 1765, "working PR drift")
    req(b["current_main_sha_observed"] == MAIN_SHA, "main synchronization drift")
    req(b["merge_priority_requested"] is True and b["merge_authorized"] is True, "merge-priority authorization drift")

    a = s["stage32_main_authority"]
    req(a["authority_pr"] == 1753 and a["authority_head_observed"] == STAGE32_AUTH_HEAD, "Stage32 authority drift")
    req(a["authority_merged_main_sha_observed"] == MAIN_SHA, "Stage32 merged-main observation drift")
    req(a["control_mode"] == "FULL178_AND_FINAL_MILESTONE_CHAIN" and a["primary_incomplete_id"] == "32-01", "Stage32 route drift")
    req(a["latest_audited_checkpoint_observed"] == "N355_FULL_KNOWN_PREFIX_BLOCK_SUM", "N355 authority drift")
    req(a["latest_audited_remaining_strata"] == 17128 and a["latest_audited_remaining_terminals"] == 66462870551188628549910, "N355 residual drift")
    req(a["n356_status"] == "AUDIT_REQUIRED_DEFERRED_TO_NEXT_STAGE32_MAIN_PR", "N356 defer drift")
    req(a["n356_audit_credit_consumed"] is False and a["n356_main_pruning_credit"] is False, "N356 credit leak")
    for k in ("V6_is_current_attack_target", "O210_is_current_attack_target", "Q602_is_current_attack_target"):
        req(a[k] is False, f"historical target reactivated: {k}")
    req(a["historical_formal_q602_residues_are_current_survivors"] is False, "historical Q602 survivor drift")

    prior = s["prior_audited_authority"]
    c1 = prior["cycle1"]
    req(c1["breadth_cycle"] == "EX5_BREADTH_CYCLE_1", "Cycle1 breadth-cycle provenance drift")
    req(c1["claim_id"] == "S32.EX5.BOUNDED_EXHAUSTION_CANDIDATE.V2", "Cycle1 claim provenance drift")
    req(c1["authority_status"] == "AUDITED" and c1["scope_firewall"] == "EX5_BREADTH_CYCLE_1_ONLY", "Cycle1 audit provenance drift")
    req(prior["early_bc2"]["claim_id"] == "S32.EX5.BC2_NODE_SUPPORT_SPAN_CHECKPOINT.V1", "early BC2 claim provenance drift")

    cur = s["current"]
    req(cur["status"] == "BC2_24_RETAINED_MERGE_CHECKPOINT_4_NEW_UNSAT_19_RETAINED_UNKNOWN", "BC2-24 merge checkpoint status drift")
    req(cur["breadth_cycle"] == "EX5_BREADTH_CYCLE_2", "breadth-cycle drift")
    req(cur["leaf"] == "BC2_24_EXPLICIT_FIBRE_DEGREE_PARTITION_RETAINED", "BC2-24 leaf drift")
    req(cur["next_route"] == "MERGE_PR_1765_BEFORE_BC2_25", "merge-first route drift")

    f = s["frontier"]
    req(f["closed_local_terminal_rank_prefix"] == [0,797], "historical e4 prefix drift")
    req(f["closed_local_e4_terminal_rank_prefix"] == [0,797], "e4 alias prefix drift")
    req(f["whole_g1_d008_e4_stratum_closed"] is False, "e4 prefix promoted")
    req((f["e8_bc2_24_source_retained_unknown_count"], f["e8_bc2_24_new_parent_unsat_count"], f["e8_bc2_24_retained_unknown_count"]) == (23,4,19), "BC2-24 parent partition drift")
    req((f["e8_bc2_24_branch_unsat_count"], f["e8_bc2_24_branch_unknown_count"], f["e8_bc2_24_branch_sat_count"]) == (147,60,0), "BC2-24 branch partition drift")
    req(f["e8_bc2_24_unretained_unknown_identity_count"] == 172 and f["e8_known_parent_unsat_count_lower_bound"] == 7145, "BC2-24 residual accounting drift")
    req(f["e8_whole_first_block_unsat"] is False and f["FULL178_complete"] is False, "BC2-24 UNKNOWN promoted")

    p = load(B2 / "bc2-24-explicit-fibre-degree-partition-checkpoint.json")
    req(p["canonical_sha256_without_this_field"] == BC2_24, "BC2-24 canonical field drift")
    req(canonical_without(p) == BC2_24, "BC2-24 canonical replay drift")
    req(p["source_locks"]["raw_result_canonical"] == BC2_24_RAW, "BC2-24 raw source lock drift")
    req(p["source_locks"]["bc2_23_checkpoint_canonical"] == BC2_23, "BC2-23 predecessor lock drift")
    r = p["result"]
    req((r["parent_unsat_count"],r["parent_unknown_count"],r["parent_sat_count"]) == (4,19,0), "BC2-24 retained parent result drift")
    req((r["branch_unsat_count"],r["branch_unknown_count"],r["branch_sat_count"]) == (147,60,0), "BC2-24 retained branch result drift")
    req(p["interpretation"]["known_parent_unsat_count_lower_bound"] == 7145, "BC2-24 lower-bound drift")
    req(p["interpretation"]["whole_first_block_unsat_proved"] is False, "BC2-24 whole-block overclaim")
    req(p["credit"]["stage32_main_credit"] is False and p["credit"]["full178_complete"] is False, "BC2-24 credit leak")
    req(p["firewalls"]["unknown_relabelled_unsat"] is False and p["firewalls"]["unretained_172_parent_identities_inferred"] is False, "BC2-24 UNKNOWN firewall drift")

    source = B2 / "bc2_24_explicit_fibre_degree_partition.py"
    req(git_blob_sha(source) == BC2_24_SOURCE_BLOB, "BC2-24 source blob drift")
    key = load(HERE / "runkeys" / "bc2-24-explicit-fibre-degree-partition.json")
    req(key["schema"] == "STAGE32EX5_BC2_24_EXPLICIT_FIBRE_DEGREE_PARTITION_RUNKEY_V1", "BC2-24 runkey schema drift")
    req(key["generation"] == 1 and key["armed"] is True, "retained BC2-24 generation drift")
    req(key["source_git_blob_sha"] == BC2_24_SOURCE_BLOB and key["bc2_23_checkpoint_canonical"] == BC2_23, "BC2-24 runkey lock drift")

    for section_name in ("credit", "historical_credit_firewall", "firewalls"):
        section = s[section_name]
        for key_name, value in section.items():
            if key_name != "level":
                req(value is False, f"unauthorized credit/firewall: {section_name}.{key_name}")
    req(s["full178_interface"]["population_wide_full178_adapter_complete"] is False, "FULL178 adapter overclaim")
    req(s["next_step"]["bc2_25_deferred_until_after_merge"] is True, "BC2-25 must remain deferred")
    req(s["next_step"]["heavy_scaleout_authorized"] is False and s["next_step"]["main_promotion_authorized"] is False, "post-checkpoint authorization leak")

    docs = {
        "README": (HERE / "README.md").read_text(encoding="utf-8"),
        "START": (HERE / "MAIN-START-HERE.md").read_text(encoding="utf-8"),
        "ROADMAP": (HERE / "CURRENT-ROADMAP.md").read_text(encoding="utf-8"),
        "AUDIT": (HERE / "CURRENT-AUDIT-CONTRACT.md").read_text(encoding="utf-8"),
    }
    for name, text in docs.items():
        for token in ("BC2-24", "7145", "19", "172", "0..797", "N355", "N356", "PR #1765"):
            req(token in text, f"{name} missing merge-checkpoint token: {token}")
        req("BC2-25" in text and "merge" in text.lower(), f"{name} merge-first routing missing")

    print("PASS: Stage32EX5 BC2-24 retained merge checkpoint is coherent")
    print("e4_local_exact_unsat_prefix=0..797")
    print("e8_bc2_24=4_NEW_UNSAT_19_RETAINED_UNKNOWN_0_SAT;172_OTHER_IDENTITIES_UNINFERRED")
    print("known_parent_unsat_lower_bound=7145")
    print("stage32_main_credit=NO_FROM_EX5")
    print("next=HOSTILE_REAUDIT_THEN_MERGE_PR_1765_BEFORE_BC2_25")


if __name__ == "__main__":
    main()
