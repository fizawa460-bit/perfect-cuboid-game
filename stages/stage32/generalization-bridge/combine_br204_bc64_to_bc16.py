#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import json
import re
from pathlib import Path

import combine_br204_bc_shards as base

NAME_RE = re.compile(r"^br204-f-b(\d+)-d(\d+)-bc(\d+)of(\d+)\.tsv(?:\.gz)?$")

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def write_parent(xs: list[dict], *, b: int, d: int, parent_idx: int, parent_count: int, out: Path) -> None:
    sig={(x["base_blob"],x["mu_sha"],x["terminal_sha"],x["worker_blob"]) for x in xs}
    req(len(sig)==1,"source/static identity drift across fine shards")
    k8={}; mu={}; dyn=[0]*9
    states=mass=tail_mass=eval_parts=0
    for x in xs:
        states+=x["states"]; mass+=x["mass"]; tail_mass+=x["tail_mass"]; eval_parts+=x["eval_parts"]
        for key,cap in x["k8"].items():
            k8[key]=k8.get(key,0)+cap
        for key,(cap,t) in x["mu"].items():
            old=mu.get(key,(0,0)); mu[key]=(old[0]+cap,old[1]+t)
        for i,v in enumerate(x["tail"][3:]):
            dyn[i]+=v
    for key,(cap,t) in mu.items():
        req(key in k8 and cap<=k8[key],f"combined mu exceeds K8 {key}")
        req(0<=t<=cap,f"combined tail exceeds mu {key}")
    base_blob,mu_sha,terminal_sha,wblob=next(iter(sig))
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open("w") as f:
        f.write("\t".join(map(str,["META",b,d,d,states,mass,tail_mass,wblob,base_blob,mu_sha,terminal_sha,eval_parts]))+"\n")
        f.write(f"PART\tBC_MOD\t{parent_idx}\t{parent_count}\n")
        for (s,B),cap in sorted(k8.items()):
            f.write(f"K\t{s}\t{B}\t{cap}\n")
        for (s,B),(cap,t) in sorted(mu.items()):
            f.write(f"M\t{s}\t{B}\t{cap}\t{t}\n")
        f.write("TAIL\t"+"\t".join(map(str,[sum(x["tail"][0] for x in xs),sum(x["tail"][1] for x in xs),tail_mass]+dyn))+"\n")
        f.write(f"SUM\t{sum(k8.values())}\t{sum(v[0] for v in mu.values())}\t{sum(v[1] for v in mu.values())}\n")

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--input-dir",action="append",default=[])
    ap.add_argument("--b",type=int,required=True)
    ap.add_argument("--d",type=int,required=True)
    ap.add_argument("--parent-shard-index",type=int,required=True)
    ap.add_argument("--parent-shard-count",type=int,default=16)
    ap.add_argument("--fine-shard-count",type=int,default=64)
    ap.add_argument("--worker-blob",required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    req(a.parent_shard_count>1,"parent shard count")
    req(a.fine_shard_count>a.parent_shard_count and a.fine_shard_count%a.parent_shard_count==0,"fine/parent count relation")
    req(0<=a.parent_shard_index<a.parent_shard_count,"parent shard index")
    expected={a.parent_shard_index+k*a.parent_shard_count for k in range(a.fine_shard_count//a.parent_shard_count)}
    found={}
    for root in map(Path,a.input_dir):
        if not root.exists():
            continue
        for p in sorted(root.rglob("br204-f-b*-d*-bc*of*.tsv*")):
            m=NAME_RE.match(p.name)
            if not m:
                continue
            b,d,idx,count=map(int,m.groups())
            if (b,d,count)!=(a.b,a.d,a.fine_shard_count) or idx not in expected:
                continue
            x=base.parse(p,a.worker_blob)
            req((x["b"],x["d"],x["idx"],x["count"])==(b,d,idx,count),f"filename/payload drift {p}")
            if idx in found:
                req(found[idx]["sha256"]==x["sha256"],f"conflicting duplicate fine shard {idx}")
            else:
                found[idx]=x
    req(set(found)==expected,f"fine coverage mismatch missing={sorted(expected-set(found))} extra={sorted(set(found)-expected)}")
    xs=[found[i] for i in sorted(expected)]
    out=Path(a.out)
    write_parent(xs,b=a.b,d=a.d,parent_idx=a.parent_shard_index,parent_count=a.parent_shard_count,out=out)
    parent=base.parse(out,a.worker_blob)
    req(parent["idx"]==a.parent_shard_index and parent["count"]==a.parent_shard_count,"parent identity drift")
    print(json.dumps({
        "status":"PASS","b":a.b,"d":a.d,
        "parent_shard_index":a.parent_shard_index,
        "parent_shard_count":a.parent_shard_count,
        "fine_shard_count":a.fine_shard_count,
        "fine_indices":sorted(expected),
        "states":parent["states"],"mass":parent["mass"],
        "output":str(out)
    },sort_keys=True))

if __name__=="__main__":
    main()
