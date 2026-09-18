#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json, shutil
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE/"run_full_bband.py"
BASE_BLOB="2c998a190baaf5f29b33a91fd9efedbb036cef46"
SHARD=HERE/"run_band7_row_range.py"
SHARD_BLOB="35c8dc88a5b4edfc1152349658910270acaad7b0"
BAND=7

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)

def git_blob(p):
    raw=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def load(path,sha,name):
    req(path.is_file() and git_blob(path)==sha,name+" blob drift")
    spec=importlib.util.spec_from_file_location(name,path)
    req(spec is not None and spec.loader is not None,"cannot load "+name)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--carry-dir",type=Path,required=True)
    ap.add_argument("--shards-root",type=Path,required=True)
    ap.add_argument("--output-dir",type=Path,required=True)
    a=ap.parse_args()
    b=load(BASE,BASE_BLOB,"hpadj22_band7_base_assemble")
    load(SHARD,SHARD_BLOB,"hpadj22_band7_shard_assemble")
    ctx=b.source_context()
    bc,bnd,h21,_,_,_,p14,_,rows,_,_,_,_=ctx
    locks=b.row_source_locks(bc,bnd,h21,p14)
    carried=b.load_resume_rows(a.carry_dir,BAND,rows,locks)
    req(set(carried)==set(range(45)),f"expected exact carry rows 0..44, got {sorted(carried)}")
    allrows=dict(carried)
    for p in sorted(a.shards_root.rglob("row-*.json")):
        d=json.loads(p.read_text())
        idx=int(d.get("row",{}).get("index",-1))
        if idx < 45: continue
        req(idx not in allrows,f"duplicate row {idx}")
        allrows[idx]=b.validate_row_obj(d,BAND,idx,rows,locks)
    req(set(allrows)==set(range(178)),f"band7 row coverage incomplete: {len(allrows)}/178")
    out=a.output_dir; rows_dir=out/"rows"; rows_dir.mkdir(parents=True,exist_ok=True)
    for idx in range(178):
        (rows_dir/f"row-{idx:03d}.json").write_text(json.dumps(allrows[idx],sort_keys=True,separators=(",",":"))+"\n")
    marker=b.complete_marker(out,BAND,allrows,locks)
    marker2,_=b.validate_complete_dir(out,BAND,ctx)
    req(marker2==marker,"band7 complete marker replay mismatch")
    print(json.dumps({"rows":178,"carried_rows":45,"computed_rows":133,"hpadj21":marker["totals"]["hpadj21_cellwise_floor_sum"],"hpadj22":marker["totals"]["hpadj22_exact_survivor_sum"],"gain":marker["totals"]["improvement"],"canonical":marker["canonical_sha256_without_this_field"]},sort_keys=True))

if __name__=="__main__": main()
