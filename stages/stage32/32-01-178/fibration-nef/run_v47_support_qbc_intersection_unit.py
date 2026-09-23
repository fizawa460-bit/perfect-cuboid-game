#!/usr/bin/env python3
from __future__ import annotations
import argparse,bisect,hashlib,importlib.util,json,math,sys,time
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SUPPORT=HERE/"run_hpadj22_support_qbc_local_row_b.py"
V47_HELPER=ROOT/"stages/stage32/management/grf04-hpadj22-joint/benchmark_grf04_hpadj22_highd_bchunk.py"
PREFLIGHT=HERE/"V47-SUPPORT-QBC-INTERSECTION-PREFLIGHT.json"

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def load(p,name):
    spec=importlib.util.spec_from_file_location(name,p); req(spec and spec.loader,"cannot load "+str(p))
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo-root",type=Path,required=True)
    ap.add_argument("--source-root",type=Path,required=True)
    ap.add_argument("--row-index",type=int,required=True)
    ap.add_argument("--b",type=int,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args(); started=time.perf_counter()
    pf=json.loads(PREFLIGHT.read_text()); v=pf["v47_authority"]; sp=pf["support_qbc_producer"]
    req(blob(SUPPORT)==sp["worker_blob_sha1"],"support worker drift")
    req(blob(V47_HELPER)==v["helper_blob_sha1"],"V47 helper drift")
    support=load(SUPPORT,"v47_support_qbc_math")
    hd=load(V47_HELPER,"v47_grf04_helper")
    req(hd.DIRECT_BLOB=="e965ab0a6ea51938006882ca2110016f48b3768e","V47 direct source drift")
    req(hd.PROJECTION_BLOB=="6b85abcd693586191eb83a7f275b8dd5d9c69b18","V47 projection source drift")
    direct=hd.load(hd.DIRECT,hd.DIRECT_BLOB,"v47_support_direct")
    proj=hd.load(hd.PROJECTION,hd.PROJECTION_BLOB,"v47_support_projection")
    old=direct.load_old(a.source_root);ctx=old.source_context()
    bc,bnd,h21,h18,h16,p15,p14,counter,rows,rejected,profiles,classes_gt2,tuples_above_second=ctx
    req(0<=a.row_index<len(rows),"row index")
    row_id,g0,d0=rows[a.row_index];g,d=int(g0),int(d0);h=d//2
    req(0<=a.b<=h,"b outside row")
    band=next(i for i,(lo,hi) in enumerate(old.PLANNED) if lo<=a.b<=hi)
    joint=bc.build_joint_bc_shard(old.HMAX,a.b,a.b)
    ca=[counter.component_a(d,x) for x in range(h+1)]
    aprof={};qa_values=set()
    for aa in range(h+1):
      if ca[aa]<0:continue
      for sa in range(4):
        tiers=profiles[aa][sa]
        if tiers:
          tt=tuple((int(q),int(w)) for q,w in tiers);aprof[(aa,sa)]=tt;qa_values.update(q for q,_ in tt)
    qa_values=sorted(qa_values);K=counter.ceil_div(d-16*g+16,4);tq=(d*d+16*d+(32 if g==0 else 0))//8
    v47=refined=0; strict=0; visited=0
    for c in range(h+1):
      jbc=joint[a.b][c];active=[];qkeys=set()
      for sbc in range(8):
       for r in (0,1):
        hist={int(q):int(w) for q,w in jbc[sbc][r].items() if int(w) and int(q)<=tq}
        if hist: active.append((sbc,r,hist));qkeys.update(hist)
      if not active:continue
      c3=counter.component3(d,a.b,c)
      if c3<0:continue
      old_intervals=hd.interval_table(proj,a.b,c,qkeys)
      points=hd.x4_points(h16,h,g,a.b,c)
      prepared=[]
      for sbc,r,hist in active:
       old_weight={};new_weight={}
       for qa in qa_values:
        if qa>tq: old_weight[qa]=new_weight[qa]=0;continue
        xs=[x4 for x4,cap in points[r] if cap>=qa]
        ow=nw=0
        for qbc,mult in hist.items():
         if qa+qbc>tq:continue
         oc=hd.count_intersection(counter,xs,d=d,g=g,tint=old_intervals.get(qbc),q=qa+qbc)
         st=support.support_t_interval(b=a.b,c=c,support=sbc,qbc=qbc)
         # support-qBC is a safe refinement of the integer projected t interval.
         oi=old_intervals.get(qbc)
         req(oi is not None,"support interval exists outside V47 integer interval")
         req(oi[0]<=st[0]<=st[1]<=oi[1],"support interval escaped V47 integer interval")
         nc=hd.count_intersection(counter,xs,d=d,g=g,tint=st,q=qa+qbc)
         req(nc<=oc,"support-qBC weakened V47 x4 intersection")
         ow+=mult*oc;nw+=mult*nc
        old_weight[qa]=ow;new_weight[qa]=nw
       prepared.append((sbc,r,old_weight,new_weight))
      for aa in range(h+1):
       if ca[aa]<0:continue
       srem=min(16,d)+ca[aa]+c3;ec={}
       for support_count in range(11):
        es=bnd.eligible_e(counter,d,g,h,aa,a.b,c,support_count,srem,K)
        if es: ec[support_count]=len(es)
       for sbc,r,ow,nw in prepared:
        for sa in range(4):
         tiers=aprof.get((aa,sa));ne=ec.get(sbc+sa)
         if tiers is None or ne is None:continue
         for qa,va in tiers:
          x=ow[qa]*va*ne;y=nw[qa]*va*ne;v47+=x;refined+=y;strict+=int(y<x);visited+=1
    req(refined<=v47,"aggregate refinement order")
    out={"schema":"STAGE32_32_01_178_V47_SUPPORT_QBC_INTERSECTION_UNIT_V1","status":"EXACT_UNIT_COMPLETE_ZERO_MAIN_CREDIT",
      "target":{"row_index":a.row_index,"row_id":row_id,"g":g,"d":d,"band_position":band,"b":a.b},
      "source_locks":{"v47_exact_head":v["source_exact_head"],"v47_helper_blob_sha1":v["helper_blob_sha1"],
        "support_qbc_worker_blob_sha1":sp["worker_blob_sha1"],"hpadj22_source_head":v["hpadj22_source_head"]},
      "result":{"v47_joint_survivors":str(v47),"v47_support_qbc_joint_survivors":str(refined),
        "exact_incremental_saving_vs_v47":str(v47-refined),"strict_weighted_cells":strict,"visited_weighted_cells":visited},
      "semantics":{"same_population_v47_replacement":True,"additive_subtraction":False,"statistical_independence":False,
        "uncovered_v47_population_unchanged_by_consumer":True,"main_consumption_performed":False},
      "timing":{"wall_seconds":time.perf_counter()-started},
      "firewalls":{"main_credit_changed":False,"theorem_credit_changed":False,"endpoint_credit_changed":False,"merge":False}}
    out["canonical_sha256_without_this_field"]=canon(out)
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print("V47_SUPPORT_QBC_UNIT="+json.dumps(out["result"],sort_keys=True))

if __name__=="__main__":main()
