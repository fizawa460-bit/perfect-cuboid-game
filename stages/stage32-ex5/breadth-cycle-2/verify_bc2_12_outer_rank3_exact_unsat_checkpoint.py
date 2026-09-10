#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
EVIDENCE = HERE / "bc2-12-outer-rank3-parent-preflight-evidence.json"
CHECKPOINT = HERE / "bc2-12-outer-rank3-exact-unsat-checkpoint.json"
EVIDENCE_CANONICAL = "d55b84e9b90692c14211e7d1affe73857f0cec2496305121067e2cd71d8da58a"
CHECKPOINT_CANONICAL = "2fdb506c601ece59ef107fa62fc4e8948b6ea5145dae413e63ccc2d11691ecd9"


def canonical_without(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    checkpoint = json.loads(CHECKPOINT.read_text())
    req(evidence["canonical_sha256_without_this_field"] == EVIDENCE_CANONICAL, "evidence canonical field drift")
    req(canonical_without(evidence) == EVIDENCE_CANONICAL, "evidence canonical replay drift")
    req(checkpoint["canonical_sha256_without_this_field"] == CHECKPOINT_CANONICAL, "checkpoint canonical field drift")
    req(canonical_without(checkpoint) == CHECKPOINT_CANONICAL, "checkpoint canonical replay drift")
    req(evidence["target"]["terminal_rank_block"] == [399, 531], "target block drift")
    req(evidence["block_semantics"]["exceptional_rank"] == 3, "outer rank drift")
    part = evidence["adaptive_exceptional_partition"]
    req(part["fixed_exceptional_mass"] == 3 and part["residual_exceptional_mass"] == 1, "exceptional mass split drift")
    req(part["mass_split_derived_from_bc2_11_terminal_and_locked_labels"] is True, "mass split provenance drift")
    req(part["parent_branch_count"] == 20, "parent partition count drift")
    parent = evidence["parent_result"]
    req(parent["aggregate_result"] == "UNSAT", "aggregate result drift")
    req(parent["tested_parent_branches"] == 20 and parent["exact_unsat_parent_branches"] == 20, "20-parent UNSAT coverage drift")
    req(parent["unknown_parent_branches"] == 0 and parent["sat_parent"] is None, "non-UNSAT parent appeared")
    req(evidence["result"]["rank_399_to_531_block_exact_unsat_authorized"] is True, "block closure credit lost")
    req(checkpoint["scope"]["local_exact_unsat_prefix"] == [0, 531], "local exact prefix drift")
    req(checkpoint["next_exact_unit"]["id"] == "BC2_13_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT", "next unit drift")
    for obj in (evidence["firewalls"], checkpoint["scope"]):
        req(obj["whole_g1_d008_e4_stratum_closed"] is False, "local result promoted to stratum closure")
        req(obj["FULL178_complete"] is False, "local result promoted to FULL178")
        req(obj["stage32_main_credit"] is False, "local result promoted to MAIN")
        req(obj["n350_production_coverage_credit"] is False, "local result promoted to N350")
        req(obj["theorem_credit"] is False and obj["endpoint_credit"] is False, "local result promoted to theorem/endpoint")
        req(obj["merge_authorized"] is False, "merge authorization drift")
    print("PASS: BC2-12 retained exact UNSAT checkpoint")
    print("local_exact_unsat_prefix=0..531")
    print("parent_partition=20/20:UNSAT")
    print("next_leaf=BC2_13_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT")


if __name__ == "__main__":
    main()
