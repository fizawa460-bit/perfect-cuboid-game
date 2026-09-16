#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
CROSS = HERE / "proof/verify_cross_lane_demands.py"
MONITOR = HERE / "proof/ACTIVE-SPECIALIST-MONITOR-CONTRACT.json"
RECEIPT = HERE / "management/td01-main-disposition/TD01-V32-HOSTILE-AUDIT-PASS-SYNC.json"
SYNC_VERIFIER = HERE / "management/td01-main-disposition/verify_td01_v32_audit_sync.py"
CLAIMS = HERE / "proof/CLAIM-REGISTRY.json"
FRONTIER = HERE / "proof/ACTIVE-FRONTIER.json"
ADAPTERS = HERE / "proof/LANE-ADAPTERS.json"

STATE_BLOB = "6fdcd15090d7951467675e0f732b6ce54c09d69d"
STATE_CANON = "7c318668df1c9fe5f1670ed52bedffed7a21c5b2f0d0fbbffc6f1fa73b5bfa47"
CROSS_BLOB = "72a9258edc25af1bccb9cb6078b20967c56ed7df"
MONITOR_BLOB = "bda53115a294d81d504ec82965b050c87430e69d"
MONITOR_CANON = "49eb62b32752726555d17ee302734ef983240080a1b8f0450a33d67cd9eae406"
RECEIPT_BLOB = "79be8d2fddaaea656f015b1b858834ca48aeb960"
RECEIPT_CANON = "0f504c054e951763580c7aadf293c38600c3cf201e4c8c6055006ee80f4a69bb"
SYNC_VERIFIER_BLOB = "bda8ae6ba16c43b54a022e7c80c83faaa47a4647"
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
    req(blob(STATE) == STATE_BLOB, "V32 state blob drift")
    state = json.loads(STATE.read_text(encoding="utf-8"))
    req(state.get("canonical_sha256_without_this_field") == STATE_CANON and canon(state) == STATE_CANON, "V32 state canonical drift")
    req(blob(CROSS) == CROSS_BLOB, "V32 cross-lane verifier drift")
    req(blob(MONITOR) == MONITOR_BLOB, "V32 monitor blob drift")
    mon = json.loads(MONITOR.read_text(encoding="utf-8"))
    req(mon.get("canonical_sha256_without_this_field") == MONITOR_CANON and canon(mon) == MONITOR_CANON, "V32 monitor canonical drift")
    req(blob(RECEIPT) == RECEIPT_BLOB, "V32 receipt blob drift")
    rec = json.loads(RECEIPT.read_text(encoding="utf-8"))
    req(rec.get("canonical_sha256_without_this_field") == RECEIPT_CANON and canon(rec) == RECEIPT_CANON, "V32 receipt canonical drift")
    req(blob(SYNC_VERIFIER) == SYNC_VERIFIER_BLOB, "V32 sync verifier drift")
    req(blob(CLAIMS) == CLAIMS_BLOB, "claim registry changed during audit sync")
    req(blob(FRONTIER) == FRONTIER_BLOB, "active frontier changed during audit sync")
    req(blob(ADAPTERS) == ADAPTERS_BLOB, "lane adapters changed during audit sync")

    runpy.run_path(str(CROSS), run_name="__main__")

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V32_TD01_AUDIT_SYNCED_HPADJ11_QUEUED", "state schema")
    req(state["current_exact_frontier"]["authoritative_remaining_strata"] == 17128, "strata")
    req(state["current_exact_frontier"]["authoritative_remaining_terminals"] == 3453268626299532038131, "authority")
    req(state["current_exact_frontier"]["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "authority semantics")
    req(state["current"]["mainbatch_stop_gate"] == "NONE", "stop gate")
    req(state["current"]["next_exact_route"] == "HPADJ11_V33_SAME_CHARACTER_BOUND_REPLACEMENT", "next route")
    req(state["current_exact_frontier"]["v31_td01_replacement_hostile_audited"] is True, "V31 audit sync")
    req(state["current_exact_frontier"]["v31_td01_replacement_hostile_audit_review_id"] == 5216133884, "V31 audit review")
    req(state["current_exact_frontier"]["hpadj11_producer_hostile_audited"] is True, "HPADJ11 audit")
    req(state["current_exact_frontier"]["hpadj11_main_consumption_performed"] is False, "HPADJ11 consumed in sync")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is False, "replacement re-audit")
    req(state["firewalls"]["full178_complete"] is False and state["firewalls"]["stage32_closed"] is False, "closure firewall")
    req(state["firewalls"]["merge_authorized"] is False, "merge firewall")

    print("PASS: Stage32 MAIN V32 V31-audit synchronization retained with zero new pruning")
    print("FULL178=ACTIVE_INCOMPLETE authority=3453268626299532038131 stop_gate=NONE HPADJ11=audited_queued")

if __name__ == "__main__":
    main()
