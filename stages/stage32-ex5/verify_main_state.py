#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE_PATH = HERE / "MAIN-STATE.json"
BC2_10_PATH = HERE / "breadth-cycle-2" / "bc2-10-outer-rank2-exact-unsat-checkpoint.json"
BC2_11_PATH = HERE / "breadth-cycle-2" / "bc2-11-next-exceptional-terminal-block-preflight-checkpoint.json"
BC2_12_EVIDENCE_PATH = HERE / "breadth-cycle-2" / "bc2-12-outer-rank3-parent-preflight-evidence.json"
BC2_12_CHECKPOINT_PATH = HERE / "breadth-cycle-2" / "bc2-12-outer-rank3-exact-unsat-checkpoint.json"
BC2_12_CLAIM_SYNC_PATH = HERE / "breadth-cycle-2" / "bc2-12-claim-sync-receipt.json"
BC2_13_PATH = HERE / "breadth-cycle-2" / "bc2-13-next-exceptional-terminal-block-preflight-checkpoint.json"
RECEIPT_PATH = HERE / "ex5-12-hostile-audit-pass-receipt.json"
CERT_PATH = HERE / "ex5-11-terminal-route-decision-certificate.json"

STATE_SCHEMA = "STAGE32EX5_MAIN_COMPACT_STATE_V4_FULL178_FINAL_CHAIN_SYNC"
MODE = "FULL178_AND_FINAL_MILESTONE_CHAIN"
BC2_13_LEAF = "BC2_13_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT"
CURRENT_LEAF = "BC2_14_OUTER_RANK4_SYMBOLIC_X4_PARENT_PREFLIGHT"
CURRENT_MAIN = "5ca6acba4b591d9e2d40057241c850598c1fa1df"
STAGE32_MAIN_HEAD = "1edbb0775d2beac51d98c1327d2fe6b83c012323"
PREDECESSOR_MERGED_MAIN = "bf2890ec0b8168f70db803de876024aa6b6d1f6d"
BC2_10_CANONICAL = "1abeb2bd5299ed217840d028eb99ed961d98238cdec75b5286b05b7f066a752b"
BC2_10_EVIDENCE = "06e4e0e8fbbe1bb64fc757be58f272fec0e85bea1e3bd7a9f21f8bf0dbda1531"
BC2_11_CANONICAL = "b7c3d16f415623dabd6356a2ed94794c96da51de39c7118a7b4ec706b7b81f0d"
BC2_12_EVIDENCE = "d55b84e9b90692c14211e7d1affe73857f0cec2496305121067e2cd71d8da58a"
BC2_12_CHECKPOINT = "2fdb506c601ece59ef107fa62fc4e8948b6ea5145dae413e63ccc2d11691ecd9"
BC2_12_CLAIM_SYNC = "3acaa613dabbaa0caa0fdee9bccf0220cd7b119fb304196d355f0528d648f639"
BC2_13_CANONICAL = "77a0d31f6c5ca4b725c8d4f34ac2a867b82e042768858ff6475d949e1444f9c0"
BC2_13_REPLAY = "c7178bb53882b5e4c88309bf26ff149e993f07d4c610aec98c50f7a9a84005d5"
N350_CANONICAL = "7d64040945f258048f9d61b0f888ca8d3720bedee6eab8902c7233ffc059d25a"
PREDECESSOR_AUDITED_HEAD = "a5e59bab3f7fe5a31e356c5a78edcbd741b093a6"
PREDECESSOR_AUDIT_REVIEW = 5161068590
CYCLE1_HEAD = "79c601b636857eaaaa97ad4c22e682e681341bad"
CYCLE1_REVIEW = 5141459384
CYCLE1_CLAIM = "S32.EX5.BOUNDED_EXHAUSTION_CANDIDATE.V2"
CYCLE1_CORE = "6e9093c4fc25455a8c08b9cdb80fc73d127d3759c0b1edfab25b259dcec210a3"
CYCLE1_CERT = "b0d0a81cf79448703d5e10d9280e6e19ac5f4f32dc31061c9c836d323bcebba7"


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_without_field(obj: dict, field: str = "canonical_sha256_without_this_field") -> str:
    cp = dict(obj)
    cp.pop(field, None)
    raw = json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def verify_current_docs() -> None:
    docs = {
        "README": (HERE / "README.md").read_text(encoding="utf-8"),
        "START": (HERE / "MAIN-START-HERE.md").read_text(encoding="utf-8"),
        "ROADMAP": (HERE / "CURRENT-ROADMAP.md").read_text(encoding="utf-8"),
        "AUDIT": (HERE / "CURRENT-AUDIT-CONTRACT.md").read_text(encoding="utf-8"),
    }
    for name, text in docs.items():
        req(MODE in text, f"{name} lost current Stage32 mode")
        req("32-01" in text and "FULL178" in text, f"{name} lost primary FULL178 routing")
        req("0..531" in text, f"{name} lost retained exact prefix")
        req("532..664" in text, f"{name} lost BC2-13 structural block")
        req("N350" in text, f"{name} lost current N350 boundary")
    req("not the current Stage32 survivor population" in docs["README"], "README Q602 provenance wording drift")
    req("not current attack targets" in docs["ROADMAP"], "current roadmap restored V6/O210/Q602 as targets")
    req("historical-credit firewall" in docs["AUDIT"], "current audit historical-credit firewall missing")
    req(CURRENT_LEAF in docs["README"] and CURRENT_LEAF in docs["ROADMAP"], "BC2-14 current next step missing")
    req("historical Cycle1 source-locked roadmap" in docs["ROADMAP"], "current roadmap does not protect historical roadmap")
    req("historical Cycle1 source-locked contract" in docs["AUDIT"], "current audit does not protect historical audit contract")


