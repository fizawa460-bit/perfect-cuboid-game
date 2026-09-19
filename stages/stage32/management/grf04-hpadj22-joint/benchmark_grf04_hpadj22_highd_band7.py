#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.util,json,math,sys,time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
DIRECT=ROOT/"stages/stage32/management/hpadj22-fast-global/benchmark_direct_count.py"
DIRECT_BLOB="e965ab0a6ea51938006882ca2110016f48b3768e"
PROJECTION=ROOT/"stages/stage32/management/grf04-quadratic-capacity/verify_grf04_main_bc_qt_integer_projection_preflight.py"
PROJECTION_BLOB="6b85abcd693586191eb83a7f275b8dd5d9c69b18"
E_VERIFY=ROOT/"stages/stage32/management/grf04-hpadj22-joint/verify_grf04_hpadj22_v46_e_independence_preflight.py"
E_VERIFY_BLOB="bcb7c6d438f6f1ce936a2e9d668d1fde9d19fc8f"
SOURCE_HEAD="4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
ROW_INDEX=177
BAND=7
SCHEMA="STAGE32_MAIN_V46_GRF04_HPADJ22_HIGHD_BAND7_BENCHMARK_V1"

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def load(path,expected,name):
    req(path.is_file() and blob(path)==expected,name+" blob drift")
    spec=importlib.util.spec_from_file_location(name,path); req(spec and spec.loader,"cannot load "+name)
    mod=importlib.util.module_from_spec(spec); sys.modules[spec.name]=mod; spec.loader.exec_module(mod); return mod

