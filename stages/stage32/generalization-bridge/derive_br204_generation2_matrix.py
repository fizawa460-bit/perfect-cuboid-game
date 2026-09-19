#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path

def req(v:bool,msg:str)->None:
    if not v: raise SystemExit("FAIL: "+msg)

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--plan",required=True)
    ap.add_argument("--targets",required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    plan=json.loads(Path(a.plan).read_text())
    targets=json.loads(Path(a.targets).read_text())
    req(targets["schema"]=="STAGE32_BR204_GENERATION1_FINER_TARGETS_V1","target schema")
    t={}
    for x in targets["targets"]:
        key=(int(x["b"]),int(x["band"][0]),int(x["band"][1]))
        req(key not in t,"multiple finer targets in one outer band are not allowed in initial generation2 plan")
        t[key]=int(x["d"])
    rows=[]
    for x in plan["missing_units"]:
        key=(int(x["b"]),int(x["d_lo"]),int(x["d_hi"]))
        d=t.get(key,-1)
        if d!=-1:
            req(x["d_lo"]<=d<=x["d_hi"] and d%2==0 and d>=max(8,2*x["b"]),"finer target outside missing band")
        rows.append({**x,"fine_d":d})
    out={
        "schema":"STAGE32_BR204_GENERATION2_MATRIX_V1",
        "source_plan_schema":plan["schema"],
        "target_count":targets["target_count"],
        "missing_outer_unit_count":len(rows),
        "finer_outer_unit_count":sum(x["fine_d"]!=-1 for x in rows),
        "matrix":rows
    }
    Path(a.out).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps(out,sort_keys=True))

if __name__=="__main__":
    main()
