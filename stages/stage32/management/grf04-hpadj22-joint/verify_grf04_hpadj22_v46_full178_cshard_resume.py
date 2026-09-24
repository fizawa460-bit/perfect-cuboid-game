#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys,tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
WORKER=HERE/"run_grf04_hpadj22_full178_parent_cshard.py"
WRAPPER=HERE/"run_grf04_hpadj22_full178_parent_window.py"
AGGREGATOR=HERE/"aggregate_grf04_hpadj22_full178_windowed.py"
SNAPSHOT_BUILDER=HERE/"build_grf04_hpadj22_full178_recovery_snapshot.py"
RUNKEY=HERE/"runkeys/V46-GRF04-HPADJ22-FULL178.json"
ROW65=HERE/"GRF04-HPADJ22-V46-FULL178-B4-C0-W1-ROW065.json"
WORKER_BLOB="611300610f8300f919c60ff1b0a234fd90d30ec3"
WRAPPER_BLOB="8592f978538fd4bc8e7091d248a52084382d8962"
AGGREGATOR_BLOB="f52ec28e397f2e6d9e10aa4a8b9b4c8263eb063e"
SNAPSHOT_BUILDER_BLOB="75f38ece92d2aa7b218c3a1dc3150ea3764c4d3e"
LEGACY_WORKER_BLOB="c9fbf71242581f096718ebf0dbc9ac88878c91f1"
ROW65_CANONICAL="df73e851b80cc6a8b44cf6228433ad85b3c5a23bd8fa0e2c4eb26d221759f172"


def req(v,m):
    if not v:raise SystemExit("FAIL: "+m)


def blob(p:Path)->str:
    b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()


def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def load_worker():
    req(blob(WORKER)==WORKER_BLOB,"worker blob drift")
    req(blob(WRAPPER)==WRAPPER_BLOB,"wrapper blob drift")
    req(blob(AGGREGATOR)==AGGREGATOR_BLOB,"aggregator blob drift")
    req(blob(SNAPSHOT_BUILDER)==SNAPSHOT_BUILDER_BLOB,"recovery snapshot builder blob drift")
    spec=importlib.util.spec_from_file_location("v46_full178_cshard_worker",WORKER);req(spec and spec.loader,"cannot load worker")
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m);return m


def load_snapshot_builder():
    req(blob(SNAPSHOT_BUILDER)==SNAPSHOT_BUILDER_BLOB,"recovery snapshot builder blob drift")
    spec=importlib.util.spec_from_file_location("v46_full178_recovery_snapshot",SNAPSHOT_BUILDER)
    req(spec and spec.loader,"cannot load recovery snapshot builder")
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
    return m