def main() -> None:
    state = load(STATE_PATH)
    req(state["schema"] == STATE_SCHEMA and state["stage"] == "32EX5", "state identity drift")
    req(state["execution"]["roadmap_contract"] == "stages/stage32-ex5/CURRENT-ROADMAP.md", "mutable roadmap routing drift")
    req(state["execution"]["historical_source_locked_roadmap"] == "stages/stage32-ex5/stage32-ex5.md", "historical roadmap routing drift")
    req(state["execution"]["audit_contract"] == "stages/stage32-ex5/CURRENT-AUDIT-CONTRACT.md", "mutable audit routing drift")
    req(state["execution"]["historical_source_locked_audit_contract"] == "stages/stage32-ex5/AUDIT-CONTRACT.md", "historical audit routing drift")

    boot = state["bootstrap"]
    req(boot["current_main_sha_observed"] == CURRENT_MAIN, "observed main drift")
    req(boot["active_work_pr"] == 1765 and boot["work_branch"] == "impl/stage32ex5-bc2-12-outer-rank3", "active EX5 surface drift")
    req(boot["merge_authorized"] is False, "merge authorization drift")

    auth = state["stage32_main_authority"]
    req(auth["authority_pr"] == 1753 and auth["authority_head_observed"] == STAGE32_MAIN_HEAD, "Stage32 MAIN authority drift")
    req(auth["control_mode"] == MODE, "Stage32 mode regression")
    req(auth["primary_incomplete_id"] == "32-01" and auth["primary_incomplete_name"] == "FULL178", "primary incomplete regression")
    req(auth["current_stop_gate_observed"] == "N350_HOSTILE_AUDIT_THEN_REGISTER_EXACT_PRODUCER_ADAPTER", "Stage32 current stop gate drift")
    for key in ("V6_is_current_attack_target", "O210_is_current_attack_target", "Q602_is_current_attack_target"):
        req(auth[key] is False, f"historical target reactivated: {key}")
    req(auth["historical_formal_q602_residues"] == [73, 97, 235], "historical Q602 triple lost")
    req(auth["historical_formal_q602_residues_are_current_survivors"] is False, "historical Q602 triple promoted")

    prov = state["historical_formal_provenance"]
    req(prov["q602_residue_triple"] == [73, 97, 235], "Q602 provenance drift")
    req(prov["q602_residue_triple_semantics"] == "HISTORICAL_FORMAL_PROVENANCE_NOT_CURRENT_SURVIVOR_POPULATION", "Q602 semantics drift")
    req(prov["v6_o210_q602_current_research_status"] == "NOT_CURRENT_TARGETS", "historical line became current")
    req(prov["old_no_q602_o210_credit_semantics"] == "HISTORICAL_CREDIT_FIREWALL", "historical-credit semantics drift")

    pred = state["prior_audited_authority"]["predecessor_pr_1742"]
    req(pred["exact_head"] == PREDECESSOR_AUDITED_HEAD and pred["review_id"] == PREDECESSOR_AUDIT_REVIEW, "predecessor audit anchor drift")
    req(pred["merged_main_sha"] == PREDECESSOR_MERGED_MAIN and pred["continuation_released"] is True, "predecessor release drift")
    p1762 = state["prior_audited_authority"]["bc2_11_pr_1762"]
    req(p1762["authority_status"] == "HOSTILE_AUDIT_PASS_AND_MERGED", "BC2-11 audit/merge authority lost")
    req(p1762["exact_head"] == "0e768adddfb57a4828fd0ca0a1494f96f7a1c8b1", "BC2-11 audited head drift")

    current = state["current"]
    req(current["status"] == "BC2_13_STRUCTURAL_PREFLIGHT_PASS_BC2_14_ACTIVE", "current status drift")
    req(current["leaf"] == CURRENT_LEAF and current["next_route"] == CURRENT_LEAF, "BC2-14 routing drift")
    req(current["route_family"] == "FULL178_PICARD64_NODE_SUPPORT_OBSTRUCTION_INTERFACE", "current EX5 role drift")
    req(current["blocker"] == "OUTER_RANK4_SYMBOLIC_X4_PICARD64_PARENT_NOT_YET_EXACTLY_CLASSIFIED", "current blocker drift")

    iface = state["full178_interface"]
    req(iface["stage32_consumption_node"] == "stages/stage32/32-01-178/nodes/N150/STATE.json", "legacy N150 compatibility alias drift")
    req(iface["current_stage32_production_leaf_gate"] == "stages/stage32/32-01-178/nodes/N350/PRODUCTION_LEAF_CERTIFICATE_CONTRACT.json", "N350 boundary drift")
    req(iface["current_stage32_production_leaf_gate_status_observed"] == "PENDING_HOSTILE_AUDIT_EMPTY_PRODUCER_REGISTRY", "N350 observed state drift")
    req(iface["n350_contract_canonical_observed"] == N350_CANONICAL and iface["n350_registered_producer_count_observed"] == 0, "N350 contract/registry drift")
    req(iface["ex5_retained_exact_unsat_progress_through_rank"] == 531, "EX5 exact prefix drift")
    req(iface["ex5_structural_replay_progress_through_rank"] == 664, "EX5 structural prefix drift")
    req(iface["newer_ex5_progress_auto_promoted_to_main"] is False, "EX5 auto-promoted to MAIN")
    req(iface["n350_producer_registration_available_to_ex5_now"] is False, "EX5 prematurely registered into N350")
    req(iface["population_wide_full178_adapter_complete"] is False, "population-wide adapter falsely complete")
    req(iface["effectivity_or_actual_curve_existence_proved_by_interface"] is False, "interface widened to existence/effectivity")

    frontier = state["frontier"]
    req(frontier["closed_local_terminal_blocks"] == [[0, 132], [133, 265], [266, 398], [399, 531]], "local block list drift")
    req(frontier["closed_local_terminal_rank_prefix"] == [0, 531], "local exact prefix drift")
    req(frontier["next_structural_block_exactly_rederived"] is True, "BC2-13 structural block lost")
    req(frontier["structural_replay_rank_prefix"] == [0, 664], "BC2-13 structural prefix drift")
    req(frontier["whole_g1_d008_e4_stratum_closed"] is False, "local progress promoted to stratum")
    req(frontier["FULL178_complete"] is False, "local progress promoted to FULL178")
    req(frontier["population_wide_main_consumable_result_complete"] is False, "MAIN-consumable result falsely complete")

    retained = state["retained_exact_progress"]
    req(retained["bc2_10_rank_266_398_checkpoint_canonical"] == BC2_10_CANONICAL, "BC2-10 provenance drift")
    req(retained["bc2_10_evidence_canonical"] == BC2_10_EVIDENCE, "BC2-10 evidence provenance drift")
    req(retained["bc2_11_rank_399_531_structural_checkpoint_canonical"] == BC2_11_CANONICAL, "BC2-11 provenance drift")
    req(retained["bc2_12_rank_399_531_evidence_canonical"] == BC2_12_EVIDENCE, "BC2-12 evidence provenance drift")
    req(retained["bc2_12_rank_399_531_checkpoint_canonical"] == BC2_12_CHECKPOINT, "BC2-12 checkpoint provenance drift")
    req(retained["bc2_12_parent_partition"] == "20_OF_20_EXACT_UNSAT_UNKNOWN_0_SAT_0", "BC2-12 parent result drift")
    req(retained["bc2_13_rank_532_664_structural_checkpoint_canonical"] == BC2_13_CANONICAL, "BC2-13 checkpoint provenance drift")
    req(retained["bc2_13_rank_532_664_replay_stream_sha256"] == BC2_13_REPLAY, "BC2-13 replay provenance drift")
    req(retained["exact_evidence_rewritten_by_semantic_sync"] is False, "semantic sync claims evidence rewrite")

    bc2_10 = load(BC2_10_PATH)
    req(bc2_10["canonical_sha256_without_this_field"] == BC2_10_CANONICAL, "BC2-10 canonical field drift")
    req(canonical_without_field(bc2_10) == BC2_10_CANONICAL, "BC2-10 canonical replay drift")
    req(bc2_10["exact_result"]["aggregate_result"] == "UNSAT", "BC2-10 result drift")
    req(bc2_10["exact_result"]["evidence_canonical_sha256"] == BC2_10_EVIDENCE, "BC2-10 evidence lock drift")

    bc2_11 = load(BC2_11_PATH)
    req(bc2_11["canonical_sha256_without_this_field"] == BC2_11_CANONICAL and canonical_without_field(bc2_11) == BC2_11_CANONICAL, "BC2-11 canonical drift")
    nxt11 = bc2_11["next_block"]
    req([nxt11["terminal_rank_start"], nxt11["terminal_rank_end"]] == [399, 531], "BC2-11 rank block drift")
    req(nxt11["outer_exceptional_rank"] == 3 and nxt11["block_width"] == 133, "BC2-11 outer-rank/block-width drift")
    req(nxt11["all_133_rank_unrank_replays_exact"] is True and nxt11["all_133_terminal_predicate_replays_exact"] is True, "BC2-11 exact replay authority lost")

    evidence = load(BC2_12_EVIDENCE_PATH)
    checkpoint = load(BC2_12_CHECKPOINT_PATH)
    req(evidence["canonical_sha256_without_this_field"] == BC2_12_EVIDENCE and canonical_without_field(evidence) == BC2_12_EVIDENCE, "BC2-12 evidence canonical drift")
    req(checkpoint["canonical_sha256_without_this_field"] == BC2_12_CHECKPOINT and canonical_without_field(checkpoint) == BC2_12_CHECKPOINT, "BC2-12 checkpoint canonical drift")
    req(evidence["target"]["terminal_rank_block"] == [399, 531], "BC2-12 target block drift")
    req(evidence["adaptive_exceptional_partition"]["fixed_exceptional_mass"] == 3, "BC2-12 fixed exceptional mass drift")
    req(evidence["adaptive_exceptional_partition"]["residual_exceptional_mass"] == 1, "BC2-12 residual exceptional mass drift")
    req(evidence["parent_result"]["tested_parent_branches"] == 20, "BC2-12 parent count drift")
    req(evidence["parent_result"]["exact_unsat_parent_branches"] == 20, "BC2-12 parent UNSAT count drift")
    req(evidence["parent_result"]["unknown_parent_branches"] == 0 and evidence["parent_result"]["sat_parent"] is None, "BC2-12 non-UNSAT parent appeared")
    req(checkpoint["scope"]["local_exact_unsat_prefix"] == [0, 531], "BC2-12 exact prefix checkpoint drift")
    req(checkpoint["next_exact_unit"]["id"] == BC2_13_LEAF, "BC2-12 next-unit drift")

    bc2_13 = load(BC2_13_PATH)
    req(bc2_13["canonical_sha256_without_this_field"] == BC2_13_CANONICAL and canonical_without_field(bc2_13) == BC2_13_CANONICAL, "BC2-13 canonical drift")
    nxt13 = bc2_13["next_block"]
    req([nxt13["terminal_rank_start"], nxt13["terminal_rank_end"]] == [532, 664], "BC2-13 rank block drift")
    req(nxt13["outer_exceptional_rank"] == 4 and nxt13["block_width"] == 133, "BC2-13 outer-rank/block-width drift")
    req(nxt13["base_terminal_x4_zero"] == [0,1,0,0,0,0,1,1,0,0,1], "BC2-13 base terminal drift")
    req(nxt13["exceptional_signature"] == [0,1,0,0,0,1,1,0,0,1], "BC2-13 exceptional signature drift")
    req(nxt13["all_133_rank_unrank_replays_exact"] is True and nxt13["all_133_terminal_predicate_replays_exact"] is True, "BC2-13 exact structural replay lost")
    req(nxt13["replay_stream_sha256"] == BC2_13_REPLAY, "BC2-13 replay stream drift")
    req(bc2_13["execution"]["solver_invoked"] is False and bc2_13["execution"]["heavy_compute_invoked"] is False, "BC2-13 widened to solver/heavy execution")
    req(bc2_13["firewalls"]["next_block_picard64_closed"] is False, "BC2-13 structural replay promoted to Picard64 closure")
    req(bc2_13["next_exact_unit"]["id"] == CURRENT_LEAF, "BC2-13 next-unit drift")

    sync = load(BC2_12_CLAIM_SYNC_PATH)
    req(sync["canonical_sha256_without_this_field"] == BC2_12_CLAIM_SYNC and canonical_without_field(sync) == BC2_12_CLAIM_SYNC, "BC2-12 claim-sync receipt drift")
    req(sync["trigger"] == "RETAINED_CONSOLIDATION", "claim-sync trigger drift")
    req(sync["claim_dag"]["existing_active_goal"] == "S32.FULL178.NUMERICAL_CENSUS.V1", "claim-sync active goal drift")
    req(sync["claim_dag"]["lane_role"] == "ATTACKS", "claim-sync lane role drift")
    req(sync["claim_dag"]["active_frontier_materially_changed"] is False, "unexpected active-frontier remap")
    req(sync["claim_dag"]["main_credit_granted"] is False, "claim-sync self-promoted to MAIN")
    req(state["claim_sync"]["receipt_canonical"] == BC2_12_CLAIM_SYNC, "state claim-sync receipt drift")

    for key, value in state["credit"].items():
        if key != "level":
            req(value is False, f"unauthorized current credit: {key}")
    for key, value in state["historical_credit_firewall"].items():
        req(value is False, f"historical-credit firewall violated: {key}")
    for key, value in state["firewalls"].items():
        req(value is False, f"current firewall violated: {key}")

    boundary = state["intermediate_audit_boundary"]
    req(boundary["audited_exact_head"] == PREDECESSOR_AUDITED_HEAD, "intermediate audit head drift")
    req(boundary["audit_review_id"] == PREDECESSOR_AUDIT_REVIEW and boundary["audit_result"] == "PASS", "intermediate audit PASS drift")
    req(boundary["freeze_released"] is True, "intermediate audit freeze not released")

    step = state["next_step"]
    req(step["id"] == CURRENT_LEAF, "next-step drift")
    req(step["heavy_scaleout_authorized"] is False, "heavy scaleout silently authorized")
    req(step["main_promotion_authorized"] is False, "MAIN promotion silently authorized")
    req(step["n350_registration_authorized"] is False, "N350 registration silently authorized")

    receipt = load(RECEIPT_PATH)
    cert = load(CERT_PATH)
    req(receipt["candidate_pr"] == 1710 and receipt["candidate_exact_head"] == CYCLE1_HEAD, "Cycle1 receipt target drift")
    req(receipt["audit_review_id"] == CYCLE1_REVIEW and receipt["audit_result"] == "PASS", "Cycle1 receipt PASS drift")
    req(receipt["claim_id"] == CYCLE1_CLAIM and receipt["claim_core_sha256"] == CYCLE1_CORE, "Cycle1 claim identity drift")
    req(cert["canonical_sha256_without_this_field"] == CYCLE1_CERT and canonical_without_field(cert) == CYCLE1_CERT, "Cycle1 certificate canonical drift")

    verify_current_docs()
    print("PASS: Stage32EX5 BC2-13 structural replay retained; BC2-14 routed")
    print(f"stage32_mode={MODE}")
    print("primary_incomplete=32-01:FULL178")
    print("historical_q602_residues=[73,97,235]:PROVENANCE_ONLY")
    print("local_exact_unsat_prefix=0..531")
    print("structural_replay_progress=0..664")
    print("bc2_13_picard64_credit=NO")
    print(f"next_leaf={CURRENT_LEAF}")
    print("claim_sync=NO_ACTIVE_FRONTIER_REMAP")
    print("n350_registration=NO:PENDING_MAIN_HOSTILE_AUDIT")
    print("stage32_main_credit=NO")
    print("merge=SEPARATE_USER_ACTION")


if __name__ == "__main__":
    main()
