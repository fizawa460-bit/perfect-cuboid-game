#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "bc2_18_n354_survivor_exceptional_mod8_decomposition.py"
CHECKPOINT = HERE / "bc2-18-n354-survivor-selected-exceptional-mod8-checkpoint.json"
CLAIM_SYNC = HERE / "bc2-18-claim-sync-receipt.json"
EXPECTED_OUTPUT_CANONICAL = "ca53c910b70cb41dd628cd1d428227b4aa91523ed49b74b0e669e89e7e88fe2e"
EXPECTED_CHECKPOINT_CANONICAL = "b789468cb515e9ebff55ca7bbfab98a32b3857137dd0ea534fcfdf20b914f6f8"
EXPECTED_CLAIM_SYNC_CANONICAL = "820c5700e58f7c82fb28fc64186876a3d1c53a810034597219ca6e3772791953"


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def canonical_without(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def load_exact(path: Path, expected: str, label: str) -> dict:
    obj = json.loads(path.read_text())
    req(obj.get("canonical_sha256_without_this_field") == expected, f"{label} canonical field drift")
    req(canonical_without(obj) == expected, f"{label} canonical replay drift")
    return obj


def main() -> None:
    cp = load_exact(CHECKPOINT, EXPECTED_CHECKPOINT_CANONICAL, "checkpoint")
    sync = load_exact(CLAIM_SYNC, EXPECTED_CLAIM_SYNC_CANONICAL, "claim-sync receipt")
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "bc2-18.json"
        subprocess.run([sys.executable, str(SOURCE), "--output", str(out)], check=True)
        fresh = json.loads(out.read_text())
    req(fresh.get("canonical_sha256_without_this_field") == EXPECTED_OUTPUT_CANONICAL, "exact source replay canonical drift")
    req(fresh["status"] == "PASS_SELECTED_EXCEPTIONAL_MOD8_DECOMPOSITION_NORMAL_POSITIVITY_REMAINS", "status drift")
    p = fresh["parent_space"]
    q = fresh["picard_integrality_extension"]
    req(p["enumerated_parent_count"] == 177100 and p["expected_parent_count"] == 177100, "parent coverage drift")
    req(q["mod8_extendable_parent_count"] == 7336, "mod8 survivor count drift")
    req(q["rejected_by_integrality_extension_count"] == 169764, "mod8 reject count drift")
    req(q["feasible_selected_residual_mass_histogram"] == {"2":6,"3":34,"4":276,"5":1244,"6":5776}, "survivor mass histogram drift")
    req(q["feasible_stream_sha256"] == "752a7618e5a4301aea16a3a4983081e02fb26451a21d84e4b8e60b8d11f84db7", "survivor stream drift")
    req(q["x4_allowed_residues_mod8_union"] == list(range(8)), "x4 residue union drift")
    req(q["x4_residue_mask_histogram"] == {"255":7336}, "x4 mask histogram drift")
    req(q["full_check"]["modulus"] == 8 and q["full_check"]["active_congruence_rows"] == 46, "HNF congruence contract drift")
    req(cp["source_locks"]["exact_output_canonical"] == EXPECTED_OUTPUT_CANONICAL, "checkpoint output lock drift")
    req(cp["exact_decomposition"]["enumerated_parent_count"] == 177100, "checkpoint parent count drift")
    req(cp["exact_decomposition"]["mod8_extendable_parent_count"] == 7336, "checkpoint survivor count drift")
    req(cp["credit"]["whole_first_block_unsat"] is False, "partial filter falsely promoted to block UNSAT")
    req(cp["next_exact_unit"]["id"] == "BC2_19_NORMAL_POSITIVITY_MASS_REPLAY_ON_MOD8_SURVIVING_PARENTS", "next route drift")
    req(sync["trigger"] == "RETAINED_CONSOLIDATION", "claim-sync trigger drift")
    req(sync["claim_dag"]["existing_active_goal"] == "S32.FULL178.NUMERICAL_CENSUS.V1", "active goal drift")
    req(sync["claim_dag"]["active_frontier_materially_changed"] is False, "unexpected frontier remap")
    req(sync["claim_dag"]["main_credit_granted"] is False, "unexpected MAIN promotion")
    for k, v in cp["firewalls"].items(): req(v is False, f"checkpoint firewall violated: {k}")
    for k, v in sync["firewalls"].items(): req(v is False, f"claim-sync firewall violated: {k}")
    print("PASS: BC2-18 exact selected-exceptional mod8 decomposition replayed")
    print("parents=177100 rejected=169764 survivors=7336")
    print("x4_residues=0..7 all retained; normal positivity/mass remains")
    print("next=BC2_19_NORMAL_POSITIVITY_MASS_REPLAY_ON_MOD8_SURVIVING_PARENTS")
    print("main_credit=NO")


if __name__ == "__main__":
    main()
