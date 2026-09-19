#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
STATE=ROOT/"stages/stage32/MAIN-STATE.json"; SYNC=HERE/"HPADJ22-V45-AUDIT-SYNC.json"
REGISTRY=ROOT/"stages/stage32/proof/CLAIM-REGISTRY.json"; FRONTIER=ROOT/"stages/stage32/proof/ACTIVE-FRONTIER.json"; ADAPTERS=ROOT/"stages/stage32/proof/LANE-ADAPTERS.json"
SYNC_BLOB="a8486ff337e030d02ce26d7404907fdbea5d3cc1"; SYNC_CANON="122052faff0cf86b7cc58e78e769f6ca4027d908881b97813edc42dc32fb0477"
V44_HEAD="142b50757b345971218c953db6a15ddd09974172"; V44_STATE_BLOB="cd9273321afc95f4861a78873ef4ef1393849390"; V44_STATE_CANON="ca31359fde60eea677b3aa585b849718055f00dfb4708a89e9c7043db48f7366"
V44_RECEIPT_BLOB="a2be82fe69bf1d2fdefc0a7ba566601246a0bec4"; V44_RECEIPT_CANON="cef45672a180124ce46972fed6ead43bb94b16e552496c6101a8e5dfa1b8a7b9"; V44_VERIFIER_BLOB="723554d2a3960c39dba1c38cc2e6d05cd2318b12"; V44_STARTUP_BLOB="c8b90c33c31f212e05837421f9ce975b1b605fba"
REGISTRY_BLOB="f3a884adc1c82aace81cb73d049ff14720ace862"; FRONTIER_BLOB="4c251be4aa5c355481fe3bcfc71c292fb6389ba4"; ADAPTERS_BLOB="c0ef34e5838e27046a20fed77063593009c56f40"
AUDIT_REVIEW=5254793258; CURRENT_MAIN="83ae3f66cfcbdfaaaebf149bea078d1b0ff11c49"; BOUND=138652739800650593494; V43_BOUND=157570677819451133507; TIGHTENING=18917938018800540013
def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None);return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def lock_json(p,b,c,label):
    req(p.is_file(),"missing "+label);req(blob(p)==b,label+" blob drift");o=json.loads(p.read_text(encoding="utf-8"));req(o.get("canonical_sha256_without_this_field")==c and canon(o)==c,label+" canonical drift");return o
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--v44-root",type=Path);args=ap.parse_args()
    state=json.loads(STATE.read_text(encoding="utf-8"));req(canon(state)==state.get("canonical_sha256_without_this_field"),"current MAIN state canonical drift")
    sync=lock_json(SYNC,SYNC_BLOB,SYNC_CANON,"V45 audit-sync receipt");req(blob(REGISTRY)==REGISTRY_BLOB and blob(FRONTIER)==FRONTIER_BLOB and blob(ADAPTERS)==ADAPTERS_BLOB,"claim DAG lock drift")
    if args.v44_root is not None:
        root=args.v44_root;old=lock_json(root/"stages/stage32/MAIN-STATE.json",V44_STATE_BLOB,V44_STATE_CANON,"V44 replacement state");req(old["current_exact_frontier"]["authoritative_remaining_terminals"]==BOUND,"V44 predecessor authority")
        lock_json(root/"stages/stage32/management/hpadj22-direct-full178/HPADJ22-V44-MAIN-BOUND-REPLACEMENT.json",V44_RECEIPT_BLOB,V44_RECEIPT_CANON,"V44 replacement receipt")
        req(blob(root/"stages/stage32/management/hpadj22-direct-full178/verify_hpadj22_v44_main_bound_replacement.py")==V44_VERIFIER_BLOB,"V44 verifier drift");req(blob(root/"stages/stage32/verify_main_startup.py")==V44_STARTUP_BLOB,"V44 startup drift")
    audit=sync["hostile_audit"];req(audit["status"]=="PASS" and audit["audited_exact_head"]==V44_HEAD and audit["review_id"]==AUDIT_REVIEW and audit["current_main_at_audit"]==CURRENT_MAIN and audit["merge_ready_freshness"]=="CLEAR","audit identity")
    s=sync["sync"];req(s["authority_version"]=="V45_PROCESS_SYNC_ONLY","sync version");req(s["authoritative_remaining_strata"]==17128 and s["authoritative_remaining_terminals"]==str(BOUND),"sync authority");req(s["additional_pruning"]==0 and s["numeric_authority_changed"] is False,"sync changed authority");req(s["logical_claim_statement_changed"] is False and s["claim_registry_mutated"] is False and s["active_frontier_mutated"] is False and s["lane_adapters_mutated"] is False,"claim DAG mutated")
    req(state["schema"]=="STAGE32_MAIN_COMPACT_STATE_V45_HPADJ22_FULL178_BOUND_AUDIT_SYNCED","state schema");a=state["authority_sync"];req(a["current_repository_main"]==CURRENT_MAIN and a["predecessor_process_head"]==V44_HEAD,"state predecessor");req(a["v44_replacement_hostile_audit_status"]=="PASS" and a["v44_replacement_hostile_audit_review_id"]==AUDIT_REVIEW and a["v45_audit_sync_additional_pruning"]==0,"state audit sync")
    f=state["current_exact_frontier"];req(f["authoritative_remaining_strata"]==17128 and f["authoritative_remaining_terminals"]==BOUND,"state authority");req(f["v44_replacement_head_hostile_audited"] is True and f["v44_replacement_head_audited_exact_head"]==V44_HEAD and f["v44_replacement_head_hostile_audit_review_id"]==AUDIT_REVIEW and f["v45_audit_sync_additional_pruning"]==0,"state audited boundary");req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,"closure")
    req(state["current"]["mainbatch_stop_gate"]=="NONE" and state["current"]["next_exact_route"]=="FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS","current route");req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is False,"reaudit gate")
    sweep=state["source_locks"]["live_specialist_sweep"];req(sweep["mb_head"]=="81ac5f243c08fb7c16a2b7cb2f09653fff78f65e" and sweep["mb_pending_main_handoff"]=="NONE","MB")
    for key in ("full178_complete","effectivity_released","receiver_credit","route_credit","theorem_credit","endpoint_credit","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized"):req(state["firewalls"][key] is False,"firewall "+key)
    req(V43_BOUND-BOUND==TIGHTENING,"arithmetic")
    print("PASS: Stage32 V45 synchronizes hostile-audited V44 HPADJ22 authority with zero new pruning")
if __name__=="__main__":main()
