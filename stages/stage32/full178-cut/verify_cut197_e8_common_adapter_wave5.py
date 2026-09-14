#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESULT = HERE / "CUT197-e8-common-adapter-wave5-result.json"
HANDOFF = HERE / "CUT197-e8-common-adapter-wave5-audit-handoff.json"
ACTIVE_RUNKEY = HERE / "runkeys/CUT197-e8-wave5.json"
EXECUTED_RUNKEY = HERE / "CUT197-e8-wave5-executed-runkey.json"
EXECUTED_WORKFLOW = HERE / "CUT197-e8-wave5-executed-workflow.yml"
WORKER = HERE / "cut197_e8_common_adapter_wave5.py"
AGGREGATOR = HERE / "aggregate_cut197_e8_wave5.py"
PREFLIGHT = HERE / "CUT197-e8-common-adapter-wave5-preflight.json"
CUT196_VERIFY = HERE / "verify_cut196_e8_common_adapter_wave4.py"

RESULT_CANONICAL = "f99d0f051ce95e269658e0ec945d727db32a94687bfd8acde5ee354e00776fa0"
HANDOFF_CANONICAL = "affabc5b6fc752de6a2ebb6e08dac105842385e7162efbe15e6adaf1fa5fa514"
EXPECTED_CLOSED = 250
EXPECTED_PRUNED = 28250
EXPECTED_RESIDUAL = [1456,1512,1638,1657,1708]
PRIMES = [2,3,5,7,11,13,17,31,127]

