#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
B2 = HERE / "breadth-cycle-2"
STATE_PATH = HERE / "MAIN-STATE.json"
BC2_10_PATH = B2 / "bc2-10-outer-rank2-exact-unsat-checkpoint.json"
BC2_11_PATH = B2 / "bc2-11-next-exceptional-terminal-block-preflight-checkpoint.json"
BC2_12_EVIDENCE_PATH = B2 / "bc2-12-outer-rank3-parent-preflight-evidence.json"
BC2_12_CHECKPOINT_PATH = B2 / "bc2-12-outer-rank3-exact-unsat-checkpoint.json"
BC2_13_PATH = B2 / "bc2-13-next-exceptional-terminal-block-preflight-checkpoint.json"
BC2_14_EVIDENCE_PATH = B2 / "bc2-14-outer-rank4-parent-preflight-evidence.json"
BC2_14_CHECKPOINT_PATH = B2 / "bc2-14-outer-rank4-exact-unsat-checkpoint.json"
BC2_14_CLAIM_SYNC_PATH = B2 / "bc2-14-claim-sync-receipt.json"
BC2_15_PATH = B2 / "bc2-15-next-exceptional-terminal-block-preflight-checkpoint.json"
RECEIPT_PATH = HERE / "ex5-12-hostile-audit-pass-receipt.json"
CERT_PATH = HERE / "ex5-11-terminal-route-decision-certificate.json"

STATE_SCHEMA = "STAGE32EX5_MAIN_COMPACT_STATE_V4_FULL178_FINAL_CHAIN_SYNC"
MODE = "FULL178_AND_FINAL_MILESTONE_CHAIN"
CURRENT_LEAF = "BC2_16_OUTER_RANK5_SYMBOLIC_X4_PARENT_PREFLIGHT"
CURRENT_MAIN = "5ca6acba4b591d9e2d40057241c850598c1fa1df"
STAGE32_MAIN_HEAD = "b1d44137e0dd87cd3a604221715596d9b3574bc5"
N349C_HANDOFF = "2034688f2f881fbd1aeab8b4a567179a8767a7378daf43105910f0de92320eec"
N350_CANONICAL = "7d64040945f258048f9d61b0f888ca8d3720bedee6eab8902c7233ffc059d25a"
BC2_10_CANONICAL = "1abeb2bd5299ed217840d028eb99ed961d98238cdec75b5286b05b7f066a752b"
BC2_10_EVIDENCE = "06e4e0e8fbbe1bb64fc757be58f272fec0e85bea1e3bd7a9f21f8bf0dbda1531"
BC2_11_CANONICAL = "b7c3d16f415623dabd6356a2ed94794c96da51de39c7118a7b4ec706b7b81f0d"
BC2_12_EVIDENCE = "d55b84e9b90692c14211e7d1affe73857f0cec2496305121067e2cd71d8da58a"
BC2_12_CHECKPOINT = "2fdb506c601ece59ef107fa62fc4e8948b6ea5145dae413e63ccc2d11691ecd9"
BC2_13_CANONICAL = "77a0d31f6c5ca4b725c8d4f34ac2a867b82e042768858ff6475d949e1444f9c0"
BC2_13_REPLAY = "c7178bb53882b5e4c88309bf26ff149e993f07d4c610aec98c50f7a9a84005d5"
BC2_14_EVIDENCE = "52fb48627a8646db2dc5b3e0b04eb32bc89ca9391988f4b91f7f51afada2de5d"
BC2_14_CHECKPOINT = "fa603024cbf3b89fb097401f4e5e9b3f0cad04a0a0b6dd0b919b3a37b2781c0e"
BC2_14_CLAIM_SYNC = "b42ff343464c2dfceaa9203309024f657ee1d0f29bfaa7e326b0dfcf21598ddc"
BC2_15_CANONICAL = "f88ebe53c4300c01fc0a4870cc0dca75a0a091b60c95c8da7e00926bcee43182"
BC2_15_REPLAY = "6655d249aa6d51cea8fe9bd7108c315c523b5ee1725d36dd1a1a537e11d4724f"
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


