#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
HELPER=ROOT/"stages/stage32/management/grf04-hpadj22-joint/benchmark_grf04_hpadj22_highd_bchunk.py"
HELPER_BLOB="99eef03657b07eb5cf86be8d880050fd8aa2d13b"
SOURCE_HEAD="4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
ROW_SCHEMA="STAGE32_MAIN_V46_GRF04_HPADJ22_FULL178_ROW_CHUNK_V1"
PARENT_SCHEMA="STAGE32_MAIN_V46_GRF04_HPADJ22_FULL178_PARENT_V1"
BANDS=((0,11),(12,23),(24,35),(36,47),(48,59),(60,71),(72,83),(84,96))

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)

def blob(p:Path)->str:
    b=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def load_helper():
    req(blob(HELPER)==HELPER_BLOB,"high-d helper blob drift")
    spec=importlib.util.spec_from_file_location("v46_full178_helper",HELPER)
    req(spec and spec.loader,"cannot load high-d helper")
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
    return m

def chunks_for_band(pos:int):
    lo,hi=BANDS[pos];n=hi-lo+1
    q,r=divmod(n,4);out=[];cur=lo
    for i in range(4):
        w=q+(1 if i<r else 0)
        out.append((cur,cur+w-1));cur+=w
    req(cur==hi+1 and out[0][0]==lo and out[-1][1]==hi,"chunk partition drift")
    return out

def validate_carry(p:Path,*,worker_blob:str,band:int,chunk:int,b0:int,b1:int,row_index:int,row_id:str,g:int,d:int):
    try:d0=json.loads(p.read_text())
    except Exception:return None
    if d0.get("schema")!=ROW_SCHEMA:return None
    if d0.get("canonical_sha256_without_this_field")!=canon(d0):return None
    t=d0.get("target",{})
    if (t.get("band_position"),t.get("chunk_position"),t.get("b_chunk"),t.get("row_index"),t.get("row_id"),t.get("g"),t.get("d")) != (band,chunk,[b0,b1],row_index,row_id,g,d):return None
    s=d0.get("source_locks",{})
    if s.get("production_worker_blob_sha1")!=worker_blob:return None
    if s.get("helper_blob_sha1")!=HELPER_BLOB or s.get("hpadj22_source_head")!=SOURCE_HEAD:return None
    if d0.get("firewalls",{}).get("main_pruning_credit") is not False:return None
    r=d0.get("result",{})
    if int(r.get("joint_exact_survivors",-1))>int(r.get("hpadj22_exact_survivors",-2)):return None
    return d0

