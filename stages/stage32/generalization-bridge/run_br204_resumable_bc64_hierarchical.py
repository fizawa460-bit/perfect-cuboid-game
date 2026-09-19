#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

PARENT_COUNT=16
CHILD_COUNT=64

def req(v:bool,msg:str)->None:
    if not v: raise SystemExit("FAIL: "+msg)

def gzip_deterministic(src:Path,dst:Path)->None:
    with src.open("rb") as inp, dst.open("wb") as out:
        with gzip.GzipFile(filename="",mode="wb",fileobj=out,compresslevel=9,mtime=0) as z:
            shutil.copyfileobj(inp,z)

def shard_name(b:int,d:int,i:int,n:int)->str:
    return f"br204-f-b{b}-d{d}-bc{i}of{n}.tsv.gz"

def validate(combiner:str,p:Path,worker_blob:str,b:int,d:int,i:int,n:int)->str:
    cp=subprocess.run([
        sys.executable,combiner,"--validate-path",str(p),
        "--b",str(b),"--d",str(d),"--shard-count",str(n),
        "--worker-blob",worker_blob,"--out","/dev/null"
    ],text=True,capture_output=True)
    req(cp.returncode==0,cp.stderr.strip() or f"invalid shard {p}")
    x=json.loads(cp.stdout.strip().splitlines()[-1])
    req(x["idx"]==i and x["count"]==n,f"shard identity drift {p}")
    return x["sha256"]

