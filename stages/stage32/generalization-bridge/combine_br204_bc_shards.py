#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import io
import json
import re
import sys
import zlib
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

COMPACT_SCHEMA="STAGE32_BR204_G4_COMPACT_CHILD_CERT_V2"
COMPACT_CODEC="delta-varint-zlib-base64-v1"

def _deterministic_gzip(raw:bytes)->bytes:
    bio=io.BytesIO()
    with gzip.GzipFile(filename="",mode="wb",fileobj=bio,compresslevel=9,mtime=0) as z:
        z.write(raw)
    return bio.getvalue()

def _uvarint(n:int)->bytes:
    req(n>=0,"negative uvarint")
    out=bytearray()
    while n>=0x80:
        out.append((n&0x7f)|0x80); n>>=7
    out.append(n)
    return bytes(out)

def _zigzag(n:int)->int:
    return n*2 if n>=0 else (-n)*2-1

def _unzigzag(n:int)->int:
    return n//2 if n%2==0 else -(n//2)-1

def _read_uvarint(buf:bytes,pos:int)->tuple[int,int]:
    shift=0; out=0
    while True:
        req(pos<len(buf),"truncated varint")
        b=buf[pos]; pos+=1; out|=(b&0x7f)<<shift
        if b<0x80: return out,pos
        shift+=7
        req(shift<=126,"oversized varint")

def _encode_compact_records(records:list[tuple[int,int,int,int]])->bytes:
    out=bytearray(); out+=_uvarint(len(records))
    ps=pB=pc=pt=0
    for s,B,cap,tailv in records:
        out+=_uvarint(_zigzag(s-ps))
        out+=_uvarint(_zigzag(B-pB))
        out+=_uvarint(_zigzag(cap-pc))
        out+=_uvarint(_zigzag(tailv-pt))
        ps,pB,pc,pt=s,B,cap,tailv
    return bytes(out)

def _decode_compact_records(comp:bytes)->list[tuple[int,int,int,int]]:
    buf=zlib.decompress(comp); pos=0
    n,pos=_read_uvarint(buf,pos); out=[]
    ps=pB=pc=pt=0
    for _ in range(n):
        ds,pos=_read_uvarint(buf,pos); dB,pos=_read_uvarint(buf,pos)
        dc,pos=_read_uvarint(buf,pos); dt,pos=_read_uvarint(buf,pos)
        s=ps+_unzigzag(ds); B=pB+_unzigzag(dB)
        cap=pc+_unzigzag(dc); tailv=pt+_unzigzag(dt)
        req(s>=0 and B>0 and cap>=0 and 0<=tailv<=cap,"decoded record invariant")
        out.append((s,B,cap,tailv)); ps,pB,pc,pt=s,B,cap,tailv
    req(pos==len(buf),"trailing compact codec bytes")
    return out

def _compact_raw_from_cert(cert:dict)->bytes:
    req(cert["schema"]==COMPACT_SCHEMA,"compact certificate schema")
    req(cert["codec"]["name"]==COMPACT_CODEC,"compact codec")
    comp=base64.b64decode(cert["codec"]["payload_b64"],validate=True)
    req(len(comp)==cert["codec"]["compressed_bytes"],"compressed byte count")
    records=_decode_compact_records(comp)
    sm=cert["summary"]; req(len(records)==sm["record_count"],"record count")
    t=cert["target"]; part=cert["partition"]; src=cert["source"]
    lines=[
        "\t".join(map(str,["META",t["b"],t["d"],t["d"],sm["state_count"],sm["mass"],sm["tail_mass"],
                           src["worker_blob"],src["base_blob"],src["mu_sha256"],src["terminal_sha256"],
                           sm["evaluated_state_parts"]])),
        "\t".join(map(str,["PART","BC_MOD",part["child_index"],part["child_count"]]))
    ]
    for s,B,cap,tailv in records: lines.append(f"K\t{s}\t{B}\t{cap}")
    for s,B,cap,tailv in records: lines.append(f"M\t{s}\t{B}\t{cap}\t{tailv}")
    lines.append("TAIL\t"+"\t".join(str(x) for x in sm["tail_record"]))
    lines.append("SUM\t"+"\t".join(str(x) for x in sm["sum_record"]))
    raw=("\n".join(lines)+"\n").encode()
    req(hashlib.sha256(raw).hexdigest()==cert["commitments"]["canonical_payload_sha256"],"compact raw SHA")
    return raw

