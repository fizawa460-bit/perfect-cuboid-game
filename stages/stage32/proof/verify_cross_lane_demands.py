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
MONITOR_BLOB="3547e58eef441aab4c6df15aa08b95b2824830de"
MONITOR_CANON="4a5a2f3eb0883af5c6175784878b1aba9023c3330b6f94967734e464a25b0815"
BOUND=726240487
V52_PREDECESSOR=5369214401
V51_PREDECESSOR=511353002049
STRATA=530
V50_PREDECESSOR=128443221087959579960
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
    req(mon["startup_rule"]["refresh_live_on_every_stage32mainbatch"] is False,"global live sweep not retired")
    req(mon["startup_rule"]["resolve_only_selected_roadmap_unit"] is True,"roadmap selection rule")
    req(mon["startup_rule"]["global_specialist_sweep_required"] is False,"global specialist sweep unexpectedly required")
    req(mon["authority"]["this_contract_is_a_snapshot_of_live_heads"] is False,"routing contract treated as live snapshot")
    surfaces={x["unit"]:x for x in mon["active_roadmap_surfaces"]}
    req(surfaces["32-02"]["dispatch_surface"]=="EX5" and surfaces["32-02"]["internal_only"] is True,"32-02 internal dispatch surface")
    req(surfaces["32-03"]["dispatch_surface"]=="MB" and surfaces["32-03"]["auxiliary_surface"]=="MB-FIB" and surfaces["32-03"]["internal_only"] is True,"32-03 internal dispatch surface")
    req(all("helper_command" not in x and "auxiliary_command" not in x for x in mon["active_roadmap_surfaces"]),"legacy specialist commands leaked into live monitor")
    req(st["schema"]=="STAGE32_MAIN_COMPACT_STATE_V52_FIXED_DIRECTION_CERTIFICATES_SYNCED","MAIN schema")
    f=st["current_exact_frontier"]
    req(f["authoritative_remaining_strata"]==STRATA and f["authoritative_remaining_terminals"]==BOUND,"MAIN authority")
    req(f["v50_predecessor_upper_bound"]==V50_PREDECESSOR and f["v50_predecessor_remaining_strata"]==17128 and f["v50_exact_tightening_vs_v49"]==V50_PREDECESSOR-V51_PREDECESSOR,"V50 MIN composition")
    req(f["v50_unibranch_node_hurwitz_main_numeric_bound_consumed"] is True and f["v50_additive_subtraction_performed"] is False and f["v50_exact_incremental_rejected_identity_set_claimed"] is False,"V50 accounting firewall")
    req(f["v44_hpadj22_main_numeric_bound_replacement_consumed"] is True and f["v45_merged_main_synced"] is True,"historical authority chain")
    req(f["v47_predecessor_upper_bound"]==OLD_BOUND and f["v47_exact_tightening_vs_v46"]==TIGHTENING,"V47 tightening")
    req(f["v47_grf04_hpadj22_audited_exact_head"]=="620b90d1ca1f5316d55b88b2620f78eeba1949c7" and f["v47_grf04_hpadj22_hostile_audit_review_id"]==5287562192,"V47 audit")
    req(f["v48_predecessor_upper_bound"]==V47_BOUND and f["v48_exact_tightening_vs_v47"]==V48_TIGHTENING,"V48 tightening")
    req(f["v48_178_support_qbc_audited_exact_head"]=="fb81be66f260879eec79e55be140857b5fc32bbc" and f["v48_178_support_qbc_hostile_audit_comment_id"]==5813812633,"V48 audit")
    req(f["v49_predecessor_upper_bound"]==V49_PREDECESSOR and f["v49_covered_v48_384_upper_bound_sum"]==V49_COVERED and f["v49_replacement_384_upper_bound_sum"]==V49_REPLACEMENT and f["v49_exact_tightening_vs_v48"]==V49_TIGHTENING,"V49 replacement arithmetic")
    req(f["v49_178_fullsupport_384_main_numeric_bound_replacement_consumed"] is True and f["v49_additive_subtraction_performed"] is False and f["v49_exact_incremental_rejected_identity_set_claimed"] is False,"V49 accounting firewall")
    req(f["full178_numerical_census_complete"] is True,"FULL178 census not synchronized")
    req(st["current"]["mainbatch_stop_gate"]=="NONE","MAIN stop gate")
    req(st["current"]["next_exact_route"]=="ROADMAP_32_02_AND_32_03_THEN_32_04_SYNTHESIS","MAIN next route")
    req(st["current"]["operator_entrypoint"]=="stage32mainbatch","MAIN operator entrypoint")
    req(st["current"]["routing_mode"]=="ROADMAP_FIRST_ON_DEMAND_SPECIALIST_DISPATCH","MAIN routing mode")
    sweep=st["source_locks"]["live_specialist_sweep"]
    req(sweep["mode"]=="ROADMAP_SELECTED_ON_DEMAND_COORDINATION_SNAPSHOT" and sweep["global_sweep_required"] is False,"coordination snapshot mode")
    req(sweep["observed_repository_main"]=="a834864923086e5f7c1647e462804f45ff9ac28d" and sweep["sweep_date"]=="2026-09-25","repository main/coordination date")
    req(sweep["lane_178_status"]=="PARKED_RETAINED_AFTER_AUDITED_32_01_COMPLETION" and sweep["lane_178_retained_source_pr"]==1821 and sweep["lane_178_compact_handoff_pr"]==1835 and sweep["lane_178_latest_audited_exact_head"]=="44d274770de1d092022ebbefff80f3cefb914982" and sweep["lane_178_latest_audit_review_id"]==5313265646 and sweep["lane_178_pending_main_handoff"]=="NONE","178 retained observation")
    req(sweep["ex5_pr"]==1831 and sweep["ex5_head"]=="ffc3cf84ff9995b91bacd406193a05708f8cc84e" and sweep["ex5_pending_main_handoff"]=="NONE","EX5 32-02 observation")
    req(sweep["mb_pr"]==1827 and sweep["mb_head"]=="50205efc2d57af4553cff75dd3667b204e4b089d" and sweep["mb_pending_main_handoff"]=="NONE","MB 32-03 observation")
    req(sweep["mb_fib_pr"]==1829 and sweep["mb_fib_head"]=="090cf1ce97819736f9be09a9a96fb6421349acad","MB-FIB auxiliary observation")
    req(sweep["bridge_status"]=="PARKED_OPTIONAL_POST_32_01_REFINEMENT" and sweep["bridge_pending_main_handoff"]=="NONE","BRIDGE parked observation")
    req(sweep["cut_status"]=="RETAINED_HISTORY_NO_OPEN_SUCCESSOR" and sweep["cut_pending_main_handoff"]=="NONE","CUT retained observation")
    for key in ("full178_complete","effectivity_released","receiver_credit","route_credit","theorem_credit","endpoint_credit","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized"):req(st["firewalls"][key] is False,f"firewall {key}")
    req(f["v51_predecessor_upper_bound"]==V51_PREDECESSOR and f["v51_exact_tightening_vs_v50"]==V51_PREDECESSOR-V52_PREDECESSOR,"V51 MIN composition")
    req(f["v51_hpadj22_unibranch_main_numeric_bound_consumed"] is True and f["v51_additive_subtraction_performed"] is False and f["v51_exact_incremental_rejected_identity_set_claimed"] is False,"V51 accounting firewall")
    req(f["v52_predecessor_upper_bound"]==V52_PREDECESSOR and f["v52_exact_tightening_vs_v51"]==V52_PREDECESSOR-BOUND,"V52 MIN composition")
    req(f["v52_fixed_direction_certificates_main_numeric_bound_consumed"] is True and f["v52_additive_subtraction_performed"] is False and f["v52_exact_incremental_rejected_identity_set_claimed"] is False,"V52 accounting firewall")
    print("PASS: Stage32 MAIN V52 cross-lane state is synchronized after hostile-audited FIXED-DIRECTION-CERTIFICATES same-population per-row MIN bound")
if __name__=="__main__":main()
