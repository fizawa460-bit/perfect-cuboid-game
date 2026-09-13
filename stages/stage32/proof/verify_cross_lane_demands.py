#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
STAGE=HERE.parent
ROOT=STAGE.parents[1]
STATE=STAGE/"MAIN-STATE.json"
RECEIPT=STAGE/"management/post-certlift03-current-v22-composition-consumption-20260913.json"
STATE_BLOB="bead809db3a008dd35d664a8923f06fecb7de5bb"
STATE_CANON="460b04ecb09d41c1082aee46795acf5da79454df42cc6126a7b92925977855aa"
RECEIPT_BLOB="7a9d84f6ca137740aba01b6983a02a229dc13036"
RECEIPT_CANON="4de6317e2bde395de5aaa58036148e8dc1df1330d614f2143d8e15e7ede2e935"
AUTH=47589703313957134649501
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
    req(f["certlift03_main_pruning_credit"] is True and f["certlift03_incremental_rejected_terminals"]==154697,"CERTLIFT coordination drift")
    req(f["cut199_main_pruning_credit"] is False,"CUT199 overcredit")
    req(f["n372_candidate_hostile_audited"] is True and f["n372_candidate_hostile_audit_review_id"]==5187357950,"N372 audit drift")
    req(f["n372_current_authority_rebased"] is True and f["n372_current_authority_witness"] is True and f["n372_survives_batch_cut193_cut197_cut198"] is True and f["n372_survives_certlift03"] is True,"N372 current authority drift")
    req(f["n372_main_pruning_credit"] is False and f["n372_full178_credit"] is False and f["n372_effectivity_final_credit"] is False,"N372 overcredit")
    req(r["composition"]["double_charge"] is False and r["composition"]["cut199_main_pruning_credit"] is False,"CERTLIFT composition drift")
    req(r["claim_sync"]["semantic_claim_core_changed"] is False and r["claim_sync"]["active_frontier_remap"] is False,"claim sync semantic drift")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,"closure drift")
    req(s["firewalls"]["replacement_head_hostile_reaudit_required"] is True,"replacement re-audit gate missing")
    req(s["firewalls"]["merge_authorized"] is False,"merge authorized")
    print(json.dumps({"verdict":"PASS_STAGE32_CROSS_LANE_DEMAND_COORDINATION_V23_CERTLIFT03","authoritative_remaining_terminals":AUTH,"batch_cuts_consumed":["CUT193","CUT197","CUT198"],"certlift03_consumed":True,"cut199_credit":False,"n372_current_authority_witness":True,"full178_complete":False,"replacement_head_hostile_reaudit_required":True,"merge_authorized":False},sort_keys=True))
if __name__=="__main__": main()
