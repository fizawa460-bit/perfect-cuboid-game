#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
STATE=ROOT/"stages/stage32/MAIN-STATE.json"
RECEIPT=HERE/"HPADJ22-V46-POSTMERGE-SUCCESSOR.json"
RECEIPT_BLOB="0ebbf672c432cb3cb1b2927bf03d660567eb417c"
RECEIPT_CANON="61b40b3a98bbc1be7a59e90225086e3bc21ff6dd35f9c96bc9cbcfcf5bb348d6"
MERGED_MAIN="659ba93b9eba657b49a728f549c6bb6028398e08"
AUDITED_HEAD="5aa6e63923946e201f51c8070cf9466029073d5e"
AUDIT_REVIEW=5254811573
BOUND=138652739800650593494
V45_STATE_BLOB="a8f873ffdcaca280f7b57158b69606b3ea496d3c"
V45_STATE_CANON="58adceeff158b8ddc4194ff7a269ed4f32237c72f0c6eb62f88d343d902df62a"
V45_RECEIPT_BLOB="a8486ff337e030d02ce26d7404907fdbea5d3cc1"
V45_VERIFIER_BLOB="d545dbc10ccdbe6342c2bfef18581ea27abdae76"
V45_STARTUP_BLOB="9460290b475c7d08622fd94c21782133d40ac6cd"
V45_CROSS_BLOB="8e55c5026ab7d3ea9b7c390d5d2562562d396c10"
def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def lock_json(p,b,c,label):
    req(p.is_file(),"missing "+label);req(blob(p)==b,label+" blob drift")
    o=json.loads(p.read_text(encoding="utf-8"));req(o.get("canonical_sha256_without_this_field")==c and canon(o)==c,label+" canonical drift");return o
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--v45-root",type=Path);args=ap.parse_args()
    rec=lock_json(RECEIPT,RECEIPT_BLOB,RECEIPT_CANON,"V46 receipt")
    req(rec["status"]=="MERGED_V45_AUTHORITY_ADOPTED__ZERO_NEW_PRUNING","receipt status")
    p=rec["merged_predecessor"];req(p["pr"]==1824 and p["merge_commit"]==MERGED_MAIN and p["audited_exact_head"]==AUDITED_HEAD and p["hostile_audit_review_id"]==AUDIT_REVIEW,"predecessor identity")
    a=rec["authority"];req(a["authoritative_remaining_strata"]==17128 and a["authoritative_remaining_terminals"]==str(BOUND) and a["additional_pruning"]==0 and a["numeric_authority_changed"] is False,"receipt authority")
    if args.v45_root is not None:
        root=args.v45_root
        old=lock_json(root/"stages/stage32/MAIN-STATE.json",V45_STATE_BLOB,V45_STATE_CANON,"merged V45 state")
        req(old["current_exact_frontier"]["authoritative_remaining_terminals"]==BOUND,"merged V45 bound")
        req(blob(root/"stages/stage32/management/hpadj22-direct-full178/HPADJ22-V45-AUDIT-SYNC.json")==V45_RECEIPT_BLOB,"V45 receipt drift")
        req(blob(root/"stages/stage32/management/hpadj22-direct-full178/verify_hpadj22_v45_audit_sync.py")==V45_VERIFIER_BLOB,"V45 verifier drift")
        req(blob(root/"stages/stage32/verify_main_startup.py")==V45_STARTUP_BLOB,"V45 startup drift")
        req(blob(root/"stages/stage32/proof/verify_cross_lane_demands.py")==V45_CROSS_BLOB,"V45 cross drift")
    st=json.loads(STATE.read_text(encoding="utf-8"));req(canon(st)==st.get("canonical_sha256_without_this_field"),"state canonical")
    req(st["schema"]=="STAGE32_MAIN_COMPACT_STATE_V46_POSTMERGE_SUCCESSOR","schema")
    req(st["authority_sync"]["current_repository_main"]==MERGED_MAIN,"current main")
    req(st["authority_sync"]["predecessor_process_head"]==AUDITED_HEAD,"predecessor head")
    req(st["authority_sync"]["v45_merge_commit"]==MERGED_MAIN and st["authority_sync"]["v45_merge_pr"]==1824 and st["authority_sync"]["v45_final_hostile_audit_review_id"]==AUDIT_REVIEW,"merge metadata")
    req(st["authority_sync"]["v46_postmerge_sync_additional_pruning"]==0,"V46 pruning")
    f=st["current_exact_frontier"];req(f["authoritative_remaining_strata"]==17128 and f["authoritative_remaining_terminals"]==BOUND,"authority");req(f["v45_merged_main_synced"] is True and f["v46_postmerge_sync_additional_pruning"]==0,"frontier sync")
    req(st["source_locks"]["live_specialist_sweep"]["observed_repository_main"]==MERGED_MAIN,"live main")
    req(st["current"]["next_exact_route"]=="FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS","route")
    for k in ("full178_complete","effectivity_released","receiver_credit","route_credit","theorem_credit","endpoint_credit","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized"):req(st["firewalls"][k] is False,"firewall "+k)
    print("PASS: Stage32 MAIN V46 adopts merged hostile-audited V45 authority with zero new pruning")
if __name__=="__main__":main()
