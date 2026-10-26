#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
HELPER=ROOT/"stages/stage32/management/grf04-hpadj22-joint/benchmark_grf04_hpadj22_highd_bchunk.py"
HELPER_BLOB="99eef03657b07eb5cf86be8d880050fd8aa2d13b"
SOURCE_HEAD="4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
LEGACY_ROW_WORKER_BLOBS=("c9fbf71242581f096718ebf0dbc9ac88878c91f1",)
ROW_SCHEMA="STAGE32_MAIN_V46_GRF04_HPADJ22_FULL178_ROW_CHUNK_V1"
CSHARD_SCHEMA="STAGE32_MAIN_V46_GRF04_HPADJ22_FULL178_ROW_CSHARD_V1"
PARENT_SCHEMA="STAGE32_MAIN_V46_GRF04_HPADJ22_FULL178_PARENT_V2_CSHARD_RESUME"
CSHARD_WIDTH=8
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


def c_ranges_for_h(h:int,width:int=CSHARD_WIDTH):
    req(h>=0 and width>0,"invalid c-shard geometry")
    out=[]
    c0=0
    while c0<=h:
        c1=min(h,c0+width-1)
        out.append((c0,c1));c0=c1+1
    req(out and out[0][0]==0 and out[-1][1]==h,"c-shard endpoint drift")
    flat=[c for a,b in out for c in range(a,b+1)]
    req(flat==list(range(h+1)),"c-shard gaps/overlaps")
    return out


def cshard_filename(row_index:int,c0:int,c1:int)->str:
    return f"row-{row_index:03d}-c{c0:03d}-{c1:03d}.json"


def _accepted_row_blobs(worker_blob=None,worker_blobs=None):
    out=set(LEGACY_ROW_WORKER_BLOBS)
    if worker_blob: out.add(str(worker_blob))
    if worker_blobs: out.update(str(x) for x in worker_blobs)
    return out


def validate_carry(p:Path|dict,*,worker_blob=None,worker_blobs=None,band:int,chunk:int,b0:int,b1:int,row_index:int,row_id:str,g:int,d:int):
    try:d0=p if isinstance(p,dict) else json.loads(p.read_text())
    except Exception:return None
    if d0.get("schema")!=ROW_SCHEMA:return None
    if d0.get("canonical_sha256_without_this_field")!=canon(d0):return None
    t=d0.get("target",{})
    if (t.get("band_position"),t.get("chunk_position"),t.get("b_chunk"),t.get("row_index"),t.get("row_id"),t.get("g"),t.get("d")) != (band,chunk,[b0,b1],row_index,row_id,g,d):return None
    s=d0.get("source_locks",{})
    if s.get("production_worker_blob_sha1") not in _accepted_row_blobs(worker_blob,worker_blobs):return None
    if s.get("helper_blob_sha1")!=HELPER_BLOB or s.get("hpadj22_source_head")!=SOURCE_HEAD:return None
    if d0.get("firewalls",{}).get("main_pruning_credit") is not False:return None
    r=d0.get("result",{})
    try:
        if int(r.get("joint_exact_survivors",-1))>int(r.get("hpadj22_exact_survivors",-2)):return None
    except Exception:return None
    return d0


def validate_cshard(p:Path|dict,*,worker_blob:str,band:int,chunk:int,b0:int,b1:int,row_index:int,row_id:str,g:int,d:int,c0:int,c1:int,c_shard_index:int,c_shard_count:int):
    try:d0=p if isinstance(p,dict) else json.loads(p.read_text())
    except Exception:return None
    if d0.get("schema")!=CSHARD_SCHEMA:return None
    if d0.get("canonical_sha256_without_this_field")!=canon(d0):return None
    t=d0.get("target",{})
    wanted=(band,chunk,[b0,b1],row_index,row_id,g,d,[c0,c1],c_shard_index,c_shard_count)
    got=(t.get("band_position"),t.get("chunk_position"),t.get("b_chunk"),t.get("row_index"),t.get("row_id"),t.get("g"),t.get("d"),t.get("c_range"),t.get("c_shard_index"),t.get("c_shard_count"))
    if got!=wanted:return None
    s=d0.get("source_locks",{})
    if s.get("production_worker_blob_sha1")!=worker_blob:return None
    if s.get("helper_blob_sha1")!=HELPER_BLOB or s.get("hpadj22_source_head")!=SOURCE_HEAD:return None
    cov=d0.get("coverage",{})
    if cov.get("gaps")!=0 or cov.get("overlaps")!=0:return None
    if cov.get("c_values")!=list(range(c0,c1+1)):return None
    if d0.get("firewalls",{}).get("main_pruning_credit") is not False:return None
    r=d0.get("result",{})
    try:
        if int(r.get("joint_exact_survivors",-1))>int(r.get("hpadj22_exact_survivors",-2)):return None
    except Exception:return None
    return d0


