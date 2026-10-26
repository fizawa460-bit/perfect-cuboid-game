#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.util,json,math,sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
DIRECT=ROOT/"stages/stage32/management/hpadj22-fast-global/benchmark_direct_count.py"
DIRECT_BLOB="e965ab0a6ea51938006882ca2110016f48b3768e"
PROJECTION=ROOT/"stages/stage32/management/grf04-quadratic-capacity/verify_grf04_main_bc_qt_integer_projection_preflight.py"
PROJECTION_BLOB="6b85abcd693586191eb83a7f275b8dd5d9c69b18"
SOURCE_HEAD="4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
MAX_D=16
SCHEMA="STAGE32_MAIN_V46_GRF04_INTEGER_PROJECTION_X_HPADJ22_BOUNDED_PILOT_V1"

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def load(path,expected,name):
    req(path.is_file() and blob(path)==expected,name+" blob drift")
    spec=importlib.util.spec_from_file_location(name,path);req(spec and spec.loader,"cannot load "+name)
    mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod);return mod

def x4_points(h16,h,g,b,c):
    out=[[],[]]
    xr=h16.a0_interval(h,g,b,c)
    if xr is None:return out
    left,right=xr
    for x4 in range(left,right+1):
        room=-h16.f0(h,g,b,c,x4)
        req(room>=0,f"x4 room regression {(g,h,b,c,x4)}")
        out[x4&1].append((x4,room//138))
    return out

def grf_interval(proj,counter,*,d,g,b,c,qbc,q,n):
    tint=proj.integer_t_interval(b,c,qbc)
    if tint is None:return None
    rhs=3*d*d+48*d+96-96*g
    rem=rhs-24*q
    if rem<0:return None
    rad=math.isqrt(rem//4)
    tlo,thi=tint
    lo=max(0,counter.ceil_div(d//2-thi-rad,2))
    hi=min(n,(d//2-tlo+rad)//2)
    return None if lo>hi else (lo,hi)

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--source-root",type=Path,required=True);ap.add_argument("--output",type=Path,required=True);a=ap.parse_args()
    direct=load(DIRECT,DIRECT_BLOB,"v46_hpadj22_direct_locked")
    proj=load(PROJECTION,PROJECTION_BLOB,"v46_grf04_integer_projection_locked")
    old=direct.load_old(a.source_root);ctx=old.source_context()
    bc,bnd,h21,h18,h16,p15,p14,counter,rows,rejected,profiles,classes_gt2,tuples_above_second=ctx
    selected=[i for i,(_,_,d) in enumerate(rows) if int(d)<=MAX_D]
    req(selected,"no bounded rows")
    max_h=max(int(rows[i][2])//2 for i in selected)
    req(max_h<=11,"bounded pilot escaped band0")
    joint=bc.build_joint_bc_shard(max_h,0,max_h)

    total_h22=total_joint=0
    strict_rows=0
    row_out=[]
    for idx in selected:
        row_id,g0,d0=rows[idx];g,d=int(g0),int(d0);h=d//2
        baseline=direct.direct_count(old,ctx,joint,0,idx)
        K=counter.ceil_div(d-16*g+16,4);threshold8=d*d+16*d+(32 if g==0 else 0)
        rebuilt=joint_count=0;strict_cells=0;tested_cells=0
        for b in range(h+1):
            for c in range(h+1):
                jbc=joint[b][c]
                if not any(any(bool(jbc[s][r]) for r in (0,1)) for s in range(8)):continue
                c3=counter.component3(d,b,c)
                if c3<0:continue
                points=x4_points(h16,h,g,b,c)
                for aa in range(h+1):
                    ca=counter.component_a(d,aa)
                    if ca<0:continue
                    srem=min(16,d)+ca+c3
                    ec={}
                    for support in range(11):
                        es=bnd.eligible_e(counter,d,g,h,aa,b,c,support,srem,K)
                        if es:ec[support]=es
                    if not ec:continue
                    for sbc,r in ((s,r) for s in range(8) for r in (0,1)):
                        hist=jbc[sbc][r]
                        if not hist:continue
                        for sa in range(4):
                            tiers=profiles[aa][sa];es=ec.get(sbc+sa)
                            if not tiers or es is None:continue
                            for qa,va0 in tiers:
                                va=int(va0)
                                picard=sum(1 for _,cap in points[r] if cap>=qa)
                                for qb0,vb0 in hist.items():
                                    qb,vb=int(qb0),int(vb0)
                                    if 8*(qa+qb)>threshold8:continue
                                    rebuilt += va*vb*picard*len(es)
                                    for e in es:
                                        n=19*d-5*int(e)
                                        gi=grf_interval(proj,counter,d=d,g=g,b=b,c=c,qbc=qb,q=qa+qb,n=n)
                                        if gi is None:
                                            count=0
                                        else:
                                            lo,hi=gi
                                            count=sum(1 for x4,cap in points[r] if cap>=qa and lo<=x4<=hi)
                                        joint_count += va*vb*count
                                        tested_cells+=1
                                        strict_cells+=int(count<picard)
        base=int(baseline["hpadj22_exact_survivors"])
        req(rebuilt==base,f"HPADJ22 exact rebuild mismatch {row_id}: {rebuilt}!={base}")
        req(joint_count<=base,f"joint condition weakened HPADJ22 {row_id}")
        strict=joint_count<base
        strict_rows+=int(strict);total_h22+=base;total_joint+=joint_count
        row_out.append({"row_index":idx,"row_id":row_id,"g":g,"d":d,"hpadj22_exact":base,"joint_exact":joint_count,"improvement":base-joint_count,"strict":strict,"tested_qbc_e_cells":tested_cells,"strict_x4_cells":strict_cells})
    out={
      "schema":SCHEMA,"stage":32,"status":"BOUNDED_EXACT_INTERSECTION_COMPLETE_ZERO_CREDIT",
      "scope":{"max_d":MAX_D,"row_count":len(selected),"b_domain":"band0 covers all b because h<=8"},
      "source_locks":{"hpadj22_source_head":SOURCE_HEAD,"direct_count_blob_sha1":DIRECT_BLOB,"integer_projection_verifier_blob_sha1":PROJECTION_BLOB,"old_hpadj22_worker_blob_sha1":direct.OLD_BLOB},
      "construction":{"hpadj22_condition":"8*(qA+qBC)<=d^2+16*d+(32 if g=0 else 0)","picard_x4_condition":"exact x4 capacity point has room//138>=qA and required parity","grf04_integer_projection":"exact integer t interval at fixed (b,c,qBC), then exact x4 interval from GRF04","intersection_count":"enumerate x4 points only; require both Picard capacity/parity and GRF04 interval for each surviving (qA,qBC,e) compact cell","min_of_counts_used":False,"raw_terminal_identity_materialized":False},
      "result":{"hpadj22_bounded_exact_survivors":total_h22,"joint_bounded_exact_survivors":total_joint,"exact_improvement":total_h22-total_joint,"strict_row_count":strict_rows,"strict":total_joint<total_h22},
      "rows":row_out,
      "interpretation":{"full178_scaleout_authorized":False,"strict_bounded_witness_required_before_scaleout":True,"same_population_direct_refinement":True,"additive_subtraction":False},
      "firewalls":{"main_pruning_credit":False,"full178_complete":False,"effectivity_credit":False,"receiver_credit":False,"route_credit":False,"theorem_credit":False,"endpoint_credit":False,"stage32_closed":False,"perfect_cuboid_credit":False,"merge_authorized":False}
    }
    out["canonical_sha256_without_this_field"]=canon(out)
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    print("GRF04_HPADJ22_BOUNDED="+json.dumps({"rows":len(selected),"h22":total_h22,"joint":total_joint,"improvement":total_h22-total_joint,"strict_rows":strict_rows,"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))
if __name__=="__main__":main()
