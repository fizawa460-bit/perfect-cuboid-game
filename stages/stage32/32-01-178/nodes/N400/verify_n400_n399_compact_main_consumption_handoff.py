#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

CURRENT_MAIN_HEAD = "117310b6a9d40273683cab8c08cc9e5e0cc584d9"
CURRENT_MAIN_STATE_BLOB = "b8df16056625db5fbb1947f1e927593de258f1ff"
CURRENT_MAIN_STATE_CANONICAL = "bdaab3df8871e656652e5c1f78f972405081a45b8d5e421cc4a9bacddef3bf5d"
CURRENT_CROSS_LANE_BLOB = "e2949866d41a78ff9169bdb23a2fcefb6d0f5dcd"
CURRENT_CROSS_LANE_CANONICAL = "a5a85f824ba8fe466dbd13a7118bc0e95220cd5925d2af273653d86746a71228"

N399_AUDITED_HEAD = "288dbc668894a5e356770abff0109d89d16ba6b3"
N399_AUDIT_REVIEW = 5202499889
N399_AUDIT_BLOB = "590ce4b0645455815e1cbb67cbc9a0b35299c0c8"
N399_AUDIT_CANONICAL = "a53747a12698afe255e06bee9d243cd5e46747b02a33293c79b4204b8392275c"
N399_RESULT_BLOB = "d9b0af789aa3bc93d6e2977454e8457949523707"
N399_RESULT_CANONICAL = "3446990aa48dfcce12032b157cd10ed853e059e42d803561c41d4a8ed91bf4c2"

N397_AUDITED_HEAD = "3600ecd7b4cabcef826677cb9b5963a9a1550148"
N397_AUDIT_REVIEW = 5195892621
N397_AUDIT_BLOB = "6855397e01b3ab7f85375bbd14acffea3f2970bc"
N397_AUDIT_CANONICAL = "c39d19dcfb71435c4529a0c807469ba046b214e56de8307228111191c0a77d01"

