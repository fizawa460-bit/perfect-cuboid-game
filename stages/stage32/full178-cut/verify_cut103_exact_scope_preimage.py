#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EX5 = ROOT / "stages/stage32-ex5/breadth-cycle-2"
N355 = ROOT / "stages/stage32/32-01-178/nodes/N355"
MAIN_STATE = ROOT / "stages/stage32/MAIN-STATE.json"

BC217 = EX5 / "bc2-17-n354-authority-picard64-retarget-v2-evidence.json"
BC218 = EX5 / "bc2-18-n354-survivor-selected-exceptional-mod8-checkpoint.json"
BC224 = EX5 / "bc2-24-explicit-fibre-degree-partition-checkpoint.json"
N355_RESULT = N355 / "FULL-PREFIX-RESULT.json"
N355_PASS = N355 / "FULL-PREFIX-HOSTILE-AUDIT-PASS.json"
CUT102 = HERE / "CUT102-final-checkpoint.json"
CUT102_RESIDUAL4 = HERE / "CUT102-residual4-result.json"
CUT102_RUNNER = HERE / "cut102_finite_ring_direct_completion_v2.py"

EXPECTED = {
    str(BC217): ("28c4b762c7f96a4898c62751062648cad066578c", "a8dd000481a39011bd1d9d108d55e38e0420dbc2bb7abf4851595dfdb5da5072"),
    str(BC218): ("0e269d5ec6da24b9b887b6dd40f4b4f33242e154", "b789468cb515e9ebff55ca7bbfab98a32b3857137dd0ea534fcfdf20b914f6f8"),
    str(BC224): ("37e12dc0bf40e0dec862784f5567bd247d451742", "ac6f8afff29a4ac969b1fd32251499f299395261c1aa96a813502cfe2b22472f"),
    str(N355_RESULT): ("0f30517cc5007ea435f4183201fc6cad699dd635", "7961cbc55993d2264879686388096fbe289a6fb84ecd4b6713b6b56c371bb775"),
    str(N355_PASS): ("033294f56fb86d81b7aa43758a51a39747ccc082", "d6bda89f94eb57bf021f0acbbc5000e198f1805c09da3e5f9a531d20b70ce004"),
    str(MAIN_STATE): ("9981889309c833a1834eaadddce73e52c0aa0176", "6143a95a0fb380e3c30c6a464722b350666cec5f018318adefdae15800a676b3"),
}
EXPECTED_CUT102_BLOB = "d7ab957618d366c17b9d68029649de4f6823a9a7"
EXPECTED_CUT102_RESIDUAL4_BLOB = "e198fb799a2173f8d8e31f9d0aa2cc5a8c111128"
EXPECTED_CUT102_RUNNER_BLOB = "fbdd1e65b509526d5198743208bff79bd2488673"
EXPECTED_RESIDUAL4_CANONICAL = "c905f7e26f6e7d4ef96b911ea0a6b0b25e66474fe75d3a8881dc9ede54055d7d"
EXPECTED_TARGETS = [584,1000,1003,1014,1030,1048,1050,1056,1064,1066,1103,1106,1117,1119,1133,1198,1218,1224,1243]
EXPECTED_GROUPS = [[101,102,103],[97,98,99],[93,94,95,96]]


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_canonical(path: Path, expected_blob: str, expected_canonical: str) -> dict:
    if git_blob_sha1(path) != expected_blob:
        raise ValueError(f"blob regression: {path}")
    obj = json.loads(path.read_text())
    if obj.get("canonical_sha256_without_this_field") != expected_canonical:
        raise ValueError(f"canonical field regression: {path}")
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    if csha(q) != expected_canonical:
        raise ValueError(f"canonical replay regression: {path}")
    return obj


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    docs = {path: load_canonical(Path(path), blob, canon) for path, (blob, canon) in EXPECTED.items()}
    bc217 = docs[str(BC217)]
    bc218 = docs[str(BC218)]
    bc224 = docs[str(BC224)]
    n355 = docs[str(N355_RESULT)]
    n355_pass = docs[str(N355_PASS)]
    main_state = docs[str(MAIN_STATE)]

    if git_blob_sha1(CUT102) != EXPECTED_CUT102_BLOB:
        raise ValueError("CUT102 final checkpoint blob regression")
    if git_blob_sha1(CUT102_RESIDUAL4) != EXPECTED_CUT102_RESIDUAL4_BLOB:
        raise ValueError("CUT102 residual4 retained result blob regression")
    if git_blob_sha1(CUT102_RUNNER) != EXPECTED_CUT102_RUNNER_BLOB:
        raise ValueError("CUT102 runner blob regression")
    cut102 = json.loads(CUT102.read_text())
    residual4 = json.loads(CUT102_RESIDUAL4.read_text())
    if residual4.get("canonical_sha256_without_this_field") != EXPECTED_RESIDUAL4_CANONICAL:
        raise ValueError("CUT102 residual4 canonical regression")
    rq = dict(residual4)
    rq.pop("canonical_sha256_without_this_field", None)
    if csha(rq) != EXPECTED_RESIDUAL4_CANONICAL:
        raise ValueError("CUT102 residual4 canonical replay regression")

    target = bc217["retarget"]["selected_target"]
    if [target["g"], target["d"], target["e"]] != [1,8,8] or target["row_id"] != "g1-d008":
        raise ValueError("BC2-17 target regression")
    if bc217["retarget"]["first_block"] != [0,112] or bc217["retarget"]["first_block_width"] != 113:
        raise ValueError("BC2-17 first-block regression")
    if bc217["retarget"]["rank_unrank_replay_count"] != 113:
        raise ValueError("BC2-17 rank/unrank replay regression")
    if bc218["target"]["first_block"] != [0,112] or bc218["target"]["row_id"] != "g1-d008":
        raise ValueError("BC2-18 target regression")
    if bc218["credit"]["parent_space_coverage_exact"] is not True:
        raise ValueError("BC2-18 exact parent-space coverage lost")
    if bc218["exact_decomposition"]["mod8_extendable_parent_count"] != 7336:
        raise ValueError("BC2-18 parent population regression")
    if bc218["exact_decomposition"]["x4_residue_mask_histogram"] != {"255":7336}:
        raise ValueError("BC2-18 x4 residue coverage regression")

    if bc224["result"]["residual_unknown_parent_indices"] != EXPECTED_TARGETS:
        raise ValueError("BC2-24 retained19 identity regression")
    if bc224["target"]["other_unretained_bc2_19_unknown_identity_count"] != 172:
        raise ValueError("BC2-24 unretained identity count regression")
    if bc224["target"]["other_unretained_bc2_19_unknown_identities_inferred"] is not False:
        raise ValueError("BC2-24 unretained identity firewall regression")

    if cut102["result"]["finite_ring_obstructed_parent_indices"] != EXPECTED_TARGETS:
        raise ValueError("CUT102 retained19 obstruction regression")
    if cut102["result"]["finite_ring_obstructed_parent_count"] != 19 or cut102["result"]["residual_retained_parent_count"] != 0:
        raise ValueError("CUT102 retained19 closure regression")
    if cut102["credit"]["stage32_main_pruning_credit"] is not False:
        raise ValueError("CUT102 prematurely gained MAIN pruning credit")
    if residual4["status"] != "PASS_ALL_EIGHT_RESIDUAL_MOD2_BRANCHES_UNSAT" or residual4["unresolved_records"]:
        raise ValueError("fresh residual replay regression")

    if n355["full_prefix_cut"]["known_groups"] != EXPECTED_GROUPS:
        raise ValueError("N355 known-group partition regression")
    if n355["full_prefix_cut"]["equivalent_cut"] != "max(group1_sum,group2_sum,group3_sum)<=floor(d/2)":
        raise ValueError("N355 full-prefix cut regression")
    if n355_pass["status"] != "PASS" or n355_pass["review_id"] != 5165895301:
        raise ValueError("N355 full-prefix audit regression")
    if main_state["authority_sync"]["n355_full_prefix_audit_credit_consumed"] is not True:
        raise ValueError("current MAIN no longer consumes audited N355 full-prefix cut")
    if main_state["current_exact_frontier"]["n355_remaining_terminals"] != 66462870551188628549910:
        raise ValueError("current N355 terminal authority regression")
    if main_state["current_exact_frontier"]["n356_main_pruning_credit"] is not False:
        raise ValueError("N356 unexpectedly consumed")

    fixed = {int(k): int(v) for k, v in bc217["retarget"]["fixed_exceptional_pairings"].items()}
    group_sums = [sum(fixed[label] for label in group) for group in EXPECTED_GROUPS]
    cap = target["d"] // 2
    if group_sums != [0,1,1] or max(group_sums) > cap:
        raise ValueError("first-block fixed exceptional signature no longer survives N355 known-prefix cap")

    result = {
        "schema": "STAGE32_FULL178_CUT103_EXACT_SCOPE_PREIMAGE_CERTIFICATE_V1",
        "stage": "32",
        "surface": "full178-cut",
        "node": "CUT103",
        "status": "PASS_SCOPE_PREIMAGE_CERTIFIED_ZERO_MAIN_TERMINAL_PRUNING_CREDIT",
        "source_locks": {
            "bc2_17_blob_sha1": EXPECTED[str(BC217)][0],
            "bc2_17_canonical_sha256": EXPECTED[str(BC217)][1],
            "bc2_18_blob_sha1": EXPECTED[str(BC218)][0],
            "bc2_18_canonical_sha256": EXPECTED[str(BC218)][1],
            "bc2_24_blob_sha1": EXPECTED[str(BC224)][0],
            "bc2_24_canonical_sha256": EXPECTED[str(BC224)][1],
            "n355_full_prefix_result_blob_sha1": EXPECTED[str(N355_RESULT)][0],
            "n355_full_prefix_result_canonical_sha256": EXPECTED[str(N355_RESULT)][1],
            "n355_full_prefix_audit_blob_sha1": EXPECTED[str(N355_PASS)][0],
            "n355_full_prefix_audit_canonical_sha256": EXPECTED[str(N355_PASS)][1],
            "main_state_blob_sha1": EXPECTED[str(MAIN_STATE)][0],
            "main_state_canonical_sha256": EXPECTED[str(MAIN_STATE)][1],
            "cut102_final_blob_sha1": EXPECTED_CUT102_BLOB,
            "cut102_residual4_blob_sha1": EXPECTED_CUT102_RESIDUAL4_BLOB,
            "cut102_residual4_canonical_sha256": EXPECTED_RESIDUAL4_CANONICAL,
            "cut102_runner_blob_sha1": EXPECTED_CUT102_RUNNER_BLOB
        },
        "scope": {
            "row_id": "g1-d008",
            "g": 1,
            "d": 8,
            "e": 8,
            "full178_first_block_rank_interval": [0,112],
            "full178_first_block_width": 113,
            "bc2_18_parent_population": 7336,
            "cut102_retained_parent_indices": EXPECTED_TARGETS,
            "cut102_retained_parent_count": 19,
            "other_unretained_unknown_parent_identity_count": 172,
            "other_unretained_unknown_parent_identities_inferred": False
        },
        "preimage": {
            "parent_semantics": "BC2-18 selected-exceptional Picard64 completion-parent indices over the fixed g1-d008/e8 first block; they are not FULL178 terminal indices.",
            "x4_terminal_rank_is_not_fixed_by_a_parent": True,
            "bc2_18_x4_all_residues_mod8_available_for_every_parent": True,
            "retained19_exact_completion_image_after_cut102": "EMPTY",
            "terminal_projection_is_not_a_disjoint_19_terminal_partition": True,
            "terminal_count_may_not_be_decremented_by_19": True
        },
        "n355_current_authority_overlap": {
            "audited_full_prefix_cut_consumed_by_main": True,
            "known_groups": EXPECTED_GROUPS,
            "fixed_first_block_group_sums": group_sums,
            "cap_floor_d_over_2": cap,
            "fixed_first_block_signature_rejected_by_n355_full_prefix": False,
            "n355_authoritative_remaining_strata": 17128,
            "n355_authoritative_remaining_terminals": 66462870551188628549910,
            "n356_consumed": False,
            "new_terminal_pruning_certified_by_cut103": 0,
            "double_count_against_consumed_n355": False
        },
        "interpretation": {
            "retained19_completion_branches_closed": True,
            "whole_first_block_unsat": False,
            "reason_whole_first_block_remains_open": "172 BC2-19 UNKNOWN parent identities were not retained/reidentified and remain explicitly uninferred; CUT may not manufacture their identities or silently claim their closure.",
            "cut104_needed_for_retained19": False,
            "next_node": "CUT190_RETAINED_CHECKPOINT_AND_HOSTILE_AUDIT_HANDOFF"
        },
        "credit": {
            "cut103_scope_certificate_complete": True,
            "stage32_main_pruning_credit": False,
            "stage32_main_pruned_terminal_count": 0,
            "whole_first_block_unsat": False,
            "whole_stratum_closed": False,
            "full178_complete": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False
        },
        "firewalls": {
            "bc2_25_identity_refinement_performed": False,
            "unretained_172_identities_inferred": False,
            "completion_parent_indices_relabelled_terminal_indices": False,
            "n356_candidate_assumed_consumed": False,
            "main_authority_mutated": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False
        }
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    print(json.dumps({"status": result["status"], "canonical": result["canonical_sha256_without_this_field"]}))


if __name__ == "__main__":
    main()
