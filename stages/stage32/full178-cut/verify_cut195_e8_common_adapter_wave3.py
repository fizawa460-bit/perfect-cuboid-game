#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESULT = HERE / "CUT195-e8-common-adapter-wave3-result.json"
HANDOFF = HERE / "CUT195-e8-common-adapter-wave3-audit-handoff.json"
ACTIVE_RUNKEY = HERE / "runkeys/CUT195-e8-wave3.json"
EXECUTED_RUNKEY = HERE / "CUT195-e8-wave3-executed-runkey.json"
EXECUTED_WORKFLOW = HERE / "CUT195-e8-wave3-executed-workflow.yml"
WORKER = HERE / "cut195_e8_common_adapter_wave3.py"
AGGREGATOR = HERE / "aggregate_cut195_e8_wave3.py"
PREFLIGHT = HERE / "CUT195-e8-common-adapter-wave3-preflight.json"
CUT194_VERIFY = HERE / "verify_cut194_e8_common_adapter_wave2.py"

RESULT_CANONICAL = "1a7d802f427761d304ee06451d00ea67a1365d7d2629cdbf2ac88b6b4ff08aed"
HANDOFF_CANONICAL = "97066158e784302333bb57c5a015ee26926a760a9c6f7f123dfed1caa4e37146"
EXPECTED_CLOSED = 232
EXPECTED_PRUNED = 26216
EXPECTED_RESIDUAL = [728,737,798,924,925,926,931,932,933,937,942,952,958,973,978,1008,1010,1014,1015,1029,1064,1065,1069]
PRIMES = [2,3,5,7,11,13,17,31,127]

