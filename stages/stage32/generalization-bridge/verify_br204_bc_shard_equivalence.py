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
    ap.add_argument("--direct-worker-source",default="stages/stage32/generalization-bridge/run_br204_full178_b_unit.cpp")
    ap.add_argument("--shard-worker-source",default="stages/stage32/generalization-bridge/run_br204_full178_bc_shard.cpp")
    ap.add_argument("--combiner",default="stages/stage32/generalization-bridge/combine_br204_bc_shards.py")
    ap.add_argument("--b",type=int,default=0)
    ap.add_argument("--d",type=int,default=8)
    ap.add_argument("--shard-count",type=int,default=16)
    ap.add_argument("--include-dir",action="append",default=[])
    a=ap.parse_args()
    req(a.shard_count==16,"retained preflight requires exactly 16 BC shards")
    direct_source=Path(a.direct_worker_source); shard_source=Path(a.shard_worker_source); combiner=Path(a.combiner)
    req(direct_source.is_file() and shard_source.is_file() and combiner.is_file(),"missing source/combiner")
    worker_blob=subprocess.check_output(["git","hash-object",str(direct_source)],text=True).strip()
    req(worker_blob=="0d5ee8e1013cab6120e957707a363e86b3c0d41e","audited generation1 worker blob drift")
    with tempfile.TemporaryDirectory() as td:
        root=Path(td); direct_exe=root/"direct-worker"; shard_exe=root/"shard-worker"; shards=root/"shards"; shards.mkdir()
        basecc=["g++","-O2","-std=c++20"]
        for inc in a.include_dir: basecc += ["-I",inc]
        run(basecc+[str(direct_source),"-o",str(direct_exe)])
        run(basecc+[str(shard_source),"-o",str(shard_exe)])
        direct=root/"direct.tsv"
        run([str(direct_exe),"--b",str(a.b),"--d-lo",str(a.d),"--d-hi",str(a.d),
             "--worker-blob",worker_blob,"--out",str(direct)])
        for i in range(a.shard_count):
            p=shards/f"br204-f-b{a.b}-d{a.d}-bc{i}of{a.shard_count}.tsv"
            run([str(shard_exe),"--b",str(a.b),"--d-lo",str(a.d),"--d-hi",str(a.d),
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
