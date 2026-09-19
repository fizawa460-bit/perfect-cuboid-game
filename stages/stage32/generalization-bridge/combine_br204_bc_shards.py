#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
from pathlib import Path

BASE_BLOB="b7fc7e0c6c889c92cb152d4e8b54d05d2b71a5d1"
NAME_RE=re.compile(r"^br204-f-b(\d+)-d(\d+)-bc(\d+)of(\d+)\.tsv(?:\.gz)?$")

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: "+msg)

def raw_bytes(p: Path) -> bytes:
    x=p.read_bytes()
    return gzip.decompress(x) if p.suffix==".gz" else x

def parse(p: Path, worker_blob: str) -> dict:
    raw=raw_bytes(p)
    lines=raw.decode().splitlines()
    req(lines and lines[0].startswith("META\t"),f"missing META {p}")
    m=lines[0].split("\t")
    req(len(m)==12,f"META field count {p}")
    _,b,dlo,dhi,states,mass,tail_mass,wblob,base,mu_sha,terminal_sha,eval_parts=m
    b,dlo,dhi=int(b),int(dlo),int(dhi)
    req(dlo==dhi,f"finer shard must be single-d {p}")
    req(wblob==worker_blob,f"worker blob drift {p}")
    req(base==BASE_BLOB,f"base blob drift {p}")
    req(len(lines)>=2 and lines[1].startswith("PART\t"),f"missing PART {p}")
    q=lines[1].split("\t")
    req(len(q)==4 and q[1]=="BC_MOD",f"bad PART {p}")
    idx,count=int(q[2]),int(q[3])
    req(count>1 and 0<=idx<count,f"bad BC shard identity {p}")
    k8={}; mu={}; tail=None; sums=None
    for line in lines[2:]:
        z=line.split("\t")
        if z[0]=="K":
            req(len(z)==4,f"bad K {p}")
            key=(int(z[1]),int(z[2])); req(key not in k8,f"duplicate K {p}")
            k8[key]=int(z[3])
        elif z[0]=="M":
            req(len(z)==5,f"bad M {p}")
            key=(int(z[1]),int(z[2])); req(key not in mu,f"duplicate M {p}")
            cap,t=int(z[3]),int(z[4]); req(0<=t<=cap,f"bad M tail {p}")
            mu[key]=(cap,t)
        elif z[0]=="TAIL":
            req(len(z)==13 and tail is None,f"bad TAIL {p}")
            tail=tuple(int(x) for x in z[1:])
        elif z[0]=="SUM":
            req(len(z)==4 and sums is None,f"bad SUM {p}")
            sums=tuple(int(x) for x in z[1:])
        else:
            raise SystemExit(f"FAIL: unknown record {z[0]} {p}")
    req(tail is not None and sums is not None,f"missing TAIL/SUM {p}")
    req(sum(k8.values())==sums[0],f"K sum drift {p}")
    req(sum(v[0] for v in mu.values())==sums[1],f"M sum drift {p}")
    req(sum(v[1] for v in mu.values())==sums[2],f"tail sum drift {p}")
    req(tail[0]+tail[1]==int(states),f"state partition drift {p}")
    req(tail[2]==int(tail_mass),f"tail assignment drift {p}")
    return {
        "b":b,"d":dlo,"idx":idx,"count":count,"states":int(states),"mass":int(mass),
        "tail_mass":int(tail_mass),"worker_blob":wblob,"base_blob":base,"mu_sha":mu_sha,
        "terminal_sha":terminal_sha,"eval_parts":int(eval_parts),"k8":k8,"mu":mu,
        "tail":tail,"sha256":hashlib.sha256(raw).hexdigest()
    }

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--input-dir",action="append",default=[])
    ap.add_argument("--b",type=int,required=True)
    ap.add_argument("--d",type=int,required=True)
    ap.add_argument("--shard-count",type=int,default=16)
    ap.add_argument("--worker-blob",required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    req(a.shard_count>1,"shard-count must exceed one")
    found={}
    for root in map(Path,a.input_dir):
        if not root.exists(): continue
        for p in sorted(root.rglob("br204-f-b*-d*-bc*of*.tsv*")):
            m=NAME_RE.match(p.name)
            if not m: continue
            b,d,idx,count=map(int,m.groups())
            if (b,d,count)!=(a.b,a.d,a.shard_count): continue
            x=parse(p,a.worker_blob)
            req((x["b"],x["d"],x["idx"],x["count"])==(b,d,idx,count),f"filename/payload drift {p}")
            if idx in found:
                req(found[idx]["sha256"]==x["sha256"],f"conflicting duplicate shard {idx}")
            else:
                found[idx]=x
    req(set(found)==set(range(a.shard_count)),
        f"BC shard coverage mismatch missing={sorted(set(range(a.shard_count))-set(found))} extra={sorted(set(found)-set(range(a.shard_count)))}")
    xs=[found[i] for i in range(a.shard_count)]
    sig={(x["base_blob"],x["mu_sha"],x["terminal_sha"],x["worker_blob"]) for x in xs}
    req(len(sig)==1,"source/static identity drift across BC shards")
    k8={}; mu={}; dyn=[0]*9; eval_parts=0
    states=mass=tail_mass=0
    for x in xs:
        states+=x["states"]; mass+=x["mass"]; tail_mass+=x["tail_mass"]; eval_parts+=x["eval_parts"]
        for key,cap in x["k8"].items(): k8[key]=k8.get(key,0)+cap
        for key,(cap,t) in x["mu"].items():
            old=mu.get(key,(0,0)); mu[key]=(old[0]+cap,old[1]+t)
        for i,v in enumerate(x["tail"][3:]): dyn[i]+=v
    for key,(cap,t) in mu.items():
        req(key in k8 and cap<=k8[key],f"combined mu exceeds K8 {key}")
        req(0<=t<=cap,f"combined tail exceeds mu {key}")
    base,mu_sha,terminal_sha,wblob=next(iter(sig))
    out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True)
    with out.open("w") as f:
        f.write("\t".join(map(str,["META",a.b,a.d,a.d,states,mass,tail_mass,wblob,base,mu_sha,terminal_sha,eval_parts]))+"\n")
        for (s,B),cap in sorted(k8.items()): f.write(f"K\t{s}\t{B}\t{cap}\n")
        for (s,B),(cap,t) in sorted(mu.items()): f.write(f"M\t{s}\t{B}\t{cap}\t{t}\n")
        f.write("TAIL\t"+"\t".join(map(str,[sum(x["tail"][0] for x in xs),sum(x["tail"][1] for x in xs),tail_mass]+dyn))+"\n")
        f.write(f"SUM\t{sum(k8.values())}\t{sum(v[0] for v in mu.values())}\t{sum(v[1] for v in mu.values())}\n")
    print(json.dumps({"status":"PASS","b":a.b,"d":a.d,"shard_count":a.shard_count,
                      "states":states,"mass":mass,"output":str(out)},sort_keys=True))

if __name__=="__main__":
    main()
