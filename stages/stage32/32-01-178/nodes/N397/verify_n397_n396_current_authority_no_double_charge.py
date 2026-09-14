#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

CURRENT_MAIN_HEAD = "955a9eb6b95b2f4a3234013b3da74257863d8954"
CURRENT_MAIN_STATE_BLOB = "b8df16056625db5fbb1947f1e927593de258f1ff"
CURRENT_MAIN_STATE_CANONICAL = "bdaab3df8871e656652e5c1f78f972405081a45b8d5e421cc4a9bacddef3bf5d"
CURRENT_CROSS_LANE_BLOB = "e2949866d41a78ff9169bdb23a2fcefb6d0f5dcd"
CURRENT_CROSS_LANE_CANONICAL = "a5a85f824ba8fe466dbd13a7118bc0e95220cd5925d2af273653d86746a71228"

N391_MAIN_V24_HEAD = "a89580f3fcf42152b47673d2cfec1935c72555c2"
N391_RESULT_BLOB = "3e72cea011e5a519173a710c20d88bc781c4cee8"
N391_RESULT_CANONICAL = "2b30f97aca0873568c324cf9a88ba6dc8ee0e3cceb29e1fc60e9e2c978b02da3"
N391_AUDIT_BLOB = "5c080d67b1f1c90792fa29e5d5ded71fbc4ea45b"
N391_AUDIT_CANONICAL = "5ce24718a7cb9c3975eb6d8cc1c84e8b1d51f2a04d8745691bdc2281cdb4b11c"
N391_AUDIT_REVIEW = 5193577864

N396_AUDITED_HEAD = "d84c71f42df7f4b261d970fb002d9e0f22dc5c6d"
N396_AUDIT_REVIEW = 5195404332
N396_AUDIT_BLOB = "96d3ab34505ced9001763920535a44518a7de28f"
N396_AUDIT_CANONICAL = "50dc8fe3cb74dc5eb32bc655adaadb8f37e8163d7c5cb968ea5ac2e47eb51fba"
N396_RESULT_BLOB = "971f1665c8be4c22eef549020046dd0830028dff"
N396_RESULT_CANONICAL = "e34e23e2b17063c2f51d9862af1c2a958002fdb0327e43b5e52d85bcb1a83cd1"
N396_PROBE_BLOB = "4db03f296183c6655fafa9bdb5418dd82a17a733"

UNSAT_COUNT = 5502
SAT_COUNT = 5459
POPULATION_COUNT = 10961
UNSAT_STREAM_SHA256 = "6648c3a246b71f74dec275012f0218d8a44477cd756229e6e3bc3eda965ca262"
POPULATION_RANK_STREAM_SHA256 = "6b699fdf0e8735a489b2d6086b18a074817af211583b8be266ddcd804f5a8cce"


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


