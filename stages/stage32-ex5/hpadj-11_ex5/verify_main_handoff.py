#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
HANDOFF = HERE / "MAIN-HANDOFF.json"
CHECKPOINT = HERE / "REMOVED-BLOCK-CHECKPOINT.json"

HANDOFF_CANONICAL = "fb829bad63622cc14b415bf5b9ca685198834bac6764598e1c0d968c5d2bee84"
CHECKPOINT_BLOB = "81abb4aa2c626ec2a77b5b1e751e99f4299c55ba"
CHECKPOINT_CANONICAL = "0eff74f8adb64b3ecd8d2a3959d55686a64b57b52bcf6baabe62ac184cc1760d"
MAIN_V31_HEAD = "f5558f0d1b23c6dd48519207e1dc872ae66127d7"
MAIN_STATE_BLOB = "a7f58ca7cccee3f0e3ae538288d3298cf5571bb6"
MAIN_STATE_CANONICAL = "0da2f2bc76d0a27b12277bbcf3f823293465f7e937afb80e75940db7f8aed31e"
V31_PACKET_BLOB = "de382039b443147a48f93570b1fd8e344bc51edd"
V31_PACKET_CANONICAL = "67c90a1487233548243bd56bc3cffce0d42de5ac88420cde22e6512ad51030f8"

PRIOR = 3453268626299532038131
PROPOSED = 3360778813767800658369
TIGHTENING = 92489812531731379762
CHARACTER = "PICARD64_X0_X4_X8_X10_PARITY_V1"


