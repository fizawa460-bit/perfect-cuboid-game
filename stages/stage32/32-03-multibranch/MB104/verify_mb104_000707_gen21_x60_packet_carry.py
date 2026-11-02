#!/usr/bin/env python3
from __future__ import annotations
import argparse,base64,gzip,hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
MANIFEST=HERE/"MB104-000707-GEN21-X60-PACKET-CARRY-MANIFEST.json"; BUNDLE=HERE/"MB104-000707-GEN21-X60-PACKET-CARRY-BUNDLE.json"
PACKET_SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_X60_INTERVAL_PACKET_V1"; AGG_SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_X60_INTERVAL_AGGREGATE_V1"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def ck(r): return (int(r["primary_value"]),int(r["secondary_residue"]),int(r["fixed_x61_value"]),int(r["x60_residue"]))
def decode_bundle(manifest_path=MANIFEST,bundle_path=BUNDLE,out_dir=None):
    m=json.loads(Path(manifest_path).read_text()); e=json.loads(Path(bundle_path).read_text()); assert m["schema"]=="STAGE32_MB104_000707_GEN21_X60_PACKET_CARRY_MANIFEST_V1" and e["schema"]=="STAGE32_MB104_000707_GEN21_X60_DURABLE_PACKET_CARRY_ENVELOPE_V1" and e["encoding"]=="gzip+base64" and e["exact_bytes_not_regenerated"] is True
    packed=base64.b64decode(e["base64"],validate=True); assert hashlib.sha256(packed).hexdigest()==e["gzip_sha256"]==m["durable_bundle"]["gzip_sha256"]; raw=gzip.decompress(packed); assert len(raw)==int(e["byte_length"]) and hashlib.sha256(raw).hexdigest()==e["payload_sha256"]==m["durable_bundle"]["payload_sha256"]; p=json.loads(raw)
    assert p["schema"]=="STAGE32_MB104_000707_GEN21_X60_PACKET_CARRY_BUNDLE_V1" and p["producing_generation"]==m["producing_generation"]==21 and p["producing_mode"]==m["producing_mode"]=="RECOVERY" and p["producing_execution_head"]==m["producing_execution_head"]=="7166da4f293ab608ff200ddcef222e1c21fc6014" and p["producing_workflow_run_id"]==m["producing_workflow_run_id"]==35586170075
    assert p["source_locks"]==m["producing_semantic_source_locks"] and int(p["packet_count"])==23 and int(p["x60_interval_child_count"])==184 and int(p["complete_interval_child_count"])==122 and int(p["incomplete_interval_child_count"])==62 and int(p["next_x60_singleton_child_count"])==311
    assert p["complete_children"]==m["complete_children"] and p["incomplete_children"]==m["incomplete_children"] and len(p["certificates"])==23
    prov={(int(r["primary_value"]),int(r["secondary_residue"]),int(r["fixed_x61_value"])):r for r in m["artifact_provenance"]}; assert len(prov)==23
    complete=[]; incomplete=[]; canon={}; certs={}
    for rec in p["certificates"]:
        key=(int(rec["primary_value"]),int(rec["secondary_residue"]),int(rec["fixed_x61_value"])); assert key in prov and key not in certs; pr=prov[key]
        rawc=base64.b64decode(rec["base64"],validate=True); assert hashlib.sha256(rawc).hexdigest()==rec["certificate_file_sha256"]==pr["certificate_file_sha256"]; d=json.loads(rawc); assert d["schema"]==PACKET_SCHEMA and d["provenance"]=={"producing_generation":21,"producing_mode":"RECOVERY"} and d["semantic_source_locks"]==p["source_locks"]
        part=d["partition"]; assert (int(part["primary_value"]),int(part["secondary_residue"]),int(part["fixed_x61_value"]))==key and part["coordinate_0based"]==60 and part["bound"]==[-20,20] and len(d["children"])==8
        cl=d["canonical_sha256_without_this_field"]; b=dict(d); b.pop("canonical_sha256_without_this_field"); assert csha(b)==cl==rec["canonical_sha256"]==pr["canonical_sha256"]; canon[f"{key[0]}:{key[1]}:{key[2]}"]=cl; cc=0
        for child in d["children"]:
            cb=dict(child); ch=cb.pop("canonical_sha256_without_this_field"); assert csha(cb)==ch
            row={"primary_value":key[0],"secondary_residue":key[1],"fixed_x61_value":key[2],"x60_residue":int(child["x60_residue"]),"x60_interval":[int(v) for v in child["x60_interval"]]}
            if child["result"]["complete"]:
                assert child["status"]=="COMPLETE_EXACT_X60_INTERVAL_ZERO_CREDIT" and child["solver"]["final_solver_result"]=="unsat" and child["solver"]["reason"] is None and child["result"]["integral_known140_nonnegative_solution_count"]==0 and child["result"]["primitive_known140_nonnegative_candidate_count"]==0 and child["result"]["primitive_known140_nonnegative_candidates"]==[]; complete.append(row); cc+=1
            else:
                assert child["status"]=="PARTIAL_UNKNOWN_NO_CREDIT" and child["solver"]["final_solver_result"]=="unknown" and child["solver"]["reason"]=="timeout"; lo,hi=row["x60_interval"]; row.update({"solver_result":"unknown","reason":"timeout","singleton_child_count":hi-lo+1}); incomplete.append(row)
        assert cc==int(d["result"]["complete_child_count"])==int(pr["complete_child_count"]) and d["result"]["complete"] is (cc==8) and all(v is False for v in d["credit_firewall"].values()); certs[key]=d
        if out_dir is not None: out=Path(out_dir); out.mkdir(parents=True,exist_ok=True); (out/f"{key[0]}-{key[1]}-{key[2]}.json").write_bytes(rawc)
    complete.sort(key=ck); incomplete.sort(key=ck); assert complete==m["complete_children"] and len(complete)==122 and incomplete==m["incomplete_children"] and len(incomplete)==62 and sum(int(r["singleton_child_count"]) for r in incomplete)==311
    ar=p["aggregate_certificate"]; araw=base64.b64decode(ar["base64"],validate=True); assert hashlib.sha256(araw).hexdigest()==ar["certificate_file_sha256"]==m["aggregate_provenance"]["certificate_file_sha256"]; ag=json.loads(araw); assert ag["schema"]==AGG_SCHEMA and ag["complete"] is False and ag["status"]=="PARTIAL_X60_INTERVAL_RECOVERY_NO_CREDIT"; ac=ag["canonical_sha256_without_this_field"]; ab=dict(ag); ab.pop("canonical_sha256_without_this_field"); assert csha(ab)==ac==ar["canonical_sha256"]==m["aggregate_provenance"]["canonical_sha256"] and ag["packet_input_canonical_sha256"]==canon and ag["coverage"]["observed_packet_count"]==23 and ag["coverage"]["missing_packets"]==[] and len(ag["coverage"]["incomplete_packets"])==22
    assert all(v is False for v in m["credit_firewall"].values()); return m,p,certs
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--manifest",type=Path,default=MANIFEST); ap.add_argument("--bundle",type=Path,default=BUNDLE); ap.add_argument("--out-dir",type=Path); a=ap.parse_args(); m,p,c=decode_bundle(a.manifest,a.bundle,a.out_dir); print(json.dumps({"success":True,"packet_count":len(c),"complete_interval_children":m["complete_interval_child_count"],"incomplete_interval_children":m["incomplete_interval_child_count"],"next_x60_singleton_children":m["next_x60_singleton_child_count"],"payload_sha256":m["durable_bundle"]["payload_sha256"]},sort_keys=True))
if __name__=="__main__": main()
