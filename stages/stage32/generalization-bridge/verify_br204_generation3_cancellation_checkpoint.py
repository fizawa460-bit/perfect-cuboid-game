#!/usr/bin/env python3
import json
from pathlib import Path
def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
x=json.loads(Path("stages/stage32/generalization-bridge/BR204-GENERATION3-CANCELLATION-CHECKPOINT.json").read_text())
req(x["schema"]=="STAGE32_BR204_GENERATION3_CANCELLATION_CHECKPOINT_V1","schema")
r=x["generation3_run"]; req(r["run_id"]==35473398160 and r["execution_head"]=="065b610d84e414d488cf36e299efb2ca67722ae4" and r["conclusion"]=="cancelled","run identity")
q=x["reconciliation"]; req((q["expected_target_count"],q["complete_canonical_d_count"],q["partial_target_count"],q["missing_target_count"])==(69,0,1,68),"counts")
req(q["partial_targets"]==[{"b":3,"d":148,"stop_reason":"IN_PROGRESS"}],"partial")
req(q["sole_partial_finalizer"]["retained_bc64_children"]==[] and q["sole_partial_finalizer"]["validated_bc16_payloads"]==[],"unexpected G3 carry")
e=x["expired_generation2_carry"]; req((e["b"],e["d"],e["parent_bc16_index"])==(2,148,0) and e["expired"] and not e["exact_bytes_available"] and not e["carry_authorized"],"expired G2 carry")
req(x["next_recovery"]["exact_bc64_children"]==[0,16,32,48] and not x["next_recovery"]["broader_69_target_recovery_authorized"],"repair firewall")
req(all(v is False for v in x["credit"].values()),"credit")
t=json.loads(Path("stages/stage32/generalization-bridge/BR204-GENERATION3-RECOVERY-TARGETS.json").read_text())
expected={(int(v["b"]),int(v["d"])) for v in t["targets"]}; miss={tuple(v) for v in q["missing_targets"]}
req(len(expected)==69 and len(miss)==68 and miss|{(3,148)}==expected,"coverage")
print("PASS generation3 cancellation checkpoint")
