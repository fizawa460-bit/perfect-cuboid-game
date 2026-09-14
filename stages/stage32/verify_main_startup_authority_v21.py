#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
STATE=HERE/"MAIN-STATE.json"
RECEIPT=HERE/"management/post-n372-current-v20-authority-rebase-20260913.json"
SNAP=HERE/"management/MAIN-STATE-V20-N372-PRE-REBASE.json"
STATE_BLOB="64dc5523652f1bbe4f19456a6854a39cb3aec87a"
STATE_CANON="739520f562fc445567969088bfea0dd9d87d85c11541d706e6f68748746e0fb7"
RECEIPT_BLOB="3bba4c4a07f6fcae672e08f80096470297aded18"
RECEIPT_CANON="c95c9a9fbe5ca1298e037d222dc595632a71806d98278df4e4dc6442c1820acc"
SNAP_BLOB="0886dc0c0a8b8960ca9b5cf8285801d4948de874"
SNAP_CANON="5b087c68f0d81893c65c8210cca112e57d881bcb0713c6ed81ff46d300584cd2"
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
    s=lock(STATE,STATE_BLOB,STATE_CANON); r=lock(RECEIPT,RECEIPT_BLOB,RECEIPT_CANON); p=lock(SNAP,SNAP_BLOB,SNAP_CANON)
    req(p["current_exact_frontier"]["n372_current_authority_rebased"] is False,"V20 predecessor rebase drift")
    f=s["current_exact_frontier"]; a=s["authority_sync"]
    req(f["authoritative_remaining_strata"]==17128 and f["authoritative_remaining_terminals"]==AUTH,"authority drift")
    req(a["v20_exact_head"]=="b6c0a1e431ac04de5326a7c42af89a7b92423ed2" and a["v20_hostile_audit_review_id"]==5187834836 and a["v20_hostile_audit_status"]=="PASS","V20 audit lock drift")
    req(f["n372_current_authority_rebased"] is True and f["n372_current_authority_witness"] is True,"N372 rebase missing")
    req(f["n372_survives_cut196"] is True and f["n372_survives_n358"] is True,"N372 survival flags drift")
    for k in ("n372_main_pruning_credit","n372_full178_credit","n372_effectivity_final_credit","full178_numerical_census_complete","stage32_closed"):
        req(f[k] is False,f"unauthorized credit: {k}")
    req(r["current_authority_rebase"]["current_authority_rebased"] is True and r["current_authority_rebase"]["incremental_rejected_terminals"]==0,"receipt rebase drift")
    req(r["authority"]["after_remaining_terminals"]==AUTH,"receipt authority drift")
    for k in ("receiver_credit","theorem_credit","endpoint_credit","route_credit","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized"):
        req(s["firewalls"][k] is False,f"firewall opened: {k}")
    print(json.dumps({"verdict":"PASS_STAGE32_MAIN_STARTUP_AUTHORITY_V21","n372_current_authority_witness":True,"authority_unchanged":True,"full178_complete":False,"effectivity_credit":False,"merge_authorized":False},sort_keys=True))
if __name__=="__main__": main()
