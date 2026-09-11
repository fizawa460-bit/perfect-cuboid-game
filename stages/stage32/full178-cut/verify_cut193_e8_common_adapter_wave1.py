#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EX5_HANDOFF = ROOT / "stages/stage32-ex5/cut-handoff"
RESULT = HERE / "CUT193-e8-common-adapter-wave1-result.json"
HANDOFF = HERE / "CUT193-e8-common-adapter-wave1-audit-handoff.json"
EXECUTED_RUNKEY = HERE / "CUT193-e8-wave1-executed-runkey.json"
EXECUTED_WORKFLOW = HERE / "CUT193-e8-wave1-executed-workflow.yml"
EX5_EXECUTED_RUNKEY = HERE / "CUT193-ex5-producer-executed-runkey.json"
ACTIVE_RUNKEY = HERE / "runkeys/CUT193-e8-wave1.json"
CUT193 = HERE / "cut193_e8_common_adapter_wave1.py"
AGGREGATOR = HERE / "aggregate_cut193_e8_wave1.py"
PREFLIGHT = HERE / "CUT193-e8-common-adapter-wave1-preflight.json"
CUT102 = HERE / "cut102_finite_ring_direct_completion_v2.py"
MAIN = ROOT / "stages/stage32/MAIN-STATE.json"
EX5_PREFLIGHT = EX5_HANDOFF / "e8-terminal-population-preflight.json"
EX5_ADAPTER = EX5_HANDOFF / "e8_terminal_population_adapter.py"
EX5_VERIFY = EX5_HANDOFF / "verify_e8_terminal_population_adapter.py"

RESULT_CANONICAL = "161abe2cf9a00b95ce2b1acd422008bbb5c72929ea7a72e9892b94546abae2c1"
HANDOFF_CANONICAL = "b095cfb6b1b0703a8821d710e5536981a5410b0d9b4699e409d242e8be37358a"
MAIN_CANONICAL = "4c143ad944a3506f0c39acdd5cc697276576aa5d0c7293c433d10834f9f462f3"
MAIN_TERMINALS = 65396964990500233636101
EXPECTED_CLOSED = 227
EXPECTED_PRUNED = 25651
EXPECTED_POST = 65396964990500233610450
EXPECTED_PARENT_BLOCKS = [3,8,9,14,29,50,85,86,95,120,141,175,267,285,286,337]
EXPECTED_PARENT_COUNTS = {3:65,8:500,9:37,14:65,29:316,50:65,85:441,86:40,95:40,120:40,141:65,175:40,267:40,285:5,286:1,337:65}
EXPECTED_RESIDUAL = [1,2,7,13,28,34,35,36,43,49,68,84,110,111,140,159,210,211,212,221,231,236,237,246,266,271,301,336]
LOCKS = {
    RESULT: "ef72967a97e41287671f25647ad6fc24aef31ccb",
    EXECUTED_RUNKEY: "f0f5e724f456034055bce7b12d7075e26f887510",
    EXECUTED_WORKFLOW: "466afbce21128b1b03e528cb16a8082196009dcd",
    EX5_EXECUTED_RUNKEY: "3d1796fc09eabf507b8293bdad7421e05dff5723",
    CUT193: "312b8bcb6d541a14757372e563f1990b7cc249fa",
    AGGREGATOR: "b640e610287f649f96385e18dfc0d51d164d2f55",
    PREFLIGHT: "8e0cc1312b7babc647c33e35ba361398d3419226",
    CUT102: "fbdd1e65b509526d5198743208bff79bd2488673",
    MAIN: "484139b653256d34c351aa10fe815c1642cc7cd8",
    EX5_PREFLIGHT: "b28539d9d0eafddc181d3bbf6d668261f2ff081e",
    EX5_ADAPTER: "6026d2c8b4a2eb69c453a2bd38c5923f46d6d74f",
    EX5_VERIFY: "8fe802444ca8c92a80058555eaf431f0c1a52c76",
}


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def checked_canonical(path: Path, canonical: str) -> dict:
    o = json.loads(path.read_text())
    q = dict(o)
    claimed = q.pop("canonical_sha256_without_this_field", None)
    req(claimed == canonical and csha(q) == canonical, f"canonical drift: {path.relative_to(ROOT)}")
    return o


