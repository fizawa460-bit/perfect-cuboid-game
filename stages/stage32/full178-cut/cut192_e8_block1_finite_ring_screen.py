#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from z3 import get_version_string

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(RESIDUAL))

import cut102_finite_ring_direct_completion_v2 as cut102
from compressed_terminal_indexer import CompressedTerminalIndexer

SCHEMA = "STAGE32_FULL178_CUT192_E8_BLOCK1_FINITE_RING_SCREEN_V1"
HANDOFF = HERE / "CUT192-EX5-E8-HANDOFF.json"
CUT191 = HERE / "CUT191-first-block-closure-checkpoint.json"
N356 = ROOT / "stages/stage32/32-01-178/nodes/N356/RESULT.json"
INDEXER = RESIDUAL / "compressed_terminal_indexer.py"
CUT102 = HERE / "cut102_finite_ring_direct_completion_v2.py"

LOCKS = {
    HANDOFF: "011fe82cd97bfa192d4efbbafacb21b0ea724b44",
    CUT191: "a90042ec931cb487ae6be852524db5a4537862f4",
    N356: "677b1ae2bab910db0805d20ee489d922522919ed",
    INDEXER: "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    CUT102: "fbdd1e65b509526d5198743208bff79bd2488673",
}
HANDOFF_CANONICAL = "41405165f081554bf3089c0cb15f568d8515fe81202cf6c809914c9490479d1c"
CUT191_CANONICAL = "1e681c456dc30342346d134f5e0d89150573f8a756cbd808c309d2af89821fdd"
N356_CANONICAL = "d1aecec8b78c78f03fa7b82b3dc136668f435d9cfb98636a1a23b704431abe31"
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
BLOCK_INDEX = 1
BLOCK_WIDTH = 113
EXPECTED_RANGE = [113, 225]
EXPECTED_BASE = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1]
EXPECTED_FIXED = {93: 0, 94: 0, 95: 0, 96: 1, 97: 0, 98: 0, 99: 1, 101: 1, 102: 0, 103: 0}
EXPECTED_GROUP_SUMS = [1, 1, 1]
DEFAULT_PRIMES = [2, 3, 5, 7, 11, 13, 17, 31, 127]


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit("FAIL: " + msg)


def checked(path: Path, canonical: str) -> dict:
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256_without_this_field", None)
    req(claimed == canonical and csha(body) == canonical, f"canonical drift: {path.relative_to(ROOT)}")
    return obj


