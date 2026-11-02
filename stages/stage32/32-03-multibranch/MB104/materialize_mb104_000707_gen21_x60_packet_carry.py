#!/usr/bin/env python3
from __future__ import annotations
import argparse,base64,gzip,hashlib,json,os,subprocess,tempfile,zipfile
from pathlib import Path
PACKET_SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_X60_INTERVAL_PACKET_V1"
AGG_SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_X60_INTERVAL_AGGREGATE_V1"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def fetch_zip(repo,aid,path):
    with path.open("wb") as f: subprocess.run(["gh","api","--method","GET",f"repos/{repo}/actions/artifacts/{int(aid)}/zip"],check=True,stdout=f)
def one_json(path):
    with zipfile.ZipFile(path) as z:
        names=z.namelist(); assert len(names)==1 and names[0].endswith(".json"),names
        return z.read(names[0])
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--source",type=Path,required=True); ap.add_argument("--bundle",type=Path,required=True); ap.add_argument("--manifest",type=Path,required=True); a=ap.parse_args()
    repo=os.environ.get("GITHUB_REPOSITORY"); assert repo and os.environ.get("GH_TOKEN")
    src=json.loads(a.source.read_text()); assert src["schema"]=="STAGE32_MB104_000707_GEN21_X60_PACKET_CARRY_SOURCE_V1"
    assert src["producing_execution_head"]=="7166da4f293ab608ff200ddcef222e1c21fc6014" and int(src["producing_workflow_run_id"])==35586170075
    assert int(src["packet_count"])==23 and int(src["x60_interval_child_count"])==184 and int(src["expected_complete_interval_child_count"])==122 and int(src["expected_incomplete_interval_child_count"])==62 and int(src["expected_next_x60_singleton_child_count"])==311
    assert src["exact_bytes_not_regenerated"] is True and all(v is False for v in src["credit_firewall"].values())
    locks=src["producing_semantic_source_locks"]; certs=[]; provenance=[]; complete=[]; incomplete=[]; seen=set(); canon={}
    with tempfile.TemporaryDirectory() as td:
        td=Path(td)
        for row in src["packet_artifacts"]:
            key=(int(row["primary_value"]),int(row["secondary_residue"]),int(row["fixed_x61_value"])); assert key not in seen; seen.add(key)
            zpath=td/f"packet-{key[0]}-{key[1]}-{key[2]}.zip"; fetch_zip(repo,row["artifact_id"],zpath); assert hashlib.sha256(zpath.read_bytes()).hexdigest()==row["artifact_zip_digest_sha256"]
            raw=one_json(zpath); d=json.loads(raw); assert d["schema"]==PACKET_SCHEMA and d["provenance"]=={"producing_generation":21,"producing_mode":"RECOVERY"} and d["semantic_source_locks"]==locks
            p=d["partition"]; assert (int(p["primary_value"]),int(p["secondary_residue"]),int(p["fixed_x61_value"]))==key and p["coordinate_0based"]==60 and p["bound"]==[-20,20] and len(d["children"])==8
            claimed=d["canonical_sha256_without_this_field"]; body=dict(d); body.pop("canonical_sha256_without_this_field"); assert csha(body)==claimed
            cc=0
            for child in d["children"]:
                cb=dict(child); ch=cb.pop("canonical_sha256_without_this_field"); assert csha(cb)==ch
                rec={"primary_value":key[0],"secondary_residue":key[1],"fixed_x61_value":key[2],"x60_residue":int(child["x60_residue"]),"x60_interval":[int(v) for v in child["x60_interval"]]}
                if child["result"]["complete"]:
                    assert child["status"]=="COMPLETE_EXACT_X60_INTERVAL_ZERO_CREDIT" and child["solver"]["final_solver_result"]=="unsat" and child["solver"]["reason"] is None
                    assert child["result"]["integral_known140_nonnegative_solution_count"]==0 and child["result"]["primitive_known140_nonnegative_candidate_count"]==0 and child["result"]["primitive_known140_nonnegative_candidates"]==[]
                    complete.append(rec); cc+=1
                else:
                    assert child["status"]=="PARTIAL_UNKNOWN_NO_CREDIT" and child["solver"]["final_solver_result"]=="unknown" and child["solver"]["reason"]=="timeout"
                    lo,hi=rec["x60_interval"]; rec.update({"solver_result":"unknown","reason":"timeout","singleton_child_count":hi-lo+1}); incomplete.append(rec)
            assert cc==int(d["result"]["complete_child_count"]) and int(d["result"]["child_count"])==8 and d["result"]["complete"] is (cc==8) and all(v is False for v in d["credit_firewall"].values())
            fsha=hashlib.sha256(raw).hexdigest(); provenance.append({**key_to_dict(key),"artifact_id":int(row["artifact_id"]),"artifact_name":row["artifact_name"],"artifact_zip_digest_sha256":row["artifact_zip_digest_sha256"],"certificate_file_sha256":fsha,"canonical_sha256":claimed,"child_count":8,"complete_child_count":cc})
            certs.append({**key_to_dict(key),"certificate_file_sha256":fsha,"canonical_sha256":claimed,"base64":base64.b64encode(raw).decode("ascii")}); canon[f"{key[0]}:{key[1]}:{key[2]}"]=claimed
        ar=src["aggregate_artifact"]; az=td/"aggregate.zip"; fetch_zip(repo,ar["artifact_id"],az); assert hashlib.sha256(az.read_bytes()).hexdigest()==ar["artifact_zip_digest_sha256"]
        araw=one_json(az); ag=json.loads(araw); assert ag["schema"]==AGG_SCHEMA and ag["complete"] is False and ag["status"]=="PARTIAL_X60_INTERVAL_RECOVERY_NO_CREDIT"
        ac=ag["canonical_sha256_without_this_field"]; ab=dict(ag); ab.pop("canonical_sha256_without_this_field"); assert csha(ab)==ac
        assert ag["provenance"]["producing_execution_head"]==src["producing_execution_head"] and ag["provenance"]["semantic_source_locks"]==locks
        assert ag["packet_input_canonical_sha256"]==canon and ag["coverage"]["observed_packet_count"]==23 and ag["coverage"]["missing_packets"]==[] and len(ag["coverage"]["incomplete_packets"])==22
        aggregate={"artifact_id":int(ar["artifact_id"]),"artifact_name":ar["artifact_name"],"artifact_zip_digest_sha256":ar["artifact_zip_digest_sha256"],"certificate_file_sha256":hashlib.sha256(araw).hexdigest(),"canonical_sha256":ac,"base64":base64.b64encode(araw).decode("ascii")}
    provenance.sort(key=lambda r:(r["primary_value"],r["secondary_residue"],r["fixed_x61_value"])); certs.sort(key=lambda r:(r["primary_value"],r["secondary_residue"],r["fixed_x61_value"])); complete.sort(key=child_key); incomplete.sort(key=child_key)
    assert len(certs)==23 and len(complete)==122 and len(incomplete)==62 and sum(int(r["singleton_child_count"]) for r in incomplete)==311 and sum(1 for r in provenance if r["complete_child_count"]==8)==1
    payload={"schema":"STAGE32_MB104_000707_GEN21_X60_PACKET_CARRY_BUNDLE_V1","producing_generation":21,"producing_mode":"RECOVERY","producing_execution_head":src["producing_execution_head"],"producing_workflow_run_id":src["producing_workflow_run_id"],"source_locks":locks,"packet_count":23,"x60_interval_child_count":184,"complete_interval_child_count":122,"incomplete_interval_child_count":62,"next_x60_singleton_child_count":311,"complete_children":complete,"incomplete_children":incomplete,"certificates":certs,"aggregate_certificate":aggregate}
    raw=json.dumps(payload,sort_keys=True,separators=(",",":")).encode(); packed=gzip.compress(raw,mtime=0)
    env={"schema":"STAGE32_MB104_000707_GEN21_X60_DURABLE_PACKET_CARRY_ENVELOPE_V1","encoding":"gzip+base64","gzip_sha256":hashlib.sha256(packed).hexdigest(),"payload_sha256":hashlib.sha256(raw).hexdigest(),"byte_length":len(raw),"compressed_byte_length":len(packed),"base64":base64.b64encode(packed).decode("ascii"),"exact_bytes_not_regenerated":True}
    a.bundle.write_text(json.dumps(env,indent=2,sort_keys=True)+"\n")
    man=dict(src); man["schema"]="STAGE32_MB104_000707_GEN21_X60_PACKET_CARRY_MANIFEST_V1"; man["artifact_provenance"]=provenance; man["complete_children"]=complete; man["incomplete_children"]=incomplete; man["complete_interval_child_count"]=122; man["incomplete_interval_child_count"]=62; man["next_x60_singleton_child_count"]=311; man["aggregate_provenance"]={k:v for k,v in aggregate.items() if k!="base64"}; man["durable_bundle"]={"schema":env["schema"],"gzip_sha256":env["gzip_sha256"],"payload_sha256":env["payload_sha256"],"exact_bytes_not_regenerated":True}
    a.manifest.write_text(json.dumps(man,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"success":True,"packets":23,"interval_children":184,"complete_interval_children":122,"incomplete_interval_children":62,"next_x60_singleton_children":311,"payload_sha256":env["payload_sha256"],"gzip_sha256":env["gzip_sha256"]},sort_keys=True))
def key_to_dict(k): return {"primary_value":k[0],"secondary_residue":k[1],"fixed_x61_value":k[2]}
def child_key(r): return (r["primary_value"],r["secondary_residue"],r["fixed_x61_value"],r["x60_residue"])
if __name__=="__main__": main()
