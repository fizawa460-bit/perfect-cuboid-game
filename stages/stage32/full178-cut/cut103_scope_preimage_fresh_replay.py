#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from z3 import sat, unknown, unsat, get_version_string

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EX5 = ROOT / "stages/stage32-ex5/breadth-cycle-2"
sys.path.insert(0, str(HERE))

import cut102_finite_ring_direct_completion_v2 as core

SCHEMA = "STAGE32_FULL178_CUT103_SCOPE_PREIMAGE_FRESH_REPLAY_V1"

LOCKS = {
    "bc2_17": (EX5 / "bc2-17-n354-authority-picard64-retarget-v2-evidence.json", "28c4b762c7f96a4898c62751062648cad066578c", "a8dd000481a39011bd1d9d108d55e38e0420dbc2bb7abf4851595dfdb5da5072"),
    "bc2_18": (EX5 / "bc2-18-n354-survivor-selected-exceptional-mod8-checkpoint.json", "0e269d5ec6da24b9b887b6dd40f4b4f33242e154", "b789468cb515e9ebff55ca7bbfab98a32b3857137dd0ea534fcfdf20b914f6f8"),
    "bc2_19": (EX5 / "bc2-19-n354-survivor-normal-positivity-mass-checkpoint.json", "7d75a46a3dc0f54b60b0d70aa2240882b516de59", "62e97cdb8bd6a8d14c0ac176576bd2cf2ec51020295f8703cbefc3bc85f001eb"),
    "bc2_21": (EX5 / "bc2-21-first64-unknown-parent-slice-checkpoint.json", "17790a9668c1eb3748e0c9f61fb6340f1bff1f5a", "8b40a6b0ee650897d276fb7e543d6f31ef3f76af6f3e923e109b8d02ecd46f4f"),
    "bc2_22": (EX5 / "bc2-22-recheck-44-residual-unknown-checkpoint.json", "f4213cf675c11e02f025f47d25c0768b99f619d8", "e8151702d8386eeab44d9e9705abe7b4fa0e19dde96933ffdabdc56329f2fdc2"),
    "bc2_23": (EX5 / "bc2-23-n355-redundant-cut-acceleration-checkpoint.json", "3c1f9f3c41a53d87303fb04a7b47bb7594f74edc", "6da1c158da8f8171d446c39b517270c0f7bf524ac62df0cd8f9d099155cdb3a0"),
    "bc2_24": (EX5 / "bc2-24-explicit-fibre-degree-partition-checkpoint.json", "37e12dc0bf40e0dec862784f5567bd247d451742", "ac6f8afff29a4ac969b1fd32251499f299395261c1aa96a813502cfe2b22472f"),
}

TARGETS = [584,1000,1003,1014,1030,1048,1050,1056,1064,1066,1103,1106,1117,1119,1133,1198,1218,1224,1243]


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def checked(path: Path, blob: str, canonical: str) -> dict:
    if git_blob_sha(path) != blob:
        raise ValueError(f"blob lock moved: {path}")
    obj = json.loads(path.read_text())
    if obj.get("canonical_sha256_without_this_field") != canonical:
        raise ValueError(f"canonical field moved: {path}")
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    if csha(q) != canonical:
        raise ValueError(f"canonical replay moved: {path}")
    return obj


