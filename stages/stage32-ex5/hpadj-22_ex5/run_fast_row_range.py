#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json, time
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE/"run_full_bband.py"
FAST=HERE/"run_full_bband_fast.py"
BASE_BLOB="2c998a190baaf5f29b33a91fd9efedbb036cef46"
FAST_BLOB="bf96761f1b8917da87efe968539ca6cf08416b03"
CERT_SCHEMA="STAGE32EX5_HPADJ21_FULL178_CELL_FLOOR_CERT_V1"
CERT_CANON="fd276094f4647ecdc348e18a376e2d61313b782cdb23659890707726707ed13a"
EXPECTED_TOTAL=157570677819451133507

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    raw=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def canon(d):
    x=dict(d); x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p,sha,name):
    req(p.is_file() and blob(p)==sha,name+" blob drift")
    spec=importlib.util.spec_from_file_location(name,p); req(spec and spec.loader,"load "+name)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def load_cert(path:Path,base):
    d=json.loads(path.read_text())
    req(d["schema"]==CERT_SCHEMA,"cert schema")
    req(d["canonical_sha256_without_this_field"]==CERT_CANON==canon(d),"cert canonical")
    req(d["coverage"]=={"cells":1424,"rows":178},"cert coverage")
    req(int(d["hpadj21_full178_cellwise_floor_sum"])==EXPECTED_TOTAL,"cert total")
    out={}
    for rec in d["rows"]:
        idx=int(rec[0]); row_id=rec[1]; cells=rec[2]
        req(len(cells)==8,f"cert cells row {idx}")
        for pos,v in enumerate(cells):
            num,den,floor,pre,post=map(int,v)
            req(num//den==floor,f"cert floor row {idx}/{pos}")
            out[(idx,pos)]={"interval_position":pos,"b_interval":list(base.PLANNED[pos]),"hpadj21_num":num,"hpadj21_den":den,"hpadj21_floor":floor,"pre_mass":pre,"post_mass":post}
    req(len(out)==1424,"cert mapping coverage")
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--band-position",type=int,required=True)
    ap.add_argument("--row-start",type=int,required=True)
    ap.add_argument("--row-stop",type=int,required=True)
    ap.add_argument("--h21-cert",type=Path,required=True)
    ap.add_argument("--output-dir",type=Path,required=True)
    a=ap.parse_args()
    req(0<=a.band_position<8,"band")
    req(0<=a.row_start<=a.row_stop<178,"row range")
    base=load(BASE,BASE_BLOB,"base_fast_range"); fast=load(FAST,FAST_BLOB,"fast_range")
    cells=load_cert(a.h21_cert,base)
    ctx=base.source_context(); bc=ctx[0]; b0,b1=base.PLANNED[a.band_position]
    t=time.perf_counter(); joint=bc.build_joint_bc_shard(base.HMAX,b0,b1); joint_s=time.perf_counter()-t
    t=time.perf_counter(); pref=fast.build_qbc_prefix(joint,b0,b1,base.HMAX); prefix_s=time.perf_counter()-t
    rows_dir=a.output_dir/"rows"; rows_dir.mkdir(parents=True,exist_ok=True)
    t=time.perf_counter(); done=[]
    for idx in range(a.row_start,a.row_stop+1):
        d=fast.compute_row_cell_fast(ctx,pref,a.band_position,idx,cells)
        (rows_dir/f"row-{idx:03d}.json").write_text(json.dumps(d,sort_keys=True,separators=(",",":"))+"\n")
        done.append(idx)
        print(json.dumps({"band":a.band_position,"row_index":idx,"row_id":d["row"]["row_id"],"gain":d["totals"]["improvement"],"completed":len(done)},sort_keys=True),flush=True)
    rows_s=time.perf_counter()-t
    receipt={"schema":"STAGE32EX5_HPADJ22_FAST_ROW_RANGE_SCRATCH_V1","status":"EXACT_FAST_RANGE_COMPLETE_ZERO_CREDIT","band_position":a.band_position,"b_interval":list(base.PLANNED[a.band_position]),"row_start":a.row_start,"row_stop":a.row_stop,"row_count":len(done),"timing":{"joint_seconds":joint_s,"prefix_seconds":prefix_s,"rows_seconds":rows_s},"source_locks":{"base_blob":BASE_BLOB,"fast_blob":FAST_BLOB,"h21_cert_canonical":CERT_CANON},"credit":{"stage32_main_credit":False,"full178_completion_credit":False,"merge_authorized":False}}
    (a.output_dir/"RANGE-RECEIPT.json").write_text(json.dumps(receipt,sort_keys=True,separators=(",",":"))+"\n")
    print("RECEIPT="+json.dumps(receipt,sort_keys=True,separators=(",",":")))
if __name__=="__main__": main()
