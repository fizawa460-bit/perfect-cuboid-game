#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
import shutil
from pathlib import Path

D_BANDS=((8,54),(56,100),(102,146),(148,192))
BASE_BLOB="b7fc7e0c6c889c92cb152d4e8b54d05d2b71a5d1"
SLICE_RE=re.compile(r"^br204-s-b(\d+)-d(\d+)\.tsv\.gz$")

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: "+msg)

def raw_bytes(path: Path) -> bytes:
    data=path.read_bytes()
    return gzip.decompress(data) if path.suffix==".gz" else data

def parse(path: Path, worker_blob: str, require_slice: bool=True) -> dict:
    raw=raw_bytes(path)
    lines=raw.decode("utf-8").splitlines()
    req(lines and lines[0].startswith("META\t"), f"missing META {path}")
    m=lines[0].split("\t")
    req(len(m)==12, f"META field count {path}")
    _,b,d_lo,d_hi,states,mass,tail_mass,wblob,base_blob,mu_sha,terminal_sha,eval_parts=m
    b,d_lo,d_hi=int(b),int(d_lo),int(d_hi)
    req(0<=b<=96, f"b outside range {path}")
    req(any(lo<=d_lo<=d_hi<=hi for lo,hi in D_BANDS), f"d range outside approved band {path}")
    req(d_lo%2==0 and d_hi%2==0, f"odd d endpoint {path}")
    if require_slice:
        req(d_lo==d_hi, f"not a single-d slice {path}")
        req(d_lo>=max(8,2*b), f"inadmissible single-d slice {path}")
    req(wblob==worker_blob, f"worker blob drift {path}")
    req(base_blob==BASE_BLOB, f"base blob drift {path}")
    k8={}
    mu={}
    tail_line=None
    sum_line=None
    for line in lines[1:]:
        q=line.split("\t")
        if q[0]=="K":
            req(len(q)==4, f"K field count {path}")
            key=(int(q[1]),int(q[2])); req(key not in k8, f"duplicate K {path}")
            k8[key]=int(q[3])
        elif q[0]=="M":
            req(len(q)==5, f"M field count {path}")
            key=(int(q[1]),int(q[2])); req(key not in mu, f"duplicate M {path}")
            cap,tail=int(q[3]),int(q[4]); req(0<=tail<=cap, f"bad mu tail {path}")
            mu[key]=(cap,tail)
        elif q[0]=="TAIL":
            req(len(q)==13 and tail_line is None, f"bad TAIL {path}")
            tail_line=tuple(int(x) for x in q[1:])
        elif q[0]=="SUM":
            req(len(q)==4 and sum_line is None, f"bad SUM {path}")
            sum_line=tuple(int(x) for x in q[1:])
        else:
            raise SystemExit(f"FAIL: unknown record {q[0]} {path}")
    req(tail_line is not None and sum_line is not None, f"missing TAIL/SUM {path}")
    req(sum(k8.values())==sum_line[0], f"K SUM drift {path}")
    req(sum(v[0] for v in mu.values())==sum_line[1], f"M SUM drift {path}")
    req(sum(v[1] for v in mu.values())==sum_line[2], f"tail SUM drift {path}")
    for key,(cap,_) in mu.items():
        req(key in k8 and cap<=k8[key], f"mu exceeds K8 {path}")
    states_i,mass_i,tail_mass_i=int(states),int(mass),int(tail_mass)
    req(tail_line[0]+tail_line[1]==states_i, f"state partition drift {path}")
    req(tail_line[2]==tail_mass_i and 0<=tail_mass_i<=mass_i, f"tail mass drift {path}")
    req(tail_line[10]<=tail_line[8] and tail_line[11]<=tail_line[9], f"mu tail capacity exceeds K8 {path}")
    return {
        "b":b,"d_lo":d_lo,"d_hi":d_hi,"states":states_i,"mass":mass_i,"tail_mass":tail_mass_i,
        "worker_blob":wblob,"base_blob":base_blob,"mu_sha":mu_sha,"terminal_sha":terminal_sha,
        "eval_parts":int(eval_parts),"k8":k8,"mu":mu,"tail":tail_line,"sum":sum_line,
        "sha256":hashlib.sha256(raw).hexdigest(),"bytes":len(raw),"source":str(path)
    }

def expected_ds(b:int, band_lo:int, band_hi:int) -> list[int]:
    req((band_lo,band_hi) in D_BANDS, "unapproved band")
    return [d for d in range(band_lo,band_hi+1,2) if d>=max(8,2*b)]

def gzip_deterministic(src: Path, dst: Path) -> None:
    with src.open("rb") as inp, dst.open("wb") as out:
        with gzip.GzipFile(filename="",mode="wb",fileobj=out,compresslevel=9,mtime=0) as gz:
            shutil.copyfileobj(inp,gz)

def cmd_validate(a) -> None:
    d=parse(Path(a.path),a.worker_blob,True)
    req(d["b"]==a.b and d["d_lo"]==a.d and d["d_hi"]==a.d, "slice identity mismatch")
    print(json.dumps({"status":"PASS","b":a.b,"d":a.d,"sha256":d["sha256"],"bytes":d["bytes"]},sort_keys=True))

