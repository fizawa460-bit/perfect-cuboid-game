#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE/"run_full_bband.py"
BASE_BLOB="2c998a190baaf5f29b33a91fd9efedbb036cef46"

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    raw=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def load_base():
    req(BASE.is_file() and blob(BASE)==BASE_BLOB,"base worker drift")
    spec=importlib.util.spec_from_file_location("base_fast_assemble",BASE); req(spec and spec.loader,"load base")
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--band-position",type=int,required=True)
    ap.add_argument("--carry-dir",type=Path,required=True)
    ap.add_argument("--fast-dir",type=Path,required=True)
    ap.add_argument("--output-dir",type=Path,required=True)
    a=ap.parse_args()
    base=load_base(); ctx=base.source_context()
    bc,bnd,h21,_,_,_,p14,_,rows,_,_,_,_=ctx
    locks=base.row_source_locks(bc,bnd,h21,p14)
    carried=base.load_resume_rows(a.carry_dir,a.band_position,rows,locks)
    combined=dict(carried)
    for p in sorted(a.fast_dir.rglob("row-*.json")):
        d=json.loads(p.read_text()); idx=int(d.get("row",{}).get("index",-1))
        req(idx not in combined,f"row overlap {idx}")
        combined[idx]=base.validate_row_obj(d,a.band_position,idx,rows,locks)
    req(set(combined)==set(range(178)),f"complete row coverage required, got {len(combined)}")
    out=a.output_dir; rows_dir=out/"rows"; rows_dir.mkdir(parents=True,exist_ok=True)
    for idx in range(178):
        (rows_dir/f"row-{idx:03d}.json").write_text(json.dumps(combined[idx],sort_keys=True,separators=(",",":"))+"\n")
    marker=base.complete_marker(out,a.band_position,combined,locks)
    replay,_=base.validate_complete_dir(out,a.band_position,ctx)
    req(replay==marker,"complete marker replay mismatch")
    print(json.dumps({"band":a.band_position,"carried_rows":len(carried),"fast_rows":178-len(carried),"hpadj21":marker["totals"]["hpadj21_cellwise_floor_sum"],"hpadj22":marker["totals"]["hpadj22_exact_survivor_sum"],"gain":marker["totals"]["improvement"],"canonical":marker["canonical_sha256_without_this_field"]},sort_keys=True))
if __name__=="__main__": main()