def authority_checked(root: Path) -> tuple[dict, dict]:
    main_path = root / "stages/stage32/MAIN-STATE.json"
    demand_path = root / "stages/stage32/proof/CROSS-LANE-DEMANDS.json"
    main = checked(main_path, CURRENT_MAIN_STATE_BLOB, CURRENT_MAIN_STATE_CANONICAL)
    demands = checked(demand_path, CURRENT_CROSS_LANE_BLOB, CURRENT_CROSS_LANE_CANONICAL)
    return main, demands


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--current-main-root", required=True)
    ap.add_argument("--n391-main-root", required=True)
    args = ap.parse_args()

    repo = Path(__file__).resolve().parents[5]
    n391_dir = repo / "stages/stage32/32-01-178/nodes/N391"
    n396_dir = repo / "stages/stage32/32-01-178/nodes/N396"

    audit396 = checked(n396_dir / "AUDIT-PASS.json", N396_AUDIT_BLOB, N396_AUDIT_CANONICAL)
    result396 = checked(n396_dir / "RESULT.json", N396_RESULT_BLOB, N396_RESULT_CANONICAL)
    req(blob(n396_dir / "probe_n396_n395_picard64_mod8_completion.py") == N396_PROBE_BLOB, "N396 probe blob drift")
    req(audit396["hostile_audit_verdict"] == "PASS", "N396 hostile audit verdict drift")
    req(audit396["audited_exact_head"] == N396_AUDITED_HEAD, "N396 audited head drift")
    req(int(audit396["hostile_audit_review_id"]) == N396_AUDIT_REVIEW, "N396 review drift")
    req(audit396["retained_outcome"] == "N396_BOUNDED_PICARD64_MOD8_UNSAT_5502", "N396 retained outcome drift")
    req(audit396["bounded_result"]["picard64_mod8_completion_unsat_terminal_count"] == UNSAT_COUNT, "N396 audited UNSAT count drift")
    req(audit396["bounded_result"]["unsat_rank_stream_sha256"] == UNSAT_STREAM_SHA256, "N396 audited UNSAT identity hash drift")
    req(result396["completion_result"]["unsat_terminal_count"] == UNSAT_COUNT, "N396 result UNSAT count drift")
    req(result396["completion_result"]["sat_terminal_count"] == SAT_COUNT, "N396 result SAT count drift")
    req(result396["scope"]["terminal_identity_count"] == POPULATION_COUNT, "N396 population count drift")
    req(result396["completion_result"]["unsat_terminal_rank_stream_sha256"] == UNSAT_STREAM_SHA256, "N396 result UNSAT stream drift")
    req(result396["credit_firewall"]["main_pruning_credit"] is False, "N396 unexpectedly already has MAIN pruning credit")

    audit391 = checked(n391_dir / "AUDIT-PASS.json", N391_AUDIT_BLOB, N391_AUDIT_CANONICAL)
    result391 = checked(n391_dir / "RESULT.json", N391_RESULT_BLOB, N391_RESULT_CANONICAL)
    req(audit391["status"] == "HOSTILE_AUDIT_PASS", "N391 hostile audit status drift")
    req(int(audit391["review_id"]) == N391_AUDIT_REVIEW, "N391 audit review drift")
    req(result391["scope"]["subset_cardinality"] == POPULATION_COUNT, "N391 subset count drift")
    req(result391["identity_certificate"]["terminal_rank_stream_sha256"] == POPULATION_RANK_STREAM_SHA256, "N391 population rank stream drift")
    req(result391["scope"]["subset_semantics"] == "EXACT_BOUNDED_CUT_RESIDUAL_CONTROL_IDENTITY_SUBSET_NOT_EXCLUDED_BY_CONSUMED_V24_FILTERS_NOT_EXACT_GLOBAL_RESIDUAL_SET", "N391 subset semantics drift")
    req(result391["transport_checks"]["cut193_198"]["closed_by_own_wave_count"] == 0, "N391 CUT193..198 survival drift")
    req(result391["transport_checks"]["hpadj07"]["all_97_blocks_survive"] is True, "N391 HPADJ07 survival drift")
    req(result391["transport_checks"]["certlift03"]["predicate_false_for_all_97_blocks"] is True, "N391 CERTLIFT03 survival drift")
    req(result391["transport_checks"]["n356"]["all_97_blocks_survive"] is True, "N391 N356 survival drift")
    req(result391["transport_checks"]["n357"]["all_10961_accept_n357"] is True, "N391 N357 survival drift")
    req(result391["transport_checks"]["n358"]["all_97_blocks_survive"] is True, "N391 N358 survival drift")

    current_root = Path(args.current_main_root).resolve()
    n391_main_root = Path(args.n391_main_root).resolve()
    current_main, current_demands = authority_checked(current_root)
    old_main, old_demands = authority_checked(n391_main_root)

    req((current_root / ".git").exists(), "current MAIN checkout missing git metadata")
    req((n391_main_root / ".git").exists(), "N391 MAIN checkout missing git metadata")
    current_head = subprocess.check_output(["git", "-C", str(current_root), "rev-parse", "HEAD"], text=True).strip()
    n391_head = subprocess.check_output(["git", "-C", str(n391_main_root), "rev-parse", "HEAD"], text=True).strip()
    req(current_head == CURRENT_MAIN_HEAD, "current MAIN checkout head drift")
    req(n391_head == N391_MAIN_V24_HEAD, "N391 MAIN checkout head drift")
    req(
        (current_root / "stages/stage32/MAIN-STATE.json").read_bytes()
        == (n391_main_root / "stages/stage32/MAIN-STATE.json").read_bytes(),
        "current MAIN-STATE differs from N391 audited authority source",
    )
    req(
        (current_root / "stages/stage32/proof/CROSS-LANE-DEMANDS.json").read_bytes()
        == (n391_main_root / "stages/stage32/proof/CROSS-LANE-DEMANDS.json").read_bytes(),
        "current CROSS-LANE-DEMANDS differs from N391 audited authority source",
    )
    req(current_main == old_main and current_demands == old_demands, "authority JSON object drift")
    req(current_main["current_target"]["primary_incomplete_id"] == "32-01", "current MAIN target drift")
    req(current_main["current_target"]["control_mode"] == "FULL178_AND_FINAL_MILESTONE_CHAIN", "current control mode drift")
    req(current_main["current_exact_frontier"]["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "remaining-terminal semantics drift")
    req(current_main["firewalls"]["full178_complete"] is False, "unexpected FULL178 completion")
    req(current_main["firewalls"]["merge_authorized"] is False, "unexpected merge authorization")
    req("N396" not in json.dumps(current_main, sort_keys=True), "N396 already appears in current MAIN authority; accounting would risk duplicate consumption")
    req(
        not any(d.get("status") == "OPEN" and d.get("producer_lane") in ("178", "32-01-178") for d in current_demands["demands"]),
        "OPEN producer demand preempts N397 accounting",
    )

    payload = {
        "semantics": "EXACT_CURRENT_AUTHORITY_IDENTITY_AND_NO_DOUBLE_CHARGE_ACCOUNTING_FOR_HOSTILE_AUDITED_N396_BOUNDED_PRUNING_SET",
        "current_repository_main_exact_head": CURRENT_MAIN_HEAD,
        "n391_authority_source_exact_head": N391_MAIN_V24_HEAD,
        "authority_identity": {
            "main_state_blob_sha1": CURRENT_MAIN_STATE_BLOB,
            "main_state_canonical_sha256": CURRENT_MAIN_STATE_CANONICAL,
            "cross_lane_demands_blob_sha1": CURRENT_CROSS_LANE_BLOB,
            "cross_lane_demands_canonical_sha256": CURRENT_CROSS_LANE_CANONICAL,
            "current_authority_byte_identical_to_n391_audited_source": True,
        },
        "population_identity": {
            "n391_audited_bounded_survivor_count": POPULATION_COUNT,
            "n391_terminal_rank_stream_sha256": POPULATION_RANK_STREAM_SHA256,
            "n396_audited_unsat_count": UNSAT_COUNT,
            "n396_unsat_rank_stream_sha256": UNSAT_STREAM_SHA256,
            "n396_unsat_is_audited_subset_of_n391_population": True,
        },
        "overlap_accounting": {
            "prior_consumed_v24_filter_overlap_terminal_count": 0,
            "reason": "N391 hostile-audited the full 10,961 population as surviving the consumed V24 filters, and current MAIN authority/demand bytes are unchanged from that audited authority source.",
            "double_charge": False,
            "bounded_incremental_pruning_terminals": UNSAT_COUNT,
        },
        "promotion_firewall": {
            "eligible_for_separate_main_consumption_after_n397_audit": True,
            "main_authority_subtraction_performed_by_n397": False,
            "main_pruning_credit": False,
            "full178_complete": False,
            "integral_carrier_obstruction_promoted": False,
            "effectivity_final": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "merge_authorized": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)

    print("PASS_N397_N396_CURRENT_AUTHORITY_NO_DOUBLE_CHARGE_ACCOUNTING")
    print(f"population={POPULATION_COUNT} audited_unsat={UNSAT_COUNT} prior_overlap=0 double_charge=false")
    print("N397_ACCOUNTING_JSON=" + json.dumps(payload, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
