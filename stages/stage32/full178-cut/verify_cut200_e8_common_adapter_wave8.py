#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULT = HERE / "CUT200-e8-common-adapter-wave8-result.json"
HANDOFF = HERE / "CUT200-e8-common-adapter-wave8-audit-handoff.json"
ACTIVE_RUNKEY = HERE / "runkeys/CUT200-e8-wave8.json"
EXECUTED_RUNKEY = HERE / "CUT200-e8-wave8-executed-runkey.json"
EXECUTED_WORKFLOW = HERE / "CUT200-e8-wave8-executed-workflow.yml"
WORKER = HERE / "cut200_e8_common_adapter_wave8.py"
AGGREGATOR = HERE / "aggregate_cut200_e8_wave8.py"
PREFLIGHT = HERE / "CUT200-e8-common-adapter-wave8-preflight.json"
CUT199_VERIFY = HERE / "verify_cut199_e8_common_adapter_wave7.py"

RESULT_CANONICAL = "c89b478765760a8df3e6feeff4d32ac25141f8e824efa2ff224348398bc1f2a3"
HANDOFF_CANONICAL = "ff0bf344d7527f9e408c884b49993d43f7645d8b370cea80d07c28dc07b5a29e"
EXPECTED_CLOSED = 252
EXPECTED_PRUNED = 28476
EXPECTED_RESIDUAL = [2484,2520,2525]
PRIMES = [2,3,5,7,11,13,17,31,127]

LOCKS = {
    RESULT: "cdf03534fc1f6b7641ea95a1bbb92150d2cd1af2",
    HANDOFF: "8b561d42ae970ce931f46182ed97751066dbcd44",
    ACTIVE_RUNKEY: "fb4a891820195e4267426cbf2100354035bb75b9",
    EXECUTED_RUNKEY: "b8019442e729e8d8b6df7c9002ef3ef89fd96bd4",
    EXECUTED_WORKFLOW: "c96a1078510fc7ca6db92f473fc9489cdd4a583c",
    WORKER: "4028e6185f05b186c0a27eeef671dd2d90286a64",
    AGGREGATOR: "450d2cb756f52cc3134a813638460362d1bd8a48",
    PREFLIGHT: "0ee93d39be3dc9dbb56203d2286ee7fa74292d2b",
    CUT199_VERIFY: "c18132376a6c0759c91e39c5bf7cc18350b3016a",
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

    req(handoff["source"]["predecessor_cut199_audited_exact_head"] == "27add15aaa2c40ab8f34b443d803d9a89ef655ac", "CUT199 audited exact head drift")
    req(handoff["source"]["predecessor_cut199_hostile_audit_review"] == 5189012817, "CUT199 hostile-audit review drift")
    req(handoff["source"]["predecessor_cut199_exact_head_ci"] == 34728606460, "CUT199 exact-head CI drift")
    req(result["source"]["cut199_audited_exact_head"] == handoff["source"]["predecessor_cut199_audited_exact_head"], "CUT199 result/handoff exact-head mismatch")
    req(result["source"]["cut199_hostile_audit_review"] == handoff["source"]["predecessor_cut199_hostile_audit_review"], "CUT199 result/handoff review mismatch")

    req(rk.get("generation") == 1 and rk.get("armed") is False and rk.get("consumed") is True, "CUT200 active runkey not consumed/disarmed")
    cb = rk.get("consumed_by", {})
    req(cb.get("workflow_run_id") == 34732279906 and cb.get("workflow_run_attempt") == 1, "CUT200 workflow run/attempt mismatch")
    req(cb.get("authorization_job_id") == 103657143921, "CUT200 authorization job mismatch")
    req(cb.get("integrity_job_id") == 103657144001, "CUT200 integrity job mismatch")
    req(cb.get("aggregate_job_id") == 103660851910, "CUT200 aggregate job mismatch")
    req(cb.get("aggregate_artifact_id") == 10310153659, "CUT200 aggregate artifact mismatch")
    req(cb.get("aggregate_artifact_digest") == "sha256:20bededea170861c4550cba77b6cea3b87bf48f231a6b7ce7dbb250780fdfb19", "CUT200 aggregate digest mismatch")
    req(cb.get("compute_exact_head") == "87f975766764d95c2b80e63ce7df9d9d67574290", "CUT200 compute exact head mismatch")
    req(exrk.get("generation") == 1 and exrk.get("armed") is True and exrk.get("consumed") is False, "executed generation1 runkey snapshot drift")

    sys.path.insert(0, str(HERE))
    import cut200_e8_common_adapter_wave8 as cut
    core = cut.core
    cut.preflight()

    survivors = core.e8.current_main_survivor_block_indices()
    wave = survivors[1786:2041]
    req(len(wave) == 255 and set(wave).isdisjoint(set(survivors[:1786])), "wave8 population/disjointness drift")
    bh = hashlib.sha256()
    for i in wave:
        bh.update(f"{i}\n".encode())
    req(bh.hexdigest() == result["target"]["block_index_stream_sha256"], "wave8 block stream drift")
    req(result["target"]["block_indices"] == wave, "retained wave8 population drift")

    closed = [int(v) for v in result["result"]["candidate_closed_block_indices"]]
    closed_set = set(closed)
    residual = sorted(set(wave) - closed_set)
    req(len(closed) == EXPECTED_CLOSED and len(closed_set) == EXPECTED_CLOSED, "closed block count/uniqueness drift")
    req(residual == EXPECTED_RESIDUAL, "residual identity drift")
    req(result["result"]["candidate_pruned_terminals"] == EXPECTED_PRUNED == 113 * EXPECTED_CLOSED, "terminal accounting drift")
    req(result["result"]["remaining_nonclosed_block_count"] == 3, "residual count drift")
    req(result["result"]["method_counts"] == {
        "ALL_HNF_PARENTS_FINITE_RING_UNSAT": 11,
        "FINITE_RING_NONCLOSING_RESIDUAL_PARENTS": 3,
        "WHOLE_BLOCK_FINITE_RING_UNSAT": 241,
    }, "executed method provenance drift")
    req(result["credit"]["stage32_main_pruning_credit"] is False and result["credit"]["cut200_pruning_credit"] is False, "credit leak")
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
    req(handoff["credit"]["stage32_main_pruning_credit"] is False and handoff["credit"]["cut200_pruning_credit"] is False, "handoff credit leak")

    print(json.dumps({
        "status": "PASS_CUT200_EXACT_HEAD_AUDIT_VERIFIER",
        "predecessor_cut199_inherited_by_external_audit_receipt": True,
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
        "remaining_nonclosed_blocks": 3,
        "stage32_main_pruning_credit": False,
        "hostile_audit_passed": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