def validate_lineage(objs: dict[str, dict]) -> dict:
    b17, b18, b19, b21, b22, b23, b24 = (objs[k] for k in ("bc2_17","bc2_18","bc2_19","bc2_21","bc2_22","bc2_23","bc2_24"))
    target = b17["retarget"]["selected_target"]
    if target != {"row_id":"g1-d008","g":1,"d":8,"e":8,"survives_n354":True}:
        raise ValueError("BC2-17 selected target moved")
    if b17["retarget"]["first_block"] != [0,112] or b17["retarget"]["first_block_width"] != 113:
        raise ValueError("BC2-17 first-block scope moved")
    if b18["exact_decomposition"]["mod8_extendable_parent_count"] != 7336:
        raise ValueError("BC2-18 parent union size moved")
    if b18["exact_decomposition"]["feasible_stream_sha256"] != core.EXPECTED_STREAM:
        raise ValueError("BC2-18 parent stream moved")
    if b19["result"]["input_mod8_parent_count"] != 7336 or b19["result"]["unknown_count"] != 236:
        raise ValueError("BC2-19 union/unknown counts moved")

    first64 = [int(v) for v in b21["target"]["retained_first64_unknown_parent_indices"]]
    r21 = [int(v) for v in b21["result"]["residual_unknown_parent_indices"]]
    u21 = [int(v) for v in b21["result"]["newly_resolved_unsat_parent_indices"]]
    if len(first64) != 64 or sorted(r21 + u21) != sorted(first64) or set(r21) & set(u21):
        raise ValueError("BC2-21 retained identity partition moved")

    r22 = [int(v) for v in b22["result"]["residual_unknown_parent_indices"]]
    u22 = [int(v) for v in b22["result"]["newly_unsat_parent_indices"]]
    if sorted(r22 + u22) != sorted(r21) or set(r22) & set(u22):
        raise ValueError("BC2-22 retained identity partition moved")

    r23 = [int(v) for v in b23["result"]["residual_unknown_parent_indices"]]
    u23 = [int(v) for v in b23["result"]["newly_unsat_parent_indices"]]
    if sorted(r23 + u23) != sorted(r22) or set(r23) & set(u23):
        raise ValueError("BC2-23 retained identity partition moved")
    if not b23["redundant_cut_certificate"]["feasible_set_preserved"] or b23["redundant_cut_certificate"]["new_mathematical_feasible_set_restriction"]:
        raise ValueError("BC2-23 redundant-cut semantics moved")

    r24 = [int(v) for v in b24["result"]["residual_unknown_parent_indices"]]
    u24 = [int(v) for v in b24["result"]["newly_unsat_parent_indices"]]
    if sorted(r24 + u24) != sorted(r23) or set(r24) & set(u24):
        raise ValueError("BC2-24 retained identity partition moved")
    if r24 != TARGETS:
        raise ValueError("BC2-24 retained19 target identities moved")
    if b24["target"]["other_unretained_bc2_19_unknown_identity_count"] != 172:
        raise ValueError("unretained identity count moved")

    return {
        "selected_target": target,
        "first_block": [0,112],
        "bc2_18_parent_union_count": 7336,
        "bc2_19_unknown_count": 236,
        "bc2_21_retained_identity_count": 64,
        "bc2_21_residual_count": len(r21),
        "bc2_22_residual_count": len(r22),
        "bc2_23_residual_count": len(r23),
        "bc2_24_residual_count": len(r24),
        "unretained_unknown_identity_count": 172,
        "n355_constraints_in_bc2_23_logically_redundant": True,
    }


