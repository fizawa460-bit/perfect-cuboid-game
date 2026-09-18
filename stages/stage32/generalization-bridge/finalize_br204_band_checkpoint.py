#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: "+msg)

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--combiner",required=True)
    ap.add_argument("--out-dir",required=True)
    ap.add_argument("--b",type=int,required=True)
    ap.add_argument("--band-lo",type=int,required=True)
    ap.add_argument("--band-hi",type=int,required=True)
    ap.add_argument("--worker-blob",required=True)
    a=ap.parse_args()

    out=Path(a.out_dir)
    out.mkdir(parents=True,exist_ok=True)
    status_path=out/"STATUS.json"
    if status_path.exists():
        s=json.loads(status_path.read_text())
    else:
        final=out/f"br204-u-b{a.b}-d{a.band_lo}-{a.band_hi}.tsv.gz"
        if final.exists():
            s={
                "schema":"STAGE32_BR204_RESUMABLE_BAND_STATUS_V3_DURABLE_LOCAL_ROLLUP",
                "b":a.b,"band":[a.band_lo,a.band_hi],
                "complete":True,"stop_reason":"INTERRUPTED_AFTER_COMPLETE_ROLLUP",
                "failed_d":None,"rollup_payload":final.name,
                "rollup_payload_gzip_bytes":final.stat().st_size,
                "checkpoint_after_each_completed_d":True,
            }
        else:
            cmd=[
                sys.executable,a.combiner,"inspect-partial",
                "--input-dir",str(out),
                "--b",str(a.b),"--band-lo",str(a.band_lo),"--band-hi",str(a.band_hi),
                "--worker-blob",a.worker_blob,
            ]
            cp=subprocess.run(cmd,text=True,capture_output=True)
            req(cp.returncode==0,cp.stderr.strip())
            info=json.loads(cp.stdout.strip().splitlines()[-1])
            if info.get("found"):
                st=info["state"]
                payload=out/f"br204-partial-b{a.b}-d{a.band_lo}-{a.band_hi}.tsv.gz"
                req(payload.exists(),"validated partial state missing local payload")
                s={
                    "schema":"STAGE32_BR204_RESUMABLE_BAND_STATUS_V3_DURABLE_LOCAL_ROLLUP",
                    "b":a.b,"band":[a.band_lo,a.band_hi],
                    "expected_d":sorted(list(map(int,st["completed_d"]))+list(map(int,st["missing_d"]))),
                    "recovered_d":[],
                    "completed_d":list(map(int,st["completed_d"])),
                    "missing_d":list(map(int,st["missing_d"])),
                    "complete":False,
                    "stop_reason":"INTERRUPTED_AFTER_LAST_D_CHECKPOINT",
                    "failed_d":None,
                    "worker_blob":a.worker_blob,
                    "rollup_payload":payload.name,
                    "rollup_payload_gzip_bytes":payload.stat().st_size,
                    "checkpoint_after_each_completed_d":True,
                }
            else:
                s={
                    "schema":"STAGE32_BR204_RESUMABLE_BAND_STATUS_V3_DURABLE_LOCAL_ROLLUP",
                    "b":a.b,"band":[a.band_lo,a.band_hi],
                    "completed_d":[],"complete":False,
                    "stop_reason":"INTERRUPTED_WITHOUT_DURABLE_D_CHECKPOINT",
                    "failed_d":None,
                    "worker_blob":a.worker_blob,
                    "rollup_payload":None,
                    "rollup_payload_gzip_bytes":0,
                    "checkpoint_after_each_completed_d":True,
                }
        status_path.write_text(json.dumps(s,sort_keys=True,indent=2)+"\n")

    req(s.get("b")==a.b and s.get("band")==[a.band_lo,a.band_hi],"status identity drift")
    payload_bytes=int(s.get("rollup_payload_gzip_bytes",0))
    req(payload_bytes<=900000,"recovery slot too large")
    final=out/f"br204-u-b{a.b}-d{a.band_lo}-{a.band_hi}.tsv.gz"
    final_bytes=final.stat().st_size if final.exists() else 0
    req(final_bytes<=900000,"final band gzip too large")
    result={
        "complete":bool(s.get("complete")),
        "stop_reason":s.get("stop_reason"),
        "payload_bytes":payload_bytes,
        "final_bytes":final_bytes,
        "has_partial":(out/f"br204-partial-b{a.b}-d{a.band_lo}-{a.band_hi}.tsv.gz").exists(),
        "status":str(status_path),
    }
    print(json.dumps(result,sort_keys=True))

if __name__=="__main__":
    main()
