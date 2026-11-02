#!/usr/bin/env python3
from __future__ import annotations
import argparse,base64,gzip,hashlib,json,os,subprocess,tempfile,zipfile
from pathlib import Path
CERT_SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_X61_SINGLETON_PACKET_V1"
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
    src=json.loads(a.source.read_text()); assert src["schema"]=="STAGE32_MB104_000707_GEN19_X61_PACKET_CARRY_SOURCE_V1"
    assert src["producing_execution_head"]=="bc1f055cfcfa9a5249244a2d50ff13e20b9d9fb1" and int(src["producing_workflow_run_id"])==35568958576
    assert int(src["packet_count"])==29 and int(src["singleton_child_count"])==146 and int(src["expected_complete_child_count"])==123 and int(src["expected_incomplete_child_count"])==23
    assert src["exact_bytes_not_regenerated"] is True and all(v is False for v in src["credit_firewall"].values())
    locks=src["producing_semantic_source_locks"]; certs=[]; provenance=[]; complete=[]; incomplete=[]; seen=set()
    with tempfile.TemporaryDirectory() as td:
        td=Path(td)
        for row in src["packet_artifacts"]:
            p=int(row["primary_value"]); s=int(row["secondary_residue"]); key=(p,s); assert key not in seen; seen.add(key)
            zpath=td/f"{p}-{s}.zip"; fetch_zip(repo,row["artifact_id"],zpath); assert hashlib.sha256(zpath.read_bytes()).hexdigest()==row["artifact_zip_digest_sha256"]
            raw=one_json(zpath); cert=json.loads(raw)
            assert cert["schema"]==CERT_SCHEMA and cert["provenance"]=={"producing_generation":19,"producing_mode":"RECOVERY"} and cert["semantic_source_locks"]==locks
            assert int(cert["partition"]["primary_value"])==p and int(cert["partition"]["secondary_residue"])==s
            claimed=cert["canonical_sha256_without_this_field"]; body=dict(cert); body.pop("canonical_sha256_without_this_field"); assert csha(body)==claimed
            cc=0
            for child in cert["children"]:
                rec={"primary_value":p,"secondary_residue":s,"fixed_x61_value":int(child["fixed_x61_value"])}
                if child["result"]["complete"]:
                    assert child["status"]=="COMPLETE_EXACT_X61_SINGLETON_ZERO_CREDIT" and child["solver"]["final_solver_result"]=="unsat" and child["solver"]["reason"] is None
                    assert child["result"]["integral_known140_nonnegative_solution_count"]==0 and child["result"]["primitive_known140_nonnegative_candidate_count"]==0 and child["result"]["primitive_known140_nonnegative_candidates"]==[]
                    complete.append(rec); cc+=1
                else:
                    assert child["status"]=="PARTIAL_UNKNOWN_NO_CREDIT" and child["solver"]["final_solver_result"]=="unknown" and child["solver"]["reason"]=="timeout"
                    rec.update({"solver_result":"unknown","reason":"timeout"}); incomplete.append(rec)
            assert cc==int(cert["result"]["complete_child_count"]) and int(cert["result"]["child_count"])==len(cert["children"]) and cert["result"]["complete"] is (cc==len(cert["children"]))
            assert all(v is False for v in cert["credit_firewall"].values())
            fsha=hashlib.sha256(raw).hexdigest(); provenance.append({"primary_value":p,"secondary_residue":s,"artifact_id":int(row["artifact_id"]),"artifact_zip_digest_sha256":row["artifact_zip_digest_sha256"],"certificate_file_sha256":fsha,"canonical_sha256":claimed,"child_count":len(cert["children"]),"complete_child_count":cc})
            certs.append({"primary_value":p,"secondary_residue":s,"certificate_file_sha256":fsha,"canonical_sha256":claimed,"base64":base64.b64encode(raw).decode("ascii")})
    provenance.sort(key=lambda r:(r["primary_value"],r["secondary_residue"])); certs.sort(key=lambda r:(r["primary_value"],r["secondary_residue"])); complete.sort(key=lambda r:(r["primary_value"],r["secondary_residue"],r["fixed_x61_value"])); incomplete.sort(key=lambda r:(r["primary_value"],r["secondary_residue"],r["fixed_x61_value"]))
    assert len(certs)==29 and sum(r["child_count"] for r in provenance)==146 and len(complete)==123 and len(incomplete)==23
    payload={"schema":"STAGE32_MB104_000707_GEN19_X61_PACKET_CARRY_BUNDLE_V1","producing_generation":19,"producing_mode":"RECOVERY","producing_execution_head":src["producing_execution_head"],"producing_workflow_run_id":src["producing_workflow_run_id"],"source_locks":locks,"packet_count":29,"singleton_child_count":146,"complete_child_count":123,"incomplete_child_count":23,"complete_children":complete,"incomplete_children":incomplete,"certificates":certs}
    raw=json.dumps(payload,sort_keys=True,separators=(",",":")).encode(); packed=gzip.compress(raw,mtime=0)
    env={"schema":"STAGE32_MB104_000707_GEN19_X61_DURABLE_PACKET_CARRY_ENVELOPE_V1","encoding":"gzip+base64","gzip_sha256":hashlib.sha256(packed).hexdigest(),"payload_sha256":hashlib.sha256(raw).hexdigest(),"byte_length":len(raw),"compressed_byte_length":len(packed),"base64":base64.b64encode(packed).decode("ascii"),"exact_bytes_not_regenerated":True}
    a.bundle.write_text(json.dumps(env,indent=2,sort_keys=True)+"\n")
    manifest=dict(src); manifest["schema"]="STAGE32_MB104_000707_GEN19_X61_PACKET_CARRY_MANIFEST_V1"; manifest["artifact_provenance"]=provenance; manifest["complete_children"]=complete; manifest["incomplete_children"]=incomplete; manifest["complete_child_count"]=123; manifest["incomplete_child_count"]=23; manifest["durable_bundle"]={"schema":env["schema"],"gzip_sha256":env["gzip_sha256"],"payload_sha256":env["payload_sha256"],"exact_bytes_not_regenerated":True}
    a.manifest.write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"success":True,"packets":29,"children":146,"complete_children":123,"incomplete_children":23,"payload_sha256":env["payload_sha256"],"gzip_sha256":env["gzip_sha256"]},sort_keys=True))
if __name__=="__main__": main()