LOCKS = {
    RESULT: "d9fe913dccd41446780dbdde9f0200970ee9129e",
    HANDOFF: "e449c1ef0b6180694f02fc4ae6ab083e2a934b26",
    ACTIVE_RUNKEY: "9345a3e53d8641d7fd322c48a78999cebaa0e9d0",
    EXECUTED_RUNKEY: "9cb839252679d896da82d76568540e69d55a378d",
    EXECUTED_WORKFLOW: "bcd127e50077ee771fabe22ad596fa0972400d3e",
    WORKER: "9f42f23272e1fc52097a0eb372cfc4dfa7d534c9",
    AGGREGATOR: "16151c4235631d03355f89417a827ea914fb6af6",
    PREFLIGHT: "0f60cad3fd9c02b84fb33be42d6b1435bf85e906",
    CUT194_VERIFY: "ea0100b8a40397243d784d552d7e406e46443767",
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

    subprocess.run([sys.executable, str(CUT194_VERIFY)], cwd=ROOT, check=True)

    result = checked_canonical(RESULT, RESULT_CANONICAL)
    handoff = checked_canonical(HANDOFF, HANDOFF_CANONICAL)
    rk = json.loads(ACTIVE_RUNKEY.read_text())
    exrk = json.loads(EXECUTED_RUNKEY.read_text())
    req(rk.get("generation") == 2 and rk.get("armed") is False and rk.get("consumed") is True, "CUT195 active runkey not generation2 consumed/disarmed")
    req(rk.get("consumed_by", {}).get("workflow_run_id") == 34659443498, "CUT195 workflow run mismatch")
    req(rk.get("consumed_by", {}).get("aggregate_job_id") == 103469696751, "CUT195 aggregate job mismatch")
    req(rk.get("consumed_by", {}).get("aggregate_artifact_id") == 10288091951, "CUT195 aggregate artifact mismatch")
    req(rk.get("consumed_by", {}).get("compute_exact_head") == "4127895e67922c381abe859c299029c3c258da0d", "CUT195 compute exact head mismatch")
    req(exrk.get("generation") == 2 and exrk.get("armed") is True and exrk.get("consumed") is False, "executed runkey snapshot drift")

    sys.path.insert(0, str(HERE))
    import cut195_e8_common_adapter_wave3 as cut
    core = cut.core
    cut.preflight()

    survivors = core.e8.current_main_survivor_block_indices()
    wave = survivors[511:766]
    req(len(wave) == 255 and 0 not in wave, "wave3 population drift")
    req(set(wave).isdisjoint(set(survivors[0:511])), "wave3 overlaps CUT191/CUT193/CUT194 prior offsets")
    bh = hashlib.sha256()
    for i in wave:
        bh.update(f"{i}\n".encode())
    req(bh.hexdigest() == result["target"]["block_index_stream_sha256"], "wave3 block stream drift")
    req(result["target"]["block_indices"] == wave, "retained target population drift")

    closed = [int(v) for v in result["result"]["candidate_closed_block_indices"]]
    closed_set = set(closed)
    residual = sorted(set(wave) - closed_set)
    req(len(closed) == EXPECTED_CLOSED and len(closed_set) == EXPECTED_CLOSED, "closed block count/uniqueness drift")
    req(residual == EXPECTED_RESIDUAL, "residual identity drift")
    req(result["result"]["candidate_pruned_terminals"] == EXPECTED_PRUNED == 113 * EXPECTED_CLOSED, "terminal accounting drift")
    req(result["result"]["remaining_nonclosed_block_count"] == 23, "residual count drift")
    req(result["result"]["method_counts"] == {
        "ALL_HNF_PARENTS_FINITE_RING_UNSAT": 18,
        "FINITE_RING_NONCLOSING_RESIDUAL_PARENTS": 23,
        "WHOLE_BLOCK_FINITE_RING_UNSAT": 214,
    }, "executed method provenance drift")
    req(result["credit"]["stage32_main_pruning_credit"] is False, "MAIN credit leak")
    req(result["credit"]["cut195_pruning_credit"] is False, "CUT195 self-credit leak")
    req(result["firewalls"]["hostile_audit_required"] is True, "hostile audit firewall drift")

    P, blocks, g = core.load_picard_interface()
    solvers = {p: core.make_solver(P, blocks, p, 5000) for p in PRIMES}
    fresh_whole = []
    fresh_hnf_empty = []
    fresh_parent = []
    fresh_parent_checks = 0
    unknown_checks = 0

    for block_index in closed:
        sig = core.e8.block_signature(block_index)
        req(sig["current_main_audited_prefix_survivor"] is True, f"block {block_index} lost audited prefix survival")
        sums = [int(v) for v in sig["n355_known_group_sums"]]
        req(max(sums) <= 4 and sums[1] - sums[2] <= 4 <= 16, f"N356 bridge drift on block {block_index}")
        fixed_terminal = {int(k): int(v) for k, v in sig["fixed_exceptional_pairings"].items()}

        whole_closed = False
        for p in PRIMES:
            s, y, _ = solvers[p]
            status, _reason = core.check_with_fixed(s, y, fixed_terminal)
            if status == "unsat":
                whole_closed = True
                fresh_whole.append(block_index)
                break
            if status == "unknown":
                unknown_checks += 1
        if whole_closed:
            continue

        parents = list(core.e8.iter_parent_population(block_index, g))
        if not parents:
            fresh_hnf_empty.append(block_index)
            continue

        for ordinal, rec in enumerate(parents):
            fresh_parent_checks += 1
            fixed = {int(label): int(value) for label, value in zip(g.exceptional_labels, rec["selected_exceptional_pairings"])}
            parent_closed = False
            for p in PRIMES:
                s, y, _ = solvers[p]
                status, _reason = core.check_with_fixed(s, y, fixed)
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
        "status": "PASS_CUT195_EXACT_HEAD_AUDIT_VERIFIER",
        "wave_blocks": 255,
        "candidate_closed_blocks": EXPECTED_CLOSED,
        "candidate_pruned_terminals": EXPECTED_PRUNED,
        "fresh_whole_block_finite_ring_unsat": len(fresh_whole),
        "fresh_hnf_empty": len(fresh_hnf_empty),
        "fresh_all_hnf_parents_finite_ring_unsat_blocks": len(fresh_parent),
        "fresh_hnf_parents_checked": fresh_parent_checks,
        "unknown_checks_not_promoted": unknown_checks,
        "remaining_nonclosed_blocks": 23,
        "stage32_main_pruning_credit": False,
        "hostile_audit_passed": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
