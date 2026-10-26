#!/usr/bin/env python3
from __future__ import annotations
import argparse,bisect,hashlib,importlib.util,json,math,sys,time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
DIRECT=ROOT/"stages/stage32/management/hpadj22-fast-global/benchmark_direct_count.py"
DIRECT_BLOB="e965ab0a6ea51938006882ca2110016f48b3768e"
PROJECTION=ROOT/"stages/stage32/management/grf04-quadratic-capacity/verify_grf04_main_bc_qt_integer_projection_preflight.py"
PROJECTION_BLOB="6b85abcd693586191eb83a7f275b8dd5d9c69b18"
E_VERIFY=ROOT/"stages/stage32/management/grf04-hpadj22-joint/verify_grf04_hpadj22_v46_e_independence_preflight.py"
E_VERIFY_BLOB="582432a2995d523c247808d39e0ff5ff14611c2a"
SOURCE_HEAD="4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
SUPERSEDED_RUN_ID=35429121561
SUPERSEDED_JOB_ID=105860468317
ROW_INDEX=177
BAND=7
SCHEMA="STAGE32_MAIN_V46_GRF04_HPADJ22_HIGHD_FAST_BAND7_BENCHMARK_V1"

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)

def blob(p):
    b=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def canon(o):
    x=dict(o)
    x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def load(path,expected,name):
    req(path.is_file() and blob(path)==expected,name+" blob drift")
    spec=importlib.util.spec_from_file_location(name,path)
    req(spec and spec.loader,"cannot load "+name)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=mod
    spec.loader.exec_module(mod)
    return mod

