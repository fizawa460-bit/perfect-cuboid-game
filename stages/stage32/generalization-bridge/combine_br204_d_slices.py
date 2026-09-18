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
STATE_RE=re.compile(r"^br204-partial-state-b(\d+)-d(\d+)-(\d+)\.json$")

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: "+msg)

def raw_bytes(path: Path) -> bytes:
    data=path.read_bytes()
    return gzip.decompress(data) if path.suffix==".gz" else data

def gzip_deterministic(src: Path, dst: Path) -> None:
    with src.open("rb") as inp, dst.open("wb") as out:
        with gzip.GzipFile(filename="",mode="wb",fileobj=out,compresslevel=9,mtime=0) as gz:
            shutil.copyfileobj(inp,gz)

def parse_payload(path: Path, worker_blob: str) -> dict:
    raw=raw_bytes(path)
    lines=raw.decode("utf-8").splitlines()
    req(lines and lines[0].startswith("META\t"), f"missing META {path}")
    m=lines[0].split("\t"); req(len(m)==12, f"META field count {path}")
    _,b,d_lo,d_hi,states,mass,tail_mass,wblob,base_blob,mu_sha,terminal_sha,eval_parts=m
    b,d_lo,d_hi=int(b),int(d_lo),int(d_hi)
    req(0<=b<=96, f"b outside range {path}")
    req(any(lo<=d_lo<=d_hi<=hi for lo,hi in D_BANDS), f"d range outside approved band {path}")
    req(d_lo%2==0 and d_hi%2==0, f"odd d endpoint {path}")
    req(wblob==worker_blob, f"worker blob drift {path}")
    req(base_blob==BASE_BLOB, f"base blob drift {path}")
    k8={}; mu={}; tail_line=None; sum_line=None
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
    for key,(cap,_) in mu.items(): req(key in k8 and cap<=k8[key], f"mu exceeds K8 {path}")
    states_i,mass_i,tail_mass_i=int(states),int(mass),int(tail_mass)
    req(tail_line[0]+tail_line[1]==states_i, f"state partition drift {path}")
    req(tail_line[2]==tail_mass_i and 0<=tail_mass_i<=mass_i, f"tail mass drift {path}")
    req(0<=tail_line[6]<=tail_line[4] and 0<=tail_line[7]<=tail_line[5], f"mu raw objective exceeds K8 {path}")
    req(0<=tail_line[10]<=tail_line[8] and 0<=tail_line[11]<=tail_line[9], f"mu capacity exceeds K8 {path}")
    return {
        "b":b,"d_lo":d_lo,"d_hi":d_hi,"states":states_i,"mass":mass_i,"tail_mass":tail_mass_i,
        "worker_blob":wblob,"base_blob":base_blob,"mu_sha":mu_sha,"terminal_sha":terminal_sha,
        "eval_parts":int(eval_parts),"k8":k8,"mu":mu,"tail":tail_line,"sum":sum_line,
        "sha256":hashlib.sha256(raw).hexdigest(),"bytes":len(raw),"source":str(path)
    }

def expected_ds(b:int, lo:int, hi:int) -> list[int]:
    req((lo,hi) in D_BANDS, "unapproved band")
    return [d for d in range(lo,hi+1,2) if d>=max(8,2*b)]

