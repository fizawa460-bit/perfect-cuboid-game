#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE_PATH = HERE / "MAIN-STATE.json"
BC2_10_PATH = HERE / "breadth-cycle-2" / "bc2-10-outer-rank2-exact-unsat-checkpoint.json"
RECEIPT_PATH = HERE / "ex5-12-hostile-audit-pass-receipt.json"
CERT_PATH = HERE / "ex5-11-terminal-route-decision-certificate.json"

STATE_SCHEMA = "STAGE32EX5_MAIN_COMPACT_STATE_V4_FULL178_FINAL_CHAIN_SYNC"
MODE = "FULL178_AND_FINAL_MILESTONE_CHAIN"
CURRENT_LEAF = "BC2_11_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT"
BC2_10_CANONICAL = "1abeb2bd5299ed217840d028eb99ed961d98238cdec75b5286b05b7f066a752b"
BC2_10_EVIDENCE = "06e4e0e8fbbe1bb64fc757be58f272fec0e85bea1e3bd7a9f21f8bf0dbda1531"
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
    req(boot["current_main_sha_observed"] == "e2da76d90a0994af5038023613c6c4084c4c507e", "observed main drift")
    req(boot["active_work_pr"] == 1742 and boot["work_branch"] == "stage32ex5-mainbatch-bc2-01b", "active EX5 surface drift")
    req(boot["merge_authorized"] is False, "merge authorization drift")

    auth = state["stage32_main_authority"]
    req(auth["authority_pr"] == 1753, "Stage32 MAIN PR drift")
    req(auth["authority_head_observed"] == "6327346d336028c910410da9bd430e117ecc024d", "Stage32 MAIN observed head drift")
    req(auth["control_mode"] == MODE, "Stage32 mode regression")
    req(auth["primary_incomplete_id"] == "32-01" and auth["primary_incomplete_name"] == "FULL178", "primary incomplete regression")
    for key in ("V6_is_current_attack_target", "O210_is_current_attack_target", "Q602_is_current_attack_target"):
        req(auth[key] is False, f"historical target reactivated: {key}")
    req(auth["historical_formal_q602_residues"] == [73,97,235], "historical Q602 triple lost")
    req(auth["historical_formal_q602_residues_are_current_survivors"] is False, "historical Q602 triple promoted to current survivors")

    prov = state["historical_formal_provenance"]
    req(prov["q602_residue_triple"] == [73,97,235], "Q602 provenance drift")
    req(prov["q602_residue_triple_semantics"] == "HISTORICAL_FORMAL_PROVENANCE_NOT_CURRENT_SURVIVOR_POPULATION", "Q602 semantics drift")
    req(prov["v6_o210_q602_current_research_status"] == "NOT_CURRENT_TARGETS", "historical line became current")
    req(prov["old_no_q602_o210_credit_semantics"] == "HISTORICAL_CREDIT_FIREWALL", "historical-credit semantics drift")

    current = state["current"]
    req(current["status"] == "BC2_10_RETAINED_LOCAL_EXACT_OBSTRUCTION_PROGRESS", "current status drift")
    req(current["leaf"] == CURRENT_LEAF and current["next_route"] == CURRENT_LEAF, "BC2-11 routing drift")
    req(current["route_family"] == "FULL178_PICARD64_NODE_SUPPORT_OBSTRUCTION_INTERFACE", "current EX5 role drift")
    req(current["blocker"] == "NEXT_133_RANK_EXCEPTIONAL_BLOCK_AFTER_RANK_398_NOT_YET_EXACTLY_REDERIVED", "current blocker drift")

    iface = state["full178_interface"]
    req(iface["stage32_consumption_node"] == "stages/stage32/32-01-178/nodes/N150/STATE.json", "N150 boundary drift")
    req(iface["main_consumed_snapshot_through_rank_observed"] == 265, "N150 snapshot drift")
    req(iface["ex5_retained_progress_through_rank"] == 398, "EX5 retained prefix drift")
    req(iface["newer_ex5_progress_auto_promoted_to_main"] is False, "EX5 auto-promoted to MAIN")
    req(iface["population_wide_full178_adapter_complete"] is False, "population-wide adapter falsely complete")
    req(iface["effectivity_or_actual_curve_existence_proved_by_interface"] is False, "interface widened to existence/effectivity")

    frontier = state["frontier"]
    req(frontier["runtime_exceptional_index_to_projective_node_bridge_complete"] is True, "runtime-node bridge lost")
    req(frontier["picard64_exact_completion_interface_available"] is True, "Picard64 interface lost")
    req(frontier["closed_local_terminal_blocks"] == [[0,132],[133,265],[266,398]], "local block list drift")
    req(frontier["closed_local_terminal_rank_prefix"] == [0,398], "local prefix drift")
    req(frontier["whole_g1_d008_e4_stratum_closed"] is False, "local prefix promoted to stratum")
    req(frontier["FULL178_complete"] is False, "local prefix promoted to FULL178")
    req(frontier["population_wide_main_consumable_result_complete"] is False, "N150 reopen condition falsely satisfied")

    retained = state["retained_exact_progress"]
    req(retained["bc2_05_rank_0_132_checkpoint_canonical"] == "cc62959ccf8c2939ff4024dc3a1e4ba59fdea38b7d33fd94817161b732c5284e", "BC2-05 provenance drift")
    req(retained["bc2_08_rank_133_265_checkpoint_canonical"] == "af197e67d3f56a6775f99f49aae59a14bc99bfa8c1b9b1d113749df3f1aa162c", "BC2-08 provenance drift")
    req(retained["bc2_10_rank_266_398_checkpoint_canonical"] == BC2_10_CANONICAL, "BC2-10 provenance drift")
    req(retained["bc2_10_evidence_canonical"] == BC2_10_EVIDENCE, "BC2-10 evidence provenance drift")
    req(retained["exact_evidence_rewritten_by_semantic_sync"] is False, "semantic sync claims evidence rewrite")

    bc2 = load(BC2_10_PATH)
    req(bc2["canonical_sha256_without_this_field"] == BC2_10_CANONICAL, "BC2-10 canonical field drift")
    req(canonical_without_field(bc2, "canonical_sha256_without_this_field") == BC2_10_CANONICAL, "BC2-10 canonical replay drift")
    req(bc2["proof_partition"]["terminal_rank_block"] == [266,398], "BC2-10 block drift")
    req(bc2["exact_result"]["aggregate_result"] == "UNSAT", "BC2-10 result drift")
    req(bc2["exact_result"]["rank_266_to_398_block_exact_unsat_authorized"] is True, "BC2-10 authority lost")
    req(bc2["exact_result"]["evidence_canonical_sha256"] == BC2_10_EVIDENCE, "BC2-10 evidence lock drift")
    req(bc2["next_exact_unit"]["id"] == CURRENT_LEAF, "BC2-10 next-unit drift")

    for key, value in state["credit"].items():
        if key != "level":
            req(value is False, f"unauthorized current credit: {key}")
    for key, value in state["historical_credit_firewall"].items():
        req(value is False, f"historical-credit firewall violated: {key}")
    for key, value in state["firewalls"].items():
        req(value is False, f"current firewall violated: {key}")
    req(state["next_step"]["id"] == CURRENT_LEAF, "next-step drift")
    req(state["next_step"]["heavy_scaleout_authorized"] is False, "heavy scaleout silently authorized")
    req(state["next_step"]["main_promotion_authorized"] is False, "MAIN promotion silently authorized")
    req(state["next_step"]["blocked_until_intermediate_hostile_audit_pass"] is True, "100-commit audit freeze missing")
    req(state["intermediate_audit_boundary"]["freeze_after_this_semantic_sync_commit"] is True, "intermediate audit boundary missing")

    # Historical Cycle1 evidence remains source-locked and must still replay.
    receipt = load(RECEIPT_PATH)
    cert = load(CERT_PATH)
    req(receipt["candidate_pr"] == 1710 and receipt["candidate_exact_head"] == CYCLE1_HEAD, "Cycle1 receipt target drift")
    req(receipt["audit_review_id"] == CYCLE1_REVIEW and receipt["audit_result"] == "PASS", "Cycle1 receipt PASS drift")
    req(receipt["claim_id"] == CYCLE1_CLAIM and receipt["claim_core_sha256"] == CYCLE1_CORE, "Cycle1 claim identity drift")
    req(cert["canonical_sha256_without_this_field"] == CYCLE1_CERT, "Cycle1 certificate canonical field drift")
    req(canonical_without_field(cert, "canonical_sha256_without_this_field") == CYCLE1_CERT, "Cycle1 certificate canonical replay drift")

    verify_current_docs()

    print("PASS: Stage32EX5 current semantics synchronized; historical source locks preserved")
    print(f"stage32_mode={MODE}")
    print("primary_incomplete=32-01:FULL178")
    print("historical_q602_residues=[73,97,235]:PROVENANCE_ONLY")
    print("local_exact_unsat_prefix=0..398")
    print(f"next_leaf={CURRENT_LEAF}:BLOCKED_PENDING_INTERMEDIATE_AUDIT")
    print("stage32_main_credit=NO")
    print("merge=SEPARATE_USER_ACTION")


if __name__ == "__main__":
    main()
