#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
REGISTRY=HERE/"CROSS-LANE-DEMANDS.json"
MONITOR=HERE/"ACTIVE-SPECIALIST-MONITOR-CONTRACT.json"
STATE=ROOT/"stages/stage32/MAIN-STATE.json"

REGISTRY_BLOB="68a02f31431ad658b42ad695f9553c67fd6cff01"
REGISTRY_CANON="aec14c8c2a843e39478a287eb48d10696b1465124b2d089e0085630c66d346f5"
MONITOR_BLOB="2d245205d2c4e597284fcefc6b5f6b43f8df7a2a"
MONITOR_CANON="f5b2403a76546db1c7aea61bfb3eb5b62b3141063969e819758e6911f3a54e6e"
STATE_BLOB="9b460df0b49e70513a13e0ab09aecb8fab375f90"
STATE_CANON="987e6d33b86170c78a3c9de3bfb0b39875314afb1f129160c8a2dfd97e3eabaa"
OLD_BOUND=3360778813767800658369
BOUND=195603649074545538415

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)

def blob(p):
    b=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def lock(p,b,c):
    req(blob(p)==b,f"blob drift {p}")
    o=json.loads(p.read_text())
    req(o.get("canonical_sha256_without_this_field")==c and canon(o)==c,f"canonical drift {p}")
    return o

def main():
    reg=lock(REGISTRY,REGISTRY_BLOB,REGISTRY_CANON)
    mon=lock(MONITOR,MONITOR_BLOB,MONITOR_CANON)
    st=lock(STATE,STATE_BLOB,STATE_CANON)

    req([d["demand_id"] for d in reg["demands"] if d["status"]=="OPEN"]==[],"unexpected OPEN demand")

    # The retained monitor contract remains a wiring/history boundary. Its
    # recorded heads are discovery hints only; ordinary MAIN startup performs
    # the required live sweep separately before substantive work.
    req(mon["schema"]=="STAGE32_ACTIVE_SPECIALIST_MONITOR_CONTRACT_V9_V33_AUDIT_SYNCED_FULL178_REENTRY","monitor schema")
    ls=mon["last_live_sweep"]
    req(ls["lane_178"]["semantic_leaf"]=="TD02_GRF04_BOUNDED_PROBE","retained 178 monitor")
    req(ls["mb"]["semantic_leaf"]=="MB104_ACTIVE_INCOMPLETE","retained MB monitor")
    c=mon["latest_main_consumption"]
    req(c["replacement_upper_bound"]==OLD_BOUND and c["main_consumed"] is True and c["double_charge"] is False,"historical V33 consumption")
    req(c["replacement_head_hostile_audited"] is True and c["replacement_head_hostile_audit_review_id"]==5216402010,"historical V33 audit")

    req(st["schema"]=="STAGE32_MAIN_COMPACT_STATE_V35_Q_QUADRATIC_CONSUMED_REAUDIT_PENDING_FULL178_ACTIVE","state schema")
    req(st["authority_sync"]["split_authority"]["orchestration_mode"]=="ROOT_NATIVE_STAGE32_MAIN_ONLY","orchestration mode")
    req(st["current_exact_frontier"]["authoritative_remaining_terminals"]==BOUND,"V35 authority")
    req(st["current_exact_frontier"]["predecessor_v34_authoritative_remaining_terminals"]==OLD_BOUND,"V34 predecessor")
    req(st["current"]["mainbatch_stop_gate"]=="REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED","replacement reaudit gate")
    req(st["firewalls"]["replacement_head_hostile_reaudit_required"] is True,"replacement firewall")
    req(st["current_exact_frontier"]["live_178_td02_main_handoff_ready"] is False,"178 audit-pending result silently consumed")
    req(st["current_exact_frontier"]["live_ex5_q_quadratic_refinement_main_handoff_ready"] is False,"EX5 audit-pending result silently consumed")
    req(st["firewalls"]["full178_complete"] is False and st["firewalls"]["merge_authorized"] is False,"firewalls")

    sweep=st["source_locks"]["live_specialist_sweep"]
    req(sweep["lane_178_head"]=="fd9b78e0d58bc1b05a565c75f8e2c0191586c62f" and sweep["lane_178_handoff"]=="AUDIT_PENDING_NO_MAIN_CREDIT","live 178 refresh")
    req(sweep["ex5_head"]=="47033b64c529426afe62050e78be02cd0619b6b6" and sweep["ex5_handoff"]=="AUDIT_PENDING_NO_MAIN_CREDIT","live EX5 refresh")
    req(sweep["cut_handoff"]=="NONE","CUT refresh")
    req(sweep["mb_head"]=="4b6bdd7957033ace15d9e924ac8ff787066a5ff8" and sweep["mb_handoff"]=="NONE","MB refresh")

    print("PASS: Stage32 V35 q-quadratic authority transition keeps specialist handoffs separate and zero-credit")
    print("PASS: replacement head is fail-closed pending hostile reaudit; FULL178 remains incomplete")

if __name__=="__main__":
    main()
