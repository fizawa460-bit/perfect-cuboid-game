#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import subprocess
from pathlib import Path

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: "+msg)

def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def validate(base_combiner: str, p: Path, *, b: int, d: int, count: int, worker_blob: str) -> None:
    cp=subprocess.run(["python",base_combiner,"--validate-path",str(p),"--b",str(b),"--d",str(d),
                       "--shard-count",str(count),"--worker-blob",worker_blob,"--out","/dev/null"],
                      text=True,capture_output=True)
    req(cp.returncode==0,cp.stderr.strip() or cp.stdout.strip() or f"validation failed {p}")

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--base-combiner",required=True)
    ap.add_argument("--out-dir",required=True)
    ap.add_argument("--b",type=int,required=True)
    ap.add_argument("--d",type=int,required=True)
    ap.add_argument("--parent-shard-index",type=int,required=True)
    ap.add_argument("--parent-shard-count",type=int,default=16)
    ap.add_argument("--fine-shard-count",type=int,default=64)
    ap.add_argument("--worker-blob",required=True)
    ap.add_argument("--hard-cap-bytes",type=int,default=300000)
    a=ap.parse_args()
    out=Path(a.out_dir)
    st_path=out/"BC64-PARENT-STATUS.json"
    req(st_path.is_file(),"missing parent status")
    s=json.loads(st_path.read_text())
    req(s["schema"]=="STAGE32_BR204_BC64_PARENT_RECOVERY_V1","status schema")
    req((int(s["b"]),int(s["d"]))==(a.b,a.d),"b/d drift")
    req(int(s["parent_shard_index"])==a.parent_shard_index,"parent index drift")
    req(int(s["parent_shard_count"])==a.parent_shard_count,"parent count drift")
    req(int(s["fine_shard_count"])==a.fine_shard_count,"fine count drift")
    req(s["worker_blob"]==a.worker_blob,"worker blob drift")
    expected=[a.parent_shard_index+k*a.parent_shard_count for k in range(a.fine_shard_count//a.parent_shard_count)]
    done=list(map(int,s["completed_fine_indices"]))
    req(done==sorted(set(done)),"completed fine indices not sorted unique")
    req(set(done)<=set(expected),"completed fine index outside expected")
    req(list(map(int,s["missing_fine_indices"]))==sorted(set(expected)-set(done)),"missing fine drift")
    rows=[]; total=0
    if bool(s["parent_complete"]):
        req(done==expected and not s["missing_fine_indices"],"complete parent missing fine coverage")
        p=out/f"br204-f-b{a.b}-d{a.d}-bc{a.parent_shard_index}of{a.parent_shard_count}.tsv.gz"
        req(p.is_file(),"complete parent payload missing")
        validate(a.base_combiner,p,b=a.b,d=a.d,count=a.parent_shard_count,worker_blob=a.worker_blob)
        total=p.stat().st_size
        rows=[{"kind":"parent","name":p.name,"gzip_bytes":total,"sha256":sha256(p)}]
    else:
        fine=out/"fine"
        for idx in done:
            p=fine/f"br204-f-b{a.b}-d{a.d}-bc{idx}of{a.fine_shard_count}.tsv.gz"
            req(p.is_file(),f"missing fine payload {idx}")
            validate(a.base_combiner,p,b=a.b,d=a.d,count=a.fine_shard_count,worker_blob=a.worker_blob)
            total+=p.stat().st_size
            rows.append({"kind":"fine","idx":idx,"name":p.name,"gzip_bytes":p.stat().st_size,"sha256":sha256(p)})
    req(total<=a.hard_cap_bytes,f"BC64 parent recovery bundle too large {total}>{a.hard_cap_bytes}")
    outj={
      "schema":"STAGE32_BR204_BC64_PARENT_FINALIZER_V1",
      "b":a.b,"d":a.d,
      "parent_shard_index":a.parent_shard_index,"parent_shard_count":a.parent_shard_count,
      "fine_shard_count":a.fine_shard_count,
      "parent_complete":bool(s["parent_complete"]),
      "completed_fine_indices":done,"missing_fine_indices":s["missing_fine_indices"],
      "stop_reason":s["stop_reason"],
      "payload_gzip_bytes":total,"hard_cap_bytes":a.hard_cap_bytes,
      "upload_safe":True,"payloads":rows
    }
    print(json.dumps(outj,sort_keys=True))

if __name__=="__main__":
    main()