def x4_points(h16,h,g,b,c):
    out=[[],[]]
    xr=h16.a0_interval(h,g,b,c)
    if xr is None:return out
    left,right=xr
    req(0<=left<=right<8*h,f"a0 interval cap regression {(g,h,b,c,xr)}")
    for x4 in range(left,right+1):
        room=-h16.f0(h,g,b,c,x4)
        req(room>=0,f"x4 room regression {(g,h,b,c,x4)}")
        out[x4&1].append((x4,room//138))
    return out

def grf_interval_e_independent(proj,counter,*,d,g,b,c,qbc,q):
    tint=proj.integer_t_interval(b,c,qbc)
    if tint is None:return None
    rhs=3*d*d+48*d+96-96*g
    rem=rhs-24*q
    if rem<0:return None
    rad=math.isqrt(rem//4)
    tlo,thi=tint
    lo=max(0,counter.ceil_div(d//2-thi-rad,2))
    hi=(d//2-tlo+rad)//2
    return None if lo>hi else (lo,hi)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--source-root",type=Path,required=True); ap.add_argument("--output",type=Path,required=True); a=ap.parse_args()
    direct=load(DIRECT,DIRECT_BLOB,"v46_h22_direct_highd")
    proj=load(PROJECTION,PROJECTION_BLOB,"v46_grf04_proj_highd")
    req(E_VERIFY.is_file() and blob(E_VERIFY)==E_VERIFY_BLOB,"e-independence verifier drift")
    old=direct.load_old(a.source_root)
    ctx=old.source_context()
    bc,bnd,h21,h18,h16,p15,p14,counter,rows,rejected,profiles,classes_gt2,tuples_above_second=ctx
    row_id,g0,d0=rows[ROW_INDEX]; g,d=int(g0),int(d0); h=d//2
    req((g,d)==(1,192),f"row177 identity drift {(row_id,g,d)}")
    req(tuple(old.PLANNED[BAND])==(84,96),"band7 interval drift")
    b0,b1=old.PLANNED[BAND]

    t0=time.perf_counter()
    joint=bc.build_joint_bc_shard(old.HMAX,b0,b1)
    t1=time.perf_counter()
    base=direct.direct_count(old,ctx,joint,BAND,ROW_INDEX)
    t2=time.perf_counter()

    K=counter.ceil_div(d-16*g+16,4)
    threshold8=d*d+16*d+(32 if g==0 else 0)
    rebuild_h22=0
    joint_exact=0
    tested_pairs=0
    strict_pairs=0
    cache={}
    point_cache={}
    for b in range(b0,min(b1,h)+1):
      for c in range(h+1):
        jbc=joint[b][c]
        if not any(any(bool(jbc[s][r]) for r in (0,1)) for s in range(8)):continue
        c3=counter.component3(d,b,c)
        if c3<0:continue
        points=point_cache.setdefault((b,c),x4_points(h16,h,g,b,c))
        for aa in range(h+1):
          ca=counter.component_a(d,aa)
          if ca<0:continue
          srem=min(16,d)+ca+c3
          ec={}
          for support in range(11):
            es=bnd.eligible_e(counter,d,g,h,aa,b,c,support,srem,K)
            if es:ec[support]=es
          if not ec:continue
          for sbc in range(8):
            for r in (0,1):
              hist=jbc[sbc][r]
              if not hist:continue
              for sa in range(4):
                tiers=profiles[aa][sa]; es=ec.get(sbc+sa)
                if not tiers or es is None:continue
                ne=len(es)
                # e-independence proof: every eligible e gives n=19d-5e >= 4d,
                # while every Picard x4 point satisfies x4 < 4d.
                req(all(19*d-5*int(e)>=4*d for e in es),f"eligible e lower n regression {(b,c,aa,sbc,sa)}")
                for qa0,va0 in tiers:
                  qa,va=int(qa0),int(va0)
                  picard=sum(1 for _,cap in points[r] if cap>=qa)
                  survive_bc=0
                  joint_weighted=0
                  for qb0,vb0 in hist.items():
                    qb,vb=int(qb0),int(vb0)
                    if 8*(qa+qb)>threshold8:continue
                    survive_bc += vb
                    key=(b,c,r,qa,qb)
                    cnt=cache.get(key)
                    if cnt is None:
                      gi=grf_interval_e_independent(proj,counter,d=d,g=g,b=b,c=c,qbc=qb,q=qa+qb)
                      if gi is None: cnt=0
                      else:
                        lo,hi=gi
                        cnt=sum(1 for x4,cap in points[r] if cap>=qa and lo<=x4<=hi)
                      req(cnt<=picard,f"joint escaped Picard {(b,c,r,qa,qb,cnt,picard)}")
                      cache[key]=cnt
                    tested_pairs+=1
                    strict_pairs+=int(cnt<picard)
                    joint_weighted += vb*cnt
                  rebuild_h22 += survive_bc*va*picard*ne
                  joint_exact += joint_weighted*va*ne
    t3=time.perf_counter()

    baseline=int(base["hpadj22_exact_survivors"])
    req(rebuild_h22==baseline,f"HPADJ22 rebuild mismatch {rebuild_h22}!={baseline}")
    req(joint_exact<=baseline,"joint weakened HPADJ22")
    improvement=baseline-joint_exact
    out={
      "schema":SCHEMA,"stage":32,"status":"HIGHD_EXACT_BENCHMARK_COMPLETE_ZERO_CREDIT",
      "target":{"row_index":ROW_INDEX,"row_id":row_id,"g":g,"d":d,"band_position":BAND,"b_interval":[b0,b1]},
      "source_locks":{"hpadj22_source_head":SOURCE_HEAD,"direct_count_blob_sha1":DIRECT_BLOB,"integer_projection_verifier_blob_sha1":PROJECTION_BLOB,"e_independence_verifier_blob_sha1":E_VERIFY_BLOB,"old_hpadj22_worker_blob_sha1":direct.OLD_BLOB},
      "exactness":{"hpadj22_exact_rebuilt":True,"x4_intersection_exact":True,"e_independence_used":True,"min_of_counts_used":False,"additive_subtraction":False,"raw_terminal_identity_materialized":False},
      "result":{"hpadj22_exact_survivors":baseline,"joint_exact_survivors":joint_exact,"exact_improvement":improvement,"strict":joint_exact<baseline,"tested_qA_qBC_pairs":tested_pairs,"strict_qA_qBC_pairs":strict_pairs,"cached_intersection_cells":len(cache)},
      "timing_seconds":{"joint_bc_build":round(t1-t0,6),"hpadj22_direct_row":round(t2-t1,6),"joint_exact_row":round(t3-t2,6),"total":round(t3-t0,6)},
      "decision":{"full178_scaleout_authorized":False,"if_strict_and_operationally_bounded":"prepare separate resumable FULL178 scaleout contract/runkey; do not grant MAIN credit until exact aggregate hostile audit","if_not_strict":"stop this route"},
      "firewalls":{"main_pruning_credit":False,"full178_complete":False,"effectivity_credit":False,"receiver_credit":False,"route_credit":False,"theorem_credit":False,"endpoint_credit":False,"stage32_closed":False,"perfect_cuboid_credit":False,"merge_authorized":False}
    }
    out["canonical_sha256_without_this_field"]=canon(out)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    print("GRF04_HPADJ22_HIGHD="+json.dumps({"baseline":baseline,"joint":joint_exact,"improvement":improvement,"strict":joint_exact<baseline,"timing":out["timing_seconds"],"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))

if __name__=="__main__":
    main()