def req(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit("FAIL: " + message)


def git_blob_bytes(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(value: dict) -> str:
    body = dict(value)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return hashlib.sha256(raw).hexdigest()


def load_locked_json(path: Path, blob: str, canon: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    raw = path.read_bytes()
    req(git_blob_bytes(raw) == blob, f"{label} blob drift")
    value = json.loads(raw.decode())
    req(
        value.get("canonical_sha256_without_this_field") == canon,
        f"{label} stored canonical drift",
    )
    req(canonical(value) == canon, f"{label} canonical drift")
    return value


def load_canonical_json(path: Path, canon: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    value = json.loads(path.read_text())
    req(
        value.get("canonical_sha256_without_this_field") == canon,
        f"{label} stored canonical drift",
    )
    req(canonical(value) == canon, f"{label} canonical drift")
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--main-root", required=True, type=Path)
    args = parser.parse_args()
    main_root = args.main_root.resolve()

    # Fail closed on source locks before using semantic fields.
    checkpoint = load_locked_json(
        CHECKPOINT, CHECKPOINT_BLOB, CHECKPOINT_CANONICAL, "HPADJ11 checkpoint"
    )
    handoff = load_canonical_json(HANDOFF, HANDOFF_CANONICAL, "HPADJ11 MAIN handoff")

    main_state_lock = handoff["target_main"]["source_locks"]["main_state"]
    v31_lock = handoff["target_main"]["source_locks"]["v31_bound_replacement"]
    main_state = load_locked_json(
        main_root / main_state_lock["path"],
        MAIN_STATE_BLOB,
        MAIN_STATE_CANONICAL,
        "MAIN V31 state",
    )
    v31 = load_locked_json(
        main_root / v31_lock["path"],
        V31_PACKET_BLOB,
        V31_PACKET_CANONICAL,
        "MAIN V31 replacement packet",
    )

    req(
        handoff["schema"]
        == "STAGE32EX5_HPADJ11_MAIN_BOUND_REPLACEMENT_HANDOFF_V1",
        "handoff schema drift",
    )
    req(
        handoff["producer"]["audited_exact_head"]
        == "1c694f6650125a8fb0121925beff7f800b5d6283",
        "producer audited head drift",
    )
    req(
        handoff["producer"]["hostile_audit_review_id"] == 5216065509
        and handoff["producer"]["hostile_audit_verdict"] == "PASS",
        "producer hostile-audit evidence drift",
    )
    req(
        handoff["target_main"]["v31_exact_head"] == MAIN_V31_HEAD,
        "target MAIN V31 head drift",
    )
    req(
        handoff["target_main"]["v31_hostile_audit_review_id"] == 5216133884
        and handoff["target_main"]["v31_hostile_audit_verdict"] == "PASS",
        "target MAIN V31 hostile-audit evidence drift",
    )
    req(
        handoff["target_main"]["audit_result_sync_observed"] is False,
        "handoff must not pretend V31 audit synchronization",
    )
    req(
        handoff["target_main"]["live_specialist_refresh_observed"] is False,
        "handoff must not pretend live specialist refresh",
    )

    req(
        checkpoint["candidate_bound"]["removed_block_refined_survivor_upper_bound"]
        == PROPOSED,
        "HPADJ11 checkpoint upper-bound drift",
    )
    req(
        checkpoint["candidate_bound"]["improvement_vs_td01_upper_bound"]
        == TIGHTENING,
        "HPADJ11 checkpoint tightening drift",
    )
    req(
        checkpoint["semantics"]["candidate_is_refinement_not_additive_subtraction"]
        is True,
        "HPADJ11 refinement semantics drift",
    )
    req(
        checkpoint["semantics"]["main_consumption_performed"] is False,
        "producer checkpoint unexpectedly consumed MAIN credit",
    )

    req(
        main_state["schema"]
        == "STAGE32_MAIN_COMPACT_STATE_V31_TD01_BOUND_CONSUMED_PENDING_REAUDIT",
        "MAIN V31 schema drift",
    )
    frontier = main_state["current_exact_frontier"]
    req(frontier["authoritative_remaining_strata"] == 17128, "MAIN strata drift")
    req(frontier["authoritative_remaining_terminals"] == PRIOR, "MAIN upper drift")
    req(
        frontier["authoritative_remaining_terminals_semantics"]
        == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET",
        "MAIN upper-bound semantics drift",
    )
    req(
        main_state["authority_sync"]["same_picard64_character_key"] == CHARACTER,
        "MAIN character drift",
    )
    req(
        main_state["authority_sync"]["hpadj10_additional_main_credit_after_td01_v31"]
        == 0,
        "MAIN HPADJ10 no-double-charge drift",
    )

    req(
        v31["bound"]["authoritative_remaining_terminals_after_consumption"] == PRIOR,
        "V31 packet upper drift",
    )
    req(
        v31["bound"]["composition_rule"]
        == "MIN_OF_INDEPENDENT_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING",
        "V31 composition drift",
    )
    req(
        v31["bound"]["exact_incremental_rejected_set_claimed"] is False
        and v31["bound"]["additive_subtraction_performed"] is False
        and v31["bound"]["double_charge"] is False,
        "V31 no-double-charge firewalls drift",
    )
    req(
        v31["same_character_disposition"]["character_key"] == CHARACTER,
        "V31 character drift",
    )
    req(
        v31["same_character_disposition"]["hpadj10_additional_main_credit_in_v31"]
        == 0,
        "V31 HPADJ10 additional credit drift",
    )

    transition = handoff["candidate_transition"]
    req(transition["prior_v31_upper_bound"] == PRIOR, "handoff prior upper drift")
    req(
        transition["proposed_hpadj11_upper_bound"] == PROPOSED,
        "handoff proposed upper drift",
    )
    req(
        transition["upper_bound_tightening"] == PRIOR - PROPOSED == TIGHTENING,
        "handoff tightening arithmetic drift",
    )
    req(
        transition["picard64_character_key"] == CHARACTER,
        "handoff character drift",
    )
    req(
        transition["composition_rule"]
        == "SAME_CHARACTER_REFINEMENT_MIN_REPLACEMENT__NO_ADDITIVE_STACKING",
        "handoff composition drift",
    )
    req(
        transition["exact_incremental_rejected_identity_set_available"] is False
        and transition["additive_subtraction_authorized"] is False
        and transition["hpadj10_additive_stacking_authorized"] is False
        and transition["hpadj10_additional_main_credit"] == 0
        and transition["ex5_main_authority_mutation_performed"] is False,
        "handoff no-double-charge/authority firewall drift",
    )

    req(
        all(value is False for value in handoff["firewalls"].values()),
        "handoff firewall unexpectedly raised",
    )

    print(
        json.dumps(
            {
                "verdict": "PASS_HPADJ11_MAIN_HANDOFF_SOURCE_LOCKED",
                "producer_audited_head": handoff["producer"]["audited_exact_head"],
                "target_main_v31_head": MAIN_V31_HEAD,
                "prior_upper_bound": PRIOR,
                "proposed_upper_bound": PROPOSED,
                "tightening": TIGHTENING,
                "same_character": CHARACTER,
                "main_credit_granted_by_ex5": False,
                "main_consumption_performed": False,
                "consumer_sync_required": True,
                "handoff_canonical": HANDOFF_CANONICAL,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
