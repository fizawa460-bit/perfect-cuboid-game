#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,subprocess
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_x61_packet as packet
import verify_mb104_000707_fibration_shell0_x61_packet as packetverify
import verify_mb104_000707_gen13_shard0_carry as oldcarry
import verify_mb104_000707_gen17_secondary_carry as gen17carry

HERE=Path(__file__).resolve().parent
RUNKEY=HERE/"runkeys"/"000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"

def fsha(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def gen13_identity(manifest:dict)->dict:
    a=manifest["artifact"]
    return {
        "certificate_file_sha256":a["certificate_file_sha256"],
        "certificate_canonical_sha256":a["certificate_canonical_sha256"],
        "artifact_id":int(a["id"]),
        "artifact_zip_digest_sha256":a["zip_digest_sha256"],
        "exact_bytes_not_regenerated":bool(a["retained_certificate_bundle"]["exact_bytes_not_regenerated"]),
    }

def gen15_zip_digest(r):
    v=r.get("zip_digest_sha256",r.get("zip_digest"))
    assert isinstance(v,str) and v
    return v.split(":",1)[1] if v.startswith("sha256:") else v

def gen15_identities(manifest:dict)->list[dict]:
    rows=[]
    for r in manifest["generation15_singleton_carry"]["artifact_provenance"]:
        rows.append({
            "value":int(r["value"]),
            "certificate_file_sha256":r["certificate_file_sha256"],
            "canonical_sha256":r["canonical"],
            "artifact_id":int(r["artifact_id"]),
            "artifact_zip_digest_sha256":gen15_zip_digest(r),
        })
    rows.sort(key=lambda r:r["value"])
    return rows

def gen17_identity(manifest_path:Path,bundle_path:Path,manifest:dict)->dict:
    rows=[]
    for r in manifest["artifact_provenance"]:
        rows.append({
            "primary_value":int(r["primary_value"]),
            "secondary_residue":int(r["secondary_residue"]),
            "certificate_file_sha256":r["certificate_file_sha256"],
            "canonical_sha256":r["canonical_sha256"],
            "artifact_id":int(r["artifact_id"]),
            "artifact_zip_digest_sha256":r["artifact_zip_digest_sha256"],
        })
    rows.sort(key=lambda r:(r["primary_value"],r["secondary_residue"]))
    return {
        "manifest_file_sha256":fsha(manifest_path),
        "bundle_file_sha256":fsha(bundle_path),
        "bundle_payload_sha256":manifest["durable_bundle"]["payload_sha256"],
        "bundle_gzip_sha256":manifest["durable_bundle"]["gzip_sha256"],
        "exact_bytes_not_regenerated":bool(manifest["durable_bundle"]["exact_bytes_not_regenerated"]),
        "complete_certificate_count":len(rows),
        "complete_certificate_identities":rows,
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input-dir",type=Path,required=True)
    ap.add_argument("--carry-certificate",type=Path,required=True)
    ap.add_argument("--carry-manifest",type=Path,required=True)
    ap.add_argument("--gen15-dir",type=Path,required=True)
    ap.add_argument("--gen17-manifest",type=Path,required=True)
    ap.add_argument("--gen17-bundle",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    old_manifest=json.loads(a.carry_manifest.read_text(encoding="utf-8"))
    gen13,gen15=oldcarry.validate_all(a.carry_certificate,a.carry_manifest,a.gen15_dir)
    m17,p17,c17=gen17carry.decode_bundle(a.gen17_manifest,a.gen17_bundle)
    expected={tuple(map(int,x)) for x in m17["incomplete_cells"]}; observed={}
    for path in sorted(a.input_dir.glob("*.json")):
        try:d=json.loads(path.read_text())
        except Exception:continue
        if d.get("schema")!=packet.SCHEMA:continue
        key=(int(d["partition"]["primary_value"]),int(d["partition"]["secondary_residue"]))
        assert key in expected and key not in observed
        observed[key]=packetverify.validate_certificate(path,*key)
    missing=sorted(expected-set(observed))
    incomplete=sorted(k for k,d in observed.items() if not d["result"]["complete"])
    complete=not missing and not incomplete and len(observed)==len(expected)==29
    candidates=[]; sx=set(); sf=set()
    for d in observed.values():
        for rec in d["result"]["primitive_known140_nonnegative_candidates"]:
            xk=tuple(rec["x_hperp_coordinates"]); fk=tuple(rec["picard_basis_coordinates"])
            assert xk not in sx and fk not in sf
            sx.add(xk); sf.add(fk); candidates.append(rec)
    candidates.sort(key=lambda r:tuple(r["picard_basis_coordinates"]))
    total_models=None
    if complete:
        total_models=int(gen13["result"]["integral_known140_nonnegative_solution_count"])+sum(int(d["result"]["integral_known140_nonnegative_solution_count"]) for d in gen15.values())+sum(int(d["result"]["integral_known140_nonnegative_solution_count"]) for d in c17.values())+sum(int(d["result"]["integral_known140_nonnegative_solution_count"]) for d in observed.values())
    k=json.loads(RUNKEY.read_text())
    execution_head=subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()
    assert len(execution_head)==40
    semantic_locks=packet.semantic_source_locks()
    out={
      "schema":"STAGE32_MB104_000707_FIBRATION_SHELL0_X61_PACKET_AGGREGATE_V2",
      "status":"COMPLETE_EXACT_SHELL0_ENUMERATION_ZERO_CREDIT" if complete else "PARTIAL_X61_PACKET_RECOVERY_NO_CREDIT",
      "complete":complete,
      "provenance":{
        "aggregate_generation":int(k["generation"]),
        "aggregate_mode":k["mode"],
        "producing_execution_head":execution_head,
        "semantic_source_locks":semantic_locks,
        "gen13_carry":gen13_identity(old_manifest),
        "gen15_carry_identities":gen15_identities(old_manifest),
        "gen17_carry":gen17_identity(a.gen17_manifest,a.gen17_bundle,m17),
        "gen17_execution_head":m17["producing_execution_head"],
        "gen17_workflow_run_id":m17["producing_workflow_run_id"],
      },
      "coverage":{
        "gen13_carried_interval":[-20,-16],
        "gen15_complete_values":sorted(gen15),
        "gen17_complete_secondary_cells":[list(x) for x in sorted(c17)],
        "refined_parent_cells":[list(x) for x in sorted(expected)],
        "expected_packet_count":29,
        "expected_singleton_child_count":146,
        "observed_packet_count":len(observed),
        "missing_packets":[list(x) for x in missing],
        "incomplete_packets":[list(x) for x in incomplete],
        "full_primary_union":[-20,20],
        "refinement_is_exact_disjoint":True,
      },
      "packet_input_canonical_sha256":{f"{p}:{s}":d["canonical_sha256_without_this_field"] for (p,s),d in sorted(observed.items())},
      "result":{
        "integral_known140_nonnegative_solution_count":total_models,
        "primitive_candidate_count":len(candidates) if complete else None,
        "primitive_candidates":candidates if complete else [],
      },
      "credit_firewall":{
        "numerical_fibration_shell_credit":False,"effectivity_credit":False,"semiampleness_credit":False,
        "global_fibration_optimum_credit":False,"MB104_complete":False,"receiver_credit":False,
        "theorem_credit":False,"endpoint_credit":False,"merge_authorized":False,
      },
    }
    out["canonical_sha256_without_this_field"]=parent.csha(out)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"complete":complete,"observed_packets":len(observed),"missing_packets":len(missing),"incomplete_packets":len(incomplete),"producing_execution_head":execution_head,"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))
    raise SystemExit(0 if complete else 2)
if __name__=="__main__": main()
