#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.util,json,os,re,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
WORKER=HERE/"run_grf04_hpadj22_full178_parent_cshard.py"
WORKER_BLOB="611300610f8300f919c60ff1b0a234fd90d30ec3"
LEGACY_ROW_WORKER_BLOBS=("c9fbf71242581f096718ebf0dbc9ac88878c91f1",)
WRAPPER_BLOB="8592f978538fd4bc8e7091d248a52084382d8962"
WINDOW_SCHEMA="STAGE32_MAIN_V46_GRF04_HPADJ22_FULL178_PARENT_WINDOW_V3_CSHARD_RESUME"
SNAPSHOT_SCHEMA="STAGE32_MAIN_V46_GRF04_HPADJ22_FULL178_RECOVERY_SNAPSHOT_V4_INVENTORY"
ROW_WINDOWS=((0,59),(60,119),(120,177))
ARTIFACT_PREFIX="stage32-main-v46-grf04-hpadj22-full178-window-"
ARTIFACT_RE=re.compile(r"^"+re.escape(ARTIFACT_PREFIX)+r"(\d+)-(\d+)-(\d+)$")
ROW_RE=re.compile(r"^row-(\d{3})\.json$")
CSHARD_RE=re.compile(r"^row-(\d{3})-c(\d{3})-(\d{3})\.json$")

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)

def blob(p:Path)->str:
    b=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def digest(value)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def load_worker():
    req(blob(WORKER)==WORKER_BLOB,"c-shard worker blob drift")
    spec=importlib.util.spec_from_file_location("v46_full178_recovery_worker",WORKER)
    req(spec and spec.loader,"cannot load c-shard worker")
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
    return m

def artifact_name(band:int,chunk:int,window:int)->str:
    return f"{ARTIFACT_PREFIX}{band}-{chunk}-{window}"

def _load_json(path:Path):
    try:return json.loads(path.read_text())
    except Exception:return None

def _valid_manifest(d,w,*,band,chunk,window,b0,b1,r0,r1,expected,implicit,valid_rows):
    if not isinstance(d,dict) or d.get("schema")!=WINDOW_SCHEMA:return False
    if d.get("canonical_sha256_without_this_field")!=canon(d):return False
    s=d.get("source_locks",{})
    if s.get("execution_wrapper_blob_sha1")!=WRAPPER_BLOB:return False
    if s.get("row_compute_worker_blob_sha1")!=WORKER_BLOB:return False
    if set(s.get("accepted_legacy_row_worker_blob_sha1",[]))!=set(LEGACY_ROW_WORKER_BLOBS):return False
    if s.get("helper_blob_sha1")!=w.HELPER_BLOB or s.get("hpadj22_source_head")!=w.SOURCE_HEAD:return False
    p=d.get("parent",{})
    if (p.get("band_position"),p.get("chunk_position"),p.get("row_window_position"),p.get("b_chunk"),p.get("row_window"))!=(band,chunk,window,[b0,b1],[r0,r1]):return False
    c=d.get("coverage",{})
    if c.get("gaps")!=0 or c.get("overlaps")!=0:return False
    if c.get("expected_computed_rows")!=expected or c.get("implicit_zero_rows")!=implicit:return False
    if int(c.get("computed_row_count",-1))!=len(expected) or int(c.get("implicit_zero_row_count",-1))!=len(implicit):return False
    if set(valid_rows)!=set(expected):return False
    listed=d.get("row_canonicals",[])
    if listed!=[{"row_index":i,"canonical":valid_rows[i]["canonical_sha256_without_this_field"]} for i in expected]:return False
    rb=sum(int(valid_rows[i]["result"]["hpadj22_exact_survivors"]) for i in expected)
    rj=sum(int(valid_rows[i]["result"]["joint_exact_survivors"]) for i in expected)
    result=d.get("result",{})
    if int(result.get("hpadj22_exact_survivors",-1))!=rb or int(result.get("joint_exact_survivors",-1))!=rj:return False
    return rj<=rb

