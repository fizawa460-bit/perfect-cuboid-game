#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path

DIRECT_REL=Path("stages/stage32/management/hpadj22-fast-global/benchmark_direct_count.py")
DIRECT_BLOB="e965ab0a6ea51938006882ca2110016f48b3768e"
HPADJ22_HEAD="4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
PARTIAL_RUN_ID=35303482505
SCHEMA="STAGE32_MAIN_HPADJ22_DIRECT_BAND_V1"

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)

def blob(p):
    raw=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def load_direct(repo_root):
    p=repo_root/DIRECT_REL
    req(p.is_file() and blob(p)==DIRECT_BLOB,"direct-count source drift")
    spec=importlib.util.spec_from_file_location("stage32_main_hpadj22_direct_locked",p)
    req(spec and spec.loader,"cannot load direct-count source")
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
    return m

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo-root",type=Path,required=True)
    ap.add_argument("--source-root",type=Path,required=True)
    ap.add_argument("--partial-root",type=Path,required=True)
    ap.add_argument("--band-position",type=int,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()

    req(0<=a.band_position<=6,"band7 is retained and must not be recomputed here")
    direct=load_direct(a.repo_root)
    old=direct.load_old(a.source_root)
    ctx=old.source_context()
    bc,bnd,h21,h18,h16,p15,p14,counter,rows,rejected,profiles,classes_gt2,tuples_above_second=ctx
    locks=old.row_source_locks(bc,bnd,h21,p14)
    baselines=old.load_resume_rows(a.partial_root,a.band_position,rows,locks)

    b0,b1=old.PLANNED[a.band_position]
    t0=time.perf_counter()
    joint=bc.build_joint_bc_shard(old.HMAX,b0,b1)
    t1=time.perf_counter()

    row_summaries=[]
    pre=reject=post=h22=0
    crosschecked=0
    stream=hashlib.sha256()
    for idx in range(178):
        got=direct.direct_count(old,ctx,joint,a.band_position,idx)
        req(got["row"]["index"]==idx,"row index drift")
        req(got["b_interval"]==list(old.PLANNED[a.band_position]),"band interval drift")
        req(got["pre_mass"]-got["rejected_mass"]==got["post_mass"],f"row mass conservation {idx}")
        if idx in baselines:
            bt=baselines[idx]["totals"]
            for k in ("pre_mass","rejected_mass","post_mass","hpadj22_exact_survivors"):
                req(int(got[k])==int(bt[k]),f"retained baseline mismatch band={a.band_position} row={idx} field={k}")
            req(got["profile"]==baselines[idx]["profile"],f"retained profile mismatch row={idx}")
            crosschecked+=1
        rec={
          "row_index":idx,"row_id":got["row"]["row_id"],"g":got["row"]["g"],"d":got["row"]["d"],
          "pre_mass":str(got["pre_mass"]),"rejected_mass":str(got["rejected_mass"]),
          "post_mass":str(got["post_mass"]),"hpadj22_exact_survivors":str(got["hpadj22_exact_survivors"]),
          "retained_partial_crosscheck":idx in baselines
        }
        row_summaries.append(rec)
        stream.update(json.dumps(rec,sort_keys=True,separators=(",",":")).encode()+b"\n")
        pre+=got["pre_mass"];reject+=got["rejected_mass"];post+=got["post_mass"];h22+=got["hpadj22_exact_survivors"]

    t2=time.perf_counter()
    req(pre-reject==post,"band mass conservation")
    req(crosschecked==len(baselines),"baseline crosscheck count drift")

    out={
      "schema":SCHEMA,"stage":32,
      "status":"EXACT_DIRECT_HPADJ22_BAND_COMPLETE_ZERO_CREDIT",
      "band":{"position":a.band_position,"b_interval":[b0,b1],"row_count":178},
      "source_locks":{
        "direct_count_blob_sha1":DIRECT_BLOB,
        "hpadj22_source_head":HPADJ22_HEAD,
        "old_band_worker_blob_sha1":direct.OLD_BLOB,
        "partial_production_run_id":PARTIAL_RUN_ID
      },
      "validation":{
        "all_178_rows_replay_retained_hpadj08_rejected_mass":True,
        "retained_partial_crosschecked_rows":crosschecked,
        "retained_partial_available_rows":len(baselines),
        "row_stream_sha256":stream.hexdigest()
      },
      "totals":{
        "pre_mass":str(pre),"rejected_mass":str(reject),"post_mass":str(post),
        "hpadj22_exact_survivor_sum":str(h22)
      },
      "timing":{
        "joint_build_seconds":round(t1-t0,6),
        "all_178_direct_rows_seconds":round(t2-t1,6),
        "total_seconds":round(t2-t0,6)
      },
      "rows":row_summaries,
      "semantics":{
        "same_population_as_hpadj21":True,
        "same_picard_qA_rule":True,
        "exact_hpadj08_deletion_location_retained":True,
        "direct_count_no_hpadj21_lp_reconstruction":True,
        "additive_subtraction":False,
        "statistical_independence":False
      },
      "firewalls":{
        "main_pruning_credit":False,"full178_complete":False,
        "hostile_audit_required_before_promotion":True,"merge_authorized":False
      }
    }
    out["canonical_sha256_without_this_field"]=canon(out)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    print("HPADJ22_DIRECT_BAND="+json.dumps({
      "band":a.band_position,"b_interval":[b0,b1],"crosschecked":crosschecked,
      "hpadj22":str(h22),"joint_seconds":round(t1-t0,3),"rows_seconds":round(t2-t1,3),
      "canonical":out["canonical_sha256_without_this_field"]
    },sort_keys=True))

if __name__=="__main__":main()