def replay_population_boundary() -> tuple[dict, dict[int, int], list[int]]:
    for path, expected in LOCKS.items():
        req(blob(path) == expected, f"source-lock drift: {path.relative_to(ROOT)}")

    handoff = checked(HANDOFF, HANDOFF_CANONICAL)
    req(handoff["schema"] == "STAGE32_FULL178_CUT192_EX5_E8_HANDOFF_V1", "handoff schema drift")
    producer = handoff["producer"]
    req(producer["pr"] == 1776, "EX5 producer PR drift")
    req(producer["exact_head"] == "fd00531181228c9f367a49eb61ddc3af6ab84ab3", "EX5 producer head drift")
    req(producer["exact_head_ci_run"] == 34598945799, "EX5 exact-head CI provenance drift")
    req(handoff["artifact"]["id"] == 10263148684, "EX5 handoff artifact id drift")
    req(handoff["artifact"]["zip_sha256"] == "df48610fbf8d6cd11640f8f3feb534256b307e6ea803688267a33cb972cfba7f", "EX5 handoff artifact digest drift")
    req(handoff["artifact"]["raw_json_canonical_sha256"] == "7344a7c23ed83b66046d4a72a27a0679ab12fdc05cb41d8f6cdcacec6adcaa01", "EX5 handoff raw canonical drift")
    req(handoff["population"]["preferred_wave_block_count"] == 255, "EX5 preferred wave block count drift")
    req(handoff["population"]["preferred_wave_terminal_count"] == 28815, "EX5 preferred wave terminal count drift")

    idx = CompressedTerminalIndexer(8, 8)
    req(idx.normal_budget == 112 and idx.exceptional_count == 11318 and idx.terminal_count == 1278934, "e8 indexer universe drift")
    lo = BLOCK_INDEX * BLOCK_WIDTH
    hi = lo + BLOCK_WIDTH - 1
    req([lo, hi] == EXPECTED_RANGE, "block1 terminal range drift")
    base = tuple(int(v) for v in idx.unrank(lo))
    top = tuple(int(v) for v in idx.unrank(hi))
    req(list(base) == EXPECTED_BASE, "block1 base terminal drift")
    req(base[4] == 0 and top[4] == 112, "block1 x4 endpoint drift")
    req(base[:4] + base[5:] == top[:4] + top[5:], "block1 exceptional signature drift")
    req(idx.rank(base) == lo and idx.rank(top) == hi, "block1 rank/unrank replay drift")
    fixed = {label: int(v) for label, v in zip(ASSIGNMENT_ORDER, base) if label != 49}
    req(fixed == EXPECTED_FIXED, "block1 fixed exceptional pairings drift")
    group_sums = [
        sum(fixed[label] for label in [101, 102, 103]),
        sum(fixed[label] for label in [97, 98, 99]),
        sum(fixed[label] for label in [93, 94, 95, 96]),
    ]
    req(group_sums == EXPECTED_GROUP_SUMS, "block1 N355 group sums drift")

    b = handoff["first_disjoint_block"]
    req(b["block_index"] == 1 and b["terminal_rank_range"] == EXPECTED_RANGE and b["terminal_count"] == 113, "handoff block1 scope drift")
    req(b["base_terminal"] == EXPECTED_BASE, "handoff block1 base drift")
    req({int(k): int(v) for k, v in b["fixed_exceptional_pairings"].items()} == fixed, "handoff fixed-pairing replay drift")
    req(b["n355_group_sums"] == group_sums, "handoff N355 group-sum drift")
    req(b["hnf_feasible_parent_count"] == 2360, "handoff HNF parent count drift")
    req(b["hnf_parent_stream_sha256"] == "4977be767465c69616288b54bc79e491b3f8ee29c94162ce089a6258b6fc00e0", "handoff HNF parent stream drift")

    cut191 = checked(CUT191, CUT191_CANONICAL)
    req(cut191["population_preimage"]["first_block_rank_range"] == [0, 112], "CUT191 consumed range drift")
    req(cut191["coverage_certificate"]["whole_first_block_picard64_unsat"] is True, "CUT191 closure regression")
    req(EXPECTED_RANGE[0] > cut191["population_preimage"]["first_block_rank_range"][1], "CUT192 block overlaps CUT191")

    n356 = checked(N356, N356_CANONICAL)
    req(n356["transport_contract"]["even_degree_specialization"] == "b-c<=3*d-e", "N356 necessary cut drift")
    a, bb, c = group_sums
    rhs = 3 * 8 - 8
    req(bb - c <= rhs, "block1 unexpectedly rejected by consumed N356 cut")
    ctx = handoff["current_stage32_consumed_authority_context"]
    req(ctx["n356_consumed"] is True and ctx["cut191_consumed"] is True, "current consumed-authority context drift")
    req(ctx["block1_n356_replay"] == {"a": 1, "b": 1, "c": 1, "lhs_b_minus_c": 0, "rhs_3d_minus_e": 16, "preserved": True}, "handoff N356 overlap replay drift")
    req(ctx["authoritative_remaining_terminals"] == 65396964990500233636101, "V12 authority count drift")
    return handoff, fixed, group_sums


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--primes", default=",".join(map(str, DEFAULT_PRIMES)))
    ap.add_argument("--per-check-timeout-ms", type=int, default=3000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    primes = [int(v) for v in args.primes.split(",") if v.strip()]
    req(bool(primes), "at least one prime is required")
    req(args.per_check_timeout_ms > 0, "positive timeout required")

    handoff, fixed, group_sums = replay_population_boundary()

    # Reuse the already-audited CUT102 finite-ring mathematics. load_interface()
    # reconstructs the exact retained 140x64 Picard pairing geometry; only its
    # first-block fixed signature/parent list is discarded here.
    P, blocks, _exceptional_labels, _old_parents, _old_fixed = cut102.load_interface()

    records = []
    obstructing = None
    for prime in primes:
        solver, y, n1, linear = cut102.make_solver(P, blocks, fixed, prime, args.per_check_timeout_ms)
        rec = cut102.classify(solver, y, n1, True)
        rec = {**linear, **rec}
        records.append(rec)
        if rec["result"] == "unsat":
            obstructing = {"prime": prime, "method": rec["method"]}
            break

    all_sat = obstructing is None and all(r["result"] == "sat" for r in records) and len(records) == len(primes)
    any_unknown = any(r["result"] == "unknown" for r in records)
    if obstructing is not None:
        status = "CANDIDATE_BLOCK1_113_TERMINALS_FINITE_RING_UNSAT_AUDIT_REQUIRED"
        candidate = 113
    elif all_sat:
        status = "BOUNDED_BLOCK1_FINITE_RING_RELAXATIONS_SAT_NO_PRUNING_CREDIT"
        candidate = 0
    else:
        status = "BOUNDED_BLOCK1_FINITE_RING_SCREEN_NONEXCLUDING_NO_PRUNING_CREDIT"
        candidate = 0

    current = handoff["current_stage32_consumed_authority_context"]["authoritative_remaining_terminals"]
    body = {
        "schema": SCHEMA,
        "stage": "32",
        "surface": "full178-cut",
        "node": "CUT192",
        "status": status,
        "z3_version": get_version_string(),
        "source_locks": {
            "ex5_handoff_blob_sha1": LOCKS[HANDOFF],
            "ex5_handoff_canonical_sha256": HANDOFF_CANONICAL,
            "ex5_exact_head": handoff["producer"]["exact_head"],
            "ex5_exact_head_ci_run": handoff["producer"]["exact_head_ci_run"],
            "ex5_wave_artifact_id": handoff["artifact"]["id"],
            "ex5_wave_artifact_zip_sha256": handoff["artifact"]["zip_sha256"],
            "cut102_implementation_blob_sha1": LOCKS[CUT102],
            "compressed_terminal_indexer_blob_sha1": LOCKS[INDEXER],
            "cut191_checkpoint_blob_sha1": LOCKS[CUT191],
            "cut191_checkpoint_canonical_sha256": CUT191_CANONICAL,
            "n356_result_blob_sha1": LOCKS[N356],
            "n356_result_canonical_sha256": N356_CANONICAL,
        },
        "target": {
            "row_id": "g1-d008",
            "g": 1,
            "d": 8,
            "e": 8,
            "block_index": 1,
            "terminal_rank_range": EXPECTED_RANGE,
            "terminal_count": 113,
            "fixed_exceptional_pairings": {str(k): v for k, v in sorted(fixed.items())},
            "n355_group_sums": group_sums,
            "hnf_feasible_parent_count_from_ex5_handoff": 2360,
            "hnf_parent_stream_sha256": handoff["first_disjoint_block"]["hnf_parent_stream_sha256"],
            "disjoint_from_consumed_cut191": True,
            "preserved_by_consumed_n356": True,
        },
        "method": {
            "screen": "whole fixed-signature finite-ring relaxation before HNF-parent descent",
            "necessity": "Every exact Picard64 completion of every terminal in ranks 113..225 satisfies the fixed exceptional signature and all CUT102 finite-ring necessary constraints. Therefore whole-relaxation UNSAT excludes the full 113-terminal block; SAT/UNKNOWN grants no feasibility or pruning credit.",
            "primes_requested": primes,
            "per_check_timeout_ms": args.per_check_timeout_ms,
            "partition_n1_on_unknown": True,
        },
        "result": {
            "obstructing_prime": obstructing,
            "prime_records": records,
            "all_requested_relaxations_sat": all_sat,
            "any_unknown": any_unknown,
            "cut192_pruning_candidate_terminals": candidate,
            "candidate_remaining_terminals_if_later_audited_and_consumed": current - candidate,
        },
        "credit": {
            "cut192_pruning_candidate_terminals": candidate,
            "hostile_audit_passed": False,
            "stage32_main_pruning_credit": False,
            "whole_stratum_closed": False,
            "full178_complete": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
        "next": {
            "if_whole_block_unsat": "freeze exact-head retained checkpoint then external stage32cut-audit; MAIN consumption remains separate",
            "if_nonexcluding": "descend to the 2360 source-locked HNF-feasible parents from the EX5 handoff before widening to the 255-block wave",
        },
        "firewalls": {
            "ex5_adapter_rebuilt_by_cut": False,
            "n357_duplicated": False,
            "sat_promoted_to_exact_feasibility": False,
            "unknown_promoted_to_unsat": False,
            "main_authority_mutated": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": status,
        "block_index": 1,
        "terminal_count": 113,
        "candidate": candidate,
        "obstructing_prime": obstructing,
        "all_sat": all_sat,
        "any_unknown": any_unknown,
        "output": str(args.output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
