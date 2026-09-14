#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESULT = HERE / "CUT194-e8-common-adapter-wave2-result.json"
HANDOFF = HERE / "CUT194-e8-common-adapter-wave2-audit-handoff.json"
ACTIVE_RUNKEY = HERE / "runkeys/CUT194-e8-wave2.json"
EXECUTED_RUNKEY = HERE / "CUT194-e8-wave2-executed-runkey.json"
EXECUTED_WORKFLOW = HERE / "CUT194-e8-wave2-executed-workflow.yml"
WORKER = HERE / "cut194_e8_common_adapter_wave2.py"
AGGREGATOR = HERE / "aggregate_cut194_e8_wave2.py"
PREFLIGHT = HERE / "CUT194-e8-common-adapter-wave2-preflight.json"
CUT193_VERIFY = HERE / "verify_cut193_e8_common_adapter_wave1.py"

RESULT_CANONICAL = "c63f6da3dd0ec443572f8561bb7774491ce7d7c09ce319a322fb52e5b1e08cd4"
HANDOFF_CANONICAL = "273ceb4cf9fba64023f9dcb5f0ab11342f4e6f1d71b5dd8574e75e886c3be4f9"
EXPECTED_CLOSED = 234
EXPECTED_PRUNED = 26442
EXPECTED_RESIDUAL = [355,406,462,463,464,469,475,490,492,496,501,546,547,552,572,602,617,672,673,678,698]
PRIMES = [2,3,5,7,11,13,17,31,127]

LOCKS = {
    RESULT: "dab1a28f55918b617112799f11ac9614eb8a481c",
    HANDOFF: "7585f93df035b928ebfbad733ccf501125d57e08",
    ACTIVE_RUNKEY: "02d1bb648cc5d09c68e499e01fc2ac7c314bc855",
    EXECUTED_RUNKEY: "75e43a7db76e5fee81295aa211e0330a8ada0dc9",
    EXECUTED_WORKFLOW: "396b639bf3549714d81c3a08666e3591088b3f4f",
    WORKER: "0da85e6e3092c04de3ad85f0b9d151628a0a4eb5",
    AGGREGATOR: "b35a611822e61800f328dbcd775a3a008b607a09",
    PREFLIGHT: "c78158c0e048253185bc51f854cd0eca0ec2b970",
}

