#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: "+msg)

def gzip_deterministic(src: Path, dst: Path) -> None:
    with src.open("rb") as inp, dst.open("wb") as out:
        with gzip.GzipFile(filename="", mode="wb", fileobj=out, compresslevel=9, mtime=0) as z:
            shutil.copyfileobj(inp,z)

def shard_name(b:int,d:int,i:int,n:int) -> str:
    return f"br204-f-b{b}-d{d}-bc{i}of{n}.tsv.gz"

def locate_valid_shard(roots:list[Path], combiner:str, worker_blob:str,
                       b:int,d:int,i:int,n:int) -> Path | None:
    hits=[]
    name=shard_name(b,d,i,n)
    for root in roots:
        if not root.exists():
            continue
        for p in root.rglob(name):
            cp=subprocess.run([
                sys.executable,combiner,"--validate-path",str(p),
                "--b",str(b),"--d",str(d),"--shard-count",str(n),
                "--worker-blob",worker_blob,"--out","/dev/null"
            ],text=True,capture_output=True)
            req(cp.returncode==0,cp.stderr.strip() or f"invalid recovered shard {p}")
            info=json.loads(cp.stdout.strip().splitlines()[-1])
            req(info["idx"]==i and info["count"]==n,f"recovered shard identity drift {p}")
            hits.append((info["sha256"],p))
    if not hits:
        return None
    req(len({h[0] for h in hits})==1,f"conflicting duplicate recovered shard b={b} d={d} i={i}")
    return hits[0][1]

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--shard-worker",required=True)
    ap.add_argument("--combiner",required=True)
    ap.add_argument("--worker-blob",required=True,
                    help="Audited generation-1 worker blob stamped into canonical payload semantics.")
    ap.add_argument("--b",type=int,required=True)
    ap.add_argument("--d",type=int,required=True)
    ap.add_argument("--shard-count",type=int,default=16)
    ap.add_argument("--resume-dir",action="append",default=[])
    ap.add_argument("--out-dir",required=True)
    ap.add_argument("--shard-timeout-seconds",type=int,default=1200)
    ap.add_argument("--soft-seconds",type=int,default=13500)
    a=ap.parse_args()

    req(0<=a.b<=96,"b outside 0..96")
    req(8<=a.d<=192 and a.d%2==0 and a.d>=2*a.b,"invalid/admissibility d")
    req(a.shard_count==16,"retained generation-2 preflight requires 16 shards")
    req(a.shard_timeout_seconds>0 and a.soft_seconds>0,"nonpositive timeout")

    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    roots=[Path(x) for x in a.resume_dir]
    local=out/"shards"; local.mkdir(exist_ok=True)
    started=time.monotonic()
    recovered=[]; completed=[]; failed_shard=None; stop_reason=None

    # Re-emit validated predecessor shards locally first, preserving exact digests.
    for i in range(a.shard_count):
        p=locate_valid_shard(roots,a.combiner,a.worker_blob,a.b,a.d,i,a.shard_count)
        if p is None:
            continue
        dst=local/shard_name(a.b,a.d,i,a.shard_count)
        shutil.copy2(p,dst)
        recovered.append(i); completed.append(i)

    for i in range(a.shard_count):
        if i in completed:
            continue
        if time.monotonic()-started>=a.soft_seconds:
            stop_reason="SOFT_DEADLINE"
            break
        plain=out/f"br204-f-b{a.b}-d{a.d}-bc{i}of{a.shard_count}.tsv"
        gz=local/shard_name(a.b,a.d,i,a.shard_count)
        cmd=[
            a.shard_worker,"--b",str(a.b),"--d-lo",str(a.d),"--d-hi",str(a.d),
            "--bc-shard-index",str(i),"--bc-shard-count",str(a.shard_count),
            "--worker-blob",a.worker_blob,"--out",str(plain)
        ]
        try:
            cp=subprocess.run(cmd,timeout=a.shard_timeout_seconds)
        except subprocess.TimeoutExpired:
            plain.unlink(missing_ok=True)
            failed_shard=i; stop_reason="SINGLE_BC_SHARD_TIMEOUT_REQUIRES_FINER_PARTITION"
            break
        if cp.returncode!=0:
            plain.unlink(missing_ok=True)
            failed_shard=i; stop_reason=f"BC_SHARD_WORKER_FAILURE_{cp.returncode}"
            break
        # Validate before persist.
        vp=subprocess.run([
            sys.executable,a.combiner,"--validate-path",str(plain),
            "--b",str(a.b),"--d",str(a.d),"--shard-count",str(a.shard_count),
            "--worker-blob",a.worker_blob,"--out","/dev/null"
        ])
        req(vp.returncode==0,f"new shard validation failed i={i}")
        gzip_deterministic(plain,gz); plain.unlink()
        completed.append(i)

    completed=sorted(set(completed))
    missing=sorted(set(range(a.shard_count))-set(completed))
    complete=not missing
    if complete:
        canonical=out/f"br204-s-b{a.b}-d{a.d}.tsv"
        cp=subprocess.run([
            sys.executable,a.combiner,"--input-dir",str(local),
            "--b",str(a.b),"--d",str(a.d),"--shard-count",str(a.shard_count),
            "--worker-blob",a.worker_blob,"--out",str(canonical)
        ])
        req(cp.returncode==0,"BC shard union failed")
        stop_reason="COMPLETE"
    elif stop_reason is None:
        stop_reason="PARTIAL_UNKNOWN"

    # Compact manifest is itself enough to tell the always-path uploader exactly
    # which validated shard payloads are recovery-eligible.
    rows=[]
    import hashlib
    for i in completed:
        p=local/shard_name(a.b,a.d,i,a.shard_count)
        rows.append({
            "idx":i,"name":p.name,"gzip_bytes":p.stat().st_size,
            "gzip_sha256":hashlib.sha256(p.read_bytes()).hexdigest()
        })
    status={
        "schema":"STAGE32_BR204_BC_SHARD_RECOVERY_V1",
        "b":a.b,"d":a.d,"shard_count":a.shard_count,
        "worker_blob":a.worker_blob,
        "recovered_shards":sorted(recovered),
        "completed_shards":completed,
        "missing_shards":missing,
        "complete":complete,
        "failed_shard":failed_shard,
        "stop_reason":stop_reason,
        "shard_timeout_seconds":a.shard_timeout_seconds,
        "soft_seconds":a.soft_seconds,
        "elapsed_seconds":round(time.monotonic()-started,3),
        "validated_shards":rows
    }
    (out/"BC-SHARD-STATUS.json").write_text(json.dumps(status,sort_keys=True,indent=2)+"\n")
    print(json.dumps(status,sort_keys=True))
    if not complete:
        raise SystemExit(75 if stop_reason=="SOFT_DEADLINE" else 76)

if __name__=="__main__":
    main()
