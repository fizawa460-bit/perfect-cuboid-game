#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HARD_CAP=900000

def req(v: bool,msg: str)->None:
    if not v:
        raise SystemExit("FAIL: "+msg)

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--combiner",required=True)
    ap.add_argument("--out-dir",required=True)
    ap.add_argument("--b",type=int,required=True)
    ap.add_argument("--d",type=int,required=True)
    ap.add_argument("--shard-count",type=int,default=16)
    ap.add_argument("--worker-blob",required=True)
    a=ap.parse_args()
    out=Path(a.out_dir)
    sp=out/"BC-SHARD-STATUS.json"
    req(sp.is_file(),"missing BC-SHARD-STATUS.json")
    s=json.loads(sp.read_text())
    req(s["schema"]=="STAGE32_BR204_BC_SHARD_RECOVERY_V1","status schema")
    req((s["b"],s["d"],s["shard_count"])==(a.b,a.d,a.shard_count),"status identity")
    req(s["worker_blob"]==a.worker_blob,"status worker blob")
    done=list(map(int,s["completed_shards"]))
    req(done==sorted(set(done)),"completed shards not sorted unique")
    req(set(done)<=set(range(a.shard_count)),"completed shard outside range")
    req(s["missing_shards"]==sorted(set(range(a.shard_count))-set(done)),"missing shard drift")
    total=0
    rows=[]
    for i in done:
        p=out/"shards"/f"br204-f-b{a.b}-d{a.d}-bc{i}of{a.shard_count}.tsv.gz"
        req(p.is_file(),f"missing shard payload {i}")
        cp=subprocess.run([
            sys.executable,a.combiner,"--validate-path",str(p),
            "--b",str(a.b),"--d",str(a.d),"--shard-count",str(a.shard_count),
            "--worker-blob",a.worker_blob,"--out","/dev/null"
        ],text=True,capture_output=True)
        req(cp.returncode==0,cp.stderr.strip() or f"invalid shard {i}")
        x=json.loads(cp.stdout.strip().splitlines()[-1])
        req(x["idx"]==i,"validated shard index drift")
        total+=p.stat().st_size
        rows.append({"idx":i,"gzip_bytes":p.stat().st_size,"sha256":x["sha256"]})
    req(total<=HARD_CAP,f"finer recovery bundle too large {total}>{HARD_CAP}")
    complete=len(done)==a.shard_count
    req(bool(s["complete"])==complete,"status complete drift")
    canonical=out/f"br204-s-b{a.b}-d{a.d}.tsv"
    if complete:
        req(canonical.is_file(),"complete finer set missing canonical d slice")
    result={
        "schema":"STAGE32_BR204_BC_SHARD_FINALIZER_V1",
        "upload_safe":True,
        "complete":complete,
        "b":a.b,"d":a.d,"shard_count":a.shard_count,
        "completed_shards":done,"missing_shards":s["missing_shards"],
        "stop_reason":s["stop_reason"],
        "payload_gzip_bytes":total,
        "hard_cap_bytes":HARD_CAP,
        "canonical_slice_present":canonical.is_file(),
        "validated_shards":rows
    }
    print(json.dumps(result,sort_keys=True))

if __name__=="__main__":
    main()