def write_aggregate(records:list[dict], b:int, lo:int, hi:int, worker_blob:str, out:Path) -> dict:
    req(records, "no records to aggregate")
    first=records[0]
    static=(first["states"],first["mass"],first["tail_mass"],first["base_blob"],first["mu_sha"],first["terminal_sha"],first["tail"][:3])
    k8={}; mu={}; dyn=[0]*9; eval_parts=0
    for x in records:
        cur=(x["states"],x["mass"],x["tail_mass"],x["base_blob"],x["mu_sha"],x["terminal_sha"],x["tail"][:3])
        req(cur==static, "static metadata drift across rollup")
        eval_parts+=x["eval_parts"]
        for key,cap in x["k8"].items(): k8[key]=k8.get(key,0)+cap
        for key,(cap,tail) in x["mu"].items():
            old=mu.get(key,(0,0)); mu[key]=(old[0]+cap,old[1]+tail)
        for i,v in enumerate(x["tail"][3:]): dyn[i]+=v
    for key,(cap,_) in mu.items(): req(key in k8 and cap<=k8[key], f"combined mu exceeds K8 {key}")
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open("w",encoding="utf-8") as f:
        f.write("\t".join(map(str,["META",b,lo,hi,first["states"],first["mass"],first["tail_mass"],worker_blob,first["base_blob"],first["mu_sha"],first["terminal_sha"],eval_parts]))+"\n")
        for (s,B),cap in sorted(k8.items()): f.write(f"K\t{s}\t{B}\t{cap}\n")
        for (s,B),(cap,tail) in sorted(mu.items()): f.write(f"M\t{s}\t{B}\t{cap}\t{tail}\n")
        f.write("TAIL\t"+"\t".join(map(str,list(first["tail"][:3])+dyn))+"\n")
        f.write(f"SUM\t{sum(k8.values())}\t{sum(v[0] for v in mu.values())}\t{sum(v[1] for v in mu.values())}\n")
    return parse_payload(out,worker_blob)

def partial_names(b:int,lo:int,hi:int) -> tuple[str,str]:
    return (f"br204-partial-b{b}-d{lo}-{hi}.tsv.gz",f"br204-partial-state-b{b}-d{lo}-{hi}.json")

def find_partial(input_dirs:list[Path], b:int, lo:int, hi:int, worker_blob:str) -> tuple[dict,dict,Path,Path] | None:
    payload_name,state_name=partial_names(b,lo,hi)
    hits=[]
    for root in input_dirs:
        if not root.exists(): continue
        states=list(root.rglob(state_name))
        for sp in states:
            candidates=list(sp.parent.rglob(payload_name))
            if not candidates:
                candidates=list(root.rglob(payload_name))
            req(candidates, f"partial state without payload {sp}")
            for pp in candidates:
                st=json.loads(sp.read_text())
                if st.get("b")==b and st.get("band")==[lo,hi]:
                    hits.append((st,parse_payload(pp,worker_blob),sp,pp))
    if not hits: return None
    canon={(json.dumps(h[0],sort_keys=True,separators=(',',':')),h[1]["sha256"]) for h in hits}
    req(len(canon)==1, f"conflicting partial band state b={b} band={lo}..{hi}")
    st,pay,sp,pp=hits[0]
    req(st["schema"]=="STAGE32_BR204_PARTIAL_BAND_STATE_V2_LINEAGE","partial state schema")
    req(st["worker_blob"]==worker_blob,"partial worker blob")
    req(pay["b"]==b and pay["d_lo"]==lo and pay["d_hi"]==hi,"partial payload identity")
    req(st["aggregate_raw_sha256"]==pay["sha256"],"partial raw digest")
    exp=expected_ds(b,lo,hi); completed=[int(d) for d in st["completed_d"]]
    req(completed==sorted(set(completed)),"partial completed_d not sorted unique")
    req(set(completed)<set(exp),"stored partial must be incomplete")
    req(st["missing_d"]==sorted(set(exp)-set(completed)),"partial missing_d drift")
    return st,pay,sp,pp

def cmd_validate_slice(a) -> None:
    x=parse_payload(Path(a.path),a.worker_blob)
    req(x["b"]==a.b and x["d_lo"]==x["d_hi"]==a.d,"slice identity")
    req(a.d in expected_ds(a.b,*next(band for band in D_BANDS if band[0]<=a.d<=band[1])),"inadmissible slice")
    print(json.dumps({"status":"PASS","b":a.b,"d":a.d,"sha256":x["sha256"],"bytes":x["bytes"]},sort_keys=True))

def cmd_inspect_partial(a) -> None:
    hit=find_partial([Path(x) for x in a.input_dir],a.b,a.band_lo,a.band_hi,a.worker_blob)
    if hit is None:
        print(json.dumps({"found":False},sort_keys=True)); return
    st,pay,_,_=hit
    print(json.dumps({"found":True,"state":st,"payload_bytes":pay["bytes"]},sort_keys=True))

