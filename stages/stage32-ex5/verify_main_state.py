#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
B2 = HERE / "breadth-cycle-2"
STATE_PATH = HERE / "MAIN-STATE.json"
MODE = "FULL178_AND_FINAL_MILESTONE_CHAIN"
CURRENT_LEAF = "BC2_17_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT"
STAGE32_MAIN_HEAD = "0f8cee995e5c982cdb7ceceae14d69f91e65588d"
N353_CANONICAL = "afd873201ed0deea149c502d681729508face43942df085af91db3e95fbf371b"
BC2_12_EVIDENCE = "d55b84e9b90692c14211e7d1affe73857f0cec2496305121067e2cd71d8da58a"
BC2_12_CHECKPOINT = "2fdb506c601ece59ef107fa62fc4e8948b6ea5145dae413e63ccc2d11691ecd9"
BC2_14_EVIDENCE = "52fb48627a8646db2dc5b3e0b04eb32bc89ca9391988f4b91f7f51afada2de5d"
BC2_14_CHECKPOINT = "fa603024cbf3b89fb097401f4e5e9b3f0cad04a0a0b6dd0b919b3a37b2781c0e"
BC2_15_CHECKPOINT = "f88ebe53c4300c01fc0a4870cc0dca75a0a091b60c95c8da7e00926bcee43182"
BC2_15_REPLAY = "6655d249aa6d51cea8fe9bd7108c315c523b5ee1725d36dd1a1a537e11d4724f"
BC2_16_EVIDENCE = "47278e00902f049e354227f02fe891b199025129a8fd3387a0249ad3b5c5ac9c"
BC2_16_CHECKPOINT = "8cfe535fbd486b32e21c9e2cbb7c2289f2880420e5aa4cf3fc98db5f7d310a20"
BC2_16_CLAIM_SYNC = "ddb8841a798ee491fd6322fcb5a25ac7ff64cc33fa1b82d7d5e717e13e3ea4fd"


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_without(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def verify_canonical(path: Path, expected: str, label: str) -> dict:
    obj = load(path)
    req(obj.get("canonical_sha256_without_this_field") == expected, f"{label} canonical field drift")
    req(canonical_without(obj) == expected, f"{label} canonical replay drift")
    return obj


def verify_docs() -> None:
    docs = {
        "README": (HERE / "README.md").read_text(encoding="utf-8"),
        "START": (HERE / "MAIN-START-HERE.md").read_text(encoding="utf-8"),
        "ROADMAP": (HERE / "CURRENT-ROADMAP.md").read_text(encoding="utf-8"),
        "AUDIT": (HERE / "CURRENT-AUDIT-CONTRACT.md").read_text(encoding="utf-8"),
    }
    for name, text in docs.items():
        req(MODE in text and "32-01" in text and "FULL178" in text, f"{name} lost Stage32 mode/primary target")
        req("0..797" in text, f"{name} lost BC2-16 exact prefix")
        req("N353" in text, f"{name} lost current MAIN checkpoint")
        req("N350" in text, f"{name} lost production boundary")
    req(CURRENT_LEAF in docs["README"] and CURRENT_LEAF in docs["ROADMAP"], "BC2-17 route missing")
    req("not the current Stage32 survivor population" in docs["README"], "README historical Q602 firewall lost")
    req("not current attack targets" in docs["ROADMAP"], "roadmap reactivated V6/O210/Q602")
    req("historical-credit firewall" in docs["AUDIT"], "audit historical-credit firewall missing")
    req("historical Cycle1 source-locked roadmap" in docs["ROADMAP"], "historical roadmap protection missing")
    req("historical Cycle1 source-locked contract" in docs["AUDIT"], "historical audit protection missing")


def main() -> None:
    s = load(STATE_PATH)
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V4_FULL178_FINAL_CHAIN_SYNC", "state schema drift")
    req(s["stage"] == "32EX5", "stage identity drift")
    req(s["bootstrap"]["active_work_pr"] == 1765 and s["bootstrap"]["merge_authorized"] is False, "working PR/merge firewall drift")

    a = s["stage32_main_authority"]
    req(a["authority_pr"] == 1753 and a["authority_head_observed"] == STAGE32_MAIN_HEAD, "Stage32 MAIN head drift")
    req(a["control_mode"] == MODE and a["primary_incomplete_id"] == "32-01" and a["primary_incomplete_name"] == "FULL178", "Stage32 routing drift")
    req(a["latest_retained_checkpoint_observed"] == "N353_UNIFORM_FULL178_SCALAR_HURWITZ_CENSUS", "N353 routing drift")
    req(a["latest_retained_checkpoint_result_canonical_observed"] == N353_CANONICAL, "N353 canonical drift")
    req(a["latest_retained_checkpoint_credit_status"] == "AUDIT_CANDIDATE_ONLY_NO_MAIN_PRUNING_CREDIT", "N353 credit ceiling drift")
    req(a["freshness_freeze_active"] is True, "MAIN freshness freeze lost")
    req(a["freshness_last_hostile_audited_head"] == "b56a832e6c194321916fe4ef63eef0d673b8ff9a", "MAIN hostile-audit anchor drift")
    req(a["freshness_commits_ahead_observed"] == 98 and a["freshness_commits_behind_observed"] == 0, "MAIN freshness distance drift")
    req(a["freshness_intermediate_reaudit_threshold"] == 90 and a["freshness_hard_halt_threshold"] == 100, "freshness thresholds drift")
    for key in ("V6_is_current_attack_target", "O210_is_current_attack_target", "Q602_is_current_attack_target"):
        req(a[key] is False, f"historical target reactivated: {key}")
    req(a["historical_formal_q602_residues"] == [73,97,235] and a["historical_formal_q602_residues_are_current_survivors"] is False, "Q602 provenance drift")

    cur = s["current"]
    req(cur["status"] == "BC2_16_EXACT_UNSAT_PASS_BC2_17_ACTIVE", "current status drift")
    req(cur["leaf"] == CURRENT_LEAF and cur["next_route"] == CURRENT_LEAF, "BC2-17 routing drift")
    req(cur["blocker"] == "NEXT_EXCEPTIONAL_OUTER_BLOCK_NOT_YET_STRUCTURALLY_REDERIVED", "BC2-17 blocker drift")

    iface = s["full178_interface"]
    req(iface["stage32_consumption_node"] == "stages/stage32/32-01-178/nodes/N150/STATE.json", "legacy N150 compatibility alias drift")
    req(iface["production_registration_boundary"] == "stages/stage32/32-01-178/nodes/N350/PRODUCTION_LEAF_CERTIFICATE_CONTRACT.json", "N350 boundary drift")
    req(iface["n350_registered_producer_count_observed"] == 0, "N350 producer registry drift")
    req(iface["latest_stage32_attack_checkpoint_observed"] == "N353_UNIFORM_FULL178_SCALAR_HURWITZ_CENSUS", "MAIN attack checkpoint projection drift")
    req(iface["ex5_retained_exact_unsat_progress_through_rank"] == 797, "EX5 exact prefix drift")
    req(iface["ex5_structural_replay_progress_through_rank"] == 797, "EX5 structural prefix drift")
    req(iface["newer_ex5_progress_auto_promoted_to_main"] is False and iface["n350_producer_registration_available_to_ex5_now"] is False, "EX5 promotion firewall drift")
    req(iface["population_wide_full178_adapter_complete"] is False and iface["effectivity_or_actual_curve_existence_proved_by_interface"] is False, "EX5 interface scope widened")

    f = s["frontier"]
    req(f["closed_local_terminal_blocks"] == [[0,132],[133,265],[266,398],[399,531],[532,664],[665,797]], "closed block list drift")
    req(f["closed_local_terminal_rank_prefix"] == [0,797], "exact prefix drift")
    req(f["structural_replay_rank_prefix"] == [0,797] and f["next_structural_block_exactly_rederived"] is False, "structural frontier drift")
    req(f["whole_g1_d008_e4_stratum_closed"] is False and f["FULL178_complete"] is False, "local block promoted to global closure")
    req(f["population_wide_main_consumable_result_complete"] is False, "MAIN-consumable result falsely complete")

    r = s["retained_exact_progress"]
    req(r["bc2_12_rank_399_531_evidence_canonical"] == BC2_12_EVIDENCE and r["bc2_12_rank_399_531_checkpoint_canonical"] == BC2_12_CHECKPOINT, "BC2-12 provenance drift")
    req(r["bc2_14_rank_532_664_evidence_canonical"] == BC2_14_EVIDENCE and r["bc2_14_rank_532_664_checkpoint_canonical"] == BC2_14_CHECKPOINT, "BC2-14 provenance drift")
    req(r["bc2_15_rank_665_797_structural_checkpoint_canonical"] == BC2_15_CHECKPOINT and r["bc2_15_rank_665_797_replay_stream_sha256"] == BC2_15_REPLAY, "BC2-15 provenance drift")
    req(r["bc2_16_rank_665_797_evidence_canonical"] == BC2_16_EVIDENCE and r["bc2_16_rank_665_797_checkpoint_canonical"] == BC2_16_CHECKPOINT, "BC2-16 provenance drift")
    req(r["bc2_16_parent_partition"] == "1_OF_1_EXACT_UNSAT_UNKNOWN_0_SAT_0", "BC2-16 parent result drift")
    req(r["exact_evidence_rewritten_by_semantic_sync"] is False, "semantic sync rewrote exact evidence")

    c15 = verify_canonical(B2 / "bc2-15-next-exceptional-terminal-block-preflight-checkpoint.json", BC2_15_CHECKPOINT, "BC2-15 checkpoint")
    req(c15["next_block"]["outer_exceptional_rank"] == 5 and c15["next_block"]["replay_stream_sha256"] == BC2_15_REPLAY, "BC2-15 structural replay drift")
    req(c15["execution"]["solver_invoked"] is False and c15["execution"]["heavy_compute_invoked"] is False, "BC2-15 solver credit drift")

    e16 = verify_canonical(B2 / "bc2-16-outer-rank5-parent-preflight-evidence.json", BC2_16_EVIDENCE, "BC2-16 evidence")
    c16 = verify_canonical(B2 / "bc2-16-outer-rank5-exact-unsat-checkpoint.json", BC2_16_CHECKPOINT, "BC2-16 checkpoint")
    sync = verify_canonical(B2 / "bc2-16-claim-sync-receipt.json", BC2_16_CLAIM_SYNC, "BC2-16 claim sync")
    p = e16["adaptive_exceptional_partition"]
    req(p["fixed_exceptional_mass"] == 4 and p["residual_exceptional_mass"] == 0, "BC2-16 mass split drift")
    req(p["mass_split_derived_from_bc2_15_terminal_and_locked_labels"] is True and p["parent_branch_count"] == 1, "BC2-16 partition provenance drift")
    pr = e16["parent_result"]
    req(pr["aggregate_result"] == "UNSAT" and pr["tested_parent_branches"] == 1 and pr["exact_unsat_parent_branches"] == 1, "BC2-16 exact result drift")
    req(pr["unknown_parent_branches"] == 0 and pr["sat_parent"] is None, "BC2-16 non-UNSAT parent appeared")
    req(c16["scope"]["local_exact_unsat_prefix"] == [0,797] and c16["next_exact_unit"]["id"] == CURRENT_LEAF, "BC2-16 checkpoint routing drift")
    req(c16["workflow"]["run_id"] == 34441599406 and c16["workflow"]["compute_job_id"] == 102757639746, "BC2-16 workflow provenance drift")
    req(sync["trigger"] == "RETAINED_CONSOLIDATION" and sync["result"] == "NO_ACTIVE_FRONTIER_REMAP_NO_MAIN_PROMOTION", "BC2-16 claim-sync result drift")
    req(sync["claim_dag"]["existing_active_goal"] == "S32.FULL178.NUMERICAL_CENSUS.V1" and sync["claim_dag"]["lane_role"] == "ATTACKS", "BC2-16 claim routing drift")
    req(sync["claim_dag"]["active_frontier_materially_changed"] is False and sync["claim_dag"]["claim_registry_core_changed"] is False and sync["claim_dag"]["main_credit_granted"] is False, "BC2-16 claim-sync promoted credit")
    req(s["claim_sync"]["receipt_canonical"] == BC2_16_CLAIM_SYNC, "state claim-sync receipt drift")

    for key, value in s["credit"].items():
        if key != "level":
            req(value is False, f"unauthorized credit: {key}")
    for key, value in s["historical_credit_firewall"].items():
        req(value is False, f"historical-credit firewall violated: {key}")
    for key, value in s["firewalls"].items():
        req(value is False, f"current firewall violated: {key}")
    req(s["next_step"]["id"] == CURRENT_LEAF and s["next_step"]["heavy_scaleout_authorized"] is False and s["next_step"]["main_promotion_authorized"] is False, "next-step authorization drift")

    verify_docs()
    print("PASS: Stage32EX5 BC2-16 exact UNSAT retained; BC2-17 routed")
    print("local_exact_unsat_prefix=0..797")
    print("bc2_16_parent_partition=1/1:UNSAT")
    print("stage32_main_checkpoint=N353:AUDIT_CANDIDATE:FRESHNESS_FREEZE")
    print("claim_sync=NO_ACTIVE_FRONTIER_REMAP")
    print("stage32_main_credit=NO")
    print("merge=SEPARATE_USER_ACTION")


if __name__ == "__main__":
    main()
