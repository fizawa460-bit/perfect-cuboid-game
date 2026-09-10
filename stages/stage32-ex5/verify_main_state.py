#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE_PATH = HERE / "MAIN-STATE.json"
BC2_10_PATH = HERE / "breadth-cycle-2" / "bc2-10-outer-rank2-exact-unsat-checkpoint.json"
BC2_11_PATH = HERE / "breadth-cycle-2" / "bc2-11-next-exceptional-terminal-block-preflight-checkpoint.json"
RECEIPT_PATH = HERE / "ex5-12-hostile-audit-pass-receipt.json"
CERT_PATH = HERE / "ex5-11-terminal-route-decision-certificate.json"

STATE_SCHEMA = "STAGE32EX5_MAIN_COMPACT_STATE_V4_FULL178_FINAL_CHAIN_SYNC"
MODE = "FULL178_AND_FINAL_MILESTONE_CHAIN"
CURRENT_LEAF = "BC2_12_OUTER_RANK3_SYMBOLIC_X4_PARENT_PREFLIGHT"
CURRENT_MAIN = "bf2890ec0b8168f70db803de876024aa6b6d1f6d"
STAGE32_MAIN_HEAD = "a2cacaeb9b61eca34399952a7daaf5288ff3b826"
BC2_10_CANONICAL = "1abeb2bd5299ed217840d028eb99ed961d98238cdec75b5286b05b7f066a752b"
BC2_10_EVIDENCE = "06e4e0e8fbbe1bb64fc757be58f272fec0e85bea1e3bd7a9f21f8bf0dbda1531"
BC2_11_CANONICAL = "b7c3d16f415623dabd6356a2ed94794c96da51de39c7118a7b4ec706b7b81f0d"
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


def canonical_without_field(obj: dict, field: str) -> str:
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
    req("not the current Stage32 survivor population" in docs["README"], "README Q602 provenance wording drift")
    req("not current attack targets" in docs["ROADMAP"], "current roadmap restored V6/O210/Q602 as targets")
    req("historical-credit firewall" in docs["AUDIT"], "current audit historical-credit firewall missing")
    req(CURRENT_LEAF in docs["README"] and CURRENT_LEAF in docs["ROADMAP"], "current next step missing")
    req("N350" in docs["README"] and "N350" in docs["ROADMAP"] and "N350" in docs["AUDIT"], "current N350 boundary missing")
    req("historical Cycle1 source-locked roadmap" in docs["ROADMAP"], "current roadmap does not protect historical roadmap")
    req("historical Cycle1 source-locked contract" in docs["AUDIT"], "current audit does not protect historical audit contract")