def main() -> None:
    for path, expected in LOCKS.items():
        req(path.exists(), f"missing source lock: {path.relative_to(ROOT)}")
        req(blob(path) == expected, f"source-lock drift: {path.relative_to(ROOT)}")

    result = checked_canonical(RESULT, RESULT_CANONICAL)
    handoff = checked_canonical(HANDOFF, HANDOFF_CANONICAL)
    main_state = checked_canonical(MAIN, MAIN_CANONICAL)

    rk = json.loads(ACTIVE_RUNKEY.read_text())
    req(rk.get("armed") is False and rk.get("consumed") is True, "CUT193 active runkey not disarmed/consumed")
    req(rk.get("consumed_by", {}).get("workflow_run_id") == 34602175336, "CUT193 consumed run mismatch")
    req(rk.get("consumed_by", {}).get("aggregate_artifact_id") == 10264888946, "CUT193 aggregate artifact mismatch")

    # Independently replay the producer adapter's complete transitive source-lock boundary.
    subprocess.run([sys.executable, str(EX5_VERIFY)], cwd=ROOT, check=True)

    # Import the locked CUT implementation only after dependency identity is established.
    sys.path.insert(0, str(HERE))
    import cut193_e8_common_adapter_wave1 as cut
    e8 = cut.e8

    f = main_state["current_exact_frontier"]
    req(main_state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V12_CUT191_AUDITED_CONSUMED", "MAIN schema drift")
    req(f["authoritative_remaining_terminals"] == MAIN_TERMINALS and f["authoritative_remaining_strata"] == 17128, "MAIN V12 authority drift")
    req(f["n356_main_pruning_credit"] is True and f["cut191_main_pruning_credit"] is True, "N356/CUT191 not consumed")

    survivors = e8.current_main_survivor_block_indices()
    wave = survivors[1:256]
    req(len(wave) == 255 and 0 not in wave, "wave population/disjointness drift")
    h = hashlib.sha256()
    for i in wave:
        h.update(f"{i}\n".encode())
    req(h.hexdigest() == "68ca7b27ffeceb52c35942449ca47105fd4a74757575544033454c3c9be514ea", "wave block stream drift")
    req(result["target"]["block_indices"] == wave, "retained aggregate target population drift")
    req(result["target"]["cut191_block0_disjoint"] is True and result["target"]["n356_preserved_all_wave_blocks"] is True, "aggregate authority bridge drift")

    closed = [int(v) for v in result["result"]["candidate_closed_block_indices"]]
    closed_set = set(closed)
    residual = sorted(set(wave) - closed_set)
    req(len(closed) == EXPECTED_CLOSED and len(closed_set) == EXPECTED_CLOSED, "closed-block count/uniqueness drift")
    req(residual == EXPECTED_RESIDUAL, "residual block identity drift")
    req(result["result"]["candidate_pruned_terminals"] == EXPECTED_PRUNED == 113 * EXPECTED_CLOSED, "candidate terminal accounting drift")
    req(result["result"]["candidate_post_cut_main_terminals"] == EXPECTED_POST == MAIN_TERMINALS - EXPECTED_PRUNED, "candidate post-CUT count drift")
    req(result["result"]["remaining_nonclosed_block_count"] == 28, "residual count drift")
    req(result["result"]["method_counts"] == {"ALL_HNF_PARENTS_FINITE_RING_UNSAT":16,"FINITE_RING_NONCLOSING_RESIDUAL_PARENTS":28,"WHOLE_BLOCK_FINITE_RING_UNSAT":211}, "method-count drift")

    # The original computation found every credited obstruction already modulo 2.
    # Re-run every credited block from exact Picard64/HNF source data at the exact head.
    P, blocks, g = cut.load_picard_interface()
    s, y, linear = cut.make_solver(P, blocks, 2, 5000)
    req(linear["prime"] == 2, "mod-2 solver construction drift")

    derived_whole = []
    derived_parent = []
    parent_counts: dict[int, int] = {}
    for block_index in closed:
        sig = e8.block_signature(block_index)
        req(sig["current_main_audited_prefix_survivor"] is True, f"credited block {block_index} left N220/N355 population")
        sums = [int(v) for v in sig["n355_known_group_sums"]]
        req(max(sums) <= 4 and sums[1] - sums[2] <= 4 <= 16, f"N356 bridge drift on block {block_index}")
        fixed_terminal = {int(k): int(v) for k, v in sig["fixed_exceptional_pairings"].items()}
        status, _ = cut.check_with_fixed(s, y, fixed_terminal)
        if status == "unsat":
            derived_whole.append(block_index)
            continue
        # Whole-block mod2 is not enough: every exact HNF-integrality-feasible parent
        # must separately be mod2 UNSAT before this block earns pruning credit.
        parents = list(e8.iter_parent_population(block_index, g))
        req(parents, f"credited parent-level block {block_index} unexpectedly has empty parent population")
        parent_counts[block_index] = len(parents)
        for ordinal, rec in enumerate(parents):
            fixed = {int(label): int(value) for label, value in zip(g.exceptional_labels, rec["selected_exceptional_pairings"])}
            pstatus, _ = cut.check_with_fixed(s, y, fixed)
            req(pstatus == "unsat", f"credited block {block_index} parent {ordinal} not mod2 UNSAT: {pstatus}")
        derived_parent.append(block_index)

    req(len(derived_whole) == 211, f"whole-block mod2 replay count drift: {len(derived_whole)}")
    req(derived_parent == EXPECTED_PARENT_BLOCKS, f"parent-level block replay drift: {derived_parent}")
    req(parent_counts == EXPECTED_PARENT_COUNTS, f"parent population replay drift: {parent_counts}")

    req(handoff["result"]["candidate_closed_block_count"] == EXPECTED_CLOSED, "handoff closed count drift")
    req(handoff["result"]["all_hnf_parent_blocks"] == EXPECTED_PARENT_BLOCKS, "handoff parent block drift")
    req({int(k): int(v) for k, v in handoff["result"]["all_hnf_parent_counts"].items()} == EXPECTED_PARENT_COUNTS, "handoff parent counts drift")
    req(handoff["result"]["residual_blocks"] == EXPECTED_RESIDUAL, "handoff residual identity drift")
    req(handoff["audit"]["hostile_audit_passed"] is False and handoff["credit"]["stage32_main_pruning_credit"] is False, "audit/credit firewall leak")
    req(result["credit"]["stage32_main_pruning_credit"] is False and result["firewalls"]["hostile_audit_required"] is True, "aggregate credit firewall leak")

    print(json.dumps({
        "status": "PASS_CUT193_EXACT_HEAD_AUDIT_VERIFIER",
        "wave_blocks": 255,
        "credited_closed_blocks": EXPECTED_CLOSED,
        "candidate_pruned_terminals": EXPECTED_PRUNED,
        "whole_block_mod2_unsat": len(derived_whole),
        "all_hnf_parents_mod2_unsat_blocks": len(derived_parent),
        "all_hnf_parent_replayed": sum(parent_counts.values()),
        "remaining_nonclosed_blocks": 28,
        "stage32_main_pruning_credit": False,
        "hostile_audit_passed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
