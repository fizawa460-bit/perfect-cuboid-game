#!/usr/bin/env python3
from __future__ import annotations

import argparse
import bisect
import hashlib
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

ROW_WORKER_BLOB="68a3edcf5be71bb75ed97959fcc5f56a2fcecbd7"
HPADJ18_BLOB="09c3a97ca47f2602b547efc572a3ddfee1d3437f"
HPADJ16_BLOB="61805f8b6d661c29805b6966e2453ed411d73189"
HPADJ15_BLOB="99ac15d18c83da050107ac7e8b113ae795ff0629"
HPADJ10_BLOB="eebeb47f91df22461c33e9974d63aceca4da3b52"
ROW_CERT_CANON="ba356db05dfb3699c7a13b59698d30cad9599a32e3bf409f6e6d5de45c42ddca"
EXPECTED_PRE=207312456066801657003
EXPECTED_POST=85212642937627265785
EXPECTED_NUM=1824391732631330409367
EXPECTED_DEN=883
EXPECTED_FLOOR=2066128802526988006


def req(v:bool,msg:str)->None:
    if not v: raise SystemExit("FAIL: "+msg)


def blob(path:Path)->str:
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def canonical(obj:dict)->str:
    body=dict(obj);body.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":")).encode()).hexdigest()


def load_module(path:Path,name:str):
    spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None: raise RuntimeError(path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod


def build_A(H:int,h10):
    out=[[Counter() for _ in range(4)] for __ in range(H+1)]
    for a in range(H+1):
        for x2 in range(a+1):
            for x3 in range(a-x2+1):
                x7=a-x2-x3
                s=int(x2>0)+int(x3>0)+int(x7>0)
                q=x2*x2+x3*x3+x7*x7
                out[a][s][q]+=1
        for s in range(4):
            req(sum(out[a][s].values())==h10.triple_free_count(a,s),f"A population drift {(a,s)}")
    return out


def add_range(diff:Counter[int],lo:int,hi:int,count:int,excluded:set[int])->None:
    if lo%2: lo+=1
    if hi%2: hi-=1
    if lo>hi:return
    diff[lo]+=count;diff[hi+2]-=count
    for ex in excluded:
        if lo<=ex<=hi and ex%2==0:
            diff[ex]-=count;diff[ex+2]+=count


def greedy(caps:dict[tuple[int,int],int],mass:int):
    total=sum(caps.values());req(total>=mass>=0,"mass outside capacity")
    ratio_caps=Counter()
    for (s,B),cap in caps.items():
        ratio_caps[Fraction(s,B)]+=int(cap)
    rem=mass;obj=Fraction(0,1);trace=[]
    for ratio,cap in sorted(ratio_caps.items(),key=lambda kv:kv[0],reverse=True):
        take=min(rem,cap)
        if take:
            obj+=ratio*take;rem-=take
        trace.append((ratio,cap,take,rem))
        if rem==0:break
    req(rem==0,"LP did not cover post mass")
    cutoff=trace[-1][0]
    return obj,total,cutoff,trace,ratio_caps


def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--row-worker",type=Path,required=True)
    ap.add_argument("--hpadj18",type=Path,required=True)
    ap.add_argument("--hpadj16",type=Path,required=True)
    ap.add_argument("--hpadj15",type=Path,required=True)
    ap.add_argument("--hpadj10",type=Path,required=True)
    ap.add_argument("--row-cert",type=Path,required=True)
    args=ap.parse_args()
    for label,path,expected in (
      ("row worker",args.row_worker,ROW_WORKER_BLOB),("HPADJ18",args.hpadj18,HPADJ18_BLOB),
      ("HPADJ16",args.hpadj16,HPADJ16_BLOB),("HPADJ15",args.hpadj15,HPADJ15_BLOB),
      ("HPADJ10",args.hpadj10,HPADJ10_BLOB)):
        req(path.is_file() and blob(path)==expected,f"{label} drift")
    row=json.loads(args.row_cert.read_text())
    req(row.get("canonical_sha256_without_this_field")==ROW_CERT_CANON and canonical(row)==ROW_CERT_CANON,"row certificate canonical drift")
    req(row["row"]=={"index":22,"row_id":"g1-d192","g":1,"d":192},"row identity drift")
    rec=[x for x in row["cell_records"] if x["b_interval"]==[36,47]]
    req(len(rec)==1,"target cell missing")
    rec=rec[0]
    req((rec["pre_mass"],rec["post_mass"],rec["hpadj21_num"],rec["hpadj21_den"],rec["hpadj21_floor"])==
        (EXPECTED_PRE,EXPECTED_POST,EXPECTED_NUM,EXPECTED_DEN,EXPECTED_FLOOR),"target cell receipt drift")

    h16=load_module(args.hpadj16,"stage32_178_cell_h16")
    h15=load_module(args.hpadj15,"stage32_178_cell_h15")
    h10=load_module(args.hpadj10,"stage32_178_cell_h10")
    req(h15.PLANNED==((0,11),(12,23),(24,35),(36,47),(48,59),(60,71),(72,83),(84,96)),"planned shards drift")
    req(h15.shard_for_b(36)==(36,47) and h15.shard_for_b(47)==(36,47),"target shard routing drift")

    g,d,h=1,192,96
    K=h10.ceil_div(d-16*g+16,4);legacy=4
    BC=h10.build_bc_exact_parity(h)
    A=build_A(h,h10)

    # Difference map: q_s -> even-e range-add of exceptional-prefix counts.
    diffs=defaultdict(Counter)
    source_groups=0
    for b in range(36,48):
      for c in range(h+1):
        bcv=BC[b][c]
        if not any(any(pair) for pair in bcv):continue
        c3=h10.component3(d,b,c)
        if c3<0:continue
        xr=h16.a0_interval(h,g,b,c)
        caps_r=[[],[]]
        if xr is not None:
            for x4 in range(xr[0],xr[1]+1):
                room=-int(h16.f0(h,g,b,c,x4))
                req(room>=0,"a0 interval contains negative room")
                caps_r[x4&1].append(room//138)
            caps_r[0].sort();caps_r[1].sort()
        for a in range(h+1):
            ca=h10.component_a(d,a)
            if ca<0:continue
            M=a+b+c;srem=min(16,d)+ca+c3
            qdist={}
            for sa in range(4):
              if not A[a][sa]:continue
              for r in (0,1):
                ctr=Counter()
                arr=caps_r[r]
                for qA,mult in A[a][sa].items():
                    qs=len(arr)-bisect.bisect_left(arr,int(qA))
                    ctr[qs]+=int(mult)
                qdist[(sa,r)]=ctr
            for sbc,pair in enumerate(bcv):
              for r in (0,1):
                left=int(pair[r])
                if not left:continue
                for sa in range(4):
                    ctr=qdist.get((sa,r))
                    if not ctr:continue
                    support=sbc+sa
                    qneed=K-support
                    if qneed>0 and srem<qneed:continue
                    lower=max(legacy,K,d-4*g+4,M,M+max(0,qneed))
                    upper=min((19*d)//5,3*d,3*d-(b-c))
                    if lower>upper:continue
                    excluded=set();e_n358=3*d-(b-c)
                    if b<=h-5 and support+srem==K and e_n358-M>=srem:
                        excluded.add(e_n358)
                    for qs,amult in ctr.items():
                        count=left*int(amult)
                        if not count:continue
                        add_range(diffs[int(qs)],lower,upper,count,excluded)
                        source_groups+=1

    req(diffs,"empty target-cell source diff")
    caps=defaultdict(int)
    min_e=min(k for diff in diffs.values() for k in diff)
    max_e=max(k for diff in diffs.values() for k in diff)
    if min_e%2:min_e+=1
    if max_e%2:max_e-=1
    for qs,diff in diffs.items():
        running=0
        for e in range(min_e,max_e+1,2):
            running+=diff.get(e,0)
            if running:
                B=19*d-5*e+1
                req(B>0 and B%2==1,f"normal B drift e={e}")
                caps[(int(qs),B)]+=running*B
    pre=sum(caps.values())
    req(pre==EXPECTED_PRE,f"reconstructed pre mass {pre} != {EXPECTED_PRE}")

    obj,total,cutoff,trace,ratio_caps=greedy(caps,EXPECTED_POST)
    req(total==EXPECTED_PRE,"LP total capacity drift")
    req(obj==Fraction(EXPECTED_NUM,EXPECTED_DEN),f"exact rational objective drift {obj}")
    req(obj.numerator//obj.denominator==EXPECTED_FLOOR,"cell floor drift")

    cutoff_bins=[]
    for (s,B),cap in sorted(caps.items()):
        if Fraction(s,B)==cutoff:
            e=(19*d+1-B)//5
            cutoff_bins.append({"s":s,"B":B,"e":e,"capacity":str(cap)})
    max_ratio=max(ratio_caps)
    selected_levels=len(trace)
    cutoff_cap=ratio_caps[cutoff]
    cutoff_take=trace[-1][2]
    next_lower=max((r for r in ratio_caps if r<cutoff),default=Fraction(0,1))
    e192_max_ratio=max((Fraction(s,B) for (s,B) in caps if B==2689),default=Fraction(0,1))

    out={
      "schema":"STAGE32_32_01_178_HPADJ21_G1D192_B36_47_CELL_REPLAY_V1",
      "status":"EXACT_CURRENT_CELL_REPLAY_PASS__ROUTING_TELEMETRY_ZERO_CREDIT",
      "source":{"row_id":"g1-d192","g":1,"d":192,"b_interval":[36,47],
                "row_certificate_canonical":ROW_CERT_CANON,
                "hpadj21_row_worker_blob":ROW_WORKER_BLOB,
                "hpadj18_optimizer_blob":HPADJ18_BLOB,
                "hpadj16_blob":HPADJ16_BLOB,"hpadj15_blob":HPADJ15_BLOB,"hpadj10_blob":HPADJ10_BLOB},
      "replay":{"source_groups":source_groups,"ratio_bin_count":len(caps),"ratio_level_count":len(ratio_caps),
                "pre_mass":str(pre),"post_mass":str(EXPECTED_POST),
                "objective_num":obj.numerator,"objective_den":obj.denominator,
                "floor":obj.numerator//obj.denominator},
      "cutoff":{"maximum_ratio":str(max_ratio),"selected_ratio_levels":selected_levels,
                "cutoff_ratio":str(cutoff),"cutoff_capacity":str(cutoff_cap),
                "cutoff_taken_mass":str(cutoff_take),"next_lower_ratio":str(next_lower),
                "cutoff_bins":cutoff_bins,
                "e192_max_ratio":str(e192_max_ratio),
                "e192_is_below_cutoff":e192_max_ratio<cutoff},
      "routing":{"next_exact_target":"Find zero-center strict refinements in current source bins with q_s/B >= the exact cutoff ratio; low-ratio e192 subsets cannot tighten this cell LP even when they strictly reduce raw survivor capacity."},
      "firewalls":{"main_credit_changed":False,"main_bound_replacement_authorized":False,"full178_complete":False,"theorem_credit_changed":False,"endpoint_credit_changed":False,"merge":False},
    }
    print("HPADJ21_G1D192_B36_47_CELL_REPLAY_SUMMARY="+json.dumps({
      "pre":str(pre),"post":str(EXPECTED_POST),"floor":EXPECTED_FLOOR,
      "max_ratio":str(max_ratio),"cutoff":str(cutoff),"next_lower":str(next_lower),
      "cutoff_bins":cutoff_bins,"e192_max_ratio":str(e192_max_ratio),
      "e192_below_cutoff":e192_max_ratio<cutoff,
    },sort_keys=True))
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