def main() -> None:
    state = load(STATE_PATH)
    req(state["schema"] == STATE_SCHEMA, "state schema drift")
    req(state["stage"] == "32EX5", "wrong stage")
    req(state["execution"]["roadmap_contract"] == "stages/stage32-ex5/CURRENT-ROADMAP.md", "mutable roadmap routing drift")
    req(state["execution"]["historical_source_locked_roadmap"] == "stages/stage32-ex5/stage32-ex5.md", "historical roadmap routing drift")
    req(state["execution"]["audit_contract"] == "stages/stage32-ex5/CURRENT-AUDIT-CONTRACT.md", "mutable audit routing drift")
    req(state["execution"]["historical_source_locked_audit_contract"] == "stages/stage32-ex5/AUDIT-CONTRACT.md", "historical audit routing drift")

    boot = state["bootstrap"]
    req(boot["current_main_sha_observed"] == CURRENT_MAIN, "observed main drift")
    req(boot["active_work_pr"] == 1762 and boot["work_branch"] == "impl/stage32ex5-bc2-11-continuation", "active EX5 surface drift")
    req(boot["merge_authorized"] is False, "merge authorization drift")

    auth = state["stage32_main_authority"]
    req(auth["authority_pr"] == 1753, "Stage32 MAIN PR drift")
    req(auth["authority_head_observed"] == STAGE32_MAIN_HEAD, "Stage32 MAIN observed head drift")
    req(auth["control_mode"] == MODE, "Stage32 mode regression")
    req(auth["primary_incomplete_id"] == "32-01" and auth["primary_incomplete_name"] == "FULL178", "primary incomplete regression")
    req(auth["current_stop_gate_observed"] == "N350_HOSTILE_AUDIT_THEN_REGISTER_EXACT_PRODUCER_ADAPTER", "Stage32 current stop gate drift")
    for key in ("V6_is_current_attack_target", "O210_is_current_attack_target", "Q602_is_current_attack_target"):
        req(auth[key] is False, f"historical target reactivated: {key}")
    req(auth["historical_formal_q602_residues"] == [73, 97, 235], "historical Q602 triple lost")
    req(auth["historical_formal_q602_residues_are_current_survivors"] is False, "historical Q602 triple promoted to current survivors")

    prov = state["historical_formal_provenance"]
    req(prov["q602_residue_triple"] == [73, 97, 235], "Q602 provenance drift")
    req(prov["q602_residue_triple_semantics"] == "HISTORICAL_FORMAL_PROVENANCE_NOT_CURRENT_SURVIVOR_POPULATION", "Q602 semantics drift")
    req(prov["v6_o210_q602_current_research_status"] == "NOT_CURRENT_TARGETS", "historical line became current")
    req(prov["old_no_q602_o210_credit_semantics"] == "HISTORICAL_CREDIT_FIREWALL", "historical-credit semantics drift")

    pred = state["prior_audited_authority"]["predecessor_pr_1742"]
    req(pred["authority_status"] == "INTERMEDIATE_HOSTILE_AUDIT_PASS_AND_MERGED", "predecessor audit status drift")
    req(pred["exact_head"] == PREDECESSOR_AUDITED_HEAD and pred["review_id"] == PREDECESSOR_AUDIT_REVIEW, "predecessor audit anchor drift")
    req(pred["merged_main_sha"] == CURRENT_MAIN and pred["continuation_released"] is True, "predecessor release drift")

    current = state["current"]
    req(current["status"] == "BC2_11_STRUCTURAL_PREFLIGHT_PASS_BC2_12_ACTIVE", "current status drift")
    req(current["leaf"] == CURRENT_LEAF and current["next_route"] == CURRENT_LEAF, "BC2-12 routing drift")
    req(current["route_family"] == "FULL178_PICARD64_NODE_SUPPORT_OBSTRUCTION_INTERFACE", "current EX5 role drift")
    req(current["blocker"] == "OUTER_RANK3_SYMBOLIC_X4_PICARD64_PARENT_NOT_YET_EXACTLY_CLASSIFIED", "current blocker drift")

    iface = state["full178_interface"]
    req(iface["current_stage32_production_leaf_gate"] == "stages/stage32/32-01-178/nodes/N350/PRODUCTION_LEAF_CERTIFICATE_CONTRACT.json", "N350 boundary drift")
    req(iface["current_stage32_production_leaf_gate_status_observed"] == "PENDING_HOSTILE_AUDIT_EMPTY_PRODUCER_REGISTRY", "N350 observed state drift")
    req(iface["n350_contract_canonical_observed"] == N350_CANONICAL, "N350 canonical drift")
    req(iface["n350_registered_producer_count_observed"] == 0, "N350 registry count drift")
    req(iface["ex5_retained_exact_unsat_progress_through_rank"] == 398, "EX5 exact prefix drift")
    req(iface["ex5_structural_replay_progress_through_rank"] == 531, "EX5 structural prefix drift")
    req(iface["newer_ex5_progress_auto_promoted_to_main"] is False, "EX5 auto-promoted to MAIN")
    req(iface["n350_producer_registration_available_to_ex5_now"] is False, "EX5 prematurely registered into N350")
    req(iface["population_wide_full178_adapter_complete"] is False, "population-wide adapter falsely complete")
    req(iface["effectivity_or_actual_curve_existence_proved_by_interface"] is False, "interface widened to existence/effectivity")

    frontier = state["frontier"]
    req(frontier["runtime_exceptional_index_to_projective_node_bridge_complete"] is True, "runtime-node bridge lost")
    req(frontier["picard64_exact_completion_interface_available"] is True, "Picard64 interface lost")
    req(frontier["closed_local_terminal_blocks"] == [[0, 132], [133, 265], [266, 398]], "local block list drift")
    req(frontier["closed_local_terminal_rank_prefix"] == [0, 398], "local exact prefix drift")
    req(frontier["structurally_rederived_next_block"] == [399, 531], "BC2-11 structural block drift")
    req(frontier["structurally_rederived_next_block_picard64_closed"] is False, "BC2-11 structural replay promoted to UNSAT")
    req(frontier["whole_g1_d008_e4_stratum_closed"] is False, "local prefix promoted to stratum")
    req(frontier["FULL178_complete"] is False, "local prefix promoted to FULL178")
    req(frontier["population_wide_main_consumable_result_complete"] is False, "MAIN-consumable result falsely complete")

    retained = state["retained_exact_progress"]
    req(retained["bc2_05_rank_0_132_checkpoint_canonical"] == "cc62959ccf8c2939ff4024dc3a1e4ba59fdea38b7d33fd94817161b732c5284e", "BC2-05 provenance drift")
    req(retained["bc2_08_rank_133_265_checkpoint_canonical"] == "af197e67d3f56a6775f99f49aae59a14bc99bfa8c1b9b1d113749df3f1aa162c", "BC2-08 provenance drift")
    req(retained["bc2_10_rank_266_398_checkpoint_canonical"] == BC2_10_CANONICAL, "BC2-10 provenance drift")
    req(retained["bc2_10_evidence_canonical"] == BC2_10_EVIDENCE, "BC2-10 evidence provenance drift")
    req(retained["bc2_11_rank_399_531_structural_checkpoint_canonical"] == BC2_11_CANONICAL, "BC2-11 provenance drift")
    req(retained["exact_evidence_rewritten_by_semantic_sync"] is False, "semantic sync claims evidence rewrite")

    bc2_10 = load(BC2_10_PATH)
    req(bc2_10["canonical_sha256_without_this_field"] == BC2_10_CANONICAL, "BC2-10 canonical field drift")
    req(canonical_without_field(bc2_10, "canonical_sha256_without_this_field") == BC2_10_CANONICAL, "BC2-10 canonical replay drift")
    req(bc2_10["proof_partition"]["terminal_rank_block"] == [266, 398], "BC2-10 block drift")
    req(bc2_10["exact_result"]["aggregate_result"] == "UNSAT", "BC2-10 result drift")
    req(bc2_10["exact_result"]["rank_266_to_398_block_exact_unsat_authorized"] is True, "BC2-10 authority lost")
    req(bc2_10["exact_result"]["evidence_canonical_sha256"] == BC2_10_EVIDENCE, "BC2-10 evidence lock drift")

    bc2_11 = load(BC2_11_PATH)
    req(bc2_11["canonical_sha256_without_this_field"] == BC2_11_CANONICAL, "BC2-11 canonical field drift")
    req(canonical_without_field(bc2_11, "canonical_sha256_without_this_field") == BC2_11_CANONICAL, "BC2-11 canonical replay drift")
    nxt = bc2_11["next_block"]
    req([nxt["terminal_rank_start"], nxt["terminal_rank_end"]] == [399, 531], "BC2-11 rank block drift")
    req(nxt["outer_exceptional_rank"] == 3 and nxt["block_width"] == 133, "BC2-11 outer-rank/block-width drift")
    req(nxt["base_terminal_x4_zero"] == [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1], "BC2-11 base terminal drift")
    req(nxt["all_133_rank_unrank_replays_exact"] is True and nxt["all_133_terminal_predicate_replays_exact"] is True, "BC2-11 exact replay authority lost")
    req(bc2_11["execution"]["solver_invoked"] is False and bc2_11["execution"]["heavy_compute_invoked"] is False, "BC2-11 widened into solver/heavy credit")
    req(bc2_11["firewalls"]["next_block_picard64_closed"] is False, "BC2-11 structural replay promoted to Picard64 closure")
    req(bc2_11["next_exact_unit"]["id"] == CURRENT_LEAF, "BC2-11 next-unit drift")

    for key, value in state["credit"].items():
        if key != "level":
            req(value is False, f"unauthorized current credit: {key}")
    for key, value in state["historical_credit_firewall"].items():
        req(value is False, f"historical-credit firewall violated: {key}")
    for key, value in state["firewalls"].items():
        req(value is False, f"current firewall violated: {key}")

    boundary = state["intermediate_audit_boundary"]
    req(boundary["predecessor_pr"] == 1742, "intermediate audit PR drift")
    req(boundary["audited_exact_head"] == PREDECESSOR_AUDITED_HEAD, "intermediate audit head drift")
    req(boundary["audit_review_id"] == PREDECESSOR_AUDIT_REVIEW and boundary["audit_result"] == "PASS", "intermediate audit PASS drift")
    req(boundary["freeze_released"] is True, "intermediate audit freeze not released")

    step = state["next_step"]
    req(step["id"] == CURRENT_LEAF, "next-step drift")
    req(step["heavy_scaleout_authorized"] is False, "heavy scaleout silently authorized")
    req(step["main_promotion_authorized"] is False, "MAIN promotion silently authorized")
    req(step["blocked_until_intermediate_hostile_audit_pass"] is False, "released intermediate audit incorrectly blocks continuation")
    req(step["n350_registration_authorized"] is False, "N350 registration silently authorized")

    # Historical Cycle1 evidence remains source-locked and must still replay.
    receipt = load(RECEIPT_PATH)
    cert = load(CERT_PATH)
    req(receipt["candidate_pr"] == 1710 and receipt["candidate_exact_head"] == CYCLE1_HEAD, "Cycle1 receipt target drift")
    req(receipt["audit_review_id"] == CYCLE1_REVIEW and receipt["audit_result"] == "PASS", "Cycle1 receipt PASS drift")
    req(receipt["claim_id"] == CYCLE1_CLAIM and receipt["claim_core_sha256"] == CYCLE1_CORE, "Cycle1 claim identity drift")
    req(cert["canonical_sha256_without_this_field"] == CYCLE1_CERT, "Cycle1 certificate canonical field drift")
    req(canonical_without_field(cert, "canonical_sha256_without_this_field") == CYCLE1_CERT, "Cycle1 certificate canonical replay drift")

    verify_current_docs()

    print("PASS: Stage32EX5 BC2-11 structural continuation synchronized; historical source locks preserved")
    print(f"stage32_mode={MODE}")
    print("primary_incomplete=32-01:FULL178")
    print("historical_q602_residues=[73,97,235]:PROVENANCE_ONLY")
    print("local_exact_unsat_prefix=0..398")
    print("structural_next_block=399..531:NO_PICARD64_CREDIT")
    print(f"next_leaf={CURRENT_LEAF}")
    print("n350_registration=NO:PENDING_MAIN_HOSTILE_AUDIT")
    print("stage32_main_credit=NO")
    print("merge=SEPARATE_USER_ACTION")


if __name__ == "__main__":
    main()
