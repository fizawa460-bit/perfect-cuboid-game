#!/usr/bin/env python3
from __future__ import annotations
import hashlib, importlib.util, json, time
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE/"run_full_bband.py"
FAST=HERE/"run_full_bband_fast.py"
BASE_BLOB="2c998a190baaf5f29b33a91fd9efedbb036cef46"
FAST_BLOB="79a99b63f517f69e162f44a4fc203e4907193078"
TARGETS=[(0,3),(6,19)]

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)

def blob(p):
    raw=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def load(p,sha,name):
    req(p.is_file() and blob(p)==sha,name+" blob drift")
    spec=importlib.util.spec_from_file_location(name,p); req(spec and spec.loader,"cannot load "+name)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def main():
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument("--h21-dir",type=Path,required=True); a=ap.parse_args()
    base=load(BASE,BASE_BLOB,"hpadj22_base_speed_bench")
    fast=load(FAST,FAST_BLOB,"hpadj22_fast_speed_bench")
    cells=fast.load_h21_cells(a.h21_dir,base)
    ctx=base.source_context()
    bc=ctx[0]
    results=[]
    for band,row in TARGETS:
        b0,b1=base.PLANNED[band]
        t0=time.perf_counter(); joint=bc.build_joint_bc_shard(base.HMAX,b0,b1); joint_s=time.perf_counter()-t0
        t0=time.perf_counter(); old=base.compute_row_cell(ctx,joint,band,row); old_s=time.perf_counter()-t0
        t0=time.perf_counter(); pref=fast.build_qbc_prefix(joint,b0,b1,base.HMAX); pref_s=time.perf_counter()-t0
        t0=time.perf_counter(); new=fast.compute_row_cell_fast(ctx,pref,band,row,cells); fast_s=time.perf_counter()-t0
        req(old==new,f"byte-semantic dictionary mismatch band={band} row={row}")
        speed=(old_s/fast_s) if fast_s else 999999.0
        results.append({"band":band,"row_index":row,"row_id":old["row"]["row_id"],"joint_seconds":joint_s,"prefix_seconds":pref_s,"old_seconds":old_s,"fast_seconds":fast_s,"speedup":speed,"canonical":old["canonical_sha256_without_this_field"]})
        print(json.dumps(results[-1],sort_keys=True),flush=True)
    out={"schema":"STAGE32EX5_HPADJ22_SPEEDUP_SCRATCH_BENCH_V1","status":"EXACT_DICTIONARY_EQUIVALENCE_PASS","targets":results,"min_speedup":min(x["speedup"] for x in results),"credit":{"stage32_main_credit":False,"full178_completion_credit":False,"merge_authorized":False}}
    print("FINAL="+json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__": main()
