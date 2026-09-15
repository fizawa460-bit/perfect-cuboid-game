#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
CROSS = HERE / "proof/verify_cross_lane_demands.py"
RECEIPT = HERE / "management/td01-main-disposition/TD01-V31-MAIN-BOUND-REPLACEMENT.json"
CLAIMS = HERE / "proof/CLAIM-REGISTRY.json"
FRONTIER = HERE / "proof/ACTIVE-FRONTIER.json"
ADAPTERS = HERE / "proof/LANE-ADAPTERS.json"

STATE_BLOB = "a7f58ca7cccee3f0e3ae538288d3298cf5571bb6"
STATE_CANON = "0da2f2bc76d0a27b12277bbcf3f823293465f7e937afb80e75940db7f8aed31e"
CROSS_BLOB = "f900700f3c20d27d9989a17ed23ae20903a96412"
RECEIPT_BLOB = "de382039b443147a48f93570b1fd8e344bc51edd"
RECEIPT_CANON = "67c90a1487233548243bd56bc3cffce0d42de5ac88420cde22e6512ad51030f8"
CLAIMS_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
ADAPTERS_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"

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

def main() -> None:
    req(blob(STATE) == STATE_BLOB, "V31 state blob drift")
    state = json.loads(STATE.read_text(encoding="utf-8"))
    req(state.get("canonical_sha256_without_this_field") == STATE_CANON and canon(state) == STATE_CANON, "V31 state canonical drift")
    req(blob(CROSS) == CROSS_BLOB, "V31 cross-lane verifier drift")
    req(blob(RECEIPT) == RECEIPT_BLOB, "V31 receipt blob drift")
    rec = json.loads(RECEIPT.read_text(encoding="utf-8"))
    req(rec.get("canonical_sha256_without_this_field") == RECEIPT_CANON and canon(rec) == RECEIPT_CANON, "V31 receipt canonical drift")
    req(blob(CLAIMS) == CLAIMS_BLOB, "claim registry changed during numeric-bound sync")
    req(blob(FRONTIER) == FRONTIER_BLOB, "active frontier changed during numeric-bound sync")
    req(blob(ADAPTERS) == ADAPTERS_BLOB, "lane adapters changed during numeric-bound sync")

    runpy.run_path(str(CROSS), run_name="__main__")

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V31_TD01_BOUND_CONSUMED_PENDING_REAUDIT", "state schema")
    req(state["current_exact_frontier"]["authoritative_remaining_strata"] == 17128, "strata")
    req(state["current_exact_frontier"]["authoritative_remaining_terminals"] == 3453268626299532038131, "authority")
    req(state["current_exact_frontier"]["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "authority semantics")
    req(state["current"]["mainbatch_stop_gate"] == "REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED", "stop gate")
    req(state["current_exact_frontier"]["td01_composition_rule"] == "MIN_OF_INDEPENDENT_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING", "composition")
    req(state["current_exact_frontier"]["td01_exact_incremental_rejected_set_vs_v30_claimed"] is False, "rejected-set claim")
    req(state["current_exact_frontier"]["td01_additive_subtraction_against_v30_performed"] is False, "additive subtraction")
    req(state["current_exact_frontier"]["hpadj10_main_additive_credit"] == 0, "HPADJ10 credit")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "replacement re-audit")
    req(state["firewalls"]["full178_complete"] is False and state["firewalls"]["stage32_closed"] is False, "closure firewall")
    req(state["firewalls"]["merge_authorized"] is False, "merge firewall")

    print("PASS: Stage32 MAIN V31 TD01 certified-bound replacement retained as pending hostile re-audit")
    print("FULL178=ACTIVE_INCOMPLETE authority=3453268626299532038131 stop_gate=REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED")

if __name__ == "__main__":
    main()
