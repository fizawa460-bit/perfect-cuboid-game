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

def run(cmd: list[str]) -> None:
    subprocess.run(cmd,check=True)

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--worker",required=True)
    ap.add_argument("--worker-blob",required=True)
    ap.add_argument("--parent-combiner",required=True)
    ap.add_argument("--base-combiner",required=True)
    ap.add_argument("--b",type=int,default=0)
    ap.add_argument("--d",type=int,default=8)
    a=ap.parse_args()
    with tempfile.TemporaryDirectory() as td:
        root=Path(td)
        direct=root/"direct"; fine=root/"fine"; rebuilt=root/"rebuilt"
        direct.mkdir(); fine.mkdir(); rebuilt.mkdir()
        for j in range(16):
            dp=direct/f"br204-f-b{a.b}-d{a.d}-bc{j}of16.tsv"
            run([a.worker,"--b",str(a.b),"--d-lo",str(a.d),"--d-hi",str(a.d),
                 "--out",str(dp),"--worker-blob",a.worker_blob,
                 "--bc-shard-index",str(j),"--bc-shard-count","16"])
            for k in range(4):
                idx=j+16*k
                fp=fine/f"br204-f-b{a.b}-d{a.d}-bc{idx}of64.tsv"
                run([a.worker,"--b",str(a.b),"--d-lo",str(a.d),"--d-hi",str(a.d),
                     "--out",str(fp),"--worker-blob",a.worker_blob,
                     "--bc-shard-index",str(idx),"--bc-shard-count","64"])
            rp=rebuilt/f"br204-f-b{a.b}-d{a.d}-bc{j}of16.tsv"
            run(["python",a.parent_combiner,"--input-dir",str(fine),
                 "--b",str(a.b),"--d",str(a.d),"--parent-shard-index",str(j),
                 "--parent-shard-count","16","--fine-shard-count","64",
                 "--worker-blob",a.worker_blob,"--out",str(rp)])
            req(dp.read_bytes()==rp.read_bytes(),f"parent shard byte mismatch j={j} direct={sha(dp)} rebuilt={sha(rp)}")
        direct_full=root/"direct-full.tsv"; rebuilt_full=root/"rebuilt-full.tsv"
        run(["python",a.base_combiner,"--input-dir",str(direct),"--b",str(a.b),"--d",str(a.d),
             "--shard-count","16","--worker-blob",a.worker_blob,"--out",str(direct_full)])
        run(["python",a.base_combiner,"--input-dir",str(rebuilt),"--b",str(a.b),"--d",str(a.d),
             "--shard-count","16","--worker-blob",a.worker_blob,"--out",str(rebuilt_full)])
        req(direct_full.read_bytes()==rebuilt_full.read_bytes(),"full canonical byte mismatch")
        print("PASS: all 16 direct BC shards equal exact unions of their four 64-way children")
        print("CANONICAL_SHA256="+sha(direct_full))

if __name__=="__main__":
    main()
