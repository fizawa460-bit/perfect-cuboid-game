#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BC2 = HERE / "breadth-cycle-2"
STATE_PATH = HERE / "MAIN-STATE.json"
README_PATH = HERE / "README.md"
START_PATH = HERE / "MAIN-START-HERE.md"
ROADMAP_PATH = HERE / "stage32-ex5.md"
AUDIT_PATH = HERE / "AUDIT-CONTRACT.md"
RECEIPT_PATH = HERE / "ex5-12-hostile-audit-pass-receipt.json"
CERT_PATH = HERE / "ex5-11-terminal-route-decision-certificate.json"
BC2_10_PATH = BC2 / "bc2-10-outer-rank2-exact-unsat-checkpoint.json"

STATE_SCHEMA = "STAGE32EX5_MAIN_COMPACT_STATE_V4_FULL178_FINAL_CHAIN_SYNC"
STAGE32_MODE = "FULL178_AND_FINAL_MILESTONE_CHAIN"
STAGE32_MAIN_PR = 1753
STAGE32_MAIN_HEAD_OBSERVED = "6327346d336028c910410da9bd430e117ecc024d"
CURRENT_MAIN_OBSERVED = "e2da76d90a0994af5038023613c6c4084c4c507e"
CURRENT_EX5_PR = 1742
CURRENT_BRANCH = "stage32ex5-mainbatch-bc2-01b"
CURRENT_LEAF = "BC2_11_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT"
CURRENT_ROUTE = "EX5R-FULL178-PICARD64-NODE-INTERFACE-001"

CYCLE1_OUTCOME = "FROZEN_BREADTH_PACKAGE_EXHAUSTED_WITHOUT_QUALIFIED_ROUTE"
CYCLE1_AUDIT_HEAD = "79c601b636857eaaaa97ad4c22e682e681341bad"
CYCLE1_AUDIT_REVIEW = 5141459384
CYCLE1_CLAIM_ID = "S32.EX5.BOUNDED_EXHAUSTION_CANDIDATE.V2"
CYCLE1_CLAIM_CORE = "6e9093c4fc25455a8c08b9cdb80fc73d127d3759c0b1edfab25b259dcec210a3"
CYCLE1_CERT_CANONICAL = "b0d0a81cf79448703d5e10d9280e6e19ac5f4f32dc31061c9c836d323bcebba7"
EARLY_BC2_CLAIM_ID = "S32.EX5.BC2_NODE_SUPPORT_SPAN_CHECKPOINT.V1"
EARLY_BC2_HEAD = "280776eb5803f69bcb28b5c1da5e546cc198b5a2"
EARLY_BC2_REVIEW = 5149663802

BC2_05_CANONICAL = "cc62959ccf8c2939ff4024dc3a1e4ba59fdea38b7d33fd94817161b732c5284e"
BC2_08_CANONICAL = "af197e67d3f56a6775f99f49aae59a14bc99bfa8c1b9b1d113749df3f1aa162c"
BC2_10_CANONICAL = "1abeb2bd5299ed217840d028eb99ed961d98238cdec75b5286b05b7f066a752b"
BC2_10_EVIDENCE = "06e4e0e8fbbe1bb64fc757be58f272fec0e85bea1e3bd7a9f21f8bf0dbda1531"


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


def require_current_docs() -> None:
    docs = {
        "README": README_PATH.read_text(encoding="utf-8"),
        "START": START_PATH.read_text(encoding="utf-8"),
        "ROADMAP": ROADMAP_PATH.read_text(encoding="utf-8"),
        "AUDIT": AUDIT_PATH.read_text(encoding="utf-8"),
    }
    for name, text in docs.items():
        req(STAGE32_MODE in text, f"{name} lost current Stage32 control mode")
        req("32-01" in text and "FULL178" in text, f"{name} lost primary FULL178 routing")
    req("not the current Stage32 survivor population" in docs["README"], "README does not demote historical Q602 residues")
    req("not current attack targets" in docs["ROADMAP"], "roadmap still permits V6/O210/Q602 as current targets")
    req("historical-credit firewall" in docs["AUDIT"], "audit contract lost historical-credit semantics")
    req(CURRENT_LEAF in docs["README"] and CURRENT_LEAF in docs["ROADMAP"], "current BC2-11 next step missing from current docs")


