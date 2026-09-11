#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
EVIDENCE = HERE / "bc2-16-outer-rank5-parent-preflight-evidence.json"
CHECKPOINT = HERE / "bc2-16-outer-rank5-exact-unsat-checkpoint.json"
CLAIM_SYNC = HERE / "bc2-16-claim-sync-receipt.json"
EVIDENCE_CANONICAL = "47278e00902f049e354227f02fe891b199025129a8fd3387a0249ad3b5c5ac9c"
CHECKPOINT_CANONICAL = "8cfe535fbd486b32e21c9e2cbb7c2289f2880420e5aa4cf3fc98db5f7d310a20"
CLAIM_SYNC_CANONICAL = "ddb8841a798ee491fd6322fcb5a25ac7ff64cc33fa1b82d7d5e717e13e3ea4fd"


def canonical_without(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    checkpoint = json.loads(CHECKPOINT.read_text())
    sync = json.loads(CLAIM_SYNC.read_text())
    for obj, expected, label in ((evidence,EVIDENCE_CANONICAL,"evidence"),(checkpoint,CHECKPOINT_CANONICAL,"checkpoint"),(sync,CLAIM_SYNC_CANONICAL,"claim-sync")):
        req(obj["canonical_sha256_without_this_field"] == expected, f"{label} canonical field drift")
        req(canonical_without(obj) == expected, f"{label} canonical replay drift")

    req(evidence["target"]["terminal_rank_block"] == [665, 797], "target block drift")
    req(evidence["block_semantics"]["exceptional_rank"] == 5, "outer rank drift")
    req(evidence["block_semantics"]["base_terminal_x4_zero"] == [0,1,0,0,0,0,2,0,0,0,1], "base terminal drift")
    part = evidence["adaptive_exceptional_partition"]
    req(part["fixed_exceptional_mass"] == 4 and part["residual_exceptional_mass"] == 0, "exceptional mass split drift")
    req(part["mass_split_derived_from_bc2_15_terminal_and_locked_labels"] is True, "mass split provenance drift")
    req(part["parent_branch_count"] == 1, "parent partition count drift")
    parent = evidence["parent_result"]
    req(parent["aggregate_result"] == "UNSAT", "aggregate result drift")
    req(parent["tested_parent_branches"] == 1 and parent["exact_unsat_parent_branches"] == 1, "one-parent UNSAT coverage drift")
    req(parent["unknown_parent_branches"] == 0 and parent["sat_parent"] is None, "non-UNSAT parent appeared")
    req(evidence["result"]["rank_665_to_797_block_exact_unsat_authorized"] is True, "block closure credit lost")

    req(checkpoint["exact_result"]["evidence_canonical_sha256"] == EVIDENCE_CANONICAL, "checkpoint evidence lock drift")
    req(checkpoint["scope"]["local_exact_unsat_prefix"] == [0, 797], "local exact prefix drift")
    req(checkpoint["next_exact_unit"]["id"] == "BC2_17_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT", "next unit drift")
    proof = checkpoint["proof_partition"]
    req(proof["parent_branch_count"] == 1 and proof["parent_exact_unsat_count"] == 1, "checkpoint parent coverage drift")
    req(proof["parent_unknown_count"] == 0 and proof["parent_sat_count"] == 0, "checkpoint non-UNSAT parent appeared")
    req(proof["fixed_exceptional_mass"] == 4 and proof["residual_exceptional_mass"] == 0, "checkpoint mass split drift")
    req(checkpoint["runkey_arm_commit"] == "3f4fcca1e1b3462a23caee72d8274ad44a7643a3", "runkey arm lock drift")
    req(checkpoint["workflow"]["run_id"] == 34441599406 and checkpoint["workflow"]["compute_job_id"] == 102757639746, "workflow provenance drift")

    req(sync["trigger"] == "RETAINED_CONSOLIDATION", "claim-sync trigger drift")
    req(sync["claim_dag"]["existing_active_goal"] == "S32.FULL178.NUMERICAL_CENSUS.V1", "claim-sync goal drift")
    req(sync["claim_dag"]["lane_role"] == "ATTACKS", "claim-sync lane role drift")
    req(sync["claim_dag"]["active_frontier_materially_changed"] is False, "unexpected active-frontier remap")
    req(sync["claim_dag"]["claim_registry_core_changed"] is False, "unexpected claim-core mutation")
    req(sync["claim_dag"]["main_credit_granted"] is False, "unexpected MAIN promotion")

    for obj in (evidence["firewalls"], checkpoint["scope"]):
        req(obj["whole_g1_d008_e4_stratum_closed"] is False, "local result promoted to stratum closure")
        req(obj["FULL178_complete"] is False, "local result promoted to FULL178")
        req(obj["stage32_main_credit"] is False, "local result promoted to MAIN")
        req(obj["n350_production_coverage_credit"] is False, "local result promoted to N350")
        req(obj["theorem_credit"] is False and obj["endpoint_credit"] is False, "local result promoted to theorem/endpoint")
        req(obj["merge_authorized"] is False, "merge authorization drift")

    print("PASS: BC2-16 retained exact UNSAT checkpoint")
    print("local_exact_unsat_prefix=0..797")
    print("parent_partition=1/1:UNSAT")
    print("claim_sync=NO_ACTIVE_FRONTIER_REMAP")
    print("next_leaf=BC2_17_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT")


if __name__ == "__main__":
    main()
