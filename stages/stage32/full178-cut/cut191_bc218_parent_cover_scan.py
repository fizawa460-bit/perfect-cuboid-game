#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from sympy import Matrix
from z3 import Int, SolverFor, Sum, get_version_string, sat, unknown, unsat

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EX5 = ROOT / "stages/stage32-ex5/breadth-cycle-2"
sys.path.insert(0, str(HERE))

import cut102_finite_ring_direct_completion_v2 as cut102

SCHEMA = "STAGE32_FULL178_CUT191_BC218_PARENT_COVER_SCAN_V1"
EXPECTED_CUT102_BLOB = "fbdd1e65b509526d5198743208bff79bd2488673"
BC219 = EX5 / "bc2-19-n354-survivor-normal-positivity-mass-checkpoint.json"
EXPECTED_BC219_BLOB = "7d75a46a3dc0f54b60b0d70aa2240882b516de59"
EXPECTED_BC219_CANONICAL = "62e97cdb8bd6a8d14c0ac176576bd2cf2ec51020295f8703cbefc3bc85f001eb"
EXPECTED_PARENT_COUNT = 7336
NORMAL_COUNT = 92
PICARD_RANK = 64
NORMAL_MASS = 112
TARGET_E = 8
TARGET_D = 8


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def canonical_replay(path: Path, expected: str) -> None:
    payload = json.loads(path.read_text())
    if payload.get("canonical_sha256_without_this_field") != expected:
        raise ValueError(f"canonical field moved: {path}")
    body = dict(payload)
    body.pop("canonical_sha256_without_this_field", None)
    if csha(body) != expected:
        raise ValueError(f"canonical replay moved: {path}")


