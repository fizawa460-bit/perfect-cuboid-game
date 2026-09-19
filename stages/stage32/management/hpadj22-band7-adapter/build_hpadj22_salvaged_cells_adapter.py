#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys
from pathlib import Path

HPADJ22_HEAD="4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
WORKER_REL=Path("stages/stage32-ex5/hpadj-22_ex5/run_full_bband.py")
WORKER_BLOB="2c998a190baaf5f29b33a91fd9efedbb036cef46"
SNAP_REL=Path("stages/stage32-ex5/hpadj-22_ex5/build_recovery_snapshot.py")
SNAP_BLOB="52359e8e8074c8bf0db369b49285bf1b927fb33c"
AGG_REL=Path("stages/stage32-ex5/hpadj-22_ex5/aggregate_full178_bands.py")
AGG_BLOB="f8bec24ab6d524aac05eb8cde9979250f260809c"
AUTH=157570677819451133507
BAND7_CANON="b367b4ba2fda193a82d8eb925ee46423fe9218cb6ad8dca204b898455ffa256d"
SNAP_CANON="02b90c4a57386eecb9cb7e0948ee1ac609baeba431263b43308a6d65915ce846"
SCHEMA="STAGE32_MAIN_HPADJ22_SALVAGED_DISJOINT_CELLS_ADAPTER_V1"

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)
def blob(p):
    raw=p.read_bytes();return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);req(spec and spec.loader,"cannot load "+name)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo-root",type=Path,required=True)
    ap.add_argument("--hpadj22-root",type=Path,required=True)
    ap.add_argument("--partial-root",type=Path,required=True)
    ap.add_argument("--complete-band7-dir",type=Path,required=True)
    ap.add_argument("--snapshot-json",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()

    wp=a.hpadj22_root/WORKER_REL; sp=a.hpadj22_root/SNAP_REL; apath=a.hpadj22_root/AGG_REL
    req(blob(wp)==WORKER_BLOB,"worker drift");req(blob(sp)==SNAP_BLOB,"snapshot builder drift");req(blob(apath)==AGG_BLOB,"aggregate drift")
    w=load(wp,"hpadj22_worker_for_salvage"); agg=load(apath,"hpadj22_agg_for_salvage")
    req(int(agg.EXPECTED_HPADJ21)==AUTH and int(agg.EXPECTED_BANDS)==8 and int(agg.EXPECTED_ROWS)==178,"aggregate authority/coverage drift")
    ctx=w.source_context()
    bc,bnd,h21,_,_,_,p14,_,rows,_,_,_,_=ctx
    locks=w.row_source_locks(bc,bnd,h21,p14)

    snap=json.loads(a.snapshot_json.read_text())
    req(snap.get("canonical_sha256_without_this_field")==SNAP_CANON,"recovery snapshot stored canonical drift")
    req(canon(snap)==SNAP_CANON,"recovery snapshot canonical drift")
    req(snap.get("all_bands_complete") is False,"unexpected original production completion")
    req(int(snap.get("validated_rows",-1))==114,"original validated-row count drift")

    partial={}
    per_band_partial={}
    for pos in range(8):
        d=a.partial_root/f"hpadj22-band-{pos}"
        carried=w.load_resume_rows(d,pos,rows,locks)
        per_band_partial[pos]=len(carried)
        for idx,obj in carried.items():
            key=(pos,idx);req(key not in partial,"duplicate original partial cell")
            partial[key]=obj
    req(len(partial)==114,f"validated partial row count drift {len(partial)}")

    band7_marker,band7_rows=w.validate_complete_dir(a.complete_band7_dir,7,ctx)
    req(band7_marker["canonical_sha256_without_this_field"]==BAND7_CANON,"complete band7 canonical drift")
    req(len(band7_rows)==178,"complete band7 row coverage")

    # Prefer the later complete band7 evidence; salvage original partials only from bands 0..6.
    selected={(7,idx):obj for idx,obj in band7_rows.items()}
    for (pos,idx),obj in partial.items():
        if pos==7: continue
        req((pos,idx) not in selected,"unexpected selected-cell duplicate")
        selected[(pos,idx)]=obj

    old_sum=new_sum=0
    stream=hashlib.sha256()
    rows_out=[]
    for pos,idx in sorted(selected):
        obj=selected[(pos,idx)];t=obj["totals"]
        old=int(t["hpadj21_floor"]);new=int(t["hpadj22_exact_survivors"]);req(new<=old,"selected cell weakens HPADJ21")
        old_sum+=old;new_sum+=new
        rec={"band_position":pos,"b_interval":obj["b_interval"],"row_index":idx,"row_id":obj["row"]["row_id"],
             "old_hpadj21_floor":old,"new_hpadj22_exact":new,"improvement":old-new,
             "canonical":obj["canonical_sha256_without_this_field"]}
        rows_out.append(rec);stream.update(json.dumps(rec,sort_keys=True,separators=(",",":")).encode()+b"\n")
    gain=old_sum-new_sum; cand=AUTH-gain
    req(gain>=427335246051551679,"salvage unexpectedly weaker than complete band7")

    state=json.loads((a.repo_root/"stages/stage32/MAIN-STATE.json").read_text())
    req(state.get("canonical_sha256_without_this_field")==canon(state),"current MAIN state canonical drift")
    req(int(state["current_exact_frontier"]["authoritative_remaining_terminals"])==AUTH,"current authority drift")
    req(state["current_exact_frontier"]["live_ex5_hpadj21_main_credit_consumed"] is True,"HPADJ21 not consumed authority")

    out={"schema":SCHEMA,"stage":32,
      "status":"EXACT_DISJOINT_CELL_COMPONENT_REPLACEMENT_CANDIDATE_ZERO_CREDIT_HOSTILE_AUDIT_REQUIRED",
      "sources":{
        "hpadj22_head":HPADJ22_HEAD,"band_worker_blob_sha1":WORKER_BLOB,"recovery_snapshot_builder_blob_sha1":SNAP_BLOB,
        "aggregate_blob_sha1":AGG_BLOB,
        "original_production":{"run_id":35303482505,"recovery_snapshot_artifact_id":10539776526,
          "recovery_snapshot_zip_sha256":"54fc1ee144078c2956749438daf884edae5372b9ccd2610518424bbf192bc320",
          "recovery_snapshot_canonical":SNAP_CANON,"validated_partial_cells":114},
        "band7_recovery":{"run_id":35336162597,"complete_artifact_id":10552562060,
          "complete_artifact_zip_sha256":"794ba29c5f757b204a7105a941f5ea7e37653b38286314377ed87fbda1430cc4",
          "band_complete_canonical":BAND7_CANON}},
      "coverage":{
        "original_partial_cells_by_band":{str(k):v for k,v in sorted(per_band_partial.items())},
        "original_validated_partial_cells":len(partial),
        "complete_band7_cells":178,
        "selected_disjoint_cells":len(selected),
        "selected_cell_stream_sha256":stream.hexdigest(),
        "full178_total_cells":1424,
        "unreplaced_cells_left_at_hpadj21":1424-len(selected)},
      "result":{"current_hpadj21_authority":AUTH,"selected_old_hpadj21_component":old_sum,
        "selected_new_hpadj22_exact_component":new_sum,"exact_component_tightening":gain,
        "candidate_global_upper_bound_if_promoted":cand},
      "composition":{
        "rule":"REPLACE_SELECTED_DISJOINT_HPADJ21_ROW_BAND_COMPONENTS_WITH_VALIDATED_EXACT_HPADJ22_COUNTS",
        "complete_band7_supersedes_original_band7_partial_rows":True,
        "other_original_partial_cells_used_once":True,
        "all_unselected_cells_left_at_hpadj21":True,
        "same_pre_domain_population":True,"same_picard_qA_rule":True,"exact_hpadj08_deletion_location_retained":True,
        "additive_independence_assumption":False,"producer_credit_inherited":False},
      "cells":rows_out,
      "firewalls":{"main_pruning_credit":False,"producer_partial_credit":False,"full178_complete":False,
        "hostile_audit_required_before_promotion":True,"theorem_credit":False,"effectivity_credit":False,
        "receiver_credit":False,"endpoint_credit":False,"stage32_closed":False,"merge_authorized":False}}
    out["canonical_sha256_without_this_field"]=canon(out)
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    print("HPADJ22_SALVAGE_ADAPTER="+json.dumps({"selected_cells":len(selected),"gain":gain,"candidate":cand,
      "partial_by_band":per_band_partial,"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))
if __name__=="__main__":main()
