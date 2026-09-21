#!/usr/bin/env python3
from __future__ import annotations

import argparse
import bisect
import hashlib
import importlib.util
import json
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HPADJ21_HEAD="33f63a4c0bb3dde9d56efd895f4e8eb19d9217e2"
ROW_REL=Path("stages/stage32-ex5/hpadj-21_ex5/run_full_hist_row.py")
ROW_BLOB="68a3edcf5be71bb75ed97959fcc5f56a2fcecbd7"
LANE178_AUDITED_HEAD="8a8efc48866f8008d253c21ebd272e698d18dc44"
SUPPORT_REL=Path("stages/stage32/32-01-178/fibration-nef/verify_fibration_nef_zero_center_x4_support_bound.py")
SUPPORT_BLOB="58eb122b0c0154bd798d33ecbd7bedd9b30c2483"
GRF_REL=Path("stages/stage32/32-01-178/topdown-02/TD02-GRF04-FULL178-AGGREGATE-CHECKPOINT.json")
GRF_BLOB="4e2ccf5f9f8d25f117e4e9792d3b54ec31a0799b"
SCHEMA="STAGE32_MAIN_GRF04_X4_SUPPORT_HPADJ21_ROW_PILOT_V1"

def req(v:bool,msg:str)->None:
    if not v:
        raise SystemExit("FAIL: "+msg)

def blob(path:Path)->str:
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def canonical(obj:dict)->str:
    body=dict(obj)
    body.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def load_module(path:Path,name:str):
    spec=importlib.util.spec_from_file_location(name,path)
    req(spec is not None and spec.loader is not None,"cannot load "+str(path))
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod

def uniform_x4_upper(g:int,d:int)->int:
    req(d>0 and d%2==0,"FULL178 d parity")
    genus=Fraction(d*d,16)+d+2-2*g
    h=d//2
    x=0
    while True:
        if 2*x < h:
            x += 1
            continue
        rho=Fraction((h-2*x)*(h-2*x),12)
        if rho <= genus:
            x += 1
            continue
        return x-1

