#!/usr/bin/env python3
from __future__ import annotations
import hashlib,importlib.util,json,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
BASE=HERE/"run_full_bband.py"; FAST=HERE/"run_full_bband_fast.py"
BASE_BLOB="2c998a190baaf5f29b33a91fd9efedbb036cef46"; FAST_BLOB="172f003f34d95cceb3d3cbbda949bce6e58b7380"
OLD_SECONDS=9929.36675

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    raw=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def load(p,s,n):
    req(p.is_file() and blob(p)==s,n+" blob drift"); spec=importlib.util.spec_from_file_location(n,p); req(spec and spec.loader,"load "+n); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def main():
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument("--h21-dir",type=Path,required=True); ap.add_argument("--old-dir",type=Path,required=True); a=ap.parse_args()
    base=load(BASE,BASE_BLOB,"base_quick1"); fast=load(FAST,FAST_BLOB,"fast_quick1")
    cells=fast.load_h21_cells(a.h21_dir,base); ctx=base.source_context(); bc=ctx[0]; b0,b1=base.PLANNED[1]
    hits=list(a.old_dir.rglob("row-007.json")); req(len(hits)==1,"old row 7"); old=json.loads(hits[0].read_text())
    t=time.perf_counter(); joint=bc.build_joint_bc_shard(base.HMAX,b0,b1); joint_s=time.perf_counter()-t
    t=time.perf_counter(); pref=fast.build_qbc_prefix(joint,b0,b1,base.HMAX); pref_s=time.perf_counter()-t
    t=time.perf_counter(); new=fast.compute_row_cell_fast(ctx,pref,1,7,cells); fast_s=time.perf_counter()-t
    req(new==old,"exact dictionary mismatch")
    out={"schema":"HPADJ22_FAST_QUICK_BAND1_V1","status":"EXACT_EQUIVALENCE_PASS","row_id":new["row"]["row_id"],"old_seconds":OLD_SECONDS,"joint_seconds":joint_s,"prefix_seconds":pref_s,"fast_seconds":fast_s,"row_speedup":OLD_SECONDS/fast_s,"canonical":new["canonical_sha256_without_this_field"]}
    print(json.dumps(out,sort_keys=True,separators=(",",":")))
if __name__=="__main__": main()
