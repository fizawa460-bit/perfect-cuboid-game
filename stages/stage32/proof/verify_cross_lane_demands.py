#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
REGISTRY=HERE/"CROSS-LANE-DEMANDS.json"
MONITOR=HERE/"ACTIVE-SPECIALIST-MONITOR-CONTRACT.json"
STATE=ROOT/"stages/stage32/MAIN-STATE.json"
REGISTRY_BLOB="68a02f31431ad658b42ad695f9553c67fd6cff01"
REGISTRY_CANON="aec14c8c2a843e39478a287eb48d10696b1465124b2d089e0085630c66d346f5"
MONITOR_BLOB="2d245205d2c4e597284fcefc6b5f6b43f8df7a2a"
MONITOR_CANON="f5b2403a76546db1c7aea61bfb3eb5b62b3141063969e819758e6911f3a54e6e"
BOUND=128443221087959579960
V47_BOUND=128645575147764659235
V48_TIGHTENING=175363029451184786
V49_PREDECESSOR=128470212118313474449
V49_COVERED=37911631052805557219
V49_REPLACEMENT=37884640022451662730
V49_TIGHTENING=26991030353894489
OLD_BOUND=138652739800650593494
TIGHTENING=10007164652885934259
def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def lock(p,b,c):
    req(blob(p)==b,f"blob drift {p}");o=json.loads(p.read_text(encoding="utf-8"))
    req(o.get("canonical_sha256_without_this_field")==c and canon(o)==c,f"canonical drift {p}");return o
def main():
    reg=lock(REGISTRY,REGISTRY_BLOB,REGISTRY_CANON);mon=lock(MONITOR,MONITOR_BLOB,MONITOR_CANON)
    st=json.loads(STATE.read_text(encoding="utf-8"));req(canon(st)==st.get("canonical_sha256_without_this_field"),"current MAIN state canonical drift")
    req([d["demand_id"] for d in reg["demands"] if d["status"]=="OPEN"]==[],"unexpected OPEN demand")
    req(mon["startup_rule"]["refresh_live_on_every_stage32mainbatch"] is True,"live sweep rule")
    req(mon["authority"]["this_contract_is_a_snapshot_of_live_heads"] is False,"monitor treated as live snapshot")
    req(st["schema"]=="STAGE32_MAIN_COMPACT_STATE_V49_POST_V48_178_FULLSUPPORT_384_AUDIT_SYNCED","MAIN schema")
    f=st["current_exact_frontier"]
    req(f["authoritative_remaining_strata"]==17128 and f["authoritative_remaining_terminals"]==BOUND,"MAIN authority")
    req(f["v44_hpadj22_main_numeric_bound_replacement_consumed"] is True and f["v45_merged_main_synced"] is True,"historical authority chain")
    req(f["v47_predecessor_upper_bound"]==OLD_BOUND and f["v47_exact_tightening_vs_v46"]==TIGHTENING,"V47 tightening")
    req(f["v47_grf04_hpadj22_audited_exact_head"]=="620b90d1ca1f5316d55b88b2620f78eeba1949c7" and f["v47_grf04_hpadj22_hostile_audit_review_id"]==5287562192,"V47 audit")
    req(f["v48_predecessor_upper_bound"]==V47_BOUND and f["v48_exact_tightening_vs_v47"]==V48_TIGHTENING,"V48 tightening")
    req(f["v48_178_support_qbc_audited_exact_head"]=="fb81be66f260879eec79e55be140857b5fc32bbc" and f["v48_178_support_qbc_hostile_audit_comment_id"]==5813812633,"V48 audit")
    req(f["v49_predecessor_upper_bound"]==V49_PREDECESSOR and f["v49_covered_v48_384_upper_bound_sum"]==V49_COVERED and f["v49_replacement_384_upper_bound_sum"]==V49_REPLACEMENT and f["v49_exact_tightening_vs_v48"]==V49_TIGHTENING,"V49 replacement arithmetic")
    req(f["v49_178_fullsupport_384_main_numeric_bound_replacement_consumed"] is True and f["v49_additive_subtraction_performed"] is False and f["v49_exact_incremental_rejected_identity_set_claimed"] is False,"V49 accounting firewall")
    req(f["full178_numerical_census_complete"] is True,"FULL178 census not synchronized")
    req(st["current"]["mainbatch_stop_gate"]=="NONE","MAIN stop gate")
    req(st["current"]["next_exact_route"]=="EFFECTIVITY_AND_MULTIBRANCH_THEN_FINAL_SYNTHESIS","MAIN next route")
    sweep=st["source_locks"]["live_specialist_sweep"]
    req(sweep["observed_repository_main"]=="a834864923086e5f7c1647e462804f45ff9ac28d" and sweep["sweep_date"]=="2026-09-25","repository main/live sweep date")
    req(sweep["lane_178_pr"]==1821 and sweep["lane_178_head"]=="adcb7eb2eef153a1207294e956bf6115794e564d" and sweep["lane_178_latest_audited_exact_head"]=="44d274770de1d092022ebbefff80f3cefb914982" and sweep["lane_178_latest_audit_review_id"]==5313265646 and sweep["lane_178_pending_main_handoff"]=="NONE","178 observation")
    req(sweep["ex5_pr"]==1831 and sweep["ex5_head"]=="e1ab78bc3de90bb116f3d65cb3e6793767b88075" and sweep["ex5_pending_main_handoff"]=="NONE","EX5 observation")
    req(sweep["mb_pr"]==1827 and sweep["mb_head"]=="aae50aa93bea7318b2b063564fa4492007ac9f22" and sweep["mb_pending_main_handoff"]=="NONE","MB observation")
    req(sweep["bridge_pr"]==1833 and sweep["bridge_head"]=="d63ed9efe6e0f7bc957de244c7a51b2025eeeca8" and sweep["bridge_pending_main_handoff"]=="NONE","BRIDGE observation")
    req(sweep["cut_open_successor"] is False and sweep["cut_handoff"]=="NONE","CUT observation")
    for key in ("full178_complete","effectivity_released","receiver_credit","route_credit","theorem_credit","endpoint_credit","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized"):req(st["firewalls"][key] is False,f"firewall {key}")
    print("PASS: Stage32 MAIN V49 cross-lane state is synchronized after hostile-audited 178 384-coordinate same-population bound replacement")
if __name__=="__main__":main()
