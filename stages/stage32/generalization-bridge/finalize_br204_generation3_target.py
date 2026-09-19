#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

HARD_CAP=5_000_000

def req(v:bool,msg:str)->None:
    if not v: raise SystemExit("FAIL: "+msg)

def validate(combiner:str,p:Path,worker_blob:str,b:int,d:int,i:int,n:int)->dict:
    cp=subprocess.run([
        sys.executable,combiner,"--validate-path",str(p),
        "--b",str(b),"--d",str(d),"--shard-count",str(n),
        "--worker-blob",worker_blob,"--out","/dev/null"
    ],text=True,capture_output=True)
    req(cp.returncode==0,cp.stderr.strip() or f"invalid shard {p}")
    return json.loads(cp.stdout.strip().splitlines()[-1])

def file_row(p:Path)->dict:
    return {"name":p.name,"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}

def gzip_deterministic(src:Path,dst:Path)->None:
    with src.open("rb") as inp, dst.open("wb") as out:
        with gzip.GzipFile(filename="",mode="wb",fileobj=out,compresslevel=9,mtime=0) as z:
            shutil.copyfileobj(inp,z)

def total_bytes(root:Path)->int:
    return sum(p.stat().st_size for p in root.rglob("*") if p.is_file())

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--mode",choices=["flat16","hier64"],required=True)
    ap.add_argument("--combiner",required=True)
    ap.add_argument("--out-dir",required=True)
    ap.add_argument("--b",type=int,required=True)
    ap.add_argument("--d",type=int,required=True)
    ap.add_argument("--worker-blob",required=True)
    a=ap.parse_args()
    out=Path(a.out_dir)
    canonical=out/f"br204-s-b{a.b}-d{a.d}.tsv"
    shard_rows=[]; child_rows=[]

    if a.mode=="flat16":
        sp=out/"BC-SHARD-STATUS.json"
        req(sp.is_file(),"missing flat BC status")
        s=json.loads(sp.read_text())
        req(s["schema"]=="STAGE32_BR204_BC_SHARD_RECOVERY_V1","flat status schema")
        req((s["b"],s["d"],s["shard_count"])==(a.b,a.d,16),"flat status identity")
        req(s["worker_blob"]==a.worker_blob,"flat worker blob")
        done=sorted(map(int,s["completed_shards"]))
        req(done==sorted(set(done)),"flat completed shards")
        for i in done:
            p=out/"shards"/f"br204-f-b{a.b}-d{a.d}-bc{i}of16.tsv.gz"
            req(p.is_file(),f"missing flat shard {i}")
            info=validate(a.combiner,p,a.worker_blob,a.b,a.d,i,16)
            row=file_row(p); row["idx"]=i; row["payload_sha256"]=info["sha256"]; shard_rows.append(row)
        complete=done==list(range(16))
        req(bool(s["complete"])==complete,"flat complete drift")
        stop_reason=s["stop_reason"]
        if complete: req(canonical.is_file(),"flat complete missing canonical")
        status_path=sp
    else:
        sp=out/"HIERARCHICAL-BC-STATUS.json"
        req(sp.is_file(),"missing hierarchical status")
        s=json.loads(sp.read_text())
        req(s["schema"]=="STAGE32_BR204_HIERARCHICAL_BC_RECOVERY_V1","hier status schema")
        req((s["b"],s["d"],s["parent_count"],s["child_count"])==(a.b,a.d,16,64),"hier status identity")
        req(s["worker_blob"]==a.worker_blob,"hier worker blob")
        done=sorted(map(int,s["completed_parent_shards"]))
        req(done==sorted(set(done)),"hier parent set")
        for i in done:
            p=out/"parents"/f"br204-f-b{a.b}-d{a.d}-bc{i}of16.tsv.gz"
            req(p.is_file(),f"missing hierarchical parent {i}")
            info=validate(a.combiner,p,a.worker_blob,a.b,a.d,i,16)
            row=file_row(p); row["idx"]=i; row["payload_sha256"]=info["sha256"]; shard_rows.append(row)
        for p in sorted((out/"children").glob(f"br204-f-b{a.b}-d{a.d}-bc*of64.tsv.gz")) if (out/"children").exists() else []:
            i=int(p.name.split("-bc",1)[1].split("of64",1)[0])
            info=validate(a.combiner,p,a.worker_blob,a.b,a.d,i,64)
            row=file_row(p); row["idx"]=i; row["payload_sha256"]=info["sha256"]; child_rows.append(row)
        complete=done==list(range(16))
        req(bool(s["complete"])==complete,"hier complete drift")
        stop_reason=s["stop_reason"]
        if complete: req(canonical.is_file(),"hier complete missing canonical")
        status_path=sp

    canonical_row=None

    # Completed targets persist only deterministic-gzip canonical slice + compact proof
    # manifest/status. Raw child/parent shards are needed only for incomplete recovery.
    if complete:
        req(canonical.is_file(),"complete target missing canonical before compaction")
        canonical_gz=out/(canonical.name+".gz")
        gzip_deterministic(canonical,canonical_gz)
        canonical.unlink()
        canonical_row=file_row(canonical_gz)
        canonical_row["compression"]="gzip-9-mtime0"
        for d in ("shards","parents","children"):
            shutil.rmtree(out/d,ignore_errors=True)

    manifest={
        "schema":"STAGE32_BR204_GENERATION3_TARGET_FINALIZER_V1",
        "mode":a.mode,"b":a.b,"d":a.d,
        "worker_blob":a.worker_blob,
        "complete":complete,
        "stop_reason":stop_reason,
        "hard_cap_bytes":HARD_CAP,
        "canonical":canonical_row,
        "validated_bc16_payloads":shard_rows,
        "retained_bc64_children":child_rows,
        "compaction_rule":"On complete targets raw shard payloads are deleted after validation; persist deterministic-gzip canonical slice plus manifest/status only. On incomplete targets retain validated recovery payloads.",
        "credit":{"stage32_main":False,"full178_complete":False,"theorem":False,"effectivity":False,"receiver":False,"endpoint":False,"perfect_cuboid":False,"merge":False}
    }
    mp=out/"GEN3-FINALIZER.json"
    mp.write_text(json.dumps(manifest,sort_keys=True,indent=2)+"\n")
    persisted=total_bytes(out)
    req(persisted<=HARD_CAP,f"generation3 persisted target bundle too large {persisted}>{HARD_CAP}")
    manifest["persisted_bytes"]=persisted
    mp.write_text(json.dumps(manifest,sort_keys=True,indent=2)+"\n")
    persisted2=total_bytes(out)
    req(persisted2<=HARD_CAP,f"generation3 final manifest pushed bundle over cap {persisted2}>{HARD_CAP}")
    print(json.dumps({**manifest,"persisted_bytes":persisted2},sort_keys=True))

if __name__=="__main__":
    main()
