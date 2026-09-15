#!/usr/bin/env python3
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
RECEIPT = HERE / "TD01-V31-MAIN-BOUND-REPLACEMENT.json"
CROSS = ROOT / "stages/stage32/proof/CROSS-LANE-DEMANDS.json"

STATE_BLOB = "a7f58ca7cccee3f0e3ae538288d3298cf5571bb6"
STATE_CANON = "0da2f2bc76d0a27b12277bbcf3f823293465f7e937afb80e75940db7f8aed31e"
RECEIPT_BLOB = "de382039b443147a48f93570b1fd8e344bc51edd"
RECEIPT_CANON = "67c90a1487233548243bd56bc3cffce0d42de5ac88420cde22e6512ad51030f8"
CROSS_BLOB = "68a02f31431ad658b42ad695f9553c67fd6cff01"
CROSS_CANON = "aec14c8c2a843e39478a287eb48d10696b1465124b2d089e0085630c66d346f5"

PRODUCER_HEAD = "54945927416a94a67533c7b06c59c5a24e50c4f1"
PRODUCER_REVIEW = 5214778974
PACKET_REL = Path("stages/stage32/32-01-178/topdown-01/EXACT-X4-ENVELOPE-BOUND.json")
PACKET_BLOB = "51271c11078459ad9171138c4fb6121d7a665c39"
PACKET_CANON = "f55bf17b7206fb81caccba46c4df7de441f5ef75fab9f422cc33148432a3242d"
HANDOFF_REL = Path("stages/stage32/32-01-178/topdown-01/AUDIT-HANDOFF.json")
HANDOFF_BLOB = "c8d4e455e51ef21a13ade2812c4de5f3179aaf85"
HANDOFF_CANON = "5ad21b989a0a56b45627ef80379c2017895f8164655e77b80760016cc327df28"
VERIFIER_REL = Path("stages/stage32/32-01-178/topdown-01/verify_td01_exact_x4_envelope_bound.py")
VERIFIER_BLOB = "4d64db072093502df2a11dbedaa108ddfa0c69b7"

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def locked_json(path: Path, expected_blob: str, expected_canon: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    req(blob(path) == expected_blob, f"{label} blob drift")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"{label} stored canonical drift")
    req(canon(obj) == expected_canon, f"{label} canonical drift")
    return obj

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--producer-root", type=Path, required=True)
    ns = ap.parse_args()

    state = locked_json(STATE, STATE_BLOB, STATE_CANON, "V31 MAIN state")
    receipt = locked_json(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON, "V31 TD01 receipt")
    cross = locked_json(CROSS, CROSS_BLOB, CROSS_CANON, "V31 cross-lane registry")

    packet = locked_json(ns.producer_root / PACKET_REL, PACKET_BLOB, PACKET_CANON, "TD01 packet")
    handoff = locked_json(ns.producer_root / HANDOFF_REL, HANDOFF_BLOB, HANDOFF_CANON, "TD01 audit handoff")
    pv = ns.producer_root / VERIFIER_REL
    req(pv.is_file() and blob(pv) == VERIFIER_BLOB, "TD01 verifier blob drift")

    req(receipt["producer"]["audited_exact_head"] == PRODUCER_HEAD, "producer head")
    req(receipt["producer"]["hostile_audit_review_id"] == PRODUCER_REVIEW, "producer review")
    req(receipt["producer"]["hostile_audit_status"] == "PASS", "producer audit")
    req(packet["main_composition_candidate"]["candidate_td01_upper_bound"] == 3453268626299532038131, "packet bound")
    req(packet["main_composition_candidate"]["current_main_upper_bound"] == 6703403803993210101494, "packet predecessor")
    req(packet["main_composition_candidate"]["rule"] == "MIN_OF_INDEPENDENT_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING", "packet composition")
    req(packet["parity_bound"]["per_block_max_retained_fraction"] == "17/33", "packet ratio")
    req(packet["parity_bound"]["exact_survivor_envelope"] == 6703403803993209250491, "packet envelope")
    req(packet["firewalls"]["main_pruning_credit"] is False, "producer self-promotion")
    req(handoff["candidate"]["td01_certified_upper_bound_candidate"] == 3453268626299532038131, "handoff bound")
    req(handoff["firewalls"]["main_authority_mutated"] is False, "handoff self-promotion")

    before = receipt["bound"]["predecessor_main_upper_bound"]
    candidate = receipt["bound"]["producer_certified_upper_bound"]
    after = receipt["bound"]["authoritative_remaining_terminals_after_consumption"]
    req(before == 6703403803993210101494, "before bound")
    req(candidate == 3453268626299532038131, "candidate bound")
    req(after == min(before, candidate), "min composition")
    req(receipt["bound"]["certified_tightening_vs_v30"] == before-after == 3250135177693678063363, "tightening")
    req(receipt["bound"]["exact_incremental_rejected_set_claimed"] is False, "exact rejected-set overclaim")
    req(receipt["bound"]["additive_subtraction_performed"] is False, "additive subtraction")
    req(receipt["bound"]["double_charge"] is False, "double charge")

    req(receipt["same_character_disposition"]["character_key"] == "PICARD64_X0_X4_X8_X10_PARITY_V1", "character key")
    req(receipt["same_character_disposition"]["hpadj10_additional_main_credit_in_v31"] == 0, "HPADJ10 duplicate credit")
    req(receipt["same_character_disposition"]["bridge_c3_additional_main_credit_in_v31"] == 0, "BRIDGE duplicate credit")

    req(receipt["claim_sync"]["claim_id"] == "S32.FULL178.NUMERICAL_CENSUS.V1", "claim id")
    req(receipt["claim_sync"]["claim_core_changed"] is False, "claim core changed")
    req(receipt["claim_sync"]["claim_registry_mutated"] is False and receipt["claim_sync"]["active_frontier_mutated"] is False, "claim registry/frontier mutation")

    req(state["current_exact_frontier"]["authoritative_remaining_terminals"] == after, "state/receipt authority")
    req(state["current"]["mainbatch_stop_gate"] == "REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED", "replacement audit gate")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "replacement firewall")
    req(state["firewalls"]["full178_complete"] is False, "FULL178 overclaim")
    req(state["firewalls"]["merge_authorized"] is False, "merge authorization")

    byid = {d["demand_id"]: d for d in cross["demands"]}
    req(byid["S32.DEMAND.TD01.178.MAIN.AUDITED_BOUND_HANDOFF.V1"]["status"] == "SATISFIED", "TD01 demand")
    req(byid["S32.DEMAND.HPADJ10.EX5.MAIN.AUDITED_POPULATION_HANDOFF.V1"]["satisfying_artifact"]["additional_main_credit"] == 0, "HPADJ10 demand credit")

    print("PASS: hostile-audited TD01 bound consumed by exact V31 min-composition")
    print("authority=3453268626299532038131 exact_rejected_set_claimed=false additive_subtraction=false")
    print("FULL178=INCOMPLETE replacement_head_hostile_reaudit_required=true merge_authorized=false")

if __name__ == "__main__":
    main()
