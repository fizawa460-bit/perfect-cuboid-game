#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[0]
B2 = HERE / "breadth-cycle-2"
STATE = HERE / "MAIN-STATE.json"
SYNC = HERE / "LIVE-MAIN-COORDINATION-SYNC-20260914.json"
RUNKEY = HERE / "runkeys/bc2-39-fresh-unknown30-replay.json"
PREFLIGHT = B2 / "bc2-39-fresh-unknown30-replay-preflight.json"
SOURCE = B2 / "bc2_39_replay_explicit_fresh_unknown30.py"
PREFLIGHT_VERIFIER = B2 / "verify_bc2_39_preflight.py"
CONSUME38_VERIFIER = B2 / "verify_bc2_38_audit_consumption.py"
WORKFLOW = ROOT.parent / ".github/workflows/stage32-ex5-main.yml"

SYNC_BLOB = "c9a3a878413df5afc634f99b94707534412b5d84"
SYNC_CANON = "fd5c7c6d025286a5677b7dcab5113f066dff83574c4647d772d89c7799b8be6c"
RUNKEY_BLOB = "48dcc39fd06d5714bb54a8485a909de0a13363b8"
PREFLIGHT_BLOB = "e3dab72865d734f2420fb71ddf3c29115f9df68e"
PREFLIGHT_CANON = "7bda94c5869c988892c979873f13a1c311debedbbe9fcc670a253e339fb5e435"
SOURCE_BLOB = "e322029cfc4476ce8cf3685ca04f35b58e2ce9f2"
PREFLIGHT_VERIFIER_BLOB = "c01b18384c63bb8a7f3bd58a53633b4dd63e62da"
CONSUME38_VERIFIER_BLOB = "9204ee2779dd81580e77d615a3dd80125a119f79"
UNKNOWN30_SHA = "d60d873c4fc66ebb6cda0530d4137e5fd195fe1b601b0a21e91f873c1df28fb7"
AUDIT38_HEAD = "5e1d07e4c92fbecff9bfa89b0bfb65cdaf564a71"
AUDIT38_REVIEW = 5190676180


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def canon(obj: dict) -> str:
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(q, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    s = json.loads(STATE.read_text())
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V31_BC2_38_AUDIT_CONSUMED_BC2_39_EXECUTION", "schema")
    b = s["bootstrap"]
    req(b["active_work_pr"] == 1776 and b["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch" and b["merge_authorized"] is False, "bootstrap")
    req(b["live_main_coordination_head"] == "9d4a24ef479d031e9c4b85001fe8f7a10198b17d", "live MAIN coordination head")

    req(blob(SYNC) == SYNC_BLOB, "live MAIN sync blob")
    sync = json.loads(SYNC.read_text())
    req(sync["canonical_sha256_without_this_field"] == SYNC_CANON and canon(sync) == SYNC_CANON, "live MAIN sync canonical")
    lm = sync["live_main_state"]
    req(lm["schema"] == "STAGE32_MAIN_COMPACT_STATE_V24_HPADJ07_AUDIT_SYNCED" and lm["mainbatch_stop_gate"] == "NONE", "live MAIN route")
    req(lm["authoritative_remaining_strata"] == 17128 and lm["certified_remaining_terminal_upper_bound"] == 26876434389242951089388, "live MAIN authority projection")
    req(lm["remaining_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET" and lm["full178_complete"] is False, "live MAIN terminal semantics")
    req(sync["live_cross_lane_registry"]["open_ex5_producer_demand_count"] == 0, "OPEN EX5 producer demand")
    req(sync["firewalls"]["terminal_to_picard64_handoff_reopened"] is False, "terminal-to-Picard64 handoff reopened")
    req(sync["ex5_routing_interpretation"]["single_bounded_replay_authorized_by_mainbatch_command"] is True and sync["ex5_routing_interpretation"]["heavy_scaleout_authorized"] is False, "bounded route authorization")

    ma = s["stage32_main_authority"]
    req(ma["current_main_schema"] == lm["schema"] and ma["authoritative_remaining_strata"] == 17128 and ma["certified_remaining_terminal_upper_bound"] == 26876434389242951089388, "MAIN authority sync")
    req(ma["remaining_terminal_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET" and ma["full178_numerical_census_complete"] is False and ma["mainbatch_stop_gate"] == "NONE", "MAIN authority semantics")
    route = s["cross_lane_routing"]
    req(route["live_registry_blob_sha"] == "e2949866d41a78ff9169bdb23a2fcefb6d0f5dcd" and route["open_ex5_producer_demand_count"] == 0 and route["local_bc2_39_execution_may_continue"] is True, "cross-lane routing")

    req(blob(PREFLIGHT) == PREFLIGHT_BLOB and blob(SOURCE) == SOURCE_BLOB, "BC2-39 source/preflight identity")
    pf = json.loads(PREFLIGHT.read_text())
    req(pf["canonical_sha256_without_this_field"] == PREFLIGHT_CANON and canon(pf) == PREFLIGHT_CANON, "BC2-39 preflight canonical")
    req(blob(PREFLIGHT_VERIFIER) == PREFLIGHT_VERIFIER_BLOB and blob(CONSUME38_VERIFIER) == CONSUME38_VERIFIER_BLOB, "BC2-39 verifier identity")

    req(blob(RUNKEY) == RUNKEY_BLOB, "BC2-39 armed runkey blob")
    rk = json.loads(RUNKEY.read_text())
    req(rk["schema"] == "STAGE32EX5_BC2_39_FRESH_UNKNOWN30_REPLAY_RUNKEY_V1" and rk["generation"] == 1 and rk["armed"] is True, "BC2-39 fresh runkey")
    req(rk["source_git_blob_sha"] == SOURCE_BLOB and rk["preflight_git_blob_sha"] == PREFLIGHT_BLOB and rk["preflight_canonical"] == PREFLIGHT_CANON, "BC2-39 runkey source locks")
    t = rk["target"]
    req(t["fresh_unknown_parent_count"] == 30 and t["fresh_unknown_parent_indices_sha256"] == UNKNOWN30_SHA and t["prior_audited_unsat_count"] == 7306 and t["targeted_replay_only"] is True, "BC2-39 runkey target")
    ex = rk["execution"]
    req(ex["per_parent_timeout_ms"] == 160000 and ex["effective_heavy_concurrency"] == 1 and ex["heavy_scaleout_authorized"] is False and ex["compact_result_only"] is True, "BC2-39 bounded runkey")
    a = rk["audit_consumption"]
    req(a["bc2_38_hostile_audit_status"] == "PASS" and a["bc2_38_hostile_audit_exact_head"] == AUDIT38_HEAD and a["bc2_38_hostile_audit_review_id"] == AUDIT38_REVIEW, "BC2-38 audit consumption")

    f = s["frontier"]
    req(f["e8_bc2_38_audited"] is True and f["e8_known_parent_unsat_count_lower_bound"] == 7306 and f["e8_bc2_38_remaining_unknown_count"] == 30 and f["e8_bc2_38_remaining_unknown_parent_indices_sha256"] == UNKNOWN30_SHA, "BC2-38 consumed frontier")
    req(f["e8_bc2_39_executed"] is False and f["e8_bc2_39_audited"] is False and f["e8_bc2_39_target_unknown_count"] == 30 and f["e8_bc2_39_target_unknown_parent_indices_sha256"] == UNKNOWN30_SHA, "BC2-39 execution frontier")
    cur = s["current"]
    req(cur["status"] == "BC2_38_HOSTILE_AUDIT_PASS_CONSUMED_BC2_39_EXECUTION_AUTHORIZED" and cur["next_route"] == "BC2_39_REFINE_REMAINING_FRESH_UNKNOWN_SET", "current route")
    ib = s["intermediate_audit_boundary"]
    req(ib["last_hostile_audit_status"] == "PASS" and ib["last_hostile_audit_exact_head"] == AUDIT38_HEAD and ib["last_hostile_audit_review_id"] == AUDIT38_REVIEW, "last hostile audit")
    req(ib["bc2_39_execution_authorized"] is True and ib["freeze_active"] is False and ib["new_audit_boundary_exists"] is False and ib["re_audit_required"] is False, "execution boundary")
    ns = s["next_step"]
    req(ns["id"] == "BC2_39_REFINE_REMAINING_FRESH_UNKNOWN_SET" and ns["bc2_39_execution_authorized"] is True and ns["bc2_40_blocked_until_bc2_39_hostile_audit_pass"] is True and ns["heavy_scaleout_authorized"] is False, "next-step firewall")

    for sec in ("historical_credit_firewall", "firewalls"):
        for key, value in s[sec].items():
            req(value is False, "firewall " + sec + "." + key)
    for key, value in s["credit"].items():
        if key != "level":
            req(value is False, "credit " + key)

    wf = WORKFLOW.read_text()
    req("authorize-bc2-39-fresh-unknown30:" in wf and "\n  bc2-39-fresh-unknown30:" in wf, "BC2-39 heavy gate missing")
    req("authorize-bc2-38-fresh-unknown34:" not in wf and "\n  bc2-38-fresh-unknown34:" not in wf, "BC2-38 heavy not retired")
    req("bc2-39-fresh-unknown30-replay.json" in wf and "160000" in wf, "BC2-39 workflow lock missing")

    subprocess.run([sys.executable, str(CONSUME38_VERIFIER)], check=True)
    subprocess.run([sys.executable, str(PREFLIGHT_VERIFIER)], check=True)
    subprocess.run([sys.executable, "-m", "py_compile", str(SOURCE)], check=True)

    print("PASS: Stage32EX5 V31 consumed BC2-38 audit and armed one bounded BC2-39 replay")
    print("audited_lower_bound=7306 target_unknown=30 timeout_ms=160000 concurrency=1 scaleout=NO main_credit=NO merge=NO")


if __name__ == "__main__":
    main()
