#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

D_BANDS=((8,54),(56,100),(102,146),(148,192))

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: "+msg)

def expected_ds(b:int, lo:int, hi:int) -> list[int]:
    req((lo,hi) in D_BANDS, "unapproved band")
    return [d for d in range(lo,hi+1,2) if d>=max(8,2*b)]

def gzip_deterministic(src:Path,dst:Path) -> None:
    with src.open("rb") as inp, dst.open("wb") as out:
        with gzip.GzipFile(filename="",mode="wb",fileobj=out,compresslevel=9,mtime=0) as gz:
            shutil.copyfileobj(inp,gz)

def run_checked(cmd:list[str]) -> None:
    subprocess.run(cmd,check=True)

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--worker",required=True)
    ap.add_argument("--combiner",required=True)
    ap.add_argument("--b",type=int,required=True)
    ap.add_argument("--band-lo",type=int,required=True)
    ap.add_argument("--band-hi",type=int,required=True)
    ap.add_argument("--worker-blob",required=True)
    ap.add_argument("--resume-dir",action="append",default=[])
    ap.add_argument("--out-dir",required=True)
    ap.add_argument("--soft-seconds",type=int,default=13500)
    ap.add_argument("--slice-timeout-seconds",type=int,default=3600)
    a=ap.parse_args()
    req(0<=a.b<=96,"b outside 0..96")
    ds=expected_ds(a.b,a.band_lo,a.band_hi)
    req(ds,"band has no admissible d")
    out=Path(a.out_dir); slices=out/"slices"; slices.mkdir(parents=True,exist_ok=True)
    status_path=out/"STATUS.json"
    started=time.monotonic()

    # Recover only source-locked, exact single-d slices for this b/band.
    recovered=[]
    for d in ds:
        name=f"br204-s-b{a.b}-d{d}.tsv.gz"
        candidates=[]
        for root in map(Path,a.resume_dir):
            if root.exists(): candidates.extend(sorted(root.rglob(name)))
        if not candidates: continue
        hashes={}
        for p in candidates:
            cp=subprocess.run([sys.executable,a.combiner,"validate-slice","--path",str(p),"--b",str(a.b),"--d",str(d),"--worker-blob",a.worker_blob],text=True,capture_output=True)
            req(cp.returncode==0,f"invalid recovered slice {p}: {cp.stderr.strip()}")
            raw=p.read_bytes(); import hashlib
            hashes.setdefault(hashlib.sha256(raw).hexdigest(),p)
        req(len(hashes)==1,f"conflicting recovered slice d={d}")
        src=next(iter(hashes.values()))
        shutil.copy2(src,slices/name)
        recovered.append(d)

    completed=set(recovered)
    stop_reason=None
    failed_d=None
    for d in ds:
        if d in completed: continue
        if time.monotonic()-started >= a.soft_seconds:
            stop_reason="SOFT_DEADLINE"
            break
        plain=out/f"br204-s-b{a.b}-d{d}.tsv"
        gz=slices/f"br204-s-b{a.b}-d{d}.tsv.gz"
        cmd=[a.worker,"--b",str(a.b),"--d-lo",str(d),"--d-hi",str(d),"--worker-blob",a.worker_blob,"--out",str(plain)]
        try:
            cp=subprocess.run(cmd,timeout=a.slice_timeout_seconds)
        except subprocess.TimeoutExpired:
            stop_reason="SINGLE_D_TIMEOUT_REQUIRES_FINER_PARTITION"
            failed_d=d
            plain.unlink(missing_ok=True)
            break
        if cp.returncode!=0:
            stop_reason=f"SINGLE_D_WORKER_FAILURE_{cp.returncode}"
            failed_d=d
            plain.unlink(missing_ok=True)
            break
        run_checked([sys.executable,a.combiner,"validate-slice","--path",str(plain),"--b",str(a.b),"--d",str(d),"--worker-blob",a.worker_blob])
        gzip_deterministic(plain,gz); plain.unlink()
        run_checked([sys.executable,a.combiner,"validate-slice","--path",str(gz),"--b",str(a.b),"--d",str(d),"--worker-blob",a.worker_blob])
        completed.add(d)

    missing=sorted(set(ds)-completed)
    complete=not missing
    final_gz=None
    if complete:
        final_plain=out/f"br204-u-b{a.b}-d{a.band_lo}-{a.band_hi}.tsv"
        run_checked([sys.executable,a.combiner,"combine","--input-dir",str(slices),"--b",str(a.b),"--band-lo",str(a.band_lo),"--band-hi",str(a.band_hi),"--worker-blob",a.worker_blob,"--out",str(final_plain)])
        final_gz=Path(str(final_plain)+".gz")
        gzip_deterministic(final_plain,final_gz); final_plain.unlink()
        stop_reason="COMPLETE"
    elif stop_reason is None:
        stop_reason="PARTIAL_UNKNOWN"

    status={
        "schema":"STAGE32_BR204_RESUMABLE_BAND_STATUS_V1",
        "b":a.b,"band":[a.band_lo,a.band_hi],
        "expected_d":ds,
        "recovered_d":sorted(recovered),
        "completed_d":sorted(completed),
        "missing_d":missing,
        "complete":complete,
        "stop_reason":stop_reason,
        "failed_d":failed_d,
        "soft_seconds":a.soft_seconds,
        "slice_timeout_seconds":a.slice_timeout_seconds,
        "elapsed_seconds":round(time.monotonic()-started,3),
        "worker_blob":a.worker_blob,
        "final_gzip":None if final_gz is None else str(final_gz),
    }
    status_path.write_text(json.dumps(status,sort_keys=True,indent=2)+"\n")
    print(json.dumps(status,sort_keys=True))

if __name__=="__main__":
    main()
