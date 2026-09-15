#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
REGISTRY=HERE/"CROSS-LANE-DEMANDS.json"
MONITOR=HERE/"ACTIVE-SPECIALIST-MONITOR-CONTRACT.json"
STATE=ROOT/"stages/stage32/MAIN-STATE.json"
REGISTRY_BLOB="68a02f31431ad658b42ad695f9553c67fd6cff01"
REGISTRY_CANON="aec14c8c2a843e39478a287eb48d10696b1465124b2d089e0085630c66d346f5"
MONITOR_BLOB="803b7148e240b7f50aa6df33bdbafcacbcf2b46c"
MONITOR_CANON="7b79bbc01cd2f501bfcf2cd737025ef13821a3bc72b4848aa8da8a5e576f0523"
STATE_BLOB="d67244969defc7da77dfc431346e0d045da0978d"
STATE_CANON="3ab94343566377b4a5a7646f1334b13968ba15f363c9f63fcb48a66e3b5b9398"
CHARACTER_KEY="PICARD64_X0_X4_X8_X10_PARITY_V1"
OLD=3453268626299532038131
NEW=3360778813767800658369
def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)
def blob(p):
    raw=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None); return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def locked(p,b,c):
    req(blob(p)==b,f"blob drift {p}"); o=json.loads(p.read_text()); req(o.get("canonical_sha256_without_this_field")==c and canon(o)==c,f"canonical drift {p}"); return o
def main():
    reg=locked(REGISTRY,REGISTRY_BLOB,REGISTRY_CANON); mon=locked(MONITOR,MONITOR_BLOB,MONITOR_CANON); st=locked(STATE,STATE_BLOB,STATE_CANON)
    req([d["demand_id"] for d in reg["demands"] if d["status"]=="OPEN"]==[],"unexpected OPEN demand")
    td=[x for x in reg["audited_result_consumption"] if x["result_id"]=="S32.TD01.V31.CERTIFIED_UPPER_BOUND_REPLACEMENT.V1"]
    req(len(td)==1 and td[0]["authoritative_remaining_terminals_after_consumption"]==OLD,"TD01 historical ledger")
    req(mon["schema"]=="STAGE32_ACTIVE_SPECIALIST_MONITOR_CONTRACT_V8_HPADJ11_V33_CONSUMED","monitor schema")
    c=mon["latest_main_consumption"]
    req(c["same_character_key"]==CHARACTER_KEY and c["predecessor_upper_bound"]==OLD and c["replacement_upper_bound"]==NEW,"monitor replacement")
    req(c["main_consumed"] is True and c["double_charge"] is False,"monitor credit")
    req(st["schema"]=="STAGE32_MAIN_COMPACT_STATE_V33_HPADJ11_BOUND_CONSUMED_PENDING_REAUDIT","state schema")
    f=st["current_exact_frontier"]
    req(f["authoritative_remaining_terminals"]==NEW,"V33 authority")
    req(f["hpadj11_main_consumption_performed"] is True,"HPADJ11 consumption")
    req(f["hpadj11_composition_rule"]=="MIN_OF_SAME_CHARACTER_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING","composition")
    req(f["hpadj11_exact_incremental_rejected_set_vs_v32_claimed"] is False and f["hpadj11_additive_subtraction_against_v32_performed"] is False and f["hpadj11_double_charge"] is False,"no double charge")
    req(st["current"]["mainbatch_stop_gate"]=="REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED","V33 stop gate")
    req(st["firewalls"]["replacement_head_hostile_reaudit_required"] is True,"V33 audit firewall")
    req(st["firewalls"]["full178_complete"] is False and st["firewalls"]["merge_authorized"] is False,"firewalls")
    print("PASS: Stage32 V33 consumes hostile-audited HPADJ11 once as a same-character min replacement")
    print("PASS: TD01/HPADJ10 are not recharged; FULL178 remains incomplete; replacement head requires hostile re-audit")
if __name__=="__main__": main()
