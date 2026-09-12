#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
STAGE=HERE.parent
ROOT=STAGE.parents[1]
STATE=STAGE/"MAIN-STATE.json"
RECEIPT=STAGE/"management/post-cut193-cut197-cut198-current-v21-batch-composition-consumption-20260913.json"
STATE_BLOB="80fb35c79854bfdf775dc5b94c331f5f8a535ced"
STATE_CANON="82ca200d81b0ce844b1756dc0c3205eec388a20cae312af5e0f3c55d959d491c"
RECEIPT_BLOB="84c1c37b5bf9ad5b42b566eeca032b631f4c4cdf"
RECEIPT_CANON="1ac16af0b323d28ad216fc3c2d2101782a14d9f8eebcd13f6128f5bb4e572121"
AUTH=47589703313957134804198
def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    r=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(r)).encode()+b"\0"+r).hexdigest()
def canon(o):
    c=dict(o); c.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(c,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def lock(p,b,c):
    req(p.is_file(),f"missing {p.relative_to(ROOT)}"); req(blob(p)==b,f"blob drift {p.relative_to(ROOT)}")
    o=json.loads(p.read_text()); req(o.get("canonical_sha256_without_this_field")==c,f"stored canonical drift {p.relative_to(ROOT)}"); req(canon(o)==c,f"canonical drift {p.relative_to(ROOT)}"); return o
def main():
    s=lock(STATE,STATE_BLOB,STATE_CANON); r=lock(RECEIPT,RECEIPT_BLOB,RECEIPT_CANON); f=s["current_exact_frontier"]
    req(f["authoritative_remaining_strata"]==17128 and f["authoritative_remaining_terminals"]==AUTH,"authority drift")
    for k in ("cut191_main_pruning_credit","cut193_main_pruning_credit","cut194_main_pruning_credit","cut195_main_pruning_credit","cut196_main_pruning_credit","cut197_main_pruning_credit","cut198_main_pruning_credit","n358_main_pruning_credit"): req(f[k] is True,f"consumed credit drift {k}")
    req(f["n372_candidate_hostile_audited"] is True and f["n372_candidate_hostile_audit_review_id"]==5187357950,"N372 audit drift")
    req(f["n372_current_authority_rebased"] is True and f["n372_current_authority_witness"] is True and f["n372_survives_batch_cut193_cut197_cut198"] is True,"N372 current authority drift")
    req(f["n372_main_pruning_credit"] is False and f["n372_full178_credit"] is False and f["n372_effectivity_final_credit"] is False,"N372 overcredit")
    req(r["composition"]["double_charge"] is False,"double charge")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,"closure drift")
    req(s["firewalls"]["merge_authorized"] is False,"merge authorized")
    print(json.dumps({"verdict":"PASS_STAGE32_CROSS_LANE_DEMAND_COORDINATION_V22","authoritative_remaining_terminals":AUTH,"batch_cuts_consumed":["CUT193","CUT197","CUT198"],"n372_current_authority_witness":True,"full178_complete":False,"merge_authorized":False},sort_keys=True))
if __name__=="__main__": main()
