#!/usr/bin/env python3
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
CONTRACT=HERE/"HPADJ23-MEASUREMENT-EXECUTION-CONTRACT.json"
PREFLIGHT=HERE/"HPADJ23-FULL178-SCALEOUT-PREFLIGHT.json"
RUNNER=HERE/"measure_scaleout_shard.py"
SHARD=HERE/"build_exact_t_joint_histogram_shard.py"
RUNKEY=ROOT/"stages/stage32-ex5/runkeys/hpadj23-scaleout-measurement.json"

LOCKS={
 "contract_blob":"bd54d80e18f2721d80f00a873e38471bfa010bf3",
 "contract_canon":"5ff7e45a1153ec192e3c2b8cd9118385f228e77d7493b4cce007c11f9f14699d",
 "preflight_blob":"0b71f07f3bfbb0497ddb0be9a0b5ad28681780b6",
 "preflight_canon":"7c2422f74dd39a53be844468d738aa061d531409740af480998e62bc0fa04b3d",
 "runner_blob":"2fe44f3ccc97ef051cfdbbd42124ecad3a45b623",
 "shard_blob":"25284ea56c0746912318ce3c0d0e75d50cf60458",
}

def req(v:bool,msg:str)->None:
    if not v:
        raise SystemExit("FAIL: "+msg)

def blob(path:Path)->str:
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def canon(obj:dict)->str:
    body=dict(obj)
    body.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def locked_json(path:Path,b:str,c:str,label:str)->dict:
    req(path.is_file(),f"missing {label}")
    req(blob(path)==b,f"{label} blob drift")
    obj=json.loads(path.read_text())
    req(obj.get("canonical_sha256_without_this_field")==c,f"{label} stored canonical drift")
    req(canon(obj)==c,f"{label} canonical drift")
    return obj

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--require-armed",action="store_true")
    ap.add_argument("--expected-head")
    args=ap.parse_args()

    contract=locked_json(CONTRACT,LOCKS["contract_blob"],LOCKS["contract_canon"],"measurement contract")
    preflight=locked_json(PREFLIGHT,LOCKS["preflight_blob"],LOCKS["preflight_canon"],"scaleout preflight")
    req(blob(RUNNER)==LOCKS["runner_blob"],"measurement runner drift")
    req(blob(SHARD)==LOCKS["shard_blob"],"shard builder drift")

    key=json.loads(RUNKEY.read_text())
    req(key["schema"]=="STAGE32EX5_HPADJ23_SCALEOUT_MEASUREMENT_RUNKEY_V1","runkey schema")
    req(key["route_id"]=="HPADJ-23_ex5","runkey route")
    req(key["canonical_sha256_without_this_field"]==canon(key),"runkey canonical drift")
    req(key["measurement_target"]=={"H":32,"b_start":0,"b_stop":11},"runkey target")
    req(key["source_locks"]["shard_builder_blob_sha1"]==LOCKS["shard_blob"],"runkey shard lock")
    req(key["source_locks"]["scaleout_preflight_canonical_sha256"]==LOCKS["preflight_canon"],"runkey preflight lock")
    req(all(v is False for v in key["credit"].values()),"runkey credit firewall")

    req(contract["source_locks"]["scaleout_preflight_canonical_sha256"]==LOCKS["preflight_canon"],"contract preflight lock")
    req(contract["source_locks"]["measurement_runner_blob_sha1"]==LOCKS["runner_blob"],"contract runner lock")
    req(contract["source_locks"]["shard_builder_blob_sha1"]==LOCKS["shard_blob"],"contract shard lock")
    req(contract["target"]==key["measurement_target"],"contract/runkey target mismatch")
    req(contract["execution"]["production_scaleout_in_same_run"] is False,"measurement run can trigger production")
    req(all(v is False for v in contract["firewalls"].values()),"contract credit firewall")
    req(preflight["authorization"]["full178_production_armed"] is False,"preflight production already armed")

    armed=bool(key["armed"])
    if args.require_armed:
        req(armed,"measurement runkey is not armed")
    if armed:
        req(int(key["generation"])>=1,"armed generation must be >=1")
        req(key["mode"]=="MEASUREMENT","armed runkey mode")
        req(key["authorized_operation"]=="H32_B0_11_MEASUREMENT","armed operation")
        head=key.get("exact_execution_head")
        req(isinstance(head,str) and re.fullmatch(r"[0-9a-f]{40}",head) is not None,"armed exact execution head")
        if args.expected_head is not None:
            req(head==args.expected_head,"runkey exact head mismatch")
    else:
        req(int(key["generation"])==0,"cold generation drift")
        req(key["mode"]=="COLD" and key["authorized_operation"]=="NONE","cold mode/operation drift")
        req(args.expected_head is None or not args.require_armed,"expected head only meaningful for armed run")

    print(json.dumps({
      "verdict":"PASS_HPADJ23_MEASUREMENT_AUTHORIZATION",
      "generation":int(key["generation"]),
      "armed":armed,
      "target":key["measurement_target"],
      "production_authorized":False,
      "main_credit":False,
    },sort_keys=True))

if __name__=="__main__":
    main()
