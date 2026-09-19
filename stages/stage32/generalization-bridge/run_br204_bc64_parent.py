#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import json
import shutil
import subprocess
import time
from pathlib import Path

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: "+msg)

def validate(base_combiner: str, p: Path, *, b: int, d: int, count: int, worker_blob: str) -> None:
    cp=subprocess.run(["python",base_combiner,"--validate-path",str(p),"--b",str(b),"--d",str(d),
                       "--shard-count",str(count),"--worker-blob",worker_blob,"--out","/dev/null"],
                      text=True,capture_output=True)
    req(cp.returncode==0,cp.stderr.strip() or cp.stdout.strip() or f"validation failed {p}")

def gz_write(src: Path, dst: Path) -> None:
    dst.write_bytes(gzip.compress(src.read_bytes(),compresslevel=9,mtime=0))

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--worker",required=True)
    ap.add_argument("--base-combiner",required=True)
    ap.add_argument("--parent-combiner",required=True)
    ap.add_argument("--worker-blob",required=True)
    ap.add_argument("--b",type=int,required=True)
    ap.add_argument("--d",type=int,required=True)
    ap.add_argument("--parent-shard-index",type=int,required=True)
    ap.add_argument("--parent-shard-count",type=int,default=16)
    ap.add_argument("--fine-shard-count",type=int,default=64)
    ap.add_argument("--out-dir",required=True)
    ap.add_argument("--subshard-timeout-seconds",type=int,default=1200)
    a=ap.parse_args()
    req(a.fine_shard_count%a.parent_shard_count==0,"fine/parent relation")
    req(0<=a.parent_shard_index<a.parent_shard_count,"parent index")
    out=Path(a.out_dir); fine=out/"fine"; fine.mkdir(parents=True,exist_ok=True)
    expected=[a.parent_shard_index+k*a.parent_shard_count for k in range(a.fine_shard_count//a.parent_shard_count)]
    completed=[]; failed=None; stop_reason=None
    started=time.monotonic()
    for idx in expected:
        p=fine/f"br204-f-b{a.b}-d{a.d}-bc{idx}of{a.fine_shard_count}.tsv.gz"
        if p.is_file():
            validate(a.base_combiner,p,b=a.b,d=a.d,count=a.fine_shard_count,worker_blob=a.worker_blob)
            completed.append(idx)
    for idx in expected:
        if idx in completed:
            continue
        tmp=out/f".fine-{idx}.tsv"
        cmd=[a.worker,"--b",str(a.b),"--d-lo",str(a.d),"--d-hi",str(a.d),
             "--out",str(tmp),"--worker-blob",a.worker_blob,
             "--bc-shard-index",str(idx),"--bc-shard-count",str(a.fine_shard_count)]
        try:
            cp=subprocess.run(cmd,timeout=a.subshard_timeout_seconds)
        except subprocess.TimeoutExpired:
            failed=idx; stop_reason="SINGLE_BC64_SUBSHARD_TIMEOUT_REQUIRES_FINER_PARTITION"; break
        if cp.returncode!=0:
            failed=idx; stop_reason=f"BC64_SUBSHARD_WORKER_FAILURE_{cp.returncode}"; break
        p=fine/f"br204-f-b{a.b}-d{a.d}-bc{idx}of{a.fine_shard_count}.tsv.gz"
        gz_write(tmp,p); tmp.unlink(missing_ok=True)
        validate(a.base_combiner,p,b=a.b,d=a.d,count=a.fine_shard_count,worker_blob=a.worker_blob)
        completed.append(idx)
    completed=sorted(set(completed))
    missing=sorted(set(expected)-set(completed))
    parent_complete=not missing
    parent_gz=None
    if parent_complete:
        parent_plain=out/f"br204-f-b{a.b}-d{a.d}-bc{a.parent_shard_index}of{a.parent_shard_count}.tsv"
        cp=subprocess.run(["python",a.parent_combiner,"--input-dir",str(fine),
                           "--b",str(a.b),"--d",str(a.d),
                           "--parent-shard-index",str(a.parent_shard_index),
                           "--parent-shard-count",str(a.parent_shard_count),
                           "--fine-shard-count",str(a.fine_shard_count),
                           "--worker-blob",a.worker_blob,"--out",str(parent_plain)])
        req(cp.returncode==0,"64-to-16 parent combine failed")
        parent_gz=out/(parent_plain.name+".gz")
        gz_write(parent_plain,parent_gz); parent_plain.unlink()
        validate(a.base_combiner,parent_gz,b=a.b,d=a.d,count=a.parent_shard_count,worker_blob=a.worker_blob)
        shutil.rmtree(fine)
        stop_reason="COMPLETE"
    elif stop_reason is None:
        stop_reason="INCOMPLETE"
    status={
      "schema":"STAGE32_BR204_BC64_PARENT_RECOVERY_V1",
      "b":a.b,"d":a.d,
      "parent_shard_index":a.parent_shard_index,"parent_shard_count":a.parent_shard_count,
      "fine_shard_count":a.fine_shard_count,"expected_fine_indices":expected,
      "completed_fine_indices":completed,"missing_fine_indices":missing,
      "failed_fine_index":failed,"parent_complete":parent_complete,
      "parent_payload":None if parent_gz is None else parent_gz.name,
      "stop_reason":stop_reason,
      "elapsed_seconds":round(time.monotonic()-started,3),
      "worker_blob":a.worker_blob
    }
    (out/"BC64-PARENT-STATUS.json").write_text(json.dumps(status,sort_keys=True,indent=2)+"\n")
    print(json.dumps(status,sort_keys=True))
    if not parent_complete:
        raise SystemExit(76 if stop_reason=="SINGLE_BC64_SUBSHARD_TIMEOUT_REQUIRES_FINER_PARTITION" else 1)

if __name__=="__main__":
    main()