def cmd_rollup(a) -> None:
    b,lo,hi=a.b,a.band_lo,a.band_hi; exp=expected_ds(b,lo,hi); req(exp,"no admissible d")
    records=[]; completed=[]
    prior=find_partial([Path(x) for x in a.prior_dir],b,lo,hi,a.worker_blob)
    if prior is not None:
        st,pay,_,_=prior; records.append(pay); completed.extend(int(d) for d in st["completed_d"])
    seen_new={}
    for root in map(Path,a.slice_dir):
        if not root.exists(): continue
        for p in sorted(root.rglob(f"br204-s-b{b}-d*.tsv.gz")):
            m=SLICE_RE.match(p.name); req(m is not None,f"bad slice filename {p}")
            bb,d=map(int,m.groups()); req(bb==b and d in exp,f"unexpected slice {p}")
            x=parse_payload(p,a.worker_blob); req(x["b"]==b and x["d_lo"]==x["d_hi"]==d,f"slice identity drift {p}")
            req(d not in completed,f"slice duplicates prior completed d={d}")
            if d in seen_new: req(seen_new[d]["sha256"]==x["sha256"],f"conflicting duplicate d={d}")
            else: seen_new[d]=x
    for d in sorted(seen_new):
        records.append(seen_new[d]); completed.append(d)
    completed=sorted(completed); req(completed,"rollup has no completed d")
    req(set(completed)<=set(exp),"rollup completed outside expected")
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    plain=out/f"br204-rollup-b{b}-d{lo}-{hi}.tsv"
    agg=write_aggregate(records,b,lo,hi,a.worker_blob,plain)
    complete=set(completed)==set(exp)
    if complete:
        gz=out/f"br204-u-b{b}-d{lo}-{hi}.tsv.gz"
        gzip_deterministic(plain,gz); plain.unlink()
        status={"schema":"STAGE32_BR204_ROLLUP_STATUS_V1","b":b,"band":[lo,hi],"completed_d":completed,"missing_d":[],"complete":True,"payload":gz.name,"payload_gzip_bytes":gz.stat().st_size,"aggregate_raw_sha256":agg["sha256"]}
    else:
        payload_name,state_name=partial_names(b,lo,hi)
        gz=out/payload_name; gzip_deterministic(plain,gz); plain.unlink()
        parent_raw_sha=None
        parent_completed=[]
        if prior is not None:
            pst,ppay,_,_=prior
            parent_raw_sha=ppay["sha256"]
            parent_completed=[int(d) for d in pst["completed_d"]]
        state={"schema":"STAGE32_BR204_PARTIAL_BAND_STATE_V2_LINEAGE","b":b,"band":[lo,hi],"completed_d":completed,"missing_d":sorted(set(exp)-set(completed)),"worker_blob":a.worker_blob,"aggregate_raw_sha256":agg["sha256"],"aggregate_gzip_sha256":hashlib.sha256(gz.read_bytes()).hexdigest(),"payload_gzip_bytes":gz.stat().st_size,"parent_aggregate_raw_sha256":parent_raw_sha,"parent_completed_d":parent_completed}
        (out/state_name).write_text(json.dumps(state,sort_keys=True,indent=2)+"\n")
        status={"schema":"STAGE32_BR204_ROLLUP_STATUS_V1","b":b,"band":[lo,hi],"completed_d":completed,"missing_d":state["missing_d"],"complete":False,"payload":gz.name,"payload_gzip_bytes":gz.stat().st_size,"aggregate_raw_sha256":agg["sha256"],"state":state_name}
    (out/"ROLLUP-STATUS.json").write_text(json.dumps(status,sort_keys=True,indent=2)+"\n")
    print(json.dumps(status,sort_keys=True))