def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit("FAIL: " + msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def checked_canonical(path: Path, expected: str) -> dict:
    o = json.loads(path.read_text())
    q = dict(o)
    claimed = q.pop("canonical_sha256_without_this_field", None)
    req(claimed == expected and csha(q) == expected, f"canonical drift: {path.name}")
    return o

def main() -> None:
    for path, expected in LOCKS.items():
        req(path.exists(), f"missing source-lock {path.name}")
        req(blob(path) == expected, f"source-lock drift {path.name}")

    subprocess.run([sys.executable, str(CUT193_VERIFY)], cwd=ROOT, check=True)

    result = checked_canonical(RESULT, RESULT_CANONICAL)
    handoff = checked_canonical(HANDOFF, HANDOFF_CANONICAL)
    rk = json.loads(ACTIVE_RUNKEY.read_text())
    req(rk.get("armed") is False and rk.get("consumed") is True, "CUT194 active runkey not consumed/disarmed")
    req(rk.get("consumed_by", {}).get("workflow_run_id") == 34614132290, "CUT194 workflow run mismatch")
    req(rk.get("consumed_by", {}).get("aggregate_artifact_id") == 10269359977, "CUT194 aggregate artifact mismatch")

    sys.path.insert(0, str(HERE))
    import cut194_e8_common_adapter_wave2 as cut
    base = cut.base
    cut.preflight()

    survivors = base.e8.current_main_survivor_block_indices()
    wave = survivors[256:511]
    req(len(wave) == 255 and 0 not in wave, "wave2 population drift")
    req(set(wave).isdisjoint(set(survivors[1:256])), "wave2 overlaps CUT193 wave1")
    bh = hashlib.sha256()
    for i in wave:
        bh.update(f"{i}\n".encode())
    req(bh.hexdigest() == result["target"]["block_index_stream_sha256"], "wave2 block stream drift")
    req(result["target"]["block_indices"] == wave, "retained target population drift")

    closed = [int(v) for v in result["result"]["candidate_closed_block_indices"]]
    closed_set = set(closed)
    residual = sorted(set(wave) - closed_set)
    req(len(closed) == EXPECTED_CLOSED and len(closed_set) == EXPECTED_CLOSED, "closed block count/uniqueness drift")
    req(residual == EXPECTED_RESIDUAL, "residual identity drift")
    req(result["result"]["candidate_pruned_terminals"] == EXPECTED_PRUNED == 113 * EXPECTED_CLOSED, "terminal accounting drift")
    req(result["result"]["remaining_nonclosed_block_count"] == 21, "residual count drift")
    req(result["result"]["method_counts"] == {
        "ALL_HNF_PARENTS_FINITE_RING_UNSAT": 17,
        "FINITE_RING_NONCLOSING_RESIDUAL_PARENTS": 21,
        "WHOLE_BLOCK_FINITE_RING_UNSAT": 217,
    }, "executed method provenance drift")
    req(result["credit"]["stage32_main_pruning_credit"] is False, "MAIN credit leak")
    req(result["credit"]["cut194_pruning_credit"] is False, "CUT194 self-credit leak")
    req(result["firewalls"]["hostile_audit_required"] is True, "hostile audit firewall drift")

    P, blocks, g = base.load_picard_interface()
    solvers = {p: base.make_solver(P, blocks, p, 5000) for p in PRIMES}
    fresh_whole = []
    fresh_hnf_empty = []
    fresh_parent = []
    fresh_parent_checks = 0
    unknown_checks = 0

    for block_index in closed:
        sig = base.e8.block_signature(block_index)
        req(sig["current_main_audited_prefix_survivor"] is True, f"block {block_index} lost audited prefix survival")
        sums = [int(v) for v in sig["n355_known_group_sums"]]
        req(max(sums) <= 4 and sums[1] - sums[2] <= 4 <= 16, f"N356 bridge drift on block {block_index}")
        fixed_terminal = {int(k): int(v) for k, v in sig["fixed_exceptional_pairings"].items()}

        whole_closed = False
        for p in PRIMES:
            s, y, _ = solvers[p]
            status, _reason = base.check_with_fixed(s, y, fixed_terminal)
            if status == "unsat":
                whole_closed = True
                fresh_whole.append(block_index)
                break
            if status == "unknown":
                unknown_checks += 1
        if whole_closed:
            continue

        parents = list(base.e8.iter_parent_population(block_index, g))
        if not parents:
            fresh_hnf_empty.append(block_index)
            continue

        for ordinal, rec in enumerate(parents):
            fresh_parent_checks += 1
            fixed = {int(label): int(value) for label, value in zip(g.exceptional_labels, rec["selected_exceptional_pairings"])}
            parent_closed = False
            for p in PRIMES:
                s, y, _ = solvers[p]
                status, _reason = base.check_with_fixed(s, y, fixed)
                if status == "unsat":
                    parent_closed = True
                    break
                if status == "unknown":
                    unknown_checks += 1
            req(parent_closed, f"credited block {block_index} parent {ordinal} survives fresh finite-ring replay")
        fresh_parent.append(block_index)

    replay = set(fresh_whole) | set(fresh_hnf_empty) | set(fresh_parent)
    req(replay == closed_set, "fresh replay did not recover exact credited set")
    req(handoff["result"]["candidate_closed_block_count"] == EXPECTED_CLOSED, "handoff count drift")
    req(handoff["result"]["candidate_pruned_terminals"] == EXPECTED_PRUNED, "handoff terminal drift")
    req(handoff["result"]["residual_blocks"] == EXPECTED_RESIDUAL, "handoff residual drift")
    req(handoff["audit"]["hostile_audit_passed"] is False, "handoff self-audit leak")
    req(handoff["credit"]["stage32_main_pruning_credit"] is False, "handoff MAIN credit leak")

    print(json.dumps({
        "status": "PASS_CUT194_EXACT_HEAD_AUDIT_VERIFIER",
        "wave_blocks": 255,
        "candidate_closed_blocks": EXPECTED_CLOSED,
        "candidate_pruned_terminals": EXPECTED_PRUNED,
        "fresh_whole_block_finite_ring_unsat": len(fresh_whole),
        "fresh_hnf_empty": len(fresh_hnf_empty),
        "fresh_all_hnf_parents_finite_ring_unsat_blocks": len(fresh_parent),
        "fresh_hnf_parents_checked": fresh_parent_checks,
        "unknown_checks_not_promoted": unknown_checks,
        "remaining_nonclosed_blocks": 21,
        "stage32_main_pruning_credit": False,
        "hostile_audit_passed": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
