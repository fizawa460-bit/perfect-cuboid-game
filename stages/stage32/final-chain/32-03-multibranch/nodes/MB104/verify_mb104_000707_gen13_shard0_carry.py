#!/usr/bin/env python3
from __future__ import annotations
import argparse, base64, gzip, hashlib, json
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as engine
GEN15_SCHEMA="STAGE32_MB104_000707_GEN15_COMPLETE_SINGLETON_CARRY_BUNDLE_V1"
GEN15_CERT_SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_RECOVERY_SINGLETON_V1"

def validate_gen15_artifact_dir(manifest:dict, artifact_dir:Path)->dict[int,dict]:
    g=manifest["generation15_singleton_carry"]
    expected=[int(v) for v in g["complete_values"]]
    assert [int(v) for v in g["unknown_values"]]==[-14,-12,-8,0,4,8,12]
    provenance={int(r["value"]):r for r in g["artifact_provenance"]}
    assert sorted(provenance)==expected and len(provenance)==int(g["complete_count"])==29
    locks=g["producing_semantic_source_locks"]; out={}
    for value in expected:
        raw=(artifact_dir/f"{value}.json").read_bytes(); rec=provenance[value]
        # The recorded ZIP digest fixes the immutable Actions artifact.  The
        # rehydrated file digest is checked and retained in the returned
        # certificate record; Gen15 did not record a separate file digest.
        file_sha256=hashlib.sha256(raw).hexdigest(); assert file_sha256==rec["certificate_file_sha256"]
        cert=json.loads(raw); assert cert["schema"]==GEN15_CERT_SCHEMA
        claimed=cert["canonical_sha256_without_this_field"]; body=dict(cert); body.pop("canonical_sha256_without_this_field")
        assert engine.csha(body)==claimed==rec["canonical"]
        assert cert["provenance"]=={"producing_generation":15,"producing_mode":"RECOVERY"}
        assert cert["semantic_source_locks"]==locks
        assert cert["partition"]["workunit_value"]==value and cert["partition"]["workunit_interval"]==[value,value]
        assert cert["partition"]["split_coordinate_0based"]==62
        assert cert["status"]=="COMPLETE_EXACT_RECOVERY_WORKUNIT_ZERO_CREDIT"
        assert cert["result"]["complete"] is True and cert["solver"]["final_solver_result"]=="unsat" and cert["solver"]["reason"] is None
        assert cert["result"]["integral_known140_nonnegative_solution_count"]==0
        assert cert["result"]["primitive_known140_nonnegative_candidate_count"]==0 and cert["result"]["primitive_known140_nonnegative_candidates"]==[]
        assert all(v is False for v in cert["credit_firewall"].values())
        cert["_rehydrated_certificate_file_sha256"]=file_sha256
        out[value]=cert
    assert g["credit"] is False
    return out

def validate_gen13(certificate:Path,manifest:dict)->dict:
    raw=certificate.read_bytes(); cert=json.loads(raw); bundle=manifest["artifact"]["retained_certificate_bundle"]
    retained=base64.b64decode(bundle["base64"],validate=True)
    assert len(retained)==int(bundle["byte_length"])==6289 and raw==retained
    assert hashlib.sha256(raw).hexdigest()==manifest["artifact"]["certificate_file_sha256"]
    claimed=cert["canonical_sha256_without_this_field"]; body=dict(cert); body.pop("canonical_sha256_without_this_field")
    assert engine.csha(body)==claimed==manifest["artifact"]["certificate_canonical_sha256"]
    wu=manifest["workunit"]; contract=engine.split_contract(0,8)
    assert cert["partition"]["shard_residue"]==wu["shard_residue"]==0 and contract["intervals"][0]==wu["shard_interval"]==[-20,-16]
    assert cert["source_locks"]==manifest["source_locks"] and cert["source_locks"]["execution_surface_generation"]==13
    assert cert["status"]=="COMPLETE_EXACT_SHARD_ZERO_CREDIT" and cert["result"]["complete"] is True
    assert cert["solver"]["final_solver_result"]=="unsat" and cert["result"]["primitive_known140_nonnegative_candidates"]==[]
    assert all(v is False for v in cert["credit_firewall"].values()) and all(v is False for v in manifest["credit_firewall"].values())
    return cert

def validate_all(certificate:Path,manifest_path:Path,gen15_dir:Path):
    manifest=json.loads(manifest_path.read_text(encoding="utf-8"))
    return validate_gen13(certificate,manifest),validate_gen15_artifact_dir(manifest,gen15_dir)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--certificate",type=Path,required=True); ap.add_argument("--manifest",type=Path,required=True); ap.add_argument("--gen15-dir",type=Path,required=True); args=ap.parse_args()
    g13,g15=validate_all(args.certificate,args.manifest,args.gen15_dir)
    print(json.dumps({"success":True,"gen13_carried_interval":[-20,-16],"gen13_canonical":g13["canonical_sha256_without_this_field"],"gen15_complete_count":len(g15),"gen15_complete_values":sorted(g15),"gen15_unknown_values":[-14,-12,-8,0,4,8,12]},sort_keys=True))
if __name__=="__main__": main()