def _row_static(ctx,row_index:int):
    bc,bnd,h21,h18,h16,p15,p14,counter,rows,rejected,profiles,classes_gt2,tuples_above_second=ctx
    row_id,g0,d0=rows[row_index];g,d=int(g0),int(d0);h=d//2
    qa_values=set();ca=[counter.component_a(d,aa) for aa in range(h+1)];aprof={}
    for aa in range(h+1):
        if ca[aa]<0:continue
        for sa in range(4):
            tiers=profiles[aa][sa]
            if tiers:
                tt=tuple((int(q),int(v)) for q,v in tiers)
                aprof[(aa,sa)]=tt;qa_values.update(q for q,_ in tt)
    K=counter.ceil_div(d-16*g+16,4)
    tq=(d*d+16*d+(32 if g==0 else 0))//8
    return row_id,g,d,h,sorted(qa_values),ca,aprof,K,tq


def compute_c_shard(hd,old,ctx,joint,shared_intervals,*,worker_blob,band,chunk,b0,b1,row_index,c0,c1,c_shard_index,c_shard_count):
    bc,bnd,h21,h18,h16,p15,p14,counter,rows,rejected,profiles,classes_gt2,tuples_above_second=ctx
    row_id,g,d,h,qa_values,ca,aprof,K,tq=_row_static(ctx,row_index)
    req(h>=b0,"compute_c_shard called for implicit-zero row")
    req(0<=c0<=c1<=h,"c-shard outside row domain")
    expected=c_ranges_for_h(h)
    monolithic=(c_shard_index==0 and c_shard_count==1 and c0==0 and c1==h)
    if not monolithic:
        req(expected[c_shard_index]==(c0,c1) and len(expected)==c_shard_count,"c-shard identity drift")
    baseline=joint_exact=0
    tested_pairs=strict_pairs=interval_keys=weighted_cells=0
    precompute=accumulate=0.0
    t0=time.perf_counter()

    for b in range(b0,min(b1,h)+1):
      for c in range(c0,c1+1):
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
        intervals=shared_intervals[(b,c)]
        interval_keys+=sum(1 for q in qkeys if q in intervals)
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
    req(joint_exact<=baseline,"joint weakened c-shard HPADJ22 baseline")
    out={
      "schema":CSHARD_SCHEMA,"stage":32,"status":"EXACT_ROW_CSHARD_COMPLETE_ZERO_CREDIT",
      "target":{"band_position":band,"chunk_position":chunk,"b_chunk":[b0,b1],
        "row_index":row_index,"row_id":row_id,"g":g,"d":d,"c_range":[c0,c1],
        "c_shard_index":c_shard_index,"c_shard_count":c_shard_count},
      "source_locks":{"production_worker_blob_sha1":worker_blob,"helper_blob_sha1":HELPER_BLOB,
        "hpadj22_source_head":SOURCE_HEAD,"direct_count_blob_sha1":hd.DIRECT_BLOB,
        "integer_projection_verifier_blob_sha1":hd.PROJECTION_BLOB,
        "e_independence_verifier_blob_sha1":hd.E_VERIFY_BLOB},
      "coverage":{"c_values":list(range(c0,c1+1)),"gaps":0,"overlaps":0},
      "exactness":{"hpadj22_partial_exact":True,"integer_t_sublevel_contiguity_checked":True,
        "x4_intersection_exact":True,"e_independence_used":True,
        "qbc_weighted_intersection_cached_outside_a_loop":True,
        "disjoint_c_range_partition":True,"min_of_counts_used":False,"additive_subtraction":False},
      "result":{"hpadj22_exact_survivors":baseline,"joint_exact_survivors":joint_exact,
        "exact_improvement":baseline-joint_exact,"strict":joint_exact<baseline,
        "tested_unique_qA_qBC_hist_pairs":tested_pairs,"strict_unique_qA_qBC_hist_pairs":strict_pairs,
        "integer_interval_thresholds":interval_keys,"weighted_cache_cells":weighted_cells},
      "timing_seconds":{"precompute":round(precompute,6),"accumulate":round(accumulate,6),"c_shard_total":round(total,6)},
      "firewalls":{"main_pruning_credit":False,"full178_complete":False,"merge_authorized":False}
    }
    out["canonical_sha256_without_this_field"]=canon(out)
    return out