def locate(roots:list[Path],combiner:str,worker_blob:str,b:int,d:int,i:int,n:int)->Path|None:
    hits=[]
    name=shard_name(b,d,i,n)
    for root in roots:
        if not root.exists(): continue
        for p in root.rglob(name):
            sha=validate(combiner,p,worker_blob,b,d,i,n)
            hits.append((sha,p))
    if not hits: return None
    req(len({x[0] for x in hits})==1,f"conflicting duplicate b={b} d={d} i={i} n={n}")
    return hits[0][1]

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--shard-worker",required=True)
    ap.add_argument("--combiner",required=True)
    ap.add_argument("--group-combiner",required=True)
    ap.add_argument("--worker-blob",required=True)
    ap.add_argument("--b",type=int,required=True)
    ap.add_argument("--d",type=int,required=True)
    ap.add_argument("--resume-dir",action="append",default=[])
    ap.add_argument("--out-dir",required=True)
    ap.add_argument("--child-timeout-seconds",type=int,default=1200)
    ap.add_argument("--soft-seconds",type=int,default=13500)
    a=ap.parse_args()
    req(0<=a.b<=96,"b outside 0..96")
    req(a.d==148 and a.d>=2*a.b,"hierarchical generation3 route is d=148 only")
    req(a.child_timeout_seconds>0 and a.soft_seconds>0,"nonpositive timeout")

    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    parents=out/"parents"; parents.mkdir(exist_ok=True)
    children=out/"children"; children.mkdir(exist_ok=True)
    roots=[Path(x) for x in a.resume_dir]
    started=time.monotonic()
    recovered_parents=[]; completed_parents=[]
    recovered_children=[]; completed_children=[]
    failed_parent=None; failed_child=None; stop_reason=None

    def checkpoint()->None:
        retained_children=[]
        for p in sorted(children.glob(f"br204-f-b{a.b}-d{a.d}-bc*of64.tsv.gz")):
            name=p.name
            i=int(name.split("-bc",1)[1].split("of64",1)[0])
            retained_children.append({
                "idx":i,"name":name,"gzip_bytes":p.stat().st_size,
                "gzip_sha256":hashlib.sha256(p.read_bytes()).hexdigest()
            })
        rows=[]
        for i in sorted(set(completed_parents)):
            p=parents/shard_name(a.b,a.d,i,PARENT_COUNT)
            rows.append({
                "idx":i,"name":p.name,"gzip_bytes":p.stat().st_size,
                "gzip_sha256":hashlib.sha256(p.read_bytes()).hexdigest()
            })
        missing=sorted(set(range(PARENT_COUNT))-set(completed_parents))
        status={
            "schema":"STAGE32_BR204_HIERARCHICAL_BC_RECOVERY_V1",
            "b":a.b,"d":a.d,"parent_count":PARENT_COUNT,"child_count":CHILD_COUNT,
            "worker_blob":a.worker_blob,
            "recovered_parent_shards":sorted(set(recovered_parents)),
            "completed_parent_shards":sorted(set(completed_parents)),
            "missing_parent_shards":missing,
            "recovered_child64_indices":sorted(set(recovered_children)),
            "completed_child64_indices":sorted(set(completed_children)),
            "retained_child64_payloads":retained_children,
            "validated_parent_payloads":rows,
            "complete":not missing,
            "failed_parent":failed_parent,
            "failed_child64":failed_child,
            "stop_reason":stop_reason or ("COMPLETE" if not missing else "IN_PROGRESS"),
            "child_timeout_seconds":a.child_timeout_seconds,
            "soft_seconds":a.soft_seconds,
            "elapsed_seconds":round(time.monotonic()-started,3)
        }
        (out/"HIERARCHICAL-BC-STATUS.json").write_text(json.dumps(status,sort_keys=True,indent=2)+"\n")

    # Carry any already-validated BC16 parents from generation2/generation3 artifacts.
    for pidx in range(PARENT_COUNT):
        p=locate(roots,a.combiner,a.worker_blob,a.b,a.d,pidx,PARENT_COUNT)
        if p is None: continue
        dst=parents/shard_name(a.b,a.d,pidx,PARENT_COUNT)
        shutil.copy2(p,dst)
        recovered_parents.append(pidx); completed_parents.append(pidx)
    checkpoint()

    for pidx in range(PARENT_COUNT):
        if pidx in completed_parents: continue
        expected=list(range(pidx,CHILD_COUNT,PARENT_COUNT))
        req(len(expected)==4,"four-child partition drift")
        for cidx in expected:
            if time.monotonic()-started>=a.soft_seconds:
                failed_parent=pidx; stop_reason="SOFT_DEADLINE"; checkpoint(); break
            existing=locate(roots+[children],a.combiner,a.worker_blob,a.b,a.d,cidx,CHILD_COUNT)
            if existing is not None:
                dst=children/shard_name(a.b,a.d,cidx,CHILD_COUNT)
                if existing.resolve()!=dst.resolve(): shutil.copy2(existing,dst)
                recovered_children.append(cidx); completed_children.append(cidx)
                checkpoint()
                continue
            plain=out/f"br204-f-b{a.b}-d{a.d}-bc{cidx}of64.tsv"
            gz=children/shard_name(a.b,a.d,cidx,CHILD_COUNT)
            cmd=[
                a.shard_worker,"--b",str(a.b),"--d-lo",str(a.d),"--d-hi",str(a.d),
                "--bc-shard-index",str(cidx),"--bc-shard-count",str(CHILD_COUNT),
                "--worker-blob",a.worker_blob,"--out",str(plain)
            ]
            try:
                cp=subprocess.run(cmd,timeout=a.child_timeout_seconds)
            except subprocess.TimeoutExpired:
                plain.unlink(missing_ok=True)
                failed_parent=pidx; failed_child=cidx
                stop_reason="SINGLE_BC64_CHILD_TIMEOUT_REQUIRES_FINER_PARTITION"
                checkpoint(); break
            if cp.returncode!=0:
                plain.unlink(missing_ok=True)
                failed_parent=pidx; failed_child=cidx
                stop_reason=f"BC64_CHILD_WORKER_FAILURE_{cp.returncode}"
                checkpoint(); break
            validate(a.combiner,plain,a.worker_blob,a.b,a.d,cidx,CHILD_COUNT)
            gzip_deterministic(plain,gz); plain.unlink()
            completed_children.append(cidx); checkpoint()
        if stop_reason is not None: break

        # Four exact BC64 children reconstruct this exact BC16 parent.
        parent_plain=out/f"br204-f-b{a.b}-d{a.d}-bc{pidx}of16.tsv"
        cp=subprocess.run([
            sys.executable,a.group_combiner,"--input-dir",str(children),
            "--b",str(a.b),"--d",str(a.d),"--parent-index",str(pidx),
            "--parent-count",str(PARENT_COUNT),"--child-count",str(CHILD_COUNT),
            "--worker-blob",a.worker_blob,"--out",str(parent_plain)
        ])
        req(cp.returncode==0,f"BC64 child union failed parent={pidx}")
        validate(a.combiner,parent_plain,a.worker_blob,a.b,a.d,pidx,PARENT_COUNT)
        parent_gz=parents/shard_name(a.b,a.d,pidx,PARENT_COUNT)
        gzip_deterministic(parent_plain,parent_gz); parent_plain.unlink()
        completed_parents.append(pidx)
        for cidx in expected:
            (children/shard_name(a.b,a.d,cidx,CHILD_COUNT)).unlink(missing_ok=True)
        checkpoint()

    completed_parents=sorted(set(completed_parents))
    complete=completed_parents==list(range(PARENT_COUNT))
    if complete:
        canonical=out/f"br204-s-b{a.b}-d{a.d}.tsv"
        cp=subprocess.run([
            sys.executable,a.combiner,"--input-dir",str(parents),
            "--b",str(a.b),"--d",str(a.d),"--shard-count",str(PARENT_COUNT),
            "--worker-blob",a.worker_blob,"--out",str(canonical)
        ])
        req(cp.returncode==0,"BC16 parent union failed")
        stop_reason="COMPLETE"
        checkpoint()
    elif stop_reason is None:
        stop_reason="PARTIAL_UNKNOWN"; checkpoint()

    print((out/"HIERARCHICAL-BC-STATUS.json").read_text().strip())
    if not complete:
        raise SystemExit(75 if stop_reason=="SOFT_DEADLINE" else 76)

if __name__=="__main__":
    main()