LOCKS = {
    RESULT: "e98f33ef093003e724ff6574bfec546ab1221955",
    HANDOFF: "236352b97ef13d3b5978f15a8a21fa67a9f331fd",
    ACTIVE_RUNKEY: "0b4a8fe5c3de7692fdbda7054a70712488b37b68",
    EXECUTED_RUNKEY: "3901106922d94804cf2dc03f6d96e99efeefc575",
    EXECUTED_WORKFLOW: "6512fa6b79bdb2926354ceb362b08cca968fe520",
    WORKER: "7124d8c88cce9d11ae3733d78a5873a0012b9848",
    AGGREGATOR: "b1b0e342ea7897f59dafa0c36367573d7f126c43",
    PREFLIGHT: "b6199a4c4aaa3ccd500ef446f9fe774b09c38be7",
    CUT196_VERIFY: "1364dc9321edc8b294c19ce43ca89d0be91192ac",
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
        if reason: rec["reason_unknown"] = reason
        if r == "sat":
            attempts.append(rec); return False, attempts
        if r == "unknown":
            s2, y2, _ = cut.core.make_solver(P, blocks, prime, 60000)
            for label, value in fixed.items(): s2.add(y2[label - 1] == int(value))
            n1_2 = 2 * y2[cut.core.PACKS[0][0] - 1] + sum((y2[j - 1] for j in blocks[0][0]), 0)
            s2.add(n1_2 == degree); r2 = str(s2.check())
            rec["retry_60s_result"] = r2
            if r2 == "unknown": rec["retry_60s_reason_unknown"] = s2.reason_unknown()
            attempts.append(rec)
            if r2 != "unsat": return False, attempts
        else:
            attempts.append(rec)
    return True, attempts


def fresh_finite_ring_obstruction(cut, P, blocks, solvers, fixed: dict[int, int]) -> tuple[bool, int | None, int, list[dict]]:
    unknown_primes: list[int] = []
    unknown_count = 0
    for p in PRIMES:
        s, y, _ = solvers[p]
        status, _reason = cut.core.check_with_fixed(s, y, fixed)
        if status == "unsat": return True, p, unknown_count, []
        if status == "unknown":
            unknown_count += 1; unknown_primes.append(p)
    fallback: list[dict] = []
    for p in unknown_primes:
        ok, attempts = split_n1_unsat_fail_closed(cut, P, blocks, p, fixed)
        fallback.extend(attempts)
        if ok: return True, p, unknown_count, fallback
    return False, None, unknown_count, fallback


def main() -> None:
    for path, expected in LOCKS.items():
        req(path.exists(), f"missing source-lock {path.name}")
        req(blob(path) == expected, f"source-lock drift {path.name}")

    result = checked_canonical(RESULT, RESULT_CANONICAL)
    handoff = checked_canonical(HANDOFF, HANDOFF_CANONICAL)
    rk = json.loads(ACTIVE_RUNKEY.read_text())
    exrk = json.loads(EXECUTED_RUNKEY.read_text())

    req(handoff["source"]["predecessor_cut196_audited_exact_head"] == "85f4e988acf6446fa0d472208e21990621a650b4", "CUT196 audited exact head drift")
    req(handoff["source"]["predecessor_cut196_hostile_audit_review"] == 5186302071, "CUT196 hostile-audit review drift")
    req(handoff["source"]["predecessor_cut196_exact_head_ci"] == 34687223279, "CUT196 exact-head CI drift")
    req(result["source"]["cut196_audited_exact_head"] == handoff["source"]["predecessor_cut196_audited_exact_head"], "CUT196 result/handoff exact-head mismatch")
    req(result["source"]["cut196_hostile_audit_review"] == handoff["source"]["predecessor_cut196_hostile_audit_review"], "CUT196 result/handoff review mismatch")

    req(rk.get("generation") == 1 and rk.get("armed") is False and rk.get("consumed") is True, "CUT197 active runkey not consumed/disarmed")
    cb = rk.get("consumed_by", {})
    req(cb.get("workflow_run_id") == 34691947196, "CUT197 workflow run mismatch")
    req(cb.get("authorization_job_id") == 103548641324, "CUT197 authorization job mismatch")
    req(cb.get("integrity_job_id") == 103548641199, "CUT197 integrity job mismatch")
    req(cb.get("aggregate_job_id") == 103552768295, "CUT197 aggregate job mismatch")
    req(cb.get("aggregate_artifact_id") == 10298431590, "CUT197 aggregate artifact mismatch")
    req(cb.get("aggregate_artifact_digest") == "sha256:df79f17eb3b13029f3df98bf017fb734a0ce5b35a50baac415d3561df297a81f", "CUT197 aggregate digest mismatch")
    req(cb.get("compute_exact_head") == "c23df92827f7be9dbe9ca28cd240a576581b1763", "CUT197 compute exact head mismatch")
    req(exrk.get("generation") == 1 and exrk.get("armed") is True and exrk.get("consumed") is False, "executed generation1 runkey snapshot drift")

    sys.path.insert(0, str(HERE))
    import cut197_e8_common_adapter_wave5 as cut
    core = cut.core
    cut.preflight()

    survivors = core.e8.current_main_survivor_block_indices()
    wave = survivors[1021:1276]
    req(len(wave) == 255 and set(wave).isdisjoint(set(survivors[:1021])), "wave5 population/disjointness drift")
    bh = hashlib.sha256()
    for i in wave: bh.update(f"{i}\n".encode())
    req(bh.hexdigest() == result["target"]["block_index_stream_sha256"], "wave5 block stream drift")
    req(result["target"]["block_indices"] == wave, "retained wave5 population drift")

    closed = [int(v) for v in result["result"]["candidate_closed_block_indices"]]
    closed_set = set(closed)
    residual = sorted(set(wave) - closed_set)
    req(len(closed) == EXPECTED_CLOSED and len(closed_set) == EXPECTED_CLOSED, "closed block count/uniqueness drift")
    req(residual == EXPECTED_RESIDUAL, "residual identity drift")
    req(result["result"]["candidate_pruned_terminals"] == EXPECTED_PRUNED == 113 * EXPECTED_CLOSED, "terminal accounting drift")
    req(result["result"]["remaining_nonclosed_block_count"] == 5, "residual count drift")
    req(result["result"]["method_counts"] == {"ALL_HNF_PARENTS_FINITE_RING_UNSAT": 6, "FINITE_RING_NONCLOSING_RESIDUAL_PARENTS": 5, "WHOLE_BLOCK_FINITE_RING_UNSAT": 244}, "executed method provenance drift")
    req(result["credit"]["stage32_main_pruning_credit"] is False and result["credit"]["cut197_pruning_credit"] is False, "credit leak")
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
        unknown_checks += u; fallback_checks += len(fb)
        if fb: fallback_blocks.add(block_index)
        if whole_closed:
            fresh_whole.append(block_index); continue

        parents = list(core.e8.iter_parent_population(block_index, g))
        if not parents:
            fresh_hnf_empty.append(block_index); continue
        for ordinal, rec in enumerate(parents):
            fresh_parent_checks += 1
            fixed = {int(label): int(value) for label, value in zip(g.exceptional_labels, rec["selected_exceptional_pairings"])}
            parent_closed, _prime, u, fb = fresh_finite_ring_obstruction(cut, P, blocks, solvers, fixed)
            unknown_checks += u; fallback_checks += len(fb)
            if fb: fallback_blocks.add(block_index)
            req(parent_closed, f"credited block {block_index} parent {ordinal} unresolved by fail-closed fresh replay: {fb[-3:] if fb else []}")
        fresh_parent.append(block_index)

    replay = set(fresh_whole) | set(fresh_hnf_empty) | set(fresh_parent)
    req(replay == closed_set, "fresh replay did not recover exact credited set")

    req(handoff["result"]["candidate_closed_block_count"] == EXPECTED_CLOSED, "handoff count drift")
    req(handoff["result"]["candidate_pruned_terminals"] == EXPECTED_PRUNED, "handoff terminal drift")
    req(handoff["result"]["residual_blocks"] == EXPECTED_RESIDUAL, "handoff residual drift")
    req(handoff["result"]["aggregate_canonical"] == RESULT_CANONICAL, "handoff canonical drift")
    req(handoff["audit"]["hostile_audit_passed"] is False and handoff["audit"]["required_command"] == "stage32cut-audit", "handoff audit firewall drift")
    req(handoff["credit"]["stage32_main_pruning_credit"] is False and handoff["credit"]["cut197_pruning_credit"] is False, "handoff credit leak")

    print(json.dumps({
        "status":"PASS_CUT197_EXACT_HEAD_AUDIT_VERIFIER",
        "predecessor_cut196_inherited_by_external_audit_receipt":True,
        "wave_blocks":255,
        "candidate_closed_blocks":EXPECTED_CLOSED,
        "candidate_pruned_terminals":EXPECTED_PRUNED,
        "fresh_whole_block_finite_ring_unsat":len(fresh_whole),
        "fresh_hnf_empty":len(fresh_hnf_empty),
        "fresh_all_hnf_parents_finite_ring_unsat_blocks":len(fresh_parent),
        "fresh_hnf_parents_checked":fresh_parent_checks,
        "timeout_partition_fallback_checks":fallback_checks,
        "timeout_partition_fallback_blocks":sorted(fallback_blocks),
        "unknown_checks_not_promoted":unknown_checks,
        "remaining_nonclosed_blocks":5,
        "stage32_main_pruning_credit":False,
        "hostile_audit_passed":False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
