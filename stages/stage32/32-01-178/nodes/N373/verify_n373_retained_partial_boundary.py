#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "STATE.json"
RESULT = HERE / "RESULT.json"
N372 = HERE.parent / "N372"
N372_AUDIT = N372 / "AUDIT-PASS.json"
N372_RESULT = N372 / "RESULT.json"

STATE_BLOB = "9a40813a25507a8f3e322fb79b17d321ea406274"
STATE_CANON = "100b1be5c34481464d8bc2f98454b2e47ae3a78600c25675c140bdcab1c003a1"
RESULT_BLOB = "2520e180f3637ab393584d95933c4d56ac15c5a8"
RESULT_CANON = "f480eec4f07f12e5f93341f307071b4ca0d44d6065bc65aa83ad01545576151d"
N372_AUDIT_BLOB = "6ff80567e922890d0fb4517789537d398b34f761"
N372_AUDIT_CANON = "4bead765cb9badfe6fb8ce4b1ae0c74807f541e35879fe1ad44b00f240680454"
N372_RESULT_BLOB = "c0267d903fd0b397fcd4766b03964bde788650e7"
N372_RESULT_CANON = "b9852fcfa926e77e8c51defe31002e0bf4b281dd1db4b5f320326166932fef48"
GENERATION_HEAD = "bdb055cfa6752fc330e5f3e16d35f05fb669fb86"
GENERATION_RUN = 34718895695


def req(v: bool, msg: str) -> None:
    if not v:
        raise RuntimeError(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def canonical(obj: dict) -> str:
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    return csha(q)


def checked(path: Path, expected_blob: str, expected_canon: str) -> dict:
    req(blob(path) == expected_blob, f"blob drift: {path}")
    obj = json.loads(path.read_text())
    req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"stored canonical drift: {path}")
    req(canonical(obj) == expected_canon, f"canonical drift: {path}")
    return obj


def main() -> None:
    state = checked(STATE, STATE_BLOB, STATE_CANON)
    result = checked(RESULT, RESULT_BLOB, RESULT_CANON)
    audit = checked(N372_AUDIT, N372_AUDIT_BLOB, N372_AUDIT_CANON)
    n372 = checked(N372_RESULT, N372_RESULT_BLOB, N372_RESULT_CANON)

    req(state["status"] == "RETAINED_PARTIAL_X4_PROJECTION_UNKNOWN_TIMEOUT_NO_CREDIT", "N373 retained state drift")
    req(state["next_gate"] == "ROTATE_TO_GLOBAL_COMPRESSION_ROUTE_NO_TIMEOUT_ESCALATION", "N373 next gate drift")
    rr = state["retained_result"]
    req(rr["exact_head"] == GENERATION_HEAD, "N373 generation head drift")
    req(rr["exact_head_ci_run"] == GENERATION_RUN, "N373 generation run drift")
    req(rr["result_blob_sha1"] == RESULT_BLOB and rr["result_canonical_sha256"] == RESULT_CANON, "N373 result binding drift")
    req(rr["status"] == "PARTIAL_X4_PROJECTION_UNKNOWN_TIMEOUT", "N373 retained status drift")
    req(rr["feasible_x4"] == [0] and rr["solver_checks_after_seed"] == 1 and rr["reason_unknown"] == "timeout", "N373 retained projection summary drift")

    req(result["status"] == "PARTIAL_X4_PROJECTION_UNKNOWN_TIMEOUT", "N373 result status drift")
    req(result["method"]["per_check_timeout_ms"] == 5000, "N373 timeout ceiling drift")
    req(result["method"]["reason_unknown"] == "timeout", "N373 reason_unknown drift")
    req(result["method"]["seed_x4"] == 0 and result["method"]["solver_checks_after_seed"] == 1, "N373 seeded-check count drift")
    p = result["projection"]
    req(p["complete"] is False, "N373 unexpectedly complete")
    req(p["feasible_x4"] == [0] and p["feasible_terminal_count"] == 1, "N373 feasible projection drift")
    req(p["infeasible_x4"] is None and p["infeasible_terminal_count"] is None, "N373 timeout incorrectly converted to infeasible")
    req(len(p["one_witness_per_feasible_x4"]) == 1, "N373 seed witness count drift")

    w = p["one_witness_per_feasible_x4"][0]
    nw = n372["witness"]
    req(w["source"] == "HOSTILE_AUDITED_N372_SEED", "N373 seed source drift")
    req(w["x4"] == 0 and w["terminal_rank"] == 128820 and w["terminal_identity"] == "g1-d008|e=8|rank=128820", "N373 seed identity drift")
    req(w["compressed_terminal_pairings"] == nw["compressed_terminal_pairings"], "N373/N372 terminal seed mismatch")
    req(w["picard64_coordinates"] == nw["picard64_coordinates"], "N373/N372 Picard64 seed mismatch")
    req(w["picard64_coordinates_sha256"] == nw["picard64_coordinates_sha256"], "N373/N372 coordinate commitment mismatch")
    req(w["all140_pairings_sha256"] == nw["all140_pairings_sha256"], "N373/N372 all140 commitment mismatch")
    req(w["self_square"] == nw["self_square"] == -4, "N373/N372 self-square mismatch")
    req(w["negative_hperp_square_N"] == nw["negative_hperp_square_N"] == 32, "N373/N372 Hperp scalar mismatch")
    req(audit["status"] == "HOSTILE_REAUDIT_PASS_CURRENT_V15_WITNESS_CANDIDATE_ONLY", "N372 hostile re-audit receipt drift")
    req(audit["review_id"] == 5187357950 and audit["audited_exact_head"] == "9fb78a0e0c7b52baca84058dea69b8b083e33774", "N372 audit identity drift")

    for owner in (state, result):
        for key, value in owner["credit"].items():
            req(value is False, f"credit firewall drift: {key}")

    print(json.dumps({
        "verdict": "PASS_N373_RETAINED_PARTIAL_X4_TIMEOUT_BOUNDARY",
        "generation_exact_head": GENERATION_HEAD,
        "generation_ci_run": GENERATION_RUN,
        "status": result["status"],
        "feasible_x4": [0],
        "additional_x4_classified": 0,
        "reason_unknown": "timeout",
        "per_check_timeout_ms": 5000,
        "timeout_ceiling_escalated": False,
        "full178_complete": False,
        "main_pruning_credit": False,
        "stage32_closed": False,
        "merge_authorized": False,
        "next_gate": state["next_gate"]
    }, sort_keys=True))


if __name__ == "__main__":
    main()
