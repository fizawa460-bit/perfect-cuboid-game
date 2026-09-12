#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
STATE=HERE/"MAIN-STATE.json"
RECEIPT=HERE/"management/post-cut193-cut197-cut198-current-v21-batch-composition-consumption-20260913.json"
STATE_BLOB="80fb35c79854bfdf775dc5b94c331f5f8a535ced"
STATE_CANON="82ca200d81b0ce844b1756dc0c3205eec388a20cae312af5e0f3c55d959d491c"
RECEIPT_BLOB="84c1c37b5bf9ad5b42b566eeca032b631f4c4cdf"
RECEIPT_CANON="1ac16af0b323d28ad216fc3c2d2101782a14d9f8eebcd13f6128f5bb4e572121"
POST=47589703313957134804198
TOTAL=81925
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
    req(f["authoritative_remaining_strata"]==17128 and f["authoritative_remaining_terminals"]==POST,"authority drift")
    req(f["batch_cut_incremental_rejected_terminals"]==TOTAL,"batch increment drift")
    for k in ("cut193_main_pruning_credit","cut197_main_pruning_credit","cut198_main_pruning_credit"): req(f[k] is True,f"credit missing {k}")
    for k in ("batch_cut_mutual_overlap_terminals","batch_cut_overlap_with_consumed_cuts_terminals","batch_cut_overlap_with_n357_terminals","batch_cut_overlap_with_n358_terminals"): req(f[k]==0,f"overlap nonzero {k}")
    req(f["n372_current_authority_witness"] is True and f["n372_survives_batch_cut193_cut197_cut198"] is True,"N372 witness lost")
    req(f["n372_main_pruning_credit"] is False and f["n372_full178_credit"] is False and f["n372_effectivity_final_credit"] is False,"N372 overcredit")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,"closure overcredit")
    req(r["composition"]["double_charge"] is False and r["authority"]["after_remaining_terminals"]==POST,"receipt drift")
    for k in ("receiver_credit","theorem_credit","endpoint_credit","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized"): req(s["firewalls"][k] is False,f"firewall opened {k}")
    req(s["firewalls"]["replacement_head_hostile_reaudit_required"] is True,"reaudit gate missing")
    print(json.dumps({"verdict":"PASS_STAGE32_MAIN_STARTUP_AUTHORITY_V22_BATCH_CUT_COMPOSITION","remaining_terminals":POST,"batch_increment":TOTAL,"full178_complete":False,"merge_authorized":False},sort_keys=True))
if __name__=="__main__": main()
