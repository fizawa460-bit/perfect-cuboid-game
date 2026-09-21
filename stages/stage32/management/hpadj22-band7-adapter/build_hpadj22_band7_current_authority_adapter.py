#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys
from pathlib import Path

HPADJ22_HEAD="4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
BAND_WORKER_REL=Path("stages/stage32-ex5/hpadj-22_ex5/run_full_bband.py")
BAND_WORKER_BLOB="2c998a190baaf5f29b33a91fd9efedbb036cef46"
AGG_REL=Path("stages/stage32-ex5/hpadj-22_ex5/aggregate_full178_bands.py")
AGG_BLOB="f8bec24ab6d524aac05eb8cde9979250f260809c"
V43_SYNC_REL=Path("stages/stage32/management/grf04-quadratic-capacity/GRF04-V43-HPADJ21-FULL178-AUDIT-SYNC.json")
V43_SYNC_BLOB="588442bf55ea03858387f78e0566ff1d5ed7699a"
V43_SYNC_CANON="7a531a5cab37702c43ee83abe98c4e822ac878354eba22f8ea1bc042349b313e"
BAND_CANON="b367b4ba2fda193a82d8eb925ee46423fe9218cb6ad8dca204b898455ffa256d"
AUTH=157570677819451133507
OLD_BAND=1833700202219843304
NEW_BAND=1406364956168291625
GAIN=427335246051551679
CAND=157143342573399581828
SCHEMA="STAGE32_MAIN_HPADJ22_BAND7_CURRENT_AUTHORITY_ADAPTER_V1"

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)
def blob(p):
    raw=p.read_bytes();return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def load_module(path,name):
    spec=importlib.util.spec_from_file_location(name,path);req(spec and spec.loader,"cannot load "+name)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo-root",type=Path,required=True)
    ap.add_argument("--hpadj22-root",type=Path,required=True)
    ap.add_argument("--band-dir",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()

    worker_path=a.hpadj22_root/BAND_WORKER_REL
    agg_path=a.hpadj22_root/AGG_REL
    req(worker_path.is_file() and blob(worker_path)==BAND_WORKER_BLOB,"HPADJ22 band worker drift")
    req(agg_path.is_file() and blob(agg_path)==AGG_BLOB,"HPADJ22 aggregate drift")
    w=load_module(worker_path,"hpadj22_band_locked_for_main_adapter")
    agg=load_module(agg_path,"hpadj22_agg_locked_for_main_adapter")
    req(int(agg.EXPECTED_HPADJ21)==AUTH,"HPADJ22 aggregate authority constant drift")
    req(int(agg.EXPECTED_ROWS)==178 and int(agg.EXPECTED_BANDS)==8 and int(agg.EXPECTED_CELLS)==1424,"HPADJ22 aggregate coverage constants")

    planned=[tuple(x) for x in w.PLANNED]
    req(planned==[(0,11),(12,23),(24,35),(36,47),(48,59),(60,71),(72,83),(84,96)],"band partition drift")
    covered=[]
    for lo,hi in planned: covered.extend(range(lo,hi+1))
    req(covered==list(range(97)) and len(set(covered))==97,"b-band partition not exact/disjoint")

    ctx=w.source_context()
    marker,_=w.validate_complete_dir(a.band_dir,7,ctx)
    req(marker["canonical_sha256_without_this_field"]==BAND_CANON,"band7 canonical drift")
    req(marker["band_position"]==7 and marker["b_interval"]==[84,96] and marker["row_count"]==178,"band7 coverage drift")
    t=marker["totals"]
    req(int(t["hpadj21_cellwise_floor_sum"])==OLD_BAND,"band7 old component drift")
    req(int(t["hpadj22_exact_survivor_sum"])==NEW_BAND,"band7 new exact count drift")
    req(int(t["improvement"])==GAIN and OLD_BAND-NEW_BAND==GAIN,"band7 gain arithmetic")
    req(int(t["hpadj22_exact_survivor_sum"])<=int(t["hpadj21_cellwise_floor_sum"]),"band7 replacement weakens bound")
    req(marker["firewalls"]["stage32_main_pruning_credit"] is False and marker["firewalls"]["full178_complete"] is False,"producer firewall drift")

    state_path=a.repo_root/"stages/stage32/MAIN-STATE.json"
    state=json.loads(state_path.read_text())
    req(state.get("canonical_sha256_without_this_field")==canon(state),"current MAIN state canonical drift")
    f=state["current_exact_frontier"]
    req(int(f["authoritative_remaining_terminals"])==AUTH,"current authority drift")
    req(int(f["authoritative_remaining_strata"])==17128,"current strata drift")
    req(f["authoritative_remaining_terminals_semantics"]=="CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET","authority semantics drift")
    req(f["live_ex5_hpadj21_full178_rows"]==178 and f["live_ex5_hpadj21_row_gap_count"]==0 and f["live_ex5_hpadj21_row_overlap_count"]==0,"HPADJ21 coverage state drift")
    req(f["live_ex5_hpadj21_main_credit_consumed"] is True,"HPADJ21 not current consumed authority")

    sync_path=a.repo_root/V43_SYNC_REL
    req(sync_path.is_file() and blob(sync_path)==V43_SYNC_BLOB,"V43 sync blob drift")
    sync=json.loads(sync_path.read_text())
    req(sync["canonical_sha256_without_this_field"]==V43_SYNC_CANON and canon(sync)==V43_SYNC_CANON,"V43 sync canonical drift")
    req(int(sync["sync"]["authoritative_remaining_terminals"])==AUTH,"V43 sync authority drift")
    req(sync["sync"]["composition_rule"]=="MIN_OF_CERTIFIED_UPPER_BOUNDS__HPADJ21_SAME_POPULATION_REFINEMENT__NO_ADDITIVE_STACKING","V43 composition drift")

    req(AUTH-OLD_BAND+NEW_BAND==CAND,"candidate arithmetic")
    out={
      "schema":SCHEMA,"stage":32,
      "status":"EXACT_DISJOINT_BAND_COMPONENT_REPLACEMENT_CANDIDATE_ZERO_CREDIT_HOSTILE_AUDIT_REQUIRED",
      "source":{
        "hpadj22_head":HPADJ22_HEAD,"band_worker_blob_sha1":BAND_WORKER_BLOB,"aggregate_blob_sha1":AGG_BLOB,
        "workflow_run_id":35336162597,"artifact_id":10552562060,"artifact_name":"hpadj22-band-7-complete",
        "artifact_zip_sha256":"794ba29c5f757b204a7105a941f5ea7e37653b38286314377ed87fbda1430cc4",
        "band_complete_canonical_sha256":BAND_CANON,
        "v43_sync_blob_sha1":V43_SYNC_BLOB,"v43_sync_canonical_sha256":V43_SYNC_CANON},
      "population":{
        "current_hpadj21_authority":AUTH,"band_partition": [list(x) for x in planned],
        "replaced_band_position":7,"replaced_b_interval":[84,96],"rows_covered":178,
        "old_hpadj21_band_component":OLD_BAND,"new_hpadj22_exact_band_count":NEW_BAND,
        "exact_component_tightening":GAIN,"candidate_global_upper_bound_if_promoted":CAND},
      "composition":{
        "rule":"REPLACE_ONE_DISJOINT_HPADJ21_B_BAND_COMPONENT_WITH_EXACT_HPADJ22_COUNT",
        "same_pre_domain_population":True,"same_picard_qA_rule":True,"exact_hpadj08_deletion_location_retained":True,
        "all_other_seven_hpadj21_band_components_left_unchanged":True,
        "band_partition_disjoint_and_exhaustive_over_b_0_96":True,
        "additive_independence_assumption":False,
        "producer_full178_completion_required_for_this_candidate":False,
        "producer_credit_inherited":False},
      "firewalls":{
        "main_pruning_credit":False,"producer_partial_credit":False,"full178_complete":False,
        "theorem_credit":False,"effectivity_credit":False,"receiver_credit":False,"endpoint_credit":False,
        "stage32_closed":False,"hostile_audit_required_before_promotion":True,"merge_authorized":False}}
    out["canonical_sha256_without_this_field"]=canon(out)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    print("HPADJ22_BAND7_MAIN_ADAPTER="+json.dumps({"gain":GAIN,"candidate":CAND,"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))
if __name__=="__main__":main()
