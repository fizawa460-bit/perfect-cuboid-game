#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE/"run_full_bband.py"
BASE_BLOB="2c998a190baaf5f29b33a91fd9efedbb036cef46"
BAND=7

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)

def git_blob(p):
    raw=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def load_base():
    req(BASE.is_file() and git_blob(BASE)==BASE_BLOB,"base band worker drift")
    spec=importlib.util.spec_from_file_location("hpadj22_band7_base_locked",BASE)
    req(spec is not None and spec.loader is not None,"cannot load base worker")
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--row-start",type=int,required=True)
    ap.add_argument("--row-stop",type=int,required=True)
    ap.add_argument("--output-dir",type=Path,required=True)
    a=ap.parse_args()
    req(45 <= a.row_start <= a.row_stop <= 177,"band7 recovery range must lie in 45..177")
    b=load_base()
    ctx=b.source_context()
    bc=ctx[0]
    joint=bc.build_joint_bc_shard(b.HMAX,*b.PLANNED[BAND])
    _,bnd,h21,_,_,_,p14,_,rows,_,_,_,_=ctx
    locks=b.row_source_locks(bc,bnd,h21,p14)
    out=a.output_dir; rows_dir=out/"rows"; rows_dir.mkdir(parents=True,exist_ok=True)
    count=0
    for idx in range(a.row_start,a.row_stop+1):
        d=b.compute_row_cell(ctx,joint,BAND,idx)
        b.validate_row_obj(d,BAND,idx,rows,locks)
        (rows_dir/f"row-{idx:03d}.json").write_text(json.dumps(d,sort_keys=True,separators=(",",":"))+"\n")
        count+=1
        print(json.dumps({"row_index":idx,"row_id":d["row"]["row_id"],"gain":d["totals"]["improvement"],"completed":count},sort_keys=True),flush=True)
    receipt={
      "schema":"STAGE32EX5_HPADJ22_BAND7_ROW_RANGE_V1",
      "band_position":7,
      "b_interval":[84,96],
      "row_start":a.row_start,
      "row_stop":a.row_stop,
      "row_count":count,
      "base_band_worker_blob_sha1":BASE_BLOB,
      "credit":{"partial_output_credit":False,"stage32_main_credit":False,"full178_completion_credit":False,"merge_authorized":False}
    }
    (out/"RANGE-RECEIPT.json").write_text(json.dumps(receipt,sort_keys=True,separators=(",",":"))+"\n")

if __name__=="__main__": main()