def build_snapshot(parents_root:Path,source_root:Path):
    w=load_worker()
    hd=w.load_helper()
    direct=hd.load(hd.DIRECT,hd.DIRECT_BLOB,"v46_full178_direct")
    old=direct.load_old(source_root)
    ctx=old.source_context();rows=ctx[8]
    req(len(rows)==178,"FULL178 row count drift")

    observed_dirs={}
    unexpected=[]
    if parents_root.exists():
        for p in sorted(x for x in parents_root.iterdir() if x.is_dir()):
            m=ARTIFACT_RE.match(p.name)
            if not m:
                unexpected.append(p.name);continue
            key=tuple(int(x) for x in m.groups())
            if key in observed_dirs:
                unexpected.append(p.name);continue
            observed_dirs[key]=p

    parent_records=[]
    valid_carry_stream=[]
    complete_ids=[];partial_ids=[];missing_ids=[];rejected_ids=[]
    total_valid_rows=total_valid_cshards=0
    total_rejected_rows=total_rejected_cshards=total_rejected_manifests=0

    for band in range(8):
      for chunk in range(4):
        b0,b1=w.chunks_for_band(band)[chunk]
        for window,(r0,r1) in enumerate(ROW_WINDOWS):
            key=(band,chunk,window);identity=[band,chunk,window]
            expected=[i for i,(_,_,d0) in enumerate(rows) if r0<=i<=r1 and int(d0)//2>=b0]
            implicit=[i for i,(_,_,d0) in enumerate(rows) if r0<=i<=r1 and int(d0)//2<b0]
            p=observed_dirs.get(key)
            if p is None:
                missing_ids.append(identity)
                parent_records.append({
                    "identity":identity,"artifact_name":artifact_name(*key),"status":"MISSING",
                    "expected_computed_row_count":len(expected),"implicit_zero_row_count":len(implicit),
                    "valid_rows":[],"missing_rows":expected,"valid_c_shards":[],"rejected_files":[]
                })
                continue

            valid_rows={};row_rejects=[];cvalid={};c_rejects=[]
            row_candidates={}
            for rp in sorted(p.rglob("row-???.json")):
                m=ROW_RE.match(rp.name)
                if not m:continue
                ri=int(m.group(1));row_candidates.setdefault(ri,[]).append(rp)
            for ri,paths in sorted(row_candidates.items()):
                good=[]
                if ri in expected:
                    row_id,g0,d0=rows[ri]
                    for rp in paths:
                        q=w.validate_carry(rp,worker_blob=WORKER_BLOB,worker_blobs=LEGACY_ROW_WORKER_BLOBS,
                            band=band,chunk=chunk,b0=b0,b1=b1,row_index=ri,row_id=str(row_id),g=int(g0),d=int(d0))
                        if q is not None:good.append((rp,q))
                        else:row_rejects.append({"path":str(rp.relative_to(p)),"row_index":ri,"reason":"VALIDATION_FAILED"})
                else:
                    row_rejects.extend({"path":str(rp.relative_to(p)),"row_index":ri,"reason":"UNEXPECTED_ROW_IDENTITY"} for rp in paths)
                if len(good)==1:
                    valid_rows[ri]=good[0][1]
                elif len(good)>1:
                    row_rejects.extend({"path":str(rp.relative_to(p)),"row_index":ri,"reason":"DUPLICATE_VALID_ROW"} for rp,_ in good)

            shard_candidates={}
            for sp in sorted(p.rglob("row-???-c???-???.json")):
                m=CSHARD_RE.match(sp.name)
                if not m:continue
                ident=tuple(int(x) for x in m.groups());shard_candidates.setdefault(ident,[]).append(sp)
            for (ri,c0,c1),paths in sorted(shard_candidates.items()):
                good=[]
                if ri in expected:
                    row_id,g0,d0=rows[ri];g,d=int(g0),int(d0);ranges=w.c_ranges_for_h(d//2)
                    try:si=ranges.index((c0,c1))
                    except ValueError:si=-1
                    if si>=0:
                        for sp in paths:
                            q=w.validate_cshard(sp,worker_blob=WORKER_BLOB,band=band,chunk=chunk,b0=b0,b1=b1,
                                row_index=ri,row_id=str(row_id),g=g,d=d,c0=c0,c1=c1,c_shard_index=si,c_shard_count=len(ranges))
                            if q is not None:good.append((sp,q))
                            else:c_rejects.append({"path":str(sp.relative_to(p)),"identity":[ri,c0,c1],"reason":"VALIDATION_FAILED"})
                    else:
                        c_rejects.extend({"path":str(sp.relative_to(p)),"identity":[ri,c0,c1],"reason":"UNEXPECTED_C_RANGE"} for sp in paths)
                else:
                    c_rejects.extend({"path":str(sp.relative_to(p)),"identity":[ri,c0,c1],"reason":"UNEXPECTED_ROW_IDENTITY"} for sp in paths)
                if len(good)==1:
                    q=good[0][1];cvalid[(ri,c0,c1)]=q
                elif len(good)>1:
                    c_rejects.extend({"path":str(sp.relative_to(p)),"identity":[ri,c0,c1],"reason":"DUPLICATE_VALID_CSHARD"} for sp,_ in good)

            manifest_paths=sorted(p.rglob("PARENT-WINDOW-COMPLETE.json"))
            manifest_valid=False;manifest_rejects=[]
            if len(manifest_paths)==1:
                md=_load_json(manifest_paths[0])
                manifest_valid=_valid_manifest(md,w,band=band,chunk=chunk,window=window,b0=b0,b1=b1,
                    r0=r0,r1=r1,expected=expected,implicit=implicit,valid_rows=valid_rows)
                if not manifest_valid:manifest_rejects.append({"path":str(manifest_paths[0].relative_to(p)),"reason":"VALIDATION_FAILED"})
            elif len(manifest_paths)>1:
                manifest_rejects.extend({"path":str(mp.relative_to(p)),"reason":"DUPLICATE_MANIFEST"} for mp in manifest_paths)

            rejects=row_rejects+c_rejects+manifest_rejects
            if rejects:
                status="REJECTED";rejected_ids.append(identity)
            elif manifest_valid and set(valid_rows)==set(expected):
                status="COMPLETE";complete_ids.append(identity)
            else:
                status="PARTIAL";partial_ids.append(identity)

            valid_row_items=[{"row_index":ri,"canonical":valid_rows[ri]["canonical_sha256_without_this_field"]} for ri in sorted(valid_rows)]
            valid_shard_items=[{"row_index":ri,"c_range":[c0,c1],"canonical":cvalid[(ri,c0,c1)]["canonical_sha256_without_this_field"],
                                "superseded_by_complete_row":ri in valid_rows} for ri,c0,c1 in sorted(cvalid)]
            missing_rows=[i for i in expected if i not in valid_rows]
            for x in valid_row_items:valid_carry_stream.append(["ROW",*identity,x["row_index"],x["canonical"]])
            for x in valid_shard_items:valid_carry_stream.append(["CSHARD",*identity,x["row_index"],*x["c_range"],x["canonical"]])
            total_valid_rows+=len(valid_row_items);total_valid_cshards+=len(valid_shard_items)
            total_rejected_rows+=len(row_rejects);total_rejected_cshards+=len(c_rejects);total_rejected_manifests+=len(manifest_rejects)
            parent_records.append({
                "identity":identity,"artifact_name":artifact_name(*key),"status":status,
                "manifest_valid":manifest_valid,
                "expected_computed_row_count":len(expected),"implicit_zero_row_count":len(implicit),
                "valid_rows":valid_row_items,"missing_rows":missing_rows,
                "valid_c_shards":valid_shard_items,"rejected_files":rejects
            })

    req(len(parent_records)==96,"recovery parent inventory drift")
    full_complete=(len(complete_ids)==96 and not rejected_ids and not unexpected)
    out={
        "schema":SNAPSHOT_SCHEMA,"stage":32,
        "status":"GENERATION_COMPLETE" if full_complete else "CHECKPOINTED_INCOMPLETE_ZERO_CREDIT",
        "source_locks":{"cshard_worker_blob_sha1":WORKER_BLOB,"legacy_row_worker_blob_sha1":list(LEGACY_ROW_WORKER_BLOBS),
                        "helper_blob_sha1":w.HELPER_BLOB,"hpadj22_source_head":w.SOURCE_HEAD},
        "coverage":{"expected_parent_windows":96,"discovered_parent_artifacts":len(observed_dirs),
                    "complete_parent_windows":len(complete_ids),"partial_parent_windows":len(partial_ids),
                    "missing_parent_windows":len(missing_ids),"rejected_parent_windows":len(rejected_ids),
                    "validated_row_certificates":total_valid_rows,"validated_c_shard_certificates":total_valid_cshards,
                    "rejected_row_files":total_rejected_rows,"rejected_c_shard_files":total_rejected_cshards,
                    "rejected_manifests":total_rejected_manifests},
        "parent_status":{"complete":complete_ids,"partial":partial_ids,"missing":missing_ids,"rejected":rejected_ids},
        "unexpected_artifact_directories":unexpected,
        "parents":parent_records,
        "validated_carry_commitment_sha256":digest(valid_carry_stream),
        "parent_inventory_commitment_sha256":digest(parent_records),
        "firewalls":{"main_pruning_credit":False,"full178_complete":False,"theorem_credit":False,
                     "effectivity_credit":False,"receiver_credit":False,"route_credit":False,
                     "endpoint_credit":False,"merge_authorized":False}
    }
    out["canonical_sha256_without_this_field"]=canon(out)
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--parents-root",type=Path,required=True)
    ap.add_argument("--source-root",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--github-output",type=Path)
    a=ap.parse_args()
    out=build_snapshot(a.parents_root,a.source_root)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    if a.github_output:
        c=out["coverage"]
        with a.github_output.open("a") as f:
            f.write(f"complete={'true' if out['status']=='GENERATION_COMPLETE' else 'false'}\n")
            f.write(f"complete_parents={c['complete_parent_windows']}\n")
            f.write(f"row_certificates={c['validated_row_certificates']}\n")
            f.write(f"c_shard_certificates={c['validated_c_shard_certificates']}\n")
            f.write(f"missing_parents={c['missing_parent_windows']}\n")
            f.write(f"rejected_parents={c['rejected_parent_windows']}\n")
    print("FULL178_RECOVERY_SNAPSHOT="+json.dumps({
        "status":out["status"],"coverage":out["coverage"],
        "validated_carry_commitment_sha256":out["validated_carry_commitment_sha256"],
        "parent_inventory_commitment_sha256":out["parent_inventory_commitment_sha256"],
        "canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))

if __name__=="__main__":main()