def fresh_parent_check(P, blocks, exceptional_labels, parents, fixed, parent_index: int, whole_timeout: int, branch_timeout: int) -> dict:
    yE, allowed = parents[parent_index]
    identity = {
        "parent_index": parent_index,
        "selected_exceptional_labels": exceptional_labels,
        "selected_exceptional_pairings": yE,
        "selected_residual_mass": sum(yE) - sum(fixed.get(label, 0) for label in exceptional_labels),
        "x4_allowed_residues_mod8": allowed,
    }
    identity_hash = csha(identity)

    s, y, n1, linear = core.make_solver(P, blocks, fixed, 2, whole_timeout)
    for label, value in zip(exceptional_labels, yE):
        s.add(y[label - 1] == value)
    r = s.check()
    if r == unsat:
        return {"identity": identity, "identity_sha256": identity_hash, "result":"unsat", "proof_mode":"fresh_whole_parent_mod2", **linear}
    if r == sat:
        model = s.model()
        vals = [int(model.eval(v, model_completion=True).as_long()) for v in y]
        return {"identity": identity, "identity_sha256": identity_hash, "result":"sat", "proof_mode":"fresh_whole_parent_mod2", "all140_pairings_sha256":csha(vals), **linear}
    if r != unknown:
        raise ValueError("unexpected whole-parent solver result")

    branches = []
    for degree in range(core.TARGET_D + 1):
        sb, yb, n1b, lb = core.make_solver(P, blocks, fixed, 2, branch_timeout)
        for label, value in zip(exceptional_labels, yE):
            sb.add(yb[label - 1] == value)
        sb.add(n1b == degree)
        br = sb.check()
        rec = {"n1":degree,"n2":core.TARGET_D-degree,"result":str(br)}
        if br == unknown:
            rec["reason_unknown"] = sb.reason_unknown()
        elif br == sat:
            model = sb.model()
            vals = [int(model.eval(v, model_completion=True).as_long()) for v in yb]
            rec["all140_pairings_sha256"] = csha(vals)
        elif br != unsat:
            raise ValueError("unexpected branch solver result")
        branches.append(rec)
    if all(b["result"] == "unsat" for b in branches):
        result = "unsat"
    elif any(b["result"] == "sat" for b in branches):
        result = "sat"
    else:
        result = "unknown"
    return {"identity": identity, "identity_sha256": identity_hash, "result":result, "proof_mode":"fresh_exhaustive_n1_mod2_partition", "whole_reason_unknown":s.reason_unknown(), "branches":branches, **linear}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--whole-timeout-ms", type=int, default=10000)
    ap.add_argument("--branch-timeout-ms", type=int, default=20000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.whole_timeout_ms <= 0 or args.branch_timeout_ms <= 0:
        raise ValueError("positive timeouts required")

    objs = {k: checked(*v) for k, v in LOCKS.items()}
    lineage = validate_lineage(objs)
    P, blocks, exceptional_labels, parents, fixed = core.load_interface()
    if len(parents) != 7336:
        raise ValueError("deterministic parent stream size moved")

    records = [fresh_parent_check(P, blocks, exceptional_labels, parents, fixed, idx, args.whole_timeout_ms, args.branch_timeout_ms) for idx in TARGETS]
    results = {r["identity"]["parent_index"]: r["result"] for r in records}
    all_unsat = all(v == "unsat" for v in results.values())
    any_sat = any(v == "sat" for v in results.values())
    unresolved = [i for i,v in results.items() if v == "unknown"]

    if all_unsat:
        status = "PASS_LOCAL_RETAINED19_EXACT_SCOPE_AND_FRESH_MOD2_UNSAT_MAIN_PREIMAGE_NOT_ESTABLISHED"
    elif any_sat:
        status = "FAIL_CUT102_CANDIDATE_FRESH_FINITE_RING_SAT_FOUND"
    else:
        status = "BLOCKED_FRESH_REPLAY_HAS_UNKNOWN"

    body = {
        "schema": SCHEMA,
        "stage": "32",
        "surface": "full178-cut",
        "node": "CUT103",
        "status": status,
        "z3_version": get_version_string(),
        "source_locks": {k:{"path":str(v[0].relative_to(ROOT)),"blob_sha1":v[1],"canonical_sha256":v[2]} for k,v in LOCKS.items()},
        "retained_interface_source_locks": {
            "bc2_18_enumerator_blob_sha1": core.EXPECTED_D18_BLOB,
            "retained_picard_bundle_blob_sha1": core.EXPECTED_RETAINED_BLOB,
            "retained_marking_blob_sha1": core.EXPECTED_MARKING_BLOB,
            "bc2_18_feasible_stream_sha256": core.EXPECTED_STREAM,
        },
        "lineage": lineage,
        "scope_certificate": {
            "exact_object": "19 deterministic Picard64 completion parent regions in the BC2-18 ordered 7336-parent stream",
            "selected_n354_target": {"row_id":"g1-d008","g":1,"d":8,"e":8,"first_block":[0,112]},
            "retained_parent_indices": TARGETS,
            "retained_parent_count": 19,
            "these_are_full178_terminal_ids": False,
            "one_parent_equals_one_full178_terminal": False,
            "full178_terminal_preimage_cardinality_known": False,
            "population_preserving_current_main_replay_established": False,
            "other_unretained_bc2_19_unknown_identity_count": 172,
            "other_unretained_bc2_19_unknown_identities_inferred": False,
            "whole_first_block_closed": False,
            "whole_g1_d008_e8_stratum_closed": False,
            "full178_closed": False,
            "reason_main_preimage_blocked": "BC2-21 intentionally retained identities for only 64 of BC2-19's 236 UNKNOWN parent regions; 172 identities were left uninferred, and the retained parent regions are completion-system regions rather than a source-locked one-to-one FULL178 terminal population ledger."
        },
        "fresh_replay": {
            "prime": 2,
            "fresh_solver_per_parent": True,
            "fresh_solver_per_partition_branch": True,
            "whole_timeout_ms": args.whole_timeout_ms,
            "branch_timeout_ms": args.branch_timeout_ms,
            "parent_count": len(records),
            "unsat_parent_count": sum(r["result"] == "unsat" for r in records),
            "sat_parent_count": sum(r["result"] == "sat" for r in records),
            "unknown_parent_count": sum(r["result"] == "unknown" for r in records),
            "unresolved_parent_indices": unresolved,
            "records": records,
        },
        "soundness": {
            "finite_ring_unsat_is_necessary_obstruction": True,
            "finite_ring_sat_would_not_prove_exact_feasibility": True,
            "n1_partition_is_exhaustive": True,
            "n1_values": list(range(9)),
            "incremental_solver_history_used_for_credit": False,
            "timeouts_relabelled_unsat": False,
        },
        "credit": {
            "cut102_retained19_candidate_replayed": all_unsat,
            "cut103_local_scope_certificate_complete": all_unsat,
            "cut103_population_preimage_certificate_complete": False,
            "stage32_main_pruning_credit": False,
            "whole_first_block_unsat": False,
            "whole_stratum_closed": False,
            "full178_complete": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
        "next": {
            "id": "CUT190_RETAINED_CHECKPOINT_OR_BLOCKER_HANDOFF" if all_unsat else "CUT103_REPLAY_REPAIR",
            "cut104_required": False if all_unsat else None,
            "cut104_skip_reason": "finite-ring obstruction is excluding on the retained19 local scope; rational dual fallback is unnecessary unless the modular result stops replaying" if all_unsat else None,
        },
        "firewalls": {
            "unretained_172_identities_inferred": False,
            "n356_candidate_assumed_consumed": False,
            "main_authority_mutated": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status":status,"unsat":body["fresh_replay"]["unsat_parent_count"],"sat":body["fresh_replay"]["sat_parent_count"],"unknown":body["fresh_replay"]["unknown_parent_count"],"output":str(args.output)}))


if __name__ == "__main__":
    main()