def capped_full_survivors(h16,profiles,h:int,g:int,b:int,c:int):
    d=2*h
    xmax=uniform_x4_upper(g,d)
    caps=[[],[]]
    xr=h16.a0_interval(h,g,b,c)
    if xr is not None:
        left,right=xr
        right=min(int(right),xmax)
        if int(left)<=right:
            for x4 in range(int(left),right+1):
                room=-h16.f0(h,g,b,c,x4)
                req(room>=0,"capped q interval construction regression")
                caps[x4&1].append(room//138)
    caps[0].sort()
    caps[1].sort()
    out=[[None for _ in range(4)] for __ in range(h+1)]
    for a in range(h+1):
        for s in range(4):
            tiers=profiles[a][s]
            if not tiers:
                continue
            grouped=defaultdict(int)
            for q,mult in tiers:
                surv=tuple(len(caps[r])-bisect.bisect_left(caps[r],q) for r in (0,1))
                grouped[surv]+=mult
            out[a][s]={"tiers":[(k[0],k[1],v) for k,v in sorted(grouped.items())]}
    return out

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--hpadj21-root",type=Path,required=True)
    ap.add_argument("--lane178-root",type=Path,required=True)
    ap.add_argument("--row-index",type=int,required=True)
    ap.add_argument("--expected-row-id",required=True)
    ap.add_argument("--expected-old-floor",type=int,required=True)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()

    row_path=args.hpadj21_root/ROW_REL
    support_path=args.lane178_root/SUPPORT_REL
    grf_path=args.lane178_root/GRF_REL
    req(row_path.is_file() and blob(row_path)==ROW_BLOB,"HPADJ21 row worker drift")
    req(support_path.is_file() and blob(support_path)==SUPPORT_BLOB,"audited x4-support source drift")
    req(grf_path.is_file() and blob(grf_path)==GRF_BLOB,"TD02 GRF04 aggregate drift")
    grf=json.loads(grf_path.read_text())
    req(grf["mathematical_adapter"]["rho"]=="q/2 + (d/2 - 2*x4 - t)^2/12","GRF04 rho identity drift")
    req(grf["mathematical_adapter"]["t"]=="x0+x1+x6+x9","GRF04 nonnegative-t identity drift")

    rowmod=load_module(row_path,"stage32_main_global_x4_hpadj21_row")
    old=rowmod.compute_row(args.row_index)
    req(old["row"]["row_id"]==args.expected_row_id,"row identity drift")
    req(int(old["totals"]["hpadj21_cellwise_floor_sum"])==args.expected_old_floor,"audited HPADJ21 old floor drift")

    pilot=rowmod.load_pilot()
    rowmod.load_pilot=lambda: pilot
    pilot.full_survivors=capped_full_survivors
    new=rowmod.compute_row(args.row_index)

    req(new["row"]==old["row"],"row identity changed")
    for k in ("pre_mass","post_mass"):
        req(new["totals"][k]==old["totals"][k],k+" changed")
    req(len(new["cell_records"])==len(old["cell_records"]),"cell coverage changed")

    cells=[]
    strict=0
    for before,after in zip(old["cell_records"],new["cell_records"]):
        req(before["b_interval"]==after["b_interval"],"cell order drift")
        req(before["pre_mass"]==after["pre_mass"] and before["post_mass"]==after["post_mass"],"cell population drift")
        old_floor=int(before["hpadj21_floor"])
        new_floor=int(after["hpadj21_floor"])
        req(new_floor<=old_floor,"GRF04 x4 support weakened a cell")
        strict += int(new_floor<old_floor)
        cells.append({"b_interval":before["b_interval"],"old_floor":old_floor,"new_floor":new_floor,"improvement":old_floor-new_floor})

    old_floor=int(old["totals"]["hpadj21_cellwise_floor_sum"])
    new_floor=int(new["totals"]["hpadj21_cellwise_floor_sum"])
    req(new_floor<=old_floor,"row floor weakened")
    g=int(old["row"]["g"])
    d=int(old["row"]["d"])
    xmax=uniform_x4_upper(g,d)
    genus=Fraction(d*d,16)+d+2-2*g
    next_rho=Fraction((d//2-2*(xmax+1))**2,12)
    req(2*(xmax+1)>=d//2 and next_rho>genus,"uniform cutoff not maximal")

    out={
      "schema":SCHEMA,
      "stage":32,
      "status":"EXACT_SAME_POPULATION_GRF04_X4_SUPPORT_ROW_REPLACEMENT_CANDIDATE_ZERO_CREDIT",
      "target":{"row_index":args.row_index,"row_id":args.expected_row_id,"g":g,"d":d},
      "theorem":{
        "rho":"q/2 + (d/2 - 2*x4 - t)^2/12",
        "q_nonnegative":True,
        "t_nonnegative":True,
        "residual_penalty_nonnegative":True,
        "genus_budget":str(genus),
        "uniform_x4_upper":xmax,
        "first_uniformly_excluded_x4":xmax+1,
        "first_excluded_static_rho":str(next_rho),
        "formula":"largest integer x with 2*x<d/2 or (d/2-2*x)^2/12 <= d^2/16+d+2-2g"
      },
      "result":{
        "old_hpadj21_row_floor":old_floor,
        "new_grf04_x4_support_row_floor":new_floor,
        "row_floor_improvement":old_floor-new_floor,
        "strict_cells_vs_hpadj21":strict,
        "cell_count":len(cells)
      },
      "cells":cells,
      "composition":{
        "same_hpadj21_pre_domain_population":True,
        "same_certified_post_mass":True,
        "only_additional_condition":"audited GRF04 t-uniform x4 static support necessity",
        "additive_subtraction_used":False,
        "statistical_independence_assumed":False,
        "row_replacement_not_additive_saving":True
      },
      "source_locks":{
        "hpadj21_head":HPADJ21_HEAD,
        "hpadj21_row_worker_blob_sha1":ROW_BLOB,
        "lane178_audited_head":LANE178_AUDITED_HEAD,
        "x4_support_verifier_blob_sha1":SUPPORT_BLOB,
        "td02_grf04_aggregate_blob_sha1":GRF_BLOB
      },
      "firewalls":{
        "main_pruning_credit":False,
        "full178_complete":False,
        "theorem_credit":False,
        "effectivity_credit":False,
        "receiver_credit":False,
        "endpoint_credit":False,
        "stage32_closed":False,
        "merge_authorized":False
      }
    }
    out["canonical_sha256_without_this_field"]=canonical(out)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    print("GRF04_X4_TOPROW_PILOT_SUMMARY="+json.dumps(out["result"],sort_keys=True))
    print("GRF04_X4_TOPROW_PILOT_THEOREM="+json.dumps(out["theorem"],sort_keys=True))
    print("GRF04_X4_TOPROW_PILOT_CANONICAL="+out["canonical_sha256_without_this_field"])

if __name__=="__main__":
    main()
