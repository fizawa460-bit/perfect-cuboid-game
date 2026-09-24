#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from combine_br204_bc_shards import parse, req

def write_parent(out:Path,a,xs:list[dict])->None:
    sig={(x["base_blob"],x["mu_sha"],x["terminal_sha"],x["worker_blob"]) for x in xs}
    req(len(sig)==1,"source/static identity drift across child shards")
    k8={}; mu={}; dyn=[0]*9
    states=mass=tail_mass=eval_parts=0
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
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open("w") as f:
        f.write("\t".join(map(str,["META",a.b,a.d,a.d,states,mass,tail_mass,wblob,base,mu_sha,terminal_sha,eval_parts]))+"\n")
        f.write(f"PART\tBC_MOD\t{a.parent_index}\t{a.parent_count}\n")
        for (s,B),cap in sorted(k8.items()): f.write(f"K\t{s}\t{B}\t{cap}\n")
        for (s,B),(cap,t) in sorted(mu.items()): f.write(f"M\t{s}\t{B}\t{cap}\t{t}\n")
        f.write("TAIL\t"+"\t".join(map(str,[sum(x["tail"][0] for x in xs),sum(x["tail"][1] for x in xs),tail_mass]+dyn))+"\n")
        f.write(f"SUM\t{sum(k8.values())}\t{sum(v[0] for v in mu.values())}\t{sum(v[1] for v in mu.values())}\n")

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--input-dir",action="append",default=[])
    ap.add_argument("--b",type=int,required=True)
    ap.add_argument("--d",type=int,required=True)
    ap.add_argument("--parent-index",type=int,required=True)
    ap.add_argument("--parent-count",type=int,default=16)
    ap.add_argument("--child-count",type=int,default=64)
    ap.add_argument("--worker-blob",required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    req(a.parent_count==16,"retained parent partition must be BC16")
    req(a.child_count==64,"generation3 child partition must be BC64")
    req(0<=a.parent_index<a.parent_count,"bad parent index")
    req(a.child_count%a.parent_count==0,"child/parent divisibility")
    expected=list(range(a.parent_index,a.child_count,a.parent_count))
    req(len(expected)==4,"expected four BC64 children per BC16 parent")
    found={}
    for root in map(Path,a.input_dir):
        if not root.exists(): continue
        for p in sorted(root.rglob(f"br204-f-b{a.b}-d{a.d}-bc*of{a.child_count}.tsv*")):
            x=parse(p,a.worker_blob)
            if x["b"]!=a.b or x["d"]!=a.d or x["count"]!=a.child_count or x["idx"] not in expected:
                continue
            i=x["idx"]
            if i in found:
                req(found[i]["sha256"]==x["sha256"],f"conflicting duplicate child {i}")
            else:
                found[i]=x
    req(set(found)==set(expected),f"child coverage mismatch missing={sorted(set(expected)-set(found))}")
    xs=[found[i] for i in expected]
    write_parent(Path(a.out),a,xs)
    parent=parse(Path(a.out),a.worker_blob)
    req((parent["b"],parent["d"],parent["idx"],parent["count"])==(a.b,a.d,a.parent_index,a.parent_count),"synthetic parent identity")
    print(f"PASS BC64->BC16 parent b={a.b} d={a.d} parent={a.parent_index} children={expected} states={parent['states']} mass={parent['mass']}")

if __name__=="__main__":
    main()
