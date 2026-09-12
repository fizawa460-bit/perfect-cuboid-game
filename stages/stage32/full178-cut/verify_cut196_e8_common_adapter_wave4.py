#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESULT = HERE / "CUT196-e8-common-adapter-wave4-result.json"
HANDOFF = HERE / "CUT196-e8-common-adapter-wave4-audit-handoff.json"
ACTIVE_RUNKEY = HERE / "runkeys/CUT196-e8-wave4.json"
EXECUTED_RUNKEY = HERE / "CUT196-e8-wave4-executed-runkey.json"
EXECUTED_WORKFLOW = HERE / "CUT196-e8-wave4-executed-workflow.yml"
WORKER = HERE / "cut196_e8_common_adapter_wave4.py"
AGGREGATOR = HERE / "aggregate_cut196_e8_wave4.py"
PREFLIGHT = HERE / "CUT196-e8-common-adapter-wave4-preflight.json"
CUT195_VERIFY = HERE / "verify_cut195_e8_common_adapter_wave3.py"

RESULT_CANONICAL = "194a37f87355f781f9aca341f9935645d818d5daa1c377883606627c80558a92"
HANDOFF_CANONICAL = "017e238704377f3ffca8adda1bab1d54254f6ecfe610e75ad9adae576b159994"
EXPECTED_CLOSED = 242
EXPECTED_PRUNED = 27346
EXPECTED_RESIDUAL = [1134,1140,1141,1145,1155,1190,1195,1209,1260,1261,1265,1386,1405]
PRIMES = [2,3,5,7,11,13,17,31,127]

