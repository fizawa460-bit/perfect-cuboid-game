#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
ROW_WORKER=ROOT/"stages/stage32/management/grf04-hpadj22-joint/run_grf04_hpadj22_full178_parent.py"
ROW_WORKER_BLOB="c9fbf71242581f096718ebf0dbc9ac88878c91f1"
WINDOW_SCHEMA="STAGE32_MAIN_V46_GRF04_HPADJ22_FULL178_PARENT_WINDOW_V2"
ROW_WINDOWS=((0,59),(60,119),(120,177))

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)

def blob(p:Path)->str:
    b=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def load_row_worker():
    req(blob(ROW_WORKER)==ROW_WORKER_BLOB,"row worker blob drift")
    spec=importlib.util.spec_from_file_location("v46_full178_row_worker",ROW_WORKER)
    req(spec and spec.loader,"cannot load row worker")
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
    return m

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-root",type=Path,required=True)
    ap.add_argument("--band-position",type=int,required=True)
    ap.add_argument("--chunk-position",type=int,required=True)
    ap.add_argument("--row-window-position",type=int,required=True)
    ap.add_argument("--output-dir",type=Path,required=True)
    ap.add_argument("--carry-root",type=Path)
    ap.add_argument("--expected-wrapper-blob",required=True)
    a=ap.parse_args()
    req(blob(Path(__file__))==a.expected_wrapper_blob,"window wrapper self-lock drift")
    req(0<=a.row_window_position<len(ROW_WINDOWS),"invalid row window")
    w=load_row_worker()
    req(0<=a.band_position<8 and 0<=a.chunk_position<4,"invalid parent identity")
    b0,b1=w.chunks_for_band(a.band_position)[a.chunk_position]
    r0,r1=ROW_WINDOWS[a.row_window_position]

    hd=w.load_helper()
    direct=hd.load(hd.DIRECT,hd.DIRECT_BLOB,"v46_full178_direct")
    proj=hd.load(hd.PROJECTION,hd.PROJECTION_BLOB,"v46_full178_projection")
    hd._full178_projection=proj
    req(hd.E_VERIFY.is_file() and w.blob(hd.E_VERIFY)==hd.E_VERIFY_BLOB,"e-independence verifier drift")
    old=direct.load_old(a.source_root)
    ctx=old.source_context()
    rows=ctx[8]
    req(len(rows)==178,"FULL178 row count drift")
    req(tuple(old.PLANNED[a.band_position])==w.BANDS[a.band_position],"band interval drift")

    a.output_dir.mkdir(parents=True,exist_ok=True)
    window=set(range(r0,r1+1))
    expected=[i for i,(_,_,d0) in enumerate(rows) if i in window and int(d0)//2>=b0]
    implicit=[i for i,(_,_,d0) in enumerate(rows) if i in window and int(d0)//2<b0]
    req(set(expected).isdisjoint(implicit) and set(expected)|set(implicit)==window,"window row partition drift")

    carried={};rejected_carry=[]
    if a.carry_root and a.carry_root.exists():
        byname={}
        for p in a.carry_root.rglob("row-*.json"):
            byname.setdefault(p.name,[]).append(p)
        for i in expected:
            row_id,g0,d0=rows[i]
            good=[]
            for p in byname.get(f"row-{i:03d}.json",[]):
                d=w.validate_carry(
                    p,worker_blob=ROW_WORKER_BLOB,band=a.band_position,chunk=a.chunk_position,
                    b0=b0,b1=b1,row_index=i,row_id=str(row_id),g=int(g0),d=int(d0))
                if d is not None: good.append((p,d))
                else: rejected_carry.append(str(p))
            req(len(good)<=1,f"duplicate valid carry row {i}")
            if good:
                carried[i]=good[0][1]
                (a.output_dir/f"row-{i:03d}.json").write_text(
                    json.dumps(good[0][1],sort_keys=True,separators=(",",":"))+"\n")

    t0=time.perf_counter()
    joint=ctx[0].build_joint_bc_shard(old.HMAX,b0,b1)
    build_s=time.perf_counter()-t0

    shared_intervals={}
    ti=time.perf_counter()
    for b in range(b0,b1+1):
        for c in range(old.HMAX+1):
            qkeys=set()
            jbc=joint[b][c]
            for sbc in range(8):
                for parity in (0,1):
                    hist=jbc[sbc][parity]
                    if hist:qkeys.update(int(q) for q,v in hist.items() if int(v))
            shared_intervals[(b,c)]=hd.interval_table(proj,b,c,qkeys) if qkeys else {}
    interval_build_s=time.perf_counter()-ti

    completed=dict(carried)
    for i in expected:
        if i in completed: continue
        d=w.compute_row(
            hd,old,ctx,joint,shared_intervals,worker_blob=ROW_WORKER_BLOB,
            band=a.band_position,chunk=a.chunk_position,b0=b0,b1=b1,row_index=i)
        p=a.output_dir/f"row-{i:03d}.json";tmp=p.with_suffix(".tmp")
        tmp.write_text(json.dumps(d,sort_keys=True,separators=(",",":"))+"\n");tmp.replace(p)
        completed[i]=d
        print("FULL178_WINDOW_ROW="+json.dumps({
            "band":a.band_position,"chunk":a.chunk_position,"window":a.row_window_position,
            "row":i,"baseline":d["result"]["hpadj22_exact_survivors"],
            "joint":d["result"]["joint_exact_survivors"],
            "canonical":d["canonical_sha256_without_this_field"]},sort_keys=True),flush=True)

    req(set(completed)==set(expected),"parent-window row completion drift")
    baseline=sum(int(completed[i]["result"]["hpadj22_exact_survivors"]) for i in expected)
    joint_total=sum(int(completed[i]["result"]["joint_exact_survivors"]) for i in expected)
    req(joint_total<=baseline,"parent-window joint weakened baseline")
    manifest={
        "schema":WINDOW_SCHEMA,"stage":32,"status":"EXACT_PARENT_WINDOW_COMPLETE_ZERO_CREDIT",
        "parent":{"band_position":a.band_position,"chunk_position":a.chunk_position,
                  "b_chunk":[b0,b1],"row_window_position":a.row_window_position,
                  "row_window":[r0,r1]},
        "source_locks":{"execution_wrapper_blob_sha1":a.expected_wrapper_blob,
                        "row_compute_worker_blob_sha1":ROW_WORKER_BLOB,
                        "helper_blob_sha1":w.HELPER_BLOB,
                        "hpadj22_source_head":w.SOURCE_HEAD},
        "coverage":{"window_rows":list(range(r0,r1+1)),
                    "expected_computed_rows":expected,"implicit_zero_rows":implicit,
                    "computed_row_count":len(expected),"implicit_zero_row_count":len(implicit),
                    "carried_validated_row_count":len(carried),
                    "newly_computed_row_count":len(expected)-len(carried),
                    "rejected_carry_count":len(rejected_carry),"gaps":0,"overlaps":0},
        "result":{"hpadj22_exact_survivors":baseline,"joint_exact_survivors":joint_total,
                  "exact_improvement":baseline-joint_total,"strict":joint_total<baseline},
        "timing_seconds":{"joint_bc_build":round(build_s,6),
                          "shared_integer_interval_build":round(interval_build_s,6)},
        "row_canonicals":[{"row_index":i,
                           "canonical":completed[i]["canonical_sha256_without_this_field"]}
                          for i in expected],
        "firewalls":{"main_pruning_credit":False,"full178_complete":False,
                     "merge_authorized":False}
    }
    manifest["canonical_sha256_without_this_field"]=canon(manifest)
    (a.output_dir/"PARENT-WINDOW-COMPLETE.json").write_text(
        json.dumps(manifest,sort_keys=True,separators=(",",":"))+"\n")
    print("FULL178_PARENT_WINDOW="+json.dumps({
        "band":a.band_position,"chunk":a.chunk_position,"window":a.row_window_position,
        "baseline":baseline,"joint":joint_total,"improvement":baseline-joint_total,
        "rows":len(expected),"carried":len(carried),
        "canonical":manifest["canonical_sha256_without_this_field"]},sort_keys=True))

if __name__=="__main__":
    main()