def build_shared_for_row(w,hd,proj,ctx,joint,b0,b1,h):
    out={}
    for b in range(b0,b1+1):
        for c in range(h+1):
            qkeys=set();jbc=joint[b][c]
            for sbc in range(8):
                for parity in (0,1):
                    hist=jbc[sbc][parity]
                    if hist:qkeys.update(int(q) for q,v in hist.items() if int(v))
            out[(b,c)]=hd.interval_table(proj,b,c,qkeys) if qkeys else {}
    return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--source-root",type=Path,required=True);a=ap.parse_args()
    w=load_worker();snapshot_builder=load_snapshot_builder();req(w.CSHARD_WIDTH==8,"c-shard width drift")
    for h in range(0,513):
        rr=w.c_ranges_for_h(h);flat=[c for x,y in rr for c in range(x,y+1)]
        req(flat==list(range(h+1)),f"c-shard coverage drift h={h}")
    req(len(w.c_ranges_for_h(82))==11 and w.c_ranges_for_h(82)[-1]==(80,82),"row65 partition drift")

    key=json.loads(RUNKEY.read_text());req(key["schema"]=="STAGE32_MAIN_V46_GRF04_HPADJ22_FULL178_RUNKEY_V3_CSHARD_RESUME","runkey schema drift")
    generation=int(key["generation"]);armed=bool(key["armed"])
    if generation==13:
        req(armed is False,"repair generation13 must remain disarmed")
    else:
        req(generation>=14 and armed is True,"post-audit execution generation must be >=14 and armed")
        auth=key["authorization"]
        req(auth["hostile_audit_pass_exact_head"]=="7424625b9280f790e2f5723be8932c6b2795fdad","generation14 hostile-audit PASS head drift")
        req(auth["next_heavy_arm_requires_hostile_audit_pass"] is True,"hostile-audit arm gate drift")
        req(key["retained_local_rows"]["recompute_forbidden"] is True,"retained local rows must remain recompute-forbidden")
    req(key["source_locks"]["recovery_snapshot_builder_blob_sha1"]==SNAPSHOT_BUILDER_BLOB,"runkey recovery snapshot builder lock drift")
    req(key["resource_preflight"]["artifact_count_upper_bound"]==98,"artifact upper bound must include 96 parents + snapshot + aggregate")
    req(key["resume_contract"]["recovery_snapshot_missing_artifacts_nonfatal"] is True,"missing-artifact snapshot contract drift")
    req(key["resume_contract"]["recovery_snapshot_inventory_replayable"] is True,"replayable inventory contract drift")
    g13=key["generation13_salvage"]
    req((g13["run_id"],g13["discovered_artifact_count"],g13["valid_row_certificates"],g13["complete_parent_windows"],g13["invalid_row_certificates"],g13["valid_c_shard_certificates"])==(35559431762,35,795,4,0,0),"generation13 salvage counts drift")
    req(g13["validated_precedence_union_windows"]==96 and g13["validated_precedence_union_rows"]==1302 and g13["canonical_conflicts"]==0,"precedence union drift")

    row65=json.loads(ROW65.read_text());req(row65.get("canonical_sha256_without_this_field")==ROW65_CANONICAL==canon(row65),"row65 canonical drift")
    accepted=w.validate_carry(row65,worker_blob=WORKER_BLOB,worker_blobs=(LEGACY_WORKER_BLOB,),band=4,chunk=0,b0=48,b1=50,row_index=65,row_id="g0-d164",g=0,d=164)
    req(accepted is not None,"legacy retained row65 no longer accepted")

    with tempfile.TemporaryDirectory() as td:
        recovery_root=Path(td)
        partial_dir=recovery_root/snapshot_builder.artifact_name(4,0,1)
        partial_dir.mkdir(parents=True)
        (partial_dir/"row-065.json").write_text(ROW65.read_text())
        snap1=snapshot_builder.build_snapshot(recovery_root,a.source_root)
        snap1_repeat=snapshot_builder.build_snapshot(recovery_root,a.source_root)
        c=snap1["coverage"]
        req(snap1["status"]=="CHECKPOINTED_INCOMPLETE_ZERO_CREDIT","missing-artifact snapshot status drift")
        req(c["discovered_parent_artifacts"]==1 and c["missing_parent_windows"]==95,"missing parent inventory drift")
        req(c["partial_parent_windows"]==1 and c["rejected_parent_windows"]==0,"partial parent inventory drift")
        req(c["validated_row_certificates"]==1 and c["validated_c_shard_certificates"]==0,"validated carry inventory drift")
        req([4,0,1] in snap1["parent_status"]["partial"],"partial parent identity missing")
        req(snap1["parent_inventory_commitment_sha256"]==snap1_repeat["parent_inventory_commitment_sha256"],"recovery inventory commitment nondeterministic")
        req(snap1["canonical_sha256_without_this_field"]==snap1_repeat["canonical_sha256_without_this_field"],"recovery snapshot canonical nondeterministic")
        (partial_dir/"row-066.json").write_text(ROW65.read_text())
        snap_bad=snapshot_builder.build_snapshot(recovery_root,a.source_root)
        cb=snap_bad["coverage"]
        req(cb["missing_parent_windows"]==95 and cb["rejected_parent_windows"]==1,"rejected parent inventory drift")
        req(cb["rejected_row_files"]==1 and [4,0,1] in snap_bad["parent_status"]["rejected"],"rejected row identity not surfaced")
        req(snap_bad["status"]=="CHECKPOINTED_INCOMPLETE_ZERO_CREDIT","rejected carry snapshot must stay zero-credit incomplete")

    hd=w.load_helper();direct=hd.load(hd.DIRECT,hd.DIRECT_BLOB,"v46_full178_direct");proj=hd.load(hd.PROJECTION,hd.PROJECTION_BLOB,"v46_full178_projection");hd._full178_projection=proj
    req(hd.E_VERIFY.is_file() and w.blob(hd.E_VERIFY)==hd.E_VERIFY_BLOB,"e-independence verifier drift")
    old=direct.load_old(a.source_root);ctx=old.source_context();rows=ctx[8];req(len(rows)==178,"FULL178 rows drift")
    band=0;chunk=0;b0,b1=w.chunks_for_band(band)[chunk]
    candidates=[(int(d0)//2,i) for i,(_,_,d0) in enumerate(rows) if int(d0)//2>=max(b0,8)]
    req(bool(candidates),"no representative row with >=2 c-shards")
    h,row_index=min(candidates);req(len(w.c_ranges_for_h(h))>=2,"representative row did not split")
    row_id,g0,d0=rows[row_index];g,d=int(g0),int(d0)
    joint=ctx[0].build_joint_bc_shard(old.HMAX,b0,b1);shared=build_shared_for_row(w,hd,proj,ctx,joint,b0,b1,h)
    monolithic=w.compute_row_monolithic(hd,old,ctx,joint,shared,worker_blob=WORKER_BLOB,band=band,chunk=chunk,b0=b0,b1=b1,row_index=row_index)
    shards=[];ranges=w.c_ranges_for_h(h)
    for si,(c0,c1) in enumerate(ranges):
        sh=w.compute_c_shard(hd,old,ctx,joint,shared,worker_blob=WORKER_BLOB,band=band,chunk=chunk,b0=b0,b1=b1,row_index=row_index,c0=c0,c1=c1,c_shard_index=si,c_shard_count=len(ranges));req(sh["canonical_sha256_without_this_field"]==w.canon(sh),f"representative c-shard canonical drift {si}");shards.append(sh)
    union_row=w.assemble_row_from_cshards(shards,worker_blob=WORKER_BLOB,band=band,chunk=chunk,b0=b0,b1=b1,row_index=row_index,row_id=str(row_id),g=g,d=d)
    req(monolithic["result"]==union_row["result"],f"monolithic/c-shard exact result mismatch row={row_index}")
    req(union_row["resume"]["gaps"]==0 and union_row["resume"]["overlaps"]==0,"representative union coverage drift")
    failed_closed=False
    try:w.assemble_row_from_cshards(shards[:-1],worker_blob=WORKER_BLOB,band=band,chunk=chunk,b0=b0,b1=b1,row_index=row_index,row_id=str(row_id),g=g,d=d)
    except SystemExit:failed_closed=True
    req(failed_closed,"missing c-shard did not fail closed")

    print(f"PASS: c-range width=8 exact partition gaps=0 overlaps=0 for h=0..512; row65 => {len(w.c_ranges_for_h(82))} shards")
    print("PASS: generation13 35 artifacts => 795 valid rows; precedence union => 1302 carried rows, conflicts=0")
    print("PASS: retained legacy row65 accepted without recompute")
    print("PASS: recovery snapshot survives missing artifacts and inventories partial/missing/rejected carry deterministically")
    print(f"PASS: representative actual FULL178 row {row_index} h={h}: old monolithic result == c-shard union result")
    print("PASS: missing c-shard fails closed; all research-credit firewalls remain zero")

if __name__=="__main__":main()
