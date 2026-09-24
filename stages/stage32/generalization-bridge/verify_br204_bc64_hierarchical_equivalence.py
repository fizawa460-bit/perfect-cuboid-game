#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import subprocess
import tempfile
from pathlib import Path

def req(v:bool,msg:str)->None:
    if not v: raise SystemExit("FAIL: "+msg)

def run(cmd:list[str])->None:
    subprocess.run(cmd,check=True)

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--direct-worker-source",default="stages/stage32/generalization-bridge/run_br204_full178_b_unit.cpp")
    ap.add_argument("--shard-worker-source",default="stages/stage32/generalization-bridge/run_br204_full178_bc_shard.cpp")
    ap.add_argument("--combiner",default="stages/stage32/generalization-bridge/combine_br204_bc_shards.py")
    ap.add_argument("--group-combiner",default="stages/stage32/generalization-bridge/combine_br204_bc64_to_bc16_parent.py")
    ap.add_argument("--include-dir",action="append",default=[])
    ap.add_argument("--b",type=int,default=0)
    ap.add_argument("--d",type=int,default=8)
    a=ap.parse_args()
    direct=Path(a.direct_worker_source); shard=Path(a.shard_worker_source)
    combiner=Path(a.combiner); group=Path(a.group_combiner)
    req(all(p.is_file() for p in (direct,shard,combiner,group)),"missing source")
    worker_blob=subprocess.check_output(["git","hash-object",str(direct)],text=True).strip()
    req(worker_blob=="0d5ee8e1013cab6120e957707a363e86b3c0d41e","audited generation1 worker blob drift")
    with tempfile.TemporaryDirectory() as td:
        root=Path(td); c64=root/"c64"; p16=root/"p16"; c64.mkdir(); p16.mkdir()
        direct_exe=root/"direct"; shard_exe=root/"shard"
        cc=["g++","-O2","-std=c++20"]
        for inc in a.include_dir: cc += ["-I",inc]
        run(cc+[str(direct),"-o",str(direct_exe)])
        run(cc+[str(shard),"-o",str(shard_exe)])
        direct_out=root/"direct.tsv"
        run([str(direct_exe),"--b",str(a.b),"--d-lo",str(a.d),"--d-hi",str(a.d),
             "--worker-blob",worker_blob,"--out",str(direct_out)])
        for i in range(64):
            out=c64/f"br204-f-b{a.b}-d{a.d}-bc{i}of64.tsv"
            run([str(shard_exe),"--b",str(a.b),"--d-lo",str(a.d),"--d-hi",str(a.d),
                 "--bc-shard-index",str(i),"--bc-shard-count","64",
                 "--worker-blob",worker_blob,"--out",str(out)])
        for p in range(16):
            out=p16/f"br204-f-b{a.b}-d{a.d}-bc{p}of16.tsv"
            run(["python3",str(group),"--input-dir",str(c64),"--b",str(a.b),"--d",str(a.d),
                 "--parent-index",str(p),"--parent-count","16","--child-count","64",
                 "--worker-blob",worker_blob,"--out",str(out)])
        joined=root/"joined.tsv"
        run(["python3",str(combiner),"--input-dir",str(p16),"--b",str(a.b),"--d",str(a.d),
             "--shard-count","16","--worker-blob",worker_blob,"--out",str(joined)])
        x=direct_out.read_bytes(); y=joined.read_bytes()
        req(x==y,"direct vs BC64->BC16 hierarchical payload mismatch")
        print("PASS BR204 hierarchical BC equivalence",
              f"b={a.b}",f"d={a.d}",f"bytes={len(x)}",
              f"sha256={hashlib.sha256(x).hexdigest()}")

if __name__=="__main__":
    main()