def compact_child(input_path:Path,output_path:Path,worker_blob:str,plan_blob:str,runkey_blob:str)->dict:
    req(len(worker_blob)==len(plan_blob)==len(runkey_blob)==40,"compact source-lock length")
    source_bytes=input_path.read_bytes()
    raw=gzip.decompress(source_bytes) if source_bytes[:2]==b"\x1f\x8b" else source_bytes
    tmp=input_path
    x=parse(tmp,worker_blob)
    keys=sorted(x["k8"])
    req(keys==sorted(x["mu"]),"compact K/M key mismatch")
    records=[]
    for key in keys:
        cap=x["k8"][key]; mcap,tailv=x["mu"][key]
        req(cap==mcap and 0<=tailv<=cap,"compact K/M cap mismatch")
        records.append((key[0],key[1],cap,tailv))
    packed=_encode_compact_records(records)
    comp=zlib.compress(packed,9)
    cert={
      "schema":COMPACT_SCHEMA,
      "status":"EXACT_COMPACT_CHILD_ZERO_CREDIT",
      "target":{"b":x["b"],"d":x["d"]},
      "partition":{"kind":"BC"+str(x["count"]),"child_index":x["idx"],"child_count":x["count"]},
      "source":{"worker_blob":x["worker_blob"],"base_blob":x["base_blob"],"mu_sha256":x["mu_sha"],
                "terminal_sha256":x["terminal_sha"],"plan_blob":plan_blob,"runkey_blob":runkey_blob},
      "summary":{"state_count":x["states"],"mass":str(x["mass"]),"tail_mass":str(x["tail_mass"]),
                 "evaluated_state_parts":str(x["eval_parts"]),"record_count":len(records),
                 "tail_record":[str(v) for v in x["tail"]],"sum_record":[str(sum(x["k8"].values())),
                 str(sum(v[0] for v in x["mu"].values())),str(sum(v[1] for v in x["mu"].values()))]},
      "commitments":{"canonical_payload_sha256":hashlib.sha256(raw).hexdigest(),
                     "deterministic_gzip_sha256":hashlib.sha256(_deterministic_gzip(raw)).hexdigest()},
      "codec":{"name":COMPACT_CODEC,"uncompressed_bytes":len(packed),"compressed_bytes":len(comp),
               "payload_b64":base64.b64encode(comp).decode()},
      "credit":False
    }
    if source_bytes[:2]==b"\x1f\x8b":
        req(hashlib.sha256(source_bytes).hexdigest()==cert["commitments"]["deterministic_gzip_sha256"],
            "input gzip is not deterministic canonical gzip")
    output_path.parent.mkdir(parents=True,exist_ok=True)
    output_path.write_text(json.dumps(cert,sort_keys=True,separators=(",",":"))+"\n")
    req(output_path.stat().st_size<=65536,"compact child exceeds 65536-byte cap")
    req(_compact_raw_from_cert(cert)==raw,"compact roundtrip mismatch")
    return cert

def verify_compact_child(cert_path:Path,output_raw:Path|None,expected_worker_blob:str|None,
                         expected_plan_blob:str|None,expected_runkey_blob:str|None)->dict:
    cert=json.loads(cert_path.read_text())
    if expected_worker_blob is not None: req(cert["source"]["worker_blob"]==expected_worker_blob,"compact worker lock")
    if expected_plan_blob is not None: req(cert["source"]["plan_blob"]==expected_plan_blob,"compact plan lock")
    if expected_runkey_blob is not None: req(cert["source"]["runkey_blob"]==expected_runkey_blob,"compact runkey lock")
    raw=_compact_raw_from_cert(cert)
    req(hashlib.sha256(_deterministic_gzip(raw)).hexdigest()==cert["commitments"]["deterministic_gzip_sha256"],
        "compact deterministic gzip SHA")
    if output_raw is not None:
        output_raw.parent.mkdir(parents=True,exist_ok=True); output_raw.write_bytes(raw)
    return {"status":"PASS","certificate_bytes":cert_path.stat().st_size,"raw_bytes":len(raw),
            "canonical_payload_sha256":cert["commitments"]["canonical_payload_sha256"],
            "deterministic_gzip_sha256":cert["commitments"]["deterministic_gzip_sha256"],
            "target":cert["target"],"partition":cert["partition"]}

def compact_cli(argv:list[str])->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",required=True); ap.add_argument("--output",required=True)
    ap.add_argument("--worker-blob",required=True); ap.add_argument("--plan-blob",required=True)
    ap.add_argument("--runkey-blob",required=True)
    a=ap.parse_args(argv)
    c=compact_child(Path(a.input),Path(a.output),a.worker_blob,a.plan_blob,a.runkey_blob)
    print(json.dumps({"status":"PASS","certificate_bytes":Path(a.output).stat().st_size,
                      "raw_sha256":c["commitments"]["canonical_payload_sha256"],
                      "gzip_sha256":c["commitments"]["deterministic_gzip_sha256"]},sort_keys=True))

def compact_verify_cli(argv:list[str])->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--certificate",required=True); ap.add_argument("--output-raw")
    ap.add_argument("--expected-worker-blob"); ap.add_argument("--expected-plan-blob"); ap.add_argument("--expected-runkey-blob")
    a=ap.parse_args(argv)
    print(json.dumps(verify_compact_child(Path(a.certificate),Path(a.output_raw) if a.output_raw else None,
          a.expected_worker_blob,a.expected_plan_blob,a.expected_runkey_blob),sort_keys=True))

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--input-dir",action="append",default=[])
    ap.add_argument("--validate-path")
    ap.add_argument("--b",type=int,required=True)
    ap.add_argument("--d",type=int,required=True)
    ap.add_argument("--shard-count",type=int,default=16)
    ap.add_argument("--worker-blob",required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    req(a.shard_count>1,"shard-count must exceed one")
    if a.validate_path:
        x=parse(Path(a.validate_path),a.worker_blob)
        req(x["b"]==a.b and x["d"]==a.d,"validated shard b/d mismatch")
        req(x["count"]==a.shard_count,"validated shard count mismatch")
        print(json.dumps({"status":"PASS","b":x["b"],"d":x["d"],"idx":x["idx"],
                          "count":x["count"],"sha256":x["sha256"]},sort_keys=True))
        return
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
    if len(sys.argv)>1 and sys.argv[1]=="compact-child": compact_cli(sys.argv[2:])
    elif len(sys.argv)>1 and sys.argv[1]=="verify-compact-child": compact_verify_cli(sys.argv[2:])
    else: main()
