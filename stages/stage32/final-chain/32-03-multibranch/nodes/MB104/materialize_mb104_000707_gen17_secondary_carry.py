#!/usr/bin/env python3
from __future__ import annotations
import argparse,base64,gzip,hashlib,json,os,subprocess,tempfile,zipfile
from pathlib import Path
CERT_SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_RESIDUAL_SECONDARY_V2"
CERT_STATUS="COMPLETE_EXACT_SECONDARY_RECOVERY_ZERO_CREDIT"
AGG_SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_SECONDARY_RECOVERY_AGGREGATE_V2"
def csha(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def fetch_zip(repo,artifact_id,path):
    with path.open("wb") as f: subprocess.run(["gh","api","--method","GET",f"repos/{repo}/actions/artifacts/{int(artifact_id)}/zip"],check=True,stdout=f)
def one_json(path):
    with zipfile.ZipFile(path) as z:
        names=z.namelist(); assert len(names)==1 and names[0].endswith(".json"),names
        return z.read(names[0])
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--source",type=Path,required=True); ap.add_argument("--bundle",type=Path,required=True); ap.add_argument("--manifest",type=Path,required=True); a=ap.parse_args()
    repo=os.environ.get("GITHUB_REPOSITORY"); assert repo and os.environ.get("GH_TOKEN")
    src=json.loads(a.source.read_text()); assert src["schema"]=="STAGE32_MB104_000707_GEN17_SECONDARY_CARRY_SOURCE_V1"
    assert src["producing_execution_head"]=="4d4f48f4f69e27731444117bc83a9c9ab7d51c50" and int(src["producing_workflow_run_id"])==35548407737
    assert int(src["complete_count"])==27 and int(src["incomplete_count"])==29 and all(v is False for v in src["credit_firewall"].values())
    locks=src["producing_semantic_source_locks"]; certs=[]
    with tempfile.TemporaryDirectory() as td:
        td=Path(td)
        for row in src["complete_cells"]:
            p=int(row["primary_value"]); s=int(row["secondary_residue"]); zpath=td/f"{p}-{s}.zip"
            fetch_zip(repo,row["artifact_id"],zpath); assert hashlib.sha256(zpath.read_bytes()).hexdigest()==row["artifact_zip_digest_sha256"]
            raw=one_json(zpath); cert=json.loads(raw)
            assert cert["schema"]==CERT_SCHEMA and cert["status"]==CERT_STATUS
            assert cert["provenance"]=={"producing_generation":17,"producing_mode":"RECOVERY"} and cert["semantic_source_locks"]==locks
            assert cert["partition"]["primary_value"]==p and cert["partition"]["secondary_residue"]==s and cert["partition"]["secondary_interval"]==row["secondary_interval"] and cert["partition"]["secondary_coordinate_0based"]==61
            assert cert["result"]["complete"] is True and cert["solver"]["final_solver_result"]=="unsat" and cert["solver"]["reason"] is None
            assert cert["result"]["integral_known140_nonnegative_solution_count"]==0 and cert["result"]["primitive_known140_nonnegative_candidate_count"]==0 and cert["result"]["primitive_known140_nonnegative_candidates"]==[]
            assert all(v is False for v in cert["credit_firewall"].values())
            claimed=cert["canonical_sha256_without_this_field"]; body=dict(cert); body.pop("canonical_sha256_without_this_field"); assert csha(body)==claimed
            certs.append({"primary_value":p,"secondary_residue":s,"secondary_interval":row["secondary_interval"],"artifact_id":int(row["artifact_id"]),"artifact_zip_digest_sha256":row["artifact_zip_digest_sha256"],"certificate_file_sha256":hashlib.sha256(raw).hexdigest(),"canonical_sha256":claimed,"base64":base64.b64encode(raw).decode("ascii")})
        az=td/"aggregate.zip"; fetch_zip(repo,src["aggregate_artifact"]["id"],az); assert hashlib.sha256(az.read_bytes()).hexdigest()==src["aggregate_artifact"]["zip_digest_sha256"]
        araw=one_json(az); agg=json.loads(araw); assert agg["schema"]==AGG_SCHEMA and agg["status"]=="PARTIAL_SECONDARY_RECOVERY_NO_CREDIT"
        claimed=agg["canonical_sha256_without_this_field"]; body=dict(agg); body.pop("canonical_sha256_without_this_field"); assert csha(body)==claimed==src["aggregate_artifact"]["canonical_sha256"]
        assert agg["coverage"]["observed_residual_workunits"]==56 and agg["coverage"]["missing_workunits"]==[] and agg["coverage"]["incomplete_workunits"]==src["incomplete_cells"]
    cells={(int(r["primary_value"]),int(r["secondary_residue"])) for r in certs}; expected={(p,s) for p in [-14,-12,-8,0,4,8,12] for s in range(8)}
    assert len(cells)==27 and sorted([list(x) for x in expected-cells])==src["incomplete_cells"]
    payload={"schema":"STAGE32_MB104_000707_GEN17_COMPLETE_SECONDARY_CARRY_BUNDLE_V1","producing_generation":17,"producing_mode":"RECOVERY","producing_execution_head":src["producing_execution_head"],"producing_workflow_run_id":src["producing_workflow_run_id"],"source_locks":locks,"complete_count":27,"complete_cells":[[r["primary_value"],r["secondary_residue"]] for r in certs],"incomplete_cells":src["incomplete_cells"],"certificates":certs}
    raw=json.dumps(payload,sort_keys=True,separators=(",",":")).encode(); packed=gzip.compress(raw,mtime=0)
    env={"schema":"STAGE32_MB104_000707_GEN17_DURABLE_SECONDARY_CARRY_ENVELOPE_V1","encoding":"gzip+base64","gzip_sha256":hashlib.sha256(packed).hexdigest(),"payload_sha256":hashlib.sha256(raw).hexdigest(),"byte_length":len(raw),"compressed_byte_length":len(packed),"base64":base64.b64encode(packed).decode("ascii"),"exact_bytes_not_regenerated":True}
    a.bundle.write_text(json.dumps(env,indent=2,sort_keys=True)+"\n")
    manifest=dict(src); manifest["schema"]="STAGE32_MB104_000707_GEN17_SECONDARY_CARRY_MANIFEST_V1"; manifest["artifact_provenance"]=[{k:r[k] for k in ("primary_value","secondary_residue","secondary_interval","artifact_id","artifact_zip_digest_sha256","certificate_file_sha256","canonical_sha256")} for r in certs]; manifest["durable_bundle"]={"schema":env["schema"],"gzip_sha256":env["gzip_sha256"],"payload_sha256":env["payload_sha256"],"exact_bytes_not_regenerated":True}
    a.manifest.write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n"); print(json.dumps({"success":True,"complete":27,"incomplete":29,"payload_sha256":env["payload_sha256"],"gzip_sha256":env["gzip_sha256"]},sort_keys=True))
if __name__=="__main__": main()