def compute_row(hd,old,ctx,joint,*,worker_blob,band,chunk,b0,b1,row_index):
    bc,bnd,h21,h18,h16,p15,p14,counter,rows,rejected,profiles,classes_gt2,tuples_above_second=ctx
    row_id,g0,d0=rows[row_index];g,d=int(g0),int(d0);h=d//2
    req(h>=b0,"compute_row called for implicit-zero row")
    qa_values=set();ca=[counter.component_a(d,aa) for aa in range(h+1)];aprof={}
    for aa in range(h+1):
        if ca[aa]<0:continue
        for sa in range(4):
            tiers=profiles[aa][sa]
            if tiers:
                tt=tuple((int(q),int(v)) for q,v in tiers)
                aprof[(aa,sa)]=tt;qa_values.update(q for q,_ in tt)
    qa_values=sorted(qa_values)
    K=counter.ceil_div(d-16*g+16,4)
    tq=(d*d+16*d+(32 if g==0 else 0))//8
    baseline=joint_exact=0
    tested_pairs=strict_pairs=interval_keys=weighted_cells=0
    precompute=accumulate=0.0
    t0=time.perf_counter()

    for b in range(b0,min(b1,h)+1):
      for c in range(h+1):
        jbc=joint[b][c]
        active=[];qkeys=set()
        for sbc in range(8):
          for parity in (0,1):
            hist=jbc[sbc][parity]
            if not hist:continue
            clean={int(q):int(v) for q,v in hist.items() if int(v)}
            if clean:
                active.append((sbc,parity,clean));qkeys.update(q for q in clean if q<=tq)
        if not active:continue
        c3=counter.component3(d,b,c)
        if c3<0:continue

        tp=time.perf_counter()
        intervals=hd.interval_table(hd.load(hd.PROJECTION,hd.PROJECTION_BLOB,"v46_full178_proj_tmp"),b,c,qkeys) if False else None
        # projection module is attached by caller after load; avoid repeated imports.
        intervals=hd.interval_table(hd._full178_projection,b,c,qkeys);interval_keys+=len(intervals)
        points=hd.x4_points(h16,h,g,b,c)
        eligible={};picard={}
        for parity in (0,1):
          for qa in qa_values:
            xs=[x4 for x4,cap in points[parity] if cap>=qa]
            eligible[(parity,qa)]=xs;picard[(parity,qa)]=len(xs)
        weighted={}
        for sbc,parity,hist in active:
          for qa in qa_values:
            cut=tq-qa
            if cut<0:
                weighted[(sbc,parity,qa)]=(0,0);continue
            xs=eligible[(parity,qa)];pcount=picard[(parity,qa)]
            survive=jweight=0
            for qb,vb in hist.items():
                if qb>cut:continue
                survive+=vb
                cnt=hd.count_intersection(counter,xs,d=d,g=g,tint=intervals.get(qb),q=qa+qb)
                req(cnt<=pcount,f"joint escaped Picard {(row_index,b,c,sbc,parity,qa,qb,cnt,pcount)}")
                tested_pairs+=1;strict_pairs+=int(cnt<pcount);jweight+=vb*cnt
            weighted[(sbc,parity,qa)]=(survive,jweight);weighted_cells+=1
        precompute+=time.perf_counter()-tp

        ta=time.perf_counter()
        for aa in range(h+1):
          if ca[aa]<0:continue
          srem=min(16,d)+ca[aa]+c3
          ec={}
          for support in range(11):
            es=bnd.eligible_e(counter,d,g,h,aa,b,c,support,srem,K)
            if es:
                req(all(19*d-5*int(e)>=4*d for e in es),f"eligible e lower n regression {(row_index,b,c,aa,support)}")
                ec[support]=len(es)
          if not ec:continue
          for sbc,parity,hist in active:
            for sa in range(4):
              tiers=aprof.get((aa,sa));ne=ec.get(sbc+sa)
              if tiers is None or ne is None:continue
              for qa,va in tiers:
                survive,jweight=weighted[(sbc,parity,qa)]
                baseline+=survive*va*picard[(parity,qa)]*ne
                joint_exact+=jweight*va*ne
        accumulate+=time.perf_counter()-ta
    total=time.perf_counter()-t0
    req(joint_exact<=baseline,"joint weakened partial HPADJ22 baseline")
    out={
      "schema":ROW_SCHEMA,"stage":32,"status":"EXACT_ROW_CHUNK_COMPLETE_ZERO_CREDIT",
      "target":{"band_position":band,"chunk_position":chunk,"b_chunk":[b0,b1],
        "row_index":row_index,"row_id":row_id,"g":g,"d":d},
      "source_locks":{"production_worker_blob_sha1":worker_blob,"helper_blob_sha1":HELPER_BLOB,
        "hpadj22_source_head":SOURCE_HEAD,"direct_count_blob_sha1":hd.DIRECT_BLOB,
        "integer_projection_verifier_blob_sha1":hd.PROJECTION_BLOB,
        "e_independence_verifier_blob_sha1":hd.E_VERIFY_BLOB},
      "exactness":{"hpadj22_partial_exact":True,"integer_t_sublevel_contiguity_checked":True,
        "x4_intersection_exact":True,"e_independence_used":True,
        "qbc_weighted_intersection_cached_outside_a_loop":True,
        "min_of_counts_used":False,"additive_subtraction":False},
      "result":{"hpadj22_exact_survivors":baseline,"joint_exact_survivors":joint_exact,
        "exact_improvement":baseline-joint_exact,"strict":joint_exact<baseline,
        "tested_unique_qA_qBC_hist_pairs":tested_pairs,"strict_unique_qA_qBC_hist_pairs":strict_pairs,
        "integer_interval_thresholds":interval_keys,"weighted_cache_cells":weighted_cells},
      "timing_seconds":{"precompute":round(precompute,6),"accumulate":round(accumulate,6),"row_total":round(total,6)},
      "firewalls":{"main_pruning_credit":False,"full178_complete":False,"merge_authorized":False}
    }
    out["canonical_sha256_without_this_field"]=canon(out)
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-root",type=Path,required=True)
    ap.add_argument("--band-position",type=int,required=True)
    ap.add_argument("--chunk-position",type=int,required=True)
    ap.add_argument("--output-dir",type=Path,required=True)
    ap.add_argument("--carry-root",type=Path)
    ap.add_argument("--expected-worker-blob",required=True)
    a=ap.parse_args()
    req(blob(Path(__file__))==a.expected_worker_blob,"production worker self-lock drift")
    req(0<=a.band_position<8 and 0<=a.chunk_position<4,"invalid parent identity")
    chunks=chunks_for_band(a.band_position);b0,b1=chunks[a.chunk_position]

    hd=load_helper()
    direct=hd.load(hd.DIRECT,hd.DIRECT_BLOB,"v46_full178_direct")
    proj=hd.load(hd.PROJECTION,hd.PROJECTION_BLOB,"v46_full178_projection")
    hd._full178_projection=proj
    req(hd.E_VERIFY.is_file() and blob(hd.E_VERIFY)==hd.E_VERIFY_BLOB,"e-independence verifier drift")
    old=direct.load_old(a.source_root)
    ctx=old.source_context()
    rows=ctx[8]
    req(len(rows)==178,"FULL178 row count drift")
    req(tuple(old.PLANNED[a.band_position])==BANDS[a.band_position],"band interval drift")

    a.output_dir.mkdir(parents=True,exist_ok=True)
    expected=[i for i,(_,_,d0) in enumerate(rows) if int(d0)//2>=b0]
    implicit=[i for i,(_,_,d0) in enumerate(rows) if int(d0)//2<b0]
    carried={};rejected_carry=[]
    if a.carry_root and a.carry_root.exists():
      byname={}
      for p in a.carry_root.rglob("row-*.json"):
        byname.setdefault(p.name,[]).append(p)
      for i in expected:
        row_id,g0,d0=rows[i]
        good=[]
        for p in byname.get(f"row-{i:03d}.json",[]):
          d=validate_carry(p,worker_blob=a.expected_worker_blob,band=a.band_position,chunk=a.chunk_position,
            b0=b0,b1=b1,row_index=i,row_id=str(row_id),g=int(g0),d=int(d0))
          if d is not None:good.append((p,d))
          else:rejected_carry.append(str(p))
        req(len(good)<=1,f"duplicate valid carry row {i}")
        if good:
          carried[i]=good[0][1]
          (a.output_dir/f"row-{i:03d}.json").write_text(json.dumps(good[0][1],sort_keys=True,separators=(",",":"))+"\n")

    t0=time.perf_counter()
    joint=ctx[0].build_joint_bc_shard(old.HMAX,b0,b1)
    build_s=time.perf_counter()-t0
    completed=dict(carried)
    for i in expected:
      if i in completed:continue
      d=compute_row(hd,old,ctx,joint,worker_blob=a.expected_worker_blob,band=a.band_position,
        chunk=a.chunk_position,b0=b0,b1=b1,row_index=i)
      p=a.output_dir/f"row-{i:03d}.json"
      tmp=p.with_suffix(".tmp")
      tmp.write_text(json.dumps(d,sort_keys=True,separators=(",",":"))+"\n")
      tmp.replace(p)
      completed[i]=d
      print("FULL178_ROW="+json.dumps({"band":a.band_position,"chunk":a.chunk_position,"row":i,
        "baseline":d["result"]["hpadj22_exact_survivors"],"joint":d["result"]["joint_exact_survivors"],
        "canonical":d["canonical_sha256_without_this_field"]},sort_keys=True),flush=True)

    req(set(completed)==set(expected),"parent row completion drift")
    baseline=sum(int(completed[i]["result"]["hpadj22_exact_survivors"]) for i in expected)
    joint_total=sum(int(completed[i]["result"]["joint_exact_survivors"]) for i in expected)
    req(joint_total<=baseline,"parent joint weakened baseline")
    manifest={
      "schema":PARENT_SCHEMA,"stage":32,"status":"EXACT_PARENT_COMPLETE_ZERO_CREDIT",
      "parent":{"band_position":a.band_position,"chunk_position":a.chunk_position,"b_chunk":[b0,b1]},
      "source_locks":{"production_worker_blob_sha1":a.expected_worker_blob,"helper_blob_sha1":HELPER_BLOB,
        "hpadj22_source_head":SOURCE_HEAD},
      "coverage":{"expected_computed_rows":expected,"implicit_zero_rows":implicit,
        "computed_row_count":len(expected),"implicit_zero_row_count":len(implicit),
        "carried_validated_row_count":len(carried),"newly_computed_row_count":len(expected)-len(carried),
        "rejected_carry_count":len(rejected_carry),"gaps":0,"overlaps":0},
      "result":{"hpadj22_exact_survivors":baseline,"joint_exact_survivors":joint_total,
        "exact_improvement":baseline-joint_total,"strict":joint_total<baseline},
      "timing_seconds":{"joint_bc_build":round(build_s,6)},
      "row_canonicals":[{"row_index":i,"canonical":completed[i]["canonical_sha256_without_this_field"]} for i in expected],
      "firewalls":{"main_pruning_credit":False,"full178_complete":False,"merge_authorized":False}
    }
    manifest["canonical_sha256_without_this_field"]=canon(manifest)
    (a.output_dir/"PARENT-COMPLETE.json").write_text(json.dumps(manifest,sort_keys=True,separators=(",",":"))+"\n")
    print("FULL178_PARENT="+json.dumps({"band":a.band_position,"chunk":a.chunk_position,
      "baseline":baseline,"joint":joint_total,"improvement":baseline-joint_total,
      "rows":len(expected),"carried":len(carried),"canonical":manifest["canonical_sha256_without_this_field"]},sort_keys=True))

if __name__=="__main__":main()
