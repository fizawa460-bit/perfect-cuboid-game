#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, runpy
from pathlib import Path
HERE=Path(__file__).resolve().parent
STATE=HERE/"MAIN-STATE.json"
SYNCV=HERE/"management/cut201-main-disposition/verify_cut201_v28_audit_sync.py"
REG=HERE/"proof/CROSS-LANE-DEMANDS.json"
MON=HERE/"proof/ACTIVE-SPECIALIST-MONITOR-CONTRACT.json"
def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    d=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(d)).encode()+b"\0"+d).hexdigest()
def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def locked(p,b,c):
    req(blob(p)==b,f"blob drift {p}"); o=json.loads(p.read_text()); req(o.get("canonical_sha256_without_this_field")==c and canon(o)==c,f"canonical drift {p}"); return o
def main():
    req(blob(SYNCV)=="b8af5c304382e4086286e1be4b3eeb107babb979","sync verifier drift"); runpy.run_path(str(SYNCV),run_name="__main__")
    s=locked(STATE,"69dd727697ab3f8d464f8a48e7bc708739d6973a","29859578ce1c4e2372379cd508595e767393d676c0b6429e7de3bc8691998fc9")
    r=locked(REG,"e14bea1a62ec287710064a96f80abe57f8b0c3f4","9a30646b5567adb30f0192b43f89a8d8a01d1464199b2f0a0d19e1138a7d9c74")
    m=locked(MON,"53f286f78574cfad59fc397a9d3268d345331594","48a0f92b1325e80507594c25e8d78dd28a0f0bf5d624bc1afd6d9d43be56e32c")
    by={d["demand_id"]:d for d in r["demands"]}; req(by["S32.DEMAND.CUT201.CUT.MAIN.V26_CURRENT_AUTHORITY_ADAPTER.V1"]["status"]=="SATISFIED","CUT201 demand")
    ls={x["lane"]:x for x in m["active_specialists"]}; req(ls["CUT"]["pending_main_handoff_ids"]==[],"CUT handoff")
    req(s["current"]["mainbatch_stop_gate"]=="NONE" and s["current_exact_frontier"]["authoritative_remaining_terminals"]==26876434389242951065128,"MAIN authority")
    print("PASS: Stage32 MAIN V28 CUT201 hostile-audit synchronization authority")
if __name__=="__main__": main()
