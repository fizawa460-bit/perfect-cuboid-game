#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess,sys,time
from pathlib import Path

D_BANDS=((8,54),(56,100),(102,146),(148,192))

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)

def expected_ds(b,lo,hi):
    req((lo,hi) in D_BANDS,"unapproved band")
    return [d for d in range(lo,hi+1,2) if d>=max(8,2*b)]

def main():
    ap=argparse.ArgumentParser()
    for k in ("worker","combiner","worker-blob","out-dir"): ap.add_argument("--"+k,required=True)
    ap.add_argument("--b",type=int,required=True); ap.add_argument("--band-lo",type=int,required=True); ap.add_argument("--band-hi",type=int,required=True)
    ap.add_argument("--resume-dir",action="append",default=[]); ap.add_argument("--soft-seconds",type=int,default=13500); ap.add_argument("--slice-timeout-seconds",type=int,default=3600)
    a=ap.parse_args(); ds=expected_ds(a.b,a.band_lo,a.band_hi); req(ds,"empty band")
    out=Path(a.out_dir); slices=out/"new-slices"; slices.mkdir(parents=True,exist_ok=True)
    started=time.monotonic()
    inspect=[sys.executable,a.combiner,"inspect-partial","--b",str(a.b),"--band-lo",str(a.band_lo),"--band-hi",str(a.band_hi),"--worker-blob",a.worker_blob]
    for r in a.resume_dir: inspect += ["--input-dir",r]
    cp=subprocess.run(inspect,text=True,capture_output=True); req(cp.returncode==0,cp.stderr.strip())
    info=json.loads(cp.stdout.strip().splitlines()[-1]); recovered=info["state"]["completed_d"] if info.get("found") else []
    completed=set(map(int,recovered)); stop_reason=None; failed_d=None
    for d in ds:
        if d in completed: continue
        if time.monotonic()-started>=a.soft_seconds:
            stop_reason="SOFT_DEADLINE"; break
        plain=out/f"br204-s-b{a.b}-d{d}.tsv"; gz=slices/f"br204-s-b{a.b}-d{d}.tsv.gz"
        cmd=[a.worker,"--b",str(a.b),"--d-lo",str(d),"--d-hi",str(d),"--worker-blob",a.worker_blob,"--out",str(plain)]
        try: w=subprocess.run(cmd,timeout=a.slice_timeout_seconds)
        except subprocess.TimeoutExpired:
            stop_reason="SINGLE_D_TIMEOUT_REQUIRES_FINER_PARTITION"; failed_d=d; plain.unlink(missing_ok=True); break
        if w.returncode!=0:
            stop_reason=f"SINGLE_D_WORKER_FAILURE_{w.returncode}"; failed_d=d; plain.unlink(missing_ok=True); break
        v=subprocess.run([sys.executable,a.combiner,"validate-slice","--path",str(plain),"--b",str(a.b),"--d",str(d),"--worker-blob",a.worker_blob])
        req(v.returncode==0,f"slice validate failed d={d}")
        import gzip,shutil
        with plain.open("rb") as inp,gz.open("wb") as o:
            with gzip.GzipFile(filename="",mode="wb",fileobj=o,compresslevel=9,mtime=0) as z: shutil.copyfileobj(inp,z)
        plain.unlink(); completed.add(d)
    roll=[sys.executable,a.combiner,"rollup","--b",str(a.b),"--band-lo",str(a.band_lo),"--band-hi",str(a.band_hi),"--worker-blob",a.worker_blob,"--out-dir",str(out/"rollup"),"--slice-dir",str(slices)]
    for r in a.resume_dir: roll += ["--prior-dir",r]
    if completed:
        rr=subprocess.run(roll,text=True,capture_output=True); req(rr.returncode==0,rr.stderr.strip())
        roll_status=json.loads((out/"rollup"/"ROLLUP-STATUS.json").read_text())
        completed= set(roll_status["completed_d"])
    else:
        roll_status={"complete":False,"completed_d":[],"missing_d":ds,"payload":None,"payload_gzip_bytes":0}
    missing=sorted(set(ds)-completed); complete=not missing
    if complete: stop_reason="COMPLETE"
    elif stop_reason is None: stop_reason="PARTIAL_UNKNOWN"
    status={"schema":"STAGE32_BR204_RESUMABLE_BAND_STATUS_V2_ROLLED_PARTIAL","b":a.b,"band":[a.band_lo,a.band_hi],"expected_d":ds,"recovered_d":sorted(map(int,recovered)),"completed_d":sorted(completed),"missing_d":missing,"complete":complete,"stop_reason":stop_reason,"failed_d":failed_d,"soft_seconds":a.soft_seconds,"slice_timeout_seconds":a.slice_timeout_seconds,"elapsed_seconds":round(time.monotonic()-started,3),"worker_blob":a.worker_blob,"rollup_payload":roll_status.get("payload"),"rollup_payload_gzip_bytes":roll_status.get("payload_gzip_bytes",0)}
    (out/"STATUS.json").write_text(json.dumps(status,sort_keys=True,indent=2)+"\n")
    print(json.dumps(status,sort_keys=True))

if __name__=="__main__": main()
