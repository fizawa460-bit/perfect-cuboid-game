#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import subprocess
import tempfile
from pathlib import Path

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: "+msg)

def run(cmd:list[str], **kw) -> None:
    subprocess.run(cmd,check=True,**kw)

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--worker-source",default="stages/stage32/generalization-bridge/run_br204_full178_b_unit.cpp")
    ap.add_argument("--combiner",default="stages/stage32/generalization-bridge/combine_br204_bc_shards.py")
    ap.add_argument("--b",type=int,default=0)
    ap.add_argument("--d",type=int,default=8)
    ap.add_argument("--shard-count",type=int,default=16)
    a=ap.parse_args()
    req(a.shard_count==16,"retained preflight requires exactly 16 BC shards")
    source=Path(a.worker_source); combiner=Path(a.combiner)
    req(source.is_file() and combiner.is_file(),"missing source/combiner")
    worker_blob=subprocess.check_output(["git","hash-object",str(source)],text=True).strip()
    req(len(worker_blob)==40,"worker blob")
    with tempfile.TemporaryDirectory() as td:
        root=Path(td); exe=root/"worker"; shards=root/"shards"; shards.mkdir()
        run(["g++","-O2","-std=c++20",str(source),"-o",str(exe)])
        direct=root/"direct.tsv"
        run([str(exe),"--b",str(a.b),"--d-lo",str(a.d),"--d-hi",str(a.d),
             "--worker-blob",worker_blob,"--out",str(direct)])
        for i in range(a.shard_count):
            p=shards/f"br204-f-b{a.b}-d{a.d}-bc{i}of{a.shard_count}.tsv"
            run([str(exe),"--b",str(a.b),"--d-lo",str(a.d),"--d-hi",str(a.d),
                 "--bc-shard-index",str(i),"--bc-shard-count",str(a.shard_count),
                 "--worker-blob",worker_blob,"--out",str(p)])
        joined=root/"joined.tsv"
        run(["python3",str(combiner),"--input-dir",str(shards),"--b",str(a.b),
             "--d",str(a.d),"--shard-count",str(a.shard_count),
             "--worker-blob",worker_blob,"--out",str(joined)])
        x=direct.read_bytes(); y=joined.read_bytes()
        req(x==y,"direct vs 16-shard canonical payload mismatch")
        print("PASS BR204 BC-shard equivalence",
              f"b={a.b}",f"d={a.d}",f"bytes={len(x)}",
              f"sha256={hashlib.sha256(x).hexdigest()}")

if __name__=="__main__":
    main()