def x4_points(h16,h,g,b,c):
    out=[[],[]]
    xr=h16.a0_interval(h,g,b,c)
    if xr is None:
        return out
    left,right=xr
    req(0<=left<=right<8*h,f"a0 interval cap regression {(g,h,b,c,xr)}")
    for x4 in range(left,right+1):
        room=-h16.f0(h,g,b,c,x4)
        req(room>=0,f"x4 room regression {(g,h,b,c,x4)}")
        out[x4&1].append((x4,room//138))
    return out

def interval_table(proj,b,c,qkeys):
    keys=sorted(set(int(q) for q in qkeys))
    if not keys:
        return {}
    vals=[]
    for t in range(b+c+1):
        q=proj.qmin_fast(b,c,t)
        req(q is not None,f"missing qmin {(b,c,t)}")
        vals.append((int(q),t))
    vals.sort()
    out={}
    pos=0
    lo=hi=None
    count=0
    for qbc in keys:
        while pos<len(vals) and vals[pos][0]<=qbc:
            _,t=vals[pos]
            lo=t if lo is None else min(lo,t)
            hi=t if hi is None else max(hi,t)
            count+=1
            pos+=1
        if count==0:
            out[qbc]=None
        else:
            req(lo is not None and hi is not None,"interval state")
            req(count==hi-lo+1,f"integer projected t-set not contiguous {(b,c,qbc,lo,hi,count)}")
            out[qbc]=(lo,hi)
    return out

def count_intersection(counter,eligible_x4,*,d,g,tint,q):
    if tint is None or not eligible_x4:
        return 0
    rhs=3*d*d+48*d+96-96*g
    rem=rhs-24*q
    if rem<0:
        return 0
    rad=math.isqrt(rem//4)
    tlo,thi=tint
    lo=max(0,counter.ceil_div(d//2-thi-rad,2))
    hi=(d//2-tlo+rad)//2
    if lo>hi:
        return 0
    return bisect.bisect_right(eligible_x4,hi)-bisect.bisect_left(eligible_x4,lo)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-root",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()

    direct=load(DIRECT,DIRECT_BLOB,"v46_h22_direct_highd_fast")
    proj=load(PROJECTION,PROJECTION_BLOB,"v46_grf04_proj_highd_fast")
    req(E_VERIFY.is_file() and blob(E_VERIFY)==E_VERIFY_BLOB,"e-independence verifier drift")

    old=direct.load_old(a.source_root)
    ctx=old.source_context()
    bc,bnd,h21,h18,h16,p15,p14,counter,rows,rejected,profiles,classes_gt2,tuples_above_second=ctx
    row_id,g0,d0=rows[ROW_INDEX]
    g,d=int(g0),int(d0)
    h=d//2
    req((g,d)==(1,190),f"row177 identity drift {(row_id,g,d)}")
    req(tuple(old.PLANNED[BAND])==(84,96),"band7 interval drift")
    b0,b1=old.PLANNED[BAND]

    qa_values=set()
    ca=[counter.component_a(d,aa) for aa in range(h+1)]
    aprof={}
    for aa in range(h+1):
        if ca[aa]<0:
            continue
        for sa in range(4):
            tiers=profiles[aa][sa]
            if tiers:
                tt=tuple((int(q),int(v)) for q,v in tiers)
                aprof[(aa,sa)]=tt
                qa_values.update(q for q,_ in tt)
    qa_values=sorted(qa_values)

    t0=time.perf_counter()
    joint=bc.build_joint_bc_shard(old.HMAX,b0,b1)
    t1=time.perf_counter()
    base=direct.direct_count(old,ctx,joint,BAND,ROW_INDEX)
    t2=time.perf_counter()

    K=counter.ceil_div(d-16*g+16,4)
    tq=(d*d+16*d+(32 if g==0 else 0))//8
    rebuild_h22=0
    joint_exact=0
    tested_pairs=0
    strict_pairs=0
    interval_key_count=0
    weighted_cache_cells=0
    point_cache={}
    precompute_seconds=0.0
    accumulate_seconds=0.0

    for b in range(b0,min(b1,h)+1):
      for c in range(h+1):
        jbc=joint[b][c]
        active=[]
        qkeys=set()
        for sbc in range(8):
          for r in (0,1):
            hist=jbc[sbc][r]
            if not hist:
                continue
            clean={int(q):int(v) for q,v in hist.items() if int(v)}
            if clean:
                active.append((sbc,r,clean))
                qkeys.update(q for q in clean if q<=tq)
        if not active:
            continue
        c3=counter.component3(d,b,c)
        if c3<0:
            continue

        tp0=time.perf_counter()
        intervals=interval_table(proj,b,c,qkeys)
        interval_key_count+=len(intervals)
        points=point_cache.setdefault((b,c),x4_points(h16,h,g,b,c))
        eligible={}
        picard={}
        for r in (0,1):
            for qa in qa_values:
                xs=[x4 for x4,cap in points[r] if cap>=qa]
                eligible[(r,qa)]=xs
                picard[(r,qa)]=len(xs)

        weighted={}
        for sbc,r,hist in active:
            for qa in qa_values:
                cut=tq-qa
                if cut<0:
                    weighted[(sbc,r,qa)]=(0,0)
                    continue
                xs=eligible[(r,qa)]
                survive=0
                joint_weight=0
                pcount=picard[(r,qa)]
                for qb,vb in hist.items():
                    if qb>cut:
                        continue
                    survive+=vb
                    cnt=count_intersection(counter,xs,d=d,g=g,tint=intervals.get(qb),q=qa+qb)
                    req(cnt<=pcount,f"joint escaped Picard {(b,c,sbc,r,qa,qb,cnt,pcount)}")
                    tested_pairs+=1
                    strict_pairs+=int(cnt<pcount)
                    joint_weight+=vb*cnt
                weighted[(sbc,r,qa)]=(survive,joint_weight)
                weighted_cache_cells+=1
        precompute_seconds+=time.perf_counter()-tp0

        ta0=time.perf_counter()
        for aa in range(h+1):
          if ca[aa]<0:
            continue
          srem=min(16,d)+ca[aa]+c3
          ec={}
          for support in range(11):
            es=bnd.eligible_e(counter,d,g,h,aa,b,c,support,srem,K)
            if es:
                req(all(19*d-5*int(e)>=4*d for e in es),
                    f"eligible e lower n regression {(b,c,aa,support)}")
                ec[support]=len(es)
          if not ec:
            continue
          for sbc,r,hist in active:
            for sa in range(4):
              tiers=aprof.get((aa,sa))
              ne=ec.get(sbc+sa)
              if tiers is None or ne is None:
                continue
              for qa,va in tiers:
                survive,joint_weight=weighted[(sbc,r,qa)]
                rebuild_h22 += survive*va*picard[(r,qa)]*ne
                joint_exact += joint_weight*va*ne
        accumulate_seconds+=time.perf_counter()-ta0

    t3=time.perf_counter()

    baseline=int(base["hpadj22_exact_survivors"])
    req(baseline==236901807892797077,f"retained row177 baseline drift {baseline}")
    req(rebuild_h22==baseline,f"HPADJ22 rebuild mismatch {rebuild_h22}!={baseline}")
    req(joint_exact<=baseline,"joint weakened HPADJ22")
    improvement=baseline-joint_exact

    out={
      "schema":SCHEMA,
      "stage":32,
      "status":"HIGHD_FAST_EXACT_BENCHMARK_COMPLETE_ZERO_CREDIT",
      "supersedes":{"workflow_run_id":SUPERSEDED_RUN_ID,"job_id":SUPERSEDED_JOB_ID,"reason":"generation5 exact benchmark was operationally coarse; generation6 preserves semantics and replaces repeated qBC interval scans with an exact per-(b,c) threshold table plus weighted intersection cache"},
      "target":{"row_index":ROW_INDEX,"row_id":row_id,"g":g,"d":d,"band_position":BAND,"b_interval":[b0,b1]},
      "source_locks":{"hpadj22_source_head":SOURCE_HEAD,"direct_count_blob_sha1":DIRECT_BLOB,"integer_projection_verifier_blob_sha1":PROJECTION_BLOB,"e_independence_verifier_blob_sha1":E_VERIFY_BLOB,"old_hpadj22_worker_blob_sha1":direct.OLD_BLOB},
      "exactness":{
        "hpadj22_exact_rebuilt":True,
        "retained_row177_baseline_crosscheck":True,
        "integer_t_sublevel_set_built_from_exact_qmin_fast_values":True,
        "integer_t_sublevel_contiguity_checked_for_every_used_qbc_threshold":True,
        "x4_intersection_exact":True,
        "e_independence_used":True,
        "qbc_weighted_intersection_cached_outside_a_loop":True,
        "min_of_counts_used":False,
        "additive_subtraction":False,
        "raw_terminal_identity_materialized":False
      },
      "result":{
        "hpadj22_exact_survivors":baseline,
        "joint_exact_survivors":joint_exact,
        "exact_improvement":improvement,
        "strict":joint_exact<baseline,
        "tested_unique_qA_qBC_hist_pairs":tested_pairs,
        "strict_unique_qA_qBC_hist_pairs":strict_pairs,
        "integer_interval_thresholds":interval_key_count,
        "weighted_cache_cells":weighted_cache_cells
      },
      "timing_seconds":{
        "joint_bc_build":round(t1-t0,6),
        "hpadj22_direct_row":round(t2-t1,6),
        "joint_precompute":round(precompute_seconds,6),
        "joint_accumulate":round(accumulate_seconds,6),
        "joint_exact_total":round(t3-t2,6),
        "total":round(t3-t0,6)
      },
      "decision":{
        "full178_scaleout_authorized":False,
        "if_strict_and_operationally_bounded":"prepare separate resume-first FULL178 band/row scaleout contract; zero MAIN credit until exact aggregate plus hostile audit",
        "if_not_strict":"stop this route"
      },
      "firewalls":{
        "main_pruning_credit":False,
        "full178_complete":False,
        "effectivity_credit":False,
        "receiver_credit":False,
        "route_credit":False,
        "theorem_credit":False,
        "endpoint_credit":False,
        "stage32_closed":False,
        "perfect_cuboid_credit":False,
        "merge_authorized":False
      }
    }
    out["canonical_sha256_without_this_field"]=canon(out)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    print("GRF04_HPADJ22_HIGHD_FAST="+json.dumps({
      "baseline":baseline,
      "joint":joint_exact,
      "improvement":improvement,
      "strict":joint_exact<baseline,
      "timing":out["timing_seconds"],
      "canonical":out["canonical_sha256_without_this_field"]
    },sort_keys=True))

if __name__=="__main__":
    main()
