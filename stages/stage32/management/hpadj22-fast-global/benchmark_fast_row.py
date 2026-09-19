#!/usr/bin/env python3
from __future__ import annotations

import argparse
import bisect
import hashlib
import importlib.util
import json
import sys
import time
from collections import defaultdict
from pathlib import Path

SOURCE_HEAD="4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
OLD_REL=Path("stages/stage32-ex5/hpadj-22_ex5/run_full_bband.py")
OLD_BLOB="2c998a190baaf5f29b33a91fd9efedbb036cef46"
SCHEMA="STAGE32_MAIN_HPADJ22_FAST_EQUIVALENCE_BENCHMARK_V1"

def req(v:bool,msg:str)->None:
    if not v: raise SystemExit("FAIL: "+msg)

def blob(path:Path)->str:
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def canonical(obj:dict)->str:
    body=dict(obj); body.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def load_old(root:Path):
    p=root/OLD_REL
    req(p.is_file() and blob(p)==OLD_BLOB,"HPADJ22 old band worker drift")
    spec=importlib.util.spec_from_file_location("hpadj22_old_locked_for_fast",p)
    req(spec is not None and spec.loader is not None,"cannot load old HPADJ22 worker")
    mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
    return mod

def qprefix(hist):
    items=sorted((int(q),int(v)) for q,v in hist.items() if int(v))
    qs=[]; pref=[]; total=0
    for q,v in items:
        qs.append(q); total+=v; pref.append(total)
    return qs,pref,total

def prefix_le(qs,pref,cut):
    i=bisect.bisect_right(qs,cut)-1
    return 0 if i<0 else pref[i]

