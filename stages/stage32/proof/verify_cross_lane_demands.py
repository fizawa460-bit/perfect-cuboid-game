#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
STAGE=HERE.parent
ROOT=STAGE.parents[1]
STATE=STAGE/"MAIN-STATE.json"
RECEIPT=STAGE/"management/post-n372-current-v20-authority-rebase-20260913.json"
STATE_BLOB="64dc5523652f1bbe4f19456a6854a39cb3aec87a"
STATE_CANON="739520f562fc445567969088bfea0dd9d87d85c11541d706e6f68748746e0fb7"
RECEIPT_BLOB="3bba4c4a07f6fcae672e08f80096470297aded18"
RECEIPT_CANON="c95c9a9fbe5ca1298e037d222dc595632a71806d98278df4e4dc6442c1820acc"
AUTH=47589703313957134886123
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
    req(f["n358_main_pruning_credit"] is True and f["n358_synchronized_head_hostile_audited"] is True,"N358 credit drift")
    req(f["cut193_main_pruning_credit"] is False and f["cut197_main_pruning_credit"] is False,"CUT credit drift")
    req(f["n372_candidate_hostile_audited"] is True and f["n372_candidate_hostile_audit_review_id"]==5187357950,"N372 audit sync drift")
    req(f["n372_current_authority_rebased"] is True and f["n372_current_authority_witness"] is True,"N372 current authority rebase missing")
    req(f["n372_survives_cut196"] is True and f["n372_survives_n358"] is True,"N372 survival route drift")
    for k in ("n372_main_pruning_credit","n372_full178_credit","n372_effectivity_final_credit","full178_numerical_census_complete","stage32_closed"):
        req(f[k] is False,f"unauthorized credit: {k}")
    req(r["current_authority_rebase"]["n372_survives_current_v20_authority"] is True,"receipt survival drift")
    req(r["current_authority_rebase"]["numerical_authority_changed"] is False,"receipt authority mutation")
    req(s["firewalls"]["merge_authorized"] is False,"merge authorized")
    print(json.dumps({"verdict":"PASS_STAGE32_CROSS_LANE_DEMAND_COORDINATION_V21","n372_current_authority_witness":True,"n372_main_pruning_credit":False,"cut197_main_credit":False,"authoritative_remaining_terminals":AUTH,"full178_complete":False,"merge_authorized":False},sort_keys=True))
if __name__=="__main__": main()