def cmd_bundle(a) -> None:
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    chosen={}
    discovered=0
    for root in map(Path,a.input_dir):
        if not root.exists(): continue
        for p in sorted(root.rglob("br204-s-b*-d*.tsv.gz")):
            discovered+=1
            m=SLICE_RE.match(p.name); req(m is not None, f"bad slice filename {p}")
            b,d=map(int,m.groups())
            x=parse(p,a.worker_blob,True)
            req((x["b"],x["d_lo"],x["d_hi"])==(b,d,d), f"filename/content drift {p}")
            key=(b,d)
            if key in chosen:
                req(chosen[key]["sha256"]==x["sha256"], f"conflicting duplicate slice {key}")
            else:
                chosen[key]=x
                shutil.copy2(p,out/p.name)
    manifest={
        "schema":"STAGE32_BR204_PARTIAL_SLICE_BUNDLE_V1",
        "discovered_slice_file_count":discovered,
        "validated_unique_slice_count":len(chosen),
        "slices":[{"b":b,"d":d,"sha256":chosen[(b,d)]["sha256"],"bytes":chosen[(b,d)]["bytes"]} for b,d in sorted(chosen)],
    }
    Path(a.manifest).write_text(json.dumps(manifest,sort_keys=True,indent=2)+"\n")
    print(json.dumps(manifest,sort_keys=True))

def cmd_combine(a) -> None:
    b,lo,hi=a.b,a.band_lo,a.band_hi
    ds=expected_ds(b,lo,hi); req(ds, "band has no admissible d")
    found={}
    for root in map(Path,a.input_dir):
        if not root.exists(): continue
        for d in ds:
            name=f"br204-s-b{b}-d{d}.tsv.gz"
            for p in root.rglob(name):
                x=parse(p,a.worker_blob,True)
                req((x["b"],x["d_lo"],x["d_hi"])==(b,d,d), f"slice identity drift {p}")
                if d in found:
                    req(found[d]["sha256"]==x["sha256"], f"conflicting duplicate d={d}")
                else: found[d]=x
    req(set(found)==set(ds), f"slice coverage mismatch missing={sorted(set(ds)-set(found))}")
    first=found[ds[0]]
    static=(first["states"],first["mass"],first["tail_mass"],first["base_blob"],first["mu_sha"],first["terminal_sha"],first["tail"][:3])
    k8={}; mu={}; dyn=[0]*9; eval_parts=0
    for d in ds:
        x=found[d]
        cur=(x["states"],x["mass"],x["tail_mass"],x["base_blob"],x["mu_sha"],x["terminal_sha"],x["tail"][:3])
        req(cur==static, f"static metadata drift d={d}")
        eval_parts+=x["eval_parts"]
        for key,cap in x["k8"].items(): k8[key]=k8.get(key,0)+cap
        for key,(cap,tail) in x["mu"].items():
            old=mu.get(key,(0,0)); mu[key]=(old[0]+cap,old[1]+tail)
        for i,v in enumerate(x["tail"][3:]): dyn[i]+=v
    for key,(cap,_) in mu.items(): req(key in k8 and cap<=k8[key], f"combined mu exceeds K8 {key}")
    out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True)
    with out.open("w",encoding="utf-8") as f:
        f.write("\t".join(map(str,["META",b,lo,hi,first["states"],first["mass"],first["tail_mass"],a.worker_blob,first["base_blob"],first["mu_sha"],first["terminal_sha"],eval_parts]))+"\n")
        for (s,B),cap in sorted(k8.items()): f.write(f"K\t{s}\t{B}\t{cap}\n")
        for (s,B),(cap,tail) in sorted(mu.items()): f.write(f"M\t{s}\t{B}\t{cap}\t{tail}\n")
        f.write("TAIL\t"+"\t".join(map(str,list(first["tail"][:3])+dyn))+"\n")
        f.write(f"SUM\t{sum(k8.values())}\t{sum(v[0] for v in mu.values())}\t{sum(v[1] for v in mu.values())}\n")
    print(json.dumps({"status":"COMPLETE","b":b,"band":[lo,hi],"slice_count":len(ds),"out":str(out)},sort_keys=True))

def main() -> None:
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest="cmd",required=True)
    p=sp.add_parser("validate-slice"); p.add_argument("--path",required=True); p.add_argument("--b",type=int,required=True); p.add_argument("--d",type=int,required=True); p.add_argument("--worker-blob",required=True); p.set_defaults(fn=cmd_validate)
    p=sp.add_parser("bundle"); p.add_argument("--input-dir",action="append",default=[]); p.add_argument("--out-dir",required=True); p.add_argument("--manifest",required=True); p.add_argument("--worker-blob",required=True); p.set_defaults(fn=cmd_bundle)
    p=sp.add_parser("combine"); p.add_argument("--input-dir",action="append",default=[]); p.add_argument("--b",type=int,required=True); p.add_argument("--band-lo",type=int,required=True); p.add_argument("--band-hi",type=int,required=True); p.add_argument("--worker-blob",required=True); p.add_argument("--out",required=True); p.set_defaults(fn=cmd_combine)
    p=sp.add_parser("self-test"); p.set_defaults(fn=lambda a: print(json.dumps({"status":"PASS","expected_single_d_slices":sum(len(expected_ds(b,lo,hi)) for b in range(97) for lo,hi in D_BANDS if hi>=max(8,2*b))},sort_keys=True)))
    a=ap.parse_args(); a.fn(a)

if __name__=="__main__": main()
