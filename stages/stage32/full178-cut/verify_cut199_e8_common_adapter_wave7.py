#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULT = HERE / "CUT199-e8-common-adapter-wave7-result.json"
HANDOFF = HERE / "CUT199-e8-common-adapter-wave7-audit-handoff.json"
ACTIVE_RUNKEY = HERE / "runkeys/CUT199-e8-wave7.json"
EXECUTED_RUNKEY = HERE / "CUT199-e8-wave7-executed-runkey.json"
EXECUTED_WORKFLOW = HERE / "CUT199-e8-wave7-executed-workflow.yml"
WORKER = HERE / "cut199_e8_common_adapter_wave7.py"
AGGREGATOR = HERE / "aggregate_cut199_e8_wave7.py"
PREFLIGHT = HERE / "CUT199-e8-common-adapter-wave7-preflight.json"
CUT198_VERIFY = HERE / "verify_cut198_e8_common_adapter_wave6.py"

RESULT_CANONICAL = "db863464795f6e910de5941f76035af54f2b1b28893b690379a18d4d3239eb50"
HANDOFF_CANONICAL = "3dc7927101dd83a5e79227647c03aa27bccfa83901dccdcb592f76cc91f41dd0"
EXPECTED_CLOSED = 247
EXPECTED_PRUNED = 27911
EXPECTED_RESIDUAL = [2121,2142,2143,2147,2268,2287,2338,2394]
PRIMES = [2,3,5,7,11,13,17,31,127]