def assemble_row_from_cshards(shards,*,worker_blob,band,chunk,b0,b1,row_index,row_id,g,d):
    h=d//2;expected=c_ranges_for_h(h)
    byidx={}
    for sh in shards:
        t=sh["target"];idx=int(t["c_shard_index"])
        req(idx not in byidx,f"duplicate c-shard index row={row_index} shard={idx}")
        req(validate_cshard(sh,worker_blob=worker_blob,band=band,chunk=chunk,b0=b0,b1=b1,row_index=row_index,row_id=row_id,g=g,d=d,c0=expected[idx][0],c1=expected[idx][1],c_shard_index=idx,c_shard_count=len(expected)) is not None,f"invalid c-shard row={row_index} shard={idx}")
        byidx[idx]=sh
    req(set(byidx)==set(range(len(expected))),f"c-shard gaps row={row_index}")
    baseline=sum(int(byidx[i]["result"]["hpadj22_exact_survivors"]) for i in range(len(expected)))
    joint_total=sum(int(byidx[i]["result"]["joint_exact_survivors"]) for i in range(len(expected)))
    tested=sum(int(byidx[i]["result"]["tested_unique_qA_qBC_hist_pairs"]) for i in range(len(expected)))
    strict_pairs=sum(int(byidx[i]["result"]["strict_unique_qA_qBC_hist_pairs"]) for i in range(len(expected)))
    intervals=sum(int(byidx[i]["result"]["integer_interval_thresholds"]) for i in range(len(expected)))
    weighted=sum(int(byidx[i]["result"]["weighted_cache_cells"]) for i in range(len(expected)))
    precompute=sum(float(byidx[i]["timing_seconds"]["precompute"]) for i in range(len(expected)))
    accumulate=sum(float(byidx[i]["timing_seconds"]["accumulate"]) for i in range(len(expected)))
    total=sum(float(byidx[i]["timing_seconds"]["c_shard_total"]) for i in range(len(expected)))
    req(joint_total<=baseline,"row c-shard union weakened baseline")
    out={
      "schema":ROW_SCHEMA,"stage":32,"status":"EXACT_ROW_CHUNK_COMPLETE_ZERO_CREDIT",
      "target":{"band_position":band,"chunk_position":chunk,"b_chunk":[b0,b1],
        "row_index":row_index,"row_id":row_id,"g":g,"d":d},
      "source_locks":{"production_worker_blob_sha1":worker_blob,"helper_blob_sha1":HELPER_BLOB,
        "hpadj22_source_head":SOURCE_HEAD,
        "direct_count_blob_sha1":byidx[0]["source_locks"]["direct_count_blob_sha1"],
        "integer_projection_verifier_blob_sha1":byidx[0]["source_locks"]["integer_projection_verifier_blob_sha1"],
        "e_independence_verifier_blob_sha1":byidx[0]["source_locks"]["e_independence_verifier_blob_sha1"]},
      "exactness":{"hpadj22_partial_exact":True,"integer_t_sublevel_contiguity_checked":True,
        "x4_intersection_exact":True,"e_independence_used":True,
        "qbc_weighted_intersection_cached_outside_a_loop":True,"c_shard_union_exact":True,
        "min_of_counts_used":False,"additive_subtraction":False},
      "resume":{"c_shard_width":CSHARD_WIDTH,"c_shard_count":len(expected),"gaps":0,"overlaps":0,
        "c_ranges":[list(x) for x in expected],
        "c_shard_canonicals":[byidx[i]["canonical_sha256_without_this_field"] for i in range(len(expected))]},
      "result":{"hpadj22_exact_survivors":baseline,"joint_exact_survivors":joint_total,
        "exact_improvement":baseline-joint_total,"strict":joint_total<baseline,
        "tested_unique_qA_qBC_hist_pairs":tested,"strict_unique_qA_qBC_hist_pairs":strict_pairs,
        "integer_interval_thresholds":intervals,"weighted_cache_cells":weighted},
      "timing_seconds":{"precompute":round(precompute,6),"accumulate":round(accumulate,6),"row_total":round(total,6)},
      "firewalls":{"main_pruning_credit":False,"full178_complete":False,"merge_authorized":False}
    }
    out["canonical_sha256_without_this_field"]=canon(out)
    return out


