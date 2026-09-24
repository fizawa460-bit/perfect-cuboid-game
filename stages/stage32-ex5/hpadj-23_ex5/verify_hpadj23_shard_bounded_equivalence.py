#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
FULL=HERE/"build_exact_t_joint_histogram.py"
SHARD=HERE/"build_exact_t_joint_histogram_shard.py"
RESULT=HERE/"HPADJ23-SHARD-BOUNDED-EQUIVALENCE.json"
MANIFEST=ROOT/"stages/stage32/residual-32-01-production/full178-manifest.json"

LOCKS={
    "full":"c02973cb9d7fdea7584661a9c5935a43e12efe92",
    "shard":"25284ea56c0746912318ce3c0d0e75d50cf60458",
    "result":"b1a0248926c176a31a57da0fbb97807c3bb0eeba",
    "result_canonical":"5899b8eaac1cd6205d421d6f92874f4dbff47a31a00b37029cc84f9365c19a9b",
    "manifest":"0a46b34e278688240656b4977e9cb7f589e90e06",
    "manifest_canonical":"46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23",
}
BANDS=((0,3),(4,7),(8,11),(12,16))
EXPECTED=((2544,5178,13354),(7717,24616,98998),(12366,52799,304826),(25040,124881,887843))

def req(v: bool,msg: str)->None:
    if not v:
        raise SystemExit("FAIL: "+msg)

def blob(path:Path)->str:
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def canon(obj:dict)->str:
    body=dict(obj);body.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def load_module(path:Path,name:str):
    spec=importlib.util.spec_from_file_location(name,path)
    req(spec is not None and spec.loader is not None,"cannot load "+name)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod)
    return mod

def normalized(hist):
    return {k:dict(sorted(v.items())) for k,v in hist.items() if v}

def metrics(hist):
    return (len(hist),sum(len(v) for v in hist.values()),sum(sum(int(x) for x in v.values()) for v in hist.values()))

def main()->None:
    req(blob(FULL)==LOCKS["full"],"full builder blob drift")
    req(blob(SHARD)==LOCKS["shard"],"shard builder blob drift")
    req(blob(RESULT)==LOCKS["result"],"bounded result blob drift")
    req(blob(MANIFEST)==LOCKS["manifest"],"FULL178 manifest blob drift")
    result=json.loads(RESULT.read_text())
    req(result["canonical_sha256_without_this_field"]==LOCKS["result_canonical"]==canon(result),"bounded result canonical drift")
    manifest=json.loads(MANIFEST.read_text())
    req(manifest["canonical_sha256_without_this_field"]==LOCKS["manifest_canonical"]==canon(manifest),"manifest canonical drift")

    rows=[]
    for arr in manifest["m_class_rows"].values():
        for row_id in arr:
            m=re.fullmatch(r"g([01])-d(\d+)",row_id)
            req(m is not None,"row-id parse drift "+row_id)
            rows.append((int(m.group(1)),int(m.group(2))))
    ds=sorted({d for _,d in rows})
    hs=sorted({d//2 for _,d in rows})
    req(len(rows)==178,"FULL178 row count")
    req(ds==list(range(8,193,2)),"degree support drift")
    req(hs==list(range(4,97)),"H support drift")
    req(len(ds)==93 and len(hs)==93,"unique degree/H count")

    full=load_module(FULL,"hpadj23_full_locked_for_shard_equiv")
    shard=load_module(SHARD,"hpadj23_shard_locked_for_equiv")

    h16=full.build_joint_bc_t(16)
    union={}
    seen=set()
    got=[]
    for (a,b),want in zip(BANDS,EXPECTED):
        part=shard.build_joint_bc_t_shard(16,a,b)
        got.append(metrics(part))
        for key,val in part.items():
            req(key not in seen,"shard overlap "+str(key))
            seen.add(key);union[key]=val
        req(got[-1]==want,f"shard metric drift {(a,b)}: {got[-1]} != {want}")
    req(normalized(union)==normalized(h16),"H16 shard union/full mismatch")
    req(metrics(union)==(47667,207474,1305021),"H16 union metric drift")

    # Prefix-invariance regression.  The mathematical reason is structural:
    # fixed nonnegative BC coordinates sum to b/c, hence are <= b/c and do not
    # see a larger ambient H once H>=max(b,c).
    h8=full.build_joint_bc_t(8)
    prefix={k:v for k,v in h16.items() if k[0]<=8 and k[1]<=8}
    req(normalized(h8)==normalized(prefix),"H8/H16 prefix invariance regression")

    s=result["scaleout_semantics"]
    req(s["full178_row_count"]==178 and s["unique_degree_count"]==93 and s["unique_H_count"]==93,"retained scaleout counts")
    req(s["H_min"]==4 and s["H_max"]==96 and s["universal_H96_can_supply_all_full178_rows"] is True,"universal H96 contract")
    req(s["scaleout_execution_armed"] is False and s["representative_measurement_required_before_arm"] is True,"scaleout authorization drift")
    req(all(v is False for v in result["firewalls"].values()),"credit/authorization firewall raised")

    print(json.dumps({
        "verdict":"PASS_HPADJ23_SHARD_BOUNDED_EQUIVALENCE",
        "full178_rows":178,
        "unique_H":93,
        "H_range":[4,96],
        "H16_union":[47667,207474,1305021],
        "prefix_invariance_H8_in_H16":True,
        "scaleout_armed":False,
    },sort_keys=True))

if __name__=="__main__":
    main()