LOCKS = {
    RESULT: "88e0fa323ad5ed26bf18388ba7724feac4457651",
    HANDOFF: "df0b9a4b20a1b7d5a2b739528ea6d667490daa3e",
    ACTIVE_RUNKEY: "c5a1d69520f773b487cfdf16cf24be70b22015ba",
    EXECUTED_RUNKEY: "3e893e5d9856f017bdae49888e11663e67b34dc4",
    EXECUTED_WORKFLOW: "6c97939fc817103aa08724443424122d1cf0ab09",
    WORKER: "06c2cd81e5676ab2b29aa248bea55d3eaea320b9",
    AGGREGATOR: "02fc5c2de78e08b38359e00a0fa82a197d05338e",
    PREFLIGHT: "f3e98c0954c3ab77263709e06e87fd3e8fa10b8f",
    CUT198_VERIFY: "3da3a5222819f59f43a017756fc792f7a5ae955e",
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

def split_n1_unsat_fail_closed(cut, P, blocks, prime: int, fixed: dict[int, int]) -> tuple[bool, list[dict]]:
    attempts: list[dict] = []
    s, y, _ = cut.core.make_solver(P, blocks, prime, 10000)
    for label, value in fixed.items():
        s.add(y[label - 1] == int(value))
    n1 = 2 * y[cut.core.PACKS[0][0] - 1] + sum((y[j - 1] for j in blocks[0][0]), 0)
    for degree in range(cut.core.TARGET_D + 1):
        s.push(); s.add(n1 == degree); r = str(s.check())
        reason = s.reason_unknown() if r == "unknown" else None
        s.pop()
        rec = {"prime": prime, "n1": degree, "result": r}
        if reason:
            rec["reason_unknown"] = reason
        if r == "sat":
            attempts.append(rec)
            return False, attempts
        if r == "unknown":
            s2, y2, _ = cut.core.make_solver(P, blocks, prime, 60000)
            for label, value in fixed.items():
                s2.add(y2[label - 1] == int(value))
            n1_2 = 2 * y2[cut.core.PACKS[0][0] - 1] + sum((y2[j - 1] for j in blocks[0][0]), 0)
            s2.add(n1_2 == degree)
            r2 = str(s2.check())
            rec["retry_60s_result"] = r2
            if r2 == "unknown":
                rec["retry_60s_reason_unknown"] = s2.reason_unknown()
            attempts.append(rec)
            if r2 != "unsat":
                return False, attempts
        else:
            attempts.append(rec)
    return True, attempts

def fresh_finite_ring_obstruction(cut, P, blocks, solvers, fixed: dict[int, int]) -> tuple[bool, int | None, int, list[dict]]:
    unknown_primes: list[int] = []
    unknown_count = 0
    for p in PRIMES:
        s, y, _ = solvers[p]
        status, _reason = cut.core.check_with_fixed(s, y, fixed)
        if status == "unsat":
            return True, p, unknown_count, []
        if status == "unknown":
            unknown_count += 1
            unknown_primes.append(p)
    fallback: list[dict] = []
    for p in unknown_primes:
        ok, attempts = split_n1_unsat_fail_closed(cut, P, blocks, p, fixed)
        fallback.extend(attempts)
        if ok:
            return True, p, unknown_count, fallback
    return False, None, unknown_count, fallback

def main() -> None:
    for path, expected in LOCKS.items():
        req(path.exists(), f"missing source-lock {path.name}")
        req(blob(path) == expected, f"source-lock drift {path.name}")

    result = checked_canonical(RESULT, RESULT_CANONICAL)
    handoff = checked_canonical(HANDOFF, HANDOFF_CANONICAL)
    rk = json.loads(ACTIVE_RUNKEY.read_text())
    exrk = json.loads(EXECUTED_RUNKEY.read_text())

    req(handoff["source"]["predecessor_cut198_audited_exact_head"] == "16e439bc65e723c9f2658c274d53fb839738dcd2", "CUT198 audited exact head drift")
    req(handoff["source"]["predecessor_cut198_hostile_audit_review"] == 5188018895, "CUT198 hostile-audit review drift")
    req(handoff["source"]["predecessor_cut198_exact_head_ci"] == 34708591071, "CUT198 exact-head CI drift")
    req(result["source"]["cut198_audited_exact_head"] == handoff["source"]["predecessor_cut198_audited_exact_head"], "CUT198 result/handoff exact-head mismatch")
    req(result["source"]["cut198_hostile_audit_review"] == handoff["source"]["predecessor_cut198_hostile_audit_review"], "CUT198 result/handoff review mismatch")

    req(rk.get("generation") == 2 and rk.get("armed") is False and rk.get("consumed") is True, "CUT199 active runkey not consumed/disarmed")
    cb = rk.get("consumed_by", {})
    req(cb.get("workflow_run_id") == 34723407910 and cb.get("workflow_run_attempt") == 2, "CUT199 workflow run/attempt mismatch")
    req(cb.get("authorization_job_id") == 103633446578, "CUT199 authorization job mismatch")
    req(cb.get("integrity_job_id") == 103633446167, "CUT199 integrity job mismatch")
    req(cb.get("aggregate_job_id") == 103642748301, "CUT199 aggregate job mismatch")
    req(cb.get("aggregate_artifact_id") == 10307699352, "CUT199 aggregate artifact mismatch")
    req(cb.get("aggregate_artifact_digest") == "sha256:d14779eac8f6dcced2d3f3a59d14db10727dd81fdd40cee5edb87e043660947e", "CUT199 aggregate digest mismatch")
    req(cb.get("compute_exact_head") == "1e387891ffab2f6b45ed3a56083e522ad26d6ce3", "CUT199 compute exact head mismatch")
    req(exrk.get("generation") == 2 and exrk.get("armed") is True and exrk.get("consumed") is False, "executed generation2 runkey snapshot drift")
    pg = rk.get("prior_failed_generation", {})
    req(pg.get("generation") == 1 and pg.get("mathematical_execution_reached") is False and pg.get("credit_granted") is False, "generation1 fail-closed record drift")
    req(pg.get("failure_class") == "PREDECESSOR_SOURCE_LOCK_DRIFT", "generation1 failure class drift")

    sys.path.insert(0, str(HERE))
    import cut199_e8_common_adapter_wave7 as cut
    core = cut.core
    cut.preflight()

    survivors = core.e8.current_main_survivor_block_indices()
    wave = survivors[1531:1786]
    req(len(wave) == 255 and set(wave).isdisjoint(set(survivors[:1531])), "wave7 population/disjointness drift")
    bh = hashlib.sha256()
    for i in wave:
        bh.update(f"{i}\n".encode())
    req(bh.hexdigest() == result["target"]["block_index_stream_sha256"], "wave7 block stream drift")
    req(result["target"]["block_indices"] == wave, "retained wave7 population drift")

    closed = [int(v) for v in result["result"]["candidate_closed_block_indices"]]
    closed_set = set(closed)
    residual = sorted(set(wave) - closed_set)
    req(len(closed) == EXPECTED_CLOSED and len(closed_set) == EXPECTED_CLOSED, "closed block count/uniqueness drift")
    req(residual == EXPECTED_RESIDUAL, "residual identity drift")
    req(result["result"]["candidate_pruned_terminals"] == EXPECTED_PRUNED == 113 * EXPECTED_CLOSED, "terminal accounting drift")
    req(result["result"]["remaining_nonclosed_block_count"] == 8, "residual count drift")
    req(result["result"]["method_counts"] == {
        "ALL_HNF_PARENTS_FINITE_RING_UNSAT": 5,
        "FINITE_RING_NONCLOSING_RESIDUAL_PARENTS": 8,
        "HNF_PARENT_POPULATION_EMPTY": 3,
        "WHOLE_BLOCK_FINITE_RING_UNSAT": 239,
    }, "executed method provenance drift")
    req(result["credit"]["stage32_main_pruning_credit"] is False and result["credit"]["cut199_pruning_credit"] is False, "credit leak")
    req(result["firewalls"]["hostile_audit_required"] is True, "hostile audit firewall drift")

    P, blocks, g = core.load_picard_interface()
    solvers = {p: core.make_solver(P, blocks, p, 5000) for p in PRIMES}
    fresh_whole: list[int] = []
    fresh_hnf_empty: list[int] = []
    fresh_parent: list[int] = []
    fresh_parent_checks = 0
    unknown_checks = 0
    fallback_checks = 0
    fallback_blocks: set[int] = set()

    for block_index in closed:
        sig = core.e8.block_signature(block_index)
        req(sig["current_main_audited_prefix_survivor"] is True, f"block {block_index} lost audited prefix survival")
        sums = [int(v) for v in sig["n355_known_group_sums"]]
        req(max(sums) <= 4 and sums[1] - sums[2] <= 4 <= 16, f"N356 bridge drift on block {block_index}")
        fixed_terminal = {int(k): int(v) for k, v in sig["fixed_exceptional_pairings"].items()}
        whole_closed, _prime, u, fb = fresh_finite_ring_obstruction(cut, P, blocks, solvers, fixed_terminal)
        unknown_checks += u
        fallback_checks += len(fb)
        if fb:
            fallback_blocks.add(block_index)
        if whole_closed:
            fresh_whole.append(block_index)
            continue

        parents = list(core.e8.iter_parent_population(block_index, g))
        if not parents:
            fresh_hnf_empty.append(block_index)
            continue
        for ordinal, rec in enumerate(parents):
            fresh_parent_checks += 1
            fixed = {int(label): int(value) for label, value in zip(g.exceptional_labels, rec["selected_exceptional_pairings"])}
            parent_closed, _prime, u, fb = fresh_finite_ring_obstruction(cut, P, blocks, solvers, fixed)
            unknown_checks += u
            fallback_checks += len(fb)
            if fb:
                fallback_blocks.add(block_index)
            req(parent_closed, f"credited block {block_index} parent {ordinal} unresolved by fail-closed fresh replay: {fb[-3:] if fb else []}")
        fresh_parent.append(block_index)

    replay = set(fresh_whole) | set(fresh_hnf_empty) | set(fresh_parent)
    req(replay == closed_set, "fresh replay did not recover exact credited set")

    req(handoff["result"]["candidate_closed_block_count"] == EXPECTED_CLOSED, "handoff count drift")
    req(handoff["result"]["candidate_pruned_terminals"] == EXPECTED_PRUNED, "handoff terminal drift")
    req(handoff["result"]["residual_blocks"] == EXPECTED_RESIDUAL, "handoff residual drift")
    req(handoff["result"]["aggregate_canonical"] == RESULT_CANONICAL, "handoff canonical drift")
    req(handoff["audit"]["hostile_audit_passed"] is False and handoff["audit"]["required_command"] == "stage32cut-audit", "handoff audit firewall drift")
    req(handoff["credit"]["stage32_main_pruning_credit"] is False and handoff["credit"]["cut199_pruning_credit"] is False, "handoff credit leak")

    print(json.dumps({
        "status": "PASS_CUT199_EXACT_HEAD_AUDIT_VERIFIER",
        "predecessor_cut198_inherited_by_external_audit_receipt": True,
        "generation1_failed_closed_without_mathematical_credit": True,
        "wave_blocks": 255,
        "candidate_closed_blocks": EXPECTED_CLOSED,
        "candidate_pruned_terminals": EXPECTED_PRUNED,
        "fresh_whole_block_finite_ring_unsat": len(fresh_whole),
        "fresh_hnf_empty": len(fresh_hnf_empty),
        "fresh_all_hnf_parents_finite_ring_unsat_blocks": len(fresh_parent),
        "fresh_hnf_parents_checked": fresh_parent_checks,
        "timeout_partition_fallback_checks": fallback_checks,
        "timeout_partition_fallback_blocks": sorted(fallback_blocks),
        "unknown_checks_not_promoted": unknown_checks,
        "remaining_nonclosed_blocks": 8,
        "stage32_main_pruning_credit": False,
        "hostile_audit_passed": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
