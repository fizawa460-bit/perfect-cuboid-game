#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, pathlib

AUT_SCHEMA="STAGE32_AUT_PERM_SOURCELOCK_V1"
EXPECTED_SOURCE_BLOB="0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_GROUP_ORDER=1536
SEED="stage32-d16-aut-a"
M=140

def sha_weights(seed:str)->list[int]:
    out=[]
    for i in range(M):
        d=hashlib.sha256(f"{seed}:{i}".encode()).digest()
        out.append(int.from_bytes(d[:4],"big")%2000003-1000001)
    return out

def compose(p:tuple[int,...],q:tuple[int,...])->tuple[int,...]:
    return tuple(q[p[i]] for i in range(M))

def load_group(path:pathlib.Path)->list[tuple[int,...]]:
    payload=json.loads(path.read_text())
    if payload.get("schema")!=AUT_SCHEMA: raise RuntimeError("bad Aut schema")
    if payload.get("source",{}).get("git_blob_sha1")!=EXPECTED_SOURCE_BLOB: raise RuntimeError("Aut source blob mismatch")
    raw=payload.get("permutations_1based")
    if not isinstance(raw,list) or len(raw)!=9: raise RuntimeError("expected nine generators")
    gens=[tuple(int(x)-1 for x in row) for row in raw]
    ident=tuple(range(M)); seen={ident}; frontier=[ident]
    while frontier:
        nxt=[]
        for cur in frontier:
            for gen in gens:
                v=compose(cur,gen)
                if v not in seen:
                    seen.add(v); nxt.append(v)
        frontier=nxt
    if len(seen)!=EXPECTED_GROUP_ORDER: raise RuntimeError(f"Aut closure order {len(seen)}")
    return sorted(seen)

def canonical_key(v:tuple[int,...],p:tuple[int,...],weights:list[int])->tuple[int,tuple[int,...]]:
    out=[0]*M
    for old in range(M): out[p[old]]=v[old]
    t=tuple(out)
    return sum(weights[i]*t[i] for i in range(M)),t

def records(path:pathlib.Path)->list[tuple[int,tuple[int,...]]]:
    raw=path.read_bytes()
    if raw[:8]!=b"S32D16C1": raise RuntimeError("bad dump magic")
    body=raw[8:]; size=M+1
    if len(body)%size: raise RuntimeError("truncated dump")
    return [(body[o],tuple(body[o+1:o+size])) for o in range(0,len(body),size)]

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--aut",type=pathlib.Path,required=True)
    ap.add_argument("--dump",type=pathlib.Path,required=True)
    ap.add_argument("--enum-json",type=pathlib.Path,required=True)
    ap.add_argument("--output",type=pathlib.Path,required=True)
    ap.add_argument("--bound",type=int,required=True)
    args=ap.parse_args()
    group=load_group(args.aut); weights=sha_weights(SEED)
    recs=records(args.dump); enum=json.loads(args.enum_json.read_text())
    if enum.get("bound")!=args.bound or enum.get("status")!="COMPLETE": raise RuntimeError("bound/status mismatch")
    if enum.get("aut_group_order")!=EXPECTED_GROUP_ORDER: raise RuntimeError("group order mismatch")
    if enum.get("canonical_survivors_including_zero")!=len(recs): raise RuntimeError("dump/result count mismatch")
    pairings=[v for _,v in recs]
    if len(pairings)!=len(set(pairings)): raise RuntimeError("duplicate canonical pairing")
    for v in pairings:
        base=(sum(weights[i]*v[i] for i in range(M)),v)
        best=min(canonical_key(v,p,weights) for p in group)
        if base!=best: raise RuntimeError("noncanonical pairing emitted")
    hist={}
    for norm,_ in recs: hist[str(norm)]=hist.get(str(norm),0)+1
    out={
      "schema":"STAGE32_18B_D16_BOUND_CANONICAL_VERIFY_V1",
      "bound":args.bound,
      "enum_schema":enum.get("schema"),
      "aut_group_order":len(group),
      "canonical_record_count":len(recs),
      "canonical_pairings_unique":True,
      "every_emitted_pairing_is_full_group_score_then_lex_minimum":True,
      "precanonical_survivors":enum.get("precanonical_survivors"),
      "canonical_survivors_including_zero":enum.get("canonical_survivors_including_zero"),
      "canonical_nonzero_survivors":enum.get("canonical_nonzero_survivors"),
      "norm_histogram":hist,
      "THEOREM_CREDIT":False,"RECEIVER_CREDIT":False,"FULL_D16_G0_ROW_COMPLETE":False
    }
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(out,sort_keys=True))
if __name__=="__main__": main()
