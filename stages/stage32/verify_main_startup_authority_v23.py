#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STATE = HERE / "MAIN-STATE.json"
RECEIPT = HERE / "management/post-certlift03-current-v22-composition-consumption-20260913.json"

STATE_BLOB = "bead809db3a008dd35d664a8923f06fecb7de5bb"
STATE_CANON = "460b04ecb09d41c1082aee46795acf5da79454df42cc6126a7b92925977855aa"
RECEIPT_BLOB = "7a9d84f6ca137740aba01b6983a02a229dc13036"
RECEIPT_CANON = "4de6317e2bde395de5aaa58036148e8dc1df1330d614f2143d8e15e7ede2e935"
POST = 47589703313957134649501
INC = 154697
BLOCKS = 1369
OVERLAP = 308

def req(v,m):
    if not v:
        raise SystemExit("FAIL: " + m)

def blob(p):
    raw=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def canon(o):
    cp=dict(o); cp.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(cp,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def lock(p,b,c):
    req(p.is_file(),f"missing {p.relative_to(ROOT)}")
    req(blob(p)==b,f"blob drift {p.relative_to(ROOT)}")
    o=json.loads(p.read_text(encoding="utf-8"))
    req(o.get("canonical_sha256_without_this_field")==c,f"stored canonical drift {p.relative_to(ROOT)}")
    req(canon(o)==c,f"canonical drift {p.relative_to(ROOT)}")
    return o

def main():
    s=lock(STATE,STATE_BLOB,STATE_CANON)
    r=lock(RECEIPT,RECEIPT_BLOB,RECEIPT_CANON)
    f=s["current_exact_frontier"]
    req(s["schema"]=="STAGE32_MAIN_COMPACT_STATE_V23_CERTLIFT03_CONSUMED","V23 schema drift")
    req(f["authoritative_remaining_strata"]==17128 and f["authoritative_remaining_terminals"]==POST,"authority drift")
    req(f["certlift03_main_pruning_credit"] is True,"CERTLIFT MAIN credit missing")
    req(f["certlift03_incremental_blocks"]==BLOCKS and f["certlift03_incremental_rejected_terminals"]==INC,"CERTLIFT increment drift")
    req(f["certlift03_prior_overlap_blocks"]==OVERLAP and f["certlift03_double_charge"] is False,"CERTLIFT overlap drift")
    req(f["cut199_main_pruning_credit"] is False,"CUT199 overcredit")
    req(f["n372_current_authority_witness"] is True and f["n372_survives_certlift03"] is True,"N372 witness lost")
    req(f["n372_main_pruning_credit"] is False and f["n372_full178_credit"] is False and f["n372_effectivity_final_credit"] is False,"N372 overcredit")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,"closure overcredit")
    req(r["authority"]["after_remaining_terminals"]==POST and r["authority"]["certlift03_main_pruning_credit"] is True,"receipt authority drift")
    req(r["composition"]["double_charge"] is False and r["composition"]["incremental_rejected_terminals"]==INC,"receipt composition drift")
    req(r["composition"]["cut199_main_pruning_credit"] is False,"receipt CUT199 overcredit")
    req(r["n372_firewall"]["certlift03_predicate_matches"] is False and r["n372_firewall"]["current_authority_witness_preserved"] is True,"receipt N372 drift")
    req(s["firewalls"]["replacement_head_hostile_reaudit_required"] is True,"replacement re-audit gate missing")
    for k in ("receiver_credit","theorem_credit","endpoint_credit","stage32_closed",
              "perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized"):
        req(s["firewalls"][k] is False,f"firewall opened {k}")
    print(json.dumps({
        "verdict":"PASS_STAGE32_MAIN_STARTUP_AUTHORITY_V23_CERTLIFT03_COMPOSITION",
        "remaining_terminals":POST,
        "certlift03_increment":INC,
        "certlift03_blocks":BLOCKS,
        "full178_complete":False,
        "replacement_head_hostile_reaudit_required":True,
        "merge_authorized":False
    },sort_keys=True))

if __name__=="__main__":
    main()
