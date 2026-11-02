#!/usr/bin/env python3
from __future__ import annotations
import argparse,base64,gzip,hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
MANIFEST=HERE/"MB104-000707-GEN19-X61-PACKET-CARRY-MANIFEST.json"; BUNDLE=HERE/"MB104-000707-GEN19-X61-PACKET-CARRY-BUNDLE.json"; CERT_SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_X61_SINGLETON_PACKET_V1"
def csha(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def decode_bundle(manifest_path=MANIFEST,bundle_path=BUNDLE,out_dir=None):
    m=json.loads(Path(manifest_path).read_text()); e=json.loads(Path(bundle_path).read_text()); assert m["schema"]=="STAGE32_MB104_000707_GEN19_X61_PACKET_CARRY_MANIFEST_V1"; assert e["schema"]=="STAGE32_MB104_000707_GEN19_X61_DURABLE_PACKET_CARRY_ENVELOPE_V1" and e["encoding"]=="gzip+base64" and e["exact_bytes_not_regenerated"] is True
    packed=base64.b64decode(e["base64"],validate=True); assert hashlib.sha256(packed).hexdigest()==e["gzip_sha256"]==m["durable_bundle"]["gzip_sha256"]; raw=gzip.decompress(packed); assert len(raw)==int(e["byte_length"]) and hashlib.sha256(raw).hexdigest()==e["payload_sha256"]==m["durable_bundle"]["payload_sha256"]; p=json.loads(raw)
    assert p["schema"]=="STAGE32_MB104_000707_GEN19_X61_PACKET_CARRY_BUNDLE_V1" and p["producing_generation"]==m["producing_generation"]==19 and p["producing_mode"]==m["producing_mode"]=="RECOVERY" and p["producing_execution_head"]==m["producing_execution_head"]=="bc1f055cfcfa9a5249244a2d50ff13e20b9d9fb1" and p["producing_workflow_run_id"]==m["producing_workflow_run_id"]==35568958576
    assert p["source_locks"]==m["producing_semantic_source_locks"] and int(p["packet_count"])==int(m["packet_count"])==29 and int(p["singleton_child_count"])==int(m["singleton_child_count"])==146 and int(p["complete_child_count"])==int(m["complete_child_count"])==123 and int(p["incomplete_child_count"])==int(m["incomplete_child_count"])==23 and p["complete_children"]==m["complete_children"] and p["incomplete_children"]==m["incomplete_children"]
    provenance={(int(r["primary_value"]),int(r["secondary_residue"])):r for r in m["artifact_provenance"]}; assert len(provenance)==29; certs={}; complete=[]; incomplete=[]
    for rec in p["certificates"]:
        key=(int(rec["primary_value"]),int(rec["secondary_residue"])); assert key in provenance and key not in certs; pr=provenance[key]; cert_raw=base64.b64decode(rec["base64"],validate=True); assert hashlib.sha256(cert_raw).hexdigest()==rec["certificate_file_sha256"]==pr["certificate_file_sha256"]; cert=json.loads(cert_raw)
        assert cert["schema"]==CERT_SCHEMA and cert["provenance"]=={"producing_generation":19,"producing_mode":"RECOVERY"} and cert["semantic_source_locks"]==p["source_locks"] and int(cert["partition"]["primary_value"])==key[0] and int(cert["partition"]["secondary_residue"])==key[1]
        claimed=cert["canonical_sha256_without_this_field"]; body=dict(cert); body.pop("canonical_sha256_without_this_field"); assert csha(body)==claimed==rec["canonical_sha256"]==pr["canonical_sha256"]; cc=0
        for child in cert["children"]:
            row={"primary_value":key[0],"secondary_residue":key[1],"fixed_x61_value":int(child["fixed_x61_value"])}
            if child["result"]["complete"]:
                assert child["status"]=="COMPLETE_EXACT_X61_SINGLETON_ZERO_CREDIT" and child["solver"]["final_solver_result"]=="unsat" and child["solver"]["reason"] is None and child["result"]["integral_known140_nonnegative_solution_count"]==0 and child["result"]["primitive_known140_nonnegative_candidate_count"]==0 and child["result"]["primitive_known140_nonnegative_candidates"]==[]; complete.append(row); cc+=1
            else:
                assert child["status"]=="PARTIAL_UNKNOWN_NO_CREDIT" and child["solver"]["final_solver_result"]=="unknown" and child["solver"]["reason"]=="timeout"; row.update({"solver_result":"unknown","reason":"timeout"}); incomplete.append(row)
        assert cc==int(cert["result"]["complete_child_count"])==int(pr["complete_child_count"]) and len(cert["children"])==int(pr["child_count"]) and cert["result"]["complete"] is (cc==len(cert["children"])) and all(v is False for v in cert["credit_firewall"].values()); certs[key]=cert
        if out_dir is not None: out=Path(out_dir); out.mkdir(parents=True,exist_ok=True); (out/f"{key[0]}-{key[1]}.json").write_bytes(cert_raw)
    complete.sort(key=lambda r:(r["primary_value"],r["secondary_residue"],r["fixed_x61_value"])); incomplete.sort(key=lambda r:(r["primary_value"],r["secondary_residue"],r["fixed_x61_value"])); assert complete==m["complete_children"] and len(complete)==123 and incomplete==m["incomplete_children"] and len(incomplete)==23 and len(certs)==29 and all(v is False for v in m["credit_firewall"].values()); return m,p,certs
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--manifest",type=Path,default=MANIFEST); ap.add_argument("--bundle",type=Path,default=BUNDLE); ap.add_argument("--out-dir",type=Path); a=ap.parse_args(); m,p,c=decode_bundle(a.manifest,a.bundle,a.out_dir); print(json.dumps({"success":True,"packet_count":len(c),"complete_children":m["complete_child_count"],"incomplete_children":m["incomplete_child_count"],"payload_sha256":m["durable_bundle"]["payload_sha256"]},sort_keys=True))
if __name__=="__main__": main()
