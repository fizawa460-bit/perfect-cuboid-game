#!/usr/bin/env python3
from __future__ import annotations
import hashlib, importlib.util, json, time
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE/"run_full_bband.py"
FAST=HERE/"run_full_bband_fast.py"
BASE_BLOB="2c998a190baaf5f29b33a91fd9efedbb036cef46"
FAST_BLOB="79a99b63f517f69e162f44a4fc203e4907193078"
TARGETS=[
  {"band":0,"row":3,"old_seconds":321.0967},
  {"band":6,"row":19,"old_seconds":675.5013},
]

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)

def blob(p):
    raw=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def load(p,sha,name):
    req(p.is_file() and blob(p)==sha,name+" blob drift")
    spec=importlib.util.spec_from_file_location(name,p); req(spec and spec.loader,"cannot load "+name)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def find_row(root:Path,row:int):
    hits=list(root.rglob(f"row-{row:03d}.json"))
    req(len(hits)==1,f"expected one old row {row}, got {hits}")
    return json.loads(hits[0].read_text())

def main():
    import argparse
    ap=argparse.ArgumentParser()
    ap.add_argument("--h21-dir",type=Path,required=True)
    ap.add_argument("--old0-dir",type=Path,required=True)
    ap.add_argument("--old6-dir",type=Path,required=True)
    a=ap.parse_args()
    base=load(BASE,BASE_BLOB,"hpadj22_base_fastonly")
    fast=load(FAST,FAST_BLOB,"hpadj22_fast_fastonly")
    cells=fast.load_h21_cells(a.h21_dir,base)
    ctx=base.source_context(); bc=ctx[0]
    results=[]
    for t in TARGETS:
        band,row=t["band"],t["row"]
        old=find_row(a.old0_dir if band==0 else a.old6_dir,row)
        req(old["band_position"]==band,"old band mismatch")
        b0,b1=base.PLANNED[band]
        t0=time.perf_counter(); joint=bc.build_joint_bc_shard(base.HMAX,b0,b1); joint_s=time.perf_counter()-t0
        t0=time.perf_counter(); pref=fast.build_qbc_prefix(joint,b0,b1,base.HMAX); pref_s=time.perf_counter()-t0
        t0=time.perf_counter(); new=fast.compute_row_cell_fast(ctx,pref,band,row,cells); fast_s=time.perf_counter()-t0
        req(new==old,f"exact dictionary mismatch band={band} row={row}")
        speed=t["old_seconds"]/fast_s
        rec={"band":band,"row_index":row,"row_id":new["row"]["row_id"],"old_seconds":t["old_seconds"],"joint_seconds":joint_s,"prefix_seconds":pref_s,"fast_seconds":fast_s,"row_speedup":speed,"canonical":new["canonical_sha256_without_this_field"]}
        results.append(rec); print(json.dumps(rec,sort_keys=True),flush=True)
    out={"schema":"STAGE32EX5_HPADJ22_FAST_ONLY_ARTIFACT_EQUIV_BENCH_V1","status":"EXACT_OLD_ARTIFACT_DICTIONARY_EQUIVALENCE_PASS","targets":results,"min_row_speedup":min(x["row_speedup"] for x in results),"credit":{"stage32_main_credit":False,"full178_completion_credit":False,"merge_authorized":False}}
    print("FINAL="+json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__": main()