def make_exact_solver(P: Matrix, blocks, fixed: dict[int, int], strong: bool, timeout_ms: int):
    x = [Int(f"x_{'strong' if strong else 'weak'}_{j}") for j in range(PICARD_RANK)]
    p = [
        Sum([int(P[i, j]) * x[j] for j in range(PICARD_RANK)])
        for i in range(P.rows)
    ]
    s = SolverFor("QF_LIA")
    s.set(timeout=timeout_ms)
    for i in range(NORMAL_COUNT):
        s.add(p[i] >= 0, p[i] <= NORMAL_MASS)
    for i in range(NORMAL_COUNT, 140):
        s.add(p[i] >= 0, p[i] <= TARGET_E)
    s.add(Sum(p[:NORMAL_COUNT]) == NORMAL_MASS)
    s.add(Sum(p[NORMAL_COUNT:]) == TARGET_E)
    for label, value in fixed.items():
        s.add(p[label - 1] == value)

    if strong:
        fibre = []
        for pack, factor_blocks in zip(cut102.PACKS, blocks):
            vals = [
                2 * p[b - 1] + Sum([p[j - 1] for j in block])
                for b, block in zip(pack, factor_blocks)
            ]
            for v in vals[1:]:
                s.add(v == vals[0])
            fibre.append(vals[0])
        n1, n2 = fibre
        s.add(n1 + n2 == TARGET_D)
        s.add(n1 >= 0, n1 <= TARGET_D, n2 >= 0, n2 <= TARGET_D)
        for label in range(93, 141):
            s.add(p[label - 1] <= TARGET_D // 2)
        for block1 in blocks[0]:
            a = Sum([p[j - 1] for j in block1])
            for block2 in blocks[1]:
                s.add(a + Sum([p[j - 1] for j in block2]) <= TARGET_D)
    return s, p


def check_parent(s, p, exceptional_labels: list[int], yE: list[int]):
    s.push()
    for label, value in zip(exceptional_labels, yE):
        s.add(p[label - 1] == int(value))
    r = s.check()
    reason = s.reason_unknown() if r == unknown else None
    s.pop()
    return r, reason


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--end", type=int, required=True)
    ap.add_argument("--weak-timeout-ms", type=int, default=500)
    ap.add_argument("--strong-timeout-ms", type=int, default=1000)
    ap.add_argument("--mod2-timeout-ms", type=int, default=1000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if not (0 <= args.start < args.end <= EXPECTED_PARENT_COUNT):
        raise ValueError("invalid parent range")
    if min(args.weak_timeout_ms, args.strong_timeout_ms, args.mod2_timeout_ms) <= 0:
        raise ValueError("timeouts must be positive")

    if cut102.git_blob_sha(Path(cut102.__file__).resolve()) != EXPECTED_CUT102_BLOB:
        raise ValueError("CUT102 implementation source lock moved")
    if cut102.git_blob_sha(BC219) != EXPECTED_BC219_BLOB:
        raise ValueError("BC2-19 checkpoint blob moved")
    canonical_replay(BC219, EXPECTED_BC219_CANONICAL)
    bc219 = json.loads(BC219.read_text())
    if bc219["result"]["input_mod8_parent_count"] != EXPECTED_PARENT_COUNT:
        raise ValueError("BC2-19 parent count regression")
    if bc219["result"]["unsat_count"] != 7100 or bc219["result"]["unknown_count"] != 236 or bc219["result"]["sat_count"] != 0:
        raise ValueError("BC2-19 historical status-count regression")
    if not bc219["interpretation"]["bc2_18_parent_union_exhaustively_addressed_by_attempt"]:
        raise ValueError("BC2-19 exhaustive-union contract regression")

    P, blocks, exceptional_labels, parents, fixed = cut102.load_interface()
    if len(parents) != EXPECTED_PARENT_COUNT:
        raise ValueError("BC2-18 parent replay count regression")

    weak, weak_p = make_exact_solver(P, blocks, fixed, False, args.weak_timeout_ms)
    strong, strong_p = make_exact_solver(P, blocks, fixed, True, args.strong_timeout_ms)
    mod2, mod2_y, _n1, mod2_meta = cut102.make_solver(P, blocks, fixed, 2, args.mod2_timeout_ms)

    counts = {
        "weak_exact_unsat": 0,
        "strong_exact_unsat": 0,
        "mod2_unsat": 0,
        "residual_strong_sat": 0,
        "residual_mod2_sat": 0,
        "residual_unknown": 0,
    }
    residual = []
    status_stream = hashlib.sha256()

    for parent_index in range(args.start, args.end):
        yE, _allowed = parents[parent_index]
        wr, wreason = check_parent(weak, weak_p, exceptional_labels, yE)
        if wr == unsat:
            counts["weak_exact_unsat"] += 1
            status_stream.update(f"{parent_index}:WEAK_EXACT_UNSAT\n".encode())
            continue

        sr, sreason = check_parent(strong, strong_p, exceptional_labels, yE)
        if sr == unsat:
            counts["strong_exact_unsat"] += 1
            status_stream.update(f"{parent_index}:STRONG_EXACT_UNSAT\n".encode())
            continue

        mod2.push()
        for label, value in zip(exceptional_labels, yE):
            mod2.add(mod2_y[label - 1] == int(value))
        mr = mod2.check()
        mreason = mod2.reason_unknown() if mr == unknown else None
        mod2.pop()
        if mr == unsat:
            counts["mod2_unsat"] += 1
            status_stream.update(f"{parent_index}:MOD2_UNSAT\n".encode())
            continue

        if sr == sat:
            kind = "residual_strong_sat"
        elif mr == sat:
            kind = "residual_mod2_sat"
        else:
            kind = "residual_unknown"
        counts[kind] += 1
        rec = {
            "parent_index": parent_index,
            "weak_exact": str(wr),
            "strong_exact": str(sr),
            "mod2": str(mr),
        }
        if wreason is not None:
            rec["weak_reason_unknown"] = wreason
        if sreason is not None:
            rec["strong_reason_unknown"] = sreason
        if mreason is not None:
            rec["mod2_reason_unknown"] = mreason
        residual.append(rec)
        status_stream.update(
            f"{parent_index}:RESIDUAL:{str(wr)}:{str(sr)}:{str(mr)}\n".encode()
        )

    checked = args.end - args.start
    covered = counts["weak_exact_unsat"] + counts["strong_exact_unsat"] + counts["mod2_unsat"]
    if covered + len(residual) != checked:
        raise ValueError("coverage accounting regression")

    body = {
        "schema": SCHEMA,
        "stage": "32",
        "surface": "full178-cut",
        "node": "CUT191",
        "status": "PASS_SHARD_ALL_PARENTS_OBSTRUCTED" if not residual else "BLOCKED_SHARD_RESIDUAL_REMAINS",
        "source_locks": {
            "cut102_implementation_blob": EXPECTED_CUT102_BLOB,
            "bc2_19_checkpoint_blob": EXPECTED_BC219_BLOB,
            "bc2_19_checkpoint_canonical": EXPECTED_BC219_CANONICAL,
            "bc2_18_feasible_stream_sha256": cut102.EXPECTED_STREAM,
            "bc2_18_parent_count": EXPECTED_PARENT_COUNT,
        },
        "scope": {
            "parent_index_start_inclusive": args.start,
            "parent_index_end_exclusive": args.end,
            "parents_checked": checked,
            "bc2_18_parent_union_meaning": "source-locked exact selected-exceptional completion-parent decomposition for the g1-d008/e8 first block x4=0..112",
            "historical_bc2_19_unknown_identity_reconstruction_used": False,
            "bc2_25_identity_refinement_used": False,
        },
        "methods": {
            "weak_exact": "exact Picard64 integer image + all140 nonnegative + normal/exceptional mass + terminal and parent selected-exceptional pairings",
            "strong_exact": "weak exact plus two fibre equalities, n1+n2=d, exceptional diagonal caps, and all cross-factor block-sum caps",
            "mod2": "left-kernel mod-2 necessary image relaxation plus the same strong bounded mass/fibre/diagonal/block constraints",
            "soundness": "Only UNSAT is covering credit. SAT and UNKNOWN remain residual. No timeout is relabelled UNSAT.",
        },
        "solver": {
            "z3_version": get_version_string(),
            "weak_timeout_ms": args.weak_timeout_ms,
            "strong_timeout_ms": args.strong_timeout_ms,
            "mod2_timeout_ms": args.mod2_timeout_ms,
            "mod2_rank": mod2_meta["rank_mod_p"],
            "mod2_left_kernel_dimension": mod2_meta["left_kernel_dimension"],
        },
        "result": {
            "counts": counts,
            "covered_parent_count": covered,
            "residual_parent_count": len(residual),
            "residual_records": residual,
            "status_stream_sha256": status_stream.hexdigest(),
        },
        "credit": {
            "shard_parent_cover_complete": not residual,
            "whole_bc2_18_parent_union_closed": False,
            "whole_first_block_unsat": False,
            "stage32_main_pruning_credit": False,
            "full178_complete": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
        "firewalls": {
            "historical_236_identity_set_assumed_stable": False,
            "unretained_172_identities_inferred": False,
            "bc2_25_identity_refinement_performed": False,
            "n356_candidate_assumed_consumed": False,
            "main_authority_mutated": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": body["status"], "start": args.start, "end": args.end, "covered": covered, "residual": len(residual), "counts": counts}, sort_keys=True))


if __name__ == "__main__":
    main()