POPULATION_COUNT = 10961
SAT_COUNT = 5459
UNSAT_COUNT = 5502
SAT_STREAM_SHA256 = "00204cd76766c48e7502cb8091de1fe307f34b7486fa161c6c58f7cdb8e36fd4"
UNSAT_STREAM_SHA256 = "6648c3a246b71f74dec275012f0218d8a44477cd756229e6e3bc3eda965ca262"
SAT_PREDICATE = "(x49 + x98) mod 2 = 1"
REJECTED_PREDICATE = "(x49 + x98) mod 2 = 0"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def checked(path: Path, expected_blob: str, expected_canonical: str) -> dict:
    req(path.is_file(), f"missing source: {path}")
    req(blob(path) == expected_blob, f"blob drift: {path}")
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256_without_this_field", None)
    req(claimed == expected_canonical, f"stored canonical drift: {path}")
    req(csha(body) == expected_canonical, f"canonical drift: {path}")
    return obj


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--current-main-root", required=True)
    args = ap.parse_args()

    repo = Path(__file__).resolve().parents[5]
    n397_dir = repo / "stages/stage32/32-01-178/nodes/N397"
    n399_dir = repo / "stages/stage32/32-01-178/nodes/N399"

    audit399 = checked(n399_dir / "AUDIT-PASS.json", N399_AUDIT_BLOB, N399_AUDIT_CANONICAL)
    result399 = checked(n399_dir / "RESULT.json", N399_RESULT_BLOB, N399_RESULT_CANONICAL)
    audit397 = checked(n397_dir / "AUDIT-PASS.json", N397_AUDIT_BLOB, N397_AUDIT_CANONICAL)

    req(audit399["hostile_audit_verdict"] == "PASS", "N399 hostile audit verdict drift")
    req(audit399["audited_exact_head"] == N399_AUDITED_HEAD, "N399 audited head drift")
    req(int(audit399["hostile_audit_review_id"]) == N399_AUDIT_REVIEW, "N399 review drift")
    req(audit399["retained_outcome"] == "TERMINAL_PARITY_PREDICATE_TRANSPORT_VERIFIED_NO_PRUNING", "N399 retained outcome drift")
    req(audit399["bounded_result"]["source_population_terminal_count"] == POPULATION_COUNT, "N399 population count drift")
    req(audit399["bounded_result"]["n396_sat_terminal_count"] == SAT_COUNT, "N399 SAT count drift")
    req(audit399["bounded_result"]["n396_unsat_terminal_count"] == UNSAT_COUNT, "N399 UNSAT count drift")
    req(audit399["bounded_result"]["terminal_predicate"] == SAT_PREDICATE, "N399 predicate drift")
    req(audit399["bounded_result"]["sat_terminal_rank_stream_sha256"] == SAT_STREAM_SHA256, "N399 SAT stream drift")
    req(audit399["bounded_result"]["unsat_terminal_rank_stream_sha256"] == UNSAT_STREAM_SHA256, "N399 UNSAT stream drift")
    req(audit399["credit"]["additional_pruning_credit"] is False, "N399 unexpectedly grants new pruning")
    req(audit399["credit"]["main_authority_subtraction_performed"] is False, "N399 unexpectedly subtracts MAIN authority")

    req(result399["certificate"]["source_terminal_count"] == POPULATION_COUNT, "N399 result population drift")
    req(result399["certificate"]["sat_terminal_count"] == SAT_COUNT, "N399 result SAT count drift")
    req(result399["certificate"]["unsat_terminal_count"] == UNSAT_COUNT, "N399 result UNSAT count drift")
    req(result399["certificate"]["predicate"] == SAT_PREDICATE, "N399 result predicate drift")
    req(result399["certificate"]["unsat_terminal_rank_stream_sha256"] == UNSAT_STREAM_SHA256, "N399 result rejected stream drift")
    req(result399["transport_checks"]["reconstructs_n396_unsat_rank_stream_exactly"] is True, "N399 exact rejected-stream reconstruction lost")

    req(audit397["hostile_audit_verdict"] == "PASS", "N397 hostile audit verdict drift")
    req(audit397["audited_exact_head"] == N397_AUDITED_HEAD, "N397 audited head drift")
    req(int(audit397["hostile_audit_review_id"]) == N397_AUDIT_REVIEW, "N397 review drift")
    req(audit397["bounded_result"]["source_population_terminal_count"] == POPULATION_COUNT, "N397 population count drift")
    req(audit397["bounded_result"]["n396_audited_unsat_terminal_count"] == UNSAT_COUNT, "N397 UNSAT count drift")
    req(audit397["bounded_result"]["prior_consumed_v24_overlap_terminal_count"] == 0, "N397 prior-overlap drift")
    req(audit397["bounded_result"]["double_charge"] is False, "N397 double-charge drift")
    req(audit397["bounded_result"]["bounded_incremental_pruning_terminals"] == UNSAT_COUNT, "N397 pruning count drift")
    req(audit397["bounded_result"]["eligible_for_separate_main_consumption"] is True, "N397 MAIN-consumption eligibility drift")
    req(audit397["credit"]["main_pruning_credit"] is False, "N397 unexpectedly grants MAIN pruning credit")
    req(audit397["credit"]["main_authority_subtraction_performed"] is False, "N397 unexpectedly subtracts MAIN authority")

    current_root = Path(args.current_main_root).resolve()
    req((current_root / ".git").exists(), "current MAIN checkout missing git metadata")
    current_head = subprocess.check_output(["git", "-C", str(current_root), "rev-parse", "HEAD"], text=True).strip()
    req(current_head == CURRENT_MAIN_HEAD, "current MAIN checkout head drift")

    main_state = checked(
        current_root / "stages/stage32/MAIN-STATE.json",
        CURRENT_MAIN_STATE_BLOB,
        CURRENT_MAIN_STATE_CANONICAL,
    )
    demands = checked(
        current_root / "stages/stage32/proof/CROSS-LANE-DEMANDS.json",
        CURRENT_CROSS_LANE_BLOB,
        CURRENT_CROSS_LANE_CANONICAL,
    )
    req(main_state["current_target"]["primary_incomplete_id"] == "32-01", "current MAIN target drift")
    req(main_state["current_target"]["control_mode"] == "FULL178_AND_FINAL_MILESTONE_CHAIN", "current control mode drift")
    req(main_state["current_exact_frontier"]["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "remaining-terminal semantics drift")
    req(main_state["firewalls"]["full178_complete"] is False, "unexpected FULL178 completion")
    req(main_state["firewalls"]["merge_authorized"] is False, "unexpected merge authorization")
    req("N396" not in json.dumps(main_state, sort_keys=True), "N396 already appears in current MAIN authority; handoff risks duplicate consumption")
    req(
        not any(d.get("status") == "OPEN" and d.get("producer_lane") in ("178", "32-01-178") for d in demands["demands"]),
        "OPEN producer demand preempts N400 handoff",
    )

    payload = {
        "semantics": "EXACT_COMPACT_MAIN_CONSUMPTION_HANDOFF_CANDIDATE_FOR_AUDITED_N396_REJECTED_SET_USING_HOSTILE_AUDITED_N399_PREDICATE_AND_N397_NO_DOUBLE_CHARGE",
        "current_repository_main_exact_head": CURRENT_MAIN_HEAD,
        "source_population": {
            "scope": "retained N391 97-block population only",
            "terminal_count": POPULATION_COUNT,
            "not_exact_global_residual_set": True,
        },
        "compact_rejected_set": {
            "predicate_on_retained_population": REJECTED_PREDICATE,
            "exact_terminal_count": UNSAT_COUNT,
            "terminal_rank_stream_sha256": UNSAT_STREAM_SHA256,
            "complement_sat_predicate": SAT_PREDICATE,
            "complement_sat_terminal_count": SAT_COUNT,
            "complement_sat_rank_stream_sha256": SAT_STREAM_SHA256,
            "identity_source": "hostile-audited N399 exact terminal predicate transport",
        },
        "no_double_charge": {
            "source": "hostile-audited N397 current-authority accounting",
            "prior_consumed_v24_overlap_terminal_count": 0,
            "double_charge": False,
            "eligible_for_separate_main_consumption": True,
        },
        "route_control": {
            "materially_distinct_from_n399": True,
            "reason": "N399 proves the exact terminal predicate; N400 binds that audited predicate to the separately audited N397 current-authority/no-double-charge result as a compact consumer handoff without repeating the 97x8 census or terminal enumeration.",
            "same_97x8_parity_census_repeated": False,
            "terminal_reenumeration_required_by_n400": False,
            "transport_beyond_retained_97_blocks": False,
        },
        "promotion_firewall": {
            "main_consumption_handoff_candidate": True,
            "main_authority_subtraction_performed_by_n400": False,
            "main_pruning_credit": False,
            "additional_pruning_credit": False,
            "full178_complete": False,
            "integral_carrier_obstruction_promoted": False,
            "effectivity_final": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "heavy_compute_authorized": False,
            "merge_authorized": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)

    print("PASS_N400_N399_COMPACT_MAIN_CONSUMPTION_HANDOFF")
    print(f"population={POPULATION_COUNT} rejected={UNSAT_COUNT} prior_overlap=0 predicate={REJECTED_PREDICATE}")
    print("N400_HANDOFF_JSON=" + json.dumps(payload, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