def cmd_bundle(a) -> None:
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    complete=set()
    if a.complete_manifest:
        p=Path(a.complete_manifest)
        if p.exists():
            m=json.loads(p.read_text())
            complete={(int(x["b"]),int(x["d_lo"]),int(x["d_hi"])) for x in m.get("subunits",[])}
    chosen={}; discovered=0
    roots=[Path(x) for x in a.input_dir]
    for root in roots:
        if not root.exists(): continue
        for sp in sorted(root.rglob("br204-partial-state-b*-d*-*.json")):
            m=STATE_RE.match(sp.name); req(m is not None,f"bad state filename {sp}")
            b,lo,hi=map(int,m.groups()); discovered+=1
            if (b,lo,hi) in complete: continue
            hit=find_partial([sp.parent],b,lo,hi,a.worker_blob); req(hit is not None,f"unreadable partial {sp}")
            st,pay,_,pp=hit; key=(b,lo,hi)
            sig=(json.dumps(st,sort_keys=True,separators=(',',':')),pay["sha256"])
            cand=(sig,st,pay,pp,sp)
            if key not in chosen:
                chosen[key]=cand
            else:
                old=chosen[key]
                if old[0]==sig:
                    continue
                old_st,old_pay=old[1],old[2]
                old_set=set(map(int,old_st["completed_d"])); new_set=set(map(int,st["completed_d"]))
                if old_set < new_set:
                    req(st.get("parent_aggregate_raw_sha256")==old_pay["sha256"],
                        f"advanced partial lacks direct parent digest {key}")
                    req(set(map(int,st.get("parent_completed_d",[])))==old_set,
                        f"advanced partial parent coverage drift {key}")
                    chosen[key]=cand
                elif new_set < old_set:
                    req(old_st.get("parent_aggregate_raw_sha256")==pay["sha256"],
                        f"existing advanced partial lacks direct parent digest {key}")
                    req(set(map(int,old_st.get("parent_completed_d",[])))==new_set,
                        f"existing advanced parent coverage drift {key}")
                else:
                    raise SystemExit(f"FAIL: non-lineage conflicting partial band {key}")
    for k,v in sorted(chosen.items()):
        _,st,pay,pp,sp=v
        shutil.copy2(sp,out/sp.name); shutil.copy2(pp,out/pp.name)
    manifest={"schema":"STAGE32_BR204_PARTIAL_BAND_BUNDLE_V3_LINEAGE","discovered_partial_state_count":discovered,"validated_partial_band_count":len(chosen),"partial_bands":[{"b":k[0],"d_lo":k[1],"d_hi":k[2],"completed_d":v[1]["completed_d"],"missing_d":v[1]["missing_d"],"aggregate_raw_sha256":v[2]["sha256"],"payload_gzip_bytes":v[3].stat().st_size,"parent_aggregate_raw_sha256":v[1].get("parent_aggregate_raw_sha256")} for k,v in sorted(chosen.items())]}
    Path(a.manifest).write_text(json.dumps(manifest,sort_keys=True,indent=2)+"\n")
    print(json.dumps(manifest,sort_keys=True))

def main() -> None:
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest="cmd",required=True)
    p=sp.add_parser("validate-slice"); p.add_argument("--path",required=True); p.add_argument("--b",type=int,required=True); p.add_argument("--d",type=int,required=True); p.add_argument("--worker-blob",required=True); p.set_defaults(fn=cmd_validate_slice)
    p=sp.add_parser("inspect-partial"); p.add_argument("--input-dir",action="append",default=[]); p.add_argument("--b",type=int,required=True); p.add_argument("--band-lo",type=int,required=True); p.add_argument("--band-hi",type=int,required=True); p.add_argument("--worker-blob",required=True); p.set_defaults(fn=cmd_inspect_partial)
    p=sp.add_parser("rollup"); p.add_argument("--prior-dir",action="append",default=[]); p.add_argument("--slice-dir",action="append",default=[]); p.add_argument("--b",type=int,required=True); p.add_argument("--band-lo",type=int,required=True); p.add_argument("--band-hi",type=int,required=True); p.add_argument("--worker-blob",required=True); p.add_argument("--out-dir",required=True); p.set_defaults(fn=cmd_rollup)
    p=sp.add_parser("bundle"); p.add_argument("--input-dir",action="append",default=[]); p.add_argument("--out-dir",required=True); p.add_argument("--manifest",required=True); p.add_argument("--worker-blob",required=True); p.add_argument("--complete-manifest"); p.set_defaults(fn=cmd_bundle)
    p=sp.add_parser("self-test"); p.set_defaults(fn=lambda a: print(json.dumps({"status":"PASS","expected_single_d_checkpoints":sum(len(expected_ds(b,lo,hi)) for b in range(97) for lo,hi in D_BANDS if hi>=max(8,2*b))},sort_keys=True)))
    a=ap.parse_args(); a.fn(a)

if __name__=="__main__": main()
