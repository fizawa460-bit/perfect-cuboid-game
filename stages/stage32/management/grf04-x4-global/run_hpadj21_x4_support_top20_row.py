#!/usr/bin/env python3
from __future__ import annotations
import argparse,bisect,hashlib,importlib.util,json,sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HPADJ21_HEAD="33f63a4c0bb3dde9d56efd895f4e8eb19d9217e2"
ROW_REL=Path("stages/stage32-ex5/hpadj-21_ex5/run_full_hist_row.py")
ROW_BLOB="68a3edcf5be71bb75ed97959fcc5f56a2fcecbd7"
LANE178_HEAD="8a8efc48866f8008d253c21ebd272e698d18dc44"
SUPPORT_REL=Path("stages/stage32/32-01-178/fibration-nef/verify_fibration_nef_zero_center_x4_support_bound.py")
SUPPORT_BLOB="58eb122b0c0154bd798d33ecbd7bedd9b30c2483"
GRF_REL=Path("stages/stage32/32-01-178/topdown-02/TD02-GRF04-FULL178-AGGREGATE-CHECKPOINT.json")
GRF_BLOB="4e2ccf5f9f8d25f117e4e9792d3b54ec31a0799b"
MANIFEST=Path(__file__).with_name("HPADJ21-TOP20-MASS-MANIFEST.json")
MANIFEST_BLOB="d4e38ed1e0b400ab8ca2ce54a0385092d3bb839c"
SCHEMA="STAGE32_MAIN_GRF04_X4_SUPPORT_HPADJ21_TOP20_ROW_V1"

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)

def blob(path):
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);req(spec and spec.loader,"cannot load "+name)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m

def uniform_x4_upper(g,d):
    genus=Fraction(d*d,16)+d+2-2*g
    h=d//2;x=0
    while True:
        if 2*x<h:
            x+=1;continue
        if Fraction((h-2*x)*(h-2*x),12)<=genus:
            x+=1;continue
        return x-1

def capped_full_survivors(h16,profiles,h,g,b,c):
    xmax=uniform_x4_upper(g,2*h)
    caps=[[],[]]
    xr=h16.a0_interval(h,g,b,c)
    if xr is not None:
        left,right=xr;right=min(int(right),xmax)
        if int(left)<=right:
            for x4 in range(int(left),right+1):
                room=-h16.f0(h,g,b,c,x4);req(room>=0,"x4 q-capacity regression")
                caps[x4&1].append(room//138)
    caps[0].sort();caps[1].sort()
    out=[[None for _ in range(4)] for __ in range(h+1)]
    for a in range(h+1):
        for s in range(4):
            tiers=profiles[a][s]
            if not tiers: continue
            grouped=defaultdict(int)
            for q,mult in tiers:
                surv=tuple(len(caps[r])-bisect.bisect_left(caps[r],q) for r in (0,1))
                grouped[surv]+=mult
            out[a][s]={"tiers":[(k[0],k[1],v) for k,v in sorted(grouped.items())]}
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--hpadj21-root",type=Path,required=True)
    ap.add_argument("--lane178-root",type=Path,required=True)
    ap.add_argument("--row-index",type=int,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    req(blob(MANIFEST)==MANIFEST_BLOB,"top20 manifest blob drift")
    mf=json.loads(MANIFEST.read_text())
    req(mf["canonical_sha256_without_this_field"]=="3067b6f6563d6b7461b5718b4508b30418ab9c22608b3003c67d07a5dc2ad14d","top20 manifest canonical drift")
    expected={int(r["row_index"]):r for r in mf["rows"]}
    req(a.row_index in expected,"row not in top20 manifest")
    exp=expected[a.row_index]

    rp=a.hpadj21_root/ROW_REL; sp=a.lane178_root/SUPPORT_REL; gp=a.lane178_root/GRF_REL
    req(rp.is_file() and blob(rp)==ROW_BLOB,"HPADJ21 row worker drift")
    req(sp.is_file() and blob(sp)==SUPPORT_BLOB,"178 x4 support source drift")
    req(gp.is_file() and blob(gp)==GRF_BLOB,"GRF04 full178 source drift")
    grf=json.loads(gp.read_text())
    req(grf["scope"]["rows_total"]==178,"GRF04 FULL178 scope drift")
    req(grf["mathematical_adapter"]["rho"]=="q/2 + (d/2 - 2*x4 - t)^2/12","GRF04 rho drift")
    req(grf["mathematical_adapter"]["t"]=="x0+x1+x6+x9","GRF04 t drift")

    rowmod=load(rp,"stage32_main_grf04_x4_top20_hpadj21")
    pilot=rowmod.load_pilot()
    pilot.full_survivors=capped_full_survivors
    rowmod.load_pilot=lambda: pilot
    got=rowmod.compute_row(a.row_index)
    req(got["row"]["row_id"]==exp["row_id"] and int(got["row"]["g"])==int(exp["g"]) and int(got["row"]["d"])==int(exp["d"]),"row identity drift")
    old=int(exp["old_hpadj21_floor"])
    new=int(got["totals"]["hpadj21_cellwise_floor_sum"])
    req(new<=old,"global x4 support weakened HPADJ21 row")
    g=int(exp["g"]);d=int(exp["d"]);xmax=uniform_x4_upper(g,d)
    genus=Fraction(d*d,16)+d+2-2*g
    first=xmax+1
    req(2*first>=d//2 and Fraction((d//2-2*first)**2,12)>genus,"x4 cutoff maximality drift")
    out={
      "schema":SCHEMA,"stage":32,
      "status":"EXACT_TOP20_ROW_GRF04_X4_SUPPORT_REPLACEMENT_CANDIDATE_ZERO_CREDIT",
      "target":{"row_index":a.row_index,"row_id":exp["row_id"],"g":g,"d":d},
      "theorem":{"uniform_x4_upper":xmax,"first_uniformly_excluded_x4":first,
        "basis":"q>=0, t=x0+x1+x6+x9>=0, residual penalty>=0 in GRF04 rho identity"},
      "population":{"pre_mass":str(got["totals"]["pre_mass"]),"post_mass":str(got["totals"]["post_mass"]),"same_hpadj21_population":True},
      "result":{"old_hpadj21_row_floor":str(old),"new_grf04_x4_row_floor":str(new),"improvement":str(old-new)},
      "source_locks":{"top20_manifest_blob_sha1":MANIFEST_BLOB,"hpadj21_head":HPADJ21_HEAD,
        "hpadj21_row_worker_blob_sha1":ROW_BLOB,"lane178_source_head":LANE178_HEAD,
        "x4_support_source_blob_sha1":SUPPORT_BLOB,"td02_grf04_full178_blob_sha1":GRF_BLOB},
      "composition":{"direct_same_population_row_replacement":True,"additive_subtraction_used":False,"statistical_independence_assumed":False},
      "firewalls":{"main_pruning_credit":False,"full178_complete":False,"theorem_credit":False,"effectivity_credit":False,"endpoint_credit":False,"stage32_closed":False,"merge_authorized":False}
    }
    out["canonical_sha256_without_this_field"]=canon(out)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    print(json.dumps({"row_index":a.row_index,"row_id":exp["row_id"],"old":old,"new":new,"gain":old-new,"x4max":xmax,"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))

if __name__=="__main__":main()