def compute_fast(old,ctx,joint,band_position,row_index):
    bc,bnd,h21,h18,h16,p15,p14,counter,rows,rejected,profiles,classes_gt2,tuples_above_second=ctx
    row_id,g0,d0=rows[row_index]
    g,d=int(g0),int(d0);h=d//2
    interval=old.PLANNED[band_position]; b0,b1=interval
    K=counter.ceil_div(d-16*g+16,4)
    threshold8=d*d+16*d+(32 if g==0 else 0)
    threshold_q=threshold8//8
    pre=reject=h22=0
    h21_caps=defaultdict(int)

    # Row-invariant A/profile summaries.
    aprof={}
    ca_by_a={}
    for a in range(h+1):
        ca=counter.component_a(d,a)
        ca_by_a[a]=ca
        if ca<0: continue
        for sa in range(4):
            tiers=profiles[a][sa]
            if tiers:
                aprof[(a,sa)]=(tuple((int(q),int(v)) for q,v in tiers),sum(int(v) for _,v in tiers))

    for b in range(b0,min(b1,h)+1):
        for c in range(h+1):
            jbc=joint[b][c]
            active=[]
            for sbc in range(8):
                for r in (0,1):
                    hist=jbc[sbc][r]
                    if not hist: continue
                    qs,pref,left_total=qprefix(hist)
                    if left_total:
                        active.append((sbc,r,qs,pref,left_total))
            if not active: continue
            c3=counter.component3(d,b,c)
            if c3<0: continue
            caps=bnd.x4_caps(h16,h,g,b,c)
            surv_cache=[{},{}]

            for a in range(h+1):
                ca=ca_by_a[a]
                if ca<0: continue
                srem=min(16,d)+ca+c3

                # eligible_e depends on support, not parity/qA/qBC.
                e_cache={}
                for support in range(11):
                    es=bnd.eligible_e(counter,d,g,h,a,b,c,support,srem,K)
                    if es:
                        Bs=tuple(19*d-5*int(e)+1 for e in es)
                        req(all(B>0 and B%2==1 for B in Bs),f"normal block drift {(g,d,a,b,c,support)}")
                        e_cache[support]=(len(Bs),sum(Bs),Bs)
                if not e_cache: continue

                for sbc,r,qs,pref,left_total in active:
                    for sa in range(4):
                        pv=aprof.get((a,sa))
                        if pv is None: continue
                        ev=e_cache.get(sbc+sa)
                        if ev is None: continue
                        tiers,a_total=pv
                        ne,normal_sum,Bs=ev
                        pre += left_total*a_total*normal_sum

                        # Same HPADJ21 capacity, but group qA levels with the same x4 survivor count.
                        by_s=defaultdict(int)
                        h22_local=0
                        rc=surv_cache[r]
                        for qa,va in tiers:
                            s=rc.get(qa)
                            if s is None:
                                s=bnd.survivor_count(caps,r,qa); rc[qa]=s
                            by_s[s]+=va
                            survive_bc=prefix_le(qs,pref,threshold_q-qa)
                            reject_bc=left_total-survive_bc
                            reject += reject_bc*va*normal_sum
                            h22_local += survive_bc*va*s
                        h22 += h22_local*ne
                        for s,va_sum in by_s.items():
                            coeff=left_total*va_sum
                            for B in Bs:
                                h21_caps[(s,B)] += coeff*B

    retained_reject=int(rejected[(interval,g,d)])
    req(reject==retained_reject,f"HPADJ08 retained rejected-mass mismatch: {reject} != {retained_reject}")
    req(sum(h21_caps.values())==pre,"HPADJ21 capacity/pre mismatch")
    post=pre-reject; req(post>=0,"negative post mass")
    if pre==0:
        req(reject==0 and h22==0 and not h21_caps,"zero-cell drift")
        from fractions import Fraction
        h21_obj=Fraction(0,1)
    else:
        h21_obj,_,_,_=h18.optimize_cell_exact_predomain(h21_caps,post)
    h21_floor=h21_obj.numerator//h21_obj.denominator
    req(h22<=h21_floor,"fast HPADJ22 weakened HPADJ21")

    out={
      "schema":old.SCHEMA_ROW,"route_id":"HPADJ-22_ex5","band_position":band_position,
      "b_interval":list(interval),"row":{"index":row_index,"row_id":row_id,"g":g,"d":d},
      "source_locks":old.row_source_locks(bc,bnd,h21,p14),
      "totals":{"pre_mass":pre,"rejected_mass":reject,"post_mass":post,
        "hpadj21_num":h21_obj.numerator,"hpadj21_den":h21_obj.denominator,
        "hpadj21_floor":h21_floor,"hpadj22_exact_survivors":h22,
        "strict":h22<h21_floor,"improvement":h21_floor-h22},
      "profile":{"classes_with_more_than_two_qA_bins":classes_gt2,"tuples_above_second_qA_level":tuples_above_second},
      "semantics":{"one_exact_hpadj15_b_shard_cell":True,"joint_qA_qBC_picard_parity_used":True,
        "retained_hpadj08_rejected_mass_replayed_exactly":True,"same_population_as_hpadj21":True,
        "same_picard_qA_rule_as_hpadj21":True,"additive_subtraction_used":False},
      "credit_firewall":{"partial_output_credit":False,"stage32_main_credit":False,"full178_completion_credit":False,
        "theorem_credit":False,"effectivity_credit":False,"receiver_credit":False,"route_credit":False,
        "endpoint_credit":False,"perfect_cuboid_credit":False,"merge_authorized":False}}
    out["canonical_sha256_without_this_field"]=old.canonical(out)
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-root",type=Path,required=True)
    ap.add_argument("--baseline-row",type=Path,required=True)
    ap.add_argument("--band-position",type=int,default=7)
    ap.add_argument("--row-index",type=int,default=177)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    old=load_old(a.source_root)
    req(0<=a.band_position<len(old.PLANNED),"band position")
    ctx=old.source_context()
    bc=ctx[0]
    b0,b1=old.PLANNED[a.band_position]
    t0=time.perf_counter()
    joint=bc.build_joint_bc_shard(old.HMAX,b0,b1)
    t1=time.perf_counter()
    got=compute_fast(old,ctx,joint,a.band_position,a.row_index)
    t2=time.perf_counter()

    baseline=json.loads(a.baseline_row.read_text())
    old.validate_row_obj(baseline,a.band_position,a.row_index,ctx[8],old.row_source_locks(ctx[0],ctx[1],ctx[2],ctx[6]))
    req(got==baseline,"fast worker differs from retained exact baseline row")

    out={"schema":SCHEMA,"stage":32,"status":"EXACT_EQUIVALENCE_PASS_ZERO_CREDIT",
      "source":{"hpadj22_source_head":SOURCE_HEAD,"old_band_worker_blob_sha1":OLD_BLOB,
        "baseline_row_canonical":baseline["canonical_sha256_without_this_field"]},
      "target":{"band_position":a.band_position,"row_index":a.row_index,"row_id":got["row"]["row_id"],"g":got["row"]["g"],"d":got["row"]["d"]},
      "timing":{"joint_build_seconds":round(t1-t0,6),"fast_row_seconds":round(t2-t1,6),"total_seconds":round(t2-t0,6)},
      "result":{"full_json_identity":True,"hpadj21_floor":got["totals"]["hpadj21_floor"],
        "hpadj22_exact_survivors":got["totals"]["hpadj22_exact_survivors"],"improvement":got["totals"]["improvement"]},
      "optimization":{"qbc_histogram_prefix_sum":True,"x4_survivor_memoization":True,
        "eligible_e_support_cache":True,"hpadj21_same_survivor_grouping":True,"mathematical_semantics_changed":False},
      "firewalls":{"main_pruning_credit":False,"full178_complete":False,"merge_authorized":False}}
    out["canonical_sha256_without_this_field"]=canonical(out)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    print("HPADJ22_FAST_BENCHMARK="+json.dumps(out,sort_keys=True))

if __name__=="__main__":main()