def compute_row_monolithic(hd,old,ctx,joint,shared_intervals,*,worker_blob,band,chunk,b0,b1,row_index):
    row_id,g,d,h,*_=_row_static(ctx,row_index)
    sh=compute_c_shard(hd,old,ctx,joint,shared_intervals,worker_blob=worker_blob,band=band,chunk=chunk,b0=b0,b1=b1,row_index=row_index,c0=0,c1=h,c_shard_index=0,c_shard_count=1)
    # Construct the legacy-style row result from one full c-range pass.
    r=sh["result"]
    out={
      "schema":ROW_SCHEMA,"stage":32,"status":"EXACT_ROW_CHUNK_COMPLETE_ZERO_CREDIT",
      "target":{"band_position":band,"chunk_position":chunk,"b_chunk":[b0,b1],"row_index":row_index,"row_id":row_id,"g":g,"d":d},
      "source_locks":dict(sh["source_locks"]),
      "exactness":{"hpadj22_partial_exact":True,"integer_t_sublevel_contiguity_checked":True,"x4_intersection_exact":True,"e_independence_used":True,"qbc_weighted_intersection_cached_outside_a_loop":True,"min_of_counts_used":False,"additive_subtraction":False},
      "result":dict(r),
      "timing_seconds":{"precompute":sh["timing_seconds"]["precompute"],"accumulate":sh["timing_seconds"]["accumulate"],"row_total":sh["timing_seconds"]["c_shard_total"]},
      "firewalls":{"main_pruning_credit":False,"full178_complete":False,"merge_authorized":False}
    }
    out["canonical_sha256_without_this_field"]=canon(out)
    return out


# Backward-compatible callable name for diagnostics that still expect compute_row().
compute_row=compute_row_monolithic


