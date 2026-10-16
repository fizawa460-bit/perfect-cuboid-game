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
CURRENT_REPOSITORY_MAIN="da573f048a82a63e459be1343fb002e663b60875"
V48_CURRENT_REPOSITORY_MAIN="e7fd29d24dd21e8529dbdb45b221a53f2cc21ed3"
V49_CURRENT_REPOSITORY_MAIN="a834864923086e5f7c1647e462804f45ff9ac28d"
AUDITED_HEAD="5aa6e63923946e201f51c8070cf9466029073d5e"
AUDIT_REVIEW=5254811573
OLD_BOUND=138652739800650593494
V47_BOUND=128645575147764659235
V47_AUDITED_HEAD="620b90d1ca1f5316d55b88b2620f78eeba1949c7"
V47_AUDIT_REVIEW=5287562192
V48_BOUND=128470212118313474449
V48_AUDITED_HEAD="fb81be66f260879eec79e55be140857b5fc32bbc"
V48_AUDIT_COMMENT=5813812633
V49_BOUND=128443221087959579960
V49_AUDITED_HEAD="44d274770de1d092022ebbefff80f3cefb914982"
V49_AUDIT_REVIEW=5313265646
V49_TIGHTENING=26991030353894489
V50_CURRENT_REPOSITORY_MAIN="5fd74ee8d9f1129fea7fbb5bf1c647e120817860"
V50_BOUND=511353002049
V50_STRATA=530
V51_CURRENT_REPOSITORY_MAIN="84f1bf9ec6723f7bbb1bef7f6271ebb528b06afa"
V51_BOUND=5369214401
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
    a=rec["authority"];req(a["authoritative_remaining_strata"]==17128 and a["authoritative_remaining_terminals"]==str(OLD_BOUND) and a["additional_pruning"]==0 and a["numeric_authority_changed"] is False,"receipt authority")
    if args.v45_root is not None:
        root=args.v45_root
        old=lock_json(root/"stages/stage32/MAIN-STATE.json",V45_STATE_BLOB,V45_STATE_CANON,"merged V45 state")
        req(old["current_exact_frontier"]["authoritative_remaining_terminals"]==OLD_BOUND,"merged V45 bound")
        req(blob(root/"stages/stage32/management/hpadj22-direct-full178/HPADJ22-V45-AUDIT-SYNC.json")==V45_RECEIPT_BLOB,"V45 receipt drift")
        req(blob(root/"stages/stage32/management/hpadj22-direct-full178/verify_hpadj22_v45_audit_sync.py")==V45_VERIFIER_BLOB,"V45 verifier drift")
        req(blob(root/"stages/stage32/verify_main_startup.py")==V45_STARTUP_BLOB,"V45 startup drift")
        req(blob(root/"stages/stage32/proof/verify_cross_lane_demands.py")==V45_CROSS_BLOB,"V45 cross drift")
    st=json.loads(STATE.read_text(encoding="utf-8"));req(canon(st)==st.get("canonical_sha256_without_this_field"),"state canonical")
    req(st["authority_sync"]["v45_merge_commit"]==MERGED_MAIN and st["authority_sync"]["v45_merge_pr"]==1824 and st["authority_sync"]["v45_final_hostile_audit_review_id"]==AUDIT_REVIEW,"merge metadata")
    schema=st["schema"];f=st["current_exact_frontier"]
    if schema=="STAGE32_MAIN_COMPACT_STATE_V46_POSTMERGE_SUCCESSOR":
        req(st["authority_sync"]["current_repository_main"]==CURRENT_REPOSITORY_MAIN,"V46 current main")
        req(f["authoritative_remaining_terminals"]==OLD_BOUND and f["full178_numerical_census_complete"] is False,"V46 authority")
        req(st["current"]["next_exact_route"]=="FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS","V46 route")
    elif schema=="STAGE32_MAIN_COMPACT_STATE_V47_GRF04_HPADJ22_FULL178_AUDIT_SYNCED":
        req(st["authority_sync"]["current_repository_main"]==CURRENT_REPOSITORY_MAIN,"V47 current main")
        req(f["authoritative_remaining_terminals"]==V47_BOUND and f["full178_numerical_census_complete"] is True,"V47 authority")
        req(f["v47_grf04_hpadj22_audited_exact_head"]==V47_AUDITED_HEAD and f["v47_grf04_hpadj22_hostile_audit_review_id"]==V47_AUDIT_REVIEW,"V47 audit")
        req(st["current"]["next_exact_route"]=="EFFECTIVITY_AND_MULTIBRANCH_THEN_FINAL_SYNTHESIS","V47 route")
    elif schema=="STAGE32_MAIN_COMPACT_STATE_V48_178_SUPPORT_QBC_AUDIT_SYNCED":
        req(st["authority_sync"]["current_repository_main"]==V48_CURRENT_REPOSITORY_MAIN,"V48 current main")
        req(f["authoritative_remaining_terminals"]==V48_BOUND and f["full178_numerical_census_complete"] is True,"V48 authority")
        req(f["v48_178_support_qbc_audited_exact_head"]==V48_AUDITED_HEAD and f["v48_178_support_qbc_hostile_audit_comment_id"]==V48_AUDIT_COMMENT,"V48 audit")
        req(st["current"]["next_exact_route"]=="EFFECTIVITY_AND_MULTIBRANCH_THEN_FINAL_SYNTHESIS","V48 route")
    elif schema=="STAGE32_MAIN_COMPACT_STATE_V49_POST_V48_178_FULLSUPPORT_384_AUDIT_SYNCED":
        req(st["authority_sync"]["current_repository_main"]==V49_CURRENT_REPOSITORY_MAIN,"V49 current main")
        req(f["authoritative_remaining_terminals"]==V49_BOUND and f["full178_numerical_census_complete"] is True,"V49 authority")
        req(f["v49_exact_tightening_vs_v48"]==V49_TIGHTENING and f["v49_178_fullsupport_384_main_numeric_bound_replacement_consumed"] is True,"V49 tightening/consumption")
        locks=st["source_locks"]["v49_post_v48_178_fullsupport_384_authority_sync"]
        req(locks["compact_handoff_audited_exact_head"]==V49_AUDITED_HEAD and locks["hostile_audit_review_id"]==V49_AUDIT_REVIEW,"V49 audit")
        req(st["current"]["next_exact_route"]=="ROADMAP_32_02_AND_32_03_THEN_32_04_SYNTHESIS","V49 route")
    elif schema=="STAGE32_MAIN_COMPACT_STATE_V50_UNIBRANCH_NODE_HURWITZ_SYNCED":
        req(st["authority_sync"]["current_repository_main"]==V50_CURRENT_REPOSITORY_MAIN,"V50 current main")
        req(f["authoritative_remaining_terminals"]==V50_BOUND and f["authoritative_remaining_strata"]==V50_STRATA and f["full178_numerical_census_complete"] is True,"V50 authority")
        req(f["v50_predecessor_upper_bound"]==V49_BOUND and f["v49_exact_tightening_vs_v48"]==V49_TIGHTENING and f["v50_unibranch_node_hurwitz_main_numeric_bound_consumed"] is True,"V50 predecessor/consumption")
        req(f["v50_additive_subtraction_performed"] is False,"V50 additive firewall")
        req(st["current"]["next_exact_route"]=="ROADMAP_32_02_AND_32_03_THEN_32_04_SYNTHESIS","V50 route")
    elif schema=="STAGE32_MAIN_COMPACT_STATE_V51_HPADJ22_UNIBRANCH_SYNCED":
        req(st["authority_sync"]["current_repository_main"]==V51_CURRENT_REPOSITORY_MAIN,"V51 current main")
        req(f["authoritative_remaining_terminals"]==V51_BOUND and f["authoritative_remaining_strata"]==V50_STRATA and f["full178_numerical_census_complete"] is True,"V51 authority")
        req(f["v51_predecessor_upper_bound"]==V50_BOUND and f["v50_predecessor_upper_bound"]==V49_BOUND and f["v51_hpadj22_unibranch_main_numeric_bound_consumed"] is True,"V51 predecessor/consumption")
        req(f["v51_additive_subtraction_performed"] is False,"V51 additive firewall")
        req(st["current"]["next_exact_route"]=="ROADMAP_32_02_AND_32_03_THEN_32_04_SYNTHESIS","V51 route")
    else:
        req(False,"unsupported successor schema")
    for k in ("full178_complete","effectivity_released","receiver_credit","route_credit","theorem_credit","endpoint_credit","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized"):req(st["firewalls"][k] is False,"firewall "+k)
    print("PASS: Stage32 MAIN preserves V46/V47/V48 predecessor authority and accepts the hostile-audited V49 178 full-support 384, V50 unibranch node-Hurwitz and V51 HPADJ22-unibranch successors when synchronized")
if __name__=="__main__":main()