LOCKS = {
    RESULT: "ae23ce6c44f69f9b2abe15e5aff09c2a10c45fde",
    HANDOFF: "d92a3369851accad0e14b4f34ef0c746a188a38a",
    ACTIVE_RUNKEY: "fd11b72dd52511cbb86a1c209f8f0ab50a180357",
    EXECUTED_RUNKEY: "a5d9f4a146c3a49958330ca54be6dd9ba59dca7b",
    EXECUTED_WORKFLOW: "d19a40b93bc72aedb09c9a95f9c62b96933b1c12",
    WORKER: "b458556ffcb895f1d05011847935b7cc1ac1f21f",
    AGGREGATOR: "86049f617b28f99eb600480272eeddecfd3d9998",
    PREFLIGHT: "1375420604bed13c72cc5cd8fd389ed2b006d3b4",
    CUT195_VERIFY: "022a8733eae7763926848b5e8bcf7f54f69bee66",
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

    subprocess.run([sys.executable, str(CUT195_VERIFY)], cwd=ROOT, check=True)

    result = checked_canonical(RESULT, RESULT_CANONICAL)
    handoff = checked_canonical(HANDOFF, HANDOFF_CANONICAL)
    rk = json.loads(ACTIVE_RUNKEY.read_text())
    exrk = json.loads(EXECUTED_RUNKEY.read_text())

    req(rk.get("generation") == 2 and rk.get("armed") is False and rk.get("consumed") is True,
        "CUT196 active runkey not generation2 consumed/disarmed")
    cb = rk.get("consumed_by", {})
    req(cb.get("workflow_run_id") == 34680928708, "CUT196 workflow run mismatch")
    req(cb.get("integrity_job_id") == 103519300939, "CUT196 integrity job mismatch")
    req(cb.get("aggregate_job_id") == 103522934349, "CUT196 aggregate job mismatch")
    req(cb.get("aggregate_artifact_id") == 10294446124, "CUT196 aggregate artifact mismatch")
    req(cb.get("aggregate_artifact_digest") == "sha256:9fa1beb6d2f9ad42072b1788c4f8467d2aee0a25e4e566645686c7e06f652ef3",
        "CUT196 aggregate digest mismatch")
    req(cb.get("compute_exact_head") == "5403328470df32c65aea9a38efe3916cb87d24a4",
        "CUT196 compute exact head mismatch")
    req(exrk.get("generation") == 2 and exrk.get("armed") is True and exrk.get("consumed") is False,
        "executed generation2 runkey snapshot drift")

    sys.path.insert(0, str(HERE))
    import cut196_e8_common_adapter_wave4 as cut
    core = cut.core
    cut.preflight()

    survivors = core.e8.current_main_survivor_block_indices()
    wave = survivors[766:1021]
    req(len(wave) == 255 and 0 not in wave, "wave4 population drift")
    req(set(wave).isdisjoint(set(survivors[0:766])), "wave4 overlaps prior CUT offsets")
    bh = hashlib.sha256()
    for i in wave:
        bh.update(f"{i}\n".encode())
    req(bh.hexdigest() == result["target"]["block_index_stream_sha256"], "wave4 block stream drift")
    req(result["target"]["block_indices"] == wave, "retained wave4 target population drift")

    closed = [int(v) for v in result["result"]["candidate_closed_block_indices"]]
    closed_set = set(closed)
    residual = sorted(set(wave) - closed_set)
    req(len(closed) == EXPECTED_CLOSED and len(closed_set) == EXPECTED_CLOSED,
        "closed block count/uniqueness drift")
    req(residual == EXPECTED_RESIDUAL, "residual identity drift")
    req(result["result"]["candidate_pruned_terminals"] == EXPECTED_PRUNED == 113 * EXPECTED_CLOSED,
        "terminal accounting drift")
    req(result["result"]["remaining_nonclosed_block_count"] == 13, "residual count drift")
    req(result["result"]["method_counts"] == {
        "ALL_HNF_PARENTS_FINITE_RING_UNSAT": 11,
        "FINITE_RING_NONCLOSING_RESIDUAL_PARENTS": 13,
        "HNF_PARENT_POPULATION_EMPTY": 1,
        "WHOLE_BLOCK_FINITE_RING_UNSAT": 230,
    }, "executed method provenance drift")
    req(result["credit"]["stage32_main_pruning_credit"] is False, "MAIN credit leak")
    req(result["credit"]["cut196_pruning_credit"] is False, "CUT196 self-credit leak")
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
        req(sig["current_main_audited_prefix_survivor"] is True,
            f"block {block_index} lost audited prefix survival")
        sums = [int(v) for v in sig["n355_known_group_sums"]]
        req(max(sums) <= 4 and sums[1] - sums[2] <= 4 <= 16,
            f"N356 bridge drift on block {block_index}")
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
            fixed = {int(label): int(value) for label, value in zip(
                g.exceptional_labels, rec["selected_exceptional_pairings"])}
            parent_closed = False
            for p in PRIMES:
                s, y, _ = solvers[p]
                status, _reason = core.check_with_fixed(s, y, fixed)
                if status == "unsat":
                    parent_closed = True
                    break
                if status == "unknown":
                    unknown_checks += 1
            req(parent_closed,
                f"credited block {block_index} parent {ordinal} survives fresh finite-ring replay")
        fresh_parent.append(block_index)

    replay = set(fresh_whole) | set(fresh_hnf_empty) | set(fresh_parent)
    req(replay == closed_set, "fresh replay did not recover exact credited set")

    req(handoff["result"]["candidate_closed_block_count"] == EXPECTED_CLOSED, "handoff count drift")
    req(handoff["result"]["candidate_pruned_terminals"] == EXPECTED_PRUNED, "handoff terminal drift")
    req(handoff["result"]["residual_blocks"] == EXPECTED_RESIDUAL, "handoff residual drift")
    req(handoff["result"]["aggregate_canonical"] == RESULT_CANONICAL, "handoff aggregate canonical drift")
    req(handoff["audit"]["hostile_audit_passed"] is False, "handoff self-audit leak")
    req(handoff["audit"]["required_command"] == "stage32cut-audit", "handoff command drift")
    req(handoff["credit"]["stage32_main_pruning_credit"] is False, "handoff MAIN credit leak")
    req(handoff["credit"]["cut196_pruning_credit"] is False, "handoff CUT196 credit leak")

    print(json.dumps({
        "status": "PASS_CUT196_EXACT_HEAD_AUDIT_VERIFIER",
        "wave_blocks": 255,
        "candidate_closed_blocks": EXPECTED_CLOSED,
        "candidate_pruned_terminals": EXPECTED_PRUNED,
        "fresh_whole_block_finite_ring_unsat": len(fresh_whole),
        "fresh_hnf_empty": len(fresh_hnf_empty),
        "fresh_all_hnf_parents_finite_ring_unsat_blocks": len(fresh_parent),
        "fresh_hnf_parents_checked": fresh_parent_checks,
        "unknown_checks_not_promoted": unknown_checks,
        "remaining_nonclosed_blocks": 13,
        "stage32_main_pruning_credit": False,
        "hostile_audit_passed": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