def canonical_without_field(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def verify_canonical(path: Path, expected: str, label: str) -> dict:
    obj = load(path)
    req(obj.get("canonical_sha256_without_this_field") == expected, f"{label} canonical field drift")
    req(canonical_without_field(obj) == expected, f"{label} canonical replay drift")
    return obj


def verify_current_docs() -> None:
    docs = {
        "README": (HERE / "README.md").read_text(encoding="utf-8"),
        "START": (HERE / "MAIN-START-HERE.md").read_text(encoding="utf-8"),
        "ROADMAP": (HERE / "CURRENT-ROADMAP.md").read_text(encoding="utf-8"),
        "AUDIT": (HERE / "CURRENT-AUDIT-CONTRACT.md").read_text(encoding="utf-8"),
    }
    for name, text in docs.items():
        req(MODE in text and "32-01" in text and "FULL178" in text, f"{name} lost Stage32 routing")
        req("0..664" in text, f"{name} lost exact prefix")
        req("665..797" in text, f"{name} lost BC2-15 structural block")
        req("N349C" in text and "N350" in text, f"{name} lost MAIN boundary distinction")
    req("not the current Stage32 survivor population" in docs["README"], "README Q602 provenance wording drift")
    req("not current attack targets" in docs["ROADMAP"], "roadmap restored historical targets")
    req("historical-credit firewall" in docs["AUDIT"], "audit historical-credit firewall missing")
    req(CURRENT_LEAF in docs["README"] and CURRENT_LEAF in docs["ROADMAP"], "BC2-16 route missing")
    req("historical Cycle1 source-locked roadmap" in docs["ROADMAP"] or "historical Cycle1 source-locked roadmap" in docs["README"], "historical roadmap lock protection missing")
    req("historical Cycle1 source-locked contract" in docs["AUDIT"], "historical audit lock protection missing")


def main() -> None:
    state = load(STATE_PATH)
    req(state["schema"] == STATE_SCHEMA and state["stage"] == "32EX5", "state identity drift")
    boot = state["bootstrap"]
    req(boot["current_main_sha_observed"] == CURRENT_MAIN and boot["active_work_pr"] == 1765, "working surface drift")
    req(boot["merge_authorized"] is False, "merge authorization drift")

    auth = state["stage32_main_authority"]
    req(auth["authority_pr"] == 1753 and auth["authority_head_observed"] == STAGE32_MAIN_HEAD, "Stage32 MAIN head drift")
    req(auth["control_mode"] == MODE and auth["primary_incomplete_id"] == "32-01", "Stage32 mode/primary incomplete drift")
    req(auth["latest_retained_checkpoint_observed"] == "N349C_HOSTILE_AUDIT", "latest MAIN checkpoint drift")
    req(auth["latest_retained_checkpoint_handoff_canonical_observed"] == N349C_HANDOFF, "N349C handoff drift")
    req(auth["startup_state_lags_latest_pr_checkpoint"] is True, "MAIN startup lag distinction lost")
    for key in ("V6_is_current_attack_target", "O210_is_current_attack_target", "Q602_is_current_attack_target"):
        req(auth[key] is False, f"historical target reactivated: {key}")
    req(auth["historical_formal_q602_residues"] == [73, 97, 235] and auth["historical_formal_q602_residues_are_current_survivors"] is False, "Q602 provenance drift")

    current = state["current"]
    req(current["status"] == "BC2_15_STRUCTURAL_PREFLIGHT_PASS_BC2_16_ACTIVE", "current status drift")
    req(current["leaf"] == CURRENT_LEAF and current["next_route"] == CURRENT_LEAF, "BC2-16 routing drift")
    req(current["blocker"] == "OUTER_RANK5_SYMBOLIC_X4_PICARD64_PARENT_NOT_YET_EXACTLY_CLASSIFIED", "BC2-16 blocker drift")

    iface = state["full178_interface"]
    req(iface["production_registration_boundary"] == "stages/stage32/32-01-178/nodes/N350/PRODUCTION_LEAF_CERTIFICATE_CONTRACT.json", "N350 boundary drift")
    req(iface["n350_contract_canonical_observed"] == N350_CANONICAL and iface["n350_registered_producer_count_observed"] == 0, "N350 contract/registry drift")
    req(iface["ex5_retained_exact_unsat_progress_through_rank"] == 664, "exact prefix drift")
    req(iface["ex5_structural_replay_progress_through_rank"] == 797, "structural prefix drift")
    req(iface["newer_ex5_progress_auto_promoted_to_main"] is False and iface["n350_producer_registration_available_to_ex5_now"] is False, "EX5 promotion firewall drift")

    frontier = state["frontier"]
    req(frontier["closed_local_terminal_blocks"] == [[0,132],[133,265],[266,398],[399,531],[532,664]], "closed block list drift")
    req(frontier["closed_local_terminal_rank_prefix"] == [0,664], "closed prefix drift")
    req(frontier["next_structural_block_exactly_rederived"] is True and frontier["structural_replay_rank_prefix"] == [0,797], "BC2-15 structural frontier drift")
    req(frontier["whole_g1_d008_e4_stratum_closed"] is False and frontier["FULL178_complete"] is False, "local progress promoted")

    c10 = verify_canonical(BC2_10_PATH, BC2_10_CANONICAL, "BC2-10 checkpoint")
    req(c10["exact_result"]["aggregate_result"] == "UNSAT" and c10["exact_result"]["evidence_canonical_sha256"] == BC2_10_EVIDENCE, "BC2-10 result drift")
    c11 = verify_canonical(BC2_11_PATH, BC2_11_CANONICAL, "BC2-11 checkpoint")
    req(c11["next_block"]["outer_exceptional_rank"] == 3, "BC2-11 outer rank drift")
    e12 = verify_canonical(BC2_12_EVIDENCE_PATH, BC2_12_EVIDENCE, "BC2-12 evidence")
    c12 = verify_canonical(BC2_12_CHECKPOINT_PATH, BC2_12_CHECKPOINT, "BC2-12 checkpoint")
    req(e12["parent_result"]["exact_unsat_parent_branches"] == 20 and e12["parent_result"]["unknown_parent_branches"] == 0, "BC2-12 partition drift")
    req(c12["scope"]["local_exact_unsat_prefix"] == [0,531], "BC2-12 prefix drift")
    c13 = verify_canonical(BC2_13_PATH, BC2_13_CANONICAL, "BC2-13 checkpoint")
    req(c13["next_block"]["replay_stream_sha256"] == BC2_13_REPLAY and c13["next_block"]["outer_exceptional_rank"] == 4, "BC2-13 structural drift")
    e14 = verify_canonical(BC2_14_EVIDENCE_PATH, BC2_14_EVIDENCE, "BC2-14 evidence")
    c14 = verify_canonical(BC2_14_CHECKPOINT_PATH, BC2_14_CHECKPOINT, "BC2-14 checkpoint")
    p14 = e14["adaptive_exceptional_partition"]
    req(p14["fixed_exceptional_mass"] == 4 and p14["residual_exceptional_mass"] == 0, "BC2-14 mass split drift")
    req(e14["parent_result"]["aggregate_result"] == "UNSAT" and e14["parent_result"]["exact_unsat_parent_branches"] == 1 and e14["parent_result"]["unknown_parent_branches"] == 0, "BC2-14 result drift")
    req(c14["scope"]["local_exact_unsat_prefix"] == [0,664], "BC2-14 prefix drift")

    c15 = verify_canonical(BC2_15_PATH, BC2_15_CANONICAL, "BC2-15 checkpoint")
    n15 = c15["next_block"]
    req([n15["terminal_rank_start"], n15["terminal_rank_end"]] == [665,797], "BC2-15 rank block drift")
    req(n15["outer_exceptional_rank"] == 5, "BC2-15 outer rank drift")
    req(n15["base_terminal_x4_zero"] == [0,1,0,0,0,0,2,0,0,0,1], "BC2-15 base terminal drift")
    req(n15["exceptional_signature"] == [0,1,0,0,0,2,0,0,0,1], "BC2-15 signature drift")
    req(n15["replay_stream_sha256"] == BC2_15_REPLAY, "BC2-15 replay stream drift")
    req(n15["all_133_rank_unrank_replays_exact"] is True and n15["all_133_terminal_predicate_replays_exact"] is True, "BC2-15 replay completeness drift")
    req(c15["execution"]["solver_invoked"] is False and c15["execution"]["heavy_compute_invoked"] is False, "BC2-15 widened to solver/heavy")
    req(c15["firewalls"]["next_block_picard64_closed"] is False, "BC2-15 structural replay promoted")
    req(c15["next_exact_unit"]["id"] == CURRENT_LEAF, "BC2-15 next route drift")

    retained = state["retained_exact_progress"]
    req(retained["bc2_15_rank_665_797_structural_checkpoint_canonical"] == BC2_15_CANONICAL, "state BC2-15 canonical drift")
    req(retained["bc2_15_rank_665_797_replay_stream_sha256"] == BC2_15_REPLAY, "state BC2-15 replay drift")

    sync = verify_canonical(BC2_14_CLAIM_SYNC_PATH, BC2_14_CLAIM_SYNC, "BC2-14 claim sync")
    req(sync["trigger"] == "RETAINED_CONSOLIDATION" and sync["claim_dag"]["existing_active_goal"] == "S32.FULL178.NUMERICAL_CENSUS.V1", "claim sync drift")
    req(sync["claim_dag"]["active_frontier_materially_changed"] is False and sync["claim_dag"]["main_credit_granted"] is False, "claim sync promotion drift")
    req(state["claim_sync"]["receipt_canonical"] == BC2_14_CLAIM_SYNC, "state claim-sync receipt drift")

    for key, value in state["credit"].items():
        if key != "level":
            req(value is False, f"unauthorized current credit: {key}")
    for key, value in state["historical_credit_firewall"].items():
        req(value is False, f"historical-credit firewall violated: {key}")
    for key, value in state["firewalls"].items():
        req(value is False, f"current firewall violated: {key}")

    step = state["next_step"]
    req(step["id"] == CURRENT_LEAF and step["heavy_scaleout_authorized"] is False, "next-step/heavy authorization drift")
    req(step["main_promotion_authorized"] is False and step["n350_registration_authorized"] is False, "promotion authorization drift")

    receipt = load(RECEIPT_PATH)
    cert = load(CERT_PATH)
    req(receipt["candidate_pr"] == 1710 and receipt["candidate_exact_head"] == CYCLE1_HEAD, "Cycle1 receipt target drift")
    req(receipt["audit_review_id"] == CYCLE1_REVIEW and receipt["audit_result"] == "PASS", "Cycle1 audit receipt drift")
    req(receipt["claim_id"] == CYCLE1_CLAIM and receipt["claim_core_sha256"] == CYCLE1_CORE, "Cycle1 claim drift")
    req(cert["canonical_sha256_without_this_field"] == CYCLE1_CERT and canonical_without_field(cert) == CYCLE1_CERT, "Cycle1 certificate drift")

    verify_current_docs()
    print("PASS: Stage32EX5 BC2-15 structural replay retained; BC2-16 routed")
    print("local_exact_unsat_prefix=0..664")
    print("structural_replay_prefix=0..797")
    print("bc2_15_outer_rank=5")
    print(f"next_leaf={CURRENT_LEAF}")
    print("stage32_main_credit=NO")
    print("merge=SEPARATE_USER_ACTION")


if __name__ == "__main__":
    main()