def _build_shared_intervals(hd,proj,ctx,joint,b0,b1,hmax):
    shared={}
    for b in range(b0,b1+1):
      for c in range(hmax+1):
        qkeys=set();jbc=joint[b][c]
        for sbc in range(8):
          for parity in (0,1):
            hist=jbc[sbc][parity]
            if hist:qkeys.update(int(q) for q,v in hist.items() if int(v))
        shared[(b,c)]=hd.interval_table(proj,b,c,qkeys) if qkeys else {}
    return shared


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

    hd=load_helper();direct=hd.load(hd.DIRECT,hd.DIRECT_BLOB,"v46_full178_direct");proj=hd.load(hd.PROJECTION,hd.PROJECTION_BLOB,"v46_full178_projection");hd._full178_projection=proj
    req(hd.E_VERIFY.is_file() and blob(hd.E_VERIFY)==hd.E_VERIFY_BLOB,"e-independence verifier drift")
    old=direct.load_old(a.source_root);ctx=old.source_context();rows=ctx[8]
    req(len(rows)==178,"FULL178 row count drift");req(tuple(old.PLANNED[a.band_position])==BANDS[a.band_position],"band interval drift")

    a.output_dir.mkdir(parents=True,exist_ok=True);cdir=a.output_dir/"cshards";cdir.mkdir(exist_ok=True)
    expected=[i for i,(_,_,d0) in enumerate(rows) if int(d0)//2>=b0];implicit=[i for i,(_,_,d0) in enumerate(rows) if int(d0)//2<b0]
    carried_rows={};rejected_rows=[]
    if a.carry_root and a.carry_root.exists():
      byname={}
      for p in a.carry_root.rglob("row-???.json"):byname.setdefault(p.name,[]).append(p)
      for i in expected:
        row_id,g0,d0=rows[i];good=[]
        for p in byname.get(f"row-{i:03d}.json",[]):
          d=validate_carry(p,worker_blob=a.expected_worker_blob,band=a.band_position,chunk=a.chunk_position,b0=b0,b1=b1,row_index=i,row_id=str(row_id),g=int(g0),d=int(d0))
          if d is not None:good.append((p,d))
          else:rejected_rows.append(str(p))
        req(len(good)<=1,f"duplicate valid carry row {i}")
        if good:
          carried_rows[i]=good[0][1];(a.output_dir/f"row-{i:03d}.json").write_text(json.dumps(good[0][1],sort_keys=True,separators=(",",":"))+"\n")

    t0=time.perf_counter();joint=ctx[0].build_joint_bc_shard(old.HMAX,b0,b1);build_s=time.perf_counter()-t0
    ti=time.perf_counter();shared_intervals=_build_shared_intervals(hd,proj,ctx,joint,b0,b1,old.HMAX);interval_build_s=time.perf_counter()-ti
    completed=dict(carried_rows);carried_cshards=new_cshards=0
    for i in expected:
      if i in completed:continue
      row_id,g0,d0=rows[i];g,d=int(g0),int(d0);ranges=c_ranges_for_h(d//2);shards=[]
      for si,(c0,c1) in enumerate(ranges):
        found=None
        if a.carry_root and a.carry_root.exists():
          candidates=list(a.carry_root.rglob(cshard_filename(i,c0,c1)));good=[]
          for p in candidates:
            q=validate_cshard(p,worker_blob=a.expected_worker_blob,band=a.band_position,chunk=a.chunk_position,b0=b0,b1=b1,row_index=i,row_id=str(row_id),g=g,d=d,c0=c0,c1=c1,c_shard_index=si,c_shard_count=len(ranges))
            if q is not None:good.append(q)
          req(len(good)<=1,f"duplicate valid carry c-shard row={i} shard={si}")
          if good:found=good[0]
        if found is None:
          found=compute_c_shard(hd,old,ctx,joint,shared_intervals,worker_blob=a.expected_worker_blob,band=a.band_position,chunk=a.chunk_position,b0=b0,b1=b1,row_index=i,c0=c0,c1=c1,c_shard_index=si,c_shard_count=len(ranges));new_cshards+=1
          p=cdir/cshard_filename(i,c0,c1);tmp=p.with_suffix(".tmp");tmp.write_text(json.dumps(found,sort_keys=True,separators=(",",":"))+"\n");tmp.replace(p)
          print("FULL178_CSHARD="+json.dumps({"band":a.band_position,"chunk":a.chunk_position,"row":i,"c_range":[c0,c1],"canonical":found["canonical_sha256_without_this_field"]},sort_keys=True),flush=True)
        else:
          carried_cshards+=1;(cdir/cshard_filename(i,c0,c1)).write_text(json.dumps(found,sort_keys=True,separators=(",",":"))+"\n")
        shards.append(found)
      row=assemble_row_from_cshards(shards,worker_blob=a.expected_worker_blob,band=a.band_position,chunk=a.chunk_position,b0=b0,b1=b1,row_index=i,row_id=str(row_id),g=g,d=d)
      p=a.output_dir/f"row-{i:03d}.json";tmp=p.with_suffix(".tmp");tmp.write_text(json.dumps(row,sort_keys=True,separators=(",",":"))+"\n");tmp.replace(p);completed[i]=row

    req(set(completed)==set(expected),"parent row completion drift")
    baseline=sum(int(completed[i]["result"]["hpadj22_exact_survivors"]) for i in expected);joint_total=sum(int(completed[i]["result"]["joint_exact_survivors"]) for i in expected);req(joint_total<=baseline,"parent joint weakened baseline")
    manifest={"schema":PARENT_SCHEMA,"stage":32,"status":"EXACT_PARENT_COMPLETE_ZERO_CREDIT","parent":{"band_position":a.band_position,"chunk_position":a.chunk_position,"b_chunk":[b0,b1]},"source_locks":{"production_worker_blob_sha1":a.expected_worker_blob,"accepted_legacy_row_worker_blob_sha1":list(LEGACY_ROW_WORKER_BLOBS),"helper_blob_sha1":HELPER_BLOB,"hpadj22_source_head":SOURCE_HEAD},"coverage":{"expected_computed_rows":expected,"implicit_zero_rows":implicit,"computed_row_count":len(expected),"implicit_zero_row_count":len(implicit),"carried_validated_row_count":len(carried_rows),"newly_assembled_row_count":len(expected)-len(carried_rows),"carried_validated_c_shard_count":carried_cshards,"newly_computed_c_shard_count":new_cshards,"rejected_carry_count":len(rejected_rows),"gaps":0,"overlaps":0},"result":{"hpadj22_exact_survivors":baseline,"joint_exact_survivors":joint_total,"exact_improvement":baseline-joint_total,"strict":joint_total<baseline},"timing_seconds":{"joint_bc_build":round(build_s,6),"shared_integer_interval_build":round(interval_build_s,6)},"row_canonicals":[{"row_index":i,"canonical":completed[i]["canonical_sha256_without_this_field"]} for i in expected],"firewalls":{"main_pruning_credit":False,"full178_complete":False,"merge_authorized":False}}
    manifest["canonical_sha256_without_this_field"]=canon(manifest);(a.output_dir/"PARENT-COMPLETE.json").write_text(json.dumps(manifest,sort_keys=True,separators=(",",":"))+"\n")

if __name__=="__main__":main()
