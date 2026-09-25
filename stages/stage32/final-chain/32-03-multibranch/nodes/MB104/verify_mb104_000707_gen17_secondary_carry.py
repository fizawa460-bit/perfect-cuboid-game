#!/usr/bin/env python3
from __future__ import annotations
import base64,gzip,hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
MANIFEST=HERE/"MB104-000707-GEN17-SECONDARY-CARRY-MANIFEST.json"
BUNDLE=HERE/"MB104-000707-GEN17-SECONDARY-CARRY-BUNDLE.json"
CERT_SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_RESIDUAL_SECONDARY_V2"
CERT_STATUS="COMPLETE_EXACT_SECONDARY_RECOVERY_ZERO_CREDIT"

def csha(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def decode_bundle(manifest_path=MANIFEST,bundle_path=BUNDLE,out_dir=None):
    m=json.loads(Path(manifest_path).read_text())
    e=json.loads(Path(bundle_path).read_text())
    assert m["schema"]=="STAGE32_MB104_000707_GEN17_SECONDARY_CARRY_MANIFEST_V1"
    assert e["schema"]=="STAGE32_MB104_000707_GEN17_DURABLE_SECONDARY_CARRY_ENVELOPE_V1"
    assert e["encoding"]=="gzip+base64" and e["exact_bytes_not_regenerated"] is True
    packed=base64.b64decode(e["base64"],validate=True)
    assert hashlib.sha256(packed).hexdigest()==e["gzip_sha256"]==m["durable_bundle"]["gzip_sha256"]
    raw=gzip.decompress(packed)
    assert len(raw)==int(e["byte_length"])
    assert hashlib.sha256(raw).hexdigest()==e["payload_sha256"]==m["durable_bundle"]["payload_sha256"]
    p=json.loads(raw)
    assert p["schema"]=="STAGE32_MB104_000707_GEN17_COMPLETE_SECONDARY_CARRY_BUNDLE_V1"
    assert p["producing_generation"]==m["producing_generation"]==17
    assert p["producing_mode"]==m["producing_mode"]=="RECOVERY"
    assert p["producing_execution_head"]==m["producing_execution_head"]=="4d4f48f4f69e27731444117bc83a9c9ab7d51c50"
    assert p["producing_workflow_run_id"]==m["producing_workflow_run_id"]==35548407737
    assert p["source_locks"]==m["producing_semantic_source_locks"]
    assert int(p["complete_count"])==int(m["complete_count"])==27
    assert p["incomplete_cells"]==m["incomplete_cells"] and len(p["incomplete_cells"])==29
    provenance={(int(r["primary_value"]),int(r["secondary_residue"])):r for r in m["artifact_provenance"]}
    assert len(provenance)==27
    certs={}
    for rec in p["certificates"]:
        key=(int(rec["primary_value"]),int(rec["secondary_residue"]))
        assert key in provenance and key not in certs
        pr=provenance[key]
        cert_raw=base64.b64decode(rec["base64"],validate=True)
        assert hashlib.sha256(cert_raw).hexdigest()==rec["certificate_file_sha256"]==pr["certificate_file_sha256"]
        cert=json.loads(cert_raw)
        assert cert["schema"]==CERT_SCHEMA and cert["status"]==CERT_STATUS
        assert cert["provenance"]=={"producing_generation":17,"producing_mode":"RECOVERY"}
        assert cert["semantic_source_locks"]==p["source_locks"]
        assert cert["partition"]["primary_value"]==key[0] and cert["partition"]["secondary_residue"]==key[1]
        assert cert["partition"]["secondary_interval"]==rec["secondary_interval"]==pr["secondary_interval"]
        assert cert["partition"]["secondary_coordinate_0based"]==61
        assert cert["result"]["complete"] is True and cert["solver"]["final_solver_result"]=="unsat" and cert["solver"]["reason"] is None
        assert cert["result"]["integral_known140_nonnegative_solution_count"]==0
        assert cert["result"]["primitive_known140_nonnegative_candidate_count"]==0 and cert["result"]["primitive_known140_nonnegative_candidates"]==[]
        assert all(v is False for v in cert["credit_firewall"].values())
        claimed=cert["canonical_sha256_without_this_field"]; body=dict(cert); body.pop("canonical_sha256_without_this_field")
        assert csha(body)==claimed==rec["canonical_sha256"]==pr["canonical_sha256"]
        certs[key]=cert
        if out_dir is not None:
            out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
            (out/f"{key[0]}-{key[1]}.json").write_bytes(cert_raw)
    assert len(certs)==27
    assert sorted([list(k) for k in certs])==sorted(p["complete_cells"])
    allcells={(x,s) for x in [-14,-12,-8,0,4,8,12] for s in range(8)}
    assert sorted([list(k) for k in allcells-set(certs)])==m["incomplete_cells"]
    assert all(v is False for v in m["credit_firewall"].values())
    return m,p,certs

def main():
    m,p,c=decode_bundle()
    print(json.dumps({"success":True,"complete_count":len(c),"incomplete_count":len(m["incomplete_cells"]),"payload_sha256":m["durable_bundle"]["payload_sha256"]},sort_keys=True))

if __name__=="__main__":
    main()
