#!/usr/bin/env python3
from __future__ import annotations

import argparse, copy, hashlib, json, re
from pathlib import Path

SCHEMA="STAGE32_CUT201_E8_COMMON_ADAPTER_WAVE9_SHARD_V1"

def csha(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def req(ok,msg):
    if not ok: raise RuntimeError(msg)

def checked(path: Path):
    obj=json.loads(path.read_text()); q=dict(obj); claimed=q.pop("canonical_sha256_without_this_field",None)
    req(obj.get("schema")==SCHEMA,f"schema drift: {path.name}")
    req(claimed==csha(q),f"canonical drift: {path.name}")
    req(obj["credit"]["stage32_main_pruning_credit"] is False and obj["credit"]["cut201_pruning_credit"] is False,"credit leak")
    req(obj["firewalls"]["main_authority_mutated"] is False,"MAIN mutation leak")
    return obj

def combine(args):
    root=args.root; sid=int(args.shard_id); start=int(args.start); end=int(args.end)
    req(start<=end,"invalid range")
    files=sorted(root.glob(f"cut201-g11-shard-{sid}-part-*.json"))
    expected=[]; x=start; pid=0
    while x<=end:
        y=min(x+7,end); expected.append((pid,x,y)); pid+=1; x=y+1
    req(len(files)==len(expected),f"expected {len(expected)} parts, got {len(files)}")
    docs=[]; got=[]
    for p in files:
        m=re.fullmatch(rf"cut201-g11-shard-{sid}-part-(\d+)\.json",p.name); req(m is not None,f"filename drift {p.name}")
        d=checked(p); a,b=map(int,d["target"]["survivor_offset_range"]); got.append((int(m.group(1)),a,b)); docs.append(d)
    req(sorted(got)==expected,f"subpart coverage drift: {sorted(got)}")
    ordered=[d for _,d in sorted(zip(got,docs),key=lambda z:z[0][0])]
    first=ordered[0]
    for d in ordered[1:]:
        req(d["source"]==first["source"] and d["method"]==first["method"] and d["credit"]==first["credit"] and d["firewalls"]==first["firewalls"],"subpart invariant drift")
        for k in ("row_id","g","d","e","cut191_block0_disjoint","cut193_wave1_disjoint","cut194_wave2_disjoint","cut195_wave3_disjoint","cut196_wave4_disjoint","cut197_wave5_disjoint","cut198_wave6_disjoint","cut199_wave7_disjoint","cut200_wave8_disjoint","n356_preserved_all_wave_blocks"):
            req(d["target"][k]==first["target"][k],f"target invariant drift: {k}")
    covered=[]; block_indices=[]; closed=[]; recs=[]; methods={}
    for d in ordered:
        a,b=d["target"]["survivor_offset_range"]; covered+=list(range(int(a),int(b)+1)); block_indices+=list(d["target"]["block_indices"]); closed+=list(d["result"]["candidate_closed_block_indices"]); recs+=list(d["result"]["blocks"])
        for k,v in d["result"]["method_counts"].items(): methods[k]=methods.get(k,0)+int(v)
    req(covered==list(range(start,end+1)),"offset union gap/overlap")
    count=end-start+1
    req(len(block_indices)==count and len(set(block_indices))==count and len(recs)==count,"block union gap/duplicate")
    req(sorted(r["block_index"] for r in recs)==sorted(block_indices),"record coverage drift")
    closed=sorted(int(v) for v in closed); req(len(closed)==len(set(closed)),"duplicate closure")
    bh=hashlib.sha256(); ch=hashlib.sha256()
    for i in block_indices: bh.update(f"{i}\n".encode())
    for i in closed: ch.update(f"{i}\n".encode())
    out=copy.deepcopy(first); out.pop("canonical_sha256_without_this_field",None)
    out["target"]["survivor_offset_range"]=[start,end]; out["target"]["block_indices"]=block_indices; out["target"]["block_index_stream_sha256"]=bh.hexdigest(); out["target"]["block_count"]=count; out["target"]["terminal_count"]=113*count
    out["result"]["candidate_closed_block_indices"]=closed; out["result"]["candidate_closed_block_count"]=len(closed); out["result"]["candidate_closed_block_stream_sha256"]=ch.hexdigest(); out["result"]["candidate_pruned_terminals"]=113*len(closed); out["result"]["method_counts"]=methods; out["result"]["blocks"]=recs
    out["canonical_sha256_without_this_field"]=csha(out); args.output.write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps({"shard_id":sid,"range":[start,end],"blocks":count,"closed":len(closed),"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--root",type=Path,required=True); ap.add_argument("--shard-id",type=int,required=True); ap.add_argument("--start",type=int,required=True); ap.add_argument("--end",type=int,required=True); ap.add_argument("--output",type=Path,required=True); combine(ap.parse_args())
if __name__=="__main__": main()