def main() -> None:
    state = load(STATE_PATH)
    req(state["schema"] == STATE_SCHEMA, "state schema drift")
    req(state["stage"] == "32EX5", "wrong stage")
    req(state["execution"]["main_command"] == "stage32ex5-mainbatch", "main command drift")
    req(state["execution"]["audit_command"] == "stage32ex5-audit", "audit command drift")

    bootstrap = state["bootstrap"]
    req(bootstrap["current_main_sha_observed"] == CURRENT_MAIN_OBSERVED, "synchronized main observation drift")
    req(bootstrap["work_branch"] == CURRENT_BRANCH, "work branch drift")
    req(bootstrap["active_work_pr"] == CURRENT_EX5_PR, "active EX5 PR drift")
    req(bootstrap["merge_authorized"] is False, "merge must remain unauthorized")

    main_auth = state["stage32_main_authority"]
    req(main_auth["authority_pr"] == STAGE32_MAIN_PR, "Stage32 MAIN PR authority drift")
    req(main_auth["authority_head_observed"] == STAGE32_MAIN_HEAD_OBSERVED, "Stage32 MAIN synchronized head drift")
    req(main_auth["control_mode"] == STAGE32_MODE, "Stage32 control mode regression")
    req(main_auth["primary_incomplete_id"] == "32-01", "primary incomplete id regression")
    req(main_auth["primary_incomplete_name"] == "FULL178", "primary incomplete name regression")
    for key in ("V6_is_current_attack_target", "O210_is_current_attack_target", "Q602_is_current_attack_target"):
        req(main_auth[key] is False, f"historical line incorrectly restored as current target: {key}")
    req(main_auth["historical_formal_q602_residues"] == [73, 97, 235], "historical Q602 provenance lost")
    req(main_auth["historical_formal_q602_residues_are_current_survivors"] is False, "historical residues promoted to current survivors")
    req(main_auth["ex5_auto_promotes_to_main"] is False, "EX5 auto-promotion firewall lost")

    prov = state["historical_formal_provenance"]
    req(prov["q602_residue_triple"] == [73, 97, 235], "formal Q602 triple provenance drift")
    req(prov["q602_residue_triple_semantics"] == "HISTORICAL_FORMAL_PROVENANCE_NOT_CURRENT_SURVIVOR_POPULATION", "Q602 triple semantics regression")
    req(prov["v6_o210_q602_current_research_status"] == "NOT_CURRENT_TARGETS", "historical route restored as current research")
    req(prov["old_no_q602_o210_credit_semantics"] == "HISTORICAL_CREDIT_FIREWALL", "old credit firewall semantics regression")

    prior = state["prior_audited_authority"]
    cycle1 = prior["cycle1"]
    req(cycle1["claim_id"] == CYCLE1_CLAIM_ID and cycle1["terminal_outcome"] == CYCLE1_OUTCOME, "Cycle1 provenance drift")
    req(cycle1["exact_head"] == CYCLE1_AUDIT_HEAD and cycle1["review_id"] == CYCLE1_AUDIT_REVIEW, "Cycle1 audit identity drift")
    req(cycle1["stage32_main_credit"] is False, "Cycle1 improperly promoted")
    early = prior["early_bc2"]
    req(early["claim_id"] == EARLY_BC2_CLAIM_ID, "early BC2 claim provenance drift")
    req(early["exact_head"] == EARLY_BC2_HEAD and early["review_id"] == EARLY_BC2_REVIEW, "early BC2 audit provenance drift")
    req(early["stage32_main_credit"] is False, "early BC2 improperly promoted")

    current = state["current"]
    req(current["status"] == "BC2_10_RETAINED_LOCAL_EXACT_OBSTRUCTION_PROGRESS", "current status drift")
    req(current["leaf"] == CURRENT_LEAF and current["next_route"] == CURRENT_LEAF, "current/next BC2 unit drift")
    req(current["route_id"] == CURRENT_ROUTE, "current FULL178 interface route drift")
    req(current["route_family"] == "FULL178_PICARD64_NODE_SUPPORT_OBSTRUCTION_INTERFACE", "route-family semantics drift")
    req(current["blocker"] == "NEXT_133_RANK_EXCEPTIONAL_BLOCK_AFTER_RANK_398_NOT_YET_EXACTLY_REDERIVED", "current blocker drift")

    required_working = {
        "stages/stage32-ex5/breadth-cycle-2/bc2-10-outer-rank2-exact-unsat-checkpoint.json",
        "stages/stage32-ex5/breadth-cycle-2/bc2-09-next-exceptional-terminal-block-preflight-checkpoint.json",
        "stages/stage32/residual-32-01-production/compressed_terminal_indexer.py",
        "stages/stage32/residual-32-01-production/compressed_terminal_family.py",
        "stages/stage32-ex5/verify_main_state.py",
    }
    req(required_working.issubset(set(state["current_leaf_working_set"])), "current BC2-11 working set incomplete")

    iface = state["full178_interface"]
    req(iface["stage32_consumption_node"] == "stages/stage32/32-01-178/nodes/N150/STATE.json", "N150 consumption boundary drift")
    req(iface["main_semantic_key"] == "s32-01-178:ex5-external-consumption-gate", "N150 semantic key drift")
    req(iface["main_consumed_snapshot_through_rank_observed"] == 265, "observed N150 snapshot drift")
    req(iface["ex5_retained_progress_through_rank"] == 398, "EX5 retained prefix drift")
    req(iface["newer_ex5_progress_auto_promoted_to_main"] is False, "newer EX5 blocks auto-promoted")
    req(iface["population_wide_full178_adapter_complete"] is False, "population-wide adapter falsely complete")
    req(iface["effectivity_or_actual_curve_existence_proved_by_interface"] is False, "interface widened to existence/effectivity")

    frontier = state["frontier"]
    req(frontier["runtime_exceptional_index_to_projective_node_bridge_complete"] is True, "retained runtime-node bridge lost")
    req(frontier["picard64_exact_completion_interface_available"] is True, "Picard64 interface lost")
    req(frontier["closed_local_terminal_blocks"] == [[0,132],[133,265],[266,398]], "closed local blocks drift")
    req(frontier["closed_local_terminal_rank_prefix"] == [0,398], "closed prefix drift")
    req(frontier["whole_g1_d008_e4_stratum_closed"] is False, "local prefix promoted to whole stratum")
    req(frontier["FULL178_complete"] is False, "local prefix promoted to FULL178")
    req(frontier["stage32_main_primary_incomplete_remains_32_01"] is True, "Stage32 primary incomplete silently changed")
    req(frontier["population_wide_main_consumable_result_complete"] is False, "N150 reopen condition falsely satisfied")

    retained = state["retained_exact_progress"]
    req(retained["bc2_05_rank_0_132_checkpoint_canonical"] == BC2_05_CANONICAL, "BC2-05 canonical provenance drift")
    req(retained["bc2_08_rank_133_265_checkpoint_canonical"] == BC2_08_CANONICAL, "BC2-08 canonical provenance drift")
    req(retained["bc2_10_rank_266_398_checkpoint_canonical"] == BC2_10_CANONICAL, "BC2-10 canonical provenance drift")
    req(retained["bc2_10_evidence_canonical"] == BC2_10_EVIDENCE, "BC2-10 evidence provenance drift")
    req(retained["exact_evidence_rewritten_by_semantic_sync"] is False, "semantic sync claims evidence rewrite")

    bc2_10 = load(BC2_10_PATH)
    req(bc2_10["canonical_sha256_without_this_field"] == BC2_10_CANONICAL, "BC2-10 checkpoint canonical field drift")
    req(canonical_without_field(bc2_10, "canonical_sha256_without_this_field") == BC2_10_CANONICAL, "BC2-10 checkpoint canonical replay drift")
    req(bc2_10["proof_partition"]["terminal_rank_block"] == [266,398], "BC2-10 rank block drift")
    req(bc2_10["exact_result"]["aggregate_result"] == "UNSAT", "BC2-10 result drift")
    req(bc2_10["exact_result"]["rank_266_to_398_block_exact_unsat_authorized"] is True, "BC2-10 UNSAT authority lost")
    req(bc2_10["exact_result"]["evidence_canonical_sha256"] == BC2_10_EVIDENCE, "BC2-10 evidence lock drift")
    req(bc2_10["next_exact_unit"]["id"] == CURRENT_LEAF, "BC2-10 next-unit drift")

    for key, value in state["credit"].items():
        if key != "level":
            req(value is False, f"unauthorized current credit: {key}")
    for key, value in state["historical_credit_firewall"].items():
        req(value is False, f"historical-credit firewall violated: {key}")
    for key, value in state["firewalls"].items():
        req(value is False, f"current firewall violated: {key}")
    req(state["next_step"]["id"] == CURRENT_LEAF, "next-step state drift")
    req(state["next_step"]["heavy_scaleout_authorized"] is False, "heavy scaleout silently authorized")
    req(state["next_step"]["main_promotion_authorized"] is False, "MAIN promotion silently authorized")

    # Preserve immutable historical Cycle1 evidence while changing only current semantics.
    receipt = load(RECEIPT_PATH)
    cert = load(CERT_PATH)
    req(receipt["schema"] == "STAGE32EX5_EX5_12_HOSTILE_AUDIT_PASS_RECEIPT_V1", "Cycle1 receipt schema drift")
    req(receipt["candidate_pr"] == 1710 and receipt["candidate_exact_head"] == CYCLE1_AUDIT_HEAD, "Cycle1 receipt target drift")
    req(receipt["audit_review_id"] == CYCLE1_AUDIT_REVIEW and receipt["audit_result"] == "PASS", "Cycle1 receipt PASS drift")
    req(receipt["claim_id"] == CYCLE1_CLAIM_ID and receipt["claim_core_sha256"] == CYCLE1_CLAIM_CORE, "Cycle1 claim identity drift")
    req(cert["terminal_decision"]["selected_outcome"] == CYCLE1_OUTCOME, "Cycle1 terminal outcome drift")
    req(cert["canonical_sha256_without_this_field"] == CYCLE1_CERT_CANONICAL, "Cycle1 certificate canonical field drift")
    req(canonical_without_field(cert, "canonical_sha256_without_this_field") == CYCLE1_CERT_CANONICAL, "Cycle1 certificate canonical replay drift")

    require_current_docs()

    print("PASS: Stage32EX5 semantics synchronized to Stage32 FULL178 final chain")
    print(f"stage32_mode={STAGE32_MODE}")
    print("primary_incomplete=32-01:FULL178")
    print("historical_q602_residues=[73,97,235]:PROVENANCE_ONLY")
    print("local_exact_unsat_prefix=0..398")
    print(f"next_leaf={CURRENT_LEAF}")
    print("stage32_main_credit=NO")
    print("merge=SEPARATE_USER_ACTION")


if __name__ == "__main__":
    main()
